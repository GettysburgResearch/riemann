import numpy as np
from wsts_core import primes_upto, bvals_X

PRALL = primes_upto(2*10**5)

def rvec(X, P=None):
    if P is None: P = PRALL[PRALL <= X]
    b = bvals_X(X)
    out = np.empty(len(P))
    for i in range(len(P)):
        p = P[i]
        idx = np.arange(p, X+1, p)
        out[i] = (b[idx] - b[idx+1]).sum()
    Pf = P.astype(np.float64)
    return P, out - np.log(X/Pf)/np.sqrt(Pf)

cacheY = {}
def margin(X):
    P, rX = rvec(X)
    Y = X//2
    if Y in cacheY: PY, rY = cacheY[Y]
    else:
        PY, rY = rvec(Y); cacheY[Y] = (PY, rY)
    s = rX.copy(); s[:len(PY)] -= rY
    w = np.log(P.astype(np.float64))*s
    M = np.cumsum(w[::-1])[::-1]
    gm = M.max()
    # non-trivial margin: z <= 0.9 X
    cut = np.searchsorted(P, 0.9*X)
    ntm = M[:cut].max() if cut > 0 else np.nan
    return gm, ntm

# scan all X in [4, 12000], then random sample up to 2e5
worstg = -np.inf; worstn = -np.inf; argg = None; argn = None
viol = []
import time
t0 = time.time()
for X in range(4, 12001):
    cacheY.clear() if len(cacheY) > 3000 else None
    gm, ntm = margin(X)
    if gm > 0: viol.append((X, gm))
    if gm > worstg: worstg, argg = gm, X
    if not np.isnan(ntm) and ntm > worstn: worstn, argn = ntm, X
print(f'scan X in [4,12000]: {time.time()-t0:.0f}s  violations(B>0): {len(viol)}')
print(f'  global max margin  = {worstg:.3e} at X={argg}')
print(f'  nontrivial (z<=0.9X) max margin = {worstn:.6f} at X={argn}')
rng = np.random.default_rng(7)
sample = rng.integers(12001, 200001, 300)
worstg2 = -np.inf; arg2=None; v2=[]
for X in sample:
    cacheY.clear()
    gm, ntm = margin(int(X))
    if gm > 0: v2.append((int(X), gm))
    if gm > worstg2: worstg2, arg2 = gm, int(X)
print(f'random sample 300 in [12k,200k]: violations: {len(v2)}, max margin {worstg2:.3e} at X={arg2}')
