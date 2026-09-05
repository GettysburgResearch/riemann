"""Band-2 finite gate: exact scan of all (X,n,p), 20 <= X <= 1999, n in (X/20, X/10], p in [n,2n).
(X < 20: band 2 empty.) Also: soundness cross-check of the certified grid bounds at X=2000..8000:
brute sqrt(X)*Sigma must exceed the certified worst 1.3788 everywhere in band 2."""
import numpy as np, sys, math
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r

def full_G(X, r):
    S = np.zeros(X + 1)
    m = np.arange(2, X + 1)
    S[2:] = m * r[2:X + 1]
    far = S.copy()
    hi = X
    while hi >= 2:
        lo = max(2, (2 * hi) // 3 + 1)
        M = np.arange(lo, hi + 1)
        a2 = M // 2; b2 = M - a2; a3 = (M + 2) // 3; b3 = M - a3
        fm = far[lo:hi + 1]
        gg = fm / (2.0 * M)
        idx = np.concatenate((a2, b2, a3, b3))
        wts = np.concatenate((a2 * gg, b2 * gg, a3 * gg, b3 * gg))
        buf = np.bincount(idx, weights=wts, minlength=lo)
        buf[lo:] = 0.0            # children always < lo; guard
        far[:len(buf)] += buf
        hi = lo - 1
    return far  # G[m]; valid as far-mass for any n restricted to m >= 2n

def band2_worst(X, r, G, nlo, nhi):
    """min over n in [nlo,nhi], p in [n, min(2n,X+1)) of sqrt(X)*Sigma."""
    sx = math.sqrt(X)
    worst = np.inf; wn = wp = None
    for n in range(nlo, nhi + 1):
        up = min(2 * n, X + 1)
        p = np.arange(n, up)
        sig = p * r[n:up]
        def add(mpar, w, pres=None):
            msk = (mpar >= 2 * n) & (mpar <= X)
            if pres is not None: msk &= pres
            sig[msk] += G[mpar[msk]] * w[msk]
        add(2 * p, np.full(len(p), 0.5))
        add(2 * p + 1, p / (2.0 * (2 * p + 1)))
        add(2 * p - 1, p / (2.0 * (2 * p - 1)))
        for j in (0, 1, 2):
            add(3 * p - j, p / (2.0 * (3 * p - j)))
        bA = (3 * p + 1) // 2
        add(bA, p / (2.0 * bA))
        bB = 3 * (p // 2) + 1  # = 3p/2+1 for even p
        add(bB, p / (2.0 * bB), pres=(p % 2 == 0))
        v = sig.min() * sx
        if v < worst: worst, wn, wp = v, n, int(p[sig.argmin()])
    return worst, wn, wp

# ---- finite gate X in [20, 1999]
worst = np.inf; where = None; pairs = 0
for X in range(20, 2000):
    nlo, nhi = X // 20 + 1, X // 10
    if nlo > nhi: continue
    mu = mobius_sieve(X); r = critical_r(X, mu); G = full_G(X, r)
    for n in range(nlo, nhi + 1): pairs += min(2 * n, X + 1) - n
    v, wn, wp = band2_worst(X, r, G, nlo, nhi)
    if v < worst: worst, where = v, (X, wn, wp)
print(f"finite gate 20<=X<=1999: {pairs} (X,n,p) triples, min sqrt(X)*Sigma = {worst:.6f} at (X,n,p)={where}"
      f" -> {'PASS (all > 0)' if worst > 0 else 'FAIL'}")

# ---- soundness cross-check of the certified claim at several X >= 2000
for X in [2000, 2001, 2048, 3000, 4999, 8000]:
    mu = mobius_sieve(X); r = critical_r(X, mu); G = full_G(X, r)
    v, wn, wp = band2_worst(X, r, G, X // 20 + 1, X // 10)
    print(f"X={X}: true band-2 worst sqrt(X)*Sigma = {v:.4f} at (n,p)=({wn},{wp})  "
          f">= certified 1.3788: {'OK' if v >= 1.3788 else 'VIOLATION'}")
