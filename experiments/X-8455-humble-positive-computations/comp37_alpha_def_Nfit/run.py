#!/usr/bin/env python3
"""C37 — fit α_def(N) from C34 and extrapolate N→∞.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from jsonutil import dumps as json_dumps  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)
SRC = ROOT / "comp34_odd_only_alpha_def" / "results" / "comp34.json"


def main():
    data = json.loads(SRC.read_text())
    defs = data["alpha_def_odd_only"]
    Ns = np.array(sorted(int(k) for k in defs), dtype=float)
    ys = np.array([defs[str(int(n))]["alpha_def_mid"] for n in Ns])
    print("N", Ns, "y", ys, flush=True)

    fits = {}
    # model: a + b/N^p for p in 1,2,3,4
    for p in (1, 2, 3, 4):
        A = np.vstack([np.ones_like(Ns), Ns ** (-p)]).T
        coef, _, _, _ = np.linalg.lstsq(A, ys, rcond=None)
        pred = A @ coef
        rmse = float(np.sqrt(np.mean((ys - pred) ** 2)))
        r2 = float(1 - np.sum((ys - pred) ** 2) / np.sum((ys - ys.mean()) ** 2))
        fits[f"a+b/N^{p}"] = {
            "a_inf": float(coef[0]),
            "b": float(coef[1]),
            "rmse": rmse,
            "r2": r2,
        }
        print(f"p={p}", fits[f"a+b/N^{p}"], flush=True)

    # also a + b/N^2 + c/N^4
    A = np.vstack([np.ones_like(Ns), Ns ** (-2), Ns ** (-4)]).T
    coef, _, _, _ = np.linalg.lstsq(A, ys, rcond=None)
    pred = A @ coef
    rmse = float(np.sqrt(np.mean((ys - pred) ** 2)))
    r2 = float(1 - np.sum((ys - pred) ** 2) / np.sum((ys - ys.mean()) ** 2))
    fits["a+b/N^2+c/N^4"] = {
        "a_inf": float(coef[0]),
        "b": float(coef[1]),
        "c": float(coef[2]),
        "rmse": rmse,
        "r2": r2,
    }
    print("2+4", fits["a+b/N^2+c/N^4"], flush=True)

    best = min(fits.items(), key=lambda kv: kv[1]["rmse"])
    payload = {
        "schema": "riemann.x8455.comp37.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Tiny-N extrapolation; not a limit theorem.",
        "source": str(SRC),
        "Ns": [int(n) for n in Ns],
        "alpha_def": [float(y) for y in ys],
        "fits": fits,
        "best_by_rmse": {"model": best[0], **best[1]},
        "suggested_questions_for_other_agents": [
            "Is lim α_def(N) equal to some explicit Φ-moment threshold?",
            "Does the 1/N^2 model match a continuum odd Sturm–Liouville reduction?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp37.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp37.txt").write_text(json_dumps({"best": payload["best_by_rmse"], "fits": fits}, indent=2) + "\n")
    print("best", best, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
