"""PART 9b: N-sweep at FIXED, SUFFICIENT pole count M=60.

PART 9's first attempt used M=20, i.e. 2M=40 rank-one terms, and was therefore
rank-deficient (hence meaningless) as soon as dim=2N+1 exceeded 40, i.e. for
N>=20: measured inertia (40,0,1), (40,0,5), (40,0,9) at N=20,22,24.
A necessary condition is M > N.  Here M=60 (120 rank-one terms) comfortably
covers dim<=49, and the whole sweep is at one M so the N-scaling is clean.

Usage: python3 bigN2.py <N1> <N2> ...
"""
import sys, time
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *

M = 60
gam = zeta_ordinates(M, dps=40)
MUS = [g * mp.mpf("1.5") for g in gam]
WS = [mp.mpf(1)] * M
NS = [int(x) for x in sys.argv[1:]] or [8, 10, 12, 14]

for N in NS:
    dps = 40 + 6 * N
    mp.mp.dps = dps
    pred = 1.6634 - 0.5316 * N - 0.05618 * N * N
    lo = int(pred) - 30
    t0 = time.time()
    Q0 = Q_of_delta(N, MUS, WS, None, None)
    inr = inertia(Q0)
    lmin0 = lambda_min(Q0)
    lmax0 = lambda_max(Q0)
    dc, info = delta_critical(N, MUS, WS, 0, lo_exp=lo, hi_exp=3, refine=32)
    T = lmax0 * mp.mpf(10) ** (-16)
    d16, _ = delta_critical(N, MUS, WS, 0, lo_exp=-25, hi_exp=3, refine=28, thresh=T)
    ok = "OK" if inr == (2 * N + 1, 0, 0) else "RANK-DEFICIENT"
    print("  N=%2d dim=%2d dps=%3d mu1/N=%.3f inertia=%-11s %s lam_max=%.4e "
          "lam_min0=%.6e log10kappa=%.2f delta_c=%.6e det16=%.4e ratio=%.3e [%.0fs] %s"
          % (N, 2*N+1, dps, float(MUS[0])/N, str(inr), ok, float(lmax0), float(lmin0),
             float(mp.log10(lmax0/lmin0)), float(dc), float(d16), float(d16/dc),
             time.time()-t0, info.get("note", "")))
    sys.stdout.flush()
