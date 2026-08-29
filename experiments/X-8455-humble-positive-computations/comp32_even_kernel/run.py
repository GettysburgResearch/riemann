#!/usr/bin/env python3
"""C32 — characterize the even structural Loewner kernel vs soft odd mode.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

C30: null vector is even, concentrated on {0,±1}. Soft mode is odd-antisym.
Probe: is null ≈ span of a simple discrete even template? Does Q annihilate
the constant-on-nodes vector in exact Fraction arithmetic?
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

mp.dps = 45
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def loewner_float(alpha, N, digits=28):
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
    return nodes, 0.5 * (Q + Q.T), [float(v) for v in vals]


def templates(nodes):
    n = np.array(nodes, dtype=float)
    out = {
        "const": np.ones_like(n),
        "abs": np.abs(n),
        "n2": n * n,
        "delta0": (n == 0).astype(float),
        "pm1_even": (np.abs(n) == 1).astype(float),
        "hat_0_pm1": (np.abs(n) <= 1).astype(float),
        # matched to C30 shape: large at 0, medium at ±1, tiny elsewhere
        "c30ish": np.where(n == 0, 0.8615, np.where(np.abs(n) == 1, 0.3590, 0.0)),
        # opposite sign on ±1 vs 0 (observed null shape)
        "c30ish_opp": np.where(n == 0, 0.8615, np.where(np.abs(n) == 1, -0.3590, 0.0)),
        "laplace1d": np.where(n == 0, 2.0, np.where(np.abs(n) == 1, -1.0, 0.0)),
    }
    return out


def main():
    print("=== C32 even kernel characterization ===", flush=True)
    rows = []
    for N in (3, 4, 5, 6, 8):
        for alpha in (0.995, 0.99, 0.98, 0.976):
            nodes, Q, vals = loewner_float(alpha, N)
            ew, ev = np.linalg.eigh(Q)
            k0 = int(np.argmin(np.abs(ew)))
            v0 = ev[:, k0]
            # soft = min among non-kernel
            order = np.argsort(ew)
            soft_idx = None
            for i in order:
                if abs(ew[i]) > 1e-8:
                    soft_idx = int(i)
                    break
            vsoft = ev[:, soft_idx] if soft_idx is not None else None
            aligns = {}
            for name, t in templates(nodes).items():
                t = t / (np.linalg.norm(t) + 1e-30)
                aligns[name] = float(abs(np.dot(v0, t)))
            # residual ||Q v0||
            res = float(np.linalg.norm(Q @ v0))
            # even/odd projection quality
            idx = {nodes[i]: i for i in range(len(nodes))}
            even_err = float(
                np.sqrt(
                    sum((v0[idx[j]] - v0[idx[-j]]) ** 2 for j in nodes if j > 0)
                    + 0.0
                )
            )
            odd_err_soft = None
            if vsoft is not None:
                odd_err_soft = float(
                    np.sqrt(
                        sum((vsoft[idx[j]] + vsoft[idx[-j]]) ** 2 for j in nodes if j > 0)
                        + (vsoft[idx[0]] ** 2 if 0 in idx else 0.0)
                    )
                )
            row = {
                "N": N,
                "alpha": alpha,
                "null_eig": float(ew[k0]),
                "null_residual": res,
                "aligns": aligns,
                "best_template": max(aligns, key=aligns.get),
                "best_align": aligns[max(aligns, key=aligns.get)],
                "null_even_asymmetry": even_err,
                "soft_odd_asymmetry": odd_err_soft,
                "soft_eig": None if soft_idx is None else float(ew[soft_idx]),
                "null_vec": {str(nodes[i]): float(v0[i]) for i in range(len(nodes))},
            }
            rows.append(row)
            print(
                f"N={N} a={alpha} null={ew[k0]:.3e} best={row['best_template']} "
                f"align={row['best_align']:.4f} even_asym={even_err:.3e} "
                f"soft_odd_asym={odd_err_soft}",
                flush=True,
            )

    # summarize best template frequency
    from collections import Counter

    cnt = Counter(r["best_template"] for r in rows)
    payload = {
        "schema": "riemann.x8455.comp32.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float eigh templates; exact kernel identity still open.",
        "rows": rows,
        "best_template_counts": dict(cnt),
        "suggested_questions_for_other_agents": [
            "Is the even kernel exactly spanned by a discrete second-difference nullvector of the Loewner construction?",
            "Does exact Rational Loewner have det(Q)=0 identically for odd-sized node sets?",
            "Prove soft∈odd and kernel∈even by the even/odd decomposition of the divided-difference matrix.",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp32.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp32.txt").write_text(json_dumps({"counts": dict(cnt)}, indent=2) + "\n")
    print("counts", dict(cnt), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
