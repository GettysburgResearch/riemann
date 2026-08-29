#!/usr/bin/env python3
"""C31 — re-read C26: second Schur eigenvalue vs λ_soft (ratio≈1?).

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C26 reported schur_min/soft ≈ 0 because Loewner Q has a structural ~0 mode;
Schur inherits that kernel. The *next* Schur eigenvalue should track λ_soft.
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
SRC = ROOT / "comp26_schur_odd" / "results" / "comp26.json"


def nonkernel_min(eigs, tol=1e-10):
    pos = [e for e in eigs if e > tol]
    return min(pos) if pos else None


def main():
    if not SRC.exists():
        print("missing", SRC)
        return 1
    data = json.loads(SRC.read_text())
    rows_out = []
    for r in data["rows"]:
        soft = r["lambda_soft_full"]
        sch = nonkernel_min(r["schur_eigs"])
        rows_out.append(
            {
                "alpha": r["alpha"],
                "N": r["N"],
                "deficit": r["deficit"],
                "block": r["block"],
                "p2": r["p2"],
                "lambda_soft": soft,
                "schur_nonkernel_min": sch,
                "schur_eigs": r["schur_eigs"],
                "ratio": None if soft in (None, 0) or sch is None else sch / soft,
            }
        )

    summary = {}
    for name in ("pm1", "pm1_0", "pm12", "odd_all"):
        ratios = [
            x["ratio"]
            for x in rows_out
            if x["block"] == name and x["deficit"] == 0 and x["ratio"] is not None
        ]
        if ratios:
            summary[name] = {
                "n": len(ratios),
                "mean": float(np.mean(ratios)),
                "std": float(np.std(ratios)),
                "min": float(np.min(ratios)),
                "max": float(np.max(ratios)),
                "mean_abs_err_from_1": float(np.mean(np.abs(np.array(ratios) - 1))),
            }
            print(name, summary[name], flush=True)

    payload = {
        "schema": "riemann.x8455.comp31.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Reinterpretation of C26 float Schur eigs; kernel threshold 1e-10.",
        "source": str(SRC.relative_to(ROOT.parent.parent)),
        "summary_pass_branch": summary,
        "rows": rows_out,
        "suggested_questions_for_other_agents": [
            "Prove that Schur(±1)_antisym = λ_soft up to the structural kernel.",
            "Is the structural kernel exactly the constants (Loewner annihilates 1)?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp31.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp31.txt").write_text(json_dumps(summary, indent=2) + "\n")
    print("wrote", OUT / "comp31.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
