#!/usr/bin/env python3
"""C19 — watch Loewner eigenvalues through the deficit jump.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Is the deficit-4 event an eigenvalue collision through zero (pair birth),
and does anything spectral move at the p±2 precursor even while n_neg=0?
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


def loewner_eigs(alpha, N=6):
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
    bvals, avals = [], []
    for lam in nodes:
        Pi = complex(P.as_expr().subs(P.gen, lam))
        Pdi = complex(Pd.subs(P.gen, lam))
        Pddi = complex(Pdd.subs(P.gen, lam))
        bvals.append(-Pdi / Pi)
        avals.append((Pdi * Pdi - Pi * Pddi) / (Pi * Pi))
    Q = np.zeros((len(nodes), len(nodes)))
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i == j:
                Q[i, j] = float(np.real(avals[i]))
            else:
                Q[i, j] = float(np.real((bvals[i] - bvals[j]) / (nodes[i] - nodes[j])))
    ew = np.linalg.eigvalsh(0.5 * (Q + Q.T))
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    nre = int(sp.Poly(P.quo(g), s).count_roots())
    return {
        "alpha": alpha,
        "deficit": deg - nre,
        "eigs": [float(x) for x in ew],
        "min_pos": float(np.min(ew[ew > 1e-12])) if np.any(ew > 1e-12) else None,
        "max_neg": float(np.max(ew[ew < -1e-12])) if np.any(ew < -1e-12) else None,
        "n_neg": int(np.sum(ew < -1e-12)),
        "n_zeroish": int(np.sum(np.abs(ew) <= 1e-12)),
        "p2": float(vals[nodes.index(2)]),
    }


def main():
    print("=== C19 Loewner collision scan ===", flush=True)
    alphas = list(np.linspace(1.01, 0.95, 37))
    rows = [loewner_eigs(float(a), N=6) for a in alphas]
    for r in rows:
        print(
            f"a={r['alpha']:.4f} def={r['deficit']} nneg={r['n_neg']} "
            f"min_pos={r['min_pos']} max_neg={r['max_neg']} p2={r['p2']:.3e}",
            flush=True,
        )

    # track the smallest positive eigenvalue around precursor and deficit
    payload = {
        "schema": "riemann.x8455.comp19.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float Loewner from rationalized polys. Near-zero eigs need directed recheck.",
        "rows": rows,
        "suggested_questions_for_other_agents": [
            "Does min_pos dip at the p2 zero without crossing, then a conjugate pair peel off at the deficit?",
            "Is n_zeroish ever >1 (corank), or always exactly the target kernel?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp19.json").write_text(text)
    (OUT / "comp19.txt").write_text(
        "\n".join(
            f"a={r['alpha']:.5f} def={r['deficit']} nneg={r['n_neg']} min_pos={r['min_pos']} max_neg={r['max_neg']}"
            for r in rows
        )
        + "\n"
    )
    print("wrote", OUT / "comp19.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
