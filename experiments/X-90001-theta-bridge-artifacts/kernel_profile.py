import numpy as np

def b_arr(X):
    m = np.arange(0, X + 2, dtype=np.float64)
    b = np.zeros(X + 2)
    mm = m[2:X + 1]
    b[2:X + 1] = 2.0 * np.sqrt(mm) * (np.log(X / mm) - 2.0 * (1.0 - np.sqrt(mm / X)))
    return b

print("=== 1. kernel envelope  |dv(d)| * d^{3/2} / (log(X/d)+2)  ===")
for X in (100000, 800000):
    b = b_arr(X)
    Db = b[:-1] - b[1:]
    v = np.zeros(X + 1)
    for d in range(2, X + 1):
        v[d] = Db[d::d].sum()
    d = np.arange(2, X)
    dv = v[3:X + 1] - v[2:X]
    env = np.abs(dv) * d ** 1.5 / (np.log(X / d) + 2.0)
    r = int(np.sqrt(X))
    bands = [(2, 50), (50, r // 2), (r // 2, 4 * r), (4 * r, X // 2), (X // 2, X - 1)]
    out = "  ".join(f"[{lo},{hi}):{env[lo-2:hi-2].max():.3f}" for lo, hi in bands)
    print(f"X={X}: {out}")
    K = (np.abs(dv) * np.sqrt(d) * np.log(d + 2.0) ** 2).sum()
    print(f"   K_total={K:.1f}   K/log^4(X)={K / np.log(X) ** 4:.4f}")

print()
print("=== 2. scaling profile:  sqrt(X)*v(xX) -> V(x),  h(u)=u^{-1/2}log(1/u)-V(u) ===")
def Vprof(x):
    K = int(np.floor(1.0 / x))
    k = np.arange(1, K + 1, dtype=np.float64)
    s = k * x
    return float(((s ** -0.5) * (4.0 - np.log(1.0 / s)) - 4.0).sum())

# integral of h on (0,1) settles the T_X(2) ~ -c*sqrt(X)? question
us = np.linspace(5e-7, 1.0, 400001)[:-1] + 1.25e-6 / 2
V = np.array([Vprof(u) for u in us[::40]])   # 10000 points
uu = us[::40]
h = uu ** -0.5 * np.log(1.0 / uu) - V
I_h = np.trapz(h, uu)
print(f"  int_0^1 h(u) du  ~ {I_h:.4f}   (trapz on 10^4 pts, u>=~1e-6)")
print(f"  h at u=0.9,0.7,0.5,0.3,0.1,0.03,0.01,0.003: ",
      [f"{h[np.searchsorted(uu, q)]:.3f}" for q in (0.9, 0.7, 0.5, 0.3, 0.1, 0.03, 0.01, 0.003)])

# 3. moat profile prediction  M_s(x) = -[ int_x^1 h - 2^{-1/2} int_{2x}^1 h ]  vs measured T^s/sqrt(X)
from numpy import trapz
def Ih(a):
    i = np.searchsorted(uu, a)
    return trapz(h[i:], uu[i:])
print()
print("=== 3. moat prediction vs measured T^s/sqrt(X) (X=200000 run) ===")
meas = {0.0001: -0.00843, 0.0011: -0.02074, 0.01: -0.05574, 0.05: -0.10117,
        0.1001: -0.11870, 0.2: -0.11937, 0.3001: -0.10147, 0.4001: -0.06992,
        0.499: -0.03965, 0.52: -0.03373, 0.6001: -0.01731, 0.7: -0.00631,
        0.8: -0.00164, 0.9: -0.00018}
print("   x       pred M_s(x)   measured")
for x, m in meas.items():
    pred = -(Ih(x) - (Ih(min(2 * x, 1.0)) / np.sqrt(2) if x <= 0.5 else 0.0))
    print(f" {x:7.4f}   {pred:+.5f}     {m:+.5f}")
