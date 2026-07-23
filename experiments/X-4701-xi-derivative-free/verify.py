#!/usr/bin/env python3
"""Exact synthetic verifier for derivative-free xi-log-derivative witnesses.

This module evaluates a finite synthetic zero multiset through

    F_Z(s) = sum_{rho in Z} 1 / (s-rho)

using Gaussian-rational arithmetic. It does not evaluate the Riemann xi
function and cannot certify an RH counterexample. Its purpose is to audit the
signs, divided-difference conventions, node ordering, and determinant logic in
L-4701--L-4703 before a ball-arithmetic producer exists.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.xi-derivative-free-synthetic.v1"
Gaussian = tuple[Fraction, Fraction]


class CertificateError(ValueError):
    """Raised for malformed or inconsistent synthetic certificates."""


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
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


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def ginv(value: Gaussian) -> Gaussian:
    real, imag = value
    denominator = real * real + imag * imag
    if denominator == 0:
        raise CertificateError("synthetic evaluation point coincides with a zero")
    return real / denominator, -imag / denominator


def parse_zero_multiset(value: Any) -> list[tuple[Fraction, Fraction]]:
    if not isinstance(value, list) or not value:
        raise CertificateError("zeros must be a nonempty array")
    zeros: list[tuple[Fraction, Fraction]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise CertificateError(f"zeros[{index}] must be an object")
        zeros.append(
            (
                parse_fraction(item.get("delta"), f"zeros[{index}].delta"),
                parse_fraction(item.get("gamma"), f"zeros[{index}].gamma"),
            )
        )
    return zeros


def finite_logderivative_value(
    zeros: Sequence[tuple[Fraction, Fraction]],
    x: Fraction,
    height: Fraction,
) -> Gaussian:
    """Evaluate F_Z at 1/2+x+i*height exactly."""
    if x <= 0:
        raise CertificateError("horizontal offset x must be positive")
    total: Gaussian = (Fraction(0), Fraction(0))
    for delta, gamma in zeros:
        total = gadd(total, ginv((x - delta, height - gamma)))
    return total


def real_f(
    zeros: Sequence[tuple[Fraction, Fraction]],
    x: Fraction,
    height: Fraction,
) -> Fraction:
    return finite_logderivative_value(zeros, x, height)[0]


def j_value(
    zeros: Sequence[tuple[Fraction, Fraction]],
    x: Fraction,
    height: Fraction,
) -> Fraction:
    """Return J_T(x^2)=x*Re(F_Z(1/2+x+iT))."""
    return x * real_f(zeros, x, height)


def secant(
    zeros: Sequence[tuple[Fraction, Fraction]],
    left_x: Fraction,
    right_x: Fraction,
    height: Fraction,
) -> Fraction:
    if not 0 < left_x < right_x:
        raise CertificateError("secant nodes must satisfy 0 < left_x < right_x")
    left_u = left_x * left_x
    right_u = right_x * right_x
    return (
        j_value(zeros, right_x, height) - j_value(zeros, left_x, height)
    ) / (right_u - left_u)


def divided_difference(
    zeros: Sequence[tuple[Fraction, Fraction]],
    x_nodes: Sequence[Fraction],
    height: Fraction,
) -> Fraction:
    if not x_nodes:
        raise CertificateError("divided-difference node list cannot be empty")
    if any(x <= 0 for x in x_nodes):
        raise CertificateError("all divided-difference offsets must be positive")
    u_nodes = [x * x for x in x_nodes]
    if len(set(u_nodes)) != len(u_nodes):
        raise CertificateError("divided-difference squared nodes must be distinct")
    if u_nodes != sorted(u_nodes):
        raise CertificateError("divided-difference nodes must be strictly increasing")

    current = [j_value(zeros, x, height) for x in x_nodes]
    count = len(current)
    for order in range(1, count):
        current = [
            (current[index + 1] - current[index])
            / (u_nodes[index + order] - u_nodes[index])
            for index in range(count - order)
        ]
    return current[0]


def cross_loewner(
    zeros: Sequence[tuple[Fraction, Fraction]],
    row_x: Sequence[Fraction],
    col_x: Sequence[Fraction],
    height: Fraction,
) -> list[list[Fraction]]:
    if not row_x or not col_x:
        raise CertificateError("cross-Loewner node lists cannot be empty")
    if any(x <= 0 for x in (*row_x, *col_x)):
        raise CertificateError("all cross-Loewner offsets must be positive")
    if list(row_x) != sorted(row_x) or len(set(row_x)) != len(row_x):
        raise CertificateError("row offsets must be strictly increasing")
    if list(col_x) != sorted(col_x) or len(set(col_x)) != len(col_x):
        raise CertificateError("column offsets must be strictly increasing")

    row_u = [x * x for x in row_x]
    col_u = [x * x for x in col_x]
    if set(row_u) & set(col_u):
        raise CertificateError(
            "row and column squared nodes must be disjoint in a value-only certificate"
        )

    row_j = [j_value(zeros, x, height) for x in row_x]
    col_j = [j_value(zeros, x, height) for x in col_x]
    return [
        [
            (row_j[i] - col_j[j]) / (row_u[i] - col_u[j])
            for j in range(len(col_x))
        ]
        for i in range(len(row_x))
    ]


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise CertificateError("determinant requires a nonempty square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    result = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column] / pivot_value
            for index in range(column + 1, size):
                work[row][index] -= factor * work[column][index]
            work[row][column] = Fraction(0)
    return result if sign > 0 else -result


def parse_fraction_list(value: Any, name: str) -> list[Fraction]:
    if not isinstance(value, list) or not value:
        raise CertificateError(f"{name} must be a nonempty array")
    return [parse_fraction(item, f"{name}[{index}]") for index, item in enumerate(value)]


def parse_claimed_matrix(value: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(value, list) or not value:
        raise CertificateError(f"{name} must be a nonempty array")
    width = None
    matrix: list[list[Fraction]] = []
    for row_index, row in enumerate(value):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{row_index}] must be a nonempty array")
        parsed = [
            parse_fraction(item, f"{name}[{row_index}][{column_index}]")
            for column_index, item in enumerate(row)
        ]
        if width is None:
            width = len(parsed)
        if len(parsed) != width:
            raise CertificateError(f"{name} rows must have equal length")
        matrix.append(parsed)
    return matrix


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    if data.get("kind") != "finite-zero-derivative-free-controls":
        raise CertificateError("unsupported synthetic certificate kind")

    zeros = parse_zero_multiset(data.get("zeros"))
    height = parse_fraction(data.get("height"), "height")

    scalar_data = data.get("negative_secant")
    if not isinstance(scalar_data, dict):
        raise CertificateError("negative_secant must be an object")
    left_x = parse_fraction(scalar_data.get("left_x"), "negative_secant.left_x")
    right_x = parse_fraction(scalar_data.get("right_x"), "negative_secant.right_x")
    left_re = real_f(zeros, left_x, height)
    right_re = real_f(zeros, right_x, height)
    scalar_secant = secant(zeros, left_x, right_x, height)
    scalar_claimed = scalar_data.get("claimed")
    if not isinstance(scalar_claimed, dict):
        raise CertificateError("negative_secant.claimed must be an object")
    if parse_fraction(scalar_claimed.get("left_re_f"), "claimed.left_re_f") != left_re:
        raise CertificateError("claimed left Re(F) mismatch")
    if parse_fraction(scalar_claimed.get("right_re_f"), "claimed.right_re_f") != right_re:
        raise CertificateError("claimed right Re(F) mismatch")
    if parse_fraction(scalar_claimed.get("secant"), "claimed.secant") != scalar_secant:
        raise CertificateError("claimed scalar secant mismatch")
    scalar_status = (
        "SYNTHETIC_POSITIVE_VALUES_NEGATIVE_SECANT"
        if left_re > 0 and right_re > 0 and scalar_secant < 0
        else "SYNTHETIC_SCALAR_CONTROL_NOT_SEPARATED"
    )
    if scalar_claimed.get("status") != scalar_status:
        raise CertificateError("claimed scalar status mismatch")

    divided_data = data.get("divided_difference")
    if not isinstance(divided_data, dict):
        raise CertificateError("divided_difference must be an object")
    divided_x = parse_fraction_list(divided_data.get("x_nodes"), "divided_difference.x_nodes")
    divided = divided_difference(zeros, divided_x, height)
    divided_order = len(divided_x) - 1
    divided_claimed = divided_data.get("claimed")
    if not isinstance(divided_claimed, dict):
        raise CertificateError("divided_difference.claimed must be an object")
    if parse_fraction(divided_claimed.get("value"), "divided claimed value") != divided:
        raise CertificateError("claimed divided difference mismatch")
    rh_signed_value = divided if divided_order % 2 == 1 else -divided
    divided_status = (
        "SYNTHETIC_DIVIDED_DIFFERENCE_SIGN_VIOLATION"
        if rh_signed_value < 0
        else "SYNTHETIC_DIVIDED_DIFFERENCE_CONTROL_NOT_SEPARATED"
    )
    if divided_claimed.get("status") != divided_status:
        raise CertificateError("claimed divided-difference status mismatch")

    loewner_data = data.get("cross_loewner")
    if not isinstance(loewner_data, dict):
        raise CertificateError("cross_loewner must be an object")
    row_x = parse_fraction_list(loewner_data.get("row_x"), "cross_loewner.row_x")
    col_x = parse_fraction_list(loewner_data.get("col_x"), "cross_loewner.col_x")
    matrix = cross_loewner(zeros, row_x, col_x, height)
    if len(matrix) != len(matrix[0]):
        raise CertificateError("committed cross-Loewner control must be square")
    det = determinant(matrix)
    claimed_matrix = parse_claimed_matrix(
        loewner_data.get("claimed_entries"), "cross_loewner.claimed_entries"
    )
    if claimed_matrix != matrix:
        raise CertificateError("claimed cross-Loewner entries mismatch")
    claimed_det = parse_fraction(
        loewner_data.get("claimed_determinant"),
        "cross_loewner.claimed_determinant",
    )
    if claimed_det != det:
        raise CertificateError("claimed cross-Loewner determinant mismatch")
    loewner_status = (
        "SYNTHETIC_POSITIVE_ENTRIES_NEGATIVE_MINOR"
        if all(value > 0 for row in matrix for value in row) and det < 0
        else "SYNTHETIC_LOEWNER_CONTROL_NOT_SEPARATED"
    )
    if loewner_data.get("status") != loewner_status:
        raise CertificateError("claimed cross-Loewner status mismatch")

    return {
        "schema": SCHEMA,
        "scalar_status": scalar_status,
        "left_re_f": fraction_json(left_re),
        "right_re_f": fraction_json(right_re),
        "scalar_secant": fraction_json(scalar_secant),
        "divided_difference_order": divided_order,
        "divided_difference": fraction_json(divided),
        "divided_status": divided_status,
        "cross_loewner_entries": [
            [fraction_json(value) for value in row] for row in matrix
        ],
        "cross_loewner_determinant": fraction_json(det),
        "cross_loewner_status": loewner_status,
        "proof_boundary": "finite synthetic zero model only; not a Riemann-xi evaluation",
    }


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify_certificate(load_json(args.certificate))
    except CertificateError as exc:
        print(json.dumps({"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
