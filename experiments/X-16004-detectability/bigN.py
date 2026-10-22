"""PART 9: push N until the perturbed pole enters the node band.

With Delta=1.5 the first zeta pole sits at mu_1 = 1.5*14.1347 = 21.202.  The
nodes are the integers -N..N, so the pole is OUTSIDE the sampled interval for
every N <= 21 and only enters it at N >= 22.  Everything in PART 1 (N<=14) is
therefore extrapolation from outside the band.  This part crosses that line.

Trimmed relative to PART 1: only lambda_min, lambda_max, delta_c and
delta_det(16) are computed (delta_det(30/50) are dropped), and each bisection
gets a tight scan floor, because the full PART-1 row costs ~800 inertia calls
and that is unaffordable at dim 49.
"""
import sys, time
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *

M = 20
gam = zeta_ordinates(M, dps=40)
MUS = [g * mp.mpf("1.5") for g in gam]
WS = [mp.mpf(1)] * M

# quadratic fit from PART 1 (4<=N<=14): log10 delta_c = 1.6634 -0.5316 N -0.05618 N^2
def floor_for(N):
    pred = 1.6634 - 0.5316 * N - 0.05618 * N * N
    return int(pred) - 25          # 25 decades of headroom below the prediction

print("### PART 9: zeta profile, star=0 (mu_1=%.4f), M=20, a=1" % float(MUS[0]))
print("  mu_1/N < 1 means the perturbed pole lies INSIDE the node band (N >= 22).")
for N in (16, 18, 20, 22, 24):
    dps = 40 + 6 * N
    mp.mp.dps = dps
    lo = floor_for(N)
    t0 = time.time()
    Q0 = Q_of_delta(N, MUS, WS, None, None)
    inr = inertia(Q0)
    lmin0 = lambda_min(Q0)
    lmax0 = lambda_max(Q0)
    dc, info = delta_critical(N, MUS, WS, 0, lo_exp=lo, hi_exp=3, refine=32)
    T = lmax0 * mp.mpf(10) ** (-16)
    d16, _ = delta_critical(N, MUS, WS, 0, lo_exp=-25, hi_exp=3, refine=28, thresh=T)
    note = info.get("note", "")
    print("  N=%2d dim=%2d dps=%3d mu1/N=%.3f inertia=%-11s lam_max=%.4e lam_min0=%.6e "
          "log10kappa=%.2f delta_c=%.6e det16=%.4e [%.0fs] %s"
          % (N, 2*N+1, dps, float(MUS[0])/N, str(inr), float(lmax0), float(lmin0),
             float(mp.log10(lmax0/lmin0)), float(dc), float(d16), time.time()-t0, note))
    sys.stdout.flush()
