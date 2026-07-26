"""
pick.py -- the Nevanlinna-Pick criterion for RH, certified.

Agent: claude-01
Implements: the computational side of T-0005 / X-0011.

THE CRITERION

Because xi is entire of order 1 with zeros exactly at the nontrivial zeros of
zeta, Hadamard's factorisation gives

    F(s) := xi'(s)/xi(s)  =  sum_rho 1/(s - rho)          (paired rho, 1-rho).

If every zero lies on Re s = 1/2 then each summand maps the half-plane
Re s > 1/2 into Re w > 0, so F does too: **RH is exactly the statement that F is
a Herglotz (Nevanlinna) function of the half-plane Re s > 1/2.**

By the Nevanlinna-Pick theorem a function is Herglotz on a half-plane iff for
EVERY finite set of points alpha_1..alpha_N in it, the Pick matrix

    P_jk  =  ( F(alpha_j) + conj(F(alpha_k)) )
             / ( (alpha_j - 1/2) + conj(alpha_k - 1/2) )

is positive semidefinite.  Hence

    a certified NOT-PSD Pick matrix is a counterexample to RH,

and the witness is a finite Hermitian matrix -- the same format as T-0001
(Hermite-Hankel) and T-0002 (Weil positivity), but from a completely different
source: no contour, no primes, no zero-finding.

WHY IT MATTERS: IT BREAKS THE 1/delta WALL

Every other criterion in this repository resolves an off-line zero at depth
delta only at cost ~1/delta:

  * the classical Li coefficients need n ~ gamma^2/delta          (T-0003)
  * the Weil form needs a test function of bandwidth ~1/delta, hence
    exp(c/delta) prime powers                                     (T-0002, X-0006)
  * the targeted Li coefficients need the centre within delta of the ordinate,
    so a scan needs a grid of spacing delta                       (T-0004)
  * a winding contour must separate 1/2 - delta from 1/2          (L-0002)

The Pick matrix does not.  N points held at distance ~1 from the ordinate detect
delta = 1e-12 (measured, X-0011).  The cost moves out of the probe count and
into precision, where it is only logarithmic:

    |min pivot| ~ delta^3            (measured slope 3.0 +/- 0.6)
    baseline floor ~ 10^{-2.5 N}     (measured)
    so  N ~ (4/3) log10(1/delta) + 8  points at ~8.3 N bits suffice.

N = 1 recovers the Herglotz positivity Re F(alpha) >= 0, which by T-0004 is
exactly lambda_1^(alpha)/(2u) -- the first targeted Li coefficient.  So this is
the multi-point strengthening of T-0004, and the strengthening is what buys the
resolution.

SOUNDNESS OF THE ONE-POINT CASE (no citation needed)

Re F(1/2+u+iv) = sum_rho (u - beta_rho)/|alpha - rho|^2 with beta_rho =
Re rho - 1/2.  Every zero with Re rho <= 1/2 + u contributes a NONNEGATIVE term.
So a certified Re F < 0 forces a zero with Re rho > 1/2 + u, i.e.
|Re rho - 1/2| > u, with no domination argument anywhere.  The conclusion is
quantitative, not merely "RH is false".
"""

from __future__ import annotations

import sys

from flint import acb, arb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402

__all__ = ["xi_logderiv", "pick_matrix", "ldl_hermitian", "pick_certificate",
           "probe_cluster"]


def xi_logderiv(s, tol_bits: int = 200) -> acb:
    """Certified enclosure of xi'/xi at the point s (Re s > 1/2 assumed).

    xi = pi^{-s/2} Gamma(s/2+1) eta,  so

        xi'/xi = -log(pi)/2 + psi(s/2+1)/2 + eta'/eta .

    Costs one Euler-Maclaurin evaluation (eta and eta' together) and one
    digamma.  No zero of zeta is used."""
    s = acb(s)
    e, ep = cz.eta_and_deta(s, tol_bits=tol_bits)
    if e.contains(acb(0)):
        raise ValueError("eta enclosure contains 0; cannot divide")
    return -acb(arb.pi().log()) / 2 + (s / 2 + 1).polygamma(acb(0)) / 2 + ep / e


def pick_matrix(alphas, tol_bits: int = 200, F=None):
    """The Pick matrix of F = xi'/xi at the given points, in ball arithmetic."""
    Fv = [xi_logderiv(a, tol_bits) if F is None else F(a) for a in alphas]
    al = [acb(a) for a in alphas]
    n = len(al)
    return [[(Fv[j] + Fv[k].conjugate())
             / ((al[j] - acb(1) / 2) + (al[k] - acb(1) / 2).conjugate())
             for k in range(n)] for j in range(n)]


def ldl_hermitian(P):
    """Interval Hermitian LDL^H without pivoting.

    Returns (verdict, pivots) with verdict in {'PD', 'NOT_PSD', 'UNDECIDED'}.

    Soundness of 'NOT_PSD': without pivoting the k-th pivot is
    det(P_k)/det(P_{k-1}), so a certified negative pivot means two consecutive
    leading principal minors have opposite signs, which no PSD matrix admits.
    The same argument as hermite.ldl_signs, for Hermitian rather than real
    symmetric matrices; the elimination is the ordinary Schur complement, which
    keeps Hermitian matrices Hermitian because the pivots are real."""
    n = len(P)
    A = [row[:] for row in P]
    piv = []
    for k in range(n):
        d = A[k][k].real
        piv.append(d)
        if d < 0:
            return "NOT_PSD", piv
        if not (d > 0):
            return "UNDECIDED", piv
        for i in range(k + 1, n):
            f = A[i][k] / d
            for j in range(k, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return "PD", piv


def probe_cluster(v0, v1, N, u="0.05"):
    """N points evenly spaced in [v0, v1] at height 1/2 + u.

    The measured geometry of X-0011: hold every probe at distance >= D from the
    ordinate of interest and span [v0, v1] = [gamma+D, gamma+2D]."""
    lo, hi, uu = arb(repr(v0)), arb(repr(v1)), arb(u)
    return [acb(arb(1) / 2 + uu, lo + (hi - lo) * arb(j) / (N - 1))
            for j in range(N)]


def pick_certificate(alphas, tol_bits: int = 200, F=None):
    """Full pipeline: evaluate F, build the Pick matrix, take the LDL verdict."""
    P = pick_matrix(alphas, tol_bits, F=F)
    verdict, piv = ldl_hermitian(P)
    return {
        "N": len(alphas),
        "verdict": verdict,
        "min_pivot": min(float(p.mid()) for p in piv),
        "min_pivot_rad": max(float(p.rad()) for p in piv),
        "pivots": [str(p) for p in piv],
        "refutes_rh": verdict == "NOT_PSD",
    }
