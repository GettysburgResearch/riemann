#!/usr/bin/env python3
"""Exact leading HLZ coefficient for the symmetrized pair (p, 1)."""

import sympy as sp


a, b, c, x = sp.symbols("a b c x")


def j_piece():
    return sp.cancel(((-a*x)**3 + (-b*x)**3
                      - (-a-b+a*x)**3 - (-a-b+b*x)**3)/(12*(a+b)))


def residue_piece(u, v, w, t):
    numerator = (t-u*x)**4 + (t-v*x)**4 + (t-w*x)**4 - t**4
    return v*numerator/(48*(u+v)*(v+w))


def i_piece(alpha, beta):
    return (residue_piece(alpha, beta, c, 0)
            + residue_piece(-beta, -alpha, c, -alpha-beta)
            + residue_piece(alpha, -c, -beta, -beta-c))


j = sp.Poly(j_piece(), a, b).coeff_monomial(a*b)
reflected = sp.diff(i_piece(a, b) + i_piece(b, a), c).subs(c, 0)
i = sp.Poly(sp.cancel(reflected), a, b).coeff_monomial(a*b)
assert sp.expand(j - (x-1)**2*(x+2)/6) == 0
assert sp.expand(i - (2*x-3)/12) == 0
assert sp.expand(12*(i+j)) == 1-4*x+2*x**3
print(sp.expand(12*(i+j)))
