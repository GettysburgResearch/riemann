#!/usr/bin/env python3
"""D3 — finite double-root equations R_N=∂r R_N=0.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Proof-facing form from PR #182 review:
  R_N(α,r)=0,  ∂r R_N(α,r)=0
with R_N(s)=Σ_{j=-N}^N p_j(α)/(j-s).
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from mpmath import mp, mpf, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from collision import solve_finite  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

# seeds: α from C41 ladder, r from continuum
ALPHA_SEEDS = {
    4: 0.97343859,
    5: 0.97456420,
    6: 0.97506279,
    8: 0.97546692,
    10: 0.97561548,
    12: 0.97568284,
    14: 0.97571779,
    16: 0.97573772,
    18: 0.97574991,
    20: 0.97575778,
}
R_SEED = 2.17949
A_INF = mpf("0.975779528461603467680421342178")


def main():
    print("=== D3 finite R=R_r=0 ===", flush=True)
    rows = []
    for N, a0 in ALPHA_SEEDS.items():
        dps = 45 if N <= 12 else 40
        print(f"solving N={N} ...", flush=True)
        sol = solve_finite(N, a0, R_SEED, dps=dps, maxsteps=40)
        a = sol["alpha"]
        gap = A_INF - a
        n3 = (gap) * (N ** 3)
        row = {
            "N": N,
            "alpha_str": sol["alpha_str"],
            "r_str": sol["r_str"],
            "R": sol["R"],
            "R_r": sol["R_r"],
            "alpha_inf_minus_alpha": nstr(gap, 20),
            "N3_times_gap": nstr(n3, 20),
            "seed_alpha": a0,
            "n_newton_steps": len(sol["history"]),
            "dps": dps,
        }
        rows.append(row)
        print(
            f"N={N} a={sol['alpha_str']} r={sol['r_str']} "
            f"R={sol['R']} Rr={sol['R_r']} N3*gap={nstr(n3,12)}",
            flush=True,
        )

    payload = {
        "schema": "riemann.x8455.d3.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "mpmath Newton on R,R_r; not interval-certified.",
        "alpha_infinity_ref": nstr(A_INF, 30),
        "rows": rows,
        "predicted_N3_constant": "0.1866219902712081",
        "suggested_next": [
            "Interval Newton on (R, R_r) for each N with directed coefficient intervals.",
            "Certify root count / inertia on both sides of alpha_N.",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "d3.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "d3.txt").write_text(
        "\n".join(
            f"N={r['N']} a={r['alpha_str']} r={r['r_str']} N3*gap={r['N3_times_gap']}"
            for r in rows
        )
        + "\n"
    )
    print("wrote", OUT / "d3.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
