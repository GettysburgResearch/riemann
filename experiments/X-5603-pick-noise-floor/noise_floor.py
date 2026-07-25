#!/usr/bin/env python3
"""Measure the noise floor of a 128-bit lambda_min screen on the PR #71 node grid.

Agent: opus5-01   Issue: #55

PR #71 nominates candidates by computing `lambda_min` of the 8x8 Pick matrix

    K_{jk} = ( F(s_j) + conj F(s_k) ) / (x_j + x_k),   s_j = 1/2 + x_j + iT,
    F = xi'/xi,   x = 2^-17, 2^-15, 2^-13, 2^-11, 2^-10, 2^-9, 2^-7, 2^-5,

from a 128-bit midpoint matrix, and flagging the ordinates where it comes out
negative.  Under RH, `K` is a Gram matrix and `lambda_min >= 0`, so a certified
negative would disprove RH.  Fifteen ordinates were flagged this way, the
strongest at `-2.626429492911995e-33`.

The question this experiment settles is not "is that particular number right?"
but the sharper one: **can a 128-bit screen on this grid produce an informative
sign at all?**  If the true `lambda_min` sits far below the rounding noise of a
128-bit evaluation, then the sign it reports is a coin flip, every nomination it
makes is uninformative, and no amount of escalating individual candidates
afterwards repairs the screen.

Method, which is direct rather than an error-propagation estimate:

 1. Evaluate `F` at the eight nodes at high precision, so that `lambda_min` is
    known to many more digits than any of the effects being measured.
 2. Perturb the eight values by independent relative errors of size `2^-p` --
    the model of a `p`-bit evaluation delivering one ulp -- and recompute
    `lambda_min` of the resulting Hermitian matrix.
 3. Repeat, and report the distribution: its spread is the noise floor, and the
    fraction of trials with `lambda_min < 0` is the screen's flag rate.

A screen is informative when the flag rate is near zero for an on-line ordinate.
A flag rate near one half means the screen is a random number generator.
"""
from __future__ import annotations

import argparse
import json
import os

from mpmath import mp, mpf, mpc, log, pi as mp_pi, digamma, zeta, mpmathify

XS = ["2^-17", "2^-15", "2^-13", "2^-11", "2^-10", "2^-9", "2^-7", "2^-5"]
T_NUM, T_DEN = 20225875608341108140435, 2 ** 32


def xval(tag):
    return mpf(2) ** int(tag.split("^")[1])


def F_of(s):
    """xi'/xi(s) = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) + zeta'/zeta(s)."""
    return (1 / s + 1 / (s - 1) - log(mp_pi) / 2 + digamma(s / 2) / 2
            + zeta(s, derivative=1) / zeta(s))


def load_or_compute(cache, dps):
    if os.path.exists(cache):
        with open(cache) as fh:
            d = json.load(fh)
        if d["dps"] >= dps:
            mp.dps = d["dps"]
            return [mpc(mpmathify(a), mpmathify(b)) for a, b in d["F"]]
    mp.dps = dps
    T = mpf(T_NUM) / mpf(T_DEN)
    out = []
    for tag in XS:
        s = mpc(mpf(1) / 2 + xval(tag), T)
        f = F_of(s)
        out.append(f)
        print("  x = %-6s  F = %s" % (tag, mp.nstr(f, 22)), flush=True)
    with open(cache, "w") as fh:
        json.dump({"dps": dps, "T": "%d/%d" % (T_NUM, T_DEN), "x": XS,
                   "F": [[mp.nstr(f.real, dps), mp.nstr(f.imag, dps)]
                         for f in out]}, fh, indent=1)
    return out


def pick_matrix(F):
    xs = [xval(t) for t in XS]
    n = len(xs)
    return [[(F[j] + mp.conj(F[k])) / (xs[j] + xs[k]) for k in range(n)]
            for j in range(n)]


def lam_min(M):
    return min(mp.eighe(mp.matrix(M))[0])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dps", type=int, default=60)
    ap.add_argument("--trials", type=int, default=400)
    ap.add_argument("--bits", type=int, nargs="+",
                    default=[128, 136, 144, 148, 152, 160, 176, 192])
    ap.add_argument("--seed", type=int, default=20250725)
    ap.add_argument("--cache", default="results/F-nodes.json")
    ap.add_argument("--out", default="results/noise-floor.json")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    print("evaluating xi'/xi at the eight nodes (dps=%d):" % args.dps, flush=True)
    F = load_or_compute(args.cache, args.dps)
    mp.dps = args.dps

    K = pick_matrix(F)
    lam_true = lam_min(K)
    ev = sorted(mp.eighe(mp.matrix(K))[0])
    print("\ntrue spectrum:")
    for e in ev:
        print("   ", mp.nstr(e, 14))
    print("cond = ", mp.nstr(ev[-1] / ev[0], 8))

    # A deterministic, reproducible pseudo-random source: no numpy, so that the
    # whole experiment runs inside mpmath at the working precision.
    import random
    rng = random.Random(args.seed)
    absF = [abs(f) for f in F]

    rows = []
    for p in args.bits:
        scale = mpf(2) ** (-p)
        neg = 0
        vals = []
        for _ in range(args.trials):
            pert = []
            for f, a in zip(F, absF):
                dre = mpf(rng.uniform(-1, 1))
                dim = mpf(rng.uniform(-1, 1))
                pert.append(f + a * scale * mpc(dre, dim))
            lm = lam_min(pick_matrix(pert))
            vals.append(lm)
            if lm < 0:
                neg += 1
        vals.sort()
        med = vals[len(vals) // 2]
        spread = (vals[int(0.84 * len(vals))] - vals[int(0.16 * len(vals))]) / 2
        rows.append({
            "bits": p,
            "flag_rate_lambda_min_negative": neg / args.trials,
            "median_lambda_min": mp.nstr(med, 10),
            "one_sigma_spread": mp.nstr(spread, 10),
            "min_seen": mp.nstr(vals[0], 10),
            "max_seen": mp.nstr(vals[-1], 10),
            "spread_over_true": float(spread / lam_true),
        })
        print("  p=%-4d flag rate %-7.3f  spread %-14s  (%.3g x true)"
              % (p, neg / args.trials, mp.nstr(spread, 6),
                 float(spread / lam_true)), flush=True)

    res = {
        "schema": "riemann.x5603-pick-noise-floor.v1",
        "agent": "opus5-01",
        "classification": "the true lambda_min is an ordinary high-precision "
                          "computation (not a directed interval); the noise "
                          "model is a simulation of p-bit rounding, not a "
                          "bound on any real implementation's error",
        "ordinate": "%d/%d" % (T_NUM, T_DEN),
        "nodes": XS,
        "working_dps": args.dps,
        "trials_per_precision": args.trials,
        "true_lambda_min": mp.nstr(lam_true, 20),
        "true_spectrum": [mp.nstr(e, 14) for e in ev],
        "condition_number": mp.nstr(ev[-1] / ev[0], 8),
        "reported_128bit_midpoint_lambda_min": -2.626429492911995e-33,
        "ladder": rows,
        "note": "flag rate is the fraction of simulated p-bit evaluations that "
                "report lambda_min < 0 at an ordinate whose true lambda_min is "
                "positive. 0.5 means the screen carries no information.",
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("\nwrote", args.out)


if __name__ == "__main__":
    main()
