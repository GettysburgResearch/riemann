import numpy as np
from sympy import mobius
from spec import build_C

# ---- (a) Dirichlet transform of row 2 along the critical line: peaks at zeta zeros?
T = 2000
C, idx = build_C(T)
n = idx.astype(float)
c2 = C[0]  # row j=2
ts = np.linspace(5, 40, 1401)
vals = np.abs(np.array([np.sum(c2 * n ** (-0.5 - 1j * t)) for t in ts]))
# local maxima
pk = [(ts[i], vals[i]) for i in range(1, len(ts) - 1) if vals[i] > vals[i-1] and vals[i] > vals[i+1]]
pk.sort(key=lambda x: -x[1])
print("top peaks of |sum c_2(n) n^{-1/2-it}| in t in [5,40]:", [(round(a,2), round(b,2)) for a,b in pk[:6]])
print("zeta zeros: 14.13 21.02 25.01 30.42 32.94 37.59")

# sanity on sigma=2: compare to E2(s)/zeta(s)
import mpmath as mp
E2 = lambda s: -2 + 4*2**(-s) - 2*3**(-s)
for s in [2.0, 1.5]:
    lhs = np.sum(c2 * n ** (-s))
    rhs = float(E2(s) / (2 * mp.zeta(s)))
    print(f"s={s}: partial sum={lhs:.6f}  E2(s)/(2 zeta(s))={rhs:.6f}")

# ---- (b) eigenvector condition number of C (cost of best similarity-symmetrizer)
for TT in [50, 100, 200, 400]:
    CC, ii = build_C(TT)
    w, V = np.linalg.eig(CC)
    kV = np.linalg.cond(V)
    print(f"T={TT}: cond(eigvec matrix) = {kV:.3e}, eig real? {np.allclose(w.imag,0)}, eig range [{w.real.min():.4f},{w.real.max():.4f}]")

# ---- (c) growth fits
Ts = np.array([200., 500., 1000., 2000.])
svmax = np.array([23.6734, 37.3709, 52.7919, 74.3483])
svmin = np.array([0.0170507, 0.00667578, 0.00330857, 0.00164586])
import numpy.polynomial as P
amax = np.polyfit(np.log(Ts), np.log(svmax), 1)[0]
amin = np.polyfit(np.log(Ts), np.log(svmin), 1)[0]
print(f"sv_max ~ T^{amax:.3f}, sv_min ~ T^{amin:.3f}, cond ~ T^{amax-amin:.3f}")
