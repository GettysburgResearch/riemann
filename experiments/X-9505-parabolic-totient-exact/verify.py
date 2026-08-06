#!/usr/bin/env python3
"""Exact Fraction-only verifier for L-9510.

Checks the rational-cell Bernoulli formula and the complete direct/Mobius
identity for every integer cutoff in a finite range. It does not verify the
Mertens asymptotic or RH.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "riemann.parabolic-totient-exact-regression.v1"


def phi_sieve(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def mobius_sieve(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue
        for multiple in range(2 * p, limit + 1, p):
            is_prime[multiple] = False
        for multiple in range(p, limit + 1, p):
            mu[multiple] *= -1
        if p * p <= limit:
            for multiple in range(p * p, limit + 1, p * p):
                mu[multiple] = 0
    mu[0] = 0
    return mu


def fractional_part(value: Fraction) -> Fraction:
    return Fraction(value.numerator % value.denominator, value.denominator)


def bernoulli_2(u: Fraction) -> Fraction:
    return u**2 - u + Fraction(1, 6)


def bernoulli_3(u: Fraction) -> Fraction:
    return u**3 - Fraction(3, 2) * u**2 + Fraction(1, 2) * u


def strict_upper_integer(y: Fraction) -> int:
    return (y.numerator + y.denominator - 1) // y.denominator - 1


def cell_sum_direct(y: Fraction) -> Fraction:
    if y <= 1:
        return Fraction(0)
    return sum(
        1 - Fraction(m * m, 1) / (y * y)
        for m in range(1, strict_upper_integer(y) + 1)
    )


def cell_sum_bernoulli(y: Fraction) -> Fraction:
    if y <= 1:
        return Fraction(0)
    u = fractional_part(y)
    return (
        Fraction(2, 3) * y
        - Fraction(1, 2)
        - bernoulli_2(u) / y
        + bernoulli_3(u) / (3 * y**2)
    )


def parabolic_totient_direct(x: int, phi: list[int]) -> Fraction:
    return sum(
        Fraction(phi[n], n) * (1 - Fraction(n * n, x * x))
        for n in range(1, x)
    ) / x


def parabolic_mobius_decomposition(x: int, mu: list[int]) -> Fraction:
    return (
        Fraction(2, 3) * sum(Fraction(mu[d], d * d) for d in range(1, x))
        - Fraction(1, 2 * x) * sum(Fraction(mu[d], d) for d in range(1, x))
        - Fraction(1, x * x) * sum(
            mu[d] * bernoulli_2(fractional_part(Fraction(x, d)))
            for d in range(1, x)
        )
        + Fraction(1, 3 * x**3) * sum(
            mu[d] * d * bernoulli_3(fractional_part(Fraction(x, d)))
            for d in range(1, x)
        )
    )


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical_digest(body: dict[str, Any]) -> str:
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verify(limit: int) -> dict[str, Any]:
    if limit < 2:
        raise ValueError("limit must be at least two")

    controls = [
        Fraction(11, 10),
        Fraction(2),
        Fraction(23, 10),
        Fraction(107, 10),
        Fraction(501, 5),
    ]
    for y in controls:
        if cell_sum_direct(y) != cell_sum_bernoulli(y):
            raise AssertionError(f"parabolic cell identity failed at y={y}")

    phi = phi_sieve(limit)
    mu = mobius_sieve(limit)
    retained = {2, 3, 5, 10, 20, 50, 100, limit}
    rows: list[dict[str, Any]] = []
    for x in range(2, limit + 1):
        direct = parabolic_totient_direct(x, phi)
        decomposed = parabolic_mobius_decomposition(x, mu)
        if direct != decomposed:
            raise AssertionError(f"parabolic direct/Mobius identity failed at x={x}")
        if x in retained:
            rows.append({"x": x, "parabolic_totient_value": fraction_json(direct)})

    body: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "PASS_EXACT_L9510_PARABOLIC_BERNOULLI_MOBIUS_IDENTITY",
        "verified_x_range": [2, limit],
        "rational_cell_controls": [fraction_json(y) for y in controls],
        "rows": rows,
        "proof_boundary": (
            "Exact finite algebra only. The Mertens estimate, asymptotic error, "
            "and RH are outside this verifier."
        ),
    }
    body["proof_object_sha256"] = canonical_digest(body)
    return body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.limit)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
