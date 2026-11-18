#!/usr/bin/env python3
"""Extract the HLZ leading kernels and integrate the band covariance exactly."""

import sympy as sp


alpha, beta, aux, x, y = sp.symbols("alpha beta aux x y")
lower, upper = sp.symbols("lower upper")


def multiply(left, right):
    """Multiply finite exponent lists (exponent, coefficient)."""
    return [(p + q, a * b) for p, a in left for q, b in right]


def residue_exponents(u, v, w, kind):
    first = [(-u*x, 1), (-w*x, 1), (0, -1)]
    second = [(-u*y, 1), (-w*y, 1), (0, -1)]
    if kind == "ratio":
        return multiply([(-v*x, 1)], second) + multiply([(-v*y, 1)], first)
    if kind == "product":
        return [(-v*(x+y), 1)] + multiply(first, second)
    if kind == "square":
        return [(-2*v*x, 1), (-2*u*x, 1), (-(u+w)*x, 1),
                (-2*w*x, 1), (-u*x, -1), (-w*x, -1)]
    raise ValueError(kind)


def j_piece(kind):
    if kind == "ratio":
        direct = [-beta*x-alpha*y, -beta*y-alpha*x]
        dual = [alpha*x+beta*y, alpha*y+beta*x]
    else:
        total = x+y if kind == "product" else 2*x
        direct = [-alpha*total, -beta*total]
        dual = [alpha*total, beta*total]
    numerator = sum(t**3 for t in direct) - sum((t-alpha-beta)**3 for t in dual)
    return sp.cancel(numerator/(12*(alpha+beta)))


def residue_piece(u, v, w, t, kind):
    numerator = sum(weight*(exponent+t)**4
                    for exponent, weight in residue_exponents(u, v, w, kind))
    return v*numerator/(48*(u+v)*(v+w))


def i_piece(a, b, c, kind):
    return (residue_piece(a, b, c, 0, kind)
            + residue_piece(-b, -a, c, -a-b, kind)
            + residue_piece(a, -c, -b, -b-c, kind))


def leading_coefficients(kind):
    j = sp.Poly(j_piece(kind), alpha, beta).coeff_monomial(alpha*beta)
    reflected = i_piece(alpha, beta, aux, kind) + i_piece(beta, alpha, aux, kind)
    i = sp.Poly(sp.cancel(sp.diff(reflected, aux).subs(aux, 0)),
                alpha, beta).coeff_monomial(alpha*beta)
    return sp.factor(j), sp.factor(i), sp.expand(12*(j+i))


def f(t):
    return 1-4*t+2*t**3


coefficients = {kind: leading_coefficients(kind) for kind in ("ratio", "product", "square")}
for kind, (j, i, kernel) in coefficients.items():
    print(f"{kind} J: {j}")
    print(f"{kind} I plus reflection: {i}")
    print(f"{kind} normalized kernel: {kernel}")

common = f(x)+f(y)-1+12*x*y-2*x*y*(x**2+y**2)
ratio, product, square = (coefficients[kind][2] for kind in ("ratio", "product", "square"))
assert sp.expand(ratio-common+6*x**2*y**2) == 0
assert sp.expand(product-common-6*x**2*y**2) == 0
assert sp.expand(square-(1-8*x+6*x**2+10*x**3+x**4)) == 0
correction = sp.expand(((ratio+product)/2-f(x)*f(y))/(x*y))
assert correction == -4*x**2*y**2+6*x**2+6*y**2-4
integrated = sp.integrate(correction, (x, lower, upper), (y, lower, upper))
d1, d3 = upper-lower, upper**3-lower**3
assert sp.expand(integrated-(-4*d1**2+4*d1*d3-4*d3**2/9)) == 0
print(f"covariance correction integrand: {correction}")
print(f"integrated covariance correction: {sp.factor(integrated)}")

# Independent CUE projection calculation in mode-frequency coordinates, x >= y.
t = sp.symbols("t")
line = lambda u: u-sp.Rational(1, 2)
shift_trace = lambda u: 2-4*u+2*u**3

edge_overlap = sp.integrate(line(t+x)*line(t+y)/4, (t, 0, y))
cos_constant_overlap = 2*(y/4+(x-y)/2)+1-2*x
cos_linear_overlap = 12*(2*edge_overlap
    + 2*sp.integrate(line(t+x)*line(t)/2, (t, y, x))
    + sp.integrate(line(t)**2, (t, x, 1-x)))
cos_rank_two = (1-x)*(1-y)+(1-3*x+2*x**3)*(1-3*y+2*y**3)
cos_cue = sp.expand(-(shift_trace(x+y)+shift_trace(x-y))/2
                    + 2*(cos_constant_overlap+cos_linear_overlap)-cos_rank_two)
assert sp.expand(cos_cue-x*y*correction) == 0

sin_constant_overlap = y/2
sin_linear_overlap = 12*(2*edge_overlap
    + 2*sp.integrate(line(t+x)*y/2, (t, y, x))+(1-2*x)*x*y)
sin_rank_two = 6*x*y*(1-x)*(1-y)
sin_cue = sp.expand(-(shift_trace(x-y)-shift_trace(x+y))/2
                    + 2*(sin_constant_overlap+sin_linear_overlap)-sin_rank_two)
assert sp.expand(sin_cue-(ratio-product)/2) == 0
print(f"CUE cosine correction: {cos_cue}")
print(f"CUE sine correction: {sin_cue}")
