#!/usr/bin/env python3
"""C8 — opposite-sign Reading-B screen + Gaussian-window control.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

1) Rebuild the X-15105-style opposite-sign isotropic probe for B_p / A_p
   instead of the weak full-matrix inertia screen used in C1.
2) Compare Phi-window vs Gaussian-window transition alphas at small N.

Invitation: if Gaussian (no zeta zeros) reproduces the Phi transition, the gate
is still mostly analytic-truncation geometry; if not, arithmetic may be leaking in.
"""

from __future__ import annotations

import hashlib
import itertools
import random
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, pi, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi, Phi_gaussian, Xi  # noqa: E402
from linalg_q import quadratic  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 45
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def to_frac(x, d=28) -> F:
    return F(nstr(x, d, strip_zeros=False))


def Bp(p):
    n = len(p)
    return [[(F(1) / p[i] if i == j else F(0)) - F(1) for j in range(n)] for i in range(n)]


def opposite_sign_screen(p, trials=200, seed=8455):
    """Search p^perp for x with x^T B x > 0 and y with y^T B y < 0.

    If both exist, the isotropic cone is nontrivial and the one-scalar family
    with Q=0 is expected to be conflicted (R-15103 style).
    """
    random.seed(seed)
    n = len(p)
    pos = []
    neg = []
    for _ in range(trials):
        x = [F(random.randint(-6, 6)) for _ in range(n)]
        if p[-1] == 0:
            continue
        dot = sum(x[i] * p[i] for i in range(n - 1))
        x[-1] = -dot / p[-1]
        if all(v == 0 for v in x):
            continue
        q = quadratic(Bp(p), x)
        if q > 0 and len(pos) < 5:
            pos.append({"x": [str(v) for v in x], "xBx": str(q)})
        if q < 0 and len(neg) < 5:
            neg.append({"x": [str(v) for v in x], "xBx": str(q)})
        if pos and neg:
            break
    return {
        "has_pos": bool(pos),
        "has_neg": bool(neg),
        "cone_nontrivial": bool(pos and neg),
        "pos_examples": pos,
        "neg_examples": neg,
        "verdict_guess": (
            "likely_scalar_conflict_for_Q0"
            if (pos and neg)
            else "cone_one_sided_or_empty_Q0_maybe_feasible"
        ),
    }


def deficit_for(vals, N):
    s = sp.symbols("s")
    nodes = list(range(-N, N + 1))
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
    return deg, nre, deg - nre, pfrac


def main():
    print("=== C8 Reading-B opposite-sign + Gaussian control ===", flush=True)
    # --- Reading B toys ---
    toys = []
    # R15103 mixed-sign
    p = [F(5, 64), F(-9, 64), F(35, 64), F(33, 64)]
    toys.append({"name": "R15103-mixed", "p": [str(x) for x in p], "screen": opposite_sign_screen(p)})
    # one-signed
    p2 = [F(1, 10), F(8, 10), F(1, 10)]
    toys.append({"name": "one-signed", "p": [str(x) for x in p2], "screen": opposite_sign_screen(p2)})
    # windowed targets near transition as p vectors (normalized)
    for alpha, N in [(1.0, 4), (0.96, 4), (0.98, 4), (1.0, 6)]:
        nodes = list(range(-N, N + 1))
        vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
        pfrac = [to_frac(v) for v in vals]
        ssum = sum(pfrac)
        pn = [v / ssum for v in pfrac]
        toys.append(
            {
                "name": f"windowed-alpha{alpha}-N{N}",
                "p": [str(x) for x in pn],
                "screen": opposite_sign_screen(pn),
            }
        )
        print(toys[-1]["name"], toys[-1]["screen"]["verdict_guess"], flush=True)

    # --- Gaussian vs Phi transition ---
    trans = []
    for N in (4, 6):
        for alpha in [1.10, 1.05, 1.00, 0.98, 0.96, 0.94, 0.90, 0.80]:
            nodes = list(range(-N, N + 1))
            phi_vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
            g_vals = [((-1) ** j) * Fwin(alpha, j, Phi_gaussian) for j in nodes]
            s_vals = [((-1) ** j) * Xi(2 * pi * mpf(alpha) * j) for j in nodes]
            dp = deficit_for(phi_vals, N)
            dg = deficit_for(g_vals, N)
            ds = deficit_for(s_vals, N)
            row = {
                "alpha": alpha,
                "N": N,
                "phi_deficit": dp[2],
                "gaussian_deficit": dg[2],
                "sampled_deficit": ds[2],
            }
            trans.append(row)
            print(row, flush=True)

    payload = {
        "schema": "riemann.x8455.comp8.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Opposite-sign screen is necessary-style evidence for Q=0 conflict, not a full "
            "L-15109 threshold certificate. Gaussian kernel is a blunt control."
        ),
        "reading_b_toys": toys,
        "gaussian_vs_phi_transition": trans,
        "suggested_questions_for_other_agents": [
            "If gaussian_deficit tracks phi_deficit across alpha, is the transition analytic rather than arithmetic?",
            "Do all mixed-sign windowed targets near alpha~1 have nontrivial B cones?",
            "Can one prove cone_nontrivial <=> n_- >= 1 and n_+ >= 2 for eta=all-ones?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp8.json").write_text(text)
    (OUT / "comp8.txt").write_text(
        "C8 provisional\n"
        + "\n".join(f"{t['name']}: {t['screen']['verdict_guess']}" for t in toys)
        + "\n"
        + "\n".join(
            f"a={r['alpha']} N={r['N']} phi={r['phi_deficit']} gauss={r['gaussian_deficit']} samp={r['sampled_deficit']}"
            for r in trans
        )
        + "\n"
    )
    print("wrote", OUT / "comp8.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
