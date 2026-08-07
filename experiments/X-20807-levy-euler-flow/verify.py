#!/usr/bin/env python3
"""Exact Fraction regression for L-20810, L-20812, and L-20813.

This is a finite algebra checker. It does not evaluate zeta, prime manifests,
transcendental Fenchel terms, or the cofinal RH inequality.
"""
from __future__ import annotations

import json
from fractions import Fraction as F


def s(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify_levy_transport() -> dict[str, str]:
    # Arithmetic compound-Poisson law with jumps 1 and 5, each intensity 1.
    taus = [F(1), F(5)]
    intensities = [F(1), F(1)]
    p = sum((lam * tau for lam, tau in zip(intensities, taus)), F())
    q = sum((lam * tau * tau for lam, tau in zip(intensities, taus)), F())

    # Synthetic reference minimizer chi(u)=1+u on 0<=u<=P.
    # It corresponds to A(t)=1+(t-1)^2/2 on t>=1, so M0=A(1)=1.
    m0 = F(1)
    reference_variance = p + p * p / 2
    a_star = reference_variance - m0
    margin = q - a_star

    assert p == 6
    assert q == 26
    assert reference_variance == 24
    assert a_star == 23
    assert margin == 3
    assert margin == m0 + q - reference_variance

    return {
        "arithmetic_mean": s(p),
        "arithmetic_variance": s(q),
        "reference_variance": s(reference_variance),
        "initial_reserve": s(m0),
        "fenchel_barrier": s(a_star),
        "reserve": s(margin),
    }


def verify_euler_riccati() -> dict[str, str]:
    # Exact local factor: r=1/2, log-prime parameter a=3, K=4.
    r = F(1, 2)
    a = F(3)
    kmax = 4

    geom = sum((r**k for k in range(1, kmax + 1)), F())
    weighted_geom = sum((k * r**k for k in range(1, kmax + 1)), F())
    p_local = a * geom
    q_local = a * a * weighted_geom

    defect = (
        a
        * a
        * r ** (kmax + 1)
        * sum(((kmax - m) * r**m for m in range(kmax)), F())
    )

    bracket_form = (
        a
        * a
        * r ** (kmax + 1)
        * (kmax - (kmax + 1) * r + r ** (kmax + 1))
        / (1 - r) ** 2
    )

    triangular = a * a * sum(
        ((ell - 1) * r**ell for ell in range(2, kmax + 1)), F()
    )
    retained_pairs = a * a * sum(
        (r ** (m + n)
         for m in range(1, kmax + 1)
         for n in range(1, kmax + 1)
         if m + n <= kmax),
        F(),
    )

    assert geom == F(15, 16)
    assert weighted_geom == F(13, 8)
    assert p_local == F(45, 16)
    assert q_local == F(117, 8)
    assert defect == F(441, 256)
    assert defect == bracket_form
    assert triangular == F(99, 16)
    assert triangular == retained_pairs
    assert p_local * p_local - defect == triangular
    assert q_local == a * p_local + triangular
    assert q_local == p_local * p_local + a * p_local - defect
    assert defect > 0
    assert triangular > 0

    return {
        "geometric_sum": s(geom),
        "weighted_geometric_sum": s(weighted_geom),
        "local_P": s(p_local),
        "local_Q": s(q_local),
        "cutoff_defect": s(defect),
        "triangular_retained_power": s(triangular),
        "retained_pair_sum": s(retained_pairs),
        "positive_reconstruction": s(a * p_local + triangular),
        "riccati_reconstruction": s(p_local * p_local + a * p_local - defect),
    }


def main() -> int:
    result = {
        "schema": "riemann.x20807.levy-euler-flow.v2",
        "classification": "EXACT_FINITE_ALGEBRA_REGRESSION",
        "levy_transport": verify_levy_transport(),
        "euler_riccati": verify_euler_riccati(),
        "verdict": "PASS_EXACT_L20810_L20812_L20813_IDENTITIES",
        "proof_boundary": (
            "Fraction-only synthetic verification of the cumulant reserve, "
            "finite Euler Riccati identity, and positive triangular "
            "retained-power recombination. No Riemann data or cofinal sign."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
