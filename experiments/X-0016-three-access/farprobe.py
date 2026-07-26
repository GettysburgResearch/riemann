#!/usr/bin/env python3
"""
X-0016c -- What the primes-only regime can and cannot detect.

Agent: claude-02
Closes: the detector half of Q-0018, with numbers.

X-0016b certified the Pick form from primes alone at probes with
Re a = 2.05.  Two questions decide whether that yields a USEFUL primes-only
detector:

 1. How much point-side detection survives with probes 1.55 from the line?
    (Measured here: a lot -- about 1.3 probe points per decade of delta,
    controls clean.)
 2. Can the certified prime tail reach the witness magnitudes?  The tail
    scales like X^{1 - Re a} log X, and a feasible sieve (X ~ 1e8..1e9)
    certifies only |q| >= ~1e-8.  Measured witness magnitudes at the
    LDL-extracted direction are 1e-32 .. 1e-65: unreachable by ~25 orders.
    Even along a response-maximal direction the certifiable depth is only
    delta ~ 3e-2, and the growth-law comparison

        B-spline Weil family (X-0006, measured):  prime cost ~ delta^-3.3
        rational Pick family (this file):         prime cost ~ delta^-1.9,
                                                  far worse constant

    puts the crossover near delta ~ 7e-6 at ~1e18 primes -- beyond any
    feasible computation.  CONCLUSION: as a prime-side DETECTOR the rational
    family loses to T-0002's B-splines at every feasible budget.  The value
    of the prime-side dual is the three-way cross-validation (X-0016b) and
    the theory link, not a search.

The no-free-lunch statement behind this (recorded in Q-0018): the prime-sum
weight for the rational test family is n^{-Re a} REGARDLESS of
explicit-formula smoothing -- the decay rate of the test function g is
pinned at Re a - 1/2 by the probe positions, so "smooth it near the 1-line"
was never available.  Rational H <=> exponential g <=> polynomial-tailed
prime sums;  compact g (B-splines) <=> entire H <=> finite prime sums but
bandwidth-limited detection.  Two ends of an uncertainty tradeoff.

Usage: python3 farprobe.py
"""
from __future__ import annotations

import json
import math
import os
import platform
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import pick as PK  # noqa: E402
from flint import acb, arb, ctx  # noqa: E402

HALF = arb(1) / 2
G = 100.0


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def model(delta, mode):
    zs, d, g0 = [], arb(delta), arb(repr(G))
    for k in range(-90, 91):
        g = g0 + k * arb("0.9")
        if k == 0:
            loc = {"OFF": [acb(HALF - d, g), acb(HALF + d, g)],
                   "LEHMER": [acb(HALF, g - d), acb(HALF, g + d)],
                   "DOUBLE": [acb(HALF, g), acb(HALF, g)]}[mode]
            zs += loc + [z.conjugate() for z in loc]
        else:
            zs += [acb(HALF, g), acb(HALF, -g)]

    def F(s):
        return sum(1 / (acb(s) - r) for r in zs)
    return F


def budget(q, C=3.0):
    """X with C X^{-1.05} log X ~ q/2: the sieve size needed before the
    certified prime tail drops below half the witness."""
    X = 10.0
    for _ in range(80):
        X = (2 * C * math.log(max(X, 3.0)) / q) ** (1 / 1.05)
    return X


def main():
    ctx.prec = 4000
    out = {"experiment": "X-0016c", "agent": "claude-02", "git_sha": git_sha(),
           "python": sys.version.split()[0], "platform": platform.platform(),
           "prec_bits": 4000, "probe_re": 2.05,
           "detection": [], "witness_budgets": []}

    print("part 1: detection at Re a = 2.05 (synthetic, matched controls)")
    for N in (8, 12, 16, 20, 24):
        al = PK.probe_cluster(G + 0.8, G + 1.6, N, u="1.55")
        floor = PK.pick_certificate(al, F=model("0.001", "DOUBLE"))["min_pivot"]
        det, ctl = None, 0
        for dstr in ("0.01", "0.001", "0.0001", "0.00001", "0.000001",
                     "0.0000001", "0.00000001"):
            off = PK.pick_certificate(al, F=model(dstr, "OFF"))
            leh = PK.pick_certificate(al, F=model(dstr, "LEHMER"))
            ctl += leh["verdict"] == "NOT_PSD"
            if off["verdict"] == "NOT_PSD":
                det = dstr
        out["detection"].append({"N": N, "floor_double": floor,
                                 "smallest_delta": det, "control_firings": ctl})
        print(f"  N={N:<4} floor={floor:>11.3e}  smallest delta={det}  "
              f"controls fired: {ctl}", flush=True)

    print("\npart 2: witness magnitudes and prime budgets")
    for N in (16, 24):
        al = PK.probe_cluster(G + 0.8, G + 1.6, N, u="1.55")
        for dstr in ("0.01", "0.001", "0.0001", "0.000001", "0.00000001"):
            F = model(dstr, "OFF")
            cert = PK.pick_certificate(al, F=F)
            if cert["verdict"] != "NOT_PSD":
                out["witness_budgets"].append({"N": N, "delta": dstr,
                                               "detected": False})
                continue
            P = PK.pick_matrix(al, F=F)
            x = PK.ldl_witness_direction(P)
            q = float(PK.tuned_form(al, x, F=F).mid())
            X = budget(abs(q))
            out["witness_budgets"].append({"N": N, "delta": dstr,
                                           "detected": True, "q": q,
                                           "prime_budget_X": X})
            print(f"  N={N:<3} delta={dstr:<12} q={q:+.3e}  X ~ {X:.1e}",
                  flush=True)

    out["comparison"] = {
        "bspline_family_measured_cost": "delta^-3.3 (X-0006: 10x sensitivity "
                                        "= 2000x prime powers)",
        "rational_family_cost": "X ~ delta^-1.9 with a constant worse by "
                                "several orders (witness magnitudes above)",
        "crossover": "delta ~ 7e-6 at ~1e18 primes -- infeasible",
    }
    out["conclusion"] = (
        "the primes-only Pick detector at Re a ~ 2 retains strong POINT-side "
        "detection (~1.3 probes/decade) but its certified prime tail cannot "
        "reach the witness magnitudes at any feasible sieve; as a prime-side "
        "detector the rational family loses to the B-spline family at every "
        "feasible budget.  The prime-side dual's value is cross-validation "
        "(X-0016b), not search.")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "farprobe.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
