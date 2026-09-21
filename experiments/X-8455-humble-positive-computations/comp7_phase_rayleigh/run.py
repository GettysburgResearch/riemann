#!/usr/bin/env python3
"""C7 — does the pole-free terminal Rayleigh track low zeta-zero phases?

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Build complete (uncapped, small) pole-free terminal Hankel cells on a dense a-grid
and correlate min Rayleigh with cos(gamma_j * 2a + phi). Looking for an unexpected
phase lock that would connect the matrix packet to the explicit formula.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np
from mpmath import mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import gammas  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

# reuse helpers from comp3 by import
import importlib.util

spec = importlib.util.spec_from_file_location("c3", ROOT / "comp3_terminal_hankel" / "run.py")
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def corr(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if len(x) < 3 or np.std(x) == 0 or np.std(y) == 0:
        return None
    return float(np.corrcoef(x, y)[0, 1])


def main():
    print("=== C7 phase–Rayleigh lock hunt (provisional) ===", flush=True)
    gs = [float(g) for g in gammas(8)]
    rows = []
    # Keep complete windows: for R=2, a in [4.2, 5.6] => hi=exp(2a) <= exp(11.2)~7e4
    R = 2.0
    x, dx, phis, vminus, G = c3.make_polefree_basis(R, m=5, grid=450)
    for a in np.linspace(4.2, 5.55, 28):
        hi = np.exp(2 * a)
        if hi > 9e4:
            continue
        # complete window (no artificial cap)
        pps, trunc = c3.prime_powers_window(float(a), R, n_cap=None)
        if trunc or len(pps) == 0:
            continue
        H = np.zeros((len(phis), len(phis)))
        for n, c in pps:
            u = 2 * a - np.log(n)
            H += 2 * c * c3.hankel(x, dx, phis, u)
        # almost pole-free already
        Hc = H - 2 * np.exp(a) * np.outer(vminus, vminus)
        stats = c3.rayleigh_stats(Hc, G)
        row = {
            "a": float(a),
            "R": R,
            "n_pps": len(pps),
            "min": stats["min"],
            "max": stats["max"],
            "absmax": stats["absmax"],
            "phases": {f"g{j+1}": float(np.cos(gs[j] * 2 * a)) for j in range(5)},
            "phases_shift3": {f"g{j+1}": float(np.cos(gs[j] * (2 * a - 3.0))) for j in range(5)},
        }
        rows.append(row)
        print(f"a={a:.3f} pps={len(pps)} min={stats['min']:.4f} cos1={row['phases']['g1']:.3f}", flush=True)

    mins = [r["min"] for r in rows]
    corrs = {}
    for key in ("phases", "phases_shift3"):
        corrs[key] = {}
        for j in range(1, 6):
            xs = [r[key][f"g{j}"] for r in rows]
            corrs[key][f"g{j}"] = {
                "corr_with_min": corr(mins, xs),
                "corr_with_absmax": corr([r["absmax"] for r in rows], xs),
            }

    # best single-phase linear predictor residual
    best = None
    for key in ("phases", "phases_shift3"):
        for j in range(1, 6):
            xs = np.array([r[key][f"g{j}"] for r in rows])
            ys = np.array(mins)
            if np.std(xs) == 0:
                continue
            # least squares ys ~ a + b xs
            A = np.vstack([np.ones_like(xs), xs]).T
            coef, _, _, _ = np.linalg.lstsq(A, ys, rcond=None)
            pred = A @ coef
            rmse = float(np.sqrt(np.mean((ys - pred) ** 2)))
            cand = {"family": key, "gamma_index": j, "rmse": rmse, "coef": [float(c) for c in coef], "corr": corr(ys, xs)}
            if best is None or rmse < best["rmse"]:
                best = cand

    payload = {
        "schema": "riemann.x8455.comp7.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Complete-window cells only at R=2 on a short a-interval. Float profiles. "
            "A large correlation is a hint, not an identification with the explicit formula."
        ),
        "rows": rows,
        "correlations": corrs,
        "best_single_phase_fit": best,
        "suggested_questions_for_other_agents": [
            "Does a two-phase fit with gamma1 and gamma2 collapse the residual below the one-phase RMSE?",
            "If profiles are Laplace-tuned to gamma1, does corr(min, cos(gamma1*2a)) approach -1?",
            "Is absmax locked to a different phase than min?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp7.json").write_text(text)
    (OUT / "comp7.txt").write_text(
        "C7 provisional\n"
        + f"n_rows={len(rows)}\n"
        + f"best={best}\n"
        + f"corr_phases={corrs['phases']}\n"
        + f"corr_shift3={corrs['phases_shift3']}\n"
    )
    print("best fit", best, flush=True)
    print("wrote", OUT / "comp7.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
