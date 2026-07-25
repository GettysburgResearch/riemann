#!/usr/bin/env python3
"""
X-0002b -- The detection threshold of T-0001 on a REAL zeta box.

Agent: claude-01

A counterexample cannot be planted inside zeta, so the sensitivity floor of
T-0001 on a real box cannot be measured the way X-0002 part 2 measures it on a
synthetic polynomial.  It can, however, be *derived* from the certificate the
box already produced.

DERIVATION

By T-0001(e), det H_N = prod_{i<j} (w_i - w_j)^2, the discriminant of the box's
zero polynomial in the normalised coordinate w.  Suppose the two zeros whose
normalised gap is g were in fact an off-critical pair at w = a +- i b instead
of two real points.  Their factor changes from g^2 to (2ib)^2 = -4b^2, so

    det H  ->  - (4 b^2 / g^2) * det H .

The certificate is decided by comparing that against the certified uncertainty
of det H.  Writing rho for the relative uncertainty of the least certain pivot
(the last one, which dominates), the verdict flips to NOT_PSD once

    4 b^2 / g^2  >  rho ,        i.e.   b > (g/2) sqrt(rho) .

In unnormalised units (b = delta / r, g = gap / r):

    delta_detect  ~  (gap / 2) * sqrt(rho).                             (*)

WHAT delta_detect IS, AND IS NOT

It is the smallest displacement at which the certificate would **positively
announce** a counterexample (verdict NOT_PSD) rather than abstain (UNDECIDED).

It is NOT a limit on what a PD verdict excludes.  By T-0001(c) the equivalence
is exact: if any zero in the box were off the line, the true Hankel matrix
would fail to be positive semidefinite, its true least pivot would be negative,
and a certified enclosure containing that negative value could never be
certified positive.  **So every PD verdict in this repository already excludes
an off-critical zero at every displacement, however small.**  delta_detect
governs the other direction only -- how large a real counterexample would have
to be before this method announced it instead of shrugging.

THE CONSEQUENCE WORTH NOTING

(*) is proportional to the **ordinate gap**.  So the displacement that could be
positively announced is smallest exactly where consecutive zeros are closest --
the quantitative justification for targeting Lehmer pairs (Z-0002), a claim
made on qualitative grounds in CANDIDATES.md before this was computed.
Measured: ordinary boxes give delta_detect ~ 0.03 to 0.28, while the four
Lehmer-pair boxes give 0.0043 to 0.0057 -- roughly fifty times better.

STATUS: EMPIRICAL, and a heuristic derivation -- (*) drops constants and treats
the last pivot as dominating.  It is an order-of-magnitude guide for choosing
targets, not a certified bound.  Q-0006 asks for the theorem with constants.

Usage: python3 threshold.py
"""
from __future__ import annotations

import glob
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BALL = re.compile(r"\[?\s*([-+0-9.eE]+)?\s*(?:\+/-\s*([-+0-9.eE]+))?\s*\]?")


def parse_ball(s: str):
    """Parse an arb string '[mid +/- rad]' or 'exact' into (mid, rad)."""
    s = s.strip()
    m = re.match(r"^\[?\s*([-+]?[0-9.]+(?:e[-+]?[0-9]+)?)?\s*(?:\+/-\s*([0-9.]+(?:e[-+]?[0-9]+)?))?\s*\]?$", s)
    if not m:
        return None, None
    mid = float(m.group(1)) if m.group(1) else 0.0
    rad = float(m.group(2)) if m.group(2) else 0.0
    return mid, rad


def threshold(pivots, gap):
    """delta_detect ~ (gap/2) sqrt(rho), rho = relative uncertainty of the
    least certain pivot."""
    rho = 0.0
    for p in pivots:
        mid, rad = parse_ball(p)
        if mid is None or mid == 0:
            continue
        rho = max(rho, abs(rad / mid))
    if rho == 0:
        return None, None
    return (gap / 2) * math.sqrt(rho), rho


def main():
    rows = []

    # boxes from the main X-0002 run: gaps taken from the known low ordinates
    ords = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
            37.586178, 40.918719, 43.327073, 48.005151, 49.773832]
    path = os.path.join(HERE, "results", "certificates-nsub32.json")
    if os.path.exists(path):
        d = json.load(open(path))
        for b in d["zeta_boxes"]:
            if "pivots" not in b:
                continue
            lo, hi = float(b["box"][2]), float(b["box"][3])
            inside = [g for g in ords if lo < g < hi]
            gap = min((inside[i + 1] - inside[i] for i in range(len(inside) - 1)),
                      default=None)
            if gap is None:
                continue
            dd, rho = threshold(b["pivots"], gap)
            rows.append({"box": b["box"], "N": b["N"], "min_gap": gap,
                         "pivot_rel_uncertainty": rho, "delta_detect": dd})

    # the Lehmer-pair boxes
    for p in sorted(glob.glob(os.path.join(HERE, "results", "lehmer-pair*.json"))) + \
             sorted(glob.glob(os.path.join(HERE, "results", "lehmer-pairs*.json"))):
        d = json.load(open(p))
        recs = d if isinstance(d, list) else [d]
        for rec in recs:
            h = rec.get("hermite", {})
            if "pivots" not in h:
                continue
            gap = rec.get("gap")
            if gap is None:
                gap = 0.0975025  # the gamma ~ 1977.17 pair
            dd, rho = threshold(h["pivots"], gap)
            rows.append({"box": f"Lehmer pair gamma~{rec.get('gamma', 1977.17):.2f}",
                         "N": h.get("N"), "min_gap": gap,
                         "pivot_rel_uncertainty": rho, "delta_detect": dd})

    print(f"{'box':>34} {'N':>3} {'min gap':>10} {'pivot rel unc':>14} "
          f"{'delta_detect':>13}")
    for r in rows:
        b = r["box"] if isinstance(r["box"], str) else \
            f"[{r['box'][0]},{r['box'][1]}]x[{r['box'][2]},{r['box'][3]}]"
        print(f"{b:>34} {str(r['N']):>3} {r['min_gap']:>10.5f} "
              f"{r['pivot_rel_uncertainty']:>14.3e} {r['delta_detect']:>13.3e}")

    out = {"experiment": "X-0002b", "agent": "claude-01",
           "status": "EMPIRICAL, heuristic derivation (see docstring); not a bound",
           "formula": "delta_detect ~ (gap/2) sqrt(relative uncertainty of least "
                      "certain Hankel pivot)",
           "consequence": "delta_detect is proportional to the ordinate gap, so "
                          "tight Lehmer pairs are quantitatively the best targets "
                          "-- which is why Z-0002 aims there",
           "rows": rows}
    with open(os.path.join(HERE, "results", "detection-thresholds.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote results/detection-thresholds.json")


if __name__ == "__main__":
    main()
