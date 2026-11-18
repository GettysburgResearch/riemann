#!/usr/bin/env python3
"""Exact three-prime HLZ coefficient and cumulant calculation."""

from itertools import product

import sympy as sp


alpha, beta, aux, x, y, z = sp.symbols("alpha beta aux x y z")
lo, hi = sp.symbols("lo hi")
frequencies = (x, y, z)


def exponential_piece(factors, exponent, degree):
    """Return degree! times the degree component of a product of exponential sums."""
    return sp.Add(*(sp.prod(weight for _, weight in choices)
                    * (exponent+sum(power for power, _ in choices))**degree
                    for choices in product(*factors)))


def j_term():
    direct = [[(-alpha*r, 1), (-beta*r, 1)] for r in frequencies]
    dual = [[(alpha*r, 1), (beta*r, 1)] for r in frequencies]
    numerator = (exponential_piece(direct, 0, 3)
                 - exponential_piece(dual, -alpha-beta, 3))
    return sp.cancel(numerator/(48*(alpha+beta)))


def residue(u, v, w, t):
    factors = [[(-u*r, 1), (-v*r, 1), (-w*r, 1), (0, -1)]
               for r in frequencies]
    return v*exponential_piece(factors, t, 4)/(192*(u+v)*(v+w))


def i_term(a, b, c):
    return (residue(a, b, c, 0)+residue(-b, -a, c, -a-b)
            + residue(a, -c, -b, -b-c))


def first(r):
    return 1-4*r+2*r**3


def pair_interaction(r, s):
    return 12*r*s-2*r*s*(r**2+s**2)


def second(r, s):
    return first(r)+first(s)-1+pair_interaction(r, s)


j_ab = sp.Poly(j_term(), alpha, beta).coeff_monomial(alpha*beta)
i_reflected = i_term(alpha, beta, aux)+i_term(beta, alpha, aux)
i_after_auxiliary = sp.cancel(sp.diff(i_reflected, aux).subs(aux, 0))
i_ab = sp.Poly(i_after_auxiliary, alpha, beta).coeff_monomial(alpha*beta)
third = sp.expand(12*(j_ab+i_ab))
pairs = ((x, y), (y, z), (z, x))
expected = (sum(first(r) for r in frequencies)-2
            + sum(pair_interaction(r, s) for r, s in pairs)-24*x*y*z)
assert sp.expand(third-expected) == 0
cumulant = sp.expand(third-second(x,y)*first(z)-second(y,z)*first(x)
                     -second(z,x)*first(y)+2*first(x)*first(y)*first(z))
integrand = sp.cancel(cumulant/(x*y*z))
assert sp.expand(integrand-(-8+24*(x*x+y*y+z*z)
                           -24*(x*x*y*y+y*y*z*z+z*z*x*x)+16*x*x*y*y*z*z)) == 0
integrated = sp.integrate(integrand, (x, lo, hi), (y, lo, hi), (z, lo, hi))
d1, d3 = hi-lo, hi**3-lo**3
assert sp.expand(integrated-(-8*d1**3+24*d1**2*d3-8*d1*d3**2
                             + sp.Rational(16,27)*d3**3)) == 0
witness = integrated.subs({lo: sp.Rational(1,20), hi: sp.Rational(1,10)})
assert witness == -sp.Rational(818904257,864000000000)
print(f"J coefficient: {sp.factor(j_ab)}")
print(f"I plus reflection coefficient: {sp.factor(i_ab)}")
print(f"Normalized distinct-prime raw kernel: {third}")
print(f"Cumulant integrand: {sp.expand(integrand)}")
print(f"Witness for [1/20, 1/10]: {witness}")
