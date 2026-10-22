"""Second round: verify the fixed lambda_min, and time the real thing."""
import time, sys
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *

print("=== lambda_min: log-bisection vs eigsy on a well-conditioned case ===")
mp.mp.dps = 60
mus = [mp.mpf(x) for x in ["1.5", "3.25", "7.1", "12.9", "21.2"]]
ws = [mp.mpf(1)] * 5
Q = Q_of_delta(4, mus, ws, None, None)
lm = lambda_min(Q)
E = mp.eigsy(mp.matrix(Q), eigvals_only=True)
print("  positive case: bisect %.10e   eigsy %.10e" % (float(lm), float(min(E))))
Qp = Q_of_delta(4, mus, ws, 0, mp.mpf("0.05"))
lmp = lambda_min(Qp)
Ep = mp.eigsy(mp.matrix(Qp), eigvals_only=True)
print("  negative case: bisect %.10e   eigsy %.10e" % (float(lmp), float(min(Ep))))

print()
print("=== lambda_min of the zeta-profile Q vs N, with dps doubling check ===")
gam = zeta_ordinates(20)
Delta = mp.mpf("1.5")
MUS = [g * Delta for g in gam]
WS = [mp.mpf(1)] * len(MUS)
for N in (4, 6, 8, 10):
    for dps in (40 + 5 * N, 2 * (40 + 5 * N)):
        mp.mp.dps = dps
        t0 = time.time()
        Q = Q_of_delta(N, MUS, WS, None, None)
        inr = inertia(Q)
        lm = lambda_min(Q)
        print("  N=%2d dim=%2d dps=%3d  inertia=%s  maxabs=%.3e  lambda_min=%.6e  (%.1fs)"
              % (N, 2 * N + 1, dps, inr, float(maxabs(Q)), float(lm), time.time() - t0))

print()
print("=== pilot: one full delta_c bisection (zeta profile, star = lowest pole) ===")
for N in (4, 6, 8):
    mp.mp.dps = 40 + 5 * N
    t0 = time.time()
    dc, info = delta_critical(N, MUS, WS, 0, lo_exp=-60, hi_exp=2, refine=30)
    print("  N=%2d  delta_c=%.6e  calls=%d  time=%.1fs" % (N, float(dc), info["calls"], time.time() - t0))
