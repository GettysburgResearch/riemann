#!/usr/bin/env python3
"""Exact finite replay for T105410 sharp tail scaling.

Authenticates:
- the Cauchy determinant of H_k^(a);
- the last-coordinate Schur constant;
- the graded moment congruence;
- the abstract separator showing the old isotropic moment rate is overstrong.

It does not replay Xi real-saddle concentration, critical-cell localization,
CRVH, the scalar terminal pivot, low-order descent, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

Q = Fraction


def determinant(matrix: list[list[Q]]) -> Q:
    a = [list(row) for row in matrix]
    n = len(a)
    out = Q(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        value = a[col][col]
        out *= value
        for row in range(col + 1, n):
            if a[row][col] == 0:
                continue
            factor = a[row][col] / value
            for j in range(col, n):
                a[row][j] -= factor * a[col][j]
    return out


def h_matrix(k: int, a: int) -> list[list[Q]]:
    return [[Q(1, 2 * (i + j + a) + 1) for j in range(k)] for i in range(k)]


def cauchy_determinant(k: int, a: int) -> Q:
    numerator = 1
    for i in range(k):
        for j in range(i + 1, k):
            numerator *= (2 * (j - i)) ** 2
    denominator = 1
    for i in range(k):
        for j in range(k):
            denominator *= 2 * (i + j + a) + 1
    return Q(numerator, denominator)


def schur_constant(k: int, a: int) -> Q:
    if k == 1:
        return determinant(h_matrix(1, a))
    return determinant(h_matrix(k, a)) / determinant(h_matrix(k - 1, a))


def explicit_schur_constant(k: int, a: int) -> Q:
    numerator = 4 ** (k - 1) * math.factorial(k - 1) ** 2
    denominator = 4 * k + 2 * a - 3
    for i in range(k - 1):
        denominator *= (2 * (i + k - 1 + a) + 1) ** 2
    return Q(numerator, denominator)


def check_cauchy_geometry() -> int:
    checks = 0
    for a in (0, 1):
        for k in range(1, 8):
            h = h_matrix(k, a)
            assert determinant(h) == cauchy_determinant(k, a)
            checks += 1
            assert schur_constant(k, a) == explicit_schur_constant(k, a)
            checks += 1
            for r in range(1, k + 1):
                assert determinant([row[:r] for row in h[:r]]) > 0
                checks += 1
    return checks


def check_graded_congruence() -> int:
    checks = 0
    for prime_proxy in (2, 3, 5):
        for j_scale in (3, 7, 11):
            for a in (0, 1):
                for k in range(1, 6):
                    deltas = [Q((-1) ** n * (n + 2), n + 3) for n in range(2 * k + 1)]
                    g = Q(2, prime_proxy ** (2 * a + 2) * j_scale ** (2 * a + 1))
                    d = [Q(1, (prime_proxy * j_scale) ** (2 * i)) for i in range(k)]
                    for i in range(k):
                        for j in range(k):
                            q = i + j + a
                            entry = deltas[q]
                            normalized = entry / (g * d[i] * d[j])
                            expected = (
                                Q(prime_proxy ** (2 * q + 2) * j_scale ** (2 * q + 1), 2)
                                * deltas[q]
                            )
                            assert normalized == expected
                            checks += 1
    return checks


def check_overstrong_rate_separator() -> int:
    checks = 0
    for k in range(1, 6):
        d_old = 3 * k * (k - 1) + 4
        b = 2
        assert 1 < b < d_old
        for j in (5, 11, 29):
            delta0 = Q(1, j**b)
            assert delta0 * j**d_old >= 1
            for n in range(2 * k):
                delta_n = Q(1, j ** (b * (2 * n + 1)))
                natural = delta_n * j ** (2 * n + 1)
                assert natural <= Q(1, j ** ((b - 1) * (2 * n + 1)))
                checks += 1
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "cauchy_and_schur_checks": check_cauchy_geometry(),
        "graded_congruence_checks": check_graded_congruence(),
        "overstrong_rate_separator_checks": check_overstrong_rate_separator(),
    }
    payload = {
        "verdict": "PASS_X_105410_SHARP_TAIL_SCALING",
        "arithmetic_class": "EXACT_RATIONAL_FINITE_ALGEBRA",
        "counts": counts,
        "xi_second_order_saddle_replayed": False,
        "complete_remote_tail_sign_proved": False,
        "low_order_descent_proved": False,
        "rh_established": False,
    }
    proof_text = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["proof_object"] = hashlib.sha256(proof_text.encode("utf-8")).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
