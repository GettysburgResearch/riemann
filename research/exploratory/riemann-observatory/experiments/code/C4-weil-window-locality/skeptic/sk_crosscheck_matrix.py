"""SKEPTIC (C4): entrywise comparison of my zeros-side matrix (sk_detect.P_matrix) with the
investigator's arithmetic-side matrix (weil_core.WeilWindow.matrix) at a few (T0, L, N)."""
import os, sys, json
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from sk_detect import P_matrix, h_imag, h_mp
from weil_core import WeilWindow
out = []
for (T0, L, N) in [(100.07452261196254, 1.5, 48), (1000.5705270975978, 2.5, 64), (9999.457871252105, 3.0, 64)]:
    Pz = P_matrix(T0, L, N)
    Wa = WeilWindow(L, N).matrix(T0)
    d = np.max(np.abs(Pz - Wa))
    ez = np.linalg.eigvalsh(0.5*(Pz+Pz.conj().T))[:3]; ea = np.linalg.eigvalsh(Wa)[:3]
    out.append({"T0": T0, "L": L, "N": N, "max_entry_diff": float(d), "eig_zeros": ez.tolist(), "eig_arith": ea.tolist()})
    print(out[-1], flush=True)
# complex evaluations: quadrature vs mpmath Bessel
a = h_imag(0.3, 2.0, 10); b = h_mp(complex(0, 0.3), 2.0, 10)
print("h(-0.3i) quad vs mpmath max diff", float(np.max(np.abs(a - b))))
json.dump(out, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic/sk_crosscheck_matrix.json", "w"), indent=1)
