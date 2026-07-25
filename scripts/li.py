"""
li.py -- certified Li coefficients.

Agent: claude-01
Implements: the computational side of T-0003 / X-0009.

LI'S CRITERION (1997).  With

    lambda_n  =  sum_rho [ 1 - (1 - 1/rho)^n ]        (paired over rho, 1-rho)

the Riemann hypothesis is equivalent to  lambda_n >= 0  for every n >= 1.
So **a certified negative lambda_n is a counterexample**, and it is a single
real number -- the most compact witness format imaginable.

HOW THEY ARE COMPUTED HERE (no zeros needed)

Li's coefficients are the Taylor coefficients of log xi under the Mobius change
of variable z = 1 - 1/s, i.e. s = 1/(1-z):

    log xi(1/(1-z))  =  log xi(1)  +  sum_{n>=1} (lambda_n / n) z^n .

So the recipe is:

  1. Taylor-expand xi about s = 1 to order p.  xi = pi^{-s/2} Gamma(s/2+1) eta(s)
     with eta = (s-1) zeta(s); eta's coefficients come from the certified
     Euler-Maclaurin Taylor model (L-0006), the pi power is elementary, and
     Gamma(s/2+1) is expanded through log Gamma using polygamma values at 3/2.
  2. Compose with s = 1/(1-z), using (z/(1-z))^k = z^k sum_j C(k+j-1, j) z^j.
  3. Take the logarithm of the resulting series by the standard recurrence.
  4. lambda_n = n * [z^n].

Everything is ball arithmetic, so each lambda_n comes with a rigorous
enclosure, and a certified negative value would be a proof.
"""

from __future__ import annotations

import sys
from math import comb, factorial

from flint import acb, arb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402

__all__ = ["li_coefficients", "xi_taylor_at_one"]


def _mul(a, b, p):
    out = [acb(0)] * p
    for i, ai in enumerate(a[:p]):
        if ai == 0:
            continue
        for j, bj in enumerate(b[: p - i]):
            out[i + j] += ai * bj
    return out


def _exp_series(u, p):
    """exp of a series with zero constant term, by E' = u' E."""
    E = [acb(0)] * p
    E[0] = acb(1)
    for n in range(1, p):
        acc = acb(0)
        for k in range(1, n + 1):
            acc += acb(k) * u[k] * E[n - k]
        E[n] = acc / n
    return E


def _log_series(F, p):
    """log of a series with F[0] != 0, by L' F = F'."""
    L = [acb(0)] * p
    L[0] = F[0].log()
    for n in range(1, p):
        acc = acb(n) * F[n]
        for k in range(1, n):
            acc -= acb(k) * L[k] * F[n - k]
        L[n] = acc / (acb(n) * F[0])
    return L


def xi_taylor_at_one(p: int, tol_bits: int = 200, R="2.0"):
    """Taylor coefficients of xi(1 + x) up to order p-1, certified.

    `eta_taylor_coeffs` returns the coefficients of the TRUNCATED
    Euler-Maclaurin expression; the omitted remainder E_{M,N} is analytic, so by
    Cauchy on the circle |s-1| = R its Taylor coefficients obey
    |E_k| <= sup_{|s-1|<=R} |E| / R^k.  eta contains the remainder as (s-1)E,
    whose k-th coefficient is E_{k-1}; so coefficient 0 is exact and each
    coefficient k >= 1 carries an extra disc of radius em(R)/R^{k-1}.

    Forgetting this was a real error (see NEGATIVE_RESULTS R-0008): the
    enclosures came out at 1e-239 when the truncation alone is 1e-61, i.e. the
    "certified" intervals were a hundred orders of magnitude too tight.

    R should be taken LARGER than 1, not smaller: the bound carries R^{-k}, so a
    big circle makes the high-order coefficients cheap.  Measured at n = 150:
    R = 0.5 gives enclosures of 6e-66, R = 2 gives 5e-104."""
    one = acb(1)
    R = arb(R)

    # eta(1 + x)
    E, _mag, params = cz.eta_taylor_coeffs(one, p, tol_bits=tol_bits)
    ball = acb(arb(1, R.upper()), arb(0, R.upper()))
    em = cz._em_error_radius(ball, params.N, params.M)
    E = list(E)
    for k in range(1, p):
        pad = arb(0, (em / R ** (k - 1)).upper())
        E[k] = E[k] + acb(pad, pad)

    # pi^{-s/2} = exp(-(1+x)/2 log pi) = pi^{-1/2} exp(-(x/2) log pi)
    lp = arb.pi().log()
    u = [acb(0)] * p
    if p > 1:
        u[1] = acb(-lp / 2)
    P = _exp_series(u, p)
    P = [acb(arb.pi() ** (arb(-1) / 2)) * c for c in P]

    # Gamma(s/2 + 1) at s = 1 + x  is  Gamma(3/2 + x/2)
    #   log Gamma(3/2 + x/2) = log Gamma(3/2) + sum_{k>=1} psi^{(k-1)}(3/2) (x/2)^k / k!
    lg = [acb(0)] * p
    lg[0] = acb(arb(3) / 2).lgamma()
    for k in range(1, p):
        pg = acb(arb(3) / 2).polygamma(acb(k - 1))
        lg[k] = pg / (acb(2) ** k * acb(factorial(k)))
    G = _exp_series([acb(0)] + lg[1:], p)
    G = [lg[0].exp() * c for c in G]

    return _mul(_mul(P, G, p), E, p)


def li_coefficients(nmax: int, tol_bits: int = 200, R="2.0"):
    """Certified lambda_1 .. lambda_nmax."""
    p = nmax + 2
    C = xi_taylor_at_one(p, tol_bits, R)

    # compose with s = 1/(1-z):  x = s - 1 = z/(1-z),
    #   (z/(1-z))^k = z^k * sum_j C(k+j-1, j) z^j
    F = [acb(0)] * p
    for k, ck in enumerate(C):
        if ck == 0:
            continue
        for j in range(0, p - k):
            F[k + j] += ck * acb(comb(k + j - 1, j) if k > 0 else (1 if j == 0 else 0))

    L = _log_series(F, p)
    return [acb(n) * L[n] for n in range(1, nmax + 1)]


if __name__ == "__main__":
    cz.set_prec(600)
    lam = li_coefficients(10)
    known = [0.0230957, 0.0923457, 0.207639, 0.368791, 0.575543,
             0.827566, 1.12488, 1.46754, 1.85502, 2.28687]
    for n, (v, k) in enumerate(zip(lam, known), start=1):
        print(f"  lambda_{n:<2} = {str(v.real)[:34]}   (known {k})")
