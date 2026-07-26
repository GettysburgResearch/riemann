#!/usr/bin/env python3
"""Exact standard-library checker for T-12202 and L-12203.

The checker handles finite rational moment tables only.  It does not evaluate
Riemann xi and cannot create an RH candidate by itself.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.moving-anchor-two-schur.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    num = integer(value.get("numerator"), f"{name}.numerator")
    den = integer(value.get("denominator"), f"{name}.denominator")
    if den <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(num, den)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def vector_json(values: Sequence[Fraction]) -> list[dict[str, str]]:
    return [fraction_json(value) for value in values]


def shifted_moments(old: Sequence[Fraction], t: Fraction) -> list[Fraction]:
    return [
        sum(
            Fraction(math.comb(k, j)) * t ** (k - j) * old[j]
            for j in range(k + 1)
        )
        for k in range(len(old))
    ]


def exact_ldl_positive(matrix: Sequence[Sequence[Fraction]]) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise CertificateError("matrix must be nonempty and square")
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots: list[Fraction] = []
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivot = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivot <= 0:
            raise CertificateError("required inherited block is not positive definite")
        pivots.append(pivot)
        for row in range(i + 1, n):
            lower[row][i] = (
                matrix[row][i]
                - sum(
                    lower[row][k] * lower[i][k] * pivots[k]
                    for k in range(i)
                )
            ) / pivot
    return pivots


def invert(matrix: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    n = len(matrix)
    aug = [
        [Fraction(matrix[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot_row = next((row for row in range(col, n) if aug[row][col]), None)
        if pivot_row is None:
            raise CertificateError("matrix is singular")
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        pivot = aug[col][col]
        aug[col] = [entry / pivot for entry in aug[col]]
        for row in range(n):
            if row == col:
                continue
            multiplier = aug[row][col]
            if multiplier:
                aug[row] = [
                    aug[row][j] - multiplier * aug[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def matrix_vector(
    matrix: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]
) -> list[Fraction]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    return sum(a * b for a, b in zip(left, right))


def poly_mul(left: Sequence[Fraction], right: Sequence[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def poly_add(left: Sequence[Fraction], right: Sequence[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return [
        (left[i] if i < len(left) else Fraction(0))
        + (right[i] if i < len(right) else Fraction(0))
        for i in range(size)
    ]


def poly_scale(poly: Sequence[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * coefficient for coefficient in poly]


def shift_z_to_y(poly: Sequence[Fraction], t: Fraction) -> list[Fraction]:
    result = [Fraction(0)] * len(poly)
    for degree, coefficient in enumerate(poly):
        for power in range(degree + 1):
            result[power] += (
                coefficient
                * Fraction(math.comb(degree, power))
                * t ** (degree - power)
            )
    return result


def convolve_value(coefficients: Sequence[Fraction], moments: Sequence[Fraction]) -> Fraction:
    square = poly_mul(coefficients, coefficients)
    if len(square) > len(moments):
        raise CertificateError("moment table is too short for polynomial contraction")
    return sum(square[k] * moments[k] for k in range(len(square)))


def build_data(old: Sequence[Fraction], t: Fraction) -> dict[str, Any]:
    if t <= 0:
        raise CertificateError("moving anchor t must be positive")
    if len(old) < 3 or (len(old) - 1) % 2:
        raise CertificateError("old moment table must have length 2m+1")
    m = (len(old) - 1) // 2
    inherited = shifted_moments(old, t)
    v = inherited[:m]
    b0 = [[inherited[i + j + 1] for j in range(m)] for i in range(m)]
    w = [inherited[i + 1] - t * inherited[i] for i in range(m)]
    b1 = [
        [inherited[i + j + 2] - t * inherited[i + j + 1] for j in range(m)]
        for i in range(m)
    ]
    pivots0 = exact_ldl_positive(b0)
    pivots1 = exact_ldl_positive(b1)
    d = matrix_vector(invert(b0), v)
    e = matrix_vector(invert(b1), w)
    theta0 = dot(v, d)
    theta1 = dot(w, e)
    upper = (inherited[0] - theta1) / t

    q0 = [Fraction(1)] + [-entry for entry in d]
    q1 = [Fraction(1)] + [-entry for entry in e]
    packet = poly_add(
        poly_scale(poly_mul(q0, q0), t),
        poly_mul([-t, Fraction(1)], poly_mul(q1, q1)),
    )
    if packet[0] != 0:
        raise AssertionError("width polynomial did not vanish at z=0")
    quotient_z = packet[1:]
    old_width_poly = shift_z_to_y(quotient_z, t)
    width_value = sum(
        old_width_poly[k] * old[k] for k in range(len(old_width_poly))
    )
    expected_width_value = t * (upper - theta0)
    if width_value != expected_width_value:
        raise AssertionError("old-cone width identity failed")
    if upper < theta0:
        raise CertificateError("moving-anchor admissible interval is empty")

    return {
        "m": m,
        "inherited": inherited,
        "b0_pivots": pivots0,
        "b1_pivots": pivots1,
        "theta0": theta0,
        "theta1": theta1,
        "upper": upper,
        "q0": q0,
        "q1": q1,
        "old_width_poly": old_width_poly,
        "width_value": width_value,
    }


def classify(c0: Fraction, theta0: Fraction, upper: Fraction) -> str:
    if c0 < theta0:
        return "LOWER_SQUARE_VIOLATION"
    if c0 > upper:
        return "UPPER_SHIFTED_SQUARE_VIOLATION"
    if c0 == theta0 == upper:
        return "COLLAPSED_BOUNDARY"
    if c0 == theta0:
        return "LOWER_BOUNDARY"
    if c0 == upper:
        return "UPPER_BOUNDARY"
    return "INTERIOR_ADMISSIBLE"


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    raw_old = data.get("old_moments")
    if not isinstance(raw_old, list):
        raise CertificateError("old_moments must be an array")
    old = [fraction(value, f"old_moments[{index}]") for index, value in enumerate(raw_old)]
    t = fraction(data.get("t"), "t")
    derived = build_data(old, t)

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    for key, exact in (
        ("theta0", derived["theta0"]),
        ("theta1", derived["theta1"]),
        ("upper", derived["upper"]),
        ("width_value", derived["width_value"]),
    ):
        if fraction(claimed.get(key), f"claimed.{key}") != exact:
            raise CertificateError(f"claimed {key} mismatch")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise CertificateError("cases must be a nonempty array")
    seen: set[str] = set()
    outputs: list[dict[str, Any]] = []
    new_moments_prefix = None
    for index, raw in enumerate(cases):
        if not isinstance(raw, dict):
            raise CertificateError(f"cases[{index}] must be an object")
        case_id = raw.get("id")
        if not isinstance(case_id, str) or not case_id or case_id in seen:
            raise CertificateError("case IDs must be nonempty and unique")
        seen.add(case_id)
        c0 = fraction(raw.get("c0"), f"cases[{index}].c0")
        status = classify(c0, derived["theta0"], derived["upper"])
        if raw.get("expected_status") != status:
            raise CertificateError(f"case {case_id}: expected status mismatch")

        moments = [c0] + list(derived["inherited"])
        lower_value = convolve_value(derived["q0"], moments)
        shifted_moments = [
            moments[k + 1] - t * moments[k] for k in range(len(moments) - 1)
        ]
        upper_value = convolve_value(derived["q1"], shifted_moments)
        if lower_value != c0 - derived["theta0"]:
            raise AssertionError("lower witness identity failed")
        if upper_value != derived["inherited"][0] - t * c0 - derived["theta1"]:
            raise AssertionError("upper witness identity failed")
        outputs.append(
            {
                "id": case_id,
                "status": status,
                "c0": fraction_json(c0),
                "lower_square_value": fraction_json(lower_value),
                "upper_shifted_square_value": fraction_json(upper_value),
            }
        )
        new_moments_prefix = moments

    return {
        "schema": SCHEMA,
        "status": "EXACT_SYNTHETIC_TWO_SCHUR_REPLAY",
        "m": derived["m"],
        "t": fraction_json(t),
        "theta0": fraction_json(derived["theta0"]),
        "theta1": fraction_json(derived["theta1"]),
        "upper": fraction_json(derived["upper"]),
        "admissible_width": fraction_json(derived["upper"] - derived["theta0"]),
        "old_width_value": fraction_json(derived["width_value"]),
        "q0": vector_json(derived["q0"]),
        "q1": vector_json(derived["q1"]),
        "old_width_polynomial": vector_json(derived["old_width_poly"]),
        "b0_ldl_pivots": vector_json(derived["b0_pivots"]),
        "b1_ldl_pivots": vector_json(derived["b1_pivots"]),
        "cases": outputs,
        "proof_boundary": "finite rational moment regression only; no Riemann-xi evaluation",
    }


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)
    try:
        output = verify_certificate(load(args.certificate))
    except CertificateError as exc:
        print(json.dumps({"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
