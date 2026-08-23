#!/usr/bin/env python3
"""Exact rational replay for L/T-105360.

The checker authenticates finite atomic moment transport, the parity-split
Stieltjes Gram factorization, and the positive-terminal-slope firewall. It does
not evaluate Xi or prove CRVH105330, TAIR105360, OASH105350, the moving saddle,
or RH.
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
    assert a and b and len(a[0]) == len(b)
    return [
        [
            sum((a[i][r] * b[r][j] for r in range(len(b))), Q(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def diagonal(values: list[Q]) -> list[list[Q]]:
    n = len(values)
    return [[values[i] if i == j else Q(0) for j in range(n)] for i in range(n)]


def determinant(a: list[list[Q]]) -> Q:
    matrix = [list(row) for row in a]
    n = len(matrix)
    out = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if matrix[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            out = -out
        pivot_value = matrix[col][col]
        out *= pivot_value
        for row in range(col + 1, n):
            if matrix[row][col] == 0:
                continue
            factor = matrix[row][col] / pivot_value
            for j in range(col, n):
                matrix[row][j] -= factor * matrix[col][j]
    return out


def moments(atoms: list[tuple[Q, Q]], maximum: int) -> list[Q]:
    """Atoms are (support point s, nonnegative weight w)."""
    return [
        sum((weight * support**n for support, weight in atoms), Q(0))
        for n in range(maximum + 1)
    ]


def hankel(sequence: list[Q], size: int, shift: int = 0) -> list[list[Q]]:
    return [
        [sequence[r + s + shift] for s in range(size)]
        for r in range(size)
    ]


def vandermonde(atoms: list[tuple[Q, Q]], size: int) -> list[list[Q]]:
    return [[support**r for r in range(size)] for support, _ in atoms]


def stieltjes_function(z: Q, atoms: list[tuple[Q, Q]]) -> Q:
    return z * sum(
        (weight / (Q(1) - support * z * z) for support, weight in atoms),
        Q(0),
    )


def check_nested_transport() -> tuple[dict[str, int], dict[str, object]]:
    # A positive outer boundary measure.
    outer_atoms = [
        (Q(0), Q(1, 5)),
        (Q(1, 9), Q(2, 7)),
    ]

    # Two crossed critical pairs. The exact weights are
    # w_c=-2*rho_c/c^2 and supports are s_c=1/c^2.
    crossed = [
        {"c": Q(2), "rho": Q(-3, 8)},
        {"c": Q(3), "rho": Q(-1, 2)},
    ]
    crossed_atoms = [
        (Q(1) / item["c"] ** 2, -Q(2) * item["rho"] / item["c"] ** 2)
        for item in crossed
    ]
    assert crossed_atoms == [(Q(1, 4), Q(3, 16)), (Q(1, 9), Q(1, 9))]
    assert all(weight >= 0 for _, weight in crossed_atoms)

    inner_atoms = outer_atoms + crossed_atoms
    outer_beta = moments(outer_atoms, 7)
    crossed_beta = moments(crossed_atoms, 7)
    inner_beta = moments(inner_atoms, 7)

    moment_checks = 0
    for n in range(8):
        assert inner_beta[n] == outer_beta[n] + crossed_beta[n]
        moment_checks += 1

    function_checks = 0
    for z in [Q(-1, 2), Q(-1, 3), Q(1, 5), Q(2, 5)]:
        assert stieltjes_function(z, inner_atoms) == (
            stieltjes_function(z, outer_atoms)
            + stieltjes_function(z, crossed_atoms)
        )
        function_checks += 1

    gram_checks = 0
    for size in range(1, 4):
        v = vandermonde(inner_atoms, size)
        even = hankel(inner_beta, size)
        odd = hankel(inner_beta, size, shift=1)
        expected_even = matmul(
            transpose(v),
            matmul(diagonal([weight for _, weight in inner_atoms]), v),
        )
        expected_odd = matmul(
            transpose(v),
            matmul(
                diagonal([support * weight for support, weight in inner_atoms]),
                v,
            ),
        )
        assert even == expected_even
        assert odd == expected_odd
        gram_checks += 2 * size * size
        assert determinant(even) >= 0
        assert determinant(odd) >= 0

    counts = {
        "nested_moment_transport_checks": moment_checks,
        "nested_function_transport_checks": function_checks,
        "stieltjes_gram_checks": gram_checks,
    }
    fixture = {
        "outer_atoms": [
            {"s": str(support), "weight": str(weight)}
            for support, weight in outer_atoms
        ],
        "crossed_critical_pairs": [
            {
                "c": str(item["c"]),
                "rho": str(item["rho"]),
                "s": str(atom[0]),
                "weight": str(atom[1]),
            }
            for item, atom in zip(crossed, crossed_atoms)
        ],
        "inner_beta_0_to_7": [str(value) for value in inner_beta],
    }
    return counts, fixture


def check_terminal_slope_firewall() -> tuple[int, dict[str, object]]:
    # H(z)=z-z^3 has positive slope at zero, but the complete origin moment
    # hierarchy fails in the second confluent direction.
    sequence = [Q(1), Q(0), Q(-1)]
    matrix = hankel(sequence, 2)
    assert sequence[0] > 0
    assert matrix == [[Q(1), Q(0)], [Q(0), Q(-1)]]
    assert determinant(matrix) == Q(-1)
    return 3, {
        "function": "z-z^3",
        "terminal_slope": "1",
        "L2": [[str(value) for value in row] for row in matrix],
        "L2_determinant": "-1",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    transport_counts, transport_fixture = check_nested_transport()
    firewall_checks, firewall_fixture = check_terminal_slope_firewall()
    counts = {
        **transport_counts,
        "terminal_slope_firewall_checks": firewall_checks,
    }
    result = {
        "verdict": "PASS_X_105360_TERMINAL_STIELTJES_TRANSPORT",
        "arithmetic_class": "EXACT_RATIONAL_ATOMIC_MOMENT_TRANSPORT",
        "checks": sum(counts.values()),
        "counts": counts,
        "fixtures": {
            "nested_transport": transport_fixture,
            "terminal_slope_firewall": firewall_fixture,
        },
        "crvh105330_proved_for_xi": False,
        "tair105360_proved_for_xi": False,
        "oash105350_proved_for_xi": False,
        "moving_saddle_proved": False,
        "rh_established": False,
    }

    assert result["checks"] == 43
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
