#!/usr/bin/env python3
"""Slab certification and rigorous gap census from Platt zero blocks.

Agent: fable5-01   Issue: #55

`platt_ctypes.py` reaches `acb_dirichlet_platt_local_hardy_z_zeros`, which at
index `4.3e13` and 128 bits isolates zeros at `0.039` s each in blocks of
2000 — `7.2x` cheaper than the sign-sampling of `certify_parallel.py`, and it
returns *rigorously isolated ordinate balls* (`+-1e-15` near the block start)
rather than mere signs.  (At 64 bits the heuristics fail and it returns 0;
128 bits is the working precision.)

This module chains blocks into two products:

**Slab certificate.**  For a dyadic slab `(a,b)`: `N` from `zeta_nzeros` as
before; then Platt balls starting at index `N(a)+1`.  The balls are checked —
from the data, not from trust — to be strictly increasing and pairwise
disjoint, and only balls strictly inside `(a,b)` are counted.  Disjoint balls
each containing a zero of `Z` give `N_0 >= count`; reaching `N` forces `D = 0`.
The semantic trust here is that an "isolated zero" ball contains a zero of `Z`
— the same trust class as `zeta_nzeros` itself, both being documented rigorous
outputs of the same library.  The pairwise-disjointness and containment gates
are re-derived exactly.

**Rigorous gap census.**  Consecutive balls give rigorous gap intervals
`[lo_{i+1}-hi_i, hi_{i+1}-lo_i]`.  Ranking by the *upper* end of the interval
yields certified-close pairs: a pair whose gap upper bound is small is
rigorously close, no scan and no refinement pass needed.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from fractions import Fraction as Fr

from flint import arb, ctx

from platt_ctypes import platt_zeros


def ball_to_interval(s: str):
    """Parse an arb ball string '[m +/- r]' (or exact 'm') into (lo, hi) Fractions."""
    s = s.strip()
    if s.startswith("["):
        body = s[1:-1]
        if "+/-" in body:
            m, r = body.split("+/-")
            mid, rad = Fr(m.strip()), Fr(r.strip())
        else:
            mid, rad = Fr(body.strip()), Fr(0)
    else:
        mid, rad = Fr(s), Fr(0)
    return mid - rad, mid + rad


def nzeros_int(t_fr: Fr, prec: int):
    ctx.prec = prec
    x = arb(t_fr.numerator) / arb(t_fr.denominator)
    if not x.is_exact():
        raise ValueError("endpoint not exact")
    n = x.zeta_nzeros().unique_fmpz()
    if n is None:
        raise ValueError("count ball does not isolate an integer")
    return int(n)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--prec", type=int, default=128)
    ap.add_argument("--count-prec", type=int, default=192)
    ap.add_argument("--block", type=int, default=2000)
    ap.add_argument("--top-gaps", type=int, default=15)
    ap.add_argument("--balls-out", default=None,
                    help="also write the ordinate balls, one '[lo,hi]' per line")
    ap.add_argument("--label", default="")
    ap.add_argument("--Na", type=int, default=None,
                    help="known rigorous N(a); skips the zeta_nzeros call")
    ap.add_argument("--Nb", type=int, default=None)
    ap.add_argument("--out", default="platt-certify.json")
    args = ap.parse_args()

    a, b = Fr(args.a), Fr(args.b)
    t0 = time.time()
    Na = args.Na if args.Na is not None else nzeros_int(a, args.count_prec)
    Nb = args.Nb if args.Nb is not None else nzeros_int(b, args.count_prec)
    N = Nb - Na
    print("%s N(a)=%d N(b)=%d -> N=%d  [%.0f s]"
          % (args.label, Na, Nb, N, time.time() - t0), flush=True)

    balls = []                      # list of (lo, hi) Fractions, strictly inside
    problems = []
    n_next = Na + 1
    t1 = time.time()
    while True:
        want = min(args.block, N - len(balls) + 8)   # small overshoot on purpose
        got, out = platt_zeros(n_next, want, args.prec)
        if got == 0:
            problems.append("platt returned 0 at index %d" % n_next)
            break
        prev_hi = balls[-1][1] if balls else None
        done = False
        for s in out:
            lo, hi = ball_to_interval(s)
            if prev_hi is not None and lo <= prev_hi:
                problems.append("balls overlap or are unordered near %s" % s[:40])
                done = True
                break
            prev_hi = hi
            if hi >= b:
                done = True
                break
            if lo > a:
                balls.append((lo, hi))
        n_next += got
        print("  ...%d balls inside, index at %d  [%.0f s]"
              % (len(balls), n_next, time.time() - t1), flush=True)
        if done or len(balls) >= N:
            break

    N0 = len(balls)
    dt = time.time() - t1

    # rigorous gap census
    t_mid = float((a + b) / 2)
    ell = math.log(t_mid / (2 * math.pi)) / (2 * math.pi)
    gaps = []
    for i in range(len(balls) - 1):
        glo = balls[i + 1][0] - balls[i][1]
        ghi = balls[i + 1][1] - balls[i][0]
        gaps.append((float(ghi) * ell, float(glo) * ell, i, float(balls[i][0])))
    by_upper = sorted(gaps)[:args.top_gaps]

    res = {
        "schema": "riemann.x5604-platt-certify.v1",
        "agent": "fable5-01",
        "classification": "RIGOROUS: N from zeta_nzeros balls isolating unique "
                          "integers; N_0 from pairwise-disjoint Platt-isolated "
                          "zero balls strictly inside the slab (semantic trust: "
                          "an isolated ball contains a zero of Z, same class as "
                          "zeta_nzeros). Gap intervals derived exactly from the "
                          "ball endpoints.",
        "label": args.label,
        "a": str(a), "b": str(b), "span": float(b - a),
        "prec_zeros": args.prec, "prec_counts": args.count_prec,
        "N": N, "N0_disjoint_balls_inside": N0,
        "D": (N - N0) if not problems else None,
        "problems": problems,
        "seconds_counts": t1 - t0, "seconds_zeros": dt,
        "seconds_per_zero": dt / max(1, N0),
        "ell": ell,
        "smallest_gaps_by_upper_bound": [
            {"delta_interval": [dlo, dhi], "gamma_approx": g}
            for dhi, dlo, i, g in by_upper],
    }
    if problems:
        res["verdict"] = "INCOMPLETE: " + "; ".join(problems)
    elif N0 == N:
        res["verdict"] = ("CERTIFIED D = 0 over %.1f units at t ~ %.6g: "
                          "N_0 = N = %d, all zeros on the critical line, all "
                          "simple, all rigorously located." % (float(b - a), float(a), N))
    elif N0 < N:
        res["verdict"] = "INCOMPLETE: N = %d, isolated %d, D <= %d" % (N, N0, N - N0)
    else:
        res["verdict"] = ("INCONSISTENT: more disjoint zero balls (%d) than "
                          "the total count (%d); refusing all conclusions"
                          % (N0, N))
    print(res["verdict"], flush=True)
    print("smallest gap upper bounds (normalised):",
          ["%.4f" % r["delta_interval"][1] for r in res["smallest_gaps_by_upper_bound"][:5]],
          flush=True)

    if args.balls_out:
        with open(args.balls_out, "w") as fh:
            for lo, hi in balls:
                fh.write("%s %s\n" % (lo, hi))
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
