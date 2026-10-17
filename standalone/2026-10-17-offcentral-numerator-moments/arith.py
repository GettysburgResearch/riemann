"""Exact rational utilities adapted from the recovered #967 verifier.
Polynomial/Bernstein and DF density formulas are inherited and credited.
Only the scale constants change here. No floating arithmetic is used.
"""
import math
from fractions import Fraction as F
EMAX=F(1,10**6)
A,H,Z0=F(4,9),F(5,9),F(2,5)
TARGET=F(2,9)

def poly(x):
    if isinstance(x, (int, F)):
        return (F(x),)
    v = tuple(F(y) for y in x)
    while len(v) > 1 and v[-1] == 0:
        v = v[:-1]
    return v or (F(0),)


def add(x, y):
    x, y = poly(x), poly(y)
    return poly(tuple((x[i] if i < len(x) else 0) +
                      (y[i] if i < len(y) else 0)
                      for i in range(max(len(x), len(y)))))


def neg(x):
    return tuple(-a for a in poly(x))


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    x, y = poly(x), poly(y)
    z = [F(0)] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i+j] += a*b
    return poly(z)


def scale(x, a):
    return mul(x, F(a))


def bernstein(x):
    """Bernstein coefficients of p(EMAX*t), 0<=t<=1."""
    x = poly(x)
    n = len(x)-1
    return tuple(sum(x[i]*EMAX**i * F(math.comb(k, i), math.comb(n, i))
                     for i in range(k+1)) for k in range(n+1))


def closed_nonnegative(x):
    return all(b >= 0 for b in bernstein(x))


def open_positive(x):
    """Sufficient exact certificate: strictly positive for 0<e<=EMAX."""
    b = bernstein(x)
    if len(b) == 1:
        return b[0] > 0
    return b[0] >= 0 and all(v > 0 for v in b[1:])


E = (F(0), F(1))
ONE_E = add(1, E)


def real_exponent(x, y, z):
    return add(add(A/2-1, x), add(scale(z, H), scale(sub(y, 1), A)))


def domain(x, y, z):
    return (
        x, y, z, sub(add(scale(z, 6), y), 1),
        sub(add(x, scale(z, 6)), 1), sub(add(x, y), 1),
        sub(add(add(x, y), scale(z, 6)), 2),
        sub(add(scale(x, 6), scale(z, 6)), 5),
        sub(x, F(1, 2)), sub(scale(x, 3), 2),
        sub(add(scale(x, 3), y), F(5, 2)))


def density(sigma):
    n, q = 6, 2*sigma-1
    if n*q <= 2:
        r, s = F(1, 2), 2/(4-n*q)
        g = 1-q/(4-n*q)
        branch = 'low'
    elif n*q <= n-1:
        den = n*q*(2*(n-1)-n*q)-2*(n-1)
        r = (n*q*(n-2)-(n-1))/den
        s = (n*q*(2*n-5)-2*(n-2))/den
        g = ((2*n-3)*q*(n+1-n*q)-2*(n-1))/den
        branch = 'middle'
    else:
        den = 1-n*(1-q)**2
        r = (n*q-n+2)/den
        s = ((n+2)*q-n+1)/den
        g = (1-q)*((n+2)*q-n+1)/den
        branch = 'upper'
    z = 1/(6-4*sigma)
    ht = (1-sigma)/(3-2*sigma)
    roots = (r, F(1), r/3+F(5, 6), 5*r/6+F(1, 3))
    powers = [F(1, 2)+(F(1, 2)-sigma)*s+t/2 for t in roots]
    powers += [(2-2*sigma)*s, 1+(1-2*sigma)*r]
    height = [F(1, 4)+(F(1, 2)-sigma)*z]*4
    height += [(2-2*sigma)*z, F(0)]
    for c, vpower in ((F(1, 3), F(11, 6)-2*sigma),
                       (F(5, 6), F(4, 3)-2*sigma)):
        powers += [c+vpower*r, c+vpower*s]
        height += [F(0), vpower*z]
    # An algebraically independent form copied from Corollary 1.5.
    if sigma <= F(2, 3):
        delta = (2*sigma-1)/((1-2*sigma)*n+4)
    elif sigma <= F(11, 12):
        delta = ((2*sigma-1)*((2*sigma-1)*n*n-(6*sigma-2)*n+3)
                 / ((2*sigma-1)*(3-2*sigma)*n*n-4*sigma*n+2))
    else:
        delta = (8*sigma*sigma-10*sigma+3)/(1-4*(1-sigma)**2*n)
    return dict(sigma=sigma, r=r, s=s, z=z, g=g, height=ht,
                norm_terms=powers, height_terms=height,
                corollary_g=1-delta, branch=branch)


def encode(obj):
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, dict):
        return {str(k): encode(v) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [encode(v) for v in obj]
    return obj


