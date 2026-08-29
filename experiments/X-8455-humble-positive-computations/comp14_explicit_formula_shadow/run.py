#!/usr/bin/env python3
"""C14 — how much of the windowed Φ coefficients is a low-zero shadow?

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY / speculative

Build a crude explicit-formula-style surrogate for the cosine transform of Φ
using only the first M zeta zeros (plus a trivial archimedean-ish constant),
then ask whether the α≈0.99 sign precursor is already present in that surrogate.

If yes, the precursor is spectral/zero-driven even before full Φ is used.
If no, the precursor needs the full θ-series / archimedean shape.
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi, nstr, cos, exp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi, gammas  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 40
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def to_frac(x, d=24) -> F:
    return F(nstr(x, d, strip_zeros=False))


def sign_and_deficit(vals, N):
    p = [to_frac(v) for v in vals]
    sc = sum(1 for a, b in zip(p, p[1:]) if a * b < 0)
    s = sp.symbols("s")
    nodes = list(range(-N, N + 1))
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
    return deg - nre, sc, "".join("+" if v > 0 else "-" for v in p)


def zero_shadow_coeff(alpha, j, gammas_list, amps, phase0=0.0):
    """Toy: p_j ~ (-1)^j * sum_k amp_k cos(γ_k * (j*alpha?) + phase).

    We do not claim this is the correct Guinand–Weil kernel. It is a probe of
    whether a low-zero cosine sum can reproduce the sign cascade.
    Coordinate guess: sample abscissa w_j = 2π j, with scale alpha in window.
    Try w = 2π alpha j as in sampled Ξ.
    """
    w = 2 * pi * mpf(alpha) * j
    s = mpf(0)
    for g, a in zip(gammas_list, amps):
        s += mpf(a) * cos(mpf(g) * w + phase0)
    return ((-1) ** j) * s


def main():
    print("=== C14 explicit-formula shadow probe ===", flush=True)
    gs = [float(g) for g in gammas(30)]
    # amplitudes ~ 1/gamma^2 and ~ exp(-c gamma)
    amps_inv = [1.0 / (g * g) for g in gs]
    amps_exp = [float(exp(-0.15 * g)) for g in gs]

    rows = []
    for N in (4, 6):
        for alpha in [1.02, 1.00, 0.99, 0.98, 0.97, 0.96, 0.94]:
            # true Phi window
            true_vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in range(-N, N + 1)]
            d0, sc0, s0 = sign_and_deficit(true_vals, N)
            for M in (1, 2, 5, 10, 30):
                for law, amps in (("inv2", amps_inv), ("exp", amps_exp)):
                    for phase0, pname in ((0.0, "ph0"), (3.0, "ph3")):
                        vals = [
                            zero_shadow_coeff(alpha, j, gs[:M], amps[:M], phase0=phase0)
                            for j in range(-N, N + 1)
                        ]
                        # avoid all-zero
                        if all(abs(float(v)) < 1e-30 for v in vals):
                            continue
                        d, sc, sgn = sign_and_deficit(vals, N)
                        # cosine similarity with true (without (-1)^j already in both)
                        a = np.array([float(v) for v in true_vals])
                        b = np.array([float(v) for v in vals])
                        cosim = float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-30))
                        rows.append(
                            {
                                "alpha": alpha,
                                "N": N,
                                "M": M,
                                "law": law,
                                "phase": pname,
                                "shadow_deficit": d,
                                "shadow_sign_changes": sc,
                                "true_deficit": d0,
                                "true_sign_changes": sc0,
                                "cosim_with_true": cosim,
                                "sign_match": sgn == s0,
                            }
                        )
            print(f"N={N} a={alpha}: true def={d0} sc={sc0}", flush=True)

    # Does any shadow family show precursor sc jump at 0.99 with deficit later?
    families = {}
    for r in rows:
        key = (r["N"], r["M"], r["law"], r["phase"])
        families.setdefault(key, []).append(r)
    cascade_hits = []
    for key, lst in families.items():
        lst = sorted(lst, key=lambda r: -r["alpha"])
        sc0, d0 = lst[0]["shadow_sign_changes"], lst[0]["shadow_deficit"]
        sc_jump = def_jump = None
        for r in lst[1:]:
            if sc_jump is None and r["shadow_sign_changes"] != sc0:
                sc_jump = r["alpha"]
            if def_jump is None and r["shadow_deficit"] != d0:
                def_jump = r["alpha"]
        if sc_jump is not None and def_jump is not None and sc_jump > def_jump:
            cascade_hits.append(
                {
                    "N": key[0],
                    "M": key[1],
                    "law": key[2],
                    "phase": key[3],
                    "sign_jump": sc_jump,
                    "deficit_jump": def_jump,
                }
            )

    payload = {
        "schema": "riemann.x8455.comp14.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "The zero-shadow model is intentionally crude and may be the wrong kernel. "
            "A negative result here does not refute an explicit-formula explanation; "
            "a positive hit is only a scheduling clue."
        ),
        "rows": rows,
        "cascade_hits": cascade_hits,
        "suggested_questions_for_other_agents": [
            "Which Guinand–Weil / Weil explicit test-function kernel matches windowed Φ coefficients?",
            "Can a correct archimedean term alone produce the 0.99 sign precursor without zeros?",
            "Do cascade_hits cluster at small M (first zero dominates) or need many zeros?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp14.json").write_text(text)
    (OUT / "comp14.txt").write_text(
        "C14\n"
        + f"n_rows={len(rows)}\n"
        + f"cascade_hits={len(cascade_hits)}\n"
        + json_dumps(cascade_hits[:20], indent=2)
        + "\n"
    )
    print("cascade_hits", len(cascade_hits), cascade_hits[:10], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
