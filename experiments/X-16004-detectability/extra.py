"""PART 7: peak signal strength over ALL delta, and PART 8: deeper M-convergence.

PART 7 matters because the signal is NON-monotone in delta: as delta -> infinity
the perturbed poles run off to infinity, ell(mu*+i delta) -> 0, and Q(delta)
tends to Q(0) with the starred rank-one terms simply deleted -- which is PSD
again.  So |lambda_min| has a maximum at some finite delta.  If that maximum,
relative to lambda_max, is below an observer's resolution, then that observer
can NEVER see the off-line pole at ANY displacement.
"""
import sys, time
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *

PART = sys.argv[1] if len(sys.argv) > 1 else "7"

_G = {}
def zeta_mus(M, Delta="1.5"):
    if M not in _G:
        _G[M] = zeta_ordinates(M, dps=40)
    return [g * mp.mpf(Delta) for g in _G[M]]


def peak_signal(N, mus, ws, star, dps=60, grid_lo=-3, grid_hi=4, pts=22,
                lo_exp=-25, steps=18, refine=14):
    """Coarse log-grid scan of lambda_min(Q(delta)) then ternary refine.

    Near the peak the negative eigenvalue is LARGE (1e-8..1e-1 relative), so
    the shifted matrices are well conditioned and a modest dps suffices; we
    verify selected cells at high dps separately.  lo_exp truncates the
    lambda_min search: values below 10^lo_exp*scale are irrelevant to a peak
    and are reported as 0, which never wins the argmin."""
    mp.mp.dps = dps
    Q0 = Q_of_delta(N, mus, ws, None, None)
    lmax0 = lambda_max(Q0)

    def lm_at(e):
        return lambda_min(Q_of_delta(N, mus, ws, star, mp.mpf(10) ** e),
                          lo_exp=lo_exp, steps=steps)

    best = (mp.mpf(0), None)
    curve = []
    for i in range(pts):
        e = mp.mpf(grid_lo) + (mp.mpf(grid_hi - grid_lo) * i) / (pts - 1)
        lm = lm_at(e)
        curve.append((float(e), lm))
        if lm < best[0]:
            best = (lm, e)
    if best[1] is not None:
        step = mp.mpf(grid_hi - grid_lo) / (pts - 1)
        a, b = best[1] - step, best[1] + step
        for _ in range(refine):
            m1 = a + (b - a) / 3
            m2 = b - (b - a) / 3
            if lm_at(m1) < lm_at(m2):
                b = m2
            else:
                a = m1
        epk = (a + b) / 2
        pk = lm_at(epk)
    else:
        epk, pk = None, mp.mpf(0)
    return lmax0, pk, epk, curve


if PART == "7":
    print("### PART 7: peak |lambda_min| over all delta  (zeta profile, M=20, a=1)")
    print("  'digits needed' = log10(lambda_max / |peak lambda_min|): an observer with")
    print("  fewer significant digits than this can NEVER detect this off-line pole,")
    print("  at any displacement delta.")
    MUS = zeta_mus(20); WS = [mp.mpf(1)] * 20
    for N in (6, 10, 14):
        for star in (0, 1, 2, 3, 4, 6, 9):
            dps = 60
            t0 = time.time()
            lmax0, pk, epk, _ = peak_signal(N, MUS, WS, star, dps)
            need = mp.log10(lmax0 / abs(pk)) if pk != 0 else mp.inf
            print("  N=%2d mu*=%7.3f (gamma_%d)  lam_max=%.4e  peak lam_min=%.6e at delta=%.4e"
                  "  ratio=%.4e  digits needed=%.2f  [%.0fs]"
                  % (N, float(MUS[star]), star + 1, float(lmax0), float(pk),
                     float(10 ** epk) if epk is not None else -1,
                     float(abs(pk) / lmax0), float(need), time.time() - t0))
            sys.stdout.flush()
    print("  -- dps check on selected cells (dps 60 vs 150) --")
    for N, star in ((10, 0), (10, 3), (14, 1)):
        for dps in (60, 150):
            lmax0, pk, epk, _ = peak_signal(N, MUS, WS, star, dps)
            print("     N=%2d star=%d dps=%3d  peak lam_min=%.8e  ratio=%.6e"
                  % (N, star, dps, float(pk), float(abs(pk) / lmax0)))
            sys.stdout.flush()

if PART == "8":
    print("### PART 8: deeper pole-count convergence at N=8 and N=10 (star=0)")
    for N in (8, 10):
        prev = None
        for M in (20, 30, 40, 60, 80, 100):
            MUS = zeta_mus(M); WS = [mp.mpf(1)] * M
            dps = 40 + 6 * N
            mp.mp.dps = dps
            t0 = time.time()
            Q0 = Q_of_delta(N, MUS, WS, None, None)
            inr = inertia(Q0); lmin0 = lambda_min(Q0); lmax0 = lambda_max(Q0)
            dc, _ = delta_critical(N, MUS, WS, 0, lo_exp=-90, hi_exp=3, refine=32)
            ch = "" if prev is None else "  change x%.4f" % float(dc / prev)
            prev = dc
            print("  N=%2d M=%3d inertia=%-11s lam_max=%.4e lam_min0=%.6e delta_c=%.8e%s [%.0fs]"
                  % (N, M, str(inr), float(lmax0), float(lmin0), float(dc), ch, time.time() - t0))
            sys.stdout.flush()
