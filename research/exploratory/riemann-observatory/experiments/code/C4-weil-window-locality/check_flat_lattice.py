"""Check of the flat-model and lattice-model theorems (C4-F, C4-LAT) in the modulated basis.
Flat: P = Psi0 * I.  Lattice: P = sum over lambda in T0 + s(Z + 1/2) of e(lambda) e(lambda)^*  (|n| <= nmax, + tail).
Prints min eigenvalue of P + quadruple(+T0 pair only) around the predicted thresholds."""
import os, sys, json, math, hashlib
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from weil_core import e_vals, quad_matrix
from detect_lib import L_flat
RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality"
out = []
T0, N = 1.0e6, 48
Psi0 = math.log(T0 / (2 * math.pi))
for d in [0.1, 0.3, 0.49]:
    Lf = L_flat(T0, d)
    for L in [Lf * 0.98, Lf * 1.02]:
        W = Psi0 * np.eye(N) + quad_matrix(T0, d, T0, L, N, sides=(1,))
        lm = float(np.linalg.eigvalsh(0.5 * (W + W.conj().T))[0])
        out.append({"model": "flat", "delta": d, "L": L, "L_flat": Lf, "lam_min": lm})
# lattice with spacing s = 2pi/Psi0 (density Psi0/2pi), Nyquist window pi/s = Psi0/2
s = 2 * math.pi / Psi0
nmax = 20000
lam = T0 + s * (np.arange(-nmax, nmax) + 0.5)
for d in [0.01, 0.1, 0.49]:
    for L in [0.9 * Psi0 / 2, 0.99 * Psi0 / 2, 1.01 * Psi0 / 2, 1.1 * Psi0 / 2]:
        if L > 7:
            continue
        Nl = 64
        E = e_vals(lam, T0, L, Nl)
        P = E @ E.conj().T
        # tail beyond |n| > nmax: average |e_j|^2 ~ (phi_j(L)^2 + phi_j(-L)^2)/w^2 -> add (2/(s * R)) * B, R = s*nmax
        from weil_core import phi_table
        ph = phi_table(np.array([L, -L]), L, Nl)
        B = np.outer(ph[:, 0], ph[:, 0]) + np.outer(ph[:, 1], ph[:, 1])
        P = P + B * 2 / (s * s * nmax)
        lam0 = float(np.linalg.eigvalsh(P)[0])
        W = P + quad_matrix(T0, d, T0, L, Nl, sides=(1,))
        lm = float(np.linalg.eigvalsh(0.5 * (W + W.conj().T))[0])
        out.append({"model": "lattice", "delta": d, "L": L, "L_N": Psi0 / 2, "lam0": lam0, "lam_min": lm,
                    "flat_prediction_detect": bool(math.sinh(2 * d * L) / (2 * d) - L > Psi0 / 2)})
for r in out:
    print(json.dumps(r))
p = os.path.join(RES, "check_flat_lattice.json")
json.dump(out, open(p, "w"), indent=1)
print("wrote", p, hashlib.sha256(open(p, "rb").read()).hexdigest())
