#!/usr/bin/env python3
"""Check the new three- and four-distinct interactions in the formal HLZ kernel."""
import sympy as sp

alpha, beta, gamma = sp.symbols("alpha beta gamma")


def reflected_cauchy_term(numerator):
    total = 0
    for a, b in ((alpha, beta), (beta, alpha)):
        tuples = ((a, b, gamma, 0), (-b, -a, gamma, -a-b),
                  (a, -gamma, -b, -b-gamma))
        for u, v, w, phase in tuples:
            total += v*numerator(u, v, w, phase)/((u+v)*(v+w))
    reduced = sp.cancel(sp.diff(total, gamma).subs(gamma, 0))
    return sp.factor(sp.diff(reduced, alpha, beta))


def check():
    cubic_j = -sp.Rational(1, 2)
    cubic_i = reflected_cauchy_term(lambda u, v, w, t: -t*(u+v+w)**3/8)
    cubic_with_square = reflected_cauchy_term(
        lambda u, v, w, t: (u*u+v*v+w*w)*(u+v+w)**2/16)
    quartic_i = reflected_cauchy_term(lambda u, v, w, t: (u+v+w)**4/16)
    assert 12*(cubic_j+cubic_i) == -24
    assert cubic_with_square == 0
    assert 12*quartic_i == 24
    print("Three linear variables (J, I, normalized):", cubic_j, cubic_i,
          12*(cubic_j+cubic_i))
    print("Three variables with one square (I):", cubic_with_square)
    print("Four linear variables (I, normalized):", quartic_i, 12*quartic_i)

    s, q, y = sp.symbols("s q y", real=True)
    coefficients = [1, -4*s+q, 6*s**2-s*q, -4*s**3, s**4]
    density = sum(c*sp.hermite_prob(i, y) for i, c in enumerate(coefficients))
    expected = (1-s*y)**4-6*s*s*(1-s*y)**2+3*s**4+q*(y-s*(y*y-1))
    assert sp.expand(density-expected) == 0
    assert sp.simplify(density.subs(y, 1/s+sp.sqrt(3))+q*(2*s+sp.sqrt(3))+6*s**4) == 0
    print("Signed density at the witness point:", sp.factor(density.subs(y, 1/s+sp.sqrt(3))))


if __name__ == "__main__":
    check()
