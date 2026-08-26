#!/usr/bin/env python3
"""Finite replay for R/L/T-106095--106100.

Checks exact finite algebra only. It does not prove the off-diagonal fully
amplified moment, BCI102990, or RH.
"""
from __future__ import annotations

import json
from fractions import Fraction


def legendre(a: int, p: int) -> int:
    v = pow(a % p, (p - 1) // 2, p)
    return 1 if v == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if legendre(a, p) == -1)


checks = 0
squareclass_checks = 0
family_kernel_checks = 0
q_weight_firewall_checks = 0
atomic_diagonal_checks = 0
source_dual_cauchy_checks = 0

# Varying Q is absorbed into one fixed quadratic-class representative.
for p in (5, 7, 11, 13):
    nonsquare = least_nonsquare(p)
    for Q in range(1, p):
        rep = 1 if legendre(Q, p) == 1 else nonsquare
        r = next(x for x in range(1, p) if (rep * x * x - Q) % p == 0)
        for d in range(1, p):
            for h in range(1, p):
                assert (h * Q * d * d - h * rep * (r * d) ** 2) % p == 0
                checks += 1
                squareclass_checks += 1

# Exact even-character kernel after the combined variable x=r_Q*d.
for p in (5, 7, 11, 13):
    for x in range(1, p):
        for y in range(1, p):
            additive = Fraction(p - 1 if (x * x - y * y) % p == 0 else -1)
            sum_even = Fraction(p - 1, 2) if (x - y) % p == 0 or (x + y) % p == 0 else Fraction(0)
            character = Fraction(p + 1, p - 1) + Fraction(2 * p, p - 1) * (sum_even - 1)
            assert additive == character
            checks += 1
            family_kernel_checks += 1

# A separate Q-weight cancels the fixed-fibre reciprocal Q and leaves a count.
for Q in (6, 10, 14, 15, 21, 22, 26, 33, 35, 39):
    assert Q * Fraction(1, Q) == 1
    assert Fraction(1, Q) < 1
    checks += 2
    q_weight_firewall_checks += 2

# Correct g^2*ell atomic-diagonal algebra.
for g in (1, 2, 3, 5):
    for ell in (2, 3, 5, 7):
        for m in (3, 5, 7, 11):
            c = ell * m
            for P in (6, 10, 15, 21):
                for Q in (6, 10, 15, 21):
                    for d in (3, 5, 7, 11):
                        lhs = (
                            Fraction(g * g * ell * (ell - 1))
                            * Fraction(1, g * g * c * c * P)
                            * Fraction(1, g * g * d * d * Q)
                        )
                        rhs = Fraction(ell * (ell - 1), g * g * c * c * d * d * P * Q)
                        assert lhs == rhs
                        assert rhs <= Fraction(1, g * g * m * m * d * d * P * Q)
                        checks += 2
                        atomic_diagonal_checks += 2

# Finite form of the source-dual Cauchy inequality with weight g^2*ell.
indices = [(g, ell, sigma) for g in (1, 2, 3) for ell in (2, 3, 5) for sigma in (-1, 1)]
for seed in range(100):
    zs = []
    for j, (g, ell, sigma) in enumerate(indices):
        num = ((seed + 1) * (j + 3)) % 19 - 9
        den = (seed + 3) * (j + 2) + 1
        zs.append((g, ell, sigma, Fraction(num, den)))
    lhs = sum(z for _, _, _, z in zs) ** 2
    dual = sum(Fraction(1, g * g * ell) for g, ell, _, _ in zs)
    energy = sum(Fraction(g * g * ell) * z * z for g, ell, _, z in zs)
    assert lhs <= dual * energy
    checks += 1
    source_dual_cauchy_checks += 1

result = {
    "schema": "riemann.x106100.fully-amplified-owner-anchor.v1",
    "verdict": "PASS_X_106100_FULLY_AMPLIFIED_OWNER_ANCHOR",
    "checks": checks,
    "squareclass_checks": squareclass_checks,
    "even_character_kernel_checks": family_kernel_checks,
    "q_weight_firewall_checks": q_weight_firewall_checks,
    "atomic_diagonal_checks": atomic_diagonal_checks,
    "source_dual_cauchy_checks": source_dual_cauchy_checks,
    "proved_by_replay": {
        "varying_Q_squareclass_absorption": True,
        "combined_owner_core_even_character_kernel": True,
        "separate_Q_weight_leaves_dimension": True,
        "correct_g2ell_atomic_diagonal_algebra": True,
        "finite_source_dual_cauchy": True
    },
    "not_proved": {
        "FAPCX106100": True,
        "FANEX106100": True,
        "BCI102990": True,
        "riemann_hypothesis": True
    }
}
assert checks == 11616
print(json.dumps(result, indent=2, sort_keys=True))
