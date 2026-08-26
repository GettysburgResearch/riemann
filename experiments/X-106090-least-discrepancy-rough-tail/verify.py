#!/usr/bin/env python3
"""Finite replay for L/T-106090.

Authenticates finite algebra only.  It does not prove the distinct-anchor
hybrid moment, BCI102990, or RH.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23)


def product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def prime_factors_squarefree(n):
    out = []
    for p in PRIMES:
        if n % p == 0:
            out.append(p)
            n //= p
    if n != 1:
        raise AssertionError(f"unsupported factor {n}")
    return tuple(out)


def squarefree_products(max_size=4):
    vals = []
    for k in range(1, max_size + 1):
        for ps in combinations(PRIMES, k):
            vals.append((product(ps), ps))
    return vals


def even_character_sum_kernel(p, a, b):
    """Exact sum over all even characters modulo p."""
    if (a - b) % p == 0 or (a + b) % p == 0:
        return Fraction(p - 1, 2)
    return Fraction(0)


checks = 0
oriented_pairs = 0
ramanujan_checks = 0
family_kernel_checks = 0
long_core_checks = 0
diagonal_weight_checks = 0
vals = squarefree_products(max_size=4)

# Unique least-discrepancy orientation on coprime nontrivial cores.
for c, cps in vals:
    for d, dps in vals:
        if math.gcd(c, d) != 1:
            continue
        pc, pd = cps[0], dps[0]
        assert pc != pd
        if pc < pd:
            ell, left, right, right_ps = pc, c, d, dps
        else:
            ell, left, right, right_ps = pd, d, c, cps
        assert left % ell == 0
        assert right % ell != 0
        assert all(r > ell for r in right_ps)
        assert right > ell
        checks += 5
        oriented_pairs += 1

        # Clean physical fixture when enough unused labels remain.
        g = next(q for q in PRIMES if q not in set(cps) | set(dps) and q != ell)
        remaining = [
            q for q in PRIMES
            if q not in set(cps) | set(dps) | {g, ell}
        ]
        if len(remaining) >= 4:
            P = remaining[0] * remaining[1]
            Q = remaining[2] * remaining[3]
            N = P * g * g * left * left
            M = Q * g * g * right * right
            assert N % ell == 0
            assert M % ell != 0
            checks += 2

            residue = (N - M) % ell
            assert residue != 0
            exponents = sorted((h * residue) % ell for h in range(1, ell))
            assert exponents == list(range(1, ell))
            checks += 2
            ramanujan_checks += 1

# Exact kernel form of the even-character family identity.
for p in (5, 7, 11, 13, 17, 19, 23):
    for a in range(1, p):
        for b in range(1, p):
            additive = Fraction(p - 1 if (a * a - b * b) % p == 0 else -1)
            sum_even = even_character_sum_kernel(p, a, b)
            character = (
                Fraction(p + 1, p - 1)
                + Fraction(2 * p, p - 1) * (sum_even - 1)
            )
            assert additive == character
            checks += 1
            family_kernel_checks += 1

# If P^-(d)>p and d is in [D,2D), then D>p/2 and 1+p/D<3.
for p in (2, 3, 5, 7, 11, 13):
    for d, dps in vals:
        if dps[0] <= p:
            continue
        D = 1 << (d.bit_length() - 1)
        assert D <= d < 2 * D
        assert D > p / 2
        assert Fraction(1, 1) + Fraction(p, D) < 3
        checks += 3
        long_core_checks += 1

# Source-dual diagonal algebra.
for g in (1, 2, 3, 5, 7):
    for c, cps in vals:
        ell = cps[0]
        for P in (6, 10, 15, 21, 35):
            for Q in (6, 10, 15, 21, 35):
                lhs = (
                    Fraction(g * g * ell * Q)
                    * Fraction(1, g * g * c * c * P)
                    * Fraction(1, g * g * Q)
                )
                rhs = Fraction(ell, g * g * c * c * P)
                assert lhs == rhs
                assert rhs <= Fraction(1, g * g * c * P)
                checks += 2
                diagonal_weight_checks += 1

result = {
    "schema": "riemann.x106090.least-discrepancy-rough-tail.v1",
    "verdict": "PASS_X_106090_LEAST_DISCREPANCY_ROUGH_TAIL",
    "checks": checks,
    "oriented_coprime_core_pairs": oriented_pairs,
    "ramanujan_fixtures": ramanujan_checks,
    "even_character_kernel_checks": family_kernel_checks,
    "fixed_fibre_long_core_checks": long_core_checks,
    "source_dual_diagonal_checks": diagonal_weight_checks,
    "proved_by_replay": {
        "unique_least_discrepancy_orientation": True,
        "opposite_core_is_strictly_rough": True,
        "nonzero_ramanujan_phase": True,
        "even_character_kernel_identity": True,
        "fixed_fibre_long_core_ratio": True,
        "source_dual_diagonal_algebra": True
    },
    "not_proved": {
        "distinct_anchor_hybrid_moment": True,
        "bci102990": True,
        "riemann_hypothesis": True
    }
}
assert checks == 142924
print(json.dumps(result, indent=2, sort_keys=True))
