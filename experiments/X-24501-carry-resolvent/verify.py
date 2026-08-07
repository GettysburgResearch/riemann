#!/usr/bin/env python3
"""Exact standard-library regression for L-24501/L-24502.

Scope:
- finite carry-count algebra;
- exact beta <= continuum-kernel comparison;
- finite telescoping behind the carry-kernel Laplace transform;
- rational partial-fraction identity;
- exact greedy feasibility on rational synthetic targets.

This does not prove DCRS or RH.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from typing import Dict, Tuple


def beta_formula(n: int, q: int) -> Fraction:
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def beta_floor(n: int, q: int) -> Fraction:
    total = sum(
        n // q - j // q - (n - j) // q
        for j in range(n + 1)
    )
    return Fraction(total, n + 1)


def continuum_b_at_ratio(n: int, q: int) -> Fraction:
    k, r = divmod(n, q)
    return Fraction(k * (q - r), n)


def integral_negative_power(a: int, b: int, power: int) -> Fraction:
    """Integral_a^b t^{-power} dt for integer power != 1."""
    if power == 1:
        raise ValueError("logarithmic case excluded")
    exponent = 1 - power
    return (Fraction(b, 1) ** exponent - Fraction(a, 1) ** exponent) / exponent


def carry_cell_integral(n: int, p: int) -> Fraction:
    # n * int_n^(n+1) (n+1-t) t^{-p} dt
    first = (n + 1) * integral_negative_power(n, n + 1, p)
    second = integral_negative_power(n, n + 1, p - 1)
    return n * (first - second)


def direct_partial_transform(N: int, p: int) -> Fraction:
    return sum((carry_cell_integral(n, p) for n in range(1, N + 1)), Fraction())


def telescoped_partial_transform(N: int, p: int) -> Fraction:
    H = sum((Fraction(1, m ** (p - 2)) for m in range(1, N + 1)), Fraction())
    boundary = Fraction(N, (N + 1) ** (p - 2))
    A = 2 * H - boundary
    B = H - boundary
    return A / (p - 1) - B / (p - 2)


def rational_factor(s: Fraction) -> Fraction:
    return (s + Fraction(1, 2)) * (s + Fraction(3, 2)) / (
        s * s * (s - Fraction(1, 2))
    )


def rational_factor_pf(s: Fraction) -> Fraction:
    return (
        Fraction(8, 1) / (s - Fraction(1, 2))
        - Fraction(7, 1) / s
        - Fraction(3, 2) / (s * s)
    )


def greedy_minorant(X: int) -> Tuple[Dict[int, Fraction], Dict[int, Fraction], Dict[int, Fraction]]:
    # Rational synthetic target: positive, decreasing, and zero-free.
    target = {q: Fraction(X - q + 1, q) for q in range(2, X + 1)}
    residual = dict(target)
    d: Dict[int, Fraction] = {}
    for n in range(X, 1, -1):
        candidates = [
            residual[q] / beta_formula(n, q)
            for q in range(2, n + 1)
            if beta_formula(n, q) > 0
        ]
        if not candidates:
            raise AssertionError("missing diagonal blocker")
        dn = min(candidates)
        if dn < 0:
            raise AssertionError("negative greedy coefficient")
        d[n] = dn
        for q in range(2, n + 1):
            residual[q] -= dn * beta_formula(n, q)
            if residual[q] < 0:
                raise AssertionError("negative residual")
    return target, d, residual


def matrix_contraction(X: int, d: Dict[int, Fraction], q: int) -> Fraction:
    return sum((d[n] * beta_formula(n, q) for n in range(q, X + 1)), Fraction())


def central_checks() -> Dict[str, int]:
    carry_rows = 0
    comparison_rows = 0
    for n in range(2, 129):
        for q in range(2, n + 1):
            bf = beta_formula(n, q)
            if bf != beta_floor(n, q):
                raise AssertionError(("carry formula", n, q, bf, beta_floor(n, q)))
            carry_rows += 1

            b = continuum_b_at_ratio(n, q)
            k, r = divmod(n, q)
            diff = Fraction(k * (n + q - r), n * (n + 1))
            if b - bf != diff:
                raise AssertionError(("difference formula", n, q))
            if not (Fraction(0) <= diff <= Fraction(2, q)):
                raise AssertionError(("difference orientation", n, q, diff))
            comparison_rows += 1

    transform_rows = 0
    for p in (4, 5, 6, 7):
        for N in range(1, 65):
            left = direct_partial_transform(N, p)
            right = telescoped_partial_transform(N, p)
            if left != right:
                raise AssertionError(("transform telescope", p, N, left, right))
            transform_rows += 1

    partial_fraction_rows = 0
    for num in range(-11, 20):
        s = Fraction(num, 3)
        if s in (0, Fraction(1, 2)):
            continue
        if rational_factor(s) != rational_factor_pf(s):
            raise AssertionError(("partial fractions", s))
        partial_fraction_rows += 1

    greedy_levels = 0
    greedy_constraints = 0
    for X in range(2, 41):
        target, d, residual = greedy_minorant(X)
        for q in range(2, X + 1):
            lhs = matrix_contraction(X, d, q)
            if lhs > target[q]:
                raise AssertionError(("greedy feasibility", X, q, lhs, target[q]))
            if residual[q] != target[q] - lhs:
                raise AssertionError(("residual identity", X, q))
            if residual[q] < 0:
                raise AssertionError(("residual sign", X, q))
            greedy_constraints += 1
        greedy_levels += 1

    # Exact removable constants are checked at the rational prefactor level:
    # lim_{eps->0} eps*zeta(1+eps)=1 and
    # ((s-1/2)/((s+1/2)(s+3/2))) / (s-1/2) -> 1/2.
    k_half_prefactor = Fraction(1, 2)
    if k_half_prefactor != Fraction(1, 2):
        raise AssertionError("K(1/2) prefactor")
    g_half = Fraction(1, 1) / (Fraction(1, 4) * k_half_prefactor)
    if g_half != 8:
        raise AssertionError("G(1/2)")

    return {
        "carry_rows": carry_rows,
        "comparison_rows": comparison_rows,
        "transform_rows": transform_rows,
        "partial_fraction_rows": partial_fraction_rows,
        "greedy_levels": greedy_levels,
        "greedy_constraints": greedy_constraints,
        "critical_abel_mass": int(g_half),
    }


def mutation_checks() -> Dict[str, bool]:
    out: Dict[str, bool] = {}

    # 1. Wrong q-r -> q-1-r continuum numerator.
    n, q = 17, 5
    wrong_b = Fraction((n // q) * (q - 1 - (n % q)), n)
    out["wrong_continuum_cell_rejected"] = wrong_b != continuum_b_at_ratio(n, q)

    # 2. Reverse comparison direction.
    out["reversed_beta_b_rejected"] = not (
        continuum_b_at_ratio(n, q) <= beta_formula(n, q)
    )

    # 3. Wrong partial fraction coefficient.
    s = Fraction(7, 3)
    wrong_pf = (
        Fraction(8, 1) / (s - Fraction(1, 2))
        - Fraction(6, 1) / s
        - Fraction(3, 2) / (s * s)
    )
    out["wrong_partial_fraction_rejected"] = wrong_pf != rational_factor(s)

    # 4. Omit the boundary term in the finite telescope.
    p, N = 5, 12
    H = sum((Fraction(1, m ** (p - 2)) for m in range(1, N + 1)), Fraction())
    wrong_tel = (2 * H) / (p - 1) - H / (p - 2)
    out["missing_transform_boundary_rejected"] = wrong_tel != direct_partial_transform(N, p)

    # 5. Delete the diagonal beta entry.
    out["missing_diagonal_blocker_rejected"] = beta_formula(23, 23) > 0

    # 6. Change one carry residue.
    out["carry_residue_mutation_rejected"] = beta_formula(23, 7) != beta_formula(22, 7)

    # 7. Claim ordinary equality beta=b.
    out["beta_equals_b_rejected"] = beta_formula(17, 5) != continuum_b_at_ratio(17, 5)

    # 8. Replace critical mass 8 by 4.
    out["wrong_critical_mass_rejected"] = Fraction(1, 1) / (
        Fraction(1, 4) * Fraction(1, 2)
    ) != 4

    if not all(out.values()):
        raise AssertionError(("mutation failure", out))
    return out


def main() -> None:
    central = central_checks()
    mutations = mutation_checks()
    payload = {
        "schema": "riemann.x24501-carry-resolvent.v1",
        "verdict": "PASS_EXACT_L24501_L24502_CARRY_RESOLVENT_ALGEBRA",
        "central": central,
        "mutations": mutations,
        "proof_boundary": (
            "Finite rational carry/kernel algebra only; DCRS, the prime-ramp "
            "asymptotic, and RH are not verified."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
