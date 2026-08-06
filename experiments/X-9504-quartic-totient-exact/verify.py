#!/usr/bin/env python3
"""Exact Fraction-only verifier for L-9508.

It checks:
1. the quartic finite-cell Bernoulli identity at rational y;
2. the direct totient observable against the finite Möbius/Bernoulli
   decomposition for every integer 2 <= x <= the requested limit.

No transcendental value and no RH assertion enters this verifier.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "riemann.quartic-totient-exact-regression.v1"


def phi_sieve(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi


def mobius_sieve(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for multiple in range(2 * p, limit + 1, p):
            prime[multiple] = False
        for multiple in range(p, limit + 1, p):
            mu[multiple] *= -1
        square = p * p
        if square <= limit:
            for multiple in range(square, limit + 1, square):
                mu[multiple] = 0
    mu[0] = 0
    return mu


def fractional_part(value: Fraction) -> Fraction:
    return Fraction(value.numerator % value.denominator, value.denominator)


def bernoulli_3(u: Fraction) -> Fraction:
    return u**3 - Fraction(3, 2) * u**2 + Fraction(1, 2) * u


def bernoulli_4(u: Fraction) -> Fraction:
    return u**4 - 2 * u**3 + u**2 - Fraction(1, 30)


def bernoulli_5(u: Fraction) -> Fraction:
    return (
        u**5
        - Fraction(5, 2) * u**4
        + Fraction(5, 3) * u**3
        - Fraction(1, 6) * u
    )


def strict_upper_integer(y: Fraction) -> int:
    """Largest integer m satisfying m < y."""
    return (y.numerator + y.denominator - 1) // y.denominator - 1


def cell_sum_direct(y: Fraction) -> Fraction:
    if y <= 1:
        return Fraction(0)
    return sum(
        (1 - Fraction(m * m, 1) / (y * y)) ** 2
        for m in range(1, strict_upper_integer(y) + 1)
    )


def cell_sum_bernoulli(y: Fraction) -> Fraction:
    if y <= 1:
        return Fraction(0)
    u = fractional_part(y)
    return (
        Fraction(8, 15) * y
        - Fraction(1, 2)
        - Fraction(4, 3) * bernoulli_3(u) / y**2
        + bernoulli_4(u) / y**3
        - Fraction(1, 5) * bernoulli_5(u) / y**4
    )


def quartic_totient_direct(x: int, phi: list[int]) -> Fraction:
    return sum(
        Fraction(phi[n], n) * (1 - Fraction(n * n, x * x)) ** 2
        for n in range(1, x)
    ) / x


def quartic_mobius_decomposition(x: int, mu: list[int]) -> Fraction:
    result = Fraction(8, 15) * sum(
        Fraction(mu[d], d * d) for d in range(1, x)
    )
    result -= Fraction(1, 2 * x) * sum(
        Fraction(mu[d], d) for d in range(1, x)
    )
    result -= Fraction(4, 3 * x**3) * sum(
        mu[d] * d * bernoulli_3(fractional_part(Fraction(x, d)))
        for d in range(1, x)
    )
    result += Fraction(1, x**4) * sum(
        mu[d] * d**2 * bernoulli_4(fractional_part(Fraction(x, d)))
        for d in range(1, x)
    )
    result -= Fraction(1, 5 * x**5) * sum(
        mu[d] * d**3 * bernoulli_5(fractional_part(Fraction(x, d)))
        for d in range(1, x)
    )
    return result


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def canonical_digest(body: dict[str, Any]) -> str:
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verify(limit: int) -> dict[str, Any]:
    if limit < 2:
        raise ValueError("limit must be at least two")

    rational_controls = [
        Fraction(11, 10),
        Fraction(2),
        Fraction(23, 10),
        Fraction(107, 10),
        Fraction(501, 5),
    ]
    for y in rational_controls:
        if cell_sum_direct(y) != cell_sum_bernoulli(y):
            raise AssertionError(f"cell identity failed at y={y}")

    phi = phi_sieve(limit)
    mu = mobius_sieve(limit)
    rows: list[dict[str, Any]] = []
    retained = {2, 3, 5, 10, 20, 50, 100, limit}
    for x in range(2, limit + 1):
        direct = quartic_totient_direct(x, phi)
        decomposed = quartic_mobius_decomposition(x, mu)
        if direct != decomposed:
            raise AssertionError(f"totient/Mobius identity failed at x={x}")
        if x in retained:
            rows.append({"x": x, "quartic_totient_value": fraction_json(direct)})

    body: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "PASS_EXACT_L9508_BERNOULLI_MOBIUS_IDENTITY",
        "verified_x_range": [2, limit],
        "rational_cell_controls": [fraction_json(y) for y in rational_controls],
        "rows": rows,
        "proof_boundary": (
            "This is an exact finite algebra regression for L-9508. It does not "
            "verify the asymptotic Mertens bound or RH."
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
