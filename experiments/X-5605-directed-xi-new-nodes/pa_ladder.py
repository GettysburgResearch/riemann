#!/usr/bin/env python3
"""Directed positive-anchor Christoffel ladder: PA-1, PA-3, PA-7 of issue #131.

Agent: fable5-01   Issue: #131

Adding `k` positive anchors `w_r` to the 16-node direct-xi table gives a
`16+k`-node table whose response cone covers every polynomial of degree
`<= 14+k` nonnegative on `[0, inf)`.  By L-9310's closure, positivity of that
entire cone is equivalent to positive semidefiniteness of the two Hankel
matrices of the extended moment sequence

    b_j = sum_i beta_i^{(j)} F(u_i)      over the enlarged node set,

with `H0 = (b_{i+j})` and `H1 = (b_{i+j+1})`.  Every ingredient is the same
machinery `directed_walls.py` validated against two oracles (their 70-digit
scan, and the directed basis blob from issue #131, all 15 moments agreeing):

  * old residuals from the 768-bit regenerated table;
  * anchor residuals from fresh 768-bit Arb evaluations at `x = sqrt(w)`
    (irrational `x` enters as a ball; the rectangle encloses the exact value);
  * exact rational basis vectors with zero-sum and response self-checks;
  * ball arithmetic end to end, so an LDL pivot that is positive as a ball is
    rigorously positive.

Verdict per packet: CERTIFIED_PSD (both Hankels positive definite -- the
whole degree-`14+k` cone is positive, no witness exists in it), or a
ball-negative pivot (an RH-disproof nomination via the corresponding
principal-minor direction), or UNDECIDED if a pivot ball straddles zero.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr

from flint import arb, acb, ctx

sys.path.insert(0, "/home/user/riemann/experiments/X-5605-directed-xi-new-nodes")
from directed_xi import T_NUM, T_DEN, SCALE_P
from directed_walls import (fr, rect_modsq_interval, residual_ball,
                            basis_vector, arb_fr)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

PACKETS = {
    "PA-1": [Fr(1)],
    "PA-3": [Fr(1, 8), Fr(3, 16), Fr(1, 4)],
    "PA-7": [Fr(1, 8), Fr(3, 16), Fr(1, 4), Fr(3, 8), Fr(1, 2), Fr(3, 4), Fr(1)],
}


def xi_scaled_ball_x(x_ball, prec):
    ctx.prec = prec
    s = acb(arb(1) / 2 + x_ball, arb_fr(Fr(T_NUM, T_DEN)))
    log_xi = ((s * (s - 1) / 2).log() - (s / 2) * arb.pi().log()
              + (s / 2).lgamma() + s.zeta().log())
    return (log_xi + arb(SCALE_P) * arb(2).log()).exp()


def anchor_residual(w: Fr, shells, prec):
    ctx.prec = prec
    z = xi_scaled_ball_x(arb_fr(w).sqrt(), prec)
    v = (z.real * z.real + z.imag * z.imag).log()
    for m_j, d2 in shells:
        v = v - arb(m_j) * arb_fr(w + d2).log()
    return v


def ldl_ball_pivots(H):
    """LDL pivots of a symmetric ball matrix; None entry = straddles zero."""
    n = len(H)
    L = [[arb(0)] * n for _ in range(n)]
    D = []
    for i in range(n):
        piv = H[i][i]
        for k in range(i):
            piv = piv - L[i][k] * L[i][k] * D[k]
        D.append(piv)
        if not (piv > 0):
            return D, (i if piv < 0 else None)
        L[i][i] = arb(1)
        for j in range(i + 1, n):
            v = H[j][i]
            for k in range(i):
                v = v - L[j][k] * L[i][k] * D[k]
            L[j][i] = v / piv
    return D, "ALL_POSITIVE"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", default="results/regenerated-table-p768.json")
    ap.add_argument("--prec", type=int, default=1500)
    ap.add_argument("--xi-prec", type=int, default=768)
    ap.add_argument("--out", default="results/pa-ladder.json")
    args = ap.parse_args()

    ctx.prec = args.prec
    cert = json.load(open(args.table))
    pts = sorted(cert["points"], key=lambda p: fr(p["u"], "u"))
    old_nodes = [fr(p["u"], "u") for p in pts]

    windows = sorted(cert["count_windows"], key=lambda w: fr(w["radius"], "r"))
    shells, prev = [], 0
    for w in windows:
        shells.append((w["count_lower"] - prev, fr(w["radius"], "r") ** 2))
        prev = w["count_lower"]

    old_res = {}
    for p, u in zip(pts, old_nodes):
        lo, hi = rect_modsq_interval(p["xi_rectangle"])
        ctx.prec = args.prec
        old_res[u] = residual_ball(lo, hi, u, shells)

    anchor_cache = {}
    results = []
    for name, anchors in PACKETS.items():
        t0 = time.time()
        for w in anchors:
            if w not in anchor_cache:
                anchor_cache[w] = anchor_residual(w, shells, args.xi_prec)
        nodes = sorted(old_nodes + anchors)
        res = dict(old_res)
        res.update({w: anchor_cache[w] for w in anchors})
        nmom = len(nodes) - 1                     # degrees 0 .. len-2
        ctx.prec = args.prec
        moments = []
        for k in range(nmom):
            beta = basis_vector(nodes, k)
            acc = arb(0)
            for u, b in zip(nodes, beta):
                acc = acc + arb_fr(b) * res[u]
            moments.append(acc)
        deg = nmom - 1                            # top usable degree 14+k
        m = (deg - 1) // 2
        H0 = [[moments[i + j] for j in range(m + 1)] for i in range(m + 1)]
        H1 = [[moments[i + j + 1] for j in range(m + 1)] for i in range(m + 1)]
        piv0, st0 = ldl_ball_pivots(H0)
        piv1, st1 = ldl_ball_pivots(H1)

        def report(pivs, st):
            if st == "ALL_POSITIVE":
                worst = min(pivs, key=lambda p: float(p.mid()))
                return "PSD", worst.str(12, radius=True)
            if st is None:
                return "UNDECIDED_PIVOT", pivs[-1].str(12, radius=True)
            return "NEGATIVE_PIVOT_%d" % st, pivs[-1].str(12, radius=True)

        s0, w0 = report(piv0, st0)
        s1, w1 = report(piv1, st1)
        verdict = ("CERTIFIED_PSD: the entire degree-%d response cone is "
                   "positive; no witness exists in this packet" % deg
                   if s0 == s1 == "PSD" else "%s / %s" % (s0, s1))
        rec = {"packet": name, "anchors": [str(a) for a in anchors],
               "nodes": len(nodes), "degree": deg,
               "hankel_size": m + 1,
               "H0_status": s0, "H0_worst_pivot": w0,
               "H1_status": s1, "H1_worst_pivot": w1,
               "verdict": verdict,
               "seconds": round(time.time() - t0, 1)}
        results.append(rec)
        print("%s  deg=%d  H0 %s (worst piv %s)  H1 %s (worst piv %s)  [%.0f s]"
              % (name, deg, s0, w0, s1, w1, rec["seconds"]), flush=True)
        print("   ", verdict, flush=True)

    out = {
        "schema": "riemann.x5605-pa-ladder.v1",
        "agent": "fable5-01",
        "classification": "DIRECTED: 768-bit primitives, exact rational basis "
                          "vectors with self-checked identities, ball LDL. A "
                          "ball-positive pivot set certifies PSD rigorously. "
                          "Moment pipeline validated against two oracles "
                          "(70-digit scan; the issue #131 directed basis blob, "
                          "all 15 moments agreeing).",
        "ordinate": {"numerator": T_NUM, "denominator": T_DEN},
        "prec_bits": {"xi": args.xi_prec, "ladder": args.prec},
        "packets": results,
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
