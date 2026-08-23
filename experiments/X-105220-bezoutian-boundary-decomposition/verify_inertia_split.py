#!/usr/bin/env python3
"""Exact replay for L-105218 and R-105203.

The checker verifies abstract rational block congruences and principal-minor
separators. It does not prove the Xi exhaustion, PRES105220, BRP105220, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

Q = Fraction


def transpose(a: list[list[Q]]) -> list[list[Q]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    assert len(a[0]) == len(b)
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def add(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def negate(a: list[list[Q]]) -> list[list[Q]]:
    return [[-x for x in row] for row in a]


def diagonal(values: list[Q]) -> list[list[Q]]:
    n = len(values)
    return [[values[i] if i == j else Q(0) for j in range(n)] for i in range(n)]


def identity(n: int) -> list[list[Q]]:
    return diagonal([Q(1)] * n)


def block(a: list[list[Q]], b: list[list[Q]], c: list[list[Q]], d: list[list[Q]]) -> list[list[Q]]:
    return [row_a + row_b for row_a, row_b in zip(a, b)] + [row_c + row_d for row_c, row_d in zip(c, d)]


def determinant(a: list[list[Q]]) -> Q:
    matrix = [list(row) for row in a]
    n = len(matrix)
    det = Q(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if matrix[row][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            det = -det
        pivot_value = matrix[col][col]
        det *= pivot_value
        for row in range(col + 1, n):
            if matrix[row][col] == 0:
                continue
            factor = matrix[row][col] / pivot_value
            for j in range(col, n):
                matrix[row][j] -= factor * matrix[col][j]
    return det


def check_schur_congruences() -> int:
    fixtures = [
        (
            [Q(2), Q(-3)],
            [Q(-1, 2), Q(5, 3)],
            [[Q(1), Q(2)], [Q(-2), Q(1)], [Q(3, 2), Q(-1, 3)]],
            [[Q(3), Q(1), Q(-1)], [Q(1), Q(4), Q(2)], [Q(-1), Q(2), Q(5)]],
        ),
        (
            [Q(-1), Q(4), Q(5)],
            [Q(2), Q(-3, 2), Q(7, 4)],
            [[Q(1), Q(0), Q(-1)], [Q(2), Q(3), Q(1)]],
            [[Q(6), Q(-2)], [Q(-2), Q(3)]],
        ),
    ]
    checks = 0
    for h_values, d_values, q_matrix, r_matrix in fixtures:
        h = diagonal(h_values)
        d = diagonal(d_values)
        q = q_matrix
        ht = h
        qt = transpose(q)

        a = negate(matmul(matmul(h, d), ht))
        upper_right = negate(matmul(matmul(h, d), qt))
        lower_left = transpose(upper_right)
        qdq = matmul(matmul(q, d), qt)
        lower_right = add(r_matrix, negate(qdq))
        b_matrix = block(a, upper_right, lower_left, lower_right)

        h_inv = diagonal([Q(1) / value for value in h_values])
        minus_h_inv_qt = negate(matmul(h_inv, qt))
        zero = [[Q(0) for _ in range(len(h_values))] for _ in range(len(r_matrix))]
        p_matrix = block(identity(len(h_values)), minus_h_inv_qt, zero, identity(len(r_matrix)))
        congruent = matmul(matmul(transpose(p_matrix), b_matrix), p_matrix)

        expected_zero_ur = [[Q(0) for _ in range(len(r_matrix))] for _ in range(len(h_values))]
        expected_zero_ll = transpose(expected_zero_ur)
        expected = block(a, expected_zero_ur, expected_zero_ll, r_matrix)
        assert congruent == expected
        checks += sum(len(row) for row in congruent)
    return checks


def check_order_four_separator() -> int:
    r = Q(-2, 5)
    m4 = [[Q(1) if i == j else r for j in range(4)] for i in range(4)]
    checks = 0

    for size in (1, 2, 3):
        principal = [row[:size] for row in m4[:size]]
        expected = {1: Q(1), 2: Q(21, 25), 3: Q(49, 125)}[size]
        assert determinant(principal) == expected
        checks += 1

    assert determinant(m4) == Q(-343, 625)
    checks += 1

    ones = [Q(1)] * 4
    quadratic = sum((ones[i] * m4[i][j] * ones[j] for i in range(4) for j in range(4)), Q(0))
    assert quadratic == Q(-4, 5)
    checks += 1
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "critical_node_schur_congruence_checks": check_schur_congruences(),
        "order_four_separator_checks": check_order_four_separator(),
    }
    result = {
        "verdict": "PASS_X_105218_CRITICAL_NODE_INERTIA_SPLIT",
        "arithmetic_class": "EXACT_RATIONAL_BLOCK_CONGRUENCE",
        "counts": counts,
        "pres105220_proved": False,
        "brp105220_proved": False,
        "rh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
