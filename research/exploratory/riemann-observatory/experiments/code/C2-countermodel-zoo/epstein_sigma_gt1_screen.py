#!/usr/bin/env python3
"""C2 zoo: NON-RIGOROUS numpy screen of |1+R(s)| (truncated Euler product, see epstein_sigma_gt1.py) on sigma=1.01,1.03, t<=1e7.
Output: best (|1+R|, t) per 1e5-block, sorted. Run: python3 epstein_sigma_gt1_screen.py > log (about 6 min, 1 core)."""
import numpy as np, time
from sympy import primerange
ps=[p for p in primerange(3,400) if p%20 in (3,7)]
t0=time.time()
for sg in [1.01, 1.03]:
    best=[]
    for T0 in np.arange(0, 1e7, 1e5):
        t=np.arange(T0, T0+1e5, 0.05)
        s=sg+1j*t
        x=np.exp(-s*np.log(2)); R=(1-x)/(1+x)
        for p in ps:
            x=np.exp(-s*np.log(p)); R*=((1-x)/(1+x))**2
        v=np.abs(1+R)
        i=np.argmin(v); best.append((float(v[i]),float(t[i])))
    best.sort(); print(sg, best[:8], time.time()-t0, flush=True)
