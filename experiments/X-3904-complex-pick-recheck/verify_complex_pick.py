#!/usr/bin/env python3
"""Independent exact checker for complex Pick directions and whole-matrix PD.

The checker evaluates no transcendental function. It intersects two supplied
outward rectangles for each F(s)=xi'(s)/xi(s) value, then uses only Python
integers and fractions.Fraction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.xi-complex-pick-balls.v1"
VERIFY_SCHEMA = "riemann.xi-complex-pick-balls.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def parse_binary(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    mantissa = parse_int(value.get("mantissa"), f"{name}.mantissa")
    exponent = parse_int(value.get("exponent"), f"{name}.exponent")
    if exponent >= 0:
        return Fraction(mantissa << exponent, 1)
    return Fraction(mantissa, 1 << (-exponent))


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise CertificateError("invalid interval")

    @classmethod
    def parse(cls, value: Any, name: str) -> "Interval":
        if not isinstance(value, dict):
            raise CertificateError(f"{name} must be an object")

        def endpoint(raw: Any, endpoint_name: str) -> Fraction:
            if not isinstance(raw, dict):
                raise CertificateError(f"{endpoint_name} must be an object")
            if "mantissa" in raw or "exponent" in raw:
                return parse_binary(raw, endpoint_name)
            return parse_fraction(raw, endpoint_name)

        return cls(
            endpoint(value.get("lower"), f"{name}.lower"),
            endpoint(value.get("upper"), f"{name}.upper"),
        )

    def intersect(self, other: "Interval") -> "Interval":
        lo = max(self.lo, other.lo)
        hi = min(self.hi, other.hi)
        if lo > hi:
            raise CertificateError("the two primitive assemblies are disjoint")
        return Interval(lo, hi)

    def scale(self, coefficient: Fraction) -> "Interval":
        if coefficient >= 0:
            return Interval(coefficient * self.lo, coefficient * self.hi)
        return Interval(coefficient * self.hi, coefficient * self.lo)

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def to_json(self) -> dict[str, object]:
        return {"lower": fraction_json(self.lo), "upper": fraction_json(self.hi)}


@dataclass(frozen=True)
class Rectangle:
    real: Interval
    imag: Interval

    @classmethod
    def parse(cls, value: Any, name: str) -> "Rectangle":
        if not isinstance(value, dict):
            raise CertificateError(f"{name} must be an object")
        return cls(
            Interval.parse(value.get("real"), f"{name}.real"),
            Interval.parse(value.get("imag"), f"{name}.imag"),
        )

    def intersect(self, other: "Rectangle") -> "Rectangle":
        return Rectangle(self.real.intersect(other.real), self.imag.intersect(other.imag))

    def to_json(self) -> dict[str, object]:
        return {"real": self.real.to_json(), "imag": self.imag.to_json()}


@dataclass(frozen=True)
class Gaussian:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        value = gaussian(other)
        return Gaussian(self.real + value.real, self.imag + value.imag)

    __radd__ = __add__

    def __sub__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        value = gaussian(other)
        return Gaussian(self.real - value.real, self.imag - value.imag)

    def __rsub__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        return gaussian(other) - self

    def __neg__(self) -> "Gaussian":
        return Gaussian(-self.real, -self.imag)

    def __mul__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        value = gaussian(other)
        return Gaussian(
            self.real * value.real - self.imag * value.imag,
            self.real * value.imag + self.imag * value.real,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        value = gaussian(other)
        denominator = value.real * value.real + value.imag * value.imag
        if denominator == 0:
            raise ZeroDivisionError
        return Gaussian(
            (self.real * value.real + self.imag * value.imag) / denominator,
            (self.imag * value.real - self.real * value.imag) / denominator,
        )

    def conjugate(self) -> "Gaussian":
        return Gaussian(self.real, -self.imag)

    def abs_squared(self) -> Fraction:
        return self.real * self.real + self.imag * self.imag

    def to_json(self) -> dict[str, object]:
        return {"real": fraction_json(self.real), "imag": fraction_json(self.imag)}


def gaussian(value: Gaussian | Fraction | int) -> Gaussian:
    return value if isinstance(value, Gaussian) else Gaussian(Fraction(value), Fraction(0))


def parse_gaussian(value: Any, name: str) -> Gaussian:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    return Gaussian(
        parse_fraction(value.get("real"), f"{name}.real"),
        parse_fraction(value.get("imag"), f"{name}.imag"),
    )


@dataclass(frozen=True)
class Point:
    identifier: str
    x: Fraction
    t: Fraction
    f: Rectangle


def parse_point(value: Any, index: int) -> Point:
    name = f"points[{index}]"
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    identifier = value.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise CertificateError(f"{name}.id must be a nonempty string")
    x = parse_fraction(value.get("x"), f"{name}.x")
    t = parse_fraction(value.get("t"), f"{name}.t")
    if x <= 0:
        raise CertificateError(f"{name} is not in Re(s)>1/2")
    first = Rectangle.parse(value.get("f_via_xi"), f"{name}.f_via_xi")
    second = Rectangle.parse(value.get("f_via_parts"), f"{name}.f_via_parts")
    f = first.intersect(second)
    lower = parse_binary(value.get("zeta_abs_lower"), f"{name}.zeta_abs_lower")
    if lower <= 0:
        raise CertificateError(f"{name} has a denominator ball touching zero")
    return Point(identifier, x, t, f)


def require_points(raw_ids: Any, points: dict[str, Point], name: str) -> list[Point]:
    if not isinstance(raw_ids, list) or not raw_ids:
        raise CertificateError(f"{name}.points must be a nonempty array")
    selected: list[Point] = []
    for index, identifier in enumerate(raw_ids):
        if not isinstance(identifier, str) or identifier not in points:
            raise CertificateError(f"{name}.points[{index}] is unknown")
        selected.append(points[identifier])
    if len(set(raw_ids)) != len(raw_ids):
        raise CertificateError(f"{name}.points contains duplicates")
    if any(point.t != selected[0].t for point in selected[1:]):
        raise CertificateError(f"{name} mixes ordinates")
    return selected


def sum_scaled(terms: list[tuple[Fraction, Interval]]) -> Interval:
    total = Interval(Fraction(0), Fraction(0))
    for coefficient, interval in terms:
        total = total.add(interval.scale(coefficient))
    return total


def complex_pick_check(check: dict[str, Any], points: dict[str, Point], name: str) -> dict[str, object]:
    selected = require_points(check.get("points"), points, name)
    raw_vector = check.get("vector")
    if not isinstance(raw_vector, list) or len(raw_vector) != len(selected):
        raise CertificateError(f"{name}.vector has the wrong length")
    vector = [parse_gaussian(value, f"{name}.vector[{i}]") for i, value in enumerate(raw_vector)]
    norm_squared = sum(value.abs_squared() for value in vector)
    if norm_squared <= 0:
        raise CertificateError(f"{name}.vector is zero")

    alphas: list[Gaussian] = []
    terms: list[tuple[Fraction, Interval]] = []
    for j, point in enumerate(selected):
        inner = Gaussian()
        for k, other in enumerate(selected):
            inner += vector[k] / (point.x + other.x)
        alpha = vector[j].conjugate() * inner
        alphas.append(alpha)
        terms.append((2 * alpha.real, point.f.real))
        terms.append((-2 * alpha.imag, point.f.imag))

    raw_interval = sum_scaled(terms)
    normalized = Interval(raw_interval.lo / norm_squared, raw_interval.hi / norm_squared)
    if normalized.hi < 0:
        status = "CERTIFIED_NEGATIVE"
    elif normalized.lo >= 0:
        status = "CERTIFIED_NONNEGATIVE"
    else:
        status = "UNRESOLVED_ZERO_TOUCH"
    return {
        "id": check.get("id"),
        "kind": "complex-pick-rayleigh",
        "status": status,
        "normalized_interval": normalized.to_json(),
        "raw_interval": raw_interval.to_json(),
        "norm_squared": fraction_json(norm_squared),
        "alphas": [value.to_json() for value in alphas],
        "points": [point.identifier for point in selected],
        "vector": [value.to_json() for value in vector],
    }


def midpoint(point: Point) -> Gaussian:
    return Gaussian(
        (point.f.real.lo + point.f.real.hi) / 2,
        (point.f.imag.lo + point.f.imag.hi) / 2,
    )


def ldl_pivots(matrix: list[list[Gaussian]], delta: Fraction) -> list[Fraction]:
    size = len(matrix)
    lower = [[Gaussian() for _ in range(size)] for _ in range(size)]
    diagonal: list[Fraction] = []
    for i in range(size):
        lower[i][i] = Gaussian(Fraction(1), Fraction(0))
    for k in range(size):
        if matrix[k][k].imag != 0:
            raise CertificateError("midpoint matrix diagonal is not real")
        pivot = matrix[k][k].real - delta
        for j in range(k):
            pivot -= lower[k][j].abs_squared() * diagonal[j]
        diagonal.append(pivot)
        if pivot <= 0:
            return diagonal
        for i in range(k + 1, size):
            value = matrix[i][k]
            for j in range(k):
                value -= lower[i][j] * lower[k][j].conjugate() * diagonal[j]
            lower[i][k] = value / pivot
    return diagonal


def whole_matrix_check(check: dict[str, Any], points: dict[str, Point], name: str) -> dict[str, object]:
    selected = require_points(check.get("points"), points, name)
    delta = parse_fraction(check.get("delta"), f"{name}.delta")
    if delta <= 0:
        raise CertificateError(f"{name}.delta must be positive")
    size = len(selected)
    values = [midpoint(point) for point in selected]
    matrix = [
        [
            (values[i] + values[j].conjugate()) / (selected[i].x + selected[j].x)
            for j in range(size)
        ]
        for i in range(size)
    ]
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != matrix[j][i].conjugate():
                raise CertificateError("midpoint Pick matrix is not exactly Hermitian")

    radii = [
        ((point.f.real.hi - point.f.real.lo) + (point.f.imag.hi - point.f.imag.lo)) / 2
        for point in selected
    ]
    row_bounds = [
        sum(
            (radii[i] + radii[j]) / (selected[i].x + selected[j].x)
            for j in range(size)
        )
        for i in range(size)
    ]
    uncertainty_norm_upper = max(row_bounds)
    pivots = ldl_pivots(matrix, delta)
    midpoint_shift_pd = len(pivots) == size and all(value > 0 for value in pivots)
    certified = midpoint_shift_pd and delta > uncertainty_norm_upper
    lower_eigenvalue_margin = delta - uncertainty_norm_upper if certified else None
    return {
        "id": check.get("id"),
        "kind": "whole-pick-positive-definite",
        "status": "CERTIFIED_POSITIVE_DEFINITE" if certified else "NOT_CERTIFIED",
        "delta": fraction_json(delta),
        "uncertainty_operator_norm_upper": fraction_json(uncertainty_norm_upper),
        "lower_eigenvalue_margin": None if lower_eigenvalue_margin is None else fraction_json(lower_eigenvalue_margin),
        "ldl_pivots": [fraction_json(value) for value in pivots],
        "points": [point.identifier for point in selected],
    }


def verify(data: dict[str, Any]) -> dict[str, object]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA}")
    raw_points = data.get("points")
    raw_checks = data.get("checks")
    if not isinstance(raw_points, list) or not isinstance(raw_checks, list):
        raise CertificateError("points and checks must be arrays")
    points: dict[str, Point] = {}
    point_summaries: list[dict[str, object]] = []
    for index, raw in enumerate(raw_points):
        point = parse_point(raw, index)
        if point.identifier in points:
            raise CertificateError("duplicate point ID")
        points[point.identifier] = point
        point_summaries.append({
            "id": point.identifier,
            "x": fraction_json(point.x),
            "t": fraction_json(point.t),
            "f_intersection": point.f.to_json(),
        })

    results: list[dict[str, object]] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_checks):
        name = f"checks[{index}]"
        if not isinstance(raw, dict):
            raise CertificateError(f"{name} must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise CertificateError(f"{name}.id must be unique and nonempty")
        seen.add(identifier)
        kind = raw.get("kind")
        if kind == "complex-pick-rayleigh":
            result = complex_pick_check(raw, points, name)
        elif kind == "whole-pick-positive-definite":
            result = whole_matrix_check(raw, points, name)
        else:
            raise CertificateError(f"{name}.kind is unsupported")
        results.append(result)

    result: dict[str, object] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "point_count": len(points),
        "check_count": len(results),
        "points": point_summaries,
        "checks": results,
        "negative_checks": [item["id"] for item in results if item.get("status") == "CERTIFIED_NEGATIVE"],
        "unresolved_checks": [item["id"] for item in results if item.get("status") in {"UNRESOLVED_ZERO_TOUCH", "NOT_CERTIFIED"}],
        "proof_boundary": (
            "The checker proves only exact finite contractions and midpoint-plus-radius Hermitian bounds from supplied primitive rectangles. "
            "It does not independently evaluate xi, zeta, gamma, or the Riemann-Siegel remainder."
        ),
    }
    result["status"] = (
        "CERTIFIED_NEGATIVE_WITNESS_PENDING_PARENT_AUDIT" if result["negative_checks"]
        else "RECHECK_INCOMPLETE" if result["unresolved_checks"]
        else "ALL_CHECKS_NONNEGATIVE_OR_POSITIVE_DEFINITE"
    )
    result["verification_sha256"] = canonical_digest(result)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("root must be an object")
        result = verify(data)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": VERIFY_SCHEMA, "verified": False, "status": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
