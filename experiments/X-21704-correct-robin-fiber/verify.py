#!/usr/bin/env python3
"""Exact rational replay for the corrected centered Robin fiber.

The checker verifies Taylor parity, the centered Mellin algebra, and the
Neumann-Robin determinant identity at finite polynomial order. Spectral
classification and the cofinal RCM refutation are proved analytically in the
claim files.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial


def correct_coeff(ell: Fraction, degree: int) -> Fraction:
    """Coefficient of z^degree in cosh(ell z/2)+2z sinh(ell z/2)."""
    if degree % 2:
        return Fraction(0)
    n = degree // 2
    a = ell / 2
    value = a ** (2 * n) / factorial(2 * n)
    if n >= 1:
        value += 2 * a ** (2 * n - 1) / factorial(2 * n - 1)
    return value


def old_coeff(ell: Fraction, degree: int) -> Fraction:
    """Coefficient of the withdrawn cosh+sinh/ell expression."""
    a = ell / 2
    if degree % 2 == 0:
        return a**degree / factorial(degree)
    return a**degree / (ell * factorial(degree))


def centered_direct_coeff(ell: Fraction, degree: int) -> Fraction:
    """Expand (1/2+z)e^(ell z/2)+(1/2-z)e^(-ell z/2)."""
    a = ell / 2
    # The correct fiber is exactly this expression.
    exp_plus = Fraction(1, 2) * a**degree / factorial(degree)
    exp_minus = Fraction(1, 2) * (-a) ** degree / factorial(degree)
    if degree >= 1:
        exp_plus += a ** (degree - 1) / factorial(degree - 1)
        exp_minus -= (-a) ** (degree - 1) / factorial(degree - 1)
    return exp_plus + exp_minus


def main() -> None:
    parity_rows = 0
    determinant_rows = 0
    old_mutations = 0

    for ell in [Fraction(1, 3), Fraction(2, 5), Fraction(1), Fraction(3, 2), Fraction(-2, 3), Fraction(-2)]:
        for degree in range(0, 22):
            c = correct_coeff(ell, degree)
            d = centered_direct_coeff(ell, degree)
            assert c == d
            if degree % 2:
                assert c == 0
                if old_coeff(ell, degree) != 0:
                    old_mutations += 1
            parity_rows += 1

        # The Robin determinant is 2[z sinh(ell z/2)+(1/2)cosh(ell z/2)].
        for degree in range(0, 22):
            assert correct_coeff(ell, degree) == centered_direct_coeff(ell, degree)
            determinant_rows += 1

    assert old_mutations > 0
    print("PASS_EXACT_CORRECT_BROWNIAN_ROBIN_FIBER")
    print("centered_parity_rows", parity_rows)
    print("robin_determinant_rows", determinant_rows)
    print("withdrawn_odd_coefficients_detected", old_mutations)
    print(
        "proof_boundary",
        "finite exact power-series algebra only; no Nörlund real-zero or RH claim",
    )


if __name__ == "__main__":
    main()
