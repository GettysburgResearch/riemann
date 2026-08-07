#!/usr/bin/env python3
"""Exact Fraction replay of L-9513.

Checks pair covariance by piecewise polynomial integration and verifies the two
closed forms for every D in a small deterministic range.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math


def mobius_table(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for m in range(2, n + 1):
        if not composite[m]:
            primes.append(m)
            mu[m] = -1
        for p in primes:
            if m * p > n:
                break
            composite[m * p] = True
            if m % p == 0:
                mu[m * p] = 0
                break
            mu[m * p] = -mu[m]
    return mu


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def jordan(n: int, r: int) -> int:
    # J_r(n) from n^r = sum_{d|n} J_r(d).
    vals = [0] * (n + 1)
    for m in range(1, n + 1):
        vals[m] = m**r - sum(vals[d] for d in divisors(m) if d < m)
    return vals[n]


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def integrate_poly(coeff: list[Fraction], left: int, right: int) -> Fraction:
    return sum(
        c * Fraction(right ** (j + 1) - left ** (j + 1), j + 1)
        for j, c in enumerate(coeff)
    )


def local_f_poly(scale: int, left: int) -> list[Fraction]:
    block = left // scale
    shift = block * scale
    # ((x-shift)/scale)^2 - 1/3
    return [
        Fraction(shift * shift, scale * scale) - Fraction(1, 3),
        Fraction(-2 * shift, scale * scale),
        Fraction(1, scale * scale),
    ]


def covariance_integral(d: int, e: int) -> Fraction:
    period = math.lcm(d, e)
    points = sorted(
        set(range(0, period + 1, d)) | set(range(0, period + 1, e))
    )
    total = Fraction(0)
    for left, right in zip(points, points[1:]):
        total += integrate_poly(
            poly_mul(local_f_poly(d, left), local_f_poly(e, left)),
            left,
            right,
        )
    return total / period


def covariance_formula(d: int, e: int) -> Fraction:
    g = math.gcd(d, e)
    return Fraction(g * g, 12 * d * e) + Fraction(
        g**4, 180 * d * d * e * e
    )


def direct_energy(D: int, mu: list[int]) -> Fraction:
    return sum(
        mu[d] * mu[e] * covariance_formula(d, e)
        for d in range(1, D + 1)
        for e in range(1, D + 1)
    )


def jordan_energy(D: int, mu: list[int]) -> Fraction:
    first = Fraction(0)
    second = Fraction(0)
    for q in range(1, D + 1):
        s1 = sum(Fraction(mu[d], d) for d in range(q, D + 1, q))
        s2 = sum(Fraction(mu[d], d * d) for d in range(q, D + 1, q))
        first += Fraction(jordan(q, 2), 12) * s1 * s1
        second += Fraction(jordan(q, 4), 180) * s2 * s2
    return first + second


def frac_json(q: Fraction) -> dict[str, int]:
    return {"numerator": q.numerator, "denominator": q.denominator}


def main() -> int:
    max_d = 12
    pair_rows = []
    for d in range(1, max_d + 1):
        for e in range(1, max_d + 1):
            direct = covariance_integral(d, e)
            formula = covariance_formula(d, e)
            if direct != formula:
                raise AssertionError(f"covariance mismatch d={d} e={e}")
            pair_rows.append({"d": d, "e": e, "value": frac_json(direct)})

    mu = mobius_table(max_d)
    energy_rows = []
    for D in range(1, max_d + 1):
        direct = direct_energy(D, mu)
        factored = jordan_energy(D, mu)
        if direct != factored:
            raise AssertionError(f"Jordan factorization mismatch D={D}")
        if direct < 0:
            raise AssertionError(f"negative energy D={D}")
        energy_rows.append({"D": D, "energy": frac_json(direct)})

    canonical = json.dumps(
        {"pairs": pair_rows, "energies": energy_rows},
        sort_keys=True,
        separators=(",", ":"),
    )
    digest = hashlib.sha256(canonical.encode()).hexdigest()
    output = {
        "schema": "riemann.x9513-bohr-mobius-packet.v1",
        "verdict": "PASS_EXACT_L9513_BOHR_JORDAN_FACTORIZATION",
        "max_denominator": max_d,
        "pair_count": len(pair_rows),
        "proof_object_sha256": digest,
        "energies": energy_rows,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
