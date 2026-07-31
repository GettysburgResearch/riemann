#!/usr/bin/env python3
"""C29 — antisym odd Rayleigh / 1D reduction vs λ_soft.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C23: soft evec is antisymmetric with ~99% mass on ±1.
C25: raw ±1 principal 2×2 does not track λ_soft.
C26: Schur of ±1 — check both eigenvalues; also compare
  R_odd = v^T Q v for v = (e_1 - e_{-1})/√2
and the 1D Schur Rayleigh after eliminating Rest against that direction.
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


def analyze(nodes, Q):
    Qs = 0.5 * (Q + Q.T)
    ew, ev = np.linalg.eigh(Qs)
    pos = ew > 1e-12
    soft = float(np.min(ew[pos])) if np.any(pos) else None
    k = int(np.argmin(np.where(pos, ew, 1e99)))
    idx = {nodes[i]: i for i in range(len(nodes))}

    # fixed antisym probe on ±1
    v = np.zeros(len(nodes))
    v[idx[1]] = 1 / np.sqrt(2)
    v[idx[-1]] = -1 / np.sqrt(2)
    ray_pm1 = float(v @ Qs @ v)

    # best antisym vector in full space: restrict to odd coords with v(-j)=-v(j)
    odds = [j for j in nodes if j > 0]
    # build Q_odd_antisym: basis f_j = (e_j - e_{-j})/√2
    m = len(odds)
    B = np.zeros((len(nodes), m))
    for t, j in enumerate(odds):
        B[idx[j], t] = 1 / np.sqrt(2)
        B[idx[-j], t] = -1 / np.sqrt(2)
    Qo = B.T @ Qs @ B
    ewo = np.linalg.eigvalsh(0.5 * (Qo + Qo.T))
    soft_odd = float(np.min(ewo))

    # Schur of ±1, both eigs + projected onto antisym / sym
    o = [idx[-1], idx[1]]
    r = [i for i in range(len(nodes)) if nodes[i] not in (-1, 1)]
    Qoo = Qs[np.ix_(o, o)]
    Qor = Qs[np.ix_(o, r)]
    Qro = Qs[np.ix_(r, o)]
    Qrr = Qs[np.ix_(r, r)]
    S = Qoo - Qor @ np.linalg.solve(Qrr, Qro)
    Ss = 0.5 * (S + S.T)
    ewS = np.linalg.eigvalsh(Ss)
    # coords o = [-1, 1]; antisym u=[ -1/√2, 1/√2 ], sym u=[1/√2,1/√2]
    u_a = np.array([-1 / np.sqrt(2), 1 / np.sqrt(2)])
    u_s = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])
    schur_antisym = float(u_a @ Ss @ u_a)
    schur_sym = float(u_s @ Ss @ u_s)

    mass1 = float(ev[idx[1], k] ** 2 + ev[idx[-1], k] ** 2)
    return {
        "lambda_soft": soft,
        "rayleigh_fixed_pm1_antisym": ray_pm1,
        "ratio_ray_over_soft": None if soft in (None, 0) else ray_pm1 / soft,
        "soft_odd_subspace_min": soft_odd,
        "ratio_oddsub_over_soft": None if soft in (None, 0) else soft_odd / soft,
        "schur_pm1_eigs": [float(x) for x in ewS],
        "schur_antisym": schur_antisym,
        "schur_sym": schur_sym,
        "ratio_schur_antisym_over_soft": None if soft in (None, 0) else schur_antisym / soft,
        "soft_mass_pm1": mass1,
        "cond_Qrr": float(np.linalg.cond(Qrr)),
        "Q_min_eig": float(np.min(ew)),
        "Q_n_near0": int(np.sum(np.abs(ew) < 1e-10)),
    }


def main():
    print("=== C29 odd Rayleigh / Schur antisym ===", flush=True)
    rows = []
    for N in (4, 6, 8):
        for alpha in np.linspace(0.995, 0.976, 12):
            nodes, Q, deficit, p2 = loewner_Q(float(alpha), N)
            row = {
                "alpha": float(alpha),
                "N": N,
                "deficit": deficit,
                "p2": p2,
                **analyze(nodes, Q),
            }
            rows.append(row)
            print(
                f"N={N} a={alpha:.4f} def={deficit} soft={row['lambda_soft']} "
                f"SchurA={row['schur_antisym']:.6f} ray={row['rayleigh_fixed_pm1_antisym']:.6f} "
                f"oddsub={row['soft_odd_subspace_min']:.6f} "
                f"rSchurA={row['ratio_schur_antisym_over_soft']}",
                flush=True,
            )

    def summarize(key):
        vals = [
            r[key]
            for r in rows
            if r["deficit"] == 0 and r[key] is not None and abs(r[key]) < 1e6
        ]
        if not vals:
            return None
        return {
            "n": len(vals),
            "mean": float(np.mean(vals)),
            "std": float(np.std(vals)),
            "min": float(np.min(vals)),
            "max": float(np.max(vals)),
        }

    summary = {
        "ratio_schur_antisym": summarize("ratio_schur_antisym_over_soft"),
        "ratio_ray_pm1": summarize("ratio_ray_over_soft"),
        "ratio_oddsub": summarize("ratio_oddsub_over_soft"),
    }
    payload = {
        "schema": "riemann.x8455.comp29.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float Loewner / Schur; looking for a 1D odd reduction that tracks λ_soft.",
        "rows": rows,
        "summary_pass_branch": summary,
        "suggested_questions_for_other_agents": [
            "Does Schur-antisym / λ_soft stay ≈1 across α (exact odd reduction)?",
            "Is the complementary Schur-sym eigenvalue always near 0, and why?",
            "Can α_def be characterized as vanishing of the odd Schur Rayleigh?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp29.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp29.txt").write_text(json_dumps(summary, indent=2) + "\n")
    print("summary", summary, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
