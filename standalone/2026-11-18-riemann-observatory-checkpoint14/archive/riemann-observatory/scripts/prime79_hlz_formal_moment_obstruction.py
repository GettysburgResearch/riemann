#!/usr/bin/env python3
"""Check the HLZ squarefree kernel and an exact-coefficient finite Hankel witness."""

import json
from fractions import Fraction
from itertools import combinations, product
from math import factorial

import sympy as sp
from flint import __FLINT_VERSION__, arb, ctx


alpha, beta, aux = sp.symbols("alpha beta aux")


def exponential_numerator(factors, time, degree):
    return sp.Add(*(sp.prod(weight for _, weight in terms)
                    * (time+sum(exponent for exponent, _ in terms))**degree
                    for terms in product(*factors)))


def three_i_terms(a, b, c, residue):
    return (residue(a, b, c, 0)+residue(-b, -a, c, -a-b)
            +residue(a, -c, -b, -b-c))


def i_ab_coefficient(residue):
    reflected = (three_i_terms(alpha, beta, aux, residue)
                 +three_i_terms(beta, alpha, aux, residue))
    after_auxiliary = sp.cancel(sp.diff(reflected, aux).subs(aux, 0))
    return sp.Poly(after_auxiliary, alpha, beta).coeff_monomial(alpha*beta)


def kernel_small(xs):
    states = 2**len(xs)
    direct = [[(-alpha*x, 1), (-beta*x, 1)] for x in xs]
    dual = [[(alpha*x, 1), (beta*x, 1)] for x in xs]
    j = (exponential_numerator(direct, 0, 3)
         -exponential_numerator(dual, -alpha-beta, 3))/(6*states*(alpha+beta))
    j_ab = sp.Poly(sp.cancel(j), alpha, beta).coeff_monomial(alpha*beta)

    def residue(u, v, w, time):
        factors = [[(-u*x, 1), (-v*x, 1), (-w*x, 1), (0, -1)] for x in xs]
        return (v*exponential_numerator(factors, time, 4)
                /(24*states*(u+v)*(v+w)))

    return sp.expand(12*(j_ab+i_ab_coefficient(residue)))


def symbolic_checks():
    frequencies = sp.symbols("x:4")
    for order in range(4):
        xs = frequencies[:order]
        expected = (1+sum(-4*x+2*x**3 for x in xs)
                    +sum(12*x*y-2*x*y*(x*x+y*y) for x, y in combinations(xs, 2))
                    -24*sum(x*y*z for x, y, z in combinations(xs, 3)))
        assert sp.expand(kernel_small(xs)-expected) == 0

    def squarefree_four(u, v, w, time):
        # Selecting one linear coefficient from each of four factors consumes
        # all four shift degrees, so exp(time) contributes only its constant.
        return v*(u+v+w)**4/(16*(u+v)*(v+w))

    fourth = 12*i_ab_coefficient(squarefree_four)
    assert fourth == 24

    d, q, z = sp.symbols("d q z")
    integrated = 1+(-4*d+q)*z+(6*d*d-d*q)*z*z-4*d**3*z**3+d**4*z**4
    assert sp.expand(integrated-((1-d*z)**4+q*z*(1-d*z))) == 0

    s, qp, y = sp.symbols("s qp y")
    coefficients = (1, -4*s+qp, 6*s*s-s*qp, -4*s**3, s**4)
    factor = sum(c*sp.hermite_prob(k, y) for k, c in enumerate(coefficients))
    expected = (1-s*y)**4-6*s*s*(1-s*y)**2+3*s**4+qp*(y-s*(y*y-1))
    assert sp.expand(factor-expected) == 0
    assert sp.simplify(factor.subs(y, 1/s+sp.sqrt(3))+6*s**4+qp*(sp.sqrt(3)+2*s)) == 0
    return int(fourth)


def gaussian_hermite_integral(degree, index, shift):
    """E[He_index(G) (sum_{j<=degree} shift^j He_j(G)/j!)^2] exactly."""
    total = Fraction()
    for i in range(degree+1):
        for j in range(max(0, i-index), min(degree, i+index)+1):
            a, b, c = i+j-index, i+index-j, j+index-i
            if min(a, b, c) >= 0 and a % 2 == 0:
                denominators = factorial(a//2)*factorial(b//2)*factorial(c//2)
                total += shift**(i+j)*Fraction(factorial(index), denominators)
    return total


def ball(q):
    return arb(q.numerator)/q.denominator


def witness(degree, s, q):
    shift = Fraction(13, 2)
    normal = gaussian_hermite_integral(degree, 0, shift)
    coefficients = (1, -4*s+q, 6*s*s-s*q, -4*s**3, s**4)
    return sum(value*ball(gaussian_hermite_integral(degree, k, shift)/normal)
               for k, value in enumerate(coefficients))


if __name__ == "__main__":
    ctx.prec = 160
    sigma = (arb(2).log()/2).sqrt()
    s, q = arb(1)/(20*sigma), arb(7)/(12000*sigma)
    attempts = {n: witness(n, s, q) for n in (30, 40, 50, 60, 70)}
    assert all(attempts[n] > 0 for n in (30, 40, 50, 60))
    assert attempts[70] < arb("-0.00118")
    print(json.dumps({
        "squarefree_degree_four_coefficient": symbolic_checks(),
        "band": ["1/20", "1/10"], "hermite_shift": "13/2",
        "witness_uses_formal_moments_through": 140, "arb_precision": ctx.prec,
        "flint": __FLINT_VERSION__,
        "normalized_formal_squared_values_by_degree": {str(k): str(v) for k, v in attempts.items()},
    }, indent=2))
