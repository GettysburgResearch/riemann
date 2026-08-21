#!/usr/bin/env python3
"""Exact finite audit for the repaired T100600/T100700 algebra.

This checker authenticates finite polynomial identities and type firewalls. It
is not a proof of the remaining analytic estimate or RH.
"""

from fractions import Fraction


def add(a, b, scale=Fraction(1)):
    out = dict(a)
    for monomial, value in b.items():
        out[monomial] = out.get(monomial, Fraction(0)) + scale * value
        if out[monomial] == 0:
            del out[monomial]
    return out


def mul(a, b):
    out = {}
    for ma, va in a.items():
        for mb, vb in b.items():
            monomial = tuple(x + y for x, y in zip(ma, mb))
            out[monomial] = out.get(monomial, Fraction(0)) + va * vb
    return {m: v for m, v in out.items() if v}


def scale(a, c):
    return {m: c * v for m, v in a.items() if c * v}


def one(nvars):
    return {(0,) * nvars: Fraction(1)}


def variable(nvars, index, power=1):
    monomial = [0] * nvars
    monomial[index] = power
    return {tuple(monomial): Fraction(1)}


def product(items, nvars):
    out = one(nvars)
    for item in items:
        out = mul(out, item)
    return out


def main():
    nvars = 5
    activities = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5),
                  Fraction(1, 7), Fraction(1, 11)]

    euler = []
    squared = []
    transition = []
    for i, r in enumerate(activities):
        x = variable(nvars, i)
        x2 = variable(nvars, i, 2)
        euler.append(add(one(nvars), scale(x, -r)))
        squared.append(add(one(nvars), scale(x2, -(r * r))))
        transition.append(add(scale(x, r), scale(x2, -(r * r))))

        # The q^2 state requires the unrestricted multiplicative shift.
        assert mul(x, x) == x2

    # Inverse-free first-transition identity.
    native = product(euler, nvars)
    rebuilt = product(squared, nvars)
    for t in range(nvars):
        term = mul(product(squared[:t], nvars),
                   mul(transition[t], product(euler[t + 1 :], nvars)))
        rebuilt = add(rebuilt, term, scale=Fraction(-1))
    assert rebuilt == native

    # Double-owner mixed-coboundary identity.
    for i in range(nvars):
        for j in range(i + 1, nvars):
            block = scale(
                mul(variable(nvars, i),
                    mul(variable(nvars, j), product(euler[i + 1 : j], nvars))),
                activities[i] * activities[j],
            )
            coboundary = add(product(euler[i : j + 1], nvars),
                             product(euler[i + 1 : j + 1], nvars),
                             scale=Fraction(-1))
            coboundary = add(coboundary, product(euler[i:j], nvars),
                             scale=Fraction(-1))
            coboundary = add(coboundary, product(euler[i + 1:j], nvars))
            assert coboundary == block

    # Dilation and divisor restriction are not the same local operation.
    # For beta's ordinary-prime local factor B_q(x)=1-x:
    # dilation x*B_q=x-x^2, whereas restriction by q (after dividing by
    # beta(q)=-1) removes the local factor and has local polynomial 1.
    dilation = {1: Fraction(1), 2: Fraction(-1)}
    restriction = {0: Fraction(1)}
    assert dilation != restriction

    # Correct local critical transition normalization on rational square p=4.
    # kappa(s)=2s-s^2 for s<=1 and 1 for s>=1.  The exact inequality is
    # p^(3/2) kappa(sqrt(p)t) > kappa(pt), not the earlier doubly weighted one.
    p = Fraction(4)
    for t in [Fraction(1, 16), Fraction(1, 8), Fraction(1, 4),
              Fraction(1, 2), Fraction(1), Fraction(2)]:
        def kappa(s):
            return 2 * s - s * s if s <= 1 else Fraction(1)

        lhs = Fraction(8) * kappa(Fraction(2) * t)
        rhs = kappa(Fraction(4) * t)
        assert lhs > rhs

    print("PASS_X_100705_RECENT_WORK_HOSTILE_AUDIT")
    print("rh_established=false")
    print("balanced_terminal_estimate_proved=false")


if __name__ == "__main__":
    main()
