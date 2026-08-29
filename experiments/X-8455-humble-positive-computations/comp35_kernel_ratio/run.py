#!/usr/bin/env python3
"""C35 — v0/v1 ratio of the even kernel vs α, N; compare to √2, 2, e, …

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY
"""

from __future__ import annotations

import hashlib
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def kernel_ratio(alpha, N):
    nodes = list(range(-N, N + 1))
    vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
    p = [F(nstr(v, 28, strip_zeros=False)) for v in vals]
    s = sp.symbols("s")
    P = 0
    for i, lam in enumerate(nodes):
        term = 1
        for mu in nodes:
            if mu != lam:
                term *= mu - s
        P += sp.Rational(p[i]) * term
    P = sp.Poly(sp.expand(P), s)
    Pd = sp.diff(P.as_expr(), P.gen)
    Pdd = sp.diff(Pd, P.gen)
    b, a = {}, {}
    for lam in nodes:
        Pi = complex(P.as_expr().subs(P.gen, lam))
        Pdi = complex(Pd.subs(P.gen, lam))
        Pddi = complex(Pdd.subs(P.gen, lam))
        b[lam] = -Pdi / Pi
        a[lam] = (Pdi * Pdi - Pi * Pddi) / (Pi * Pi)
    Q = np.zeros((len(nodes), len(nodes)))
    for i, li in enumerate(nodes):
        for j, lj in enumerate(nodes):
            Q[i, j] = float(np.real(a[li] if i == j else (b[li] - b[lj]) / (li - lj)))
    ew, ev = np.linalg.eigh(0.5 * (Q + Q.T))
    k0 = int(np.argmin(np.abs(ew)))
    v = ev[:, k0]
    idx = {nodes[i]: i for i in range(len(nodes))}
    v0 = float(v[idx[0]])
    v1 = float(0.5 * (v[idx[1]] + v[idx[-1]]))  # even part
    tail = float(np.sqrt(sum(v[idx[j]] ** 2 for j in nodes if abs(j) >= 2)))
    ratio = None if abs(v1) < 1e-30 else -v0 / v1  # positive if opposite signs
    return {
        "null_eig": float(ew[k0]),
        "v0": v0,
        "v1_even": v1,
        "ratio_minus_v0_over_v1": ratio,
        "tail_l2": tail,
        "mass_0_pm1": float(v0**2 + 2 * v1**2),
    }


def main():
    print("=== C35 even-kernel v0/v1 ratio ===", flush=True)
    rows = []
    for N in (3, 4, 5, 6, 8, 10):
        for alpha in np.linspace(0.995, 0.976, 10):
            row = {"N": N, "alpha": float(alpha), **kernel_ratio(float(alpha), N)}
            rows.append(row)
            print(
                f"N={N} a={alpha:.4f} ratio={row['ratio_minus_v0_over_v1']:.6f} "
                f"tail={row['tail_l2']:.3e} mass01={row['mass_0_pm1']:.6f}",
                flush=True,
            )

    ratios = [r["ratio_minus_v0_over_v1"] for r in rows if r["ratio_minus_v0_over_v1"]]
    cands = {
        "2": 2.0,
        "sqrt(2)*sqrt(2)?": 2.0,
        "sqrt(6)": math.sqrt(6),  # laplace (2,-1,-1) => |v0/v1|=2
        "sqrt(5)": math.sqrt(5),
        "e/1": math.e,
        "pi/sqrt(2)": math.pi / math.sqrt(2),
        "2*sqrt(2)/sqrt(3)?": 2 * math.sqrt(2) / math.sqrt(3),
        "sqrt(8/1.5)?": math.sqrt(8 / 1.5),
    }
    # For discrete Laplacian (2,-1,-1)/norm, |v0/v1|=2 exactly.
    mean_r = float(np.mean(ratios))
    diffs = {k: abs(mean_r - v) for k, v in cands.items()}
    payload = {
        "schema": "riemann.x8455.comp35.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Constant fishing on a float ratio; Laplacian predicts 2.",
        "rows": rows,
        "ratio_mean": mean_r,
        "ratio_std": float(np.std(ratios)),
        "ratio_min": float(np.min(ratios)),
        "ratio_max": float(np.max(ratios)),
        "candidate_diffs_vs_mean": diffs,
        "nearest_candidate": min(diffs, key=diffs.get),
        "suggested_questions_for_other_agents": [
            "Is the even kernel exactly the discrete Laplacian null of the 3-point stencil, deformed by tiny tails?",
            "Why is |v0/v1| ≈ 2.40 rather than 2 — closed form?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp35.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp35.txt").write_text(
        json_dumps(
            {
                "ratio_mean": mean_r,
                "nearest": payload["nearest_candidate"],
                "diffs": diffs,
            },
            indent=2,
        )
        + "\n"
    )
    print("mean_ratio", mean_r, "nearest", payload["nearest_candidate"], diffs[payload["nearest_candidate"]], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
