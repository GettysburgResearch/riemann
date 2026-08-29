#!/usr/bin/env python3
"""C30 — identify the near-null Loewner mode + fine α_def binary search.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Diagnosis from C26/C29 probe: float Loewner Q has a ~1e-14 eigenvalue
(structural?), and the soft mode is the *next* one. Schur(±1) then looks like
{≈0, ≈λ_soft}. Here: characterize the nullish vector and bisect α_def where
λ_soft crosses 0 (after filtering the structural kernel).
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


def loewner_pack(alpha, N, digits=26):
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
    ew, ev = np.linalg.eigh(Qs)
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    nre = int(sp.Poly(P.quo(g), s).count_roots())
    return nodes, Qs, ew, ev, deg - nre, float(vals[nodes.index(2)]), p


def classify_null(nodes, ew, ev):
    k0 = int(np.argmin(np.abs(ew)))
    v = ev[:, k0]
    # compare to constant / linear / quadratic discrete modes
    c = np.ones(len(nodes))
    lin = np.array(nodes, dtype=float)
    quad = lin**2
    def align(u):
        u = u / (np.linalg.norm(u) + 1e-30)
        return float(abs(np.dot(v, u)))
    return {
        "null_eig": float(ew[k0]),
        "null_vec": {str(nodes[i]): float(v[i]) for i in range(len(nodes))},
        "align_const": align(c),
        "align_linear": align(lin),
        "align_quadratic": align(quad),
        "mass_even": float(sum(v[i] ** 2 for i, j in enumerate(nodes) if j % 2 == 0)),
        "mass_odd": float(sum(v[i] ** 2 for i, j in enumerate(nodes) if j % 2 != 0)),
    }


def soft_after_kernel(ew, tol=1e-8):
    """Drop a single structural near-null, return algebraic min of the rest.

    Important: do NOT treat a soft mode that has crossed near 0 as kernel —
    only drop the eigenvalue closest to 0 when |λ|<tol.
    """
    ew = np.asarray(ew, dtype=float)
    k0 = int(np.argmin(np.abs(ew)))
    mask = np.ones(len(ew), dtype=bool)
    if abs(ew[k0]) < tol:
        mask[k0] = False
    rest = ew[mask]
    if rest.size == 0:
        return None
    return float(np.min(rest))


def main():
    print("=== C30 kernel identity + alpha_def bisect ===", flush=True)
    null_rows = []
    for N in (3, 4, 5, 6, 8):
        for alpha in (0.99, 0.98, 0.97):
            nodes, Qs, ew, ev, deficit, p2, _ = loewner_pack(alpha, N)
            info = classify_null(nodes, ew, ev)
            soft = soft_after_kernel(ew)
            row = {
                "N": N,
                "alpha": alpha,
                "deficit": deficit,
                "p2": p2,
                "soft_after_kernel": soft,
                "n_neg": int(np.sum(ew < -1e-12)),
                **info,
            }
            null_rows.append(row)
            print(
                f"N={N} a={alpha} null={info['null_eig']:.3e} "
                f"align(c,lin,quad)=({info['align_const']:.4f},{info['align_linear']:.4f},{info['align_quadratic']:.4f}) "
                f"soft={soft} def={deficit}",
                flush=True,
            )

    # fine bisect alpha_def for several N: where soft_after_kernel crosses 0.
    # Soft decreases as alpha decreases, so the pass branch is the HIGH-alpha side.
    defs = {}
    for N in (4, 5, 6, 8, 10):
        lo, hi = 0.968, 0.982  # lo = known-fail side, hi = known-pass side
        for _ in range(28):
            mid = 0.5 * (lo + hi)
            _, _, ew, _, deficit, _, _ = loewner_pack(mid, N)
            soft = soft_after_kernel(ew)
            failed = soft is None or soft < 0 or deficit > 0
            if failed:
                lo = mid  # still below the crossing; search upward
            else:
                hi = mid  # still on pass branch; search downward
        defs[str(N)] = {
            "alpha_def_lo": lo,
            "alpha_def_hi": hi,
            "alpha_def_mid": 0.5 * (lo + hi),
        }
        print("alpha_def", N, defs[str(N)], flush=True)

    payload = {
        "schema": "riemann.x8455.comp30.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Float eigh; 'null' may be a discretization/rationalization artifact.",
        "null_rows": null_rows,
        "alpha_def_bisect": defs,
        "suggested_questions_for_other_agents": [
            "Is the ~1e-14 Loewner eigenvalue exactly zero for exact Q (kernel theorem)?",
            "If the kernel is the constant mode, does Loewner live on mean-zero functions?",
            "Use Schur-antisym = 0 as a definition of α_def independent of N≥5?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp30.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp30.txt").write_text(
        json_dumps({"alpha_def_bisect": defs, "null_sample": null_rows[:5]}, indent=2) + "\n"
    )
    print("wrote", OUT / "comp30.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
