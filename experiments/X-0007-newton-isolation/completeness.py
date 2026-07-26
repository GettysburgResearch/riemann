#!/usr/bin/env python3
"""
X-0007b -- Completeness closure for the Newton sweep, by pinning each disc to
its scan zero.

Agent: claude-02 (second agent; first independent-verification pass on this
repository).

WHY claude-01's CHECK FAILED, AND WHY THE RESULT IS NEVERTHELESS COMPLETE

newton-T2000.json records `discs_pairwise_disjoint: False` and therefore
`accounts_for_every_zero: False`.  The check behind that flag was

    min ordinate gap  >  2 * starting disc radius      (0.0975 > 0.1: FALSE)

i.e. it demanded that the STARTING discs (radius 0.05) be pairwise disjoint.
The Lehmer pair at gamma ~ 1977.17 / 1977.27 has gap 0.0975, so two starting
discs overlap and the flag is honest -- but the disjointness of starting discs
is not what completeness needs.  The correct argument:

  1. (census, L-0004)  The box [0,1] x [0,T] contains EXACTLY n zeros, counted
     with multiplicity.
  2. (scan, X-0004)  There are n pairwise disjoint on-line enclosures
     gamma_k +/- r_k^scan, each certified (sign change of Hardy Z) to contain a
     zero z_k with Re z_k = 1/2.  Disjointness makes the z_k pairwise distinct;
     matching counts with 1. makes {z_1..z_n} ALL the zeros -- that much is the
     census result itself.
  3. (Newton, L-0007)  Disc k is B(1/2 + i gamma_k, R) with R = 0.05.  Since
     r_k^scan < R, the scan zero z_k LIES IN disc k.  Interval Newton certifies
     that disc k contains EXACTLY ONE zero, that it is simple, and that it
     satisfies |Re rho - 1/2| <= bound.  The unique zero of disc k is therefore
     z_k itself, so the certificate attaches to z_k -- regardless of whether
     disc k overlaps disc j.  Overlap could at worst make two discs certify the
     same zero; the pinning shows disc k certifies z_k, and the z_k are
     distinct by 2.

  Conclusion: every zero of zeta with 0 < t <= T is simple and satisfies
  |Re rho - 1/2| <= bound.  (The on-line statement itself is already the
  census's; what Newton adds is an INDEPENDENT machinery -- no winding number,
  no count -- arriving at a stronger quantitative form of the same fact.)

This script verifies the hypotheses mechanically from the three artifacts and
writes the closure record.  It certifies nothing new numerically; it composes
three existing certificates whose composition claude-01's too-strict check
declined to make.

Usage: python3 completeness.py [T]
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def parse_ball(s):
    """'[1977.17394369 +/- 6.55e-13]' -> (mid, rad)"""
    s = s.strip().lstrip("[").rstrip("]")
    if "+/-" in s:
        m, r = s.split("+/-")
        return float(m), float(r)
    return float(s), 0.0


def main():
    T = int(float(sys.argv[1])) if len(sys.argv) > 1 else 2000

    newton = json.load(open(os.path.join(HERE, "results", f"newton-T{T}.json")))
    if T == 2000:
        census = json.load(open(os.path.join(
            HERE, "..", "X-0001-certified-zero-census", "results", f"census-T{T}.json")))
        scanp = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "lehmer-T2000.json")
        scan = json.load(open(scanp))
        # scan['zeros'] entries are strings like '[gamma +/- r] ...':
        ords = []
        for s in scan["zeros"]:
            seg = s[s.index("["):s.index("]") + 1] if "[" in s else s
            ords.append(parse_ball(seg))
        n_scan = len(ords)
        N_box = census["N_box"]
        census_ok = bool(census["ok"])
    elif T == 5000:
        box = json.load(open(os.path.join(
            HERE, "..", "X-0001-certified-zero-census", "results",
            "census-T5000-boxcount.json")))
        scan = json.load(open(os.path.join(
            HERE, "..", "X-0004-lehmer-pairs", "results", "zeros-T5000.json")))
        ords = []
        for s in scan["zeros"]:
            seg = s[s.index("["):s.index("]") + 1] if "[" in s else s
            ords.append(parse_ball(seg))
        n_scan = len(ords)
        N_box = box["N_box"]
        census_ok = bool(box["ok"]) and scan.get("undetermined", 1) == 0
    else:
        raise SystemExit(f"no census artifacts wired for T={T}")

    R = float(newton["disc_radius"])
    checks = {
        "census_ok": census_ok,
        "counts_match_census_eq_scan": N_box == n_scan,
        "counts_match_scan_eq_newton": n_scan == int(newton["n_certified"]),
        "newton_no_failures": int(newton["n_failed"]) == 0,
        "scan_enclosures_pairwise_disjoint":
            all(ords[i + 1][0] - ords[i][0] > ords[i + 1][1] + ords[i][1]
                for i in range(len(ords) - 1)),
        "every_scan_zero_inside_its_disc":
            all(r < R for (_, r) in ords),   # |z_k - c_k| <= r_k^scan < R
        "ordinates_positive_and_below_T": 0 < ords[0][0] and ords[-1][0] < T,
    }
    complete = all(checks.values())

    out = {
        "experiment": "X-0007b", "agent": "claude-02", "git_sha": git_sha(),
        "T": T, "n_zeros": N_box,
        "argument": "pin each Newton disc to its scan zero: r_scan < disc "
                    "radius puts scan zero k inside disc k; interval-Newton "
                    "uniqueness makes it THE zero of disc k; scan zeros are "
                    "pairwise distinct and, by the census count, exhaustive. "
                    "Starting-disc overlap is irrelevant.",
        "checks": checks,
        "max_abs_re_minus_half": newton["max_abs_re_minus_half"],
        "completeness_established": complete,
        "conclusion": (
            f"every zero of zeta with 0 < t <= {T} is simple and satisfies "
            f"|Re rho - 1/2| <= {newton['max_abs_re_minus_half']:.3e}"
            if complete else "NOT closed -- see failing checks"),
    }
    p = os.path.join(HERE, "results", f"completeness-T{T}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    for k, v in checks.items():
        print(f"  {'PASS' if v else 'FAIL'}  {k}")
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
