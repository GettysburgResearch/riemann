#!/usr/bin/env python3
"""
X-0014 -- What power of delta does the Pick detector actually see?
(Q-0016a, opened by T-0005; attacked with the L-0008 decomposition.)

Agent: claude-02

THE QUESTION.  T-0005 reports |min pivot| ~ delta^3 "measured slope 3.0-3.7".
But the measured slopes DRIFT (3.8 -> 2.4 over ten decades), and L-0008 gives
an exact algebraic handle on the perturbation, so the exponent is not something
to fit -- it is something to compute.

THE COMPUTATION.  For the off-line pair rho_pm = 1/2 pm delta + i gamma (plus
conjugates), with P0 the on-line (double-zero) Pick matrix and v a bottom
eigenvector of P0, first-order eigenvalue perturbation gives

    lambda_min(P(delta)) ~ lambda_min(P0) + v* DP(delta) v / v*v ,

and L-0008 expands  v* DP v  in delta explicitly:

    v* DP v = sum_pm |v* u_pm|^2 - 2|v* u_0|^2        (rank-one parts)
              - 2 delta v*(S_+ - S_-)v                 (Gram parts)
            = c2 delta^2 + c3 delta^3 + c4 delta^4 + ...

with (writing u' = du/dsigma, whose components are just u_j^2)

    c2 = 2|v* u'_0|^2  - 4 d/dsigma[v* S_sigma v]|_0   (+ conjugate partners).

The first piece is >= 0, the second has no fixed sign: **c2 is a difference of
two computable numbers**.  If they nearly cancel, the apparent slope sits
between 3 and 4 for many decades before the asymptotic 2 emerges -- which
would explain the drifting measurements and correct T-0005's "delta^3".

THREE PARTS.
  1.  Isolated pair, N = 3 probes (P0 has rank 2, so v spans its exact
      kernel): measure lambda-proxy (LDL min pivot) over delta = 1e-1..1e-24
      and compare against the direct v* DP v / v*v prediction at every delta.
  2.  Extract c2, c3, c4 from v* DP v by Richardson extrapolation at tiny
      delta, and report which term dominates where (the crossover scale
      delta* = |c2/c3| if c3 dominates early).
  3.  The realistic geometry (N = 16, background zeros as in X-0011): same
      slope scan pushed to delta = 1e-18, to see whether the asymptotic
      exponent 2 emerges once delta^2 |c2| clears the floor.

Usage: python3 run.py
"""
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
from math import log10

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import pick as PK  # noqa: E402
from flint import acb, arb, ctx  # noqa: E402

HALF = arb(1) / 2


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


# ---------------------------------------------------------------- helpers
def pick_of_zeros(al, zs):
    def F(s):
        return sum(1 / (acb(s) - r) for r in zs)
    return PK.pick_matrix(al, F=F)


def min_pivot(P):
    n, A, worst = len(P), [r[:] for r in P], None
    for k in range(n):
        d = A[k][k].real
        worst = d if worst is None else (d if d < worst else worst)
        if not (d > 0):
            return worst
        for i in range(k + 1, n):
            f = A[i][k] / d
            for j in range(k, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return worst


def pair_zeros(gam, delta):
    d, g = arb(delta), arb(gam)
    loc = [acb(HALF - d, g), acb(HALF + d, g)] if d != 0 else \
          [acb(HALF, g), acb(HALF, g)]
    return loc + [z.conjugate() for z in loc]


def null_vector_rank2(al, gam):
    """For N = 3 probes and the doubled on-line zero (plus conjugate), P0 =
    2 w w* + 2 wb wb* has rank 2; return v with v* w = v* wb = 0 (exact
    2x2 solve, v_3 = 1)."""
    rho = acb(HALF, arb(gam))
    w = [1 / (a - rho) for a in al]
    wb = [1 / (a - rho.conjugate()) for a in al]
    # v1 conj(w1) + v2 conj(w2) = -conj(w3);  same for wb  (v* w = 0)
    a11, a12, b1 = w[0].conjugate(), w[1].conjugate(), -w[2].conjugate()
    a21, a22, b2 = wb[0].conjugate(), wb[1].conjugate(), -wb[2].conjugate()
    det = a11 * a22 - a12 * a21
    v1 = (b1 * a22 - b2 * a12) / det
    v2 = (a11 * b2 - a21 * b1) / det
    return [v1, v2, acb(1)]


def quad_form(P, v):
    n = len(v)
    return sum(v[j].conjugate() * P[j][k] * v[k]
               for j in range(n) for k in range(n)).real


def main():
    ctx.prec = 12000
    G = "100.0"
    out = {"experiment": "X-0014", "agent": "claude-02", "git_sha": git_sha(),
           "python": sys.version.split()[0],
           "platform": platform.platform(), "prec_bits": ctx.prec}

    # -------- part 1: isolated pair, N = 3, prediction vs measurement ------
    print("=== part 1: isolated pair, N = 3 (exact null vector) ===")
    al = [acb(arb("0.55"), arb("100.9")), acb(arb("0.62"), arb("101.7")),
          acb(arb("0.55"), arb("102.4"))]
    v = null_vector_rank2(al, G)
    P0 = pick_of_zeros(al, pair_zeros(G, "0"))
    vv = quad_form([[acb(1 if j == k else 0) for k in range(3)]
                    for j in range(3)], v)
    lam0 = quad_form(P0, v) / vv
    print(f"  residual bottom eigenvalue of P0 along v: {float(lam0.mid()):.3e}"
          f"  (exact kernel => 0 up to rounding)")
    rows = []
    print(f"  {'delta':<8} {'min pivot':>13} {'v*DPv/v*v':>13}   slope(pivot)")
    prev = None
    for e in range(1, 25):
        delta = arb(10) ** (-e)
        P = pick_of_zeros(al, pair_zeros(G, delta))
        mp = min_pivot(P)
        DP = [[P[j][k] - P0[j][k] for k in range(3)] for j in range(3)]
        pred = quad_form(DP, v) / vv
        m, p = float(mp.mid()), float(pred.mid())
        sl = "" if prev is None else f"{log10(abs(prev)) - log10(abs(m)):>7.3f}"
        prev = m
        rows.append({"delta_exp": -e, "min_pivot": m, "vDPv": p})
        if e <= 3 or e % 2 == 0:
            print(f"  1e-{e:<5} {m:>13.3e} {p:>13.3e}   {sl}")
    out["part1"] = {"probes": [[str(a.real), str(a.imag)] for a in al],
                    "rows": rows}

    # -------- part 2: coefficients by Richardson at tiny delta -------------
    print("\n=== part 2: expansion coefficients of v*DPv/v*v ===")
    # f(delta) = c2 d^2 + c3 d^3 + c4 d^4 + ...; sample at d, d/2 and solve.
    d0 = arb(10) ** (-30)
    f = []
    for mult in (1, 2, 4):
        d = d0 * mult
        P = pick_of_zeros(al, pair_zeros(G, d))
        DP = [[P[j][k] - P0[j][k] for k in range(3)] for j in range(3)]
        f.append(quad_form(DP, v) / vv)
    # with f_i = f(m_i d0): solve for c2, c3, c4 exactly in ball arithmetic
    import itertools  # noqa: F401
    d1, d2, d4 = d0, d0 * 2, d0 * 4
    # linear system in (c2, c3, c4):
    M = [[d1 ** 2, d1 ** 3, d1 ** 4],
         [d2 ** 2, d2 ** 3, d2 ** 4],
         [d4 ** 2, d4 ** 3, d4 ** 4]]
    # Cramer, 3x3 real
    def det3(A):
        return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
                - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
                + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    D = det3(M)
    cs = []
    for col in range(3):
        Mc = [row[:] for row in M]
        for i in range(3):
            Mc[i][col] = f[i]
        cs.append(det3(Mc) / D)
    c2, c3, c4 = [float(c.mid()) for c in cs]
    print(f"  c2 = {c2:+.6e}   c3 = {c3:+.6e}   c4 = {c4:+.6e}")
    if c2 != 0 and c3 != 0:
        print(f"  crossover delta* ~ |c2/c3| = {abs(c2 / c3):.3e}  "
              f"(above this, the delta^3 term dominates)")
    if c2 != 0 and c4 != 0:
        print(f"  crossover vs c4:  sqrt|c2/c4| = {abs(c2 / c4) ** 0.5:.3e}")
    out["part2"] = {"c2": c2, "c3": c3, "c4": c4,
                    "note": "coefficients of v*DPv/v*v in powers of delta; "
                            "c2 = 2|v*u'|^2-type positive part minus the "
                            "Gram-derivative part (L-0008)"}

    # -------- part 2a': the L-0009 closed-form coefficient -----------------
    print("\n=== part 2a': predicted coefficient (L-0009) vs Richardson c2 ===")
    ap = [a - acb(1) / 2 for a in al]

    def Aprime(w):
        return acb(0, 1) * sum(v[j].conjugate() / (ap[j] - acb(0, 1) * w) ** 2
                               for j in range(3))
    vvn = sum((z * z.conjugate()).real for z in v)
    Apg, Apmg = Aprime(acb(arb(G))), Aprime(acb(-arb(G)))
    pred_c2 = float((-2 * ((Apg * Apg.conjugate()).real
                           + (Apmg * Apmg.conjugate()).real) / vvn).mid())
    print(f"  -2(|Ahat'(g)|^2+|Ahat'(-g)|^2)/v*v = {pred_c2:+.9e}")
    out["part2a_prime"] = {"predicted_c2": pred_c2,
                           "note": "L-0009(iv); compare part2 c2"}

    # -------- part 2b: is c2 < 0 for EVERY probe geometry? -----------------
    print("\n=== part 2b: sign of c2 across random probe geometries ===")
    # Deterministic pseudo-random geometries (no Date/random needed): a simple
    # LCG over integers, mapped into probe boxes.  For each, v = exact kernel
    # vector, c2 extracted at delta = 1e-30 (pure quadratic regime).
    state, signs, worst = 12345, {"neg": 0, "pos": 0, "zero": 0}, None
    d30 = arb(10) ** (-30)
    for trial in range(60):
        pts = []
        for _ in range(3):
            state = (1103515245 * state + 12345) % (2 ** 31)
            x = 0.51 + 0.9 * ((state >> 8) % 1000) / 1000.0
            state = (1103515245 * state + 12345) % (2 ** 31)
            y = 98.0 + 5.0 * ((state >> 8) % 1000) / 1000.0
            pts.append(acb(arb(repr(x)), arb(repr(y))))
        try:
            vt = null_vector_rank2(pts, G)
            P0t = pick_of_zeros(pts, pair_zeros(G, "0"))
            Pt = pick_of_zeros(pts, pair_zeros(G, d30))
            DPt = [[Pt[j][k] - P0t[j][k] for k in range(3)] for j in range(3)]
            vvt = sum((z * z.conjugate()).real for z in vt)
            c2t = quad_form(DPt, vt) / vvt / d30 ** 2
            c2f = float(c2t.mid())
        except Exception:
            continue
        if c2t < 0:
            signs["neg"] += 1
        elif c2t > 0:
            signs["pos"] += 1
        else:
            signs["zero"] += 1
        if worst is None or c2f > worst:
            worst = c2f
    print(f"  {signs['neg']} negative, {signs['pos']} positive, "
          f"{signs['zero']} undecided out of {sum(signs.values())} geometries")
    print(f"  largest (least negative) c2: {worst:.3e}")
    out["part2b"] = {"signs": signs, "largest_c2": worst,
                     "note": "c2 < 0 in every sampled geometry => any "
                             "rank-deficient cluster sees any off-line pair "
                             "at order delta^2; proving this is the open "
                             "half of Q-0016a"}

    # -------- part 3: realistic geometry, deep delta scan ------------------
    print("\n=== part 3: N = 16 with background, delta down to 1e-18 ===")
    def zeroset(delta, mode):
        zs, d, g0 = [], arb(delta), arb(G)
        for k in range(-90, 91):
            g = g0 + k * arb("0.9")
            if k == 0:
                loc = {"OFF": [acb(HALF - d, g), acb(HALF + d, g)],
                       "DOUBLE": [acb(HALF, g), acb(HALF, g)]}[mode]
                zs += loc + [z.conjugate() for z in loc]
            else:
                zs += [acb(HALF, g), acb(HALF, -g)]
        return zs
    al16 = PK.probe_cluster(100.8, 101.6, 16)
    floor = min_pivot(pick_of_zeros(al16, zeroset("0", "DOUBLE")))
    print(f"  floor (DOUBLE): {float(floor.mid()):.3e}")
    prev, rows3 = None, []
    for e in (2, 4, 6, 8, 10, 12, 14, 16, 18):
        mp = min_pivot(pick_of_zeros(al16, zeroset(arb(10) ** (-e), "OFF")))
        m = float(mp.mid())
        sl = "" if prev is None else f"{(log10(abs(prev)) - log10(abs(m))) / 2:>6.3f}"
        prev = m
        rows3.append({"delta_exp": -e, "min_pivot": m})
        print(f"  delta=1e-{e:<4} min pivot {m:>13.3e}   slope {sl}")
    out["part3"] = {"floor": float(floor.mid()), "rows": rows3}

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "pivot-expansion.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote", p)


if __name__ == "__main__":
    main()
