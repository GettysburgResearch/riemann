#!/usr/bin/env python3
"""C1 — provisional windowed vs sampled target tables + Reading-B-style probes.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY only.

Intent:
  Produce a small digestible table comparing
    (A) sampled coefficients  p_j ~ (-1)^j Xi(2 pi alpha j)
    (B) hard-window Fourier coefficients of Polya's Phi
  and then probe, on tiny exact models, whether a one-scalar arithmetic gate
  can fail while a free/canonical completion succeeds.

Nothing here certifies a production Weil matrix, and nothing here proves or
disproves RH. Earlier repository censuses mixed these targets; this script
keeps them side by side so another agent can see the mismatch cheaply.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi, zeta, gamma, exp, cos, quad, zetazero, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from linalg_q import inertia_ldl, mat_add, quadratic  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 80
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def xi_half(s):
    return mpf("0.5") * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def Xi(z):
    return (xi_half(mpf("0.5") + 1j * mpf(z))).real


def Phi(t):
    t = abs(mpf(t))
    tot = mpf(0)
    for n in range(1, 60):
        en = exp(2 * t)
        term = (4 * pi**2 * n**4 * exp(mpf("4.5") * t) - 6 * pi * n**2 * exp(mpf("2.5") * t)) * exp(
            -pi * n**2 * en
        )
        tot += term
        if n > 4 and abs(term) < mpf("1e-50") * max(abs(tot), mpf(1)):
            break
    return tot


def Fwin(alpha, j):
    T = mpf(1) / (2 * mpf(alpha))
    return 2 * quad(lambda t: Phi(t) * cos(2 * pi * mpf(alpha) * j * t), [0, T])


def to_frac(x, digits=50) -> F:
    return F(nstr(x, digits, strip_zeros=False))


def interpolation_poly(nodes, pvals, s):
    P = sp.Integer(0)
    for i, (lam, pi_) in enumerate(zip(nodes, pvals)):
        term = sp.Integer(1)
        for j, mu in enumerate(nodes):
            if i != j:
                term *= mu - s
        P += sp.Rational(pi_) * term
    return sp.Poly(sp.expand(P), s)


def count_real_roots(P):
    deg = int(P.degree())
    g = sp.gcd(P, P.diff())
    sqfree = sp.Poly(P.quo(g), P.gen)
    return deg, int(sqfree.count_roots()), int(sp.Poly(g, P.gen).degree())


def loewner_from_poly(P, nodes):
    """Canonical Loewner of g=-P'/P at integer/rational nodes (exact Fraction)."""
    co = [F(int(c.p), int(c.q)) for c in P.all_coeffs()]  # descending

    def ev(cs, x):
        r = F(0)
        for c in cs:
            r = r * x + c
        return r

    d1 = [co[i] * (len(co) - 1 - i) for i in range(len(co) - 1)]
    d2 = [d1[i] * (len(d1) - 1 - i) for i in range(len(d1) - 1)]
    b, a = {}, {}
    for lam in nodes:
        Pi = ev(co, F(lam))
        if Pi == 0:
            raise ZeroDivisionError(f"P vanishes at node {lam}; Loewner undefined in this form")
        Pdi = ev(d1, F(lam))
        Pddi = ev(d2, F(lam))
        b[lam] = -Pdi / Pi
        a[lam] = (Pdi * Pdi - Pi * Pddi) / (Pi * Pi)
    Q = [[(a[i] if i == j else (b[i] - b[j]) / F(i - j)) for j in nodes] for i in nodes]
    return Q, b, a


def loewner_inertia_float(P, nodes):
    """Discovery-only Loewner inertia via float64 eigh. Not a certificate."""
    xs = sp.symbols("x")
    Pd = sp.diff(P.as_expr(), P.gen)
    Pdd = sp.diff(Pd, P.gen)
    bvals = []
    avals = []
    for lam in nodes:
        Pi = complex(P.as_expr().subs(P.gen, lam))
        if abs(Pi) < 1e-30:
            return {"error": f"near-zero P at node {lam}"}
        Pdi = complex(Pd.subs(P.gen, lam))
        Pddi = complex(Pdd.subs(P.gen, lam))
        bvals.append(-Pdi / Pi)
        avals.append((Pdi * Pdi - Pi * Pddi) / (Pi * Pi))
    n = len(nodes)
    Q = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i == j:
                Q[i, j] = float(np.real(avals[i]))
            else:
                Q[i, j] = float(np.real((bvals[i] - bvals[j]) / (nodes[i] - nodes[j])))
    ew = np.linalg.eigvalsh(0.5 * (Q + Q.T))
    pos = int(np.sum(ew > 1e-10))
    neg = int(np.sum(ew < -1e-10))
    zero = n - pos - neg
    return {"inertia_float": [pos, neg, zero], "eigs_head": [float(v) for v in ew[:3]], "eigs_tail": [float(v) for v in ew[-3:]]}


def Bp_matrix(p):
    """B_p = diag(1/p_i) - ee^T for eta=all-ones (working-note form)."""
    n = len(p)
    return [[(F(1) / p[i] if i == j else F(0)) - F(1) for j in range(n)] for i in range(n)]


def Ap_from_Q(Q, p):
    n = len(p)
    Qp = [sum(Q[i][j] * p[j] for j in range(n)) for i in range(n)]
    return [[Q[i][j] - (Qp[i] / p[i] if i == j else F(0)) for j in range(n)] for i in range(n)]


def isotropic_signs(B, p, trials=40):
    """Probe random rational directions in p^perp for signs of x^T B x.

    Returns counts of positive / negative / near-zero quadratic forms.
    Purely heuristic discovery arithmetic.
    """
    import random

    random.seed(8455)
    n = len(p)
    pos = neg = zeroish = 0
    samples = []
    for _ in range(trials):
        x = [F(random.randint(-5, 5)) for _ in range(n)]
        # project away from p in the Euclidean sense over Q by subtracting mean weighted? 
        # Exact: choose free coords then set last to enforce x·p = 0 if p_last != 0
        if p[-1] == 0:
            continue
        dot = sum(x[i] * p[i] for i in range(n - 1))
        x[-1] = -dot / p[-1]
        if all(v == 0 for v in x):
            continue
        q = quadratic(B, x)
        if q > 0:
            pos += 1
        elif q < 0:
            neg += 1
        else:
            zeroish += 1
        if len(samples) < 6:
            samples.append({"x": [str(v) for v in x], "xBx": str(q)})
    return {"pos": pos, "neg": neg, "zeroish": zeroish, "samples": samples}


def scalar_gate_probe(Q, p):
    """Heuristic: search a few rational c for PSD of U^T (A+cB) U on p^perp.

    Uses LDL inertia on the full T(c) and checks kernel dimension via inertia zeros.
    This is a coarse screen, not L-15109 threshold arithmetic.
    """
    A = Ap_from_Q(Q, p)
    B = Bp_matrix(p)
    candidates = [F(k, 2) for k in range(-40, 41)]
    feasible = []
    for c in candidates:
        T = mat_add(A, B, c)
        ine = inertia_ldl(T)
        # hope: (n-1, 0, 1) for corank-one PSD
        if ine[1] == 0 and ine[2] >= 1:
            feasible.append({"c": str(c), "inertia": list(ine)})
            if len(feasible) >= 5:
                break
    return {
        "B_inertia": list(inertia_ldl(B)),
        "A_inertia": list(inertia_ldl(A)),
        "isotropic_B": isotropic_signs(B, p),
        "feasible_c_found": feasible,
        "note": "coarse rational c-screen only; absence of a hit is not a proof of infeasibility",
    }


def target_table():
    rows = []
    s = sp.symbols("s")
    # Scaled from smoke tests (~0.07s/Fwin coeff; Sturm negligible at N<=8).
    # Small-scale first confirmed sampled vs windowed can disagree at alpha=1,N=4.
    grid = [
        (1.2, 4), (1.1, 4), (1.0, 4), (0.95, 4), (0.9, 4), (0.8, 4),
        (1.1, 6), (1.0, 6), (0.9, 6), (0.8, 6), (0.7, 6),
        (1.0, 8), (0.9, 8), (0.8, 8),
    ]
    for alpha, N in grid:
        nodes = list(range(-N, N + 1))
        sampled = [((-1) ** j) * Xi(2 * pi * mpf(alpha) * j) for j in nodes]
        windowed = [((-1) ** j) * Fwin(alpha, j) for j in nodes]
        # relative tail mismatch
        abs_samp = [abs(v) for v in sampled]
        abs_win = [abs(v) for v in windowed]
        ratios = []
        for a, b in zip(abs_samp, abs_win):
            if b > mpf("1e-40"):
                ratios.append(float(a / b))
            else:
                ratios.append(None)
        # deficits via rationalized polys; Loewner inertia is float discovery only
        # (exact LDL on 45-digit Fractions was too slow in the smoke→scale step).
        def deficit(vals):
            digits = 35 if N <= 6 else 28
            pfrac = [to_frac(v, digits) for v in vals]
            P = interpolation_poly(nodes, pfrac, s)
            deg, nre, mult = count_real_roots(P)
            try:
                ine = loewner_inertia_float(P, nodes)
            except Exception as exc:  # noqa: BLE001
                ine = {"error": str(exc)}
            return {
                "deg": deg,
                "n_real": nre,
                "deficit": deg - nre,
                "gcd_deg": mult,
                "loewner": ine,
            }

        row = {
            "alpha": alpha,
            "N": N,
            "T_halfwidth": float(1 / (2 * alpha)),
            "sampled": deficit(sampled),
            "windowed": deficit(windowed),
            "abs_ratio_sampled_over_windowed": ratios,
            "max_abs_sampled": float(max(abs_samp)),
            "max_abs_windowed": float(max(abs_win)),
            "min_abs_sampled_tail": float(min(abs_samp[0], abs_samp[-1])),
            "min_abs_windowed_tail": float(min(abs_win[0], abs_win[-1])),
        }
        rows.append(row)
        print(
            f"alpha={alpha} N={N}: sampled deficit={row['sampled']['deficit']} "
            f"windowed deficit={row['windowed']['deficit']} "
            f"tail|samp|/|win|~{ratios[0]}",
            flush=True,
        )
    return rows


def reading_b_tiny_models():
    """Exact tiny models that may inspire a lemma about scalar vs free completion."""
    s = sp.symbols("s")
    models = []

    # Model R15103-style: real-rooted but scalar-infeasible with Q=0
    nodes = [F(0), F(1), F(2), F(3)]
    p = [F(5, 64), F(-9, 64), F(35, 64), F(33, 64)]
    P = interpolation_poly(nodes, p, s)
    deg, nre, _ = count_real_roots(P)
    Q0 = [[F(0) for _ in nodes] for _ in nodes]
    probe0 = scalar_gate_probe(Q0, p)
    Qcan, _, _ = loewner_from_poly(P, nodes)
    probe_can = scalar_gate_probe(Qcan, p)
    models.append(
        {
            "name": "R15103-style-mixed-sign-realrooted",
            "nodes": [str(x) for x in nodes],
            "p": [str(x) for x in p],
            "deg": deg,
            "n_real": nre,
            "with_Q_zero": probe0,
            "with_canonical_Loewner_as_Q": probe_can,
            "commentary": (
                "Expected: free/canonical completion looks healthy while Q=0 scalar line "
                "struggles. Useful as a reminder that Reading A ≠ Reading B."
            ),
        }
    )

    # Zero-matched tiny N=2 only (N=3 with 40-digit Fractions made exact LDL too slow
    # in the hour-budget run). This remains a toy Reading-B screen.
    N = 2
    nodes_z = [F(j) for j in range(-N, N + 1)]
    gam = [mp.im(zetazero(k)) for k in range(1, N + 1)]
    roots = []
    for g in gam:
        r = to_frac(g / (2 * pi), 20)
        roots.extend([r, -r])
    Pt = sp.Poly(sp.expand(sp.prod([(s - sp.Rational(r)) for r in roots])), s)
    xis = []
    for lam in nodes_z:
        num = F(Pt.eval(lam))
        den = F(1)
        for mu in nodes_z:
            if mu != lam:
                den *= mu - lam
        xis.append(num / den)
    ssum = sum(xis)
    p_z = [v / ssum for v in xis]
    Pz = interpolation_poly(nodes_z, p_z, s)
    degz, nrez, _ = count_real_roots(Pz)
    Qz0 = [[F(0) for _ in nodes_z] for _ in nodes_z]
    # Skip exact canonical Loewner LDL here; report float inertia instead.
    loew_f = loewner_inertia_float(Pz, [int(x) for x in nodes_z])
    models.append(
        {
            "name": "zero-matched-N2-normalized",
            "nodes": [str(x) for x in nodes_z],
            "p": [str(x) for x in p_z],
            "deg": degz,
            "n_real": nrez,
            "with_Q_zero": scalar_gate_probe(Qz0, p_z),
            "canonical_loewner_float": loew_f,
            "commentary": (
                "Zero-matched targets force Reading A. Putting Q=0 asks whether the "
                "arithmetic-null source still admits a scalar completion. A negative "
                "screen here would only suggest that Weil arithmetic must enter through "
                "a nontrivial beta, not that RH fails. Kept at N=2 after N=3 exact LDL "
                "proved too slow for this session."
            ),
        }
    )

    # One-signed positive target: cone should collapse (vacuous gate)
    nodes_pos = [F(-1), F(0), F(1)]
    p_pos = [F(1, 10), F(8, 10), F(1, 10)]
    Ppos = interpolation_poly(nodes_pos, p_pos, s)
    degp, nrep, _ = count_real_roots(Ppos)
    models.append(
        {
            "name": "one-signed-positive-vacuous",
            "nodes": [str(x) for x in nodes_pos],
            "p": [str(x) for x in p_pos],
            "deg": degp,
            "n_real": nrep,
            "with_Q_zero": scalar_gate_probe([[F(0)] * 3 for _ in range(3)], p_pos),
            "commentary": (
                "Trap check: one-signed p makes B_p PSD on p^perp, so the isotropic cone "
                "is empty and every special Q is 'feasible'. Useful as a negative control."
            ),
        }
    )
    return models


def main():
    print("=== C1 target comparison (provisional) ===")
    table = target_table()
    print("=== C1 Reading-B tiny models (provisional) ===")
    models = reading_b_tiny_models()
    for m in models:
        print(
            f"{m['name']}: deg={m['deg']} n_real={m['n_real']} "
            f"Q0_feasible_hits={len(m.get('with_Q_zero', {}).get('feasible_c_found', []))} "
            f"B_inertia={m.get('with_Q_zero', {}).get('B_inertia')}"
        )

    payload = {
        "schema": "riemann.x8455.comp1.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": (
            "Not a certificate. Windowed integrals use mpmath.quad; sampled Xi uses "
            "mpmath zeta/gamma. Rationalization truncates. Do not cite as a method closure."
        ),
        "target_comparison": table,
        "reading_b_tiny_models": models,
        "suggested_questions_for_other_agents": [
            "Is there a uniform lower bound on |p_j^windowed - p_j^sampled| in the outer third of the band?",
            "For zero-matched p, which arithmetic beta (if any) makes the scalar line meet the canonical Loewner cone?",
            "Can one prove that mixed-sign B_p isotropic cones are nonempty whenever #negative p-entries >= 2?",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(text.encode()).hexdigest()
    payload["content_sha256"] = digest
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    (OUT / "comp1.json").write_text(text)
    (OUT / "comp1.txt").write_text(
        "C1 provisional summary\n"
        + "\n".join(
            f"alpha={r['alpha']} N={r['N']}: sampled_def={r['sampled']['deficit']} "
            f"windowed_def={r['windowed']['deficit']}"
            for r in table
        )
        + "\n"
        + "\n".join(
            f"model={m['name']} n_real={m['n_real']} "
            f"Q0_hits={len(m.get('with_Q_zero', {}).get('feasible_c_found', []))}"
            for m in models
        )
        + f"\nsha256={digest}\n"
    )
    print(f"wrote {OUT/'comp1.json'} sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
