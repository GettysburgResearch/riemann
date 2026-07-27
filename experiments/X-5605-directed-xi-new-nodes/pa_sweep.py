#!/usr/bin/env python3
"""PA-3 directed sweep across the 65 PR #103 ordinate shifts (issue #131 step 3).

Agent: fable5-01   Issue: #131

For each shift `s = j/32`, `j = -32..32`, around the PR #71 count center:

  * the deflation profile is the committed L-9306 nested-count rule taken from
    `X-9302/results/complete-result.json`: nine unconditional nested windows
    `(count_k, r_k)` around the center, entering the residual at the shifted
    ordinate `T_s = center + s` with squared distance `(r_k + |s|)^2` — the
    `shifted_radius_rule = source_radius + absolute_ordinate_shift` recorded in
    that artifact.  One profile, uniform across the sweep.  (The atomized
    profile of the center certificate is sharper but is committed only for one
    shift; a sweep must not change functionals mid-flight.)
  * 19 primitives (16 old nodes `u = 4^-20..4^-5`, anchors `{1/8, 3/16, 1/4}`)
    are evaluated fresh at 768 bits per shift;
  * 18 ball moments over the 19-node table, then the degree-17 cone's two
    Hankel matrices, ball LDL.

Verdict per shift: CERTIFIED_PSD, or a ball-negative pivot (an RH-disproof
nomination pending the parent-representation review), or UNDECIDED.

Workers shard by shift; each worker writes its own JSON and the merge step
assembles the landscape.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr

from flint import arb, acb, ctx

sys.path.insert(0, "/home/user/riemann/experiments/X-5605-directed-xi-new-nodes")
from directed_walls import basis_vector, arb_fr
from pa_ladder import ldl_ball_pivots

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

CENTER = Fr(20225875608341108140435, 2 ** 32)
SCALE_P = 5335951715288
OLD_NODES = [Fr(1, 4 ** j) for j in range(20, 4, -1)]      # 4^-20 .. 4^-5
ANCHORS = [Fr(1, 8), Fr(3, 16), Fr(1, 4)]

RAW_WINDOWS_FILE = ("/home/user/riemann/experiments/X-5605-directed-xi-new-nodes/"
                    "raw-nested-windows.json")


def xi_scaled_at(T: Fr, x_ball, prec: int):
    ctx.prec = prec
    s = acb(arb(1) / 2 + x_ball, arb_fr(T))
    log_xi = ((s * (s - 1) / 2).log() - (s / 2) * arb.pi().log()
              + (s / 2).lgamma() + s.zeta().log())
    return (log_xi + arb(SCALE_P) * arb(2).log()).exp()


def residual_at(T: Fr, node: Fr, shells, xi_prec: int, work_prec: int):
    z = xi_scaled_at(T, arb_fr(node).sqrt(), xi_prec)
    ctx.prec = work_prec
    v = (z.real * z.real + z.imag * z.imag).log()
    for m_k, d2 in shells:
        v = v - arb(m_k) * arb_fr(node + d2).log()
    return v


def run_shift(j: int, raw_windows, xi_prec: int, work_prec: int):
    s = Fr(j, 32)
    T = CENTER + s
    shells, prev = [], 0
    for cnt, r in raw_windows:
        shells.append((cnt - prev, (r + abs(s)) ** 2))
        prev = cnt
    nodes = sorted(OLD_NODES + ANCHORS)
    res = {}
    t0 = time.time()
    for u in nodes:
        res[u] = residual_at(T, u, shells, xi_prec, work_prec)
    ctx.prec = work_prec
    moments = []
    for k in range(len(nodes) - 1):
        beta = basis_vector(nodes, k)
        acc = arb(0)
        for u, b in zip(nodes, beta):
            acc = acc + arb_fr(b) * res[u]
        moments.append(acc)
    deg = len(moments) - 1
    m = (deg - 1) // 2
    H0 = [[moments[i + k] for k in range(m + 1)] for i in range(m + 1)]
    H1 = [[moments[i + k + 1] for k in range(m + 1)] for i in range(m + 1)]
    piv0, st0 = ldl_ball_pivots(H0)
    piv1, st1 = ldl_ball_pivots(H1)

    def rep(pivs, st):
        if st == "ALL_POSITIVE":
            worst = min(pivs, key=lambda p: float(p.mid()))
            return "PSD", float(worst.mid()), float(worst.rad())
        return ("NEGATIVE_PIVOT" if isinstance(st, int) else "UNDECIDED",
                float(pivs[-1].mid()), float(pivs[-1].rad()))

    s0, m0, r0 = rep(piv0, st0)
    s1, m1, r1 = rep(piv1, st1)
    return {
        "j": j, "shift": str(s), "T": str(T),
        "H0": s0, "H0_worst_mid": m0, "H0_worst_rad": r0,
        "H1": s1, "H1_worst_mid": m1, "H1_worst_rad": r1,
        "verdict": ("CERTIFIED_PSD" if s0 == s1 == "PSD"
                    else "%s/%s" % (s0, s1)),
        "seconds": round(time.time() - t0, 1),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--j-lo", type=int, required=True)
    ap.add_argument("--j-hi", type=int, required=True)
    ap.add_argument("--xi-prec", type=int, default=768)
    ap.add_argument("--work-prec", type=int, default=1500)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    raw = [(w["count"], Fr(w["radius"]["numerator"], w["radius"]["denominator"]))
           for w in json.load(open(RAW_WINDOWS_FILE))]

    rows = []
    for j in range(args.j_lo, args.j_hi + 1):
        r = run_shift(j, raw, args.xi_prec, args.work_prec)
        rows.append(r)
        print("j=%-4d shift=%-7s  %s  H0 worst %.3e  H1 worst %.3e  [%.0f s]"
              % (j, r["shift"], r["verdict"], r["H0_worst_mid"],
                 r["H1_worst_mid"], r["seconds"]), flush=True)
    with open(args.out, "w") as fh:
        json.dump({"schema": "riemann.x5605-pa3-sweep.v1",
                   "agent": "fable5-01",
                   "deflation_profile": "L-9306 nested windows, "
                   "shifted_radius_rule = source_radius + |shift|",
                   "anchors": [str(a) for a in ANCHORS],
                   "rows": rows}, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
