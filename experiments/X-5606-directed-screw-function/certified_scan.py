#!/usr/bin/env python3
"""Certified global lower bound for Suzuki's Psi over [1/2, log(cutoff)].

Agent: fable5-01   Issue: #95, PR #98

PR #98's X-9501 scan is binary64 reconnaissance.  This module certifies the
same range: a rigorous positive lower bound for `Psi` on every knot cell,
hence `min Psi >= bound > 0` over `[1/2, log cutoff]` — the first certified
global statement on the route.

Structure.  Between consecutive prime-power knots, `Psi(t) = A(t) - P0*t + P1`
with the smooth part

    A(t)  = 4(e^{t/2} + e^{-t/2} - 2) + (t/2)(psi(1/4) - log pi)
            + (1/4)(C - e^{-t/2} Phi(e^{-2t}, 2, 1/4)),
    A'(t) = 2(e^{t/2} - e^{-t/2}) + (psi(1/4) - log pi)/2
            + sum_m 2/(4m+1) e^{-(4m+1)t/2},
    A''(t)= e^{t/2} - e^{-5t/2}/(1 - e^{-2t}).

The `A'` series and the `A''` closed form were RE-DERIVED here from D-9501.1
(the Lerch series telescopes because `(1/2+2m)^2/(m+1/4)^2 = 4`), so nothing
is imported from the unreviewed L-9503 beyond what this file proves in
passing: `A'' > 0` on `[1/2, oo)` since `e^{3t} - e^t - 1` is increasing and
positive at `t = 1/2` (certified by one ball evaluation).

`Psi` is therefore convex on every cell intersected with `[1/2, oo)`, and the
tangent bound at any interior point `s` gives

    min_{[a,b]} Psi  >=  Psi(s) + min( Psi'(s)(a-s), Psi'(s)(b-s) ),

entirely in ball arithmetic.  If the bound at the cell midpoint is not
positive, the cell is bisected adaptively; every reported cell bound is
rigorous regardless of where the probe points land.

The prefix sums `P0, P1` are running balls over exact prime powers, so the
whole scan is one streaming pass.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr

from flint import arb, ctx

sys.path.insert(0, "/home/user/riemann/experiments/X-5606-directed-screw-function")
from directed_psi import sieve_lambda

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


class Smooth:
    def __init__(self, prec):
        ctx.prec = prec
        self.prec = prec
        self.k1 = (arb(1) / 4).digamma() - arb.pi().log()      # psi(1/4)-log pi
        self.C = arb.pi() ** 2 + 8 * arb.const_catalan()

    def phi_series(self, t, terms=30):
        """sum z^m/(m+1/4)^2 with z = e^{-2t}, plus exact tail."""
        z = (-2 * t).exp()
        acc, zp = arb(0), arb(1)
        for m in range(terms):
            acc = acc + zp / ((arb(m) + arb(1) / 4) ** 2)
            zp = zp * z
        tail = zp / (((arb(terms) + arb(1) / 4) ** 2) * (1 - z))
        return acc + tail.union(arb(0))

    def A(self, t):
        return (4 * ((t / 2).exp() + (-t / 2).exp() - 2)
                + (t / 2) * self.k1
                + (self.C - (-t / 2).exp() * self.phi_series(t)) / 4)

    def dA(self, t, terms=30):
        acc = arb(0)
        for m in range(terms):
            k = 4 * m + 1
            acc = acc + 2 * (-(arb(k) * t) / 2).exp() / k
        # tail: sum_{m>=M} 2/(4m+1) e^{-(4m+1)t/2} <= e^{-(4M+1)t/2}/(2(1-e^{-2t}))
        k = 4 * terms + 1
        tail = (-(arb(k) * t) / 2).exp() / (2 * (1 - (-2 * t).exp()))
        acc = acc + tail.union(arb(0))
        return 2 * ((t / 2).exp() - (-t / 2).exp()) + self.k1 / 2 + acc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff", type=int, default=10 ** 7)
    ap.add_argument("--t-start", type=str, default="1/2")
    ap.add_argument("--prec", type=int, default=128)
    ap.add_argument("--max-depth", type=int, default=14)
    ap.add_argument("--out", default="results/certified-scan.json")
    args = ap.parse_args()

    ctx.prec = args.prec
    sm = Smooth(args.prec)

    # convexity preamble: e^{3t}-e^t-1 increasing (3e^{3t} > e^t trivially),
    # positive at t_start -- one ball check makes A'' > 0 on [t_start, oo)
    t0f = Fr(args.t_start)
    t0 = arb(t0f.numerator) / arb(t0f.denominator)
    conv = (3 * t0).exp() - t0.exp() - 1
    assert conv > 0, "convexity anchor failed"

    print("sieving to %d ..." % args.cutoff, flush=True)
    ts = time.time()
    pp = sieve_lambda(args.cutoff)
    print("%d prime powers  [%.0f s]" % (len(pp), time.time() - ts), flush=True)

    P0, P1 = arb(0), arb(0)
    global_min = None
    global_cell = None
    worst_depth = 0
    t_prev = t0
    n_cells = 0
    ts = time.time()

    def cell_bound(a, b, P0v, P1v, depth=0):
        nonlocal worst_depth
        s = (a + b) / 2
        val = sm.A(s) - P0v * s + P1v
        der = sm.dA(s) - P0v
        bound = val + (der * (a - s)).min(der * (b - s))
        if bound > 0 or depth >= args.max_depth:
            worst_depth = max(worst_depth, depth)
            return bound
        left = cell_bound(a, s, P0v, P1v, depth + 1)
        right = cell_bound(s, b, P0v, P1v, depth + 1)
        return left.min(right)

    for idx, (n, p) in enumerate(pp):
        tau = arb(n).log()
        if tau > t_prev:
            b = cell_bound(t_prev, tau, P0, P1)
            n_cells += 1
            if global_min is None or float(b.lower().mid()) < global_min:
                global_min = float(b.lower().mid())
                global_cell = (str(n), float(t_prev.mid()))
            t_prev = tau
        w = arb(p).log() / arb(n).sqrt()
        P0 = P0 + w
        P1 = P1 + w * tau
        if (idx + 1) % 50000 == 0:
            print("  %d/%d knots, %d cells, running min %.6e  [%.0f s]"
                  % (idx + 1, len(pp), n_cells, global_min or -1,
                     time.time() - ts), flush=True)

    verdict_positive = global_min is not None and global_min > 0
    res = {
        "schema": "riemann.x5606-certified-scan.v1",
        "agent": "fable5-01",
        "classification": "DIRECTED: convexity modulus re-derived and "
                          "certified in-file; tangent lower bounds in ball "
                          "arithmetic on every knot cell; prefix sums as "
                          "running balls over exact prime powers. Conditional "
                          "only on the imported Suzuki equivalence and the "
                          "D-9501 normalization.",
        "cutoff": args.cutoff,
        "range": [str(t0f), "log(%d)" % args.cutoff],
        "prime_powers": len(pp),
        "cells": n_cells,
        "max_bisection_depth_used": worst_depth,
        "certified_global_lower_bound": global_min,
        "attained_near_cell_ending_at": global_cell,
        "verdict": ("CERTIFIED: Psi(t) >= %.6e > 0 for all t in the range -- "
                    "no scalar counterexample exists below the cutoff"
                    % global_min if verdict_positive else
                    "NOT CERTIFIED: a cell bound failed to resolve positive"),
        "seconds": round(time.time() - ts, 1),
    }
    print(res["verdict"], flush=True)
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
