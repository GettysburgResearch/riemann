#!/usr/bin/env python3
"""D2 — continuum double root: G(α,r)=∂rG(α,r)=0.

Agent: cursor-grok-8455
Status: EMPIRICAL / high-dps discovery (not directed/Arb certified)

Target values from PR #182 review (for cross-check):
  α_∞ = 0.975779528461603467680421342178...
  r_∞ = 2.179490220360796425562316317235...
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from mpmath import mp, mpf, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from collision import solve_continuum, G, G_r  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

REF_A = mpf("0.975779528461603467680421342178")
REF_R = mpf("2.179490220360796425562316317235")


def main():
    print("=== D2 continuum G=G_r=0 ===", flush=True)
    results = []
    for dps in (40, 60, 80):
        # try a few seeds
        for seed in (
            (0.97578, 2.1795),
            (0.9757, 2.18),
            (float(REF_A), float(REF_R)),
        ):
            try:
                sol = solve_continuum(seed[0], seed[1], dps=dps)
            except Exception as exc:  # noqa: BLE001
                print("fail", dps, seed, exc, flush=True)
                continue
            da = abs(sol["alpha"] - REF_A)
            dr = abs(sol["r"] - REF_R)
            row = {
                "dps": dps,
                "seed": seed,
                "alpha": sol["alpha_str"],
                "r": sol["r_str"],
                "G": sol["G_str"],
                "G_r": sol["G_r_str"],
                "abs_diff_alpha_vs_ref": nstr(da, 12),
                "abs_diff_r_vs_ref": nstr(dr, 12),
            }
            results.append(row)
            print(
                f"dps={dps} seed={seed} a={sol['alpha_str']} r={sol['r_str']} "
                f"G={sol['G_str']} Gr={sol['G_r_str']} da={nstr(da,8)} dr={nstr(dr,8)}",
                flush=True,
            )
            break  # one success per dps enough

    # residual at published ref
    mp.dps = 80
    ref_res = {
        "G_at_ref": nstr(G(REF_A, REF_R), 20),
        "G_r_at_ref": nstr(G_r(REF_A, REF_R), 20),
    }
    print("ref residuals", ref_res, flush=True)

    payload = {
        "schema": "riemann.x8455.d2.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "mpmath findroot / quad; not Arb directed balls.",
        "reference_from_review": {
            "alpha_infinity": nstr(REF_A, 30),
            "r_infinity": nstr(REF_R, 30),
        },
        "solutions": results,
        "residuals_at_reference": ref_res,
        "suggested_next": [
            "Certify with interval Newton / Arb that the Jacobian is nonsingular and the root is unique in a box.",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "d2.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "d2.txt").write_text(json_dumps({"solutions": results, "ref_res": ref_res}, indent=2) + "\n")
    print("wrote", OUT / "d2.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
