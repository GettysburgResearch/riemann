#!/usr/bin/env python3
"""Summarize sweep_out.npz: global and per-decade minima of the three margins."""
import numpy as np

z = np.load("sweep_out.npz")
x = z["x"]; strict = z["strict"]
print(f"total points: {len(x)} (activation left-limits: {int(strict.sum())})")
for key, ek in (("M2", "eps2"), ("M3", "eps3"), ("Msc", "epssc")):
    v = z[key]; e = z[ek]
    i = int(np.argmin(v))
    print(f"GLOBAL min {key} = {v[i]:.6f} (+- {e[i]:.2e}) at x = {x[i]:.8e}"
          f" {'(activation left-limit)' if strict[i] else ''}")
    print(f"   min of (value - err) = {np.min(v - e):.6f}; points <= 0: {int(np.sum(v - e <= 0))}")
print("\nper-decade minima (decade lower edge, min M2, min M3, min Msc, argmin x of M2):")
lo = 6
while 10.0 ** lo < x.max():
    m = (x >= 10.0 ** lo) & (x < 10.0 ** (lo + 1))
    if m.sum():
        v2 = z["M2"][m]; v3 = z["M3"][m]; vs = z["Msc"][m]
        print(f"  1e{lo:02d}: M2>={v2.min():9.4f}  M3>={v3.min():8.4f}  "
              f"Msc>={vs.min():8.5f}  n={int(m.sum()):6d}  "
              f"argminM2={x[m][np.argmin(v2)]:.4e}")
    lo += 1
# largest downward excursion relative to local trend: fit M2 ~ a log x + b on [1e12,]
lx = np.log(x)
for key in ("M2", "M3"):
    sel = x > 1e12
    A = np.vstack([lx[sel], np.ones(int(sel.sum()))]).T
    coef, *_ = np.linalg.lstsq(A, z[key][sel], rcond=None)
    resid = z[key][sel] - A @ coef
    print(f"{key} trend fit on x>1e12: {coef[0]:.4f} log x + {coef[1]:.3f}; "
      f"residual range [{resid.min():.3f}, {resid.max():.3f}]")
print("\nM_sc stabilization: last 5 grid values:",
      np.round(z["Msc"][~strict][-5:], 6))
