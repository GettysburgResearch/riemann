"""Why is delta_c NOT sqrt(lambda_min)?  Test the second-order model.

Expanding ell(mu+i d) = ell + i d ell' - (d^2/2) ell'' + O(d^3) (derivatives
in mu), the conjugate pair of weight a/2 each contributes

   a Re[ell(mu+id) ell(mu+id)^T]
     = a[ ell ell^T - d^2 ell' ell'^T - (d^2/2)(ell ell''^T + ell'' ell^T) ] + O(d^4)

so   Q(d) = Q(0) + d^2 B + O(d^4),
     B = -a sum_{mu in {+mu*,-mu*}} [ ell' ell'^T + (1/2)(ell ell''^T + ell'' ell^T) ].

Then delta_c^2 = 1/rho, rho = largest eigenvalue of -Q0^{-1/2} B Q0^{-1/2}
(a generalized eigenvalue of (-B, Q0)).  This is NOT lambda_min/||B||
unless B's negative direction aligns with Q0's bottom eigenvector.

We measure:
  * delta_c from the exact (all-orders) matrix           -> dc_exact
  * delta_c from the quadratic model Q0 + d^2 B          -> dc_quad
  * the alignment factor  align = (lambda_min(Q0)/lam_max(Q0)) / (dc^2 * rho_scaled)
    reported simply as the ratio dc_exact / sqrt(lambda_min(Q0)/lambda_max(Q0)),
    i.e. how far the true threshold sits above the naive conditioning guess.
"""
import sys, time
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *


def ell_d(mu, lam, k):
    """k-th derivative in mu of ell(mu)_j = 1/(lam_j-mu):  k!/(lam_j-mu)^{k+1}"""
    f = mp.factorial(k)
    return [f / (lj - mu) ** (k + 1) for lj in lam]


def build_B(N, mus, ws, star):
    lam = nodes(N)
    n = len(lam)
    B = [[mp.mpf(0)] * n for _ in range(n)]
    a = ws[star]
    for sgn in (1, -1):
        mu = sgn * mp.mpf(mus[star])
        e0 = ell_d(mu, lam, 0); e1 = ell_d(mu, lam, 1); e2 = ell_d(mu, lam, 2)
        for i in range(n):
            for j in range(n):
                B[i][j] -= a * (e1[i] * e1[j] + (e0[i] * e2[j] + e2[i] * e0[j]) / 2)
    return B


def quad_delta_c(N, mus, ws, star, lo_exp=-90, hi_exp=3, refine=32):
    lam = nodes(N)
    Q0 = Q_of_delta(N, mus, ws, None, None)
    B = build_B(N, mus, ws, star)
    n = len(Q0)

    def neg(logd):
        d2 = (mp.mpf(10) ** logd) ** 2
        M = [[Q0[i][j] + d2 * B[i][j] for j in range(n)] for i in range(n)]
        return n_neg(M)

    e = lo_exp; hi = None
    while e <= hi_exp:
        if neg(mp.mpf(e)) >= 1:
            hi = e; break
        e += 1
    if hi is None:
        return None
    a_, b_ = mp.mpf(hi - 1), mp.mpf(hi)
    for _ in range(refine):
        m = (a_ + b_) / 2
        if neg(m) >= 1:
            b_ = m
        else:
            a_ = m
    return mp.mpf(10) ** ((a_ + b_) / 2)


if __name__ == "__main__":
    gam = zeta_ordinates(20, dps=40)
    MUS = [g * mp.mpf("1.5") for g in gam]
    WS = [mp.mpf(1)] * 20
    print("N   dps  delta_c(exact)   delta_c(quadratic model)  rel.diff    "
          "sqrt(lmin/lmax)   ratio dc/naive")
    for N in (4, 6, 8, 10, 12):
        mp.mp.dps = 40 + 6 * N
        t0 = time.time()
        Q0 = Q_of_delta(N, MUS, WS, None, None)
        lmin = lambda_min(Q0); lmax = lambda_max(Q0)
        dce, _ = delta_critical(N, MUS, WS, 0, lo_exp=-90, hi_exp=3, refine=32)
        dcq = quad_delta_c(N, MUS, WS, 0)
        naive = mp.sqrt(lmin / lmax)
        print("%-3d %-4d %.8e   %.8e            %.2e   %.4e      %.3e   [%.0fs]"
              % (N, mp.mp.dps, float(dce), float(dcq), float(abs(dce - dcq) / dce),
                 float(naive), float(dce / naive), time.time() - t0))
        sys.stdout.flush()
