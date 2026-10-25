"""Finite arithmetic and polynomial quadrature check of the shift bridge.

This checks signs, both H factors, and the exact Stieltjes remainder.
It does not test an asymptotic zero-free claim.
"""
import json
import math
from fractions import Fraction

import numpy as np
from numpy.polynomial import Polynomial as Poly
from numpy.polynomial.legendre import leggauss


def arithmetic(limit):
    mu = np.ones(limit + 1, dtype=np.int64)
    mu[0] = 0
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    lam = np.zeros(limit + 1)
    for p in range(2, limit + 1):
        if prime[p]:
            prime[2*p::p] = False
            mu[p::p] *= -1
            mu[p*p::p*p] = 0
            q = p
            while q <= limit:
                lam[q] = math.log(p)
                q *= p
    return mu, lam, np.cumsum(mu), np.cumsum(lam)


u1, u2 = Poly([-1, 1]), Poly([2, -1])
W = u1**2 * u2**2
Wp = W.deriv()
K = 140 * u1**3 * u2**3
Kp, Kpp = K.deriv(), K.deriv(2)
nodes, weights = leggauss(8)


def integrate_polynomial(f, a, b):
    xs = (a+b)/2 + nodes*(b-a)/2
    return (b-a)/2 * np.dot(weights, f(xs))


def check(X, H):
    mu, lam, M, psi = arithmetic(2*X + 1)
    MW = sum(mu[n] * W(n/X) for n in range(X, 2*X + 1))
    S = sum(
        K(h/H) * sum(mu[n]*lam[n-h]*W(n/X)
                      for n in range(X, 2*X + 1))
        for h in range(H + 1, 2*H)
    )
    direct = S - H*MW

    # For integer H, all changes of the polynomial piece of the nested
    # integral occur at integer u. Both 8-node quadratures are exact
    # for their polynomial degree; floating point roundoff remains.
    remainder = 0.0
    for j in range(X, 2*X):
        def outer(us):
            vals = []
            for u in us:
                lo, hi = u - 2*H, u - H
                cuts = [lo] + list(range(math.floor(lo) + 1,
                                         math.ceil(hi))) + [hi]
                total = 0.0
                for a, b in zip(cuts, cuts[1:]):
                    k = math.floor((a+b)/2)
                    def inner(ts):
                        v = (u-ts)/H
                        kernel = Wp(u/X)*Kp(v)/(X*H)
                        kernel += W(u/X)*Kpp(v)/(H*H)
                        return (psi[k] - ts) * kernel
                    total += integrate_polynomial(inner, a, b)
                vals.append(-M[j] * total)
            return np.asarray(vals)
        remainder += integrate_polynomial(outer, j, j+1)
    error = abs(remainder-direct)
    assert error < 3e-8 * max(1, abs(direct)), (X, H, error)
    return dict(X=X, H=H, S=S, M_W=MW,
                direct_centered=direct, double_stieltjes=remainder,
                absolute_error=error)


if __name__ == "__main__":
    results = [check(40, 5), check(80, 10), check(120, 12)]
    beta = 0.874886647039964
    theta = 0.98
    exponents = [beta]
    for _ in range(3):
        exponents.append(2*exponents[-1]+1-2*theta)
    rational = [Fraction(7, 8)]
    for _ in range(3):
        rational.append(2*rational[-1] + 1 - 2*Fraction(49, 50))
    assert rational == [Fraction(7, 8), Fraction(79, 100),
                        Fraction(31, 50), Fraction(7, 25)]
    print(json.dumps({"checks": results, "unclipped_exponents": exponents,
                      "conditional_rational_example": [str(q) for q in rational]},
                     indent=2))
