# A2 gevrey_num.py -- (a) Gevrey-2 bump Fourier decay exp(-c sqrt xi): measure c.
# (b) crossover T_x where c sqrt T = C log T loglog T, and the Gevrey-weighted
#     Ingham tail  I(H) = int_H^inf T^{3/5} log^6 T * exp(-c sqrt T + C log T loglog T) dT
#     (log^5 from Ingham, one more log from the RvM partner count), numerically.
import json, math
from mpmath import mp, mpf, quad, exp, log, sqrt, cos, sin, findroot
mp.dps = 30

# (a) bump g(u) = exp(-1/u - 1/(d-u)) on (0,d), d = 0.25 (corner width delta).
d = mpf("0.25")
def g(u): return exp(-1/u - 1/(d - u)) if 0 < u < d else mp.mpf(0)
def ghat_abs(xi):
    re = quad(lambda u: g(u) * cos(xi * u), [0, d/2, d])
    im = quad(lambda u: g(u) * sin(xi * u), [0, d/2, d])
    return sqrt(re**2 + im**2)
xis = [100, 200, 400, 800, 1600, 3200]
vals = [(xi, float(ghat_abs(xi))) for xi in xis]
# fit log|ghat| = A - c*sqrt(xi) on the last pairs
import numpy as np
X = np.array([math.sqrt(x) for x, v in vals if v > 0])
Y = np.array([math.log(v) for x, v in vals if v > 0])
A_ = np.polyfit(X, Y, 1)
c_fit = -A_[0]
# theory for exp(-1/u - 1/(d-u)): saddle gives |ghat| ~ exp(-2 sqrt(xi)) as xi->inf
# (the -1/u factor alone gives exp(-2 sqrt xi)); with scaling u -> u the constant
# c_theory = 2 for the u^-1 singularity (independent of d to leading order).

# (b) crossover: solve c*sqrt(T) = C*log(T)*log(log(T))
def crossover(c, C):
    f = lambda T: c * sqrt(T) - C * log(T) * log(log(T))
    T0 = mpf(100)
    try:
        return float(findroot(f, mpf(5000)))
    except Exception:
        # scan
        T = mpf(60)
        while f(T) < 0 and T < mpf("1e12"):
            T *= 2
        return float(T)

def tail(H, c, C):
    # I(H) = int_H^inf T^{3/5} log^6 T exp(-c sqrt T + C log T loglog T) dT
    f = lambda T: T**mpf("0.6") * log(T)**6 * exp(-c*sqrt(T) + C*log(T)*log(log(T)))
    Tx = crossover(c, C)
    hi = max(4*Tx, float(H)*4) + 1e6
    return float(quad(f, [H, max(2*float(H), Tx), hi, mpf(1e9)]))

grid = []
for c in [0.5, 1.0, 2.0]:
    for C in [2.0, 5.0, 10.0]:
        Tx = crossover(c, C)
        I60 = tail(60, c, C)
        ITx = tail(Tx, c, C)
        grid.append(dict(c=c, C=C, T_cross=Tx, I_from_60=I60, I_from_Tcross=ITx))

cP2 = 2/(3*math.pi) * 0.04782893516094**2   # |c_P|^2
out = dict(delta=float(d), ghat_samples=vals, c_fit=float(c_fit),
           c_theory_note="exp(-1/u) endpoint gives |ghat| ~ exp(-2 sqrt xi): c ~ 2",
           cP_sq=cP2, grid=grid)
with open(__file__.replace("gevrey_num.py", "gevrey_num_out.json"), "w") as f:
    json.dump(out, f, indent=1)
print("Gevrey-2 bump, delta =", float(d))
for xi, v in vals: print(f"  xi={xi:5d}  |ghat|={v:.3e}  log/-sqrt(xi)={math.log(v)/-math.sqrt(xi):.4f}")
print(f"fitted c in exp(-c sqrt xi): {c_fit:.4f}   (theory ~ 2 for the 1/u endpoint)")
print(f"|c_P|^2 = {cP2:.4e}")
print(" c    C     T_cross        I(60)             I(T_cross)")
for gr in grid:
    print(f" {gr['c']:.1f}  {gr['C']:4.1f}  {gr['T_cross']:.4g}   {gr['I_from_60']:.4g}   {gr['I_from_Tcross']:.4g}")
