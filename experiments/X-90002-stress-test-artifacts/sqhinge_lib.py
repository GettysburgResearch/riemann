"""Square-root hinge carry inverse: exact reference implementations.

Definitions implemented (quoted from repo):
  D-23801.1: beta_{nq} = floor(n/q)*(q-1-(n mod q))/(n+1)
  T-32301.1 / D-23801.5: h_T(q) = sum_{n=q}^T c_T(n) beta_{nq}  (i.e. B^T c = h)
  L-32701.4: c_T(j) = ((j+1)[j u_j - (j-2) u_{j+1}] + 2 sum_{m=j+2}^T u_m)/(j(j-1)),
             u_m = sum_{k<=T/m} mu(k) w(mk)
  L-32701.6/7: K_j = (f_j * mu)/(j(j-1)), f_j(d) = -2 (d<=j-1), (j+2)(j-1) (d=j), -j(j-1) (d=j+1)
"""
from fractions import Fraction


def mobius_sieve(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    comp = [False] * (n + 1)
    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def beta(n, q):
    a = n // q
    r = n - q * a
    return Fraction(a * (q - 1 - r), n + 1)


def solve_direct(T, w):
    """Exact back-substitution of B^T c = w (w indexed 2..T)."""
    c = {}
    for q in range(T, 1, -1):
        s = w[q]
        for n in range(q + 1, T + 1):
            b = beta(n, q)
            if b:
                s -= c[n] * b
        c[q] = s / beta(q, q)
    return c


def f_coeff(j, d):
    if d <= j - 1:
        return -2
    if d == j:
        return (j + 2) * (j - 1)
    return -j * (j - 1)
