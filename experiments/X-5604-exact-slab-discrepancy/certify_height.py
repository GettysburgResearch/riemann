#!/usr/bin/env python3
"""Drive a complete unconditional D = 0 certificate at a given height.

Agent: opus5-01   Issue: #55

Two steps, both rigorous:

  1. `N(a,b)` from Arb's `zeta_nzeros` -- the total number of zeros of zeta in
     the strip with `a < Im rho < b`, counted with multiplicity, on the line or
     off it.  Each endpoint is an exact dyadic and each count must isolate a
     unique integer.
  2. `N_0 >= (certified sign changes of Z)` from `certify_gram.py` -- Gram
     points and adaptive bisection to place samples, Arb ball arithmetic to
     certify each sign.

Since `N_0 <= N` always, `N_0 = N` forces `D = N - N_0 = 0`: no zero off the
critical line in the slab, and every zero in it simple.

Endpoints are `t0 + 1/2` and `t0 + span + 1/2`, chosen half-integral so that
they are exactly representable and unlikely to sit near a zero.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from fractions import Fraction as Fr

HERE = __file__.rsplit("/", 1)[0]


def frac_arg(f: Fr) -> str:
    return "%d/%d" % (f.numerator, f.denominator)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t0", required=True, type=str, help="integer base height")
    ap.add_argument("--span", required=True, type=int)
    ap.add_argument("--procs", type=int, default=3)
    ap.add_argument("--prec", type=int, default=192)
    ap.add_argument("--max-rounds", type=int, default=8)
    ap.add_argument("--tag", required=True)
    args = ap.parse_args()

    t0 = int(float(args.t0)) if "e" in args.t0.lower() else int(args.t0)
    a = Fr(2 * t0 + 1, 2)
    b = Fr(2 * (t0 + args.span) + 1, 2)
    label = "t=%.6g span=%d" % (t0, args.span)
    print("=== %s ===" % label, flush=True)

    slab_out = "%s/results/height-%s-slab.json" % (HERE, args.tag)
    t = time.time()
    r = subprocess.run([sys.executable, "-u", "%s/slab_discrepancy.py" % HERE,
                        "--a", frac_arg(a), "--b", frac_arg(b),
                        "--prec", str(args.prec), "--out", slab_out],
                       capture_output=True, text=True)
    print(r.stdout.strip(), flush=True)
    if r.returncode != 0:
        print("slab_discrepancy failed:\n" + r.stderr[-2000:], flush=True)
        sys.exit(1)
    with open(slab_out) as fh:
        N = json.load(fh)["N_total_in_slab"]
    print("  N = %d   [%.0f s]" % (N, time.time() - t), flush=True)

    gram_out = "%s/results/height-%s-gram.json" % (HERE, args.tag)
    r = subprocess.run([sys.executable, "-u", "%s/certify_gram.py" % HERE,
                        "--a", frac_arg(a), "--b", frac_arg(b),
                        "--procs", str(args.procs),
                        "--expected-N", str(N),
                        "--max-rounds", str(args.max_rounds),
                        "--label", label, "--out", gram_out],
                       capture_output=True, text=True)
    print(r.stdout.strip(), flush=True)
    if r.returncode != 0:
        print("certify_gram failed:\n" + r.stderr[-2000:], flush=True)
        sys.exit(1)

    with open(gram_out) as fh:
        g = json.load(fh)
    summary = {
        "schema": "riemann.x5604-height-certificate.v1",
        "agent": "opus5-01",
        "tag": args.tag, "t0": t0, "span": args.span,
        "a": frac_arg(a), "b": frac_arg(b),
        "N_total": N,
        "N0_certified_lower_bound": g["certified_sign_changes"],
        "D": (0 if g["certified_sign_changes"] == N else None),
        "D_upper_bound": N - g["certified_sign_changes"],
        "samples": g["total_samples"],
        "rounds": g["rounds"],
        "seconds_total": time.time() - t,
        "verdict": g.get("verdict"),
    }
    out = "%s/results/height-%s.json" % (HERE, args.tag)
    with open(out) if False else open(out, "w") as fh:
        json.dump(summary, fh, indent=1)
    print("TOTAL %.0f s -> %s" % (time.time() - t, out), flush=True)


if __name__ == "__main__":
    main()
