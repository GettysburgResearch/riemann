#!/usr/bin/env python3
"""How much height does ONE D-0801 pass actually cover?

Agent: opus5-01   Issue: #55

`optimal_detection.py` answers "how small a displacement could this carrier
detect, at the best possible offset `u`?" and returns a single number
(`eta_min = 0.0315` at the production parameters).  That number is encouraging
in isolation and misleading in context, because it is attained only at one
offset.  The question that decides whether the whole route is a viable *search*
is different:

    for how many units of height u does eta_min(u) stay below the admissible
    ceiling |eta| < 1/2 ?

That measure -- call it the pass coverage `m` -- converts a per-pass cost into a
cost per unit height, which is the only quantity that can be compared against
other methods.  A pass costing `C` seconds and covering `m` units of height runs
at `C/m` seconds per unit; Turing's method runs at its own rate and detects ANY
eta > 0 rather than only eta > eta_min(u).  Whichever number is smaller decides
where compute should go.

The machinery is L-5604's: near the carrier the exact form responds to a
quadruple `{1/2 +- eta +- i(T+u)}` as

    v^* Q v  -  eta^2 v^* M''(u) v  +  O(eta^4),      M'' = C S C^*  (rank <= 3)

so the family can be driven negative at offset `u` exactly when

    eta^2 > 1 / lambda_max( S C^* Q^{-1} C ) =: eta_min(u)^2 .

This module evaluates `eta_min(u)` on a fine grid spanning several mean zero
spacings and reports the measure of the sub-level sets.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

import numpy as np
from mpmath import mp, mpf, log, pi as mp_pi

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analyze_stream as A                                    # noqa: E402
import archimedean_block as AB                                # noqa: E402
import archimedean_asymptotic as AA                           # noqa: E402
from optimal_detection import beta_and_derivs                 # noqa: E402


def sublevel_measure(us, etas, thr):
    """Measure of {u : eta_min(u) <= thr}, by linear interpolation of crossings."""
    below = etas <= thr
    if not below.any():
        return 0.0, []
    du = us[1] - us[0]
    total = float(below.sum()) * du
    # collect the maximal runs, for reporting the window structure
    runs, start = [], None
    for i, b in enumerate(below):
        if b and start is None:
            start = i
        elif not b and start is not None:
            runs.append((float(us[start]), float(us[i - 1])))
            start = None
    if start is not None:
        runs.append((float(us[start]), float(us[-1])))
    return total, runs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("stream")
    ap.add_argument("--carrier-num", type=int, required=True)
    ap.add_argument("--carrier-den", type=int, required=True)
    ap.add_argument("--u-range", type=float, default=6.0)
    ap.add_argument("--u-points", type=int, default=3001)
    ap.add_argument("--pass-seconds", type=float, default=316.0,
                    help="wall time of the prime pass this coverage refers to")
    ap.add_argument("--out", default="detection-coverage.json")
    args = ap.parse_args()

    st = A.load_stream(args.stream)
    k, cutoff = st["cells"], st["cutoff"]

    mp.dps = 40
    L = log(mpf(cutoff))
    delta = float(L / (2 * mp_pi))
    h = delta / k
    centers = -delta / 2 + (np.arange(k) + 0.5) * h
    T = args.carrier_num / args.carrier_den
    ell_T = math.log(T / (2 * math.pi)) / (2 * math.pi)
    mean_spacing = 1.0 / ell_T

    za, _r, _b, _o, _p = AA.asymptotic_lags(cutoff, k, args.carrier_num,
                                            args.carrier_den, 3)
    z1, shift, _bb, _oo = AA.lag_one_and_diagonal(cutoff, k, args.carrier_num,
                                                  args.carrier_den, 3)
    za[1] = z1
    gate = A.correction_gate(cutoff, k, args.carrier_num, args.carrier_den)
    q = (AB.archimedean_matrix(gate["ell_T_float"] + shift, za)
         + AB.pole_matrix(cutoff, k, T)
         - A.toeplitz_matrix(st))
    q = 0.5 * (q + q.conj().T)
    lam_min = float(np.linalg.eigvalsh(q)[0])
    assert lam_min > 0, "Q is not positive definite; the L-5604 reduction needs Q > 0"
    qinv = np.linalg.inv(q)

    s3 = np.array([[0, 0, 1], [0, 2, 0], [1, 0, 0]], dtype=np.complex128)
    us = np.linspace(-args.u_range, args.u_range, args.u_points)
    etas = np.empty(len(us))
    for i, u in enumerate(us):
        b0, b1, b2 = beta_and_derivs(float(u), centers, h)
        cmat = np.stack([np.conj(b0), np.conj(b1), np.conj(b2)], axis=1)
        ev = np.linalg.eigvals(s3 @ (cmat.conj().T @ (qinv @ cmat))).real
        lam = float(ev.max())
        etas[i] = math.sqrt(1.0 / lam) if lam > 0 else math.inf

    thresholds = [0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01]
    cov = {}
    for thr in thresholds:
        m, runs = sublevel_measure(us, etas, thr)
        cov[str(thr)] = {
            "coverage_in_t": m,
            "coverage_in_mean_spacings": m / mean_spacing,
            "fraction_of_scanned_range": m / (2 * args.u_range),
            "n_windows": len(runs),
            "windows": runs[:12],
            "seconds_per_unit_height": (args.pass_seconds / m) if m > 0 else None,
        }

    finite = etas[np.isfinite(etas)]
    res = {
        "schema": "riemann.x5601-detection-coverage.v1",
        "agent": "opus5-01",
        "classification": "floating throughout; the blocks are assembled by "
                          "L-5603 in ordinary arithmetic and the response is "
                          "the leading term of an eta-expansion. The claim is "
                          "the order of magnitude of the coverage, not digits.",
        "cutoff": cutoff, "cells": k,
        "carrier": f"{args.carrier_num}/{args.carrier_den}",
        "T": T, "ell_T": ell_T, "mean_spacing": mean_spacing,
        "Delta": delta, "h": h,
        "nyquist_ratio_Delta_over_ellT": delta / ell_T,
        "lambda_min_exact_form": lam_min,
        "u_range_scanned": args.u_range,
        "eta_min_global": float(finite.min()) if len(finite) else None,
        "eta_min_argmin_u": float(us[int(np.argmin(etas))]),
        "eta_min_median_over_u": float(np.median(finite)) if len(finite) else None,
        "pass_seconds": args.pass_seconds,
        "coverage_by_threshold": cov,
        "note": "coverage at threshold 0.5 is the ONLY physically meaningful "
                "one, since |Re rho - 1/2| < 1/2 for every nontrivial zero: "
                "outside that set the pass cannot fire for any admissible "
                "displacement whatsoever.",
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
