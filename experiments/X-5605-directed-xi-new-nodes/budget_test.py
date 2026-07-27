#!/usr/bin/env python3
"""First directed run of the L-13203 line-mass budget (issue #137).

Agent: fable5-01   Issue: #137

The predicate: a *positive* multi-anchor response can still contradict RH if
it is smaller than the unavoidable contribution of certified surviving
critical-line zero bins,

    upper( L(R) )  <  sum_j m_j lambda_j   ==>  RH-disproof nomination,

with R = q(y)^2 / W(y) (or y q^2 / W), y_gamma = (T - gamma)^2, and the bins
required to be zeros NOT already consumed by the parent certificate's
atomized deflation shells (the SELECTED_FACTOR_RESIDUAL discipline: only
zeros beyond the largest shell radius are used, whose mass was never
subtracted).

Bins here are Platt-isolated ordinate balls (X-5604 engine) inside the
O-5608 window, each a rigorous enclosure of one simple critical-line zero;
`m_j = 1`, pairwise disjoint by construction, with location -- exactly the
"proof-grade disjoint zero bins with multiplicity lower bounds" the issue
requires and notes that global counts cannot supply.

Two cases, in the issue's candidate order:

  A. one-anchor `x = 1/20` (`w = 1/400`), `q = 1`: the total response is the
     new scalar `b0` itself;
  B. PA-7 near-null direction: `q` frozen to a rational vector near the
     midpoint minimal eigenvector of the degree-21 packet's `H0`, the total
     `sum v_j v_k b_{j+k}` contracted against ball moments.

Everything on the bin side is exact rational arithmetic per L-13203's
leverage recipe (interval Horner for q, `W` at the upper endpoint); the
total-response side is ball arithmetic on the twice-oracle-validated moment
pipeline.  Classification: conditional on the inherited L-9308 response
representation, exactly as issue #137 states.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr

from flint import arb, ctx

sys.path.insert(0, "/home/user/riemann/experiments/X-5605-directed-xi-new-nodes")
from directed_xi import T_NUM, T_DEN
from directed_walls import fr, rect_modsq_interval, residual_ball, basis_vector, arb_fr
from pa_ladder import anchor_residual, PACKETS

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

COUNT_CENTER = Fr(20225875608341108140435, 2 ** 32)
T_PRIM = Fr(T_NUM, T_DEN)


def poly_eval_interval(coeffs, ylo: Fr, yhi: Fr):
    """Interval Horner for a rational-coefficient polynomial on [ylo, yhi]."""
    lo, hi = Fr(coeffs[-1]), Fr(coeffs[-1])
    for c in reversed(coeffs[:-1]):
        cands = [lo * ylo, lo * yhi, hi * ylo, hi * yhi]
        lo, hi = min(cands) + c, max(cands) + c
    return lo, hi


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", default="results/regenerated-table-p768.json")
    ap.add_argument("--balls", default="results/balls-pr103-window.txt")
    ap.add_argument("--prec", type=int, default=1500)
    ap.add_argument("--out", default="results/budget-test.json")
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
    r_max = max(fr(w["radius"], "r") for w in windows)

    old_res = {}
    for p, u in zip(pts, old_nodes):
        lo, hi = rect_modsq_interval(p["xi_rectangle"])
        old_res[u] = residual_ball(lo, hi, u, shells)

    # surviving bins: Platt balls strictly beyond every shell radius
    bins = []
    for line in open(args.balls):
        parts = line.split()
        if len(parts) != 2:
            continue
        glo, ghi = Fr(parts[0]), Fr(parts[1])
        # distance from the COUNT CENTER decides survival (fail-closed: the
        # whole ball must be beyond r_max)
        if ghi < COUNT_CENTER - r_max or glo > COUNT_CENTER + r_max:
            d1, d2 = T_PRIM - ghi, T_PRIM - glo      # gamma below T -> positive
            if glo > T_PRIM:                          # gamma above T
                d1, d2 = glo - T_PRIM, ghi - T_PRIM
            dlo, dhi = min(abs(d1), abs(d2)), max(abs(d1), abs(d2))
            bins.append((dlo * dlo, dhi * dhi))
    bins.sort()
    print("surviving bins beyond shell radius %.4f: %d  (y from %.2f to %.2f)"
          % (float(r_max), len(bins), float(bins[0][0]), float(bins[-1][1])),
          flush=True)

    def budget_case(name, anchors, qcoeffs, total_ball, wpoly_nodes):
        t0 = time.time()
        lam_sum = Fr(0)
        n_zero_lam = 0
        for ylo, yhi in bins:
            qlo, qhi = poly_eval_interval(qcoeffs, ylo, yhi)
            if qlo <= 0 <= qhi:
                qmin2 = Fr(0)
                n_zero_lam += 1
            else:
                qmin2 = min(qlo * qlo, qhi * qhi)
            W = Fr(1)
            for u in wpoly_nodes:
                W *= (yhi + u)
            lam_sum += qmin2 / W
        upper_total = total_ball.upper()
        man, ex = upper_total.mid().man_exp()
        ub = Fr(int(man)) * (Fr(2) ** int(ex))
        reversal = ub < lam_sum
        sat = float(lam_sum) / float(total_ball.mid()) if float(total_ball.mid()) else None
        rec = {
            "case": name, "anchors": [str(a) for a in anchors],
            "bins_used": len(bins), "bins_with_zero_leverage": n_zero_lam,
            "certified_line_mass": float(lam_sum),
            "total_response_ball": total_ball.str(15, radius=True),
            "saturation_ratio": sat,
            "reversal": bool(reversal),
            "verdict": ("RH-DISPROOF NOMINATION (pending L-9308 review and "
                        "independent reproduction)" if reversal else
                        "NO REVERSAL: response dominates certified line mass, "
                        "consistent with RH"),
            "seconds": round(time.time() - t0, 1),
        }
        print("%s: line mass %.4e  vs response %s  saturation %.3e  %s"
              % (name, float(lam_sum), total_ball.str(10, radius=True),
                 sat if sat else -1,
                 "REVERSAL!" if reversal else "no reversal"), flush=True)
        return rec

    results = []

    # -- Case A: x = 1/20, q = 1 ------------------------------------------
    w_a = Fr(1, 400)
    res_a = anchor_residual(w_a, shells, 768)
    nodes17 = sorted(old_nodes + [w_a])
    res17 = dict(old_res)
    res17[w_a] = res_a
    ctx.prec = args.prec
    beta = basis_vector(nodes17, 0)
    b0 = arb(0)
    for u, b in zip(nodes17, beta):
        b0 = b0 + arb_fr(b) * res17[u]
    results.append(budget_case("A: x=1/20, q=1", [w_a], [Fr(1)], b0, nodes17))

    # -- Case B: PA-7 near-null H0 direction ------------------------------
    anchors7 = PACKETS["PA-7"]
    res23 = dict(old_res)
    for w in anchors7:
        res23[w] = anchor_residual(w, shells, 768)
    nodes23 = sorted(old_nodes + anchors7)
    ctx.prec = args.prec
    moments = []
    for k in range(len(nodes23) - 1):
        bvec = basis_vector(nodes23, k)
        acc = arb(0)
        for u, b in zip(nodes23, bvec):
            acc = acc + arb_fr(b) * res23[u]
        moments.append(acc)
    m = (len(moments) - 1 - 1) // 2                  # degree 21 -> m = 10
    import numpy as np
    H0mid = np.array([[float(moments[i + j].mid()) for j in range(m + 1)]
                      for i in range(m + 1)])
    evals, evecs = np.linalg.eigh(H0mid)
    v = evecs[:, 0] / np.max(np.abs(evecs[:, 0]))
    qc = [Fr(round(x * (1 << 40)), 1 << 40) for x in v]
    total = arb(0)
    for i, vi in enumerate(qc):
        for j, vj in enumerate(qc):
            total = total + arb_fr(vi * vj) * moments[i + j]
    results.append(budget_case("B: PA-7 near-null H0 direction", anchors7,
                               qc, total, nodes23))

    out = {
        "schema": "riemann.x5605-line-mass-budget.v1",
        "agent": "fable5-01",
        "classification": "conditional on the inherited L-9308 response "
                          "representation (as issue #137 itself states); the "
                          "bin side is exact rational arithmetic on "
                          "Platt-certified zero balls, the response side is "
                          "ball arithmetic on the twice-oracle-validated "
                          "moment pipeline. SELECTED_FACTOR_RESIDUAL "
                          "discipline: only zeros beyond the largest "
                          "deflation shell are used.",
        "ordinate": {"numerator": T_NUM, "denominator": T_DEN},
        "count_center": str(COUNT_CENTER),
        "max_shell_radius": str(r_max),
        "cases": results,
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
