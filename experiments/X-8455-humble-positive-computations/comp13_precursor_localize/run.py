#!/usr/bin/env python3
"""C13 — localize the α≈0.99 sign-change precursor; track Loewner negatives.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Questions:
  1) Which adjacent pairs flip at the precursor?
  2) Does Loewner neg_eig_sum appear at the sign jump (0.99) or only at the deficit jump (0.97)?
  3) Do Fejer-tapered windows preserve the two-step cascade?
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi, nstr, exp, cos, quad

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Phi, Fwin  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 45
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def to_frac(x, d=26) -> F:
    return F(nstr(x, d, strip_zeros=False))


def Fwin_fejer(alpha, j):
    """Fejer taper on the hard window: (1-|t|/T)_+ weight."""
    T = mpf(1) / (2 * mpf(alpha))

    def kern(t):
        t = mpf(t)
        w = 1 - abs(t) / T
        if w <= 0:
            return mpf(0)
        return w * Phi(t)

    return 2 * quad(lambda t: kern(t) * cos(2 * pi * mpf(alpha) * j * t), [0, T])


def analyze(alpha, N, maker):
    nodes = list(range(-N, N + 1))
    vals = [((-1) ** j) * maker(alpha, j) for j in nodes]
    p = [to_frac(v) for v in vals]
    signs = ["+" if v > 0 else "-" if v < 0 else "0" for v in p]
    flips = []
    for i in range(len(p) - 1):
        if p[i] * p[i + 1] < 0:
            flips.append({"left_node": nodes[i], "right_node": nodes[i + 1]})
    sc = len(flips)
    # poly / deficit / loewner
    s = sp.symbols("s")
    P = sp.Integer(0)
    for i, lam in enumerate(nodes):
        term = sp.Integer(1)
        for mu in nodes:
            if mu != lam:
                term *= mu - s
        P += sp.Rational(p[i]) * term
    P = sp.Poly(sp.expand(P), s)
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    nre = int(sp.Poly(P.quo(g), s).count_roots())
    # float Loewner eigs
    Pd = sp.diff(P.as_expr(), P.gen)
    Pdd = sp.diff(Pd, P.gen)
    bvals, avals = [], []
    ok = True
    for lam in nodes:
        Pi = complex(P.as_expr().subs(P.gen, lam))
        if abs(Pi) < 1e-30:
            ok = False
            break
        Pdi = complex(Pd.subs(P.gen, lam))
        Pddi = complex(Pdd.subs(P.gen, lam))
        bvals.append(-Pdi / Pi)
        avals.append((Pdi * Pdi - Pi * Pddi) / (Pi * Pi))
    if ok:
        Q = np.zeros((len(nodes), len(nodes)))
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i == j:
                    Q[i, j] = float(np.real(avals[i]))
                else:
                    Q[i, j] = float(np.real((bvals[i] - bvals[j]) / (nodes[i] - nodes[j])))
        ew = np.linalg.eigvalsh(0.5 * (Q + Q.T))
        neg_sum = float(np.sum(ew[ew < -1e-12]))
        n_neg = int(np.sum(ew < -1e-12))
    else:
        neg_sum, n_neg, ew = None, None, None
    return {
        "alpha": alpha,
        "N": N,
        "deficit": deg - nre,
        "sign_changes": sc,
        "flip_edges": flips,
        "sign_pattern": "".join(signs),
        "loewner_n_neg": n_neg,
        "loewner_neg_sum": neg_sum,
    }


def main():
    print("=== C13 precursor localization ===", flush=True)
    rows = []
    for kind, maker in (("hard", lambda a, j: Fwin(a, j, Phi)), ("fejer", Fwin_fejer)):
        for N in (4, 6):
            for alpha in [1.02, 1.00, 0.995, 0.99, 0.985, 0.98, 0.975, 0.97, 0.965, 0.96]:
                row = analyze(alpha, N, maker)
                row["window"] = kind
                rows.append(row)
                print(
                    f"{kind:5} N={N} a={alpha}: def={row['deficit']} sc={row['sign_changes']} "
                    f"nneg={row['loewner_n_neg']} flips={[ (f['left_node'],f['right_node']) for f in row['flip_edges'] ]}",
                    flush=True,
                )

    # cascade summary
    summary = {}
    for kind in ("hard", "fejer"):
        summary[kind] = {}
        for N in (4, 6):
            sub = [r for r in rows if r["window"] == kind and r["N"] == N]
            # assume alpha decreasing
            sc0, d0, nn0 = sub[0]["sign_changes"], sub[0]["deficit"], sub[0]["loewner_n_neg"]
            jumps = {"sign": None, "deficit": None, "loewner_neg": None}
            for r in sub[1:]:
                if jumps["sign"] is None and r["sign_changes"] != sc0:
                    jumps["sign"] = r["alpha"]
                if jumps["deficit"] is None and r["deficit"] != d0:
                    jumps["deficit"] = r["alpha"]
                if jumps["loewner_neg"] is None and (r["loewner_n_neg"] or 0) != (nn0 or 0):
                    jumps["loewner_neg"] = r["alpha"]
            summary[kind][str(N)] = jumps

    payload = {
        "schema": "riemann.x8455.comp13.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float Loewner; Fejer via mpmath.quad. Cascade alphas are grid-limited.",
        "rows": rows,
        "cascade_jumps": summary,
        "suggested_questions_for_other_agents": [
            "Are the precursor flip edges always the outermost ones, or near zero?",
            "Does Fejer destroy the precursor gap between sign jump and deficit jump?",
            "Is loewner_n_neg synchronized with deficit, not with sign_changes?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp13.json").write_text(text)
    (OUT / "comp13.txt").write_text("C13\n" + json_dumps(summary, indent=2) + "\n")
    print("cascade", summary, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
