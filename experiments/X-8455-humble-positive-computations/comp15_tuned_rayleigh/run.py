#!/usr/bin/env python3
"""C15 — Laplace-tune pole-free profiles toward γ₁ and remeasure phase lock.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C7 found corr(min, cos(γ₁ 2a))≈0.997 with generic bumps. Here we bias the
profile basis by multiplying with cos(γ₁ r) / sin(γ₁ r) style carriers, then
recompute the correlation. If the lock is real, tuning should raise |corr| or
shrink RMSE; if it was an accident of the interval, it should degrade.
"""

from __future__ import annotations

import hashlib
import importlib.util
import sys
from pathlib import Path

import numpy as np
from mpmath import mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import gammas  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

spec = importlib.util.spec_from_file_location("c3", ROOT / "comp3_terminal_hankel" / "run.py")
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

mp.dps = 30
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def make_tuned_basis(R, gamma, m=5, grid=450, mode="cos"):
    x = np.linspace(0.0, R, grid)
    dx = x[1] - x[0]
    # start from polefree basis then modulate
    _, _, phis0, _, _ = c3.make_polefree_basis(R, m=m, grid=grid)
    phis = []
    for phi in phis0:
        if mode == "cos":
            phis.append(phi * np.cos(gamma * x))
        elif mode == "sin":
            phis.append(phi * np.sin(gamma * x))
        else:
            phis.append(phi.copy())
    # re-kill Laplace mass
    w = np.exp(-0.5 * x)
    masses = np.array([np.sum(w * y) * dx for y in phis])
    # project out last
    if abs(masses[-1]) > 1e-15:
        phis = [phis[i] - (masses[i] / masses[-1]) * phis[-1] for i in range(len(phis) - 1)]
    vminus = np.array([np.sum(w * phi) * dx for phi in phis])
    G = np.zeros((len(phis), len(phis)))
    for i in range(len(phis)):
        for j in range(i, len(phis)):
            G[i, j] = G[j, i] = np.sum(phis[i] * phis[j]) * dx
    return x, dx, phis, vminus, G


def ladder(mode, gamma, R=2.0):
    x, dx, phis, vminus, G = make_tuned_basis(R, gamma, mode=mode)
    rows = []
    for a in np.linspace(4.2, 5.55, 24):
        hi = np.exp(2 * a)
        if hi > 9e4:
            continue
        pps, trunc = c3.prime_powers_window(float(a), R, n_cap=None)
        if trunc or not pps:
            continue
        H = np.zeros((len(phis), len(phis)))
        for n, c in pps:
            u = 2 * a - np.log(n)
            H += 2 * c * c3.hankel(x, dx, phis, u)
        Hc = H - 2 * np.exp(a) * np.outer(vminus, vminus)
        stats = c3.rayleigh_stats(Hc, G)
        rows.append({"a": float(a), "min": stats["min"], "absmax": stats["absmax"], "n_pps": len(pps)})
    return rows


def fit_corr(rows, gamma):
    mins = np.array([r["min"] for r in rows])
    xs = np.cos(gamma * 2 * np.array([r["a"] for r in rows]))
    if len(mins) < 3 or np.std(xs) == 0 or np.std(mins) == 0:
        return None
    corr = float(np.corrcoef(mins, xs)[0, 1])
    A = np.vstack([np.ones_like(xs), xs]).T
    coef, _, _, _ = np.linalg.lstsq(A, mins, rcond=None)
    pred = A @ coef
    rmse = float(np.sqrt(np.mean((mins - pred) ** 2)))
    r2 = float(1 - np.sum((mins - pred) ** 2) / np.sum((mins - np.mean(mins)) ** 2))
    return {"corr": corr, "rmse": rmse, "r2": r2, "coef": [float(c) for c in coef], "n": len(rows)}


def main():
    print("=== C15 tuned Rayleigh phase lock ===", flush=True)
    g1 = float(gammas(1)[0])
    g2 = float(gammas(2)[1])
    results = {}
    for mode in ("plain", "cos", "sin"):
        # plain uses untuned polefree via mode branch
        if mode == "plain":
            # reuse c3 basis without modulation
            x, dx, phis, vminus, G = c3.make_polefree_basis(2.0, m=5, grid=450)
            rows = []
            for a in np.linspace(4.2, 5.55, 24):
                if np.exp(2 * a) > 9e4:
                    continue
                pps, trunc = c3.prime_powers_window(float(a), 2.0, n_cap=None)
                if trunc or not pps:
                    continue
                H = np.zeros((len(phis), len(phis)))
                for n, c in pps:
                    H += 2 * c * c3.hankel(x, dx, phis, 2 * a - np.log(n))
                Hc = H - 2 * np.exp(a) * np.outer(vminus, vminus)
                stats = c3.rayleigh_stats(Hc, G)
                rows.append({"a": float(a), "min": stats["min"], "absmax": stats["absmax"], "n_pps": len(pps)})
        else:
            rows = ladder(mode, g1)
        fit1 = fit_corr(rows, g1)
        fit2 = fit_corr(rows, g2)
        results[mode] = {"fit_gamma1": fit1, "fit_gamma2": fit2, "n_rows": len(rows)}
        print(mode, "g1", fit1, "g2", fit2, flush=True)

    payload = {
        "schema": "riemann.x8455.comp15.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Modulation+reprojection is a blunt tuning proxy, not an optimal Laplace design.",
        "gamma1": g1,
        "gamma2": g2,
        "results": results,
        "suggested_questions_for_other_agents": [
            "Does cos-modulation increase r^2 for gamma1 relative to plain?",
            "If sin-modulation flips the sign of corr, is the packet picking an odd carrier?",
            "Can an exact complex exponential profile make residual RMSE drop by another order?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp15.json").write_text(text)
    (OUT / "comp15.txt").write_text(json_dumps(results, indent=2) + "\n")
    print("wrote", OUT / "comp15.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
