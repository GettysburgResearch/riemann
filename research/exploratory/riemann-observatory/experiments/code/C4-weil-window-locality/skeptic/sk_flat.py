"""SKEPTIC (C4-LAT): flat model P = Psi0 * I with one pair {T0 +- i delta}; exact criterion
sinh(2 dL)/(2d) - L > Psi0/2 checked against (a) direct Galerkin min eigenvalue (my h_imag quadrature),
(b) closed-form 2x2 eigenvalue Psi0/(sinh(2dL)/d - 2L) - 1, and kappa_c root of sinh k = 2k."""
import sys, os, math, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np, mpmath as mp
from numpy.polynomial.legendre import leggauss, legval
def h_imag(b, L, N, q=300):
    t, w = leggauss(q); x = L * t
    return np.array([np.sum(w * L * math.sqrt((2*j+1)/(2*L)) * legval(t, np.eye(j+1)[j]) * np.exp(-b*x)) for j in range(N)], complex)
out = []
Psi0 = math.log(1e6 / (2 * math.pi)); N = 48
for d in (0.1, 0.3, 0.49):
    Lf = float(mp.findroot(lambda L: mp.sinh(2*d*L)/(2*d) - L - Psi0/2, 3.0))
    for fac in (0.98, 1.02):
        L = Lf * fac
        hp, hm = h_imag(d, L, N), h_imag(-d, L, N)
        W = Psi0 * np.eye(N) + np.outer(hp, hm.conj()) + np.outer(hm, hp.conj())
        lm = float(np.linalg.eigvalsh(0.5*(W+W.conj().T))[0])
        closed = Psi0 * (Psi0/(math.sinh(2*d*L)/d - 2*L) - 1) / Psi0
        out.append({"delta": d, "L/L_flat": fac, "galerkin_lam_min": lm, "closed_form_eig(G^-1+M)": Psi0/(math.sinh(2*d*L)/d - 2*L) - 1})
        print(out[-1])
kc = float(mp.findroot(lambda k: mp.sinh(k) - 2*k, 2.2)); print("kappa_c", kc)
json.dump({"rows": out, "kappa_c": kc}, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic/sk_flat.json", "w"), indent=1)
