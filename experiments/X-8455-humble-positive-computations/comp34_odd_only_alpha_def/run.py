#!/usr/bin/env python3
"""C34 — α_def from the odd block alone (ignore even kernel).

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


def odd_min(alpha, N):
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
    Qs = 0.5 * (Q + Q.T)
    idx = {nodes[i]: i for i in range(len(nodes))}
    odds = [j for j in nodes if j > 0]
    B = np.zeros((len(nodes), len(odds)))
    for t, j in enumerate(odds):
        B[idx[j], t] = 1 / np.sqrt(2)
        B[idx[-j], t] = -1 / np.sqrt(2)
    Qo = B.T @ Qs @ B
    return float(np.min(np.linalg.eigvalsh(0.5 * (Qo + Qo.T)))), float(vals[nodes.index(2)])


def main():
    print("=== C34 odd-only alpha_def ===", flush=True)
    defs = {}
    for N in (4, 5, 6, 8, 10, 12):
        lo, hi = 0.968, 0.982
        for _ in range(30):
            mid = 0.5 * (lo + hi)
            om, p2 = odd_min(mid, N)
            if om < 0:
                lo = mid
            else:
                hi = mid
        defs[str(N)] = {
            "alpha_def_mid": 0.5 * (lo + hi),
            "alpha_def_lo": lo,
            "alpha_def_hi": hi,
            "odd_min_at_hi": odd_min(hi, N)[0],
            "odd_min_at_lo": odd_min(lo, N)[0],
        }
        print("N", N, defs[str(N)], flush=True)

    # also sample odd_min vs alpha for N=6
    curve = []
    for a in np.linspace(0.997, 0.97, 28):
        om, p2 = odd_min(float(a), 6)
        curve.append({"alpha": float(a), "odd_min": om, "p2": p2})

    payload = {
        "schema": "riemann.x8455.comp34.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Odd-block float eigh only; compares to C30 full-matrix bisect.",
        "alpha_def_odd_only": defs,
        "curve_N6": curve,
        "suggested_questions_for_other_agents": [
            "Does alpha_def(N) converge as N→∞, and to what?",
            "Is the odd-block ground state Rayleigh a monotone function of alpha on (α_def, α*)?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp34.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp34.txt").write_text(json_dumps(defs, indent=2) + "\n")
    print("wrote", OUT / "comp34.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
