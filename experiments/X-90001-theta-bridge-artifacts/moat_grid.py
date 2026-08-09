import numpy as np

NMAX = 4_000_000
inv = 1.0/np.sqrt(np.arange(1, NMAX+1))
S = np.cumsum(inv)                       # S[n-1] = S_n
A = np.cumsum(inv*np.log(np.arange(1, NMAX+1)))

def Hval(t):
    t = np.asarray(t, dtype=float)
    n = np.floor(1.0/t).astype(np.int64)
    n = np.minimum(n, NMAX)
    Sn = S[n-1]; An = A[n-1]
    return -2*np.sqrt(t)*(An + (Sn+1)*np.log(t) + 2*Sn - 2) + 4*n*t - 4

def Hc(t, c):
    out = Hval(t).copy()
    m = t <= c
    out[m] -= np.sqrt(c)*Hval(t[m]/c)
    return out

# global check H<=0 and J monotone
tg = np.geomspace(1e-6, 1.0, 4_000_000)
Hg = Hval(tg)
print("max H on grid:", Hg.max(), "at t=", tg[Hg.argmax()])
Jg = Hg/np.sqrt(tg)
dJ = np.diff(Jg)
print("min diff(J) on grid (should be >= -tiny):", dJ.min())

for c in [1/3, 0.4, 0.5]:
    t = np.geomspace(1e-6, 1.0, 4_000_000)
    v = Hc(t, c)
    i = v.argmax(); j = v.argmin()
    print("c=%.6f  max Hc=%.3e at t=%.6f   min Hc=%.6f at t=%.6f" % (c, v[i], t[i], v[j], t[j]))

# refine min near reported theta~0.141 for each c
from scipy.optimize import minimize_scalar
for c in [1/3, 0.4, 0.5]:
    # find min over each cell near the argmin by fine local grid
    t = np.linspace(0.05, 0.35, 2_000_001)
    v = Hc(t, c)
    j = v.argmin()
    print("refine c=%.6f: min Hc=%.8f at t=%.8f  (cell N=%d, N'=%d)"
          % (c, v[j], t[j], int(1/t[j]), int(c/t[j])))
