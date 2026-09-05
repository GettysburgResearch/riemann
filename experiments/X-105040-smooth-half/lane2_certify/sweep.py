#!/usr/bin/env python3
"""Lane 2 dense sweep: measure M_2, M_3, M_sc over [1e6, 5*P61].
Part A: [1e6,1e9]: 10k log-uniform + ALL lattice activation left-limits (strict).
Part B: (1e9,1e12]: 5k log-uniform + all ODD activation left-limits.
Part C: (1e12, 5*P61]: 10k log-uniform.
Saves sweep_out.npz incrementally; prints running minima.
"""
import numpy as np
from math import log
import time
import common as C

XLO, XMID1, XMID2 = 1e6, 1e9, 1e12
XHI = float(5 * C.P61)

jobs = []  # (x, strict)
# Part A
for x in np.geomspace(XLO, XMID1, 10001):
    jobs.append((float(x), False))
d = C.LAT["d"]
selA = (d > XLO) & (d <= XMID1)
for x in d[selA]:
    jobs.append((float(x), True))
# Part B
for x in np.geomspace(XMID1, XMID2, 5001)[1:]:
    jobs.append((float(x), False))
selB = (d > XMID1) & (d <= XMID2) & C.LAT["is_odd"]
for x in d[selB]:
    jobs.append((float(x), True))
# Part C
for x in np.geomspace(XMID2, XHI, 10001)[1:]:
    jobs.append((float(x), False))

jobs.sort(key=lambda t: t[0])
print(f"total evaluations: {len(jobs)}  (A grid 10001, A act {int(np.sum(selA))}, "
      f"B grid 5000, B act {int(np.sum(selB))}, C grid 10000)", flush=True)

n = len(jobs)
xs = np.zeros(n); m2 = np.zeros(n); m3 = np.zeros(n); msc = np.zeros(n)
e2 = np.zeros(n); e3 = np.zeros(n); esc = np.zeros(n)
est = np.zeros(n); strict_f = np.zeros(n, dtype=bool)

t0 = time.time()
mins = {"M2": (1e18, 0), "M3": (1e18, 0), "M_sc": (1e18, 0)}
for i, (x, st) in enumerate(jobs):
    r = C.eval_point(x, strict=st)
    xs[i] = x; strict_f[i] = st
    m2[i] = r["M2"]; m3[i] = r["M3"]; msc[i] = r["M_sc"]
    e2[i] = r["eps2"]; e3[i] = r["eps3"]; esc[i] = r["eps_sc"]
    est[i] = r["e_star"]
    for key, v in (("M2", r["M2"]), ("M3", r["M3"]), ("M_sc", r["M_sc"])):
        if v < mins[key][0]:
            mins[key] = (v, x)
    if (i + 1) % 5000 == 0 or i == n - 1:
        el = time.time() - t0
        print(f"[{i+1}/{n}] x={x:.3e} elapsed={el:.0f}s  "
              + "  ".join(f"min {k}={v[0]:.4f}@{v[1]:.4e}" for k, v in mins.items()),
              flush=True)
        np.savez_compressed("sweep_out.npz", x=xs[:i+1], M2=m2[:i+1], M3=m3[:i+1],
                            Msc=msc[:i+1], eps2=e2[:i+1], eps3=e3[:i+1],
                            epssc=esc[:i+1], estar=est[:i+1], strict=strict_f[:i+1])

print("== FINAL SWEEP MINIMA ==")
for k, (v, xx) in mins.items():
    print(f"  {k}: min = {v:.6f} at x = {xx:.6e}")
neg = int(np.sum(m2 - e2 <= 0) + np.sum(m3 - e3 <= 0) + np.sum(msc - esc <= 0))
print(f"points with margin-minus-error <= 0: {neg}")
