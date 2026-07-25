#!/usr/bin/env python3
"""Exact verifier for an eight-point Hermitian Pick matrix box.

All arithmetic uses integers and ``fractions.Fraction``. The certificate
contains outward rectangles for primitive F=xi'/xi values. The verifier
reconstructs the exact midpoint Pick matrix, proves ``M-lambda I`` positive
definite by an exact Hermitian LDL decomposition, bounds every admitted matrix
perturbation by a maximum row sum, and checks the final strict spectral moat.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.xi-pick-box-positive-definite.v1"
VERIFY_SCHEMA = "riemann.xi-pick-box-positive-definite.verification.v1"
Gaussian = tuple[Fraction, Fraction]


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
    raise CertificateError(f"{name} must be an integer or string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def parse_interval(value: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    lower = parse_fraction(value.get("lower"), f"{name}.lower")
    upper = parse_fraction(value.get("upper"), f"{name}.upper")
    if lower > upper:
        raise CertificateError(f"{name} has reversed endpoints")
    return lower, upper


def gsub(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] - b[0], a[1] - b[1]


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gconj(a: Gaussian) -> Gaussian:
    return a[0], -a[1]


def gscale(a: Gaussian, value: Fraction) -> Gaussian:
    return a[0] * value, a[1] * value


def gdiv_real(a: Gaussian, value: Fraction) -> Gaussian:
    if value == 0:
        raise CertificateError("division by zero")
    return a[0] / value, a[1] / value


def midpoint_radius(interval: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    lower, upper = interval
    return (lower + upper) / 2, (upper - lower) / 2


def hermitian_ldl_pivots(matrix: list[list[Gaussian]], shift: Fraction) -> list[Fraction]:
    n = len(matrix)
    lower: list[list[Gaussian]] = [
        [(Fraction(0), Fraction(0)) for _ in range(n)] for _ in range(n)
    ]
    pivots: list[Fraction] = []
    for i in range(n):
        value = (matrix[i][i][0] - shift, matrix[i][i][1])
        for k in range(i):
            value = gsub(
                value,
                gscale(gmul(lower[i][k], gconj(lower[i][k])), pivots[k]),
            )
        if value[1] != 0:
            raise CertificateError(f"LDL pivot {i} is not real")
        pivot = value[0]
        pivots.append(pivot)
        if pivot <= 0:
            raise CertificateError(f"LDL pivot {i} is not positive")
        lower[i][i] = (Fraction(1), Fraction(0))
        for j in range(i + 1, n):
            value = matrix[j][i]
            for k in range(i):
                value = gsub(
                    value,
                    gscale(gmul(lower[j][k], gconj(lower[i][k])), pivots[k]),
                )
            lower[j][i] = gdiv_real(value, pivot)
    return pivots


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, object]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    matrix_data = data.get("matrix")
    if not isinstance(matrix_data, dict):
        raise CertificateError("matrix must be an object")
    raw_points = matrix_data.get("points")
    point_count = parse_int(matrix_data.get("point_count"), "matrix.point_count")
    if not isinstance(raw_points, list) or len(raw_points) != point_count or point_count < 1:
        raise CertificateError("matrix points do not match point_count")

    points: list[dict[str, object]] = []
    identifiers: set[str] = set()
    heights: set[Fraction] = set()
    for index, raw in enumerate(raw_points):
        name = f"matrix.points[{index}]"
        if not isinstance(raw, dict):
            raise CertificateError(f"{name} must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in identifiers:
            raise CertificateError(f"{name}.id is invalid or duplicated")
        identifiers.add(identifier)
        x = parse_fraction(raw.get("x"), f"{name}.x")
        t = parse_fraction(raw.get("t"), f"{name}.t")
        if x <= 0:
            raise CertificateError(f"{name}.x must be positive")
        heights.add(t)
        primitive = raw.get("f_intersection")
        if not isinstance(primitive, dict):
            raise CertificateError(f"{name}.f_intersection must be an object")
        real = parse_interval(primitive.get("real"), f"{name}.f_intersection.real")
        imag = parse_interval(primitive.get("imag"), f"{name}.f_intersection.imag")
        real_mid, real_radius = midpoint_radius(real)
        imag_mid, imag_radius = midpoint_radius(imag)
        points.append(
            {
                "id": identifier,
                "x": x,
                "t": t,
                "mid": (real_mid, imag_mid),
                "real_radius": real_radius,
                "imag_radius": imag_radius,
            }
        )
    if len(heights) != 1:
        raise CertificateError("points are not at one exact ordinate")

    midpoint: list[list[Gaussian]] = []
    entry_radii: list[list[Fraction]] = []
    for first in points:
        row: list[Gaussian] = []
        radius_row: list[Fraction] = []
        for second in points:
            denominator = first["x"] + second["x"]  # type: ignore[operator]
            first_mid = first["mid"]  # type: ignore[assignment]
            second_mid = second["mid"]  # type: ignore[assignment]
            numerator = (
                first_mid[0] + second_mid[0],  # type: ignore[index]
                first_mid[1] - second_mid[1],  # type: ignore[index]
            )
            row.append(gdiv_real(numerator, denominator))
            radius_row.append(
                (
                    first["real_radius"] + second["real_radius"]  # type: ignore[operator]
                    + first["imag_radius"] + second["imag_radius"]  # type: ignore[operator]
                )
                / denominator
            )
        midpoint.append(row)
        entry_radii.append(radius_row)

    for i in range(point_count):
        if midpoint[i][i][1] != 0:
            raise CertificateError("midpoint diagonal is not real")
        for j in range(point_count):
            if midpoint[i][j] != gconj(midpoint[j][i]):
                raise CertificateError("midpoint matrix is not exactly Hermitian")
            if entry_radii[i][j] != entry_radii[j][i] or entry_radii[i][j] < 0:
                raise CertificateError("entry-radius matrix is invalid")

    midpoint_bound = data.get("midpoint_lower_bound")
    if not isinstance(midpoint_bound, dict):
        raise CertificateError("midpoint_lower_bound must be an object")
    shift = parse_fraction(midpoint_bound.get("lambda"), "midpoint_lower_bound.lambda")
    if shift <= 0:
        raise CertificateError("midpoint lambda must be positive")
    pivots = hermitian_ldl_pivots(midpoint, shift)
    claimed_pivots = midpoint_bound.get("pivots")
    if claimed_pivots is not None:
        if not isinstance(claimed_pivots, list) or len(claimed_pivots) != len(pivots):
            raise CertificateError("claimed pivot array has wrong length")
        parsed = [
            parse_fraction(value, f"midpoint_lower_bound.pivots[{index}]")
            for index, value in enumerate(claimed_pivots)
        ]
        if parsed != pivots:
            raise CertificateError("claimed LDL pivots do not match reconstruction")

    operator_bound = max(sum(row, Fraction(0)) for row in entry_radii)
    uncertainty = data.get("uncertainty_operator_bound")
    if not isinstance(uncertainty, dict):
        raise CertificateError("uncertainty_operator_bound must be an object")
    claimed_exact = parse_fraction(uncertainty.get("exact"), "uncertainty_operator_bound.exact")
    if claimed_exact != operator_bound:
        raise CertificateError("claimed exact uncertainty bound does not match")
    claimed_upper = parse_fraction(
        uncertainty.get("upper_power_of_two"), "uncertainty_operator_bound.upper_power_of_two"
    )
    if not operator_bound < claimed_upper:
        raise CertificateError("uncertainty bound is not below its claimed upper moat")

    final_data = data.get("final_matrix_lower_bound")
    if not isinstance(final_data, dict):
        raise CertificateError("final_matrix_lower_bound must be an object")
    final_lower = parse_fraction(final_data.get("lambda"), "final_matrix_lower_bound.lambda")
    rigorous_lower = shift - operator_bound
    if not rigorous_lower > final_lower > 0:
        raise CertificateError("final strict eigenvalue lower bound is not proved")

    result: dict[str, object] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": "CERTIFIED_POSITIVE_DEFINITE_FINITE_MATRIX",
        "point_count": point_count,
        "exact_ordinate": fraction_json(next(iter(heights))),
        "midpoint_eigenvalue_lower_bound": fraction_json(shift),
        "uncertainty_operator_upper_bound": fraction_json(operator_bound),
        "rigorous_matrix_eigenvalue_lower_bound": fraction_json(rigorous_lower),
        "claimed_simplified_lower_bound": fraction_json(final_lower),
        "minimum_ldl_pivot": fraction_json(min(pivots)),
        "counterexample_candidate": None,
        "proof_boundary": (
            "This exact checker certifies positive definiteness only for the Hermitian "
            "matrix box reconstructed from the supplied primitive rectangles."
        ),
    }
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
            raise CertificateError("certificate root must be an object")
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
