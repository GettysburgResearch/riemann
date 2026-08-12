#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import comb
from pathlib import Path
import json


def beta_integer(n: int, q: int) -> Fraction:
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def beta_real(n: int, q: Fraction) -> Fraction:
    m = n + 1
    a = ceil_fraction(Fraction(m, 1) / q) - 1
    if a <= 0:
        return Fraction(0)
    return Fraction(a, m) * ((a + 1) * q - m)


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def main():
    integer_beta_checks = 0
    affine_beta_checks = 0
    atomized_checks = 0
    binomial_injection_checks = 0

    for n in range(1, 101):
        for q in range(2, n + 2):
            assert beta_real(n, Fraction(q)) == beta_integer(n, q)
            integer_beta_checks += 1

    rational_columns = [
        Fraction(a, b)
        for b in range(1, 8)
        for a in range(1, 140)
    ]

    for m in (2, 3, 5, 7, 59):
        for n in range(1, 50):
            lifted = m * (n + 1) - 1
            for q in rational_columns:
                assert beta_real(lifted, m * q) == beta_real(n, q)
                affine_beta_checks += 1

            for j in range(n + 1):
                for r in range(m if m < 8 else 8):
                    J = m * j + r
                    for q in range(2, n + 2):
                        assert carry(lifted, J, m * q) == carry(n, j, q)
                        atomized_checks += 1

    for m in range(2, 9):
        for n in range(1, 25):
            N = m * (n + 1) - 1
            for j in range(n + 1):
                rhs = comb(n, j) ** m
                for r in range(m):
                    assert comb(N, m * j + r) >= rhs
                    binomial_injection_checks += 1

    result = {
        "classification": "PASS_AFFINE_PASCAL_DILATION_AND_SCORE_AMPLIFICATION",
        "integer_beta_checks": integer_beta_checks,
        "affine_real_column_checks": affine_beta_checks,
        "atomized_carry_checks": atomized_checks,
        "binomial_injection_checks": binomial_injection_checks,
        "tested_lift_factors": [2, 3, 5, 7, 59],
        "scope": (
            "Exact integer and Fraction arithmetic. The checker verifies the "
            "continuous-column Pascal extension, affine covariance, atomized "
            "carry covariance, and the finite binomial inequalities underlying "
            "G_(m(n+1)-1) >= m G_n. The general proofs are in L-91318."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
