#!/usr/bin/env python3
"""Exact rational replay for L-105390 and T-105390.

The checker verifies finite reciprocal-square Vandermonde Gram identities and
the exponent balance used in the growing-prefix theorem. It does not evaluate
Xi or prove the analytic approximation estimates.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

Q = Fraction


def determinant(a: list[list[Q]]) -> Q:
    m = [row[:] for row in a]
    n = len(m)
    det = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            det = -det
        pv = m[col][col]
        det *= pv
        for r in range(col + 1, n):
            if m[r][col] == 0:
                continue
            factor = m[r][col] / pv
            for j in range(col, n):
                m[r][j] -= factor * m[col][j]
    return det


def atom(parity: str, j: int) -> tuple[Q, Q]:
    """Rationally rescaled tangent/cotangent atom; pi factors are positive."""
    if parity == "odd":
        d = 2 * j + 1
        return Q(8, d * d), Q(4, d * d)
    assert parity == "even"
    return Q(2, j * j), Q(1, j * j)


def gram(atoms: list[tuple[Q, Q]], k: int, shift: int) -> list[list[Q]]:
    return [
        [
            sum((w * s ** (r + c + shift) for w, s in atoms), Q(0))
            for c in range(k)
        ]
        for r in range(k)
    ]


def vandermonde_det(locations: list[Q]) -> Q:
    out = Q(1)
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            out *= locations[j] - locations[i]
    return out


def check_vandermonde_grams() -> int:
    checks = 0
    for parity in ("odd", "even"):
        for k in range(1, 5):
            for shift in (0, 1):
                for J in (5, 11, 23):
                    indices = list(range(J + 1, J + k + 1))
                    atoms = [atom(parity, j) for j in indices]
                    matrix = gram(atoms, k, shift)
                    det_matrix = determinant(matrix)
                    locations = [s for _, s in atoms]
                    expected = vandermonde_det(locations) ** 2
                    for weight, location in atoms:
                        expected *= weight * location**shift

                    assert det_matrix == expected
                    checks += 1
                    assert det_matrix > 0
                    checks += 1

                    matrix_trace = sum((matrix[i][i] for i in range(k)), Q(0))
                    assert matrix_trace > 0
                    checks += 1

                    lower_proxy = det_matrix / matrix_trace ** (k - 1)
                    assert lower_proxy > 0
                    checks += 1
    return checks


def check_growth_exponents() -> int:
    checks = 0
    for k in range(1, 5):
        d = 3 * k * (k - 1) + 4
        gamma = Q(1, 4 * (d + 1))
        assert gamma * d < Q(1, 2)
        checks += 1
        assert gamma * (d + 1) < Q(1, 2)
        checks += 1
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "vandermonde_gram_checks": check_vandermonde_grams(),
        "growth_exponent_checks": check_growth_exponents(),
    }
    total = sum(counts.values())
    assert total == 200

    result = {
        "verdict": "PASS_X_105390_GROWING_PREFIX_CAPACITY",
        "arithmetic_class": "EXACT_RATIONAL_VANDERMONDE_TAIL",
        "checks": total,
        "counts": counts,
        "xi_real_saddle_estimate_replayed": False,
        "xi_growing_cell_approximation_replayed": False,
        "complete_critical_tail_proved": False,
        "rh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print("PASS_X_105390_GROWING_PREFIX_CAPACITY")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
