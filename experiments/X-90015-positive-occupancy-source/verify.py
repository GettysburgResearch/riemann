#!/usr/bin/env python3
"""Exact finite-algebra replay for L-90015--L-90017.

This checker verifies formal prime-log coefficients only.  It does not certify
Mellin inversion, the aggregate mean-age inequality, or RH.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

MAX_ENDPOINT = 500


def primes_upto(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for k in range(p * p, n + 1, p):
                is_prime[k] = False
    return [p for p in range(2, n + 1) if is_prime[p]]


def factor(n: int) -> Counter[int]:
    out: Counter[int] = Counter()
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


def occupancy_deficit_at_integer(q: int, n: int) -> Fraction:
    r = n % q
    return Fraction(1) if r == 0 else Fraction(r, q)


def main() -> None:
    primes = primes_upto(MAX_ENDPOINT)
    prime_rows = 0
    lambda_rows = 0
    slope_rows = 0

    for n in range(2, MAX_ENDPOINT + 1):
        radical_prefix_coefficients: Counter[int] = Counter()
        for m in range(1, n + 1):
            for p in factor(m):
                radical_prefix_coefficients[p] += 1
        radical_n = set(factor(n))

        for p in primes:
            if p > n:
                break

            # L-90016.19--20, coefficient of log p.
            lhs = occupancy_deficit_at_integer(p, n)
            rhs = (
                Fraction(n, p)
                - radical_prefix_coefficients[p]
                + (1 if p in radical_n else 0)
            )
            assert lhs == rhs, (n, p, lhs, rhs)
            prime_rows += 1

            # L-90017.7--8, coefficient of log p in the cell slope.
            lhs_slope = Fraction(-(p - 1), p) if n % p == 0 else Fraction(1, p)
            rhs_slope = Fraction(1, p) - (1 if n % p == 0 else 0)
            assert lhs_slope == rhs_slope
            slope_rows += 1

            # L-90016.21, coefficient of log p in the full Lambda source.
            powers: list[int] = []
            q = p
            while q <= n:
                powers.append(q)
                q *= p
            lhs_lambda = sum(
                (occupancy_deficit_at_integer(q, n) for q in powers),
                Fraction(),
            )
            vp_factorial = sum(n // q for q in powers)
            vp_n = factor(n)[p]
            rhs_lambda = (
                n * sum((Fraction(1, q) for q in powers), Fraction())
                - vp_factorial
                + vp_n
            )
            assert lhs_lambda == rhs_lambda, (n, p, lhs_lambda, rhs_lambda)
            lambda_rows += 1

    result = {
        "schema": "X-90015-positive-occupancy-source-v1",
        "classification": "PASS_EXACT_OCCUPANCY_SOURCE_FINITE_ALGEBRA",
        "max_endpoint": MAX_ENDPOINT,
        "prime_source_coefficient_rows": prime_rows,
        "lambda_source_coefficient_rows": lambda_rows,
        "cell_slope_rows": slope_rows,
        "does_not_prove": [
            "analytic Mellin identity",
            "aggregate mean-age inequality",
            "Riemann Hypothesis",
        ],
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["sha256_without_digest"] = hashlib.sha256(canonical).hexdigest()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"

    output = Path(__file__).with_name("results") / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
