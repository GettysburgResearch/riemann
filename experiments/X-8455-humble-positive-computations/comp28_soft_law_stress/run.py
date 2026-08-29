#!/usr/bin/env python3
"""C28 — stress the linear soft-mode law across N and digitizations.

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

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def soft_min(alpha, N, digits=26):
    mp.dps = max(30, digits + 5)
    nodes = list(range(-N, N + 1))
    vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
    p = [F(nstr(v, digits, strip_zeros=False)) for v in vals]
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
    ew = np.linalg.eigvalsh(0.5 * (Q + Q.T))
    soft = float(np.min(ew[ew > 1e-12])) if np.any(ew > 1e-12) else None
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    nre = int(sp.Poly(P.quo(g), s).count_roots())
    return soft, deg - nre, float(vals[nodes.index(2)])


def fit_law(alphas, softs):
    A = np.vstack([np.ones(len(alphas)), alphas]).T
    coef, _, _, _ = np.linalg.lstsq(A, softs, rcond=None)
    pred = A @ coef
    rmse = float(np.sqrt(np.mean((softs - pred) ** 2)))
    r2 = float(1 - np.sum((softs - pred) ** 2) / np.sum((softs - softs.mean()) ** 2))
    a0, b = float(coef[0]), float(coef[1])
    return {
        "intercept": a0,
        "slope": b,
        "rmse": rmse,
        "r2": r2,
        "alpha_hit0": None if b == 0 else -a0 / b,
    }


def main():
    print("=== C28 soft law stress ===", flush=True)
    results = []
    alphas = np.linspace(0.994, 0.977, 18)
    for N in (4, 5, 6, 8, 10):
        for digits in (18, 26, 34):
            softs, defs, p2s = [], [], []
            keep_a = []
            for a in alphas:
                sft, d, p2 = soft_min(float(a), N, digits=digits)
                if d != 0 or sft is None:
                    continue
                if p2 <= 0:
                    continue  # only post-α* branch
                softs.append(sft)
                defs.append(d)
                p2s.append(p2)
                keep_a.append(float(a))
            if len(softs) < 5:
                continue
            law = fit_law(np.array(keep_a), np.array(softs))
            row = {"N": N, "digits": digits, "n_pts": len(softs), **law}
            results.append(row)
            print(row, flush=True)

    payload = {
        "schema": "riemann.x8455.comp28.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Rationalization digits and float eigh both matter near the jump.",
        "fits": results,
        "suggested_questions_for_other_agents": [
            "Is slope ≈ 13.25 stable in N and digits?",
            "Does alpha_hit0 converge with N to a universal α_def?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp28.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp28.txt").write_text("\n".join(str(r) for r in results) + "\n")
    print("wrote", OUT / "comp28.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
