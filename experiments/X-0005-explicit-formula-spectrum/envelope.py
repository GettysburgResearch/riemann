#!/usr/bin/env python3
"""
X-0005e -- Envelope vs oscillation: a consistency test between O-0001 and O-0002.

Agent: claude-01

O-0001 measures the *envelope* of the prime error term through the Nicolas
margin (fitted exponent `b = Theta - 1`).  O-0002 measures its *oscillation*
through the spectral lines (each line's amplitude grows like `X^delta`).  Both
are views of the same object,

    f(u) = (psi(e^u) - e^u) / e^{u/2}   =   - sum_rho e^{(rho - 1/2) u} / rho ,

so they must agree.  This file runs the cheapest possible version of the test.

By Parseval, the mean square of `f` over a window is (to leading order) half
the sum of the squared line amplitudes.  If every zero is on the critical line
`f` is almost periodic and its RMS is **constant** in `u`; a zero at
`Re = 1/2 + delta` makes the RMS grow like `e^{delta u}`.  So

    slope of log(RMS) against u   =   Theta - 1/2 ,

estimated directly from a prime sieve, with no zeta evaluation, no fitted line
positions, and no windowing subtleties -- a genuinely different statistic from
both O-0001 and O-0002.

WHAT THE TIGHT ERROR BAR IS NOT

This statistic aggregates ALL zeros, so its apparent precision is misleading as
a per-zero statement.  A single off-critical zero at height gamma contributes an
amplitude 2/|rho| e^{delta u}; for it to move the RMS (which is ~0.22, the
combined effect of every zero) it must first come to dominate that sum.  At
gamma ~ 100, 2/|rho| ~ 0.02, so over the ~10 units of u available it needs
e^{10 delta} >~ 11, i.e. delta >~ 0.24.

So: the aggregate exponent is pinned to +/- 0.007, but the *per-zero* displacement
this test could detect is an order of magnitude WORSE than the per-line test of
X-0005d (~0.013).  Tight error bars on an aggregate are not tight bounds on a
component.  Quote this as a consistency check between O-0001 and O-0002, which
is what it is, and not as a bound on Theta.

STATUS: EMPIRICAL.  Floating point, finite sieve.  Like every other screen here
it can be fooled by a long quiet stretch (the Omega-versus-limsup problem noted
in O-0001), so a null result is consistency, not evidence.

Usage: python3 envelope.py [X] [nwindows]
"""
from __future__ import annotations

import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from run import psi_samples  # noqa: E402


def main():
    X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 4 * 10**7
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    ulo, uhi = math.log(1000.0), math.log(X)
    n = 24000
    us = [ulo + (uhi - ulo) * i / (n - 1) for i in range(n)]
    psis = psi_samples(X, us)
    f = [(p - math.exp(u)) / math.exp(u / 2) for u, p in zip(us, psis)]

    per = n // K
    rows = []
    for k in range(K):
        seg = f[k * per:(k + 1) * per]
        useg = us[k * per:(k + 1) * per]
        rms = math.sqrt(sum(v * v for v in seg) / len(seg))
        rows.append({"u_centre": (useg[0] + useg[-1]) / 2,
                     "x_centre": math.exp((useg[0] + useg[-1]) / 2),
                     "rms": rms})

    xs = [r["u_centre"] for r in rows]
    ys = [math.log(r["rms"]) for r in rows]
    m = len(xs)
    mx, my = sum(xs) / m, sum(ys) / m
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum(
        (x - mx) ** 2 for x in xs)
    # crude scatter of the residuals -> a rough uncertainty on the slope
    resid = [y - (my + slope * (x - mx)) for x, y in zip(xs, ys)]
    sd = math.sqrt(sum(r * r for r in resid) / max(1, m - 2))
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    slope_err = sd / sx if sx else float("nan")

    print(f"X = {X:.3g}, {K} windows of width {(uhi-ulo)/K:.3f} in u")
    for r in rows:
        print(f"  x ~ {r['x_centre']:12.3e}   RMS f = {r['rms']:.4f}")
    print(f"\n  slope of log(RMS) vs u  =  {slope:+.5f} +/- {slope_err:.5f}")
    print(f"  => Theta - 1/2 estimated at {slope:+.5f}, i.e. Theta ~ "
          f"{0.5 + slope:.5f}")
    print("  (RH predicts slope 0, Theta = 1/2)")

    out = {"experiment": "X-0005e", "agent": "claude-01", "status": "EMPIRICAL",
           "X": X, "n_windows": K, "windows": rows,
           "slope_log_rms_vs_u": slope, "slope_stderr": slope_err,
           "Theta_estimate": 0.5 + slope,
           "consistency": "O-0001 fits the envelope via the Nicolas margin "
                          "(b = Theta - 1); O-0002 fits the oscillation via "
                          "spectral line amplitudes; this fits the RMS. All "
                          "three are views of the same error term and must "
                          "agree.",
           "caveat": "a finite computation cannot bound Theta from below "
                     "(Omega-results are about limsup); a null result here is "
                     "consistency, not evidence",
           "sensitivity_caveat": "this statistic aggregates all zeros: a single "
                     "off-critical zero at gamma ~ 100 would need delta >~ 0.24 "
                     "to move the RMS, an order of magnitude WORSE than the "
                     "per-line test of X-0005d. Tight error bars on an aggregate "
                     "are not tight bounds on a component."}
    with open(os.path.join(HERE, "results", f"envelope-X{X}.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote results/envelope-X%d.json" % X)


if __name__ == "__main__":
    main()
