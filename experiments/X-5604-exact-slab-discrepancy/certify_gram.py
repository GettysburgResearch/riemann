#!/usr/bin/env python3
"""Self-contained certified sign-change counter: Gram points + adaptive refinement.

Agent: opus5-01   Issue: #55

`certify_parallel.py` needs a list of approximate zeros to place its samples,
which means running an uncertified Riemann–Siegel scanner first.  That list can
never manufacture a sign change, so the certificate was sound -- but it made the
pipeline depend on a second program, and it doubled the work, since the scanner
evaluates `Z` about sixteen times per zero and then the certifier evaluates it
again.

This version needs no scanner.  Sample positions come from **Gram points**,
`theta(g_n) = n pi`, which are available in closed form up to a Newton solve on
the Stirling series.  Gram's law -- that `Z` alternates in sign at consecutive
Gram points -- holds for most `n`, so most zeros are certified by one evaluation
each.  Where it fails, the two neighbouring samples share a sign, and the gap is
**subdivided adaptively** until the missing sign changes are found or a depth
budget is spent.

Nothing about Gram's law is assumed.  It is only a heuristic for *where to look*;
every reported sign is an Arb ball certified strictly on one side of zero, and a
failure of the heuristic costs evaluations, never correctness.  The output is a
rigorous lower bound on `N_0`, and comparing it to a rigorous `N` from
`slab_discrepancy.py` gives `D`.

The approximate Gram solve uses `mpmath` and is *not* part of the certificate:
a sample point is just a number at which `Z` is then certified.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import time
from fractions import Fraction as Fr
from multiprocessing import Pool

LADDER = (64, 96, 160, 256, 448)


def _sign_at(args):
    i, num, den = args
    from flint import acb, arb, ctx
    Z = None
    for p in LADDER:
        ctx.prec = p
        t = arb(num) / arb(den)
        if not t.is_exact():
            return (i, None, p, "sample not exact in arb")
        th = acb(arb(1) / 4, t / 2).lgamma().imag - (t / 2) * arb.pi().log()
        Z = (acb(0, th).exp() * acb(arb(1) / 2, t).zeta()).real
        if Z > 0:
            return (i, 1, p, None)
        if Z < 0:
            return (i, -1, p, None)
    return (i, None, LADDER[-1], Z.str(12, radius=True) if Z is not None else "?")


def gram_points(a: float, b: float):
    """Approximate Gram points in (a,b).  Heuristic only -- not certified.

    theta is monotone increasing with theta'(t) = (1/2) log(t/2pi), which is
    essentially constant across a short window, so linear interpolation in
    theta gives an initial guess good to many digits and two Newton steps
    finish it.  (findroot from a generic start is both slower and unreliable
    here, because theta ~ 3e14 while the window is only tens of units wide.)
    """
    from mpmath import mp, mpf, log, pi
    mp.dps = 30
    A, B = mpf(a), mpf(b)

    def theta(t):
        return (t / 2) * log(t / (2 * pi)) - t / 2 - pi / 8 + 1 / (48 * t) \
            + 7 / (5760 * t ** 3)

    def dtheta(t):
        return log(t / (2 * pi)) / 2

    ta, tb = theta(A), theta(B)
    n_lo = int(mp.floor(ta / pi)) + 1
    n_hi = int(mp.floor(tb / pi))
    out = []
    for n in range(n_lo, n_hi + 1):
        target = mpf(n) * pi
        t = A + (target - ta) / dtheta(A)          # linear in theta
        for _ in range(3):                          # Newton
            t = t - (theta(t) - target) / dtheta(t)
        tf = float(t)
        if a < tf < b:
            out.append(tf)
    return sorted(out)


def dyadic(x: float, bits: int) -> Fr:
    return Fr(round(x * (1 << bits)), 1 << bits)


def run(points, procs, bits):
    work = [(i, p.numerator, p.denominator) for i, p in enumerate(points)]
    res = [None] * len(points)
    with Pool(procs) as pool:
        for i, s, p, msg in pool.imap_unordered(_sign_at, work, chunksize=8):
            res[i] = (s, p, msg)
    return res


def count_changes(signs):
    changes, last = 0, None
    for s in signs:
        if s is None:
            last = None
            continue
        if last is not None and s != last:
            changes += 1
        last = s
    return changes


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--bits", type=int, default=24)
    ap.add_argument("--procs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--expected-N", type=int, default=None)
    ap.add_argument("--max-rounds", type=int, default=6)
    ap.add_argument("--label", default="")
    ap.add_argument("--out", default="certify-gram.json")
    args = ap.parse_args()

    a, b = Fr(args.a), Fr(args.b)
    af, bf = float(a), float(b)

    t0 = time.time()
    g = gram_points(af, bf)
    pts = sorted({dyadic(x, args.bits) for x in g})
    pts = [p for p in pts if a < p < b]
    print("%s slab (%.4f, %.4f) span %.1f  %d Gram samples  %d procs"
          % (args.label, af, bf, bf - af, len(pts), args.procs), flush=True)

    signs = run(pts, args.procs, args.bits)
    changes = count_changes([s[0] for s in signs])
    total_evals = len(pts)
    print("  round 0 (Gram): %d certified sign changes  [%.0f s]"
          % (changes, time.time() - t0), flush=True)

    rounds = [{"round": 0, "samples": len(pts), "changes": changes}]

    # Adaptive refinement: subdivide every adjacent same-sign (or undecided) gap.
    target = args.expected_N
    for r in range(1, args.max_rounds + 1):
        if target is not None and changes >= target:
            break
        new = []
        for i in range(len(pts) - 1):
            s1, s2 = signs[i][0], signs[i + 1][0]
            if s1 is not None and s2 is not None and s1 != s2:
                continue                       # already yields a sign change
            lo, hi = pts[i], pts[i + 1]
            for k in (1, 2, 3):                # three interior points
                m = lo + (hi - lo) * Fr(k, 4)
                m = dyadic(float(m), args.bits + 2 * r)
                if lo < m < hi:
                    new.append(m)
        # also probe outside the extreme Gram points
        if pts:
            new.append(dyadic((af + float(pts[0])) / 2, args.bits + 2 * r))
            new.append(dyadic((float(pts[-1]) + bf) / 2, args.bits + 2 * r))
        new = [p for p in new if a < p < b]
        if not new:
            break
        merged = sorted(set(pts) | set(new))
        signs = run(merged, args.procs, args.bits)
        pts = merged
        total_evals += len(new)
        changes = count_changes([s[0] for s in signs])
        print("  round %d: +%d samples -> %d certified sign changes  [%.0f s]"
              % (r, len(new), changes, time.time() - t0), flush=True)
        rounds.append({"round": r, "added": len(new), "samples": len(pts),
                       "changes": changes})

    dt = time.time() - t0
    undecided = [{"t": str(pts[i]), "Z": s[2]} for i, s in enumerate(signs)
                 if s[0] is None]

    res = {
        "schema": "riemann.x5604-certify-gram.v1",
        "agent": "opus5-01",
        "classification": "RIGOROUS lower bound on N_0. Sample POSITIONS come "
                          "from Gram points and adaptive bisection, which are "
                          "heuristics; every accepted SIGN is an Arb ball "
                          "strictly on one side of zero. No scanner, no "
                          "uncertified guide list, no assumption of Gram's law.",
        "label": args.label,
        "a": str(a), "b": str(b), "height": af, "span": bf - af,
        "total_samples": len(pts),
        "rounds": rounds,
        "undecided": undecided,
        "certified_sign_changes": changes,
        "N0_lower_bound": changes,
        "seconds": dt,
        "seconds_per_zero": dt / max(1, changes),
    }
    if args.expected_N is not None:
        N = args.expected_N
        res["N_total"] = N
        if changes > N:
            res["verdict"] = ("INCONSISTENT: certified N_0 >= %d exceeds "
                              "rigorous N = %d; concluding nothing."
                              % (changes, N))
        elif changes == N:
            res["D"] = 0
            res["verdict"] = ("CERTIFIED D = 0 over %.1f units at t ~ %.6g: "
                              "N_0 = N = %d, no zero off the critical line, "
                              "every zero simple. Unconditional."
                              % (bf - af, af, N))
        else:
            res["D_upper_bound"] = N - changes
            res["verdict"] = ("INCOMPLETE after %d rounds: N = %d, certified "
                              "N_0 >= %d, so D <= %d."
                              % (len(rounds) - 1, N, changes, N - changes))
        print(res["verdict"], flush=True)

    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("wrote %s  [%.0f s total]" % (args.out, dt), flush=True)


if __name__ == "__main__":
    main()
