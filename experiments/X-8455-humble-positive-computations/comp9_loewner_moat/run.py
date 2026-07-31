#!/usr/bin/env python3
"""C9 — Loewner spectral moat, coefficient energy, and cross-links.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Objects not usually put on one row:
  - Sturm deficit
  - float Loewner inertia
  - spectral moat = min |eig| over nonzero eigenvalues
  - coefficient L2 energy and tail energy
  - sampled/windowed cosine similarity
  - dynamic range log10(max|p|/min|p|)

Looking for a scalar that predicts the pass/fail jump better than alpha alone.
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Xi, Fwin, Phi  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 50
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def to_frac(x, d=28) -> F:
    return F(nstr(x, d, strip_zeros=False))


def loewner_eigs(P, nodes):
    Pd = sp.diff(P.as_expr(), P.gen)
    Pdd = sp.diff(Pd, P.gen)
    bvals, avals = [], []
    for lam in nodes:
        Pi = complex(P.as_expr().subs(P.gen, lam))
        if abs(Pi) < 1e-30:
            return None
        Pdi = complex(Pd.subs(P.gen, lam))
        Pddi = complex(Pdd.subs(P.gen, lam))
        bvals.append(-Pdi / Pi)
        avals.append((Pdi * Pdi - Pi * Pddi) / (Pi * Pi))
    n = len(nodes)
    Q = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                Q[i, j] = float(np.real(avals[i]))
            else:
                Q[i, j] = float(np.real((bvals[i] - bvals[j]) / (nodes[i] - nodes[j])))
    ew = np.linalg.eigvalsh(0.5 * (Q + Q.T))
    return ew


def analyze(alpha, N, kind):
    nodes = list(range(-N, N + 1))
    if kind == "windowed":
        vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
    else:
        vals = [((-1) ** j) * Xi(2 * pi * mpf(alpha) * j) for j in nodes]
    absv = np.array([abs(float(v)) for v in vals])
    # also need the other kind for cosine similarity
    other = (
        [((-1) ** j) * Xi(2 * pi * mpf(alpha) * j) for j in nodes]
        if kind == "windowed"
        else [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
    )
    a = np.array([float(v) for v in vals])
    b = np.array([float(v) for v in other])
    cosim = float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-30))

    s = sp.symbols("s")
    pfrac = [to_frac(v) for v in vals]
    P = sp.Integer(0)
    for i, lam in enumerate(nodes):
        term = sp.Integer(1)
        for mu in nodes:
            if mu != lam:
                term *= mu - s
        P += sp.Rational(pfrac[i]) * term
    P = sp.Poly(sp.expand(P), s)
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    nre = int(sp.Poly(P.quo(g), s).count_roots())
    ew = loewner_eigs(P, nodes)
    if ew is None:
        moat = None
        inertia = None
    else:
        nz = ew[np.abs(ew) > 1e-10]
        moat = float(np.min(np.abs(nz))) if len(nz) else 0.0
        inertia = [int(np.sum(ew > 1e-10)), int(np.sum(ew < -1e-10)), int(np.sum(np.abs(ew) <= 1e-10))]

    # energies
    mid = len(absv) // 2
    core = absv[mid - min(2, mid) : mid + min(2, mid) + 1]
    tails = np.concatenate([absv[:2], absv[-2:]])
    return {
        "alpha": alpha,
        "N": N,
        "kind": kind,
        "deficit": deg - nre,
        "n_real": nre,
        "loewner_inertia_float": inertia,
        "loewner_moat": moat,
        "neg_eig_sum": float(np.sum(ew[ew < 0])) if ew is not None else None,
        "energy_l2": float(np.linalg.norm(a)),
        "tail_over_core_energy": float(np.linalg.norm(tails) / (np.linalg.norm(core) + 1e-30)),
        "dynamic_range_log10": float(np.log10((absv.max() + 1e-30) / (absv.min() + 1e-30))),
        "cosim_with_other_kind": cosim,
    }


def main():
    print("=== C9 Loewner moat / energy cross-links ===", flush=True)
    rows = []
    for N in (4, 6):
        for alpha in [1.2, 1.1, 1.05, 1.02, 1.0, 0.98, 0.96, 0.94, 0.9, 0.8]:
            for kind in ("windowed", "sampled"):
                row = analyze(alpha, N, kind)
                rows.append(row)
                print(
                    f"{kind:8} a={alpha} N={N} def={row['deficit']} moat={row['loewner_moat']} "
                    f"cosim={row['cosim_with_other_kind']:.4f} dyn={row['dynamic_range_log10']:.2f}",
                    flush=True,
                )

    # simple predictors: among windowed rows, which scalar best separates deficit 0 vs >0?
    win = [r for r in rows if r["kind"] == "windowed" and r["loewner_moat"] is not None]
    sep = {}
    for key in ("loewner_moat", "cosim_with_other_kind", "dynamic_range_log10", "tail_over_core_energy", "energy_l2", "neg_eig_sum"):
        pos = [r[key] for r in win if r["deficit"] == 0]
        neg = [r[key] for r in win if r["deficit"] > 0]
        if not pos or not neg:
            continue
        # Fisher-ish separation
        mu0, mu1 = float(np.mean(pos)), float(np.mean(neg))
        s0, s1 = float(np.std(pos) + 1e-12), float(np.std(neg) + 1e-12)
        sep[key] = {
            "mean_pass": mu0,
            "mean_fail": mu1,
            "fisher_like": abs(mu0 - mu1) / (s0 + s1),
            "pass_range": [float(min(pos)), float(max(pos))],
            "fail_range": [float(min(neg)), float(max(neg))],
        }

    payload = {
        "schema": "riemann.x8455.comp9.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float Loewner moats and energies only. Separation scores are descriptive.",
        "rows": rows,
        "windowed_separator_scores": sep,
        "suggested_questions_for_other_agents": [
            "Is loewner_moat the best separator, or is cosim_with_sampled sharper near the jump?",
            "Does neg_eig_sum ≈ -constant on all deficit-4 windowed fails?",
            "Can dynamic_range_log10 explain sampled failures where windowed still passes?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp9.json").write_text(text)
    (OUT / "comp9.txt").write_text(
        "C9 provisional\n" + "\n".join(f"{k}: {v}" for k, v in sep.items()) + "\n"
    )
    print("separators", sep, flush=True)
    print("wrote", OUT / "comp9.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
