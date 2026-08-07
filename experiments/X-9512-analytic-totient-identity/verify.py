#!/usr/bin/env python3
"""Exact Q[C] replay of L-9512.

C is a formal symbol for 1/zeta(2)=6/pi^2.  The checker never evaluates pi.
It compares the finite parabolic Riesz state with the infinite fractional-part
series after the absolutely convergent tail is collapsed to C.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json


@dataclass(frozen=True)
class Affine:
    rational: Fraction = Fraction(0)
    c_coeff: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Affine":
        if not isinstance(other, Affine):
            other = Affine(Fraction(other))
        return Affine(self.rational + other.rational,
                      self.c_coeff + other.c_coeff)

    __radd__ = __add__

    def __neg__(self) -> "Affine":
        return Affine(-self.rational, -self.c_coeff)

    def __sub__(self, other: object) -> "Affine":
        return self + (-other if isinstance(other, Affine)
                       else -Affine(Fraction(other)))

    def scale(self, q: Fraction) -> "Affine":
        return Affine(q * self.rational, q * self.c_coeff)

    def to_json(self) -> dict[str, dict[str, int]]:
        return {
            "rational": {
                "numerator": self.rational.numerator,
                "denominator": self.rational.denominator,
            },
            "c_coefficient": {
                "numerator": self.c_coeff.numerator,
                "denominator": self.c_coeff.denominator,
            },
        }


def mobius_table(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = n * p
            if m > limit:
                break
            composite[m] = True
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def phi_table(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for n in range(p, limit + 1, p):
                phi[n] -= phi[n] // p
    return phi


def floor_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator


def fractional_part(x: Fraction) -> Fraction:
    return x - floor_fraction(x)


def strict_positive_integer_cutoff(x: Fraction) -> int:
    """Largest positive integer n with n < x."""
    return (x.numerator - 1) // x.denominator


def verify_point(x: Fraction) -> dict[str, object]:
    if x < 1:
        raise ValueError("L-9512 identity checker requires x >= 1")

    floor_x = floor_fraction(x)
    mu = mobius_table(max(1, floor_x))
    phi = phi_table(max(1, floor_x))

    finite_riesz = sum(
        Fraction(phi[n], n) * (x - n)
        for n in range(1, strict_positive_integer_cutoff(x) + 1)
    )
    riesz = Affine(finite_riesz, -x * x / 2)

    finite_fractional = sum(
        Fraction(mu[d]) * fractional_part(x / d) ** 2
        for d in range(1, floor_x + 1)
    )
    finite_mu_over_d2 = sum(
        Fraction(mu[d], d * d) for d in range(1, floor_x + 1)
    )

    # For d > x, {x/d}=x/d.  Hence the infinite tail is
    # x^2 * (C - sum_{d<=floor(x)} mu(d)/d^2).
    analytic = Affine(
        Fraction(1, 2) * (1 + finite_fractional
                          - x * x * finite_mu_over_d2),
        x * x / 2,
    )

    if riesz != -analytic:
        raise AssertionError(f"identity failure at x={x}: {riesz} != {-analytic}")

    # Independently verify sum mu(d) floor(x/d)=1.
    inversion = sum(
        mu[d] * floor_fraction(x / d) for d in range(1, floor_x + 1)
    )
    if inversion != 1:
        raise AssertionError(f"Möbius floor identity failure at x={x}")

    return {
        "x": {"numerator": x.numerator, "denominator": x.denominator},
        "riesz": riesz.to_json(),
        "analytic": analytic.to_json(),
        "mobius_floor_sum": inversion,
        "identity": True,
    }


def main() -> int:
    points = [
        Fraction(1), Fraction(3, 2), Fraction(2), Fraction(7, 3),
        Fraction(10), Fraction(101, 7), Fraction(257, 16),
    ]
    # Add a deterministic mixed rational grid.
    for q in range(2, 13):
        for p in range(q, 9 * q + 1, q + 1):
            points.append(Fraction(p, q))

    unique = sorted(set(points))
    results = [verify_point(x) for x in unique]
    canonical = json.dumps(results, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output = {
        "schema": "riemann.x9512-analytic-totient-identity.v1",
        "verdict": "PASS_EXACT_L9512_ANALYTIC_TOTIENT_IDENTITY",
        "formal_symbol": "C=1/zeta(2)=6/pi^2",
        "point_count": len(results),
        "proof_object_sha256": digest,
        "points": results,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
