#!/usr/bin/env python3
"""C10 — unexpected object probes.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY / deliberately odd

Three odd comparisons that are cheap and might spark a lemma:

A) Rank-one CvS perturbation spectrum: eigenvalues of D' = D - (D p) 1^T
   (non-symmetric) at high mpmath precision vs Sturm deficit.
   (Trap warning from NEGATIVE_RESULTS: float64 can invent strip zeros.)

B) Discrete Hilbert-ish adjacent phase: arg(p_{j+1}/p_j) along windowed coeffs.

C) "Prime-truncated Polya": replace Phi by its first K prime terms and watch
   whether the windowed deficit transition moves. If K=1 already locks the
   transition, arithmetic depth is shallow at this scale; if it drifts with K,
   something more interesting may be afoot.
"""

from __future__ import annotations

import hashlib
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi, exp, cos, quad, nstr, matrix, eye, eig

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi, Xi  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 60
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def to_frac(x, d=30) -> F:
    return F(nstr(x, d, strip_zeros=False))


def deficit(vals, N):
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
    return deg - nre, pfrac


def phi_truncated(t, K):
    t = abs(mpf(t))
    tot = mpf(0)
    for n in range(1, K + 1):
        en = exp(2 * t)
        tot += (4 * pi**2 * n**4 * exp(mpf("4.5") * t) - 6 * pi * n**2 * exp(mpf("2.5") * t)) * exp(
            -pi * n**2 * en
        )
    return tot


def Fwin_trunc(alpha, j, K):
    T = mpf(1) / (2 * mpf(alpha))
    return 2 * quad(lambda t: phi_truncated(t, K) * cos(2 * pi * mpf(alpha) * j * t), [0, T])


def cv_spectrum(pfrac, N):
    """Eigenvalues of non-symmetric D' = D - u 1^T with u = D p, using mpmath."""
    nodes = list(range(-N, N + 1))
    n = len(nodes)
    # Build D' explicitly
    p = [mpf(str(x)) for x in pfrac]
    D = matrix(n)
    for i, lam in enumerate(nodes):
        D[i, i] = mpf(lam)
    u = matrix([D[i, i] * p[i] for i in range(n)])
    ones = matrix([mpf(1) for _ in range(n)])
    Dp = D - u * ones.T
    # eigenvalues
    E, _ER = eig(Dp)
    ev = [E[i] for i in range(n)]
    # classify
    realish = []
    complexish = []
    for z in ev:
        if abs(z.imag) < mpf("1e-20"):
            realish.append(float(z.real))
        elif z.imag > 0:
            complexish.append((float(z.real), float(z.imag)))
    return {
        "n_realish": len(realish),
        "n_complex_pairs": len(complexish),
        "max_abs_imag": float(max([0] + [im for _, im in complexish])),
        "complex_pairs": complexish[:6],
    }


def adjacent_phase(pfrac):
    phases = []
    for a, b in zip(pfrac, pfrac[1:]):
        if a == 0 or b == 0:
            phases.append(None)
            continue
        z = complex(float(b)) / complex(float(a))
        phases.append(float(np.angle(z)))
    return phases


def main():
    print("=== C10 unexpected probes ===", flush=True)
    # A + B on a few alphas
    ab_rows = []
    for alpha, N in [(1.05, 4), (1.0, 4), (0.98, 4), (0.96, 4), (1.0, 6), (0.96, 6)]:
        nodes = list(range(-N, N + 1))
        vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
        defi, pfrac = deficit(vals, N)
        spec = cv_spectrum(pfrac, N)
        phases = adjacent_phase(pfrac)
        # compare to sampled
        svals = [((-1) ** j) * Xi(2 * pi * mpf(alpha) * j) for j in nodes]
        sdef, spfrac = deficit(svals, N)
        sspec = cv_spectrum(spfrac, N)
        row = {
            "alpha": alpha,
            "N": N,
            "windowed_deficit": defi,
            "windowed_Dp": spec,
            "windowed_adj_phase": phases,
            "sampled_deficit": sdef,
            "sampled_Dp": sspec,
            "phase_l1": float(np.sum(np.abs([p for p in phases if p is not None]))),
        }
        ab_rows.append(row)
        print(
            f"a={alpha} N={N}: win_def={defi} maxIm={spec['max_abs_imag']:.4g} "
            f"samp_def={sdef} samp_maxIm={sspec['max_abs_imag']:.4g} phaseL1={row['phase_l1']:.3f}",
            flush=True,
        )

    # C) prime-truncated Phi transition at N=4
    trunc_rows = []
    for K in (1, 2, 3, 5, 10, 20):
        for alpha in (1.05, 1.00, 0.98, 0.96, 0.94, 0.90):
            N = 4
            nodes = list(range(-N, N + 1))
            vals = [((-1) ** j) * Fwin_trunc(alpha, j, K) for j in nodes]
            defi, _ = deficit(vals, N)
            trunc_rows.append({"K": K, "alpha": alpha, "N": N, "deficit": defi})
        # summarize transition estimate: last alpha with deficit 0
        sub = [r for r in trunc_rows if r["K"] == K]
        passing = [r["alpha"] for r in sub if r["deficit"] == 0]
        failing = [r["alpha"] for r in sub if r["deficit"] > 0]
        print(
            f"K={K}: pass_alphas={passing} fail_alphas={failing}",
            flush=True,
        )

    payload = {
        "schema": "riemann.x8455.comp10.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "mpmath eig on non-symmetric D' at 60 dps; still not interval arithmetic. "
            "Prime truncation of Phi is a blunt probe of arithmetic depth."
        ),
        "cv_and_phase_rows": ab_rows,
        "prime_truncated_transition": trunc_rows,
        "suggested_questions_for_other_agents": [
            "Does max_abs_imag of D' jump in lockstep with the Sturm deficit?",
            "Is adjacent-phase L1 a cheaper predictor than building P?",
            "Why would K=1 already freeze the transition alpha, if it does?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp10.json").write_text(text)
    (OUT / "comp10.txt").write_text(
        "C10 provisional\n"
        + "\n".join(
            f"a={r['alpha']} N={r['N']} win_def={r['windowed_deficit']} maxIm={r['windowed_Dp']['max_abs_imag']}"
            for r in ab_rows
        )
        + "\n"
    )
    print("wrote", OUT / "comp10.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
