#!/usr/bin/env python3
"""Check the third kernels in aggregate HLZ and rooted CUE."""
from functools import lru_cache
from itertools import combinations

import sympy as sp

from weighted71_hlz_covariance_kernels import mixed_coefficients
from weighted73_cue_band_checks import basis, s, x, y

z = sp.Symbol("z", real=True)


def arithmetic_raw(left, right):
    return sp.factor(12*sum(mixed_coefficients(left, right)))


def arithmetic_cumulant():
    def one(t):
        return 1-4*t+2*t**3

    def two(u, v):
        return one(u)+one(v)-1+12*u*v-2*u*v*(u**2+v**2)

    three = sum(arithmetic_raw(left, right) for left, right in
                (((x, y, z), ()), ((x, y), (z,)), ((x, z), (y,)), ((y, z), (x,))))/4
    return sp.factor(three-two(x,y)*one(z)-two(x,z)*one(y)-two(y,z)*one(x)
                     +2*one(x)*one(y)*one(z))


@lru_cache(maxsize=None)
def transfer_matrix(shifts, sample):
    offsets = [sp.Integer(0)]
    for step in reversed(shifts):
        offsets.append(offsets[-1]+step)
    evaluations = [offset.subs(dict(zip((x, y, z), sample))) for offset in offsets]
    lo = -offsets[evaluations.index(min(evaluations))]
    hi = 1-offsets[evaluations.index(max(evaluations))]
    integrand = basis(s+offsets[-1])*basis(s).T
    return integrand.applyfunc(lambda entry: sp.integrate(entry, (s, lo, hi)))


def trace_correction(shifts, sample):
    """Tr product with E-Q minus its value with E in the polynomial chamber."""
    length = len(shifts)
    correction = 0
    for size in range(1, length+1):
        for positions in combinations(range(length), size):
            cut = positions + (positions[0]+length,)
            cyclic = shifts*2
            value = sp.eye(2)
            for start, stop in zip(cut, cut[1:]):
                value *= transfer_matrix(cyclic[start:stop], sample)
            correction += (-1)**size*sp.trace(value)
    return sp.factor(correction)


def cue_complex_cumulant(k, l, m, sample):
    single = trace_correction((k+l+m,), sample)
    double = sum(trace_correction(shifts, sample)
                 for shifts in ((k, l+m), (l, k+m), (m, k+l)))
    triple = trace_correction((k, l, m), sample)+trace_correction((k, m, l), sample)
    return sp.factor(single-double+triple)


def check():
    expected = 8*x*y*z*(2*x**2*y**2*z**2-3*(x**2*y**2+x**2*z**2+y**2*z**2)
                        +3*(x**2+y**2+z**2)-1)
    arithmetic = arithmetic_cumulant()
    assert sp.expand(arithmetic-expected) == 0
    # For ordered x<y<z the signed path ranges change only across z=x+y.
    # At a boundary both polynomial limits agree by continuity of the matrices.
    for chamber in [(3, 4, 5), (2, 3, 6)]:
        sample = tuple(sp.Rational(k, 100) for k in chamber)
        signed_terms = ((x, y, z), (-x, y, z), (x, -y, z), (x, y, -z))
        cue_signed_cosine = -sum(cue_complex_cumulant(*ks, sample)
                                 for ks in signed_terms)/4
        assert sp.expand(cue_signed_cosine-expected) == 0
        print(f"Rooted CUE polynomial chamber {chamber}: matched")
    print("Common cubic kernel:", sp.factor(expected))
    print("At x=y=z=1/10:", expected.subs(dict.fromkeys((x, y, z), sp.Rational(1, 10))))


if __name__ == "__main__":
    check()
