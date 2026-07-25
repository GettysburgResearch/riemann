#!/usr/bin/env python3
"""Exact verifier for directed Hermitian Toeplitz coefficient boxes.

Supports fixed complex vectors, positive Gram portfolios, and a small-matrix
midpoint-radius positive-definiteness certificate. After parsing rational
endpoints, it uses only Python integers and fractions.Fraction.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.toeplitz-box-spectral-closure.v1"
VERIFY_SCHEMA = "riemann.toeplitz-box-spectral-closure.verification.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not an integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("reversed interval")

    @classmethod
    def parse(cls, value: Any, name: str) -> "Interval":
        if not isinstance(value, dict):
            raise CertificateError(f"{name} must be an object")
        return cls(
            fraction(value.get("lower"), f"{name}.lower"),
            fraction(value.get("upper"), f"{name}.upper"),
        )

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def scale(self, coefficient: Fraction) -> "Interval":
        first = self.lower * coefficient
        second = self.upper * coefficient
        return Interval(min(first, second), max(first, second))

    def to_json(self) -> dict[str, object]:
        return {
            "lower": fraction_json(self.lower),
            "upper": fraction_json(self.upper),
        }


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
        return {
            "real": fraction_json(self.real),
            "imag": fraction_json(self.imag),
        }


def gaussian(value: Gaussian | Fraction | int) -> Gaussian:
    return value if isinstance(value, Gaussian) else Gaussian(Fraction(value), Fraction(0))


def parse_gaussian(value: Any, name: str) -> Gaussian:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    return Gaussian(
        fraction(value.get("real"), f"{name}.real"),
        fraction(value.get("imag"), f"{name}.imag"),
    )


def parse_vector(value: Any, dimension: int, name: str) -> list[Gaussian]:
    if not isinstance(value, list) or len(value) != dimension:
        raise CertificateError(f"{name} has the wrong length")
    vector = [parse_gaussian(entry, f"{name}[{index}]") for index, entry in enumerate(value)]
    if not any(entry.real or entry.imag for entry in vector):
        raise CertificateError(f"{name} is zero")
    return vector


def autocorrelation(vector: list[Gaussian]) -> list[Gaussian]:
    dimension = len(vector)
    result: list[Gaussian] = []
    for lag in range(dimension):
        value = Gaussian()
        for index in range(dimension - lag):
            value += vector[index + lag] * vector[index].conjugate()
        result.append(value)
    return result


def aggregate_portfolio(
    raw_terms: Any,
    dimension: int,
    name: str,
) -> tuple[Fraction, list[Gaussian]]:
    if not isinstance(raw_terms, list) or not raw_terms:
        raise CertificateError(f"{name} must be a nonempty array")
    trace_weight = Fraction(0)
    aggregate = [Gaussian() for _ in range(dimension)]
    for index, raw_term in enumerate(raw_terms):
        if not isinstance(raw_term, dict):
            raise CertificateError(f"{name}[{index}] must be an object")
        weight = fraction(raw_term.get("weight"), f"{name}[{index}].weight")
        if weight <= 0:
            raise CertificateError("Gram weights must be positive")
        vector = parse_vector(
            raw_term.get("vector"),
            dimension,
            f"{name}[{index}].vector",
        )
        vector_autocorrelation = autocorrelation(vector)
        trace_weight += weight * sum(entry.abs_squared() for entry in vector)
        for lag in range(dimension):
            aggregate[lag] += weight * vector_autocorrelation[lag]
    return trace_weight, aggregate


def contract_prime(
    lags: list[tuple[Interval, Interval]],
    aggregate: list[Gaussian],
) -> Interval:
    total = Interval(Fraction(0), Fraction(0))
    for (real_box, imag_box), coefficient in zip(lags, aggregate):
        total = total.add(real_box.scale(coefficient.real))
        total = total.add(imag_box.scale(-coefficient.imag))
    return total


def full_trace_interval(
    alpha: Interval,
    correction_radius: Fraction,
    trace_weight: Fraction,
    prime: Interval,
) -> Interval:
    return Interval(
        alpha.lower * trace_weight - prime.upper - correction_radius * trace_weight,
        alpha.upper * trace_weight - prime.lower + correction_radius * trace_weight,
    )


def midpoint(lag: tuple[Interval, Interval]) -> Gaussian:
    real_box, imag_box = lag
    return Gaussian(
        (real_box.lower + real_box.upper) / 2,
        (imag_box.lower + imag_box.upper) / 2,
    )


def ldl_pivots(matrix: list[list[Gaussian]]) -> list[Fraction]:
    dimension = len(matrix)
    lower = [[Gaussian() for _ in range(dimension)] for _ in range(dimension)]
    diagonal: list[Fraction] = []
    for index in range(dimension):
        lower[index][index] = Gaussian(Fraction(1), Fraction(0))

    for column in range(dimension):
        if matrix[column][column].imag != 0:
            raise CertificateError("Hermitian diagonal is not real")
        pivot = matrix[column][column].real
        for prior in range(column):
            pivot -= lower[column][prior].abs_squared() * diagonal[prior]
        diagonal.append(pivot)
        if pivot <= 0:
            return diagonal
        for row in range(column + 1, dimension):
            value = matrix[row][column]
            for prior in range(column):
                value -= (
                    lower[row][prior]
                    * lower[column][prior].conjugate()
                    * diagonal[prior]
                )
            lower[row][column] = value / pivot
    return diagonal


def whole_matrix_positive(
    alpha: Interval,
    correction_radius: Fraction,
    lags: list[tuple[Interval, Interval]],
    delta: Fraction,
) -> tuple[bool, list[Fraction], Fraction, Fraction, Fraction]:
    dimension = len(lags)
    alpha_midpoint = (alpha.lower + alpha.upper) / 2
    alpha_radius = (alpha.upper - alpha.lower) / 2
    coefficient_midpoints = [midpoint(lag) for lag in lags]
    if coefficient_midpoints[0].imag != 0:
        raise CertificateError("lag-zero midpoint must be real")

    # H_0 - delta I = alpha_mid I - S_mid - delta I.
    matrix = [[Gaussian() for _ in range(dimension)] for _ in range(dimension)]
    for row in range(dimension):
        matrix[row][row] = Gaussian(
            alpha_midpoint - coefficient_midpoints[0].real - delta
        )
        for column in range(row + 1, dimension):
            entry = coefficient_midpoints[column - row] / 2
            matrix[row][column] = -entry
            matrix[column][row] = -entry.conjugate()

    pivots = ldl_pivots(matrix)
    midpoint_is_positive = len(pivots) == dimension and all(pivot > 0 for pivot in pivots)

    coefficient_radii: list[Fraction] = []
    for real_box, imag_box in lags:
        coefficient_radii.append(
            (
                real_box.upper
                - real_box.lower
                + imag_box.upper
                - imag_box.lower
            )
            / 2
        )
    toeplitz_radius = coefficient_radii[0] + sum(coefficient_radii[1:])
    total_radius = alpha_radius + toeplitz_radius + correction_radius
    certified = midpoint_is_positive and total_radius < delta
    return certified, pivots, toeplitz_radius, total_radius, delta - total_radius


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA}")
    dimension = integer(data.get("dimension"), "dimension")
    if dimension < 1:
        raise CertificateError("dimension must be positive")
    alpha = Interval.parse(data.get("alpha_interval"), "alpha_interval")
    correction_radius = fraction(
        data.get("correction_operator_radius"),
        "correction_operator_radius",
    )
    if correction_radius < 0:
        raise CertificateError("correction radius must be nonnegative")

    raw_lags = data.get("lags")
    if not isinstance(raw_lags, list) or len(raw_lags) != dimension:
        raise CertificateError("wrong lag count")
    lags: list[tuple[Interval, Interval]] = []
    for lag, raw_row in enumerate(raw_lags):
        if not isinstance(raw_row, dict):
            raise CertificateError(f"lags[{lag}] must be an object")
        if integer(raw_row.get("lag"), f"lags[{lag}].lag") != lag:
            raise CertificateError("lag order mismatch")
        real_box = Interval.parse(
            raw_row.get("real_interval"),
            f"lags[{lag}].real_interval",
        )
        imag_box = Interval.parse(
            raw_row.get("imag_interval"),
            f"lags[{lag}].imag_interval",
        )
        if lag == 0 and (imag_box.lower != 0 or imag_box.upper != 0):
            raise CertificateError("lag zero must be real")
        lags.append((real_box, imag_box))

    raw_checks = data.get("checks")
    if not isinstance(raw_checks, list):
        raise CertificateError("checks must be an array")
    seen_ids: set[str] = set()
    checks: list[dict[str, Any]] = []
    for index, raw_check in enumerate(raw_checks):
        if not isinstance(raw_check, dict):
            raise CertificateError(f"checks[{index}] must be an object")
        identifier = raw_check.get("id")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in seen_ids
        ):
            raise CertificateError("check IDs must be unique and nonempty")
        seen_ids.add(identifier)
        kind = raw_check.get("kind")

        if kind == "fixed-vector":
            vector = parse_vector(
                raw_check.get("vector"),
                dimension,
                f"checks[{index}].vector",
            )
            trace_weight = sum(entry.abs_squared() for entry in vector)
            aggregate = autocorrelation(vector)
            prime = contract_prime(lags, aggregate)
            full = full_trace_interval(
                alpha,
                correction_radius,
                trace_weight,
                prime,
            )
            status = (
                "CERTIFIED_NEGATIVE_MATRIX"
                if full.upper < 0
                else "CERTIFIED_POSITIVE_TRACE"
                if full.lower > 0
                else "UNRESOLVED"
            )
            checks.append(
                {
                    "id": identifier,
                    "kind": kind,
                    "status": status,
                    "trace_weight": fraction_json(trace_weight),
                    "prime_interval": prime.to_json(),
                    "full_interval": full.to_json(),
                }
            )

        elif kind == "gram-portfolio":
            trace_weight, aggregate = aggregate_portfolio(
                raw_check.get("terms"),
                dimension,
                f"checks[{index}].terms",
            )
            prime = contract_prime(lags, aggregate)
            full = full_trace_interval(
                alpha,
                correction_radius,
                trace_weight,
                prime,
            )
            status = (
                "CERTIFIED_NEGATIVE_MATRIX"
                if full.upper < 0
                else "CERTIFIED_POSITIVE_TRACE"
                if full.lower > 0
                else "UNRESOLVED"
            )
            checks.append(
                {
                    "id": identifier,
                    "kind": kind,
                    "status": status,
                    "trace_weight": fraction_json(trace_weight),
                    "prime_interval": prime.to_json(),
                    "full_interval": full.to_json(),
                    "aggregate_autocorrelation": [
                        coefficient.to_json() for coefficient in aggregate
                    ],
                }
            )

        elif kind == "whole-matrix-positive":
            delta = fraction(raw_check.get("delta"), f"checks[{index}].delta")
            if delta <= 0:
                raise CertificateError("delta must be positive")
            certified, pivots, toeplitz_radius, total_radius, margin = (
                whole_matrix_positive(
                    alpha,
                    correction_radius,
                    lags,
                    delta,
                )
            )
            checks.append(
                {
                    "id": identifier,
                    "kind": kind,
                    "status": (
                        "CERTIFIED_POSITIVE_DEFINITE"
                        if certified
                        else "NOT_CERTIFIED"
                    ),
                    "delta": fraction_json(delta),
                    "toeplitz_uncertainty_radius": fraction_json(
                        toeplitz_radius
                    ),
                    "total_operator_radius": fraction_json(total_radius),
                    "lower_margin": fraction_json(margin),
                    "ldl_pivots": [fraction_json(pivot) for pivot in pivots],
                }
            )

        else:
            raise CertificateError(f"unsupported check kind {kind!r}")

    negatives = [
        check["id"]
        for check in checks
        if check["status"] == "CERTIFIED_NEGATIVE_MATRIX"
    ]
    unresolved = [
        check["id"]
        for check in checks
        if check["status"] in {"UNRESOLVED", "NOT_CERTIFIED"}
    ]
    return {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "dimension": dimension,
        "checks": checks,
        "negative_matrix_certificates": negatives,
        "unresolved_checks": unresolved,
        "status": (
            "CERTIFIED_NEGATIVE_MATRIX"
            if negatives
            else "INCOMPLETE"
            if unresolved
            else "NO_NEGATIVE_IN_DECLARED_CHECKS"
        ),
        "proof_boundary": (
            "Exact finite arithmetic over supplied coefficient boxes. A negative "
            "D-0801 RH implication retains the parent admissibility and "
            "Guinand--Weil normalization dependencies."
        ),
    }


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
        result = {
            "schema": VERIFY_SCHEMA,
            "verified": False,
            "status": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
