#!/usr/bin/env python3
"""C39 — Schur-reduce even rest onto {0,±1}; null ratio should match full.

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


def main():
    print("=== C39 even Schur {0,±1} kernel ratio ===", flush=True)
    rows = []
    for N in (4, 6, 8, 10):
        for alpha in np.linspace(0.995, 0.976, 8):
            nodes, Q = loewner(float(alpha), N)
            idx = {nodes[i]: i for i in range(len(nodes))}
            # even basis all j>=0
            ev = [j for j in nodes if j >= 0]
            B = np.zeros((len(nodes), len(ev)))
            for t, j in enumerate(ev):
                if j == 0:
                    B[idx[0], t] = 1.0
                else:
                    B[idx[j], t] = B[idx[-j], t] = 1 / np.sqrt(2)
            Qe = B.T @ Q @ B
            # keep first two coords: j=0 and j=1 (since ev sorted? ensure order)
            # rebuild with explicit order
            ev = [0] + [j for j in range(1, N + 1)]
            B = np.zeros((len(nodes), len(ev)))
            for t, j in enumerate(ev):
                if j == 0:
                    B[idx[0], t] = 1.0
                else:
                    B[idx[j], t] = B[idx[-j], t] = 1 / np.sqrt(2)
            Qe = 0.5 * ((B.T @ Q @ B) + (B.T @ Q @ B).T)
            keep = [0, 1]
            rest = list(range(2, len(ev)))
            Qkk = Qe[np.ix_(keep, keep)]
            Qkr = Qe[np.ix_(keep, rest)]
            Qrk = Qe[np.ix_(rest, keep)]
            Qrr = Qe[np.ix_(rest, rest)]
            S = Qkk - Qkr @ np.linalg.solve(Qrr, Qrk)
            Ss = 0.5 * (S + S.T)
            ee, ve = np.linalg.eigh(Ss)
            k = int(np.argmin(np.abs(ee)))
            w = ve[:, k]
            schur_ratio = float(-np.sqrt(2) * w[0] / w[1])

            # full
            ew, evv = np.linalg.eigh(Q)
            k0 = int(np.argmin(np.abs(ew)))
            v = evv[:, k0]
            v0 = float(v[idx[0]])
            v1 = float(0.5 * (v[idx[1]] + v[idx[-1]]))
            full_ratio = -v0 / v1

            # raw 2x2
            ee2, ve2 = np.linalg.eigh(Qkk)
            k2 = int(np.argmin(np.abs(ee2)))
            w2 = ve2[:, k2]
            raw_ratio = float(-np.sqrt(2) * w2[0] / w2[1])

            row = {
                "N": N,
                "alpha": float(alpha),
                "full_ratio": full_ratio,
                "schur_ratio": schur_ratio,
                "raw2_ratio": raw_ratio,
                "abs_err_schur": abs(schur_ratio - full_ratio),
                "abs_err_raw2": abs(raw_ratio - full_ratio),
                "schur_null_eig": float(ee[k]),
            }
            rows.append(row)
            print(
                f"N={N} a={alpha:.4f} full={full_ratio:.6f} schur={schur_ratio:.6f} "
                f"errS={row['abs_err_schur']:.3e} err2={row['abs_err_raw2']:.3e}",
                flush=True,
            )

    payload = {
        "schema": "riemann.x8455.comp39.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float even Schur; looking for exact 2×2 reduction of the kernel.",
        "rows": rows,
        "summary": {
            "mean_abs_err_schur": float(np.mean([r["abs_err_schur"] for r in rows])),
            "max_abs_err_schur": float(np.max([r["abs_err_schur"] for r in rows])),
            "mean_abs_err_raw2": float(np.mean([r["abs_err_raw2"] for r in rows])),
            "max_abs_err_raw2": float(np.max([r["abs_err_raw2"] for r in rows])),
        },
        "suggested_questions_for_other_agents": [
            "Does even-Schur({0,±1}) null ratio equal the full kernel ratio to machine precision?",
            "Write the 2×2 even Schur entries in terms of divided differences of p.",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp39.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp39.txt").write_text(json_dumps(payload["summary"], indent=2) + "\n")
    print("summary", payload["summary"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
