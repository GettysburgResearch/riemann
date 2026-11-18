"""Exact symbolic and finite-weight checks of the multiplicity transform."""
from math import comb, factorial

import sympy as sy


def check():
    mu, b, s = sy.symbols('mu b s')
    degree = 9
    coefficients = [
        sy.prod(mu - j * (j + 1) for j in range(i + 1))
        / (factorial(i) * factorial(i + 1))
        for i in range(degree)
    ]
    transform = [
        sy.expand(sum(sy.Rational(comb(k - 1, ell - 1), ell)
                      * sum(coefficients[i] * coefficients[ell - 1 - i] for i in range(ell))
                      for ell in range(1, k + 1)))
        for k in range(1, degree + 1)
    ]
    assert transform[:2] == [mu**2, mu**3 / 2]
    weights = {1: sy.Rational(1, 17), 2: sy.Rational(2, 5),
               4: sy.Rational(1, 7), 8: sy.Rational(3, 19)}
    series = 0
    for m, weight in weights.items():
        derivative = sy.diff(sy.legendre(m - 1, 1 + 2*s), s)
        polynomial = m*m + sy.integrate(sy.expand(derivative**2), (s, 0, s))
        series += weight * sy.series(polynomial.subs(s, b/(1-b)), b, 0, degree+1).removeO()

    recovered = []
    for k, polynomial in enumerate(transform, 1):
        row = sy.Poly(sy.cancel(polynomial/mu**2), mu)
        expected = sy.Rational(comb(2*k, k), factorial(k)*factorial(k+1))
        assert row.degree() == k-1 and row.LC() == expected
        observed = sy.expand(series).coeff(b, k)
        lower_terms = sum(row.nth(j) * recovered[j] for j in range(k-1))
        recovered.append((observed-lower_terms)/row.LC())
        assert recovered[-1] == sum(weight*(m*(m-1))**(k+1)
                                    for m, weight in weights.items() if m >= 2)
    assert sy.expand(series).coeff(b, 0) == sum(weight*m*m for m, weight in weights.items())
    for length in range(degree):
        sites = [(m, m*(m-1)) for m in range(2, length+3)]
        barycentric = [
            sy.S.One / sy.prod(site-other for _, other in sites if site != other)
            for _, site in sites
        ]
        assert all(sum(a*site**j for a, (_, site) in zip(barycentric, sites)) == 0
                   for j in range(length))
        assert sum(a*site**length for a, (_, site) in zip(barycentric, sites)) == 1
        positive = {m: max(a, sy.S.Zero)/site**2 for a, (m, site) in zip(barycentric, sites)}
        negative = {m: max(-a, sy.S.Zero)/site**2 for a, (m, site) in zip(barycentric, sites)}
        cost_positive = sum(m*m*w for m, w in positive.items())
        cost_negative = sum(m*m*w for m, w in negative.items())
        mass = max(cost_positive, cost_negative)
        positive[1], negative[1] = mass-cost_positive, mass-cost_negative
        assert positive != negative and min([*positive.values(), *negative.values()]) >= 0
        assert sum(m*m*w for m, w in positive.items()) == sum(m*m*w for m, w in negative.items())
        difference = [sum((positive[m]-negative[m])*polynomial.subs(mu, m*(m-1))
                          for m in positive) for polynomial in transform[:length+1]]
        assert difference[:-1] == [0]*length and difference[-1] > 0

    print('SymPy version', sy.__version__)
    print('Leading coefficients checked to order', degree)
    print('First four polynomials:', transform[:4])
    print('All synthetic moments recovered exactly')
    print('Finite nonnegative ambiguity checked for K = 0 to 8')


if __name__ == '__main__':
    check()
