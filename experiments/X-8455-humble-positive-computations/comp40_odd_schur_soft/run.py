#!/usr/bin/env python3
"""C40 — odd Schur({±1}) vs λ_soft (mirror of C39 for the soft mode).

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C29: full odd-subspace min = λ_soft exactly; Schur-antisym on ±1 was ~1.004.
Here: Schur-reduce the *odd rest* {|j|≥3 odd} onto the ±1 odd coordinate and
compare that 1×1 (or 2×2 before antisym) Rayleigh to λ_soft.
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
    p = [F(nstr(v, 26, strip_zeros=False)) for v in vals]
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
    print("=== C40 odd Schur({±1}) vs lambda_soft ===", flush=True)
    rows = []
    for N in (4, 6, 8, 10):
        for alpha in np.linspace(0.995, 0.976, 10):
            nodes, Q = loewner(float(alpha), N)
            idx = {nodes[i]: i for i in range(len(nodes))}
            # odd basis j=1,3,5,...
            odds = [j for j in range(1, N + 1)]
            B = np.zeros((len(nodes), len(odds)))
            for t, j in enumerate(odds):
                B[idx[j], t] = 1 / np.sqrt(2)
                B[idx[-j], t] = -1 / np.sqrt(2)
            Qo = 0.5 * ((B.T @ Q @ B) + (B.T @ Q @ B).T)
            soft_odd = float(np.min(np.linalg.eigvalsh(Qo)))

            # Schur keep j=1 (first coord), rest = higher odd
            if len(odds) == 1:
                schur1 = float(Qo[0, 0])
            else:
                keep = [0]
                rest = list(range(1, len(odds)))
                Qkk = Qo[np.ix_(keep, keep)]
                Qkr = Qo[np.ix_(keep, rest)]
                Qrk = Qo[np.ix_(rest, keep)]
                Qrr = Qo[np.ix_(rest, rest)]
                S = Qkk - Qkr @ np.linalg.solve(Qrr, Qrk)
                schur1 = float(S[0, 0])

            # also full-matrix soft (skip near0)
            ew = np.linalg.eigvalsh(Q)
            k0 = int(np.argmin(np.abs(ew)))
            soft_full = float(np.min([e for i, e in enumerate(ew) if i != k0]))

            row = {
                "N": N,
                "alpha": float(alpha),
                "soft_odd": soft_odd,
                "soft_full_nonkernel": soft_full,
                "schur_odd_pm1": schur1,
                "ratio_schur_over_soft": schur1 / soft_odd if soft_odd != 0 else None,
                "abs_err": abs(schur1 - soft_odd),
            }
            rows.append(row)
            print(
                f"N={N} a={alpha:.4f} soft={soft_odd:.6f} schur1={schur1:.6f} "
                f"ratio={row['ratio_schur_over_soft']:.8f} err={row['abs_err']:.3e}",
                flush=True,
            )

    ratios = [r["ratio_schur_over_soft"] for r in rows]
    payload = {
        "schema": "riemann.x8455.comp40.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float odd Schur 1×1 on the ±1 odd coordinate.",
        "rows": rows,
        "summary": {
            "mean_ratio": float(np.mean(ratios)),
            "std_ratio": float(np.std(ratios)),
            "mean_abs_err": float(np.mean([r["abs_err"] for r in rows])),
            "max_abs_err": float(np.max([r["abs_err"] for r in rows])),
        },
        "suggested_questions_for_other_agents": [
            "Is λ_soft exactly the odd-Schur({±1}) scalar (1×1 after eliminating higher odd modes)?",
            "Does α_def solve odd-Schur({±1})(α)=0?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp40.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp40.txt").write_text(json_dumps(payload["summary"], indent=2) + "\n")
    print("summary", payload["summary"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
