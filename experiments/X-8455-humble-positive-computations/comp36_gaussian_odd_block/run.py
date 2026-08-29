#!/usr/bin/env python3
"""C36 — Gaussian-kernel control: even/odd split + delayed deficit?

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C8/C18: Gaussian has a p2-type flip but no Φ-like delayed deficit.
Check whether Loewner is still even/odd block diagonal, and whether the odd
ground state crosses 0 near the flip or much later.
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
from phi_xi import Fwin, Phi_gaussian  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def pack(alpha, N, kern):
    nodes = list(range(-N, N + 1))
    vals = [((-1) ** j) * Fwin(alpha, j, kern) for j in nodes]
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
    Qs = 0.5 * (Q + Q.T)
    idx = {nodes[i]: i for i in range(len(nodes))}
    ev_nodes = [j for j in nodes if j >= 0]
    od_nodes = [j for j in nodes if j > 0]
    Be = np.zeros((len(nodes), len(ev_nodes)))
    Bo = np.zeros((len(nodes), len(od_nodes)))
    for t, j in enumerate(ev_nodes):
        if j == 0:
            Be[idx[0], t] = 1.0
        else:
            Be[idx[j], t] = Be[idx[-j], t] = 1 / np.sqrt(2)
    for t, j in enumerate(od_nodes):
        Bo[idx[j], t] = 1 / np.sqrt(2)
        Bo[idx[-j], t] = -1 / np.sqrt(2)
    Qee = Be.T @ Qs @ Be
    Qoo = Bo.T @ Qs @ Bo
    Qeo = Be.T @ Qs @ Bo
    ewe = np.linalg.eigvalsh(0.5 * (Qee + Qee.T))
    ewo = np.linalg.eigvalsh(0.5 * (Qoo + Qoo.T))
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    nre = int(sp.Poly(P.quo(g), s).count_roots())
    return {
        "p2": float(vals[nodes.index(2)]),
        "deficit": deg - nre,
        "leak": float(np.linalg.norm(Qeo, "fro") / (np.linalg.norm(Qs, "fro") + 1e-30)),
        "even_min_abs": float(np.min(np.abs(ewe))),
        "odd_min": float(np.min(ewo)),
    }


def main():
    print("=== C36 Gaussian odd-block control ===", flush=True)
    rows = []
    for N in (4, 6):
        for alpha in np.linspace(0.9, 0.2, 36):
            r = pack(float(alpha), N, Phi_gaussian)
            row = {"N": N, "alpha": float(alpha), **r}
            rows.append(row)
            if abs(alpha * 20 - round(alpha * 20)) < 1e-9 or r["deficit"] or r["p2"] * rows[-2]["p2"] < 0 if len(rows) > 1 and rows[-2]["N"] == N else False:
                print(
                    f"N={N} a={alpha:.3f} p2={r['p2']:.4e} def={r['deficit']} "
                    f"odd={r['odd_min']:.4f} leak={r['leak']:.2e}",
                    flush=True,
                )

    # find p2 zero and odd_min zero roughly
    summary = {}
    for N in (4, 6):
        sub = [r for r in rows if r["N"] == N]
        p2_cross = None
        odd_cross = None
        for a, b in zip(sub, sub[1:]):
            if p2_cross is None and a["p2"] * b["p2"] <= 0:
                p2_cross = 0.5 * (a["alpha"] + b["alpha"])
            if odd_cross is None and a["odd_min"] * b["odd_min"] <= 0:
                odd_cross = 0.5 * (a["alpha"] + b["alpha"])
        summary[str(N)] = {
            "p2_cross_approx": p2_cross,
            "odd_min_cross_approx": odd_cross,
            "max_leak": float(max(r["leak"] for r in sub)),
            "min_even_min_abs": float(min(r["even_min_abs"] for r in sub)),
        }
        print("summary", N, summary[str(N)], flush=True)

    payload = {
        "schema": "riemann.x8455.comp36.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Gaussian control; compares cascade anatomy to Φ.",
        "rows": rows,
        "summary": summary,
        "suggested_questions_for_other_agents": [
            "Is even/odd block diagonalization universal for even coefficient sequences?",
            "Why does Gaussian odd_min cross near p2 while Φ delays to α_def≪α*?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp36.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp36.txt").write_text(json_dumps(summary, indent=2) + "\n")
    print("wrote", OUT / "comp36.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
