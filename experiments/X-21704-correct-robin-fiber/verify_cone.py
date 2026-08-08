#!/usr/bin/env python3
"""Exact rational replay of the positive-Robin-fiber cone counterexample."""
from fractions import Fraction


def phi_coeff(ell: Fraction, degree: int) -> Fraction:
    if degree % 2:
        return Fraction(0)
    n = degree // 2
    if n == 0:
        return Fraction(1)
    a = ell / 2
    from math import factorial
    return (
        a ** (2 * n) / factorial(2 * n)
        + 2 * a ** (2 * n - 1) / factorial(2 * n - 1)
    )


def main() -> None:
    ell = Fraction(8)
    eps = Fraction(1, 10)
    c0 = Fraction(1) + eps * phi_coeff(ell, 0)
    c1 = eps * phi_coeff(ell, 2)
    c2 = eps * phi_coeff(ell, 4)

    assert phi_coeff(ell, 2) == 16
    assert phi_coeff(ell, 4) == 32
    assert c0 == Fraction(11, 10)
    assert c1 == Fraction(8, 5)
    assert c2 == Fraction(16, 5)
    assert c1 * c1 == Fraction(64, 25)
    assert 2 * c0 * c2 == Fraction(176, 25)
    assert c1 * c1 < 2 * c0 * c2

    print("PASS_EXACT_POSITIVE_ROBIN_CONE_COUNTEREXAMPLE")
    print("mixture", "Phi_0 + (1/10) Phi_8")
    print("c0", c0)
    print("c1", c1)
    print("c2", c2)
    print("newton_lhs", c1 * c1)
    print("newton_rhs", 2 * c0 * c2)
    print(
        "proof_boundary",
        "exact coefficient obstruction only; no Nörlund or RH conclusion",
    )


if __name__ == "__main__":
    main()
