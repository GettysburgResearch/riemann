"""Reproduce the one-zero effective zeta lower-bound constants."""
from fractions import Fraction
from math import factorial

import flint
from flint import acb, arb, ctx, fmpq


def main():
    ctx.prec = 160
    low = arb("111.029535543169674524646")
    high = arb("111.029535543169674524666")
    root = acb(fmpq(1, 2), low.union(high))
    logarithmic_derivative = (
        3 / root
        + 3 / (1 - root)
        - arb.pi().log()
        + ((root / 2).digamma() + ((1 - root) / 2).digamma()) / 2
    ).real
    assert 111 < abs(root) < 112
    assert 0 < logarithmic_derivative < 3
    assert 16 * arb.pi() ** 2 / 9 < 18
    assert (arb(4) / 3) ** 2 * 16 * arb.pi() ** 2 / 15 < 20

    # Eqs. for the conservative envelopes in the proof.
    polynomial = [1433, 602, 38]
    tail = sum(left * right * factorial(i + j)
               for i, left in enumerate(polynomial)
               for j, right in enumerate(polynomial))
    gram_bound = tail + 4 * 1800 + 1800**2
    old_constant = 2 * Fraction(7216, 111) + Fraction(gram_bound, 111**2)
    new_constant = 2 * Fraction(36, 25 * 111) + Fraction(27, 5 * 111**2)
    assert old_constant == Fraction(3293255, 4107) < 802
    assert new_constant == Fraction(903, 34225) < Fraction(27, 1000)
    large_cutoff_constant = (
        2 * Fraction(8, 10**9 * 111) + Fraction(3000001, 10**6 * 111**2)
    )
    assert large_cutoff_constant < Fraction(1, 4000)
    print("python-flint", flint.__version__, "precision bits", ctx.prec)
    print("Re V'/V on certified root box:", logarithmic_derivative)
    print("coarse constant:", old_constant)
    print("short-interval constant:", new_constant)
    print("short-interval constant for log N >= 10:", large_cutoff_constant)


if __name__ == "__main__":
    main()
