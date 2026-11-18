#!/usr/bin/env python3
"""Extract the fixed Q=1 and Q=2*2**(-s)-1 HLZ derivative polynomials."""

import argparse
from functools import lru_cache

import sympy as sp

L, q, c0, c1, c2, c3 = sp.symbols("L q c0 c1 c2 c3")
# zeta(1+x) = 1/x + c0 + c1*x + c2*x**2 + c3*x**3 + ...
# q = log(2); c_j = (-1)**j * Stieltjes(j) / j!.


def add(*terms):
    result = {}
    for term in terms:
        for degree, value in term.items():
            result[degree] = result.get(degree, 0) + value
    return {degree: sp.expand(value) for degree, value in result.items()}


def scale(term, value):
    return {degree: value * coeff for degree, coeff in term.items()}


def multiply(left, right, limit=4):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            if i + j <= limit:
                result[i+j] = result.get(i+j, 0) + a*b
    return {degree: sp.expand(value) for degree, value in result.items()}


def inverse_unit(term, limit=4):
    assert term[0] != 0
    result = {0: 1/sp.sympify(term[0])}
    for degree in range(1, limit+1):
        result[degree] = sp.expand(-sum(term.get(j, 0)*result[degree-j]
                                              for j in range(1, degree+1))/term[0])
    return result


def exponential(linear):
    return {j: linear**j / sp.factorial(j) for j in range(5)}


def zeta(slope):
    assert slope != 0
    return {-1: 1/sp.sympify(slope), 0: c0, 1: slope*c1, 2: slope**2*c2, 3: slope**3*c3}


def log_derivative(slope):
    assert slope != 0
    unit = {0: 1, 1: slope*c0, 2: slope**2*c1, 3: slope**3*c2, 4: slope**4*c3}
    differentiated = {0: c0, 1: 2*slope*c1, 2: 3*slope**2*c2, 3: 4*slope**3*c3}
    return add({-1: -1/sp.sympify(slope)}, multiply(differentiated, inverse_unit(unit), 3))


@lru_cache(maxsize=None)
def local(u, v, w, twisted):
    if not twisted:
        return {0: 1}, {}
    U, V, W = [exponential(-slope*q) for slope in (u, v, w)]
    half = sp.Rational(1, 2)
    den_inv = inverse_unit(add({0: 1}, scale(V, -half)))
    numerator = add(U, W, {0: -1}, scale(multiply(multiply(U, W), V), -half))
    local_factor = add({0: 3}, scale(V, -1), scale(multiply(numerator, den_inv), -1))
    # Partial derivative with respect to the third original shift, not the ray variable.
    local_third = scale(multiply(multiply(W, add({0: 1}, scale(multiply(U, V), -half))), den_inv), q)
    return local_factor, local_third


def d_term(u, v, twisted):
    factor, third = local(u, v, 0, twisted)
    return multiply(zeta(u+v), add(multiply(log_derivative(v), factor, 3), third), 3)


def i_ray(a, b, twisted):
    # Multiplying a pair of simple-pole series needs exp to order four.
    second = multiply(exponential(-(a+b)*L), d_term(-b, -a, twisted), 2)
    factor = local(a, 0, -b, twisted)[0]
    third = multiply(multiply(zeta(a), zeta(-b), 2), factor, 2)
    return add(d_term(a, b, twisted), second,
               scale(multiply(exponential(-b*L), third, 2), -1))


def j_ray(a, b, twisted):
    minus = add({0: 3}, scale(exponential(-a*q), -1),
                scale(exponential(-b*q), -1)) if twisted else {0: 1}
    plus = add({0: 3}, scale(exponential(a*q), -1),
               scale(exponential(b*q), -1)) if twisted else {0: 1}
    return scale(add(multiply(zeta(a+b), minus, 2),
                     multiply(exponential(-(a+b)*L), multiply(zeta(-a-b), plus, 2), 2)), L)


def quadratic_ray(a, b, twisted):
    combined = add(j_ray(a, b, twisted), i_ray(a, b, twisted), i_ray(b, a, twisted))
    assert combined.get(-2, 0) == 0 and combined.get(-1, 0) == 0
    return combined.get(2, 0)


def extract(twisted):
    ray_12 = quadratic_ray(1, 2, twisted)
    ray_13 = quadratic_ray(1, 3, twisted)
    cross = sp.expand(2*ray_12 - ray_13)
    pure = sp.expand((ray_12 - 2*cross)/5)
    assert sp.expand(quadratic_ray(2, 3, twisted) - 13*pure - 6*cross) == 0
    # At either shift zero and a zero of zeta, the finite shifted sum vanishes.
    assert pure == 0
    assert cross.coeff(L, 4) == sp.Rational(1, 12)
    return cross


def integrated(poly, sign):
    return sp.expand(sum(sign**k * sp.diff(poly, L, k) for k in range(5)))


def independent_untwisted_polynomial():
    """Milinovich P4 in Durkan–Hughes–Pearce-Crump (1.4)."""
    # Their gamma_j are the Stieltjes constants, with the alternating sign in zeta.
    g0, g1, g2, g3 = c0, -c1, 2*c2, -6*c3
    p1 = sp.Rational(1, 12)*L**4 + (2*g0-1)*L**3/3
    p1 += (1-2*g0+g0**2-2*g1)*L**2
    p1 += (-2+4*g0-2*g0**2-2*g0**3-10*g0*g1+4*g1-g2)*L
    p1 += (6+6*g0*(5*g1+4*g2-2)+6*g0**2*(g0+g0**2+6*g1+1)
           -12*g1+42*g1**2+3*g2+10*g3)/3
    return sp.expand(p1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--numeric", action="store_true", help="also show noncertified 25-digit coefficients")
    args = parser.parse_args()
    untwisted = extract(False)
    assert sp.expand(integrated(untwisted, -1) - independent_untwisted_polynomial()) == 0
    assert sp.expand(extract(True).subs(q, 0) - untwisted) == 0
    print("Independent untwisted polynomial and formal local-factor checks passed.")
    for title, twisted in (("Q=1", False), ("Q=2*2**(-s)-1", True)):
        differential = extract(twisted)
        cumulative, tail = integrated(differential, -1), integrated(differential, 1)
        print(title)
        for label, polynomial in (("density", differential), ("cumulative", cumulative), ("tail", tail)):
            print(label, sp.Poly(polynomial, L))
        if args.numeric:
            values = {q: sp.log(2), c0: sp.stieltjes(0),
                      c1: -sp.stieltjes(1), c2: sp.stieltjes(2)/2,
                      c3: -sp.stieltjes(3)/6}
            print("numeric tail coefficients (high to low)",
                  [sp.N(v.subs(values), 25) for v in sp.Poly(tail, L).all_coeffs()])
            if twisted:
                for height in (100, 400, 1000, 10**4, 10**6):
                    center = sp.log(height/(2*sp.pi))
                    value = tail.subs(values).subs(L, center) / (sp.pi*height)
                    print("noncertified tail main term at", height, sp.N(value, 20))
