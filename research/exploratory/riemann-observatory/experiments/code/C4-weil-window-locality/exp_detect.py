"""Experiment D: detection threshold L*(T, delta) of an injected off-line quadruple.

For each target height, T0 = midpoint between two consecutive Arb-certified ordinates (first 100000
zeros, or zeros located with mpmath for T0 > 74920); the quadruple {+-T0 +- i delta} is added to the
zero side (additive model; 'collision' variant also removes the two neighbouring zeros).  The window
form W_true is evaluated exactly on the arithmetic side (exact archimedean moments for T0 <= 1e5,
asymptotic archimedean symbol psi(1/4+iT0/2)-log pi otherwise).  L is scanned upward on a grid and
the first sign change of the minimal eigenvalue (< -tau) is refined by bisection.

Also records lam0(L) = min eigenvalue of the unperturbed window form in the basis modulated at T0
(the 'local floor'), whose collapse marks the Nyquist transition T0 ~ 2 pi e^{2L}.

Usage: OPENBLAS_NUM_THREADS=1 python3 exp_detect.py TAG T1,T2,... [model] [Nscale]
"""
import os, sys, json, time, math, hashlib, platform
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C1-detection-horizons")
import numpy as np
from detect_lib import W_true, lam_min, lam_mod, L_nyquist, L_flat, kappa_cross

RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality"
DELTAS = [float(x) for x in os.environ.get("C4_DELTAS", "0.01,0.03,0.1,0.2,0.3,0.4,0.45,0.49").split(",")]
LCAP = float(os.environ.get("C4_LCAP", "99"))
TAU = 1e-8


def N_rule(L, scale=1.0):
    base = 48 if L <= 2.0 else (64 if L <= 3.5 else 96)
    return int(round(base * scale / 8.0) * 8)


def neighbors_for(Ttarget):
    from common import load_zeros
    g, _ = load_zeros()
    if Ttarget < g[-1] - 5:
        k = int(np.searchsorted(g, Ttarget))
        return float(g[k - 1]), float(g[k]), "arb-certified table (first 100000 zeros)"
    import mpmath as mp
    mp.mp.dps = 30
    t = mp.mpf(Ttarget)
    step = mp.mpf(2 * math.pi / math.log(Ttarget / (2 * math.pi))) / 8
    z0 = mp.siegelz(t)
    a = t
    while True:
        b = a + step
        zb = mp.siegelz(b)
        if mp.sign(zb) != mp.sign(z0):
            r1 = mp.findroot(mp.siegelz, (a, b), solver="anderson")
            break
        a, z0 = b, zb
    a = r1 + step / 4
    z0 = mp.siegelz(a)
    while True:
        b = a + step
        zb = mp.siegelz(b)
        if mp.sign(zb) != mp.sign(z0):
            r2 = mp.findroot(mp.siegelz, (a, b), solver="anderson")
            break
        a, z0 = b, zb
    return float(r1), float(r2), "mpmath siegelz sign changes (non-rigorous; consecutive sign changes on a fine grid)"


def run_T(Ttarget, model="add", Nscale=1.0, step=0.1, nbis=5):
    g1, g2, src = neighbors_for(Ttarget)
    T0 = 0.5 * (g1 + g2)
    asym = T0 > 1e5
    LN = L_nyquist(T0)
    preds = {d: min(LN, L_flat(T0, d)) for d in DELTAS}
    Llo = max(0.3, min(preds.values()) - 0.6)
    Lhi = min(LN + 1.5, LCAP)
    grid = list(np.round(np.arange(Llo, Lhi + 1e-9, step), 6))
    floor, pending, found = [], set(DELTAS), {}
    t0 = time.time()
    prev = None
    lam_hist = {d: [] for d in DELTAS}
    for L in grid:
        N = N_rule(L, Nscale)
        W = W_true(T0, L, N, asym=asym)
        l0 = lam_min(W)
        floor.append([float(L), N, l0])
        for d in sorted(pending):
            lm = lam_mod(T0, d, L, N, model, (g1, g2), asym, W=W)
            lam_hist[d].append([float(L), lm])
            if lm < -TAU:
                found[d] = (prev, float(L))
                pending.discard(d)
        prev = float(L)
        if not pending:
            break
    rows = []
    for d in DELTAS:
        rec = {"delta": d, "L_nyquist": LN, "L_flat": L_flat(T0, d), "kappa": d * math.log(T0 / (2 * math.pi))}
        if d in found:
            lo, hi = found[d]
            if lo is None:
                rec.update({"L_star": hi, "bracket": [None, hi], "note": "detected at first grid point"})
            else:
                for _ in range(nbis):
                    mid = 0.5 * (lo + hi)
                    N = N_rule(mid, Nscale)
                    if lam_mod(T0, d, mid, N, model, (g1, g2), asym) < -TAU:
                        hi = mid
                    else:
                        lo = mid
                rec.update({"L_star": 0.5 * (lo + hi), "bracket": [lo, hi]})
        else:
            rec.update({"L_star": None, "bracket": [grid[-1], None], "note": "not detected up to L_hi"})
        rec["lam_grid"] = lam_hist[d]
        rows.append(rec)
    return {"T_target": Ttarget, "T0": T0, "neighbors": [g1, g2], "neighbor_source": src, "asym_arch": asym,
            "model": model, "Nscale": Nscale, "tau": TAU, "grid_step": step, "nbis": nbis,
            "floor": floor, "rows": rows, "seconds": round(time.time() - t0, 1)}


def main():
    tag = sys.argv[1]
    Ts = [float(x) for x in sys.argv[2].split(",")]
    model = sys.argv[3] if len(sys.argv) > 3 else "add"
    Nscale = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    out = []
    tall = time.time()
    for T in Ts:
        r = run_T(T, model, Nscale)
        out.append(r)
        print(json.dumps({"T0": r["T0"], "secs": r["seconds"],
                          "Lstar": [(x["delta"], None if x["L_star"] is None else round(x["L_star"], 4)) for x in r["rows"]],
                          "LN": round(r["rows"][0]["L_nyquist"], 4)}), flush=True)
    import scipy, mpmath
    meta = {"experiment": "detection threshold of injected off-line quadruple", "deltas": DELTAS, "L_cap": LCAP,
            "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
            "mpmath": mpmath.__version__, "runtime_s": round(time.time() - tall, 1), "kappa_cross": kappa_cross()}
    path = os.path.join(RES, f"detect_{tag}.json")
    with open(path, "w") as f:
        json.dump({"meta": meta, "results": out}, f)
    print("wrote", path, hashlib.sha256(open(path, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
