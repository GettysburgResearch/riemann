#!/usr/bin/env python3
"""C38 — predict even-kernel |v0/v1| from the 3×3 even Loewner block alone.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

If the null vector is supported on {0,±1}, its ratio is the nullvector of the
even 3×3 (coords: δ0, (δ1+δ_{-1})/√2, and optionally higher even modes
projected out). Compare predicted ratio to full-Q null ratio (C35).
"""

from __future__ import annotations

import hashlib
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


def loewner(alpha, N):
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
    return nodes, 0.5 * (Q + Q.T)


def even_basis(nodes, max_j):
    """Even basis up to |j|<=max_j: e0=δ0, e_j=(δ_j+δ_{-j})/√2 for j=1..max_j."""
    idx = {nodes[i]: i for i in range(len(nodes))}
    js = [j for j in range(0, max_j + 1) if j in idx and -j in idx]
    B = np.zeros((len(nodes), len(js)))
    for t, j in enumerate(js):
        if j == 0:
            B[idx[0], t] = 1.0
        else:
            B[idx[j], t] = B[idx[-j], t] = 1 / np.sqrt(2)
    return js, B


def main():
    print("=== C38 even-3 predicted kernel ratio ===", flush=True)
    rows = []
    for N in (4, 6, 8):
        for alpha in (0.995, 0.99, 0.98, 0.976):
            nodes, Q = loewner(float(alpha), N)
            # full null ratio
            ew, ev = np.linalg.eigh(Q)
            k0 = int(np.argmin(np.abs(ew)))
            v = ev[:, k0]
            idx = {nodes[i]: i for i in range(len(nodes))}
            v0 = float(v[idx[0]])
            v1 = float(0.5 * (v[idx[1]] + v[idx[-1]]))
            full_ratio = None if abs(v1) < 1e-30 else -v0 / v1

            pred = {}
            for m in (1, 2, 3, min(N, 4)):
                js, B = even_basis(nodes, m)
                Qe = B.T @ Q @ B
                ee, ve = np.linalg.eigh(0.5 * (Qe + Qe.T))
                k = int(np.argmin(np.abs(ee)))
                w = ve[:, k]
                # w[0] is coeff of δ0; w[1] of (δ1+δ-1)/√2
                # physical v1_even = w[1]/√2 if we measured 0.5*(v1+v-1)=w[1]/√2
                # In C35, v1_even = 0.5*(v[1]+v[-1]) = w[1]/√2
                # ratio_minus_v0_over_v1 = -v0 / v1_even = -w[0] / (w[1]/√2) = -√2 w[0]/w[1]
                if abs(w[1]) < 1e-30:
                    r = None
                else:
                    r = -np.sqrt(2) * w[0] / w[1]
                pred[f"even_maxj={m}"] = {
                    "null_eig": float(ee[k]),
                    "ratio": None if r is None else float(r),
                    "abs_err_vs_full": None if r is None or full_ratio is None else abs(float(r) - full_ratio),
                }

            row = {
                "N": N,
                "alpha": float(alpha),
                "full_ratio": full_ratio,
                "full_null_eig": float(ew[k0]),
                "pred": pred,
            }
            rows.append(row)
            p1 = pred.get("even_maxj=1", {})
            print(
                f"N={N} a={alpha} full={full_ratio:.6f} even1={p1.get('ratio')} "
                f"err1={p1.get('abs_err_vs_full')} even2={pred.get('even_maxj=2',{}).get('ratio')}",
                flush=True,
            )

    # summarize even1 errors
    errs1 = [r["pred"]["even_maxj=1"]["abs_err_vs_full"] for r in rows if r["pred"]["even_maxj=1"]["abs_err_vs_full"] is not None]
    errs2 = [r["pred"]["even_maxj=2"]["abs_err_vs_full"] for r in rows if r["pred"]["even_maxj=2"]["abs_err_vs_full"] is not None]
    payload = {
        "schema": "riemann.x8455.comp38.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float even-block nullvectors.",
        "rows": rows,
        "err_summary": {
            "even1_mean_abs_err": float(np.mean(errs1)),
            "even2_mean_abs_err": float(np.mean(errs2)),
            "even1_max_abs_err": float(np.max(errs1)),
            "even2_max_abs_err": float(np.max(errs2)),
        },
        "suggested_questions_for_other_agents": [
            "Is the structural kernel exactly the nullvector of the even 2×2 on {0, (1+-1)/√2}?",
            "Closed form for that 2×2 null ratio in terms of p_j / Loewner a,b?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp38.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp38.txt").write_text(json_dumps(payload["err_summary"], indent=2) + "\n")
    print("err_summary", payload["err_summary"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
