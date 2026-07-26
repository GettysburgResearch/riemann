#!/usr/bin/env python3
"""Exact checker for the positive-node one-scalar Geronimus extension.

This checker evaluates no special function and uses only Python integers and
fractions.Fraction. It verifies the finite moment algebra in L-9314, including
both explicit polynomial-square witnesses when the new scalar leaves its exact
admissible interval.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SCHEMA = "riemann.positive-node-one-scalar.v1"
RESULT_SCHEMA = "riemann.positive-node-one-scalar.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rat(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def ldl_positive(matrix: list[list[Fraction]], name: str) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise CertificateError(f"{name} must be nonempty and square")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise CertificateError(f"{name} must be symmetric")
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    diagonal: list[Fraction] = []
    for i in range(n):
        pivot = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * diagonal[k] for k in range(i)
        )
        if pivot <= 0:
            raise CertificateError(f"{name} is not positive definite at pivot {i}")
        diagonal.append(pivot)
        lower[i][i] = Fraction(1)
        for j in range(i + 1, n):
            numerator = matrix[j][i] - sum(
                lower[j][k] * lower[i][k] * diagonal[k] for k in range(i)
            )
            lower[j][i] = numerator / pivot
    return diagonal


def solve(
    matrix: list[list[Fraction]], vector: list[Fraction], name: str
) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or len(vector) != n or any(len(row) != n for row in matrix):
        raise CertificateError(f"bad dimensions in {name}")
    augmented = [matrix[i][:] + [vector[i]] for i in range(n)]
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if augmented[row][column]), None
        )
        if pivot is None:
            raise CertificateError(f"singular matrix in {name}")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(n + 1)
                ]
    return [augmented[i][-1] for i in range(n)]


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    if len(left) != len(right):
        raise CertificateError("dot-product dimension mismatch")
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def one_minus_linear_times(
    coefficients: list[Fraction], w: Fraction
) -> list[Fraction]:
    product = poly_mul([w, Fraction(1)], coefficients)
    result = [-value for value in product]
    result[0] += 1
    return result


def moment_value(
    polynomial: list[Fraction], moments: list[Fraction]
) -> Fraction:
    if len(polynomial) > len(moments):
        raise CertificateError("polynomial exceeds available moment degree")
    return sum(
        (coefficient * moments[i] for i, coefficient in enumerate(polynomial)),
        Fraction(0),
    )


def verify_case(case: dict[str, Any], index: int) -> dict[str, Any]:
    identifier = case.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise CertificateError(f"cases[{index}].id must be a nonempty string")
    w = rat(case.get("w"), f"cases[{index}].w")
    if w <= 0:
        raise CertificateError("the added node w must be positive")
    raw_moments = case.get("old_moments")
    if not isinstance(raw_moments, list):
        raise CertificateError("old_moments must be a list")
    old = [
        rat(value, f"cases[{index}].old_moments[{j}]")
        for j, value in enumerate(raw_moments)
    ]
    if len(old) < 3 or len(old) % 2 != 1:
        raise CertificateError("old_moments must have odd length 2m-1")
    m = (len(old) + 1) // 2
    b0 = rat(case.get("new_b0"), f"cases[{index}].new_b0")

    size = m - 1
    r0 = old[:size]
    r1 = old[1 : size + 1]
    c0 = [
        [old[i + j + 1] + w * old[i + j] for j in range(size)]
        for i in range(size)
    ]
    c1 = [
        [old[i + j + 2] + w * old[i + j + 1] for j in range(size)]
        for i in range(size)
    ]
    pivots0 = ldl_positive(c0, f"{identifier}.C0")
    pivots1 = ldl_positive(c1, f"{identifier}.C1")
    coeff0 = solve(c0, r0, f"{identifier}.C0 solve")
    coeff1 = solve(c1, r1, f"{identifier}.C1 solve")
    lower = dot(r0, coeff0)
    upper = (old[0] - dot(r1, coeff1)) / w
    if lower > upper:
        raise CertificateError("computed scalar interval is empty")

    new_moments = [b0]
    for k, value in enumerate(old):
        new_moments.append(value - w * new_moments[k])

    q_lower = one_minus_linear_times(coeff0, w)
    q_upper = one_minus_linear_times(coeff1, w)
    lower_value = moment_value(poly_mul(q_lower, q_lower), new_moments)
    upper_poly = [Fraction(0)] + poly_mul(q_upper, q_upper)
    upper_value = moment_value(upper_poly, new_moments)
    if lower_value != b0 - lower:
        raise CertificateError("lower square-witness identity failed")
    if upper_value != w * (upper - b0):
        raise CertificateError("upper y-square-witness identity failed")

    if b0 < lower:
        status = "CERTIFIED_NEGATIVE_LOWER_SQUARE_WITNESS"
        if lower_value >= 0:
            raise CertificateError("lower witness was not negative")
    elif b0 > upper:
        status = "CERTIFIED_NEGATIVE_UPPER_Y_SQUARE_WITNESS"
        if upper_value >= 0:
            raise CertificateError("upper witness was not negative")
    elif b0 == lower or b0 == upper:
        status = "EXACT_BOUNDARY_ZERO"
    else:
        status = "CERTIFIED_INSIDE_ONE_SCALAR_INTERVAL"
        ldl_positive(
            [[new_moments[i + j] for j in range(m)] for i in range(m)],
            f"{identifier}.H0",
        )
        ldl_positive(
            [[new_moments[i + j + 1] for j in range(m)] for i in range(m)],
            f"{identifier}.H1",
        )

    expected = case.get("expected_status")
    if expected is not None and expected != status:
        raise CertificateError(
            f"{identifier} expected {expected!r} but reconstructed {status!r}"
        )

    return {
        "id": identifier,
        "status": status,
        "w": fj(w),
        "m": m,
        "old_moment_count": len(old),
        "new_moments": [fj(value) for value in new_moments],
        "lower_threshold": fj(lower),
        "upper_threshold": fj(upper),
        "new_b0": fj(b0),
        "lower_gap": fj(b0 - lower),
        "upper_gap": fj(upper - b0),
        "C0_ldl_pivots": [fj(value) for value in pivots0],
        "C1_ldl_pivots": [fj(value) for value in pivots1],
        "lower_witness_q": [fj(value) for value in q_lower],
        "lower_witness_value": fj(lower_value),
        "upper_witness_q": [fj(value) for value in q_upper],
        "upper_witness_yq2_value": fj(upper_value),
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    raw_cases = data.get("cases")
    if not isinstance(raw_cases, list) or not raw_cases:
        raise CertificateError("cases must be a nonempty list")
    identifiers: set[str] = set()
    results = []
    for index, case in enumerate(raw_cases):
        if not isinstance(case, dict):
            raise CertificateError(f"cases[{index}] must be an object")
        result = verify_case(case, index)
        if result["id"] in identifiers:
            raise CertificateError("duplicate case id")
        identifiers.add(result["id"])
        results.append(result)
    output = {
        "schema": RESULT_SCHEMA,
        "verified": True,
        "case_count": len(results),
        "negative_case_count": sum(
            result["status"].startswith("CERTIFIED_NEGATIVE")
            for result in results
        ),
        "cases": results,
        "proof_boundary": (
            "Exact finite moment algebra only. No special-function value, RH claim, "
            "or Riemann-xi counterexample is produced by a synthetic case."
        ),
    }
    output["proof_object_sha256"] = canonical_sha(output)
    return output


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
            "schema": RESULT_SCHEMA,
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
