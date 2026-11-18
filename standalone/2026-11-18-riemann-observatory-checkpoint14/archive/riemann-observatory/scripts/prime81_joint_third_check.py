#!/usr/bin/env python3
"""Exact mixed HLZ and rooted-CUE third cumulants in all frequency chambers."""

from functools import lru_cache
from itertools import combinations, permutations, product

import sympy as sp


alpha, beta, aux, x, y, z = sp.symbols("alpha beta aux x y z")
frequencies = (x, y, z)


def exponential_numerator(factors, time, degree):
    return sp.Add(*(sp.prod(weight for _, weight in terms)
                    * (time+sum(exponent for exponent, _ in terms))**degree
                    for terms in product(*factors)))


def arithmetic_mixed():
    # h-slot choice has sign +1 and k-slot choice -1 in each sine.
    sign = (1, -1, -1)
    direct = [[(-beta*r, 1), (-alpha*r, m)] for r, m in zip(frequencies, sign)]
    dual = [[(alpha*r, 1), (beta*r, m)] for r, m in zip(frequencies, sign)]
    j = -(exponential_numerator(direct, 0, 3)
          -exponential_numerator(dual, -alpha-beta, 3))/(48*(alpha+beta))
    j_ab = sp.Poly(sp.cancel(j), alpha, beta).coeff_monomial(alpha*beta)

    def residue(u, v, w, time):
        factors = [[(-v*r, 1), (-u*r, m), (-w*r, m), (0, -m)]
                   for r, m in zip(frequencies, sign)]
        return -v*exponential_numerator(factors, time, 4)/(192*(u+v)*(v+w))

    def pieces(a, b, c):
        return (residue(a, b, c, 0)+residue(-b, -a, c, -a-b)
                +residue(a, -c, -b, -b-c))

    reflected = pieces(alpha, beta, aux)+pieces(beta, alpha, aux)
    i = sp.cancel(sp.diff(reflected, aux).subs(aux, 0))
    i_ab = sp.Poly(i, alpha, beta).coeff_monomial(alpha*beta)
    raw = sp.expand(12*(j_ab+i_ab))
    assert raw == -6*y*y*z*z
    centered = sp.factor(raw-(1-4*x+2*x**3)*(-6*y*y*z*z))
    assert sp.expand(centered-12*x*y*y*z*z*(x*x-2)) == 0
    print("Arithmetic J coefficient:", j_ab)
    print("Arithmetic reflected I coefficient:", i_ab)
    print("Arithmetic mixed raw kernel:", raw)
    return centered


@lru_cache(maxsize=None)
def transfer_matrix(shifts, chamber):
    """Projection path transfer on the interval [0,1] in a rational mode basis."""
    offsets = [sp.Integer(0)]
    for step in reversed(shifts):
        offsets.append(offsets[-1]+step)
    evaluated = [offset.subs(dict(zip(frequencies, chamber))) for offset in offsets]
    lo = -offsets[evaluated.index(min(evaluated))]
    hi = 1-offsets[evaluated.index(max(evaluated))]
    step = offsets[-1]

    # Conjugate the orthonormal matrix by diag(1,sqrt(12)) and integrate.
    # Its integrand entries become 1, 12(s-1/2), s+step-1/2,
    # 12(s+step-1/2)(s-1/2), respectively.
    length = hi-lo
    linear = (hi**2-lo**2)/2-length/2
    square = (hi**3-lo**3)/3-(hi**2-lo**2)/2+length/4
    return sp.Matrix(((length, 12*linear),
                      (linear+step*length, 12*(square+step*linear))))


def trace_correction(shifts, chamber):
    """Expand each P=E-Q and split cyclic paths at each occurrence of Q."""
    correction = 0
    count = len(shifts)
    cyclic = shifts*2
    for size in range(1, count+1):
        for chosen in combinations(range(count), size):
            cuts = chosen+(chosen[0]+count,)
            path = sp.eye(2)
            for lo, hi in zip(cuts, cuts[1:]):
                path *= transfer_matrix(cyclic[lo:hi], chamber)
            correction += (-1)**size*sp.trace(path)
    return correction


def cue_exponential_third(k, l, m, chamber):
    single = trace_correction((k+l+m,), chamber)
    double = sum(trace_correction(word, chamber)
                 for word in ((k,l+m), (l,k+m), (m,k+l)))
    triple = trace_correction((k,l,m), chamber)+trace_correction((k,m,l), chamber)
    return single-double+triple


def check_cue(mixed):
    cosine = 8*x*y*z*(-1+3*(x*x+y*y+z*z)-3*(x*x*y*y+y*y*z*z+z*z*x*x)
                      +2*x*x*y*y*z*z)
    # Global sign reflection reduces eight choices to four with x positive.
    signs = tuple((j, k) for j, k in product((-1, 1), repeat=2))
    count = 0
    for chamber_type in ((3, 4, 5), (2, 3, 6)):
        for values in permutations(chamber_type):
            chamber = tuple(sp.Rational(v, 100) for v in values)
            terms = [cue_exponential_third(x, j*y, k*z, chamber) for j,k in signs]
            raw_mixed = sum(j*k*value for (j,k), value in zip(signs, terms))/4
            raw_cosine = -sum(terms)/4
            assert sp.expand(raw_mixed-mixed) == 0
            assert sp.expand(raw_cosine-cosine) == 0
            count += 1
    print("Rooted-CUE mixed and cosine chambers verified:", count)


if __name__ == "__main__":
    mixed = arithmetic_mixed()
    check_cue(mixed)
    lo, hi = sp.symbols("lo hi")
    d1, d2, d3 = hi-lo, hi**2-lo**2, hi**3-lo**3
    band = sp.integrate(sp.cancel(mixed/(x*y*z)), (x,lo,hi), (y,lo,hi), (z,lo,hi))
    assert sp.expand(band-(d3-6*d1)*d2**2) == 0
    explicit = band.subs({lo:sp.Rational(1,20),hi:sp.Rational(1,10)})
    print("Shared mixed centered kernel:", mixed)
    print("Same-band [1/20,1/10] mixed cumulant:", explicit)
