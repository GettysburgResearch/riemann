#!/usr/bin/env python3
"""Finite exact regressions for L-91410--L-91412.

This script verifies only elementary finite algebra and rational inequalities.
It does not evaluate zeta, construct the missing source ports, prove any
Stieltjes measure theorem, or prove RH.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [i for i, flag in enumerate(sieve) if flag]


def prove_log2_lt_three_quarters(terms: int = 12) -> bool:
    # log 2 = sum_{k>=1} 1/(k 2^k).
    partial = sum(Fraction(1, k * 2**k) for k in range(1, terms + 1))
    # For k>=terms+1, 1/k <= 1/(terms+1).
    tail_upper = Fraction(1, (terms + 1) * 2**terms)
    return partial + tail_upper < Fraction(3, 4)


def main() -> dict[str, object]:
    # Route I: every rough least prime immediately enters the next reset scale.
    c0_lower = Fraction(1844367547103, 10**14)
    first_entrance_checks = 0
    for p in primes_upto(2000):
        if p >= 67:
            assert Fraction(1, p) < c0_lower
            first_entrance_checks += 1

    # Route II: exact two-channel Stieltjes feature identity.
    rs = [Fraction(1, 3), Fraction(2, 5), Fraction(7, 4)]
    ts = [Fraction(0), Fraction(1, 2), Fraction(3), Fraction(11, 7)]
    stieltjes_feature_checks = 0
    for r in rs:
        for s in rs:
            for t in ts:
                h_r = r / (r * r + t)
                h_s = s / (s * s + t)
                lhs = (h_r + h_s) / (r + s)
                rhs = (
                    r / (r * r + t) * s / (s * s + t)
                    + t / ((r * r + t) * (s * s + t))
                )
                assert lhs == rhs
                stieltjes_feature_checks += 1

    # Route II: exact two-point determinant factorization.
    ell = [Fraction(1, 5), Fraction(2, 7), Fraction(3, 8)]
    two_point_determinant_checks = 0
    for i, r in enumerate(rs):
        for j, s in enumerate(rs):
            if r == s:
                continue
            er, es = ell[i], ell[j]
            lhs = er / r * es / s - ((er + es) / (r + s)) ** 2
            qr, qs = er / r, es / s
            rhs = (qr - qs) * (s * es - r * er) / (r + s) ** 2
            assert lhs == rhs
            two_point_determinant_checks += 1

    # Route III: exact two-Green boundary-jet identity for a synthetic source.
    source = {
        1: Fraction(1),
        2: Fraction(3, 5),
        3: Fraction(2, 7),
        5: Fraction(4, 11),
    }
    c = Fraction(1, 13)
    two_green_identity_checks = 0
    for q in range(1, 9):
        z = sum(value / n ** (1 + q) for n, value in source.items())
        lhs = Fraction(q + 4, q) * (z - c / q)
        atoms = sum(
            value / n ** (1 + q)
            for n, value in source.items()
            if n >= 2
        )
        rhs = (
            1
            + atoms
            - c / q
            + Fraction(4, q) * (z - c / q)
        )
        assert lhs == rhs
        two_green_identity_checks += 1

    assert prove_log2_lt_three_quarters()

    return {
        "classification": "PASS_X_91410_THREE_FRONT_EXACT_ALGEBRA",
        "first_entrance_prime_checks": first_entrance_checks,
        "stieltjes_feature_checks": stieltjes_feature_checks,
        "two_point_determinant_checks": two_point_determinant_checks,
        "two_green_identity_checks": two_green_identity_checks,
        "log2_lt_three_quarters_certified": True,
        "route_I_matrix_port_identified": False,
        "route_II_stieltjes_measure_constructed": False,
        "route_III_completed_colligation_constructed": False,
        "rh_proved": False,
        "scope": (
            "finite rational algebra, first-entrance scale checks, and an "
            "elementary rational upper bound for log(2) only"
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text, end="")
