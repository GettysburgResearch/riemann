#!/usr/bin/env python3
"""C18 — do Gaussian / Hermite-ish transitions also begin with a p±2 flip?

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi, nstr, exp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi, Phi_gaussian  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 35
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def Phi_hermiteish(t):
    t = mpf(t)
    return (t * t) * exp(-pi * t * t)


def analyze_kernel(name, kern, alpha_lo, alpha_hi, N=6, npts=40):
    alphas = np.linspace(alpha_hi, alpha_lo, npts)  # descending
    rows = []
    prev_signs = None
    for a in alphas:
        nodes = list(range(-N, N + 1))
        vals = [((-1) ** j) * Fwin(float(a), j, kern) for j in nodes]
        p = [F(nstr(v, 22, strip_zeros=False)) for v in vals]
        signs = "".join("+" if v > 0 else "-" if v < 0 else "0" for v in p)
        sc = sum(1 for x, y in zip(p, p[1:]) if x * y < 0)
        # deficit
        s = sp.symbols("s")
        P = 0
        for i, lam in enumerate(nodes):
            term = 1
            for mu in nodes:
                if mu != lam:
                    term *= mu - s
            P += sp.Rational(p[i]) * term
        P = sp.Poly(sp.expand(P), s)
        deg = int(P.degree())
        g = sp.gcd(P, P.diff())
        nre = int(sp.Poly(P.quo(g), s).count_roots())
        # p2 value
        p2 = float(vals[nodes.index(2)])
        row = {
            "alpha": float(a),
            "deficit": deg - nre,
            "sign_changes": sc,
            "sign_pattern": signs,
            "p2": p2,
            "pattern_changed": prev_signs is not None and signs != prev_signs,
        }
        rows.append(row)
        prev_signs = signs
    # summarize jumps
    sc0, d0, pat0 = rows[0]["sign_changes"], rows[0]["deficit"], rows[0]["sign_pattern"]
    jumps = {"sign_alpha": None, "deficit_alpha": None, "p2_sign_flip_alpha": None, "new_pattern": None}
    p2_sign0 = np.sign(rows[0]["p2"])
    for r in rows[1:]:
        if jumps["sign_alpha"] is None and r["sign_changes"] != sc0:
            jumps["sign_alpha"] = r["alpha"]
            jumps["new_pattern"] = r["sign_pattern"]
        if jumps["deficit_alpha"] is None and r["deficit"] != d0:
            jumps["deficit_alpha"] = r["alpha"]
        if jumps["p2_sign_flip_alpha"] is None and np.sign(r["p2"]) != p2_sign0 and np.sign(r["p2"]) != 0:
            jumps["p2_sign_flip_alpha"] = r["alpha"]
    return {"kernel": name, "jumps": jumps, "start_pattern": pat0, "rows": rows}


def main():
    print("=== C18 cross-kernel p2 / cascade ===", flush=True)
    # ranges tuned from earlier deep scans
    jobs = [
        ("Phi", Phi, 0.90, 1.05),
        ("Gaussian", Phi_gaussian, 0.20, 0.70),
        ("Hermiteish", Phi_hermiteish, 0.20, 0.70),
    ]
    results = []
    for name, kern, lo, hi in jobs:
        res = analyze_kernel(name, kern, lo, hi, N=6, npts=35)
        results.append(res)
        print(name, res["jumps"], "start", res["start_pattern"], flush=True)

    payload = {
        "schema": "riemann.x8455.comp18.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Grid-limited jump alphas. Pattern comparison is qualitative.",
        "results": results,
        "suggested_questions_for_other_agents": [
            "Is a p±2 flip the universal first instability for even positive kernels, or special to Φ?",
            "Do Gaussian/Hermite cascades skip the precursor and jump deficit+signs together?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp18.json").write_text(text)
    (OUT / "comp18.txt").write_text(
        "\n".join(f"{r['kernel']}: {r['jumps']} start={r['start_pattern']}" for r in results) + "\n"
    )
    print("wrote", OUT / "comp18.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
