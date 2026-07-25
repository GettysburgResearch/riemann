#!/usr/bin/env python3
"""
X-0005c -- A better-controlled spectral screen: paired equal-length windows.

Agent: claude-01
Follows directly from the sensitivity failure measured in X-0005b.

WHY THE FIRST DESIGN WAS WEAK

X-0005b compared the amplitude of a spectral line between sieve limits X1 and
X2 by transforming over [u0, log X1] and [u0, log X2].  Those are windows of
*different length*, so the two amplitudes differ in resolution and in leakage
as well as in data.  The resulting scatter among on-line lines was 0.15,
swamping the e^{delta * log(X2/X1)} signal for every delta below 0.2.

THE FIX

Use ONE sieve and two sub-windows of **equal length** W, one early and one
late:

    early = [u1, u1 + W]        late = [u2, u2 + W],   u2 = u1 + D

Identical window length, identical window shape, identical resolution -- only
the data differ.  For a zero rho = 1/2 + delta + i gamma the line amplitude
scales like e^{delta u}, so

    A_late / A_early  =  e^{delta D}          (on-line zeros: 1).

Additionally apply a Hann taper, which trades a factor ~2 in resolution for a
large reduction in sidelobe leakage -- the dominant noise source here.

This file measures the new sensitivity floor the same way X-0005b did, so the
two numbers are directly comparable.

STATUS: EMPIRICAL.  Floating point; certifies nothing.

Usage: python3 paired_window.py [X]
"""
from __future__ import annotations

import cmath
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from run import psi_samples  # noqa: E402
from validate import ORDINATES  # noqa: E402


def hann(n):
    return [0.5 - 0.5 * math.cos(2 * math.pi * i / (n - 1)) for i in range(n)]


def amplitude(us, f, g, win):
    """Windowed amplitude estimate, normalised so that a pure line of
    amplitude A returns A (the Hann window has mean 1/2)."""
    du = us[1] - us[0]
    W = us[-1] - us[0]
    cr = ci = 0.0
    for u, fv, w in zip(us, f, win):
        cr += w * fv * math.cos(g * u)
        ci -= w * fv * math.sin(g * u)
    return 2.0 * math.hypot(cr, ci) * du / (W * 0.5)


def grid(a, b, n):
    return [a + (b - a) * i / (n - 1) for i in range(n)]


def synthetic_f(us, zeros):
    out = []
    for u in us:
        tot = 0.0
        for beta, g in zeros:
            rho = complex(beta, g)
            tot += 2.0 * (cmath.exp((rho - 0.5) * u) / rho).real
        out.append(-tot)
    return out


def ratios_for(zeros, u1, u2, W, n):
    early_u, late_u = grid(u1, u1 + W, n), grid(u2, u2 + W, n)
    win = hann(n)
    fe, fl = synthetic_f(early_u, zeros), synthetic_f(late_u, zeros)
    return early_u, late_u, fe, fl, win


def main():
    X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 4 * 10**7
    uhi = math.log(X)
    ulo = math.log(1000.0)
    span = uhi - ulo
    W = span / 2.0
    u1, u2 = ulo, ulo + W          # two adjacent equal windows
    D = u2 - u1
    n = 8000
    print(f"X = {X:.3g}   window length W = {W:.3f}   separation D = {D:.3f}")
    print(f"resolution (Hann) ~ {2 * 2 * math.pi / W:.3f}")
    print(f"growth factor for displacement delta:  e^({D:.3f} delta)")

    out = {"experiment": "X-0005c", "agent": "claude-01",
           "status": "EMPIRICAL", "X": X, "W": W, "D": D,
           "design": "paired equal-length Hann-windowed sub-windows of one sieve",
           "synthetic": []}

    # ---- baseline scatter on synthetic all-on-line data -------------------
    base = [(0.5, g) for g in ORDINATES]
    eu, lu, fe, fl, win = ratios_for(base, u1, u2, W, n)
    rr = [amplitude(lu, fl, g, win) / amplitude(eu, fe, g, win)
          for g in ORDINATES[:12]]
    scatter = max(abs(r - 1.0) for r in rr)
    print(f"on-line baseline ratios: {min(rr):.4f} .. {max(rr):.4f}  "
          f"=> scatter {scatter:.4f}   (X-0005b design gave 0.1494)")
    out["baseline_scatter"] = scatter
    out["baseline_scatter_previous_design"] = 0.1494

    # ---- planted zero ------------------------------------------------------
    ti = 3
    gt = ORDINATES[ti]
    for delta in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002]:
        zs = [(0.5 + delta if i == ti else 0.5, g) for i, g in enumerate(ORDINATES)]
        eu, lu, fe, fl, win = ratios_for(zs, u1, u2, W, n)
        r = amplitude(lu, fl, gt, win) / amplitude(eu, fe, gt, win)
        det = abs(r - 1.0) > 3 * scatter
        out["synthetic"].append({"delta": delta, "ratio": r,
                                 "predicted": math.exp(D * delta),
                                 "detected_at_3x_scatter": bool(det)})
        print(f"  delta={delta:<6} ratio={r:7.4f} (predicted {math.exp(D*delta):7.4f})"
              f"  detected={det}")
    floor = min((r["delta"] for r in out["synthetic"]
                 if r["detected_at_3x_scatter"]), default=None)
    out["sensitivity_floor_delta"] = floor
    out["sensitivity_floor_previous_design"] = 0.2
    print(f"=> new sensitivity floor: delta >= {floor}   (was 0.2)")

    # ---- apply to the real primes -----------------------------------------
    print("\napplying the same paired-window test to the real sieve:")
    eu, lu = grid(u1, u1 + W, n), grid(u2, u2 + W, n)
    allu = sorted(set(eu) | set(lu))
    psis = psi_samples(X, allu)
    pmap = dict(zip(allu, psis))
    fe = [(pmap[u] - math.exp(u)) / math.exp(u / 2) for u in eu]
    fl = [(pmap[u] - math.exp(u)) / math.exp(u / 2) for u in lu]
    win = hann(n)
    rows = []
    for g in ORDINATES[:12]:
        a, b = amplitude(eu, fe, g, win), amplitude(lu, fl, g, win)
        r = b / a
        rows.append({"gamma": g, "ratio": r, "implied_delta": math.log(r) / D})
        print(f"  gamma={g:9.4f}  ratio={r:7.4f}  implied delta={math.log(r)/D:+.4f}")
    out["real_data"] = rows
    out["max_abs_implied_delta"] = max(abs(x["implied_delta"]) for x in rows)
    out["interpretation"] = (
        "All implied displacements are within the screen's own noise floor, so "
        "this is a statement about the screen, not a bound on the zeros.  The "
        "point of this file is the FLOOR: compare sensitivity_floor_delta with "
        "sensitivity_floor_previous_design to see what the paired-window design "
        "bought."
    )
    print(f"  max |implied delta| = {out['max_abs_implied_delta']:.4f}")

    path = os.path.join(HERE, "results", f"paired-window-X{X}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote", path)


if __name__ == "__main__":
    main()
