#!/usr/bin/env python3
"""D5 — float L-15124-style root displacement / soft-mode localization.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY / not directed

Near α_def, isolate real finite roots u_k of P, pair with r_k = γ_k / h
where h = 2π α in the hard-window node scaling? 

For the hard-window cosine lattice used here, the node coordinate is already
the integer index j, and the Xi frequency identification used in L-15124 is
for a different CCM length L. This recon uses the natural pairing:

  r_k^{line} := γ_k / (2π α)     # so that cos(2π α · r · t) ~ cos(γ t) phase

and records δ_k = |u_k - r_k^{line}| for the real roots u_k of P near the
collision, plus which soft Loewner mode sits nearest the colliding ±r.
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, nstr, pi

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi, gammas  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def pack(alpha, N):
    nodes = list(range(-N, N + 1))
    pvals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
    pf = [F(nstr(v, 24, strip_zeros=False)) for v in pvals]
    s = sp.symbols("s")
    P = 0
    for i, lam in enumerate(nodes):
        term = 1
        for mu in nodes:
            if mu != lam:
                term *= mu - s
        P += sp.Rational(pf[i]) * term
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
    return nodes, np.array([float(v) for v in pvals]), 0.5 * (Q + Q.T), P


def main():
    print("=== D5 root-displacement / soft localization recon ===", flush=True)
    gs = [float(g) for g in gammas(40)]
    rows = []
    for N in (6, 8, 10):
        for alpha in (0.978, 0.9765, 0.9758, 0.9752, 0.9745):
            nodes, p, Q, P = pack(alpha, N)
            coeffs = [float(c) for c in P.all_coeffs()]
            rts = np.roots(coeffs)
            u_real = sorted(
                [float(z.real) for z in rts if abs(z.imag) < 1e-5 and abs(z.real) > 0.2],
                key=lambda x: abs(x),
            )
            # line-node coordinates
            h = 2 * np.pi * alpha
            r_line = [g / h for g in gs]
            pairs = []
            used = set()
            for u in u_real:
                # nearest unused line node
                best = None
                best_d = 1e9
                for i, r in enumerate(r_line):
                    if i in used:
                        continue
                    d = abs(u - r)
                    if d < best_d:
                        best_d = d
                        best = i
                if best is None:
                    continue
                used.add(best)
                pairs.append(
                    {
                        "u": u,
                        "gamma_index": best + 1,
                        "gamma": gs[best],
                        "r_line": r_line[best],
                        "delta": best_d,
                    }
                )

            ew, ev = np.linalg.eigh(Q)
            # soft = smallest |eig| not aligning with p
            order = np.argsort(np.abs(ew))
            idx = {nodes[i]: i for i in range(len(nodes))}
            soft = None
            for k in order:
                al = abs(np.dot(ev[:, k] / (np.linalg.norm(ev[:, k]) + 1e-30), p / (np.linalg.norm(p) + 1e-30)))
                if al > 0.95 and abs(ew[k]) < 1e-9:
                    continue
                soft = {
                    "eig": float(ew[k]),
                    "align_p": float(al),
                    "mass_abs": {str(nodes[i]): float(ev[i, k] ** 2) for i in range(len(nodes))},
                }
                break

            # which |u| is closest to the collision scale ~2.18?
            collide = min(u_real, key=lambda x: abs(abs(x) - 2.18)) if u_real else None
            row = {
                "N": N,
                "alpha": float(alpha),
                "n_real_roots": len(u_real),
                "n_neg_Q": int(np.sum(ew < -1e-12)),
                "pairs_top": pairs[:8],
                "min_delta": min((p["delta"] for p in pairs), default=None),
                "collision_scale_root": collide,
                "soft": soft,
            }
            rows.append(row)
            print(
                f"N={N} a={alpha:.4f} n_real={len(u_real)} n_neg={row['n_neg_Q']} "
                f"min_delta={row['min_delta']} collide_u={collide} soft_eig={None if soft is None else soft['eig']}",
                flush=True,
            )

    payload = {
        "schema": "riemann.x8455.d5.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Float roots + heuristic gamma/(2πα) pairing. Not the directed "
            "L-15124 ledger (needs certified Xi zeros, F-enclosures, B_kl, E_k)."
        ),
        "rows": rows,
        "suggested_next": [
            "Build directed δ_k, B_kl, and the diagonal margin from L-15124 at α just above α_def.",
            "Localize soft mode to the root index whose margin → 0.",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "d5.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "d5.txt").write_text(
        "\n".join(
            f"N={r['N']} a={r['alpha']} n_real={r['n_real_roots']} n_neg={r['n_neg_Q']} "
            f"min_delta={r['min_delta']} collide={r['collision_scale_root']}"
            for r in rows
        )
        + "\n"
    )
    print("wrote", OUT / "d5.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
