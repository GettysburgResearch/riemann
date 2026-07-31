#!/usr/bin/env python3
"""C21 — quantify Loewner soft-mode slope between α* and the deficit jump."""

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


def main():
    # reuse C19 rows
    c19 = json.loads((ROOT / "comp19_loewner_collision" / "results" / "comp19.json").read_text())
    rows = c19["rows"]
    # focus on pass region after p2 flip: p2>0 and deficit=0
    seg = [r for r in rows if r["deficit"] == 0 and r["p2"] > 0]
    alphas = np.array([r["alpha"] for r in seg])
    mins = np.array([r["min_pos"] for r in seg], float)
    # linear fit min_pos ≈ a + b alpha
    A = np.vstack([np.ones_like(alphas), alphas]).T
    coef, _, _, _ = np.linalg.lstsq(A, mins, rcond=None)
    pred = A @ coef
    rmse = float(np.sqrt(np.mean((mins - pred) ** 2)))
    r2 = float(1 - np.sum((mins - pred) ** 2) / np.sum((mins - mins.mean()) ** 2))
    # also vs p2
    p2s = np.array([r["p2"] for r in seg])
    A2 = np.vstack([np.ones_like(p2s), p2s]).T
    coef2, _, _, _ = np.linalg.lstsq(A2, mins, rcond=None)
    pred2 = A2 @ coef2
    rmse2 = float(np.sqrt(np.mean((mins - pred2) ** 2)))
    r22 = float(1 - np.sum((mins - pred2) ** 2) / np.sum((mins - mins.mean()) ** 2))
    # extrapolate linear-in-alpha to min_pos=0
    a0, b = float(coef[0]), float(coef[1])
    alpha_hit = None if b == 0 else -a0 / b
    payload = {
        "schema": "riemann.x8455.comp21.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Uses float Loewner min_pos from C19; linear fits are descriptive.",
        "n_points": len(seg),
        "fit_vs_alpha": {"intercept": a0, "slope": b, "rmse": rmse, "r2": r2, "alpha_where_fit_hits_0": alpha_hit},
        "fit_vs_p2": {
            "intercept": float(coef2[0]),
            "slope": float(coef2[1]),
            "rmse": rmse2,
            "r2": r22,
        },
        "segment": [{"alpha": r["alpha"], "min_pos": r["min_pos"], "p2": r["p2"]} for r in seg],
        "note": "If alpha_where_fit_hits_0 ≈ deficit jump, soft mode is nearly linear in alpha.",
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp21.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp21.txt").write_text(json_dumps(payload["fit_vs_alpha"], indent=2) + "\n" + json_dumps(payload["fit_vs_p2"], indent=2) + "\n")
    print(payload["fit_vs_alpha"], flush=True)
    print(payload["fit_vs_p2"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
