"""Finite gate: for every X in [4, 1999], every n with X/10 < n < ceil(X/5),
check min_p Sigma_{X,n}(p) > 0 (float64; theoretical margins ~2.7/sqrt(X) >> 1e-9)."""
import numpy as np, sys, math
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r, sigma_first_entrance

gmin = 1e18; arg = None; count = 0
for X in range(4, 2000):
    r = critical_r(X)
    nlo = X//10 + 1
    nhi = -(-X//5) - 1
    for n in range(max(2, nlo), nhi+1):
        ps, sig = sigma_first_entrance(r, X, n)
        m = sig.min(); count += 1
        if m*math.sqrt(X) < gmin: gmin = m*math.sqrt(X); arg = (X, n, ps[sig.argmin()], m)
        if m <= 0:
            print("VIOLATION", X, n, ps[sig.argmin()], m)
print(f"checked {count} (X,n) pairs; min sqrt(X)*Sigma over all open-band cells = {gmin:.6f} at {arg}")
print("PASS" if gmin > 1e-6 else "MARGIN_TOO_SMALL")
