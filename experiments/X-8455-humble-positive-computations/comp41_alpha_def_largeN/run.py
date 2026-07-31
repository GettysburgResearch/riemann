#!/usr/bin/env python3
"""C41 — push odd-only α_def to larger N (14,16,20) for extrapolation.

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

mp.dps = 35
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def odd_min(alpha, N, digits=22):
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
    Qs = 0.5 * (Q + Q.T)
    idx = {nodes[i]: i for i in range(len(nodes))}
    odds = [j for j in nodes if j > 0]
    B = np.zeros((len(nodes), len(odds)))
    for t, j in enumerate(odds):
        B[idx[j], t] = 1 / np.sqrt(2)
        B[idx[-j], t] = -1 / np.sqrt(2)
    Qo = B.T @ Qs @ B
    return float(np.min(np.linalg.eigvalsh(0.5 * (Qo + Qo.T))))


def main():
    print("=== C41 large-N odd alpha_def ===", flush=True)
    # include previous C34 points plus new
    prev = {
        4: 0.9734385944092645,
        5: 0.9745642049359158,
        6: 0.9750627888059245,
        8: 0.9754669242082166,
        10: 0.9756154785668478,
        12: 0.9756828425684942,
    }
    defs = {str(k): {"alpha_def_mid": v, "source": "C34"} for k, v in prev.items()}
    for N in (14, 16, 18, 20):
        lo, hi = 0.9745, 0.9770
        for _ in range(22):
            mid = 0.5 * (lo + hi)
            om = odd_min(mid, N)
            if om < 0:
                lo = mid
            else:
                hi = mid
            print(f"N={N} mid={mid:.8f} odd_min={om:.3e}", flush=True)
        defs[str(N)] = {
            "alpha_def_mid": 0.5 * (lo + hi),
            "alpha_def_lo": lo,
            "alpha_def_hi": hi,
            "source": "C41",
        }
        print("DONE N", N, defs[str(N)], flush=True)

    Ns = np.array(sorted(int(k) for k in defs), dtype=float)
    ys = np.array([defs[str(int(n))]["alpha_def_mid"] for n in Ns])
    fits = {}
    for p in (2, 3, 4):
        A = np.vstack([np.ones_like(Ns), Ns ** (-p)]).T
        coef, _, _, _ = np.linalg.lstsq(A, ys, rcond=None)
        pred = A @ coef
        rmse = float(np.sqrt(np.mean((ys - pred) ** 2)))
        fits[f"a+b/N^{p}"] = {"a_inf": float(coef[0]), "b": float(coef[1]), "rmse": rmse}
    A = np.vstack([np.ones_like(Ns), Ns ** (-2), Ns ** (-4)]).T
    coef, _, _, _ = np.linalg.lstsq(A, ys, rcond=None)
    pred = A @ coef
    fits["a+b/N^2+c/N^4"] = {
        "a_inf": float(coef[0]),
        "b": float(coef[1]),
        "c": float(coef[2]),
        "rmse": float(np.sqrt(np.mean((ys - pred) ** 2))),
    }
    print("fits", fits, flush=True)

    payload = {
        "schema": "riemann.x8455.comp41.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Larger N still tiny; float Loewner. Extrapolation provisional.",
        "alpha_def": defs,
        "fits": fits,
        "suggested_questions_for_other_agents": [
            "With N≤20, does a_inf stabilize near 0.9758–0.9760?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp41.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp41.txt").write_text(json_dumps({"defs": defs, "fits": fits}, indent=2) + "\n")
    print("wrote", OUT / "comp41.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
