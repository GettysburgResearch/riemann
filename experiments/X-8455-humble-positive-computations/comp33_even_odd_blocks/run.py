#!/usr/bin/env python3
"""C33 — even/odd block diagonalization of the windowed Loewner matrix.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

If Q maps even→even and odd→odd (nodes symmetric about 0), then the soft
mode and structural kernel live in separate invariant subspaces. Measure
off-block leakage ||Q_eo|| / ||Q||.
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
    Q = np.zeros((len(nodes), len(nodes)))
    for i, li in enumerate(nodes):
        for j, lj in enumerate(nodes):
            Q[i, j] = float(np.real(a[li] if i == j else (b[li] - b[lj]) / (li - lj)))
    return nodes, 0.5 * (Q + Q.T)


def even_odd_split(nodes, Q):
    # basis change: even coords j>=0 with e_j=(e_j+e_{-j})/√(2or1), odd j>0
    idx = {nodes[i]: i for i in range(len(nodes))}
    ev_nodes = [j for j in nodes if j >= 0]
    od_nodes = [j for j in nodes if j > 0]
    Be = np.zeros((len(nodes), len(ev_nodes)))
    Bo = np.zeros((len(nodes), len(od_nodes)))
    for t, j in enumerate(ev_nodes):
        if j == 0:
            Be[idx[0], t] = 1.0
        else:
            Be[idx[j], t] = 1 / np.sqrt(2)
            Be[idx[-j], t] = 1 / np.sqrt(2)
    for t, j in enumerate(od_nodes):
        Bo[idx[j], t] = 1 / np.sqrt(2)
        Bo[idx[-j], t] = -1 / np.sqrt(2)
    Qee = Be.T @ Q @ Be
    Qoo = Bo.T @ Q @ Bo
    Qeo = Be.T @ Q @ Bo
    Qoe = Bo.T @ Q @ Be
    fro = lambda A: float(np.linalg.norm(A, "fro"))
    leak = fro(Qeo) / (fro(Q) + 1e-30)
    ewe = np.linalg.eigvalsh(0.5 * (Qee + Qee.T))
    ewo = np.linalg.eigvalsh(0.5 * (Qoo + Qoo.T))
    return {
        "leak_eo_over_Q": leak,
        "fro_Qeo": fro(Qeo),
        "fro_Qoe": fro(Qoe),
        "fro_Q": fro(Q),
        "even_eigs": [float(x) for x in ewe],
        "odd_eigs": [float(x) for x in ewo],
        "even_min_abs": float(np.min(np.abs(ewe))),
        "odd_min": float(np.min(ewo)),
        "odd_min_pos": float(np.min(ewo[ewo > 1e-12])) if np.any(ewo > 1e-12) else None,
    }


def main():
    print("=== C33 even/odd Loewner blocks ===", flush=True)
    rows = []
    for N in (3, 4, 5, 6, 8):
        for alpha in (0.995, 0.99, 0.98, 0.976, 0.97):
            nodes, Q = loewner_Q(float(alpha), N)
            split = even_odd_split(nodes, Q)
            row = {"N": N, "alpha": float(alpha), **split}
            rows.append(row)
            print(
                f"N={N} a={alpha} leak={split['leak_eo_over_Q']:.3e} "
                f"even_minabs={split['even_min_abs']:.3e} odd_min={split['odd_min']:.6f}",
                flush=True,
            )
    leaks = [r["leak_eo_over_Q"] for r in rows]
    payload = {
        "schema": "riemann.x8455.comp33.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float change-of-basis; leakage near machine epsilon supports exact block diagonalization.",
        "rows": rows,
        "leak_summary": {
            "max": float(np.max(leaks)),
            "mean": float(np.mean(leaks)),
            "median": float(np.median(leaks)),
        },
        "suggested_questions_for_other_agents": [
            "Prove Q is exactly even/odd block diagonal for symmetric node sets and even coefficient sequences p_{-j}=p_j.",
            "Is the structural kernel exactly the lowest even mode, and α_def the zero of the lowest odd mode?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp33.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp33.txt").write_text(json_dumps(payload["leak_summary"], indent=2) + "\n")
    print("leak_summary", payload["leak_summary"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
