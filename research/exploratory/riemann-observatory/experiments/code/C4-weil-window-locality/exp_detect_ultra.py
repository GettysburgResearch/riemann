"""Experiment D-ultra: growth-regime detection thresholds at very large heights (1e12 ... 1e50).

T0 is a fixed decimal height (the neighbouring zeros are NOT located; the additive model only needs
T0).  The window form is the arithmetic side with the asymptotic archimedean symbol
psi(1/4 + i T0/2) - log pi (error O(log T0 / T0)) and exact prime phases T0 log n mod 2pi computed in
60-digit arithmetic.  The test-function detection uses the N-term Legendre basis modulated at T0.
Also reports L_sinh: the threshold obtained with the single test function e^{-iT0 x} sinh(delta x)
(the function used in Theorem C4-B), evaluated on the true window form.
Usage: OPENBLAS_NUM_THREADS=1 python3 exp_detect_ultra.py
"""
import os, sys, json, time, math, hashlib
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from detect_lib import W_true, lam_min, L_nyquist, L_flat
from weil_core import quad_matrix, phi_table, leggauss

RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality"
HEIGHTS = ["1e12", "1e15", "1e20", "1e30", "1e50"]
DELTAS = [0.3, 0.4, 0.45, 0.49]
TAU = 1e-8


def N_rule(L):
    return 48 if L <= 3.0 else 64


def sinh_coeffs(delta, L, N):
    t, w = leggauss(N + 40)
    x = L * t
    P = phi_table(x, L, N)
    return (P * (L * w) * np.sinh(delta * x)[None, :]).sum(axis=1)


def lam_and_sinh(Ts, d, L):
    N = N_rule(L)
    T0 = float(Ts)
    W = W_true(Ts, L, N, asym=True)
    Wm = W + quad_matrix(T0, d, T0, L, N, sides=(1,))  # -T0 pair: |terms| <= Ac^2/(2 T0^2), negligible
    Wm = 0.5 * (Wm + Wm.conj().T)
    c = sinh_coeffs(d, L, N)
    rq = float(np.real(c.conj() @ Wm @ c) / np.real(c.conj() @ c))
    return lam_min(Wm), rq


def thr(Ts, d, Lgrid, which):
    prev = None
    for L in Lgrid:
        v = lam_and_sinh(Ts, d, L)[which]
        if v < -TAU:
            if prev is None:
                return L
            lo, hi = prev, L
            for _ in range(6):
                m = 0.5 * (lo + hi)
                if lam_and_sinh(Ts, d, m)[which] < -TAU:
                    hi = m
                else:
                    lo = m
            return 0.5 * (lo + hi)
        prev = L
    return None


def main():
    out = []
    t0 = time.time()
    for Ts in HEIGHTS:
        T0 = float(Ts)
        for d in DELTAS:
            Lf = L_flat(T0, d)
            grid = list(np.round(np.arange(max(1.0, Lf - 1.5), Lf + 1.5, 0.1), 6))
            Ls = thr(Ts, d, grid, 0)
            Lsh = thr(Ts, d, grid, 1)
            rec = {"T0": Ts, "delta": d, "L_N": L_nyquist(T0), "L_flat": Lf, "L_star": Ls, "L_sinh": Lsh,
                   "kappa": d * math.log(T0 / (2 * math.pi))}
            out.append(rec)
            print(json.dumps(rec), flush=True)
    path = os.path.join(RES, "detect_ultra.json")
    with open(path, "w") as f:
        json.dump({"meta": {"runtime_s": round(time.time() - t0, 1), "tau": TAU,
                            "note": "asymptotic archimedean symbol; neighbours not located"}, "rows": out}, f, indent=1)
    print("wrote", path, hashlib.sha256(open(path, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
