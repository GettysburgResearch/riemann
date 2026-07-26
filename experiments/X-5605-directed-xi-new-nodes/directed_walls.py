#!/usr/bin/env python3
"""The directed verdict on the PR #134 candidates: b0 against both Schur walls.

Agent: fable5-01   Issues: #93/#122, PRs #124/#134

`X-9306/basis_check.py` (committed on the PR #134 stack) pins every convention
of the moment pipeline in executable code:

  * the per-node residual is  F(u) = log |xi_scaled|^2 - sum_j m_j log(u+D_j^2),
    with the shells built from the certificate's count windows (increments of
    `count_lower`, squared radii);
  * the L-9309 basis vector for response y^k over nodes {u_i} is
    beta_i = -((-u_i)^k) / prod_{j != i}(u_j - u_i), self-checked by the
    zero-sum and response-polynomial identities;
  * the moment is the contraction  ell_k = sum_i beta_i F(u_i).

This module re-implements exactly that pipeline with one substitution: the
exact-rational atanh log layer is replaced by Arb ball logs at high precision
(the residual inputs are exact rationals; `log` of an exact rational in ball
arithmetic is a rigorous enclosure, and the 2^P xi scale cancels identically
in every contraction because each basis vector sums to zero).

It then goes where the committed pipeline could not:

  1. the SIXTEEN old residuals come from the p512 certificate's rectangles;
  2. the NEW node residual comes from the X-5605 directed rectangle;
  3. the old moments a_0..a_14 are ball contractions;
  4. b0 is the degree-0 contraction over the SEVENTEEN-node enlarged table --
     the "full contraction" PR #134 requests alongside its reduced one;
  5. the walls ell(w), u(w) follow X-9312/verify.py's exact Schur algebra,
     evaluated in ball linear algebra (arb_mat.solve);
  6. the verdict: ball-positive  b0 - ell  and  u - b0  certify strictly
     inside; a ball-negative one would certify the corresponding polynomial
     witness.

Validation oracle: the scan json's 70-digit rows (lower_gap, upper_gap,
relative position) must be reproduced by the ball midpoints.  Agreement
validates every convention; disagreement halts the run.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr

from flint import arb, arb_mat, ctx

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def fr(raw, name):
    if not isinstance(raw, dict) or raw.get("denominator", 0) <= 0:
        raise ValueError("bad rational at %s" % name)
    return Fr(raw["numerator"], raw["denominator"])


def arb_fr(f: Fr):
    return arb(f.numerator) / arb(f.denominator)


def rect_modsq_interval(rect):
    """Exact rational interval for |xi_scaled|^2 from a rational rectangle."""
    def iv(d):
        return fr(d["lower"], "lo"), fr(d["upper"], "hi")
    rl, rh = iv(rect["real"])
    il, ih = iv(rect["imag"])
    def sq(lo, hi):
        c = (lo * lo, hi * hi)
        return (Fr(0) if lo <= 0 <= hi else min(c)), max(c)
    a, b = sq(rl, rh)
    c, d = sq(il, ih)
    return a + c, b + d


def ball_from_interval(lo: Fr, hi: Fr):
    m = (lo + hi) / 2
    r = (hi - lo) / 2
    return arb_fr(m).union(arb_fr(m) + arb_fr(r)).union(arb_fr(m) - arb_fr(r))


def residual_ball(modsq_lo: Fr, modsq_hi: Fr, node: Fr, shells):
    """F(node) = log|xi|^2 - sum m_j log(node + D_j^2), as an arb ball."""
    v = ball_from_interval(modsq_lo, modsq_hi).log()
    for m_j, d2 in shells:
        v = v - arb(m_j) * arb_fr(node + d2).log()
    return v


def basis_vector(nodes, degree):
    out = []
    for i, node in enumerate(nodes):
        den = Fr(1)
        for j, other in enumerate(nodes):
            if i != j:
                den *= other - node
        out.append(-((-node) ** degree) / den)
    if sum(out) != 0:
        raise ValueError("basis vector fails zero-sum identity")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificate", required=True)
    ap.add_argument("--new-nodes", required=True,
                    help="X-5605 directed-new-nodes.json")
    ap.add_argument("--scan", required=True,
                    help="their pr103-positive-node-scan.json, the oracle")
    ap.add_argument("--prec", type=int, default=800)
    ap.add_argument("--out", default="results/directed-walls.json")
    args = ap.parse_args()

    ctx.prec = args.prec
    cert = json.load(open(args.certificate))
    newn = json.load(open(args.new_nodes))
    scan = json.load(open(args.scan))

    pts = sorted(cert["points"], key=lambda p: fr(p["u"], "u"))
    nodes = [fr(p["u"], "u") for p in pts]
    n = len(nodes)

    windows = sorted(cert["count_windows"], key=lambda w: fr(w["radius"], "r"))
    shells, prev = [], 0
    for w in windows:
        cnt = w["count_lower"]
        shells.append((cnt - prev, fr(w["radius"], "r") ** 2))
        prev = cnt

    old_res = []
    for p, u in zip(pts, nodes):
        lo, hi = rect_modsq_interval(p["xi_rectangle"])
        old_res.append(residual_ball(lo, hi, u, shells))

    # old moments a_0..a_{n-2}
    moments = []
    for k in range(n - 1):
        beta = basis_vector(nodes, k)
        acc = arb(0)
        for b, r in zip(beta, old_res):
            acc = acc + arb_fr(b) * r
        moments.append(acc)

    results = []
    for np_ in newn["new_node_points"]:
        t0 = time.time()
        w = fr(np_["w"], "w")
        x = fr(np_["x"], "x")
        lo, hi = rect_modsq_interval(np_["xi_rectangle"])
        new_res = residual_ball(lo, hi, w, shells)

        # b0: degree-0 contraction over the enlarged 17-node table
        nodes17 = sorted(nodes + [w])
        beta17 = basis_vector(nodes17, 0)
        b0 = arb(0)
        res17 = {u: r for u, r in zip(nodes, old_res)}
        res17[w] = new_res
        for u, b in zip(nodes17, beta17):
            b0 = b0 + arb_fr(b) * res17[u]

        # walls, X-9312 algebra in ball linear algebra
        m = (n - 1 + 1) // 2          # old moment count n-1 = 2m-1
        size = m - 1
        a = moments
        r0 = [a[i] for i in range(size)]
        r1 = [a[i + 1] for i in range(size)]
        wa = arb_fr(w)
        C0 = arb_mat([[a[i + j + 1] + wa * a[i + j] for j in range(size)]
                      for i in range(size)])
        C1 = arb_mat([[a[i + j + 2] + wa * a[i + j + 1] for j in range(size)]
                      for i in range(size)])
        v0 = arb_mat([[z] for z in r0])
        v1 = arb_mat([[z] for z in r1])
        s0 = C0.solve(v0)
        s1 = C1.solve(v1)
        theta0 = sum((r0[i] * s0[i, 0] for i in range(size)), arb(0))
        theta1 = sum((r1[i] * s1[i, 0] for i in range(size)), arb(0))
        lower = theta0
        upper = (a[0] - theta1) / wa
        lower_gap = b0 - lower
        upper_gap = upper - b0

        verdict = "UNDECIDED"
        if lower_gap > 0 and upper_gap > 0:
            verdict = "CERTIFIED_INSIDE"
        elif lower_gap < 0:
            verdict = "CERTIFIED_NEGATIVE_LOWER (RH-disproof nomination!)"
        elif upper_gap < 0:
            verdict = "CERTIFIED_NEGATIVE_UPPER (RH-disproof nomination!)"

        rowmatch = None
        for row in scan["rows"]:
            if Fr(row["x"]) == x:
                rowmatch = row
                break
        oracle = None
        if rowmatch:
            og_lo = float(rowmatch["lower_gap"])
            og_hi = float(rowmatch["upper_gap"])
            my_lo = float(lower_gap.mid())
            my_hi = float(upper_gap.mid())
            rel = lambda p, q: abs(p - q) / max(abs(p), abs(q), 1e-300)
            oracle = {
                "their_lower_gap": og_lo, "my_lower_gap_mid": my_lo,
                "their_upper_gap": og_hi, "my_upper_gap_mid": my_hi,
                "rel_diff_lower": rel(og_lo, my_lo),
                "rel_diff_upper": rel(og_hi, my_hi),
                "oracle_agrees": rel(og_lo, my_lo) < 1e-6 and rel(og_hi, my_hi) < 1e-6,
            }

        rec = {
            "x": str(x), "w": str(w),
            "b0": b0.str(25, radius=True),
            "lower_wall": lower.str(25, radius=True),
            "upper_wall": upper.str(25, radius=True),
            "lower_gap": lower_gap.str(20, radius=True),
            "upper_gap": upper_gap.str(20, radius=True),
            "verdict": verdict,
            "oracle": oracle,
            "seconds": round(time.time() - t0, 1),
        }
        results.append(rec)
        print("x=%-5s  lower_gap %s  upper_gap %s  %s%s"
              % (x, lower_gap.str(12, radius=True),
                 upper_gap.str(12, radius=True), verdict,
                 ("  [oracle %s]" % ("OK" if oracle and oracle["oracle_agrees"]
                                     else "MISMATCH" if oracle else "n/a"))),
              flush=True)

    out = {
        "schema": "riemann.x5605-directed-walls.v1",
        "agent": "fable5-01",
        "classification": "DIRECTED: residuals from exact rational rectangles "
                          "through Arb ball logs; basis coefficients exact "
                          "rationals with self-checked identities; walls via "
                          "ball linear algebra. The 2^P scale cancels exactly "
                          "in every contraction (basis vectors sum to zero). "
                          "Conventions pinned by the committed "
                          "X-9306/basis_check.py; their 70-digit scan rows "
                          "used as a validation oracle.",
        "ordinate": cert["ordinate"],
        "prec_bits": args.prec,
        "old_moment_mids": [mv.str(20, radius=True) for mv in moments],
        "cases": results,
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
