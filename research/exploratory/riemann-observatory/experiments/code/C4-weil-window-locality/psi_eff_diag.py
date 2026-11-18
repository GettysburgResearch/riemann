"""Diagnostic: effective local symbol Psi_eff(T0, L, delta) = W_true(g)/||g||^2 for g = e^{-iT0x} sinh(delta x) on [-L,L],
at the measured thresholds of detect_highT.json; compared with log(T0/2pi).  The flat criterion with Psi0 -> Psi_eff
(2 sigma^2 = Psi_eff) is exactly the single-test-function threshold."""
import os, sys, json, math, hashlib
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from detect_lib import W_true
from exp_detect_ultra import sinh_coeffs
RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality"
d = json.load(open(os.path.join(RES, "detect_highT.json")))
out = []
for r in d["results"]:
    T0 = r["T0"]
    for x in r["rows"]:
        L = x["L_star"]; dl = x["delta"]
        N = 64
        W = W_true(repr(T0), L, N, asym=True)
        c = sinh_coeffs(dl, L, N)
        psi = float(np.real(c.conj() @ W @ c) / np.real(c.conj() @ c))
        s2 = math.sinh(2 * dl * L) / (2 * dl) - L
        rec = {"T0": T0, "delta": dl, "L_star": L, "log_T_over_2pi": math.log(T0 / (2 * math.pi)), "Psi_eff_at_Lstar": psi, "two_sigma2_at_Lstar": 2 * s2}
        out.append(rec); print(json.dumps(rec))
p = os.path.join(RES, "psi_eff_diag.json"); json.dump(out, open(p, "w"), indent=1)
print("wrote", p, hashlib.sha256(open(p, "rb").read()).hexdigest())
