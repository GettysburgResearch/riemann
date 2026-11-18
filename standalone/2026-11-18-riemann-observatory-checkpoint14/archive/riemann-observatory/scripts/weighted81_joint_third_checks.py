#!/usr/bin/env python3
"""Exact HLZ and rooted-CUE cosine–sine–sine cubic kernels."""
import sympy as sp

from weighted71_hlz_covariance_kernels import mixed_coefficients

from weighted73_cue_third_kernel_checks import (
    cue_complex_cumulant,
    x,
    y,
    z,
)


def arithmetic_joint():
    allocations = [((x, y, z), ()), ((y, z), (x,)),
                   ((x, z), (y,)), ((x, y), (z,))]
    coefficients = [mixed_coefficients(*allocation) for allocation in allocations]
    signed_j, signed_i = [
        sp.factor(sum(sign * coeff[slot] for sign, coeff
                      in zip((-1, -1, 1, 1), coefficients))/4)
        for slot in range(2)
    ]
    assert sp.expand(signed_j + y*z*(x+y+z-1)/2) == 0
    assert sp.expand(signed_i - y*z*(x-y*z+y+z-1)/2) == 0
    raw = sp.factor(12*(signed_j+signed_i))
    assert raw == -6*y*y*z*z
    cosine_mean = 1-4*x+2*x**3
    sine_second = -6*y*y*z*z
    return raw, sp.factor(raw-cosine_mean*sine_second)


def cue_joint(sample):
    signs = [(x, y, z), (-x, y, z), (x, -y, z), (x, y, -z)]
    signs_weight = [1, 1, -1, -1]
    return sp.factor(sum(weight*cue_complex_cumulant(*term, sample)
                         for term, weight in zip(signs, signs_weight))/4)


def check():
    raw, expected = arithmetic_joint()
    assert sp.expand(expected-12*x*y*y*z*z*(x*x-2)) == 0
    lower, upper = sp.symbols("lower upper", positive=True)
    interval = (y, lower, upper), (z, lower, upper), (x, lower, upper)
    integral = sp.integrate(expected/(x*y*z), *interval)
    assert sp.expand(integral-(upper**3-lower**3-6*(upper-lower))
                     *(upper**2-lower**2)**2) == 0
    print("HLZ raw:", raw)
    print("HLZ centered:", expected)
    for sorted_chamber in [(3, 4, 5), (2, 3, 6)]:
        a, b, c = sorted_chamber
        for chamber in [(a, b, c), (b, a, c), (c, a, b)]:
            sample = tuple(sp.Rational(k, 100) for k in chamber)
            rooted = cue_joint(sample)
            assert sp.expand(rooted-expected) == 0, (chamber, rooted)
            print("Rooted CUE chamber", chamber, "matches")


if __name__ == "__main__":
    check()
