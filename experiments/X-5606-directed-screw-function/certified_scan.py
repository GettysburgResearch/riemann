#!/usr/bin/env python3
"""Certified lower bound for Suzuki's Psi over [t_start, log(cutoff)].

Audit repair, 2026-07-27:

* the original scanner stopped at the last prime-power knot and omitted the
  terminal interval to ``log(cutoff)`` whenever the cutoff was not itself a
  prime power;
* the repaired scanner evaluates that terminal cell with the final prefix sums;
* the verdict requires explicit complete coverage and positivity of every cell;
* the exact binary lower endpoint is retained instead of relying only on a
  binary64 copy;
* imports are relative to this experiment directory instead of a fixed home
  path.

The analytic structure remains the one used by the original producer. Between
consecutive prime-power knots,

    Psi(t) = A(t) - P0*t + P1,

and A is strictly convex for t >= 1/2. A tangent at any interior point supplies
a rigorous lower bound on the whole cell. All special-function and accumulated
quantities are Arb balls.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from directed_psi import sieve_lambda

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


class Smooth:
    def __init__(self, prec):
        ctx.prec = prec
        self.prec = prec
        self.k1 = (arb(1) / 4).digamma() - arb.pi().log()
        self.C = arb.pi() ** 2 + 8 * arb.const_catalan()

    def phi_series(self, t, terms=30):
        """Enclose sum z^m/(m+1/4)^2, z=exp(-2t), with a positive tail."""
        z = (-2 * t).exp()
        acc, zp = arb(0), arb(1)
        for m in range(terms):
            acc = acc + zp / ((arb(m) + arb(1) / 4) ** 2)
            zp = zp * z
        tail = zp / (((arb(terms) + arb(1) / 4) ** 2) * (1 - z))
        return acc + tail.union(arb(0))

    def A(self, t):
        return (
            4 * ((t / 2).exp() + (-t / 2).exp() - 2)
            + (t / 2) * self.k1
            + (self.C - (-t / 2).exp() * self.phi_series(t)) / 4
        )

    def dA(self, t, terms=30):
        acc = arb(0)
        for m in range(terms):
            k = 4 * m + 1
            acc = acc + 2 * (-(arb(k) * t) / 2).exp() / k
        # For m>=M, 2/(4m+1) <= 1/2 and successive exponentials differ by
        # exp(-2t), giving this positive geometric tail enclosure.
        k = 4 * terms + 1
        tail = (-(arb(k) * t) / 2).exp() / (2 * (1 - (-2 * t).exp()))
        acc = acc + tail.union(arb(0))
        return 2 * ((t / 2).exp() - (-t / 2).exp()) + self.k1 / 2 + acc


def exact_binary_point(value):
    """Serialize an exact Arb endpoint as one rational binary number."""
    mantissa, exponent = value.man_exp()
    mantissa = int(mantissa)
    exponent = int(exponent)
    if exponent >= 0:
        numerator = mantissa << exponent
        denominator = 1
    else:
        numerator = mantissa
        denominator = 1 << (-exponent)
        while numerator and numerator % 2 == 0:
            numerator //= 2
            denominator //= 2
    return {
        "numerator": str(numerator),
        "denominator": str(denominator),
        "mantissa": str(mantissa),
        "exponent": exponent,
    }


def terminal_cell_needed(last_prime_power: int | None, cutoff: int) -> bool:
    """Whether [last knot, log(cutoff)] is a nonempty terminal cell."""
    return last_prime_power is None or last_prime_power < cutoff


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff", type=int, default=10**7)
    ap.add_argument("--t-start", type=str, default="1/2")
    ap.add_argument("--prec", type=int, default=128)
    ap.add_argument("--max-depth", type=int, default=14)
    ap.add_argument("--out", default="results/certified-scan.json")
    args = ap.parse_args()
    if args.cutoff < 2:
        raise SystemExit("cutoff must be at least 2")

    ctx.prec = args.prec
    sm = Smooth(args.prec)

    t0f = Fr(args.t_start)
    t0 = arb(t0f.numerator) / arb(t0f.denominator)
    t_end = arb(args.cutoff).log()
    if not (t0 < t_end):
        raise SystemExit("t_start must be strictly below log(cutoff)")

    # A''>0 iff exp(3t)-exp(t)-1>0. This function is increasing for t>=1/2.
    conv = (3 * t0).exp() - t0.exp() - 1
    if not (conv > 0):
        raise SystemExit("convexity anchor failed")

    print(f"sieving to {args.cutoff} ...", flush=True)
    sieve_started = time.time()
    pp = sieve_lambda(args.cutoff)
    print(
        f"{len(pp)} prime powers  [{time.time() - sieve_started:.0f} s]",
        flush=True,
    )

    P0, P1 = arb(0), arb(0)
    global_lower = None
    global_bound = None
    global_cell = None
    all_cells_positive = True
    worst_depth = 0
    t_prev = t0
    n_cells = 0
    scan_started = time.time()

    def cell_bound(a, b, P0v, P1v, depth=0):
        nonlocal worst_depth
        if not (a < b):
            raise RuntimeError("attempted to bound a nonpositive-width cell")
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

    def record_cell(bound, start_label, end_label):
        nonlocal global_lower, global_bound, global_cell
        nonlocal all_cells_positive, n_cells
        n_cells += 1
        if not (bound > 0):
            all_cells_positive = False
        lower = bound.lower()
        if global_lower is None or lower < global_lower:
            global_lower = lower
            global_bound = bound
            global_cell = {
                "start": start_label,
                "end": end_label,
            }

    last_n = None
    for idx, (n, p) in enumerate(pp):
        if n > args.cutoff:
            raise RuntimeError("sieve emitted a prime power above the cutoff")
        tau = arb(n).log()
        if tau > t_prev:
            bound = cell_bound(t_prev, tau, P0, P1)
            record_cell(bound, str(t_prev), f"log({n})")
            t_prev = tau
        w = arb(p).log() / arb(n).sqrt()
        P0 = P0 + w
        P1 = P1 + w * tau
        last_n = n
        if (idx + 1) % 50000 == 0:
            running = float(global_lower.mid()) if global_lower is not None else -1.0
            print(
                f"  {idx + 1}/{len(pp)} knots, {n_cells} cells, "
                f"running min {running:.6e}  "
                f"[{time.time() - scan_started:.0f} s]",
                flush=True,
            )

    final_cell_added = terminal_cell_needed(last_n, args.cutoff)
    if final_cell_added:
        # This interval was absent from the original implementation whenever
        # cutoff was not itself a prime power (including cutoff=10^7).
        bound = cell_bound(t_prev, t_end, P0, P1)
        record_cell(bound, str(t_prev), f"log({args.cutoff})")
        t_prev = t_end

    coverage_complete = (
        n_cells > 0
        and (
            (last_n == args.cutoff and not final_cell_added)
            or (last_n is None and final_cell_added)
            or (last_n is not None and last_n < args.cutoff and final_cell_added)
        )
    )
    verdict_positive = (
        coverage_complete
        and all_cells_positive
        and global_lower is not None
        and global_lower > 0
    )

    result = {
        "schema": "riemann.x5606-certified-scan.v2",
        "agent": "fable5-01; terminal-cell audit repair by gpt56-06-g",
        "classification": (
            "Directed convex-cell lower bounds over exact prime-power prefix "
            "balls. Conditional on the imported Suzuki equivalence and the "
            "D-9501 normalization."
        ),
        "cutoff": args.cutoff,
        "range": [str(t0f), f"log({args.cutoff})"],
        "prime_powers": len(pp),
        "last_prime_power": last_n,
        "terminal_cell_added": final_cell_added,
        "coverage_complete": coverage_complete,
        "cells": n_cells,
        "all_cells_strictly_positive": all_cells_positive,
        "max_bisection_depth_used": worst_depth,
        "certified_global_lower_bound_binary": (
            exact_binary_point(global_lower) if global_lower is not None else None
        ),
        "certified_global_lower_bound_ball": (
            str(global_bound) if global_bound is not None else None
        ),
        "certified_global_lower_bound_float_diagnostic": (
            float(global_lower.mid()) if global_lower is not None else None
        ),
        "attained_near_cell": global_cell,
        "verdict": (
            "CERTIFIED_POSITIVE_COMPLETE_RANGE"
            if verdict_positive
            else "NOT_CERTIFIED_COMPLETE_RANGE"
        ),
        "seconds": round(time.time() - scan_started, 1),
        "audit_note": (
            "Version 1 omitted the terminal interval after the last prime-power "
            "knot whenever cutoff was not itself a prime power. No v1 global "
            "range verdict is retained without this repaired replay."
        ),
    }
    print(result["verdict"], flush=True)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"wrote {output}", flush=True)


if __name__ == "__main__":
    main()
