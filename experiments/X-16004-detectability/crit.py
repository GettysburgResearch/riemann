"""PART 10: is 'NEVER' genuine?  The deepest excursion of lambda_min over delta.

For each configuration we scan delta on a log grid and record
   m = min_delta lambda_min(Q(delta))
If m > 0 the form NEVER loses positive definiteness, however far off the line
the pole is pushed -- the PSD background from the remaining poles dominates at
every delta.  If m < 0 the form does lose it, and |m| is the best signal any
observer could ever hope for.
"""
import sys, time
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *

PROFILE = sys.argv[1] if len(sys.argv) > 1 else "ladder"


def scan(N, mus, ws, star, dps=70, lo=-3, hi=4, pts=29, lo_exp=-40, steps=20):
    mp.mp.dps = dps
    Q0 = Q_of_delta(N, mus, ws, None, None)
    l0 = lambda_min(Q0, lo_exp=lo_exp, steps=steps)
    lmax0 = lambda_max(Q0)
    best = (l0, mp.mpf(0))
    for i in range(pts):
        e = mp.mpf(lo) + (mp.mpf(hi - lo) * i) / (pts - 1)
        d = mp.mpf(10) ** e
        lm = lambda_min(Q_of_delta(N, mus, ws, star, d), lo_exp=lo_exp, steps=steps)
        if lm < best[0]:
            best = (lm, d)
    return lmax0, l0, best


if PROFILE == "ladder":
    MUS = [mp.pi / 2 * k for k in range(1, 21)]
    WS = [mp.mpf(1)] * 20
    print("### PART 10 (ladder mu_k = k*pi/2, M=20, a=1): deepest excursion of lambda_min")
    print("  N  mu*      mu*/N   lam_max      lam_min(0)     min_delta lam_min   at delta     verdict")
    for N in (4, 6, 8, 10, 12):
        for star in (0, 4, 7, 19):
            t0 = time.time()
            lmax0, l0, (m, dm) = scan(N, MUS, WS, star)
            verdict = "loses PD" if m < 0 else "NEVER loses PD"
            print("  %-2d %8.3f %6.2f  %.4e  %+.6e  %+.6e     %.3e  %s  [%.0fs]"
                  % (N, float(MUS[star]), float(MUS[star]) / N, float(lmax0),
                     float(l0), float(m), float(dm), verdict, time.time() - t0))
            sys.stdout.flush()
