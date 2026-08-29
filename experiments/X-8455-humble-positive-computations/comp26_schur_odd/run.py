#!/usr/bin/env python3
"""C26 — Schur complement of the ±1 Loewner block vs λ_soft.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C25 showed the raw principal subblock on {-1,1} does not track λ_soft.
Here: partition nodes into Odd={-1,1} and Rest, form
    S = Q_OO - Q_OR Q_RR^{-1} Q_RO
and compare eig(S) to the full soft eigenvalue / eigenvector mass.

NOTE: schur_min alone is misleading — Q has a structural ~0 mode that
Schur inherits. Compare the *non-kernel* Schur eigenvalue to lambda_soft (C31).
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


def loewner_Q(alpha, N):
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
    n = len(nodes)
    Q = np.zeros((n, n))
    for i, li in enumerate(nodes):
        for j, lj in enumerate(nodes):
            Q[i, j] = float(np.real(a[li] if i == j else (b[li] - b[lj]) / (li - lj)))
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    nre = int(sp.Poly(P.quo(g), s).count_roots())
    return nodes, Q, deg - nre, float(vals[nodes.index(2)])


def schur_odd(nodes, Q, odd_set=(-1, 1)):
    idx = {nodes[i]: i for i in range(len(nodes))}
    o = [idx[j] for j in odd_set]
    r = [i for i in range(len(nodes)) if nodes[i] not in odd_set]
    Qoo = Q[np.ix_(o, o)]
    Qor = Q[np.ix_(o, r)]
    Qro = Q[np.ix_(r, o)]
    Qrr = Q[np.ix_(r, r)]
    # regularize tiny kernel directions if needed
    try:
        S = Qoo - Qor @ np.linalg.solve(Qrr, Qro)
        ok = True
        cond = float(np.linalg.cond(Qrr))
    except np.linalg.LinAlgError:
        S = Qoo
        ok = False
        cond = float("inf")
    ewS = np.linalg.eigvalsh(0.5 * (S + S.T))
    ewQ = np.linalg.eigvalsh(0.5 * (Q + Q.T))
    soft = float(np.min(ewQ[ewQ > 1e-12])) if np.any(ewQ > 1e-12) else None
    # also try odd set = {-1,0,1} and {-2,-1,1,2}
    return {
        "schur_eigs": [float(x) for x in ewS],
        "schur_min": float(np.min(ewS)),
        "lambda_soft_full": soft,
        "ratio": None if soft in (None, 0) else float(np.min(ewS) / soft),
        "solve_ok": ok,
        "cond_Qrr": cond,
    }


def main():
    print("=== C26 Schur odd reductions ===", flush=True)
    rows = []
    for N in (4, 6, 8):
        for alpha in np.linspace(0.995, 0.976, 16):
            nodes, Q, deficit, p2 = loewner_Q(float(alpha), N)
            for name, odd in (
                ("pm1", (-1, 1)),
                ("pm1_0", (-1, 0, 1)),
                ("pm12", (-2, -1, 1, 2)),
                ("odd_all", tuple(j for j in nodes if j % 2 != 0)),
            ):
                sch = schur_odd(nodes, Q, odd)
                row = {
                    "alpha": float(alpha),
                    "N": N,
                    "deficit": deficit,
                    "p2": p2,
                    "block": name,
                    **sch,
                }
                rows.append(row)
            # print pm1 only
            r = [x for x in rows if x["N"] == N and x["alpha"] == float(alpha) and x["block"] == "pm1"][-1]
            print(
                f"N={N} a={alpha:.4f} def={deficit} soft={r['lambda_soft_full']:.6f} "
                f"Schur_pm1={r['schur_min']:.6f} ratio={r['ratio']}",
                flush=True,
            )

    # summarize ratio stability for each block on pass rows
    summary = {}
    for name in ("pm1", "pm1_0", "pm12", "odd_all"):
        ratios = [
            r["ratio"]
            for r in rows
            if r["block"] == name and r["deficit"] == 0 and r["ratio"] is not None and abs(r["ratio"]) < 1e6
        ]
        if ratios:
            summary[name] = {
                "n": len(ratios),
                "mean": float(np.mean(ratios)),
                "std": float(np.std(ratios)),
                "min": float(np.min(ratios)),
                "max": float(np.max(ratios)),
                "mean_abs_log_ratio": float(np.mean(np.abs(np.log(np.abs(ratios))))),
            }

    payload = {
        "schema": "riemann.x8455.comp26.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float Schur complements of rationalized Loewner matrices.",
        "rows": rows,
        "ratio_summary_pass_branch": summary,
        "suggested_questions_for_other_agents": [
            "Is there a block whose Schur min equals lambda_soft (ratio≈1) across alpha?",
            "If odd_all works, is the soft mode exactly the odd subspace ground state?",
            "Does cond(Q_RR) explode at the deficit jump?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp26.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp26.txt").write_text(json_dumps(summary, indent=2) + "\n")
    print("summary", summary, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
