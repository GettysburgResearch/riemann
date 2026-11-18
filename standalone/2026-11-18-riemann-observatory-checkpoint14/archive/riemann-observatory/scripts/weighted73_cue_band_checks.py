#!/usr/bin/env python3
"""Symbolic continuous limits of the rank-two rooted-CUE DPP correction."""
import sympy as sp

s, x, y = sp.symbols("s x y", real=True)


def q(u, v):
    return 1 + 12*(u-sp.Rational(1, 2))*(v-sp.Rational(1, 2))


def basis(t):
    return sp.Matrix([1, sp.sqrt(12)*(t-sp.Rational(1, 2))])


def shift_matrix(t):
    integrand = basis(s+t)*basis(s).T
    return integrand.applyfunc(lambda entry: sp.factor(sp.integrate(entry, (s, 0, 1-t))))


def trace_interval(d, start, stop):
    return sp.integrate(q(s, s+d), (s, start, stop))


def check():
    mx, my = shift_matrix(x), shift_matrix(y)
    one = sp.factor(sp.trace(mx))
    same_sign = sp.factor(trace_interval(x+y, 0, 1-x-y)-sp.trace(mx*my))
    # Opposite signs: x >= y, x+y <= 1. Symmetry extends the result to x < y.
    opposite_sign = sp.factor(trace_interval(x-y, y, 1-x)-sp.trace(mx*my.T))
    cosine = sp.factor((same_sign+opposite_sign)/2)
    sine = sp.factor((opposite_sign-same_sign)/2)
    assert sp.expand(one-1) == 2*x**3-4*x+1
    assert sp.expand(cosine) == -4*x**3*y**3+6*x**3*y+6*x*y**3-4*x*y
    assert sine == -6*x**2*y**2
    print("shift matrix:", mx)
    print("mean kernel:", sp.expand(one-1))
    print("same-sign covariance:", same_sign)
    print("opposite-sign covariance:", opposite_sign)
    print("cosine covariance:", cosine)
    print("sine covariance:", sine)


if __name__ == "__main__":
    check()
