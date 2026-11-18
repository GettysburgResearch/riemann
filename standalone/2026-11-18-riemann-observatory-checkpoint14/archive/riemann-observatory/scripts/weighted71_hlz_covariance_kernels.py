#!/usr/bin/env python3
"""Extract the leading real two-prime coefficients from HLZ (5) and (24)."""
from itertools import product

import sympy as sp

a, b, c, x, y = sp.symbols("a b c x y")


def mixed_coefficients(left, right):
    """The reduced twist uses disjoint prime-log lists left and right."""
    X, Y = sum(left), sum(right)
    main = sp.cancel(
        ((-b*X-a*Y)**3+(-b*Y-a*X)**3
         -(-a-b+a*X+b*Y)**3-(-a-b+a*Y+b*X)**3)/(12*(a+b))
    )

    def quartic(u, v, w, time, h, k):
        shifts = [[(-u*z, 1), (-w*z, 1), (0, -1)] for z in k]
        exponent = time-v*sum(h)
        return sum(sp.prod(sgn for _, sgn in choices)
                   *(exponent+sum(arg for arg, _ in choices))**4
                   for choices in product(*shifts))

    reflected = 0
    for alpha, beta in ((a, b), (b, a)):
        for u, v, w, time in ((alpha, beta, c, 0),
                              (-beta, -alpha, c, -alpha-beta),
                              (alpha, -c, -beta, -beta-c)):
            exponent = quartic(u, v, w, time, left, right)
            exponent += quartic(u, v, w, time, right, left)
            reflected += v*exponent/(48*(u+v)*(v+w))
    mixed_derivative = sp.cancel(sp.diff(reflected, c).subs(c, 0))
    return tuple(sp.factor(sp.diff(term, a, b)) for term in (main, mixed_derivative))


def check():
    def kernel(left, right):
        j, i = mixed_coefficients(left, right)
        return sp.factor(12*(j+i))

    first = kernel((x,), ())
    ratio = kernel((x,), (y,))
    prod = kernel((x, y), ())
    covariance = sp.factor((ratio+prod)/2-first*first.subs(x, y))
    baseline = 1-4*(x+y)+2*(x**3+y**3)+12*x*y-2*x*y*(x**2+y**2)
    assert first == 2*x**3-4*x+1
    assert sp.expand(ratio-(baseline-6*x**2*y**2)) == 0
    assert sp.expand(prod-(baseline+6*x**2*y**2)) == 0
    assert sp.expand(covariance-(-4*x*y+6*x**3*y+6*x*y**3-4*x**3*y**3)) == 0
    lower, upper = sp.symbols("lower upper", positive=True)
    correction = sp.integrate(sp.integrate(covariance/(x*y), (x, lower, upper)),
                              (y, lower, upper))
    width = upper-lower
    cubic = upper**3-lower**3
    assert sp.expand(correction-(-4*width**2+4*width*cubic-sp.Rational(4, 9)*cubic**2)) == 0
    assert ratio.subs(y, 0) == first
    assert prod.subs(y, 0) == first
    for name, expr in (
        ("first", first), ("ratio", ratio), ("product", prod), ("covariance", covariance)
    ):
        print(name, "=", expr)
    print("ratio (J,I) =", mixed_coefficients((x,), (y,)))
    print("product (J,I) =", mixed_coefficients((x, y), ()))
    print("integrated correction =", sp.factor(correction))


if __name__ == "__main__":
    check()
