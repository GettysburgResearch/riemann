#!/usr/bin/env python3
"""Exact/synthetic regressions for L-19840/L-19841/L-19846.

This checker verifies algebraic identities only. It does not verify PSWF,
zeta, WKB, Airy, endpoint, or local-Weyl estimates.
"""

from __future__ import annotations

from fractions import Fraction
from math import isclose, pi, sqrt
import cmath


def signed_constraint_vectors() -> None:
    # Synthetic hierarchy preserving d0 << d4 << d6 << d8.
    d0 = Fraction(1, 10**12)
    d2 = Fraction(1, 10**10)
    d4 = Fraction(1, 10**8)
    d6 = Fraction(1, 10**4)
    d8 = Fraction(1, 10)

    # q_n=1 is enough to check the exact source constraints.
    # Coordinates are [e0,e2,e4,e6,e8].
    p_plus = [Fraction(1), 0, Fraction(-1), 0, 0]
    p_minus = [0, Fraction(1), 0, Fraction(-1), 0]
    p_plus2 = [0, 0, Fraction(1), 0, Fraction(-1)]

    r_plus = d4 - d0
    r_minus = -(d6 - d2)
    r_plus2 = d8 - d4

    u1 = [r_minus * x - r_plus * y for x, y in zip(p_plus, p_minus)]
    u2 = [r_plus2 * x - r_minus * y for x, y in zip(p_minus, p_plus2)]

    eps = [1, -1, 1, -1, 1]
    chi = [1 - d0, 1 - d2, 1 - d4, 1 - d6, 1 - d8]

    assert sum(u1) == 0
    assert sum(Fraction(e) * c * x for e, c, x in zip(eps, chi, u1)) == 0
    assert sum(u2) == 0
    assert sum(Fraction(e) * c * x for e, c, x in zip(eps, chi, u2)) == 0


def quotient_energy_small_singular_values_are_safe() -> None:
    # Source tail D has scales d4,d6. The source map S nearly kills the second
    # coordinate. In output coordinates the second energy becomes larger.
    d4 = Fraction(1, 10**8)
    d6 = Fraction(1, 10**4)
    eps = Fraction(1, 10**20)

    # S=diag(1,eps); induced D_V=S^{-T} D S^{-1}.
    out1 = d4
    out2 = d6 / (eps * eps)
    assert out1 == d4
    assert out2 > d6
    assert out1 / out2 < d4 / d6


def complete_alias_cross_identity() -> None:
    # One-dimensional exact identity:
    # |F+H|^2 = 1 + (F*H+H*F) + |H|^2, F=1.
    for h in [Fraction(-1, 3), Fraction(2, 5), Fraction(7, 4)]:
        lhs = (1 + h) ** 2
        cross = 2 * h
        positive_self = h * h
        rhs = 1 + cross + positive_self
        assert lhs == rhs
        # If |cross|<1, positivity follows without making self-energy small.
        if abs(cross) < 1:
            assert lhs >= 1 - abs(cross)


def exact_log_source_correction() -> None:
    # Use q=1_[0,1], which is compact BV. Its Fourier transform is explicit.
    ell = 11.0

    def qhat(z: complex) -> complex:
        if abs(z) < 1e-14:
            return 1.0 + 0.0j
        return (1.0 - cmath.exp(-1j * z)) / (1j * z)

    def hhat(z: complex) -> complex:
        return (1.0 - cmath.exp(-1j * z * ell)) * qhat(z)

    cden = hhat(0.5j)
    assert abs(cden) > 1.0

    for k in range(-4, 5):
        tk = 2.0 * pi * k / ell

        def g0hat(z: complex) -> complex:
            a = z - tk
            if abs(a) < 1e-12:
                return 1.0 + 0.0j
            return (1.0 - cmath.exp(-1j * a * ell)) / (1j * a * ell)

        ik = g0hat(0.5j)

        def ghat(z: complex) -> complex:
            return g0hat(z) - ik * hhat(z) / cden

        assert abs(ghat(0.5j)) < 1e-10
        for j in range(-4, 5):
            tj = 2.0 * pi * j / ell
            expected = 1.0 if j == k else 0.0
            assert abs(ghat(tj) - expected) < 1e-9


def radial_phase_separation() -> None:
    # S0'(v)=sqrt(v^2-1)/v. Check the exact k>=2 separation on a broad grid.
    def sp(v: float) -> float:
        return sqrt(v * v - 1.0) / v

    for k in range(2, 80):
        for a in range(0, 500):
            v = 1.0 + a / 37.0
            gap = k * sp(k * v) - sp(v)
            assert gap > 0.0
            assert gap + 1e-12 >= (k - 1) * 0.99


def same_branch_complex_cancellation() -> None:
    # For an analytic real-type action S, overline(exp(iR S(conj z)))
    # * exp(iR S(z)) = 1 exactly.
    R = 137.0
    z = 1.7 + 0.003j

    def action(w: complex) -> complex:
        return w * w + 0.2 * w + 1.0

    left = cmath.exp(1j * R * action(z.conjugate())).conjugate()
    right = cmath.exp(1j * R * action(z))
    assert abs(left * right - 1.0) < 1e-10


def main() -> None:
    signed_constraint_vectors()
    quotient_energy_small_singular_values_are_safe()
    complete_alias_cross_identity()
    exact_log_source_correction()
    radial_phase_separation()
    same_branch_complex_cancellation()
    print("PASS: quotient-energy prolate repair algebra verified")


if __name__ == "__main__":
    main()
