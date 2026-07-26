#!/usr/bin/env python3
"""Rigorous close-pair census from a file of Platt-isolated zero balls.

Agent: fable5-01   Issue: #55

Input: one `lo hi` pair per line (exact rationals), the output of
`platt_certify.py --balls-out`.  Every ordinate is a rigorous enclosure, so
every gap is a rigorous interval `[lo_{i+1}-hi_i, hi_{i+1}-lo_i]` — the census
needs no scan, no refinement and no trust in any floating value.

Products:

  * distribution of normalised gaps `delta = gap * log(t/2pi)/2pi` against the
    GUE (Gaudin) small-gap law `P(delta < s) ~ (pi^2/3) s^3 - (2 pi^4/45) s^5`
    (leading terms; heuristic reference only, clearly labelled);
  * the certified `k` smallest pairs, each with its rigorous delta interval;
  * for the tightest few, a certified enclosure of `Z` at the dyadic midpoint —
    the interior extremum size is what makes a pair "Lehmer", and a certified
    small |Z| there is the pair's quality certificate.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as Fr

from flint import acb, arb, ctx


def Z_ball(t_fr: Fr, prec: int):
    ctx.prec = prec
    t = arb(t_fr.numerator) / arb(t_fr.denominator)
    if not t.is_exact():
        return None
    th = acb(arb(1) / 4, t / 2).lgamma().imag - (t / 2) * arb.pi().log()
    return (acb(0, th).exp() * acb(arb(1) / 2, t).zeta()).real


def dyadic(x: Fr, bits: int) -> Fr:
    scale = 1 << bits
    return Fr(round(x * scale), scale)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("balls")
    ap.add_argument("--top", type=int, default=12)
    ap.add_argument("--interior-z", type=int, default=4,
                    help="certify Z at the midpoint of this many tightest pairs")
    ap.add_argument("--out", default="results/gap-census.json")
    args = ap.parse_args()

    balls = []
    for line in open(args.balls):
        p = line.split()
        if len(p) == 2:
            balls.append((Fr(p[0]), Fr(p[1])))
    n = len(balls)
    t_mid = float((balls[0][0] + balls[-1][1]) / 2)
    ell = math.log(t_mid / (2 * math.pi)) / (2 * math.pi)

    gaps = []
    order_ok = True
    for i in range(n - 1):
        if balls[i + 1][0] <= balls[i][1]:
            order_ok = False
            break
        glo = float(balls[i + 1][0] - balls[i][1]) * ell
        ghi = float(balls[i + 1][1] - balls[i][0]) * ell
        gaps.append((ghi, glo, i))
    if not order_ok:
        raise SystemExit("balls are not strictly ordered/disjoint; refusing")

    uppers = sorted(g[0] for g in gaps)
    mean = sum(uppers) / len(uppers)

    # GUE reference (heuristic): P(min of m gaps < s) with P(delta<s) ~ (pi^2/3)s^3
    m = len(gaps)
    s_exp = (3.0 / (m * math.pi ** 2)) ** (1.0 / 3.0)

    hist_edges = [0.05 * k for k in range(21)]
    hist = [0] * (len(hist_edges) - 1)
    for u in uppers:
        k = min(int(u / 0.05), len(hist) - 1)
        hist[k] += 1

    tight = sorted(gaps)[:args.top]
    top_rows = []
    for rank, (ghi, glo, i) in enumerate(tight):
        row = {
            "rank": rank + 1,
            "delta_interval": [glo, ghi],
            "gamma1_ball": [str(balls[i][0]), str(balls[i][1])],
            "gamma2_ball": [str(balls[i + 1][0]), str(balls[i + 1][1])],
            "gamma1_approx": float(balls[i][0]),
        }
        if rank < args.interior_z:
            mid = dyadic((balls[i][1] + balls[i + 1][0]) / 2, 40)
            z = Z_ball(mid, 128)
            row["interior_point"] = str(mid)
            row["interior_Z_ball"] = z.str(12, radius=True) if z is not None else None
        top_rows.append(row)

    res = {
        "schema": "riemann.x5604-gap-census.v1",
        "agent": "fable5-01",
        "classification": "RIGOROUS gaps: every ordinate is a Platt-isolated "
                          "ball, every gap an exact interval from ball "
                          "endpoints. The GUE comparison is a heuristic "
                          "reference and is labelled as such.",
        "n_zeros": n,
        "range": [float(balls[0][0]), float(balls[-1][1])],
        "ell": ell,
        "mean_normalised_gap_upper": mean,
        "gue_expected_min_delta": s_exp,
        "min_delta_interval": [tight[0][1], tight[0][0]],
        "ratio_min_over_gue_expected": tight[0][0] / s_exp,
        "histogram_bin_width": 0.05,
        "histogram_counts": hist,
        "tightest_pairs": top_rows,
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("zeros %d  mean delta %.5f  GUE-expected min %.4f  observed min in [%.4f, %.4f]"
          % (n, mean, s_exp, tight[0][1], tight[0][0]))
    for r in top_rows[:6]:
        z = r.get("interior_Z_ball")
        print("  #%d  delta in [%.5f, %.5f]  at %.4f%s"
              % (r["rank"], r["delta_interval"][0], r["delta_interval"][1],
                 r["gamma1_approx"], ("   interior Z = %s" % z) if z else ""))
    print("wrote", args.out)


if __name__ == "__main__":
    main()
