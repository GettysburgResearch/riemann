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


def xi_taylor_at(centre, p: int, tol_bits: int = 200, R="2.0"):
    """Taylor coefficients of xi(centre + x) up to order p-1, certified.

    Same construction as xi_taylor_at_one but about an arbitrary centre, which
    is what the generalised (targeted) Li coefficients need."""
    c = acb(centre)
    Rr = arb(R)
    E, _mag, params = cz.eta_taylor_coeffs(c, p, tol_bits=tol_bits)
    ball = acb(arb(c.real.mid(), Rr.upper()), arb(c.imag.mid(), Rr.upper()))
    em = cz._em_error_radius(ball, params.N, params.M)
    # eta carries the remainder as (s-1)E; |[(s-1)E]_k| <= |c-1| em/R^k + em/R^{k-1}
    E = list(E)
    for k in range(p):
        b = em / Rr ** k * arb((ball - 1).abs_upper())
        if k >= 1:
            b = b + em / Rr ** (k - 1)
        pad = arb(0, b.upper())
        E[k] = E[k] + acb(pad, pad)

    # pi^{-s/2} at s = c + x
    lp = arb.pi().log()
    u = [acb(0)] * p
    if p > 1:
        u[1] = acb(-lp / 2)
    P = _exp_series(u, p)
    P = [((-c / 2) * acb(lp)).exp() * q for q in P]

    # Gamma(s/2+1) at s = c + x  is  Gamma(c/2 + 1 + x/2)
    z0 = c / 2 + 1
    lg = [acb(0)] * p
    lg[0] = z0.lgamma()
    for k in range(1, p):
        lg[k] = z0.polygamma(acb(k - 1)) / (acb(2) ** k * acb(factorial(k)))
    G = _exp_series([acb(0)] + lg[1:], p)
    G = [lg[0].exp() * q for q in G]

    return _mul(_mul(P, G, p), E, p)


def li_general(alpha, nmax: int, tol_bits: int = 300, R="2.0"):
    """Generalised (targeted) Li coefficients.

    The classical lambda_n use the Mobius map s = 1/(1-z), which sends the unit
    disc onto Re s > 1/2 with z = 0 at s = 1.  EVERY map

        s = 1/2 + (a + conj(a) z)/(1 - z),      a = alpha - 1/2, Re a > 0,

    does the same, now with z = 0 at s = alpha, and each gives an equivalent
    criterion: lambda_n^(alpha) >= 0 for all n iff every zero has Re rho >= 1/2.

    Why bother: an off-critical zero at 1/2 - delta + i gamma is mapped to a
    point of modulus

        sqrt((u+delta)^2 + (gamma-v)^2) / sqrt((u-delta)^2 + (gamma-v)^2),
        alpha = 1/2 + u + i v,

    which for the classical choice (u = 1/2, v = 0) is 1 + O(delta/gamma^2) --
    the reason lambda_n needs n ~ gamma^2/delta to see anything -- but is
    UNBOUNDED as u -> delta, v -> gamma.  Aiming alpha at a suspected zero
    therefore turns an exponentially slow criterion into a fast one.

    Implementation note: with x = s - alpha one gets x = 2u z/(1-z), i.e. the
    same composition as the classical case up to the scale 2u.  So this is the
    classical routine with the expansion re-centred at alpha and the composition
    rescaled."""
    al = acb(alpha)
    u = al.real - arb(1) / 2
    if not (u > 0):
        raise ValueError("need Re(alpha) > 1/2")
    p = nmax + 2
    C = xi_taylor_at(al, p, tol_bits, R)
    scale = 2 * u
    # x = scale * z/(1-z);  (z/(1-z))^k = z^k sum_j C(k+j-1,j) z^j
    F = [acb(0)] * p
    for k, ck in enumerate(C):
        if ck == 0:
            continue
        t = ck * acb(scale) ** k
        for j in range(0, p - k):
            F[k + j] += t * acb(comb(k + j - 1, j) if k > 0 else (1 if j == 0 else 0))
    L = _log_series(F, p)
    return [acb(n) * L[n] for n in range(1, nmax + 1)]


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
