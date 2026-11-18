#!/usr/bin/env python3
"""Verify the Nakamura–Suzuki Poisson-rate and zero-atom intervals with Arb."""

from flint import __FLINT_VERSION__, acb, acb_series, arb, ctx


def xi_rate():
    center = arb(1) / 2
    s = acb_series([center, 1], 3)
    xi = s * (s - 1) * (-s * arb.pi().log() / 2).exp()
    xi *= (s / 2).gamma() * s.zeta() / 2
    assert xi[0].real > 0 and xi[1].real.contains(0)
    return 2 * xi[2].real / xi[0].real


def first_weights():
    cutoff = arb(100) + arb(1) / 1024
    assert cutoff.zeta_nzeros() == arb(29)
    roots = acb.zeta_zeros(1, 29)
    assert len(roots) == 29
    assert roots[0].imag > 0 and roots[-1].imag < 100
    assert all(left.imag < right.imag for left, right in zip(roots, roots[1:]))
    weights = []
    for root in roots:
        assert root.real == arb(1) / 2
        derivative = acb_series([root, 1], 2).zeta()[1]
        assert abs(derivative) > 0
        weights.append(1 / (root.imag * root.imag))
    return weights


def check_atom():
    rate = xi_rate()
    assert arb("0.04620998623083794157") < rate < arb("0.04620998623083794158")
    weights = first_weights()
    known_squares = sum(weight * weight for weight in weights)
    remaining_positive_mass = rate / 2 - sum(weights)
    assert remaining_positive_mass > 0

    a, b, height = arb("0.3611"), arb("9.3675"), arb(100)
    individual_cap = 2 * (a * height.log() + b) / (height * height)
    p_zero_jumps = (-rate).exp()
    p_three_or_more = 1 - p_zero_jumps * (1 + rate + rate * rate / 2)
    lower = p_zero_jumps * (1 + known_squares)
    upper = lower + p_zero_jumps * individual_cap * remaining_positive_mass + p_three_or_more
    assert arb("0.95487677454644730") < lower
    assert upper < arb("0.95490529007639706")
    print(f"FLINT {__FLINT_VERSION__}, conditional rate S: {rate}")
    print(f"Lower bound for the atom at 0: {lower}")
    print(f"Upper bound for the atom at 0: {upper}")


if __name__ == "__main__":
    ctx.prec = 128
    check_atom()
