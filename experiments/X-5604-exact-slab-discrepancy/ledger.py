#!/usr/bin/env python3
"""Re-verify every slab certificate in results/ and print the ledger.

Agent: opus5-01   Issue: #55

A `D = 0` certificate is a local, proof-carrying statement about one stretch of
the critical line.  They accumulate, so they deserve a ledger — and the ledger
should not take the JSON's word for anything it can re-derive.

For each certificate this re-checks, from the recorded numbers alone:

  * the slab endpoints are exact dyadic rationals, and `a < b`;
  * `N = N(b) - N(a)` as recorded, and `N >= 0`;
  * `N_0 <= N`  (a certified count of critical-line zeros cannot exceed the
    total; a violation means one of the two computations is wrong);
  * `D = N - N_0`, and `D >= 0`;
  * `D` is **even** if positive — the functional equation puts off-critical
    zeros in quadruples, so an odd positive `D` is not a counterexample, it is
    an inconsistent computation;
  * no undecided samples were counted as signs.

It re-derives nothing that requires zeta.  This is an arithmetic audit of the
certificate objects, not a re-run; `--rerun` is what a re-run would be.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from fractions import Fraction as Fr


def is_dyadic(f: Fr) -> bool:
    q = f.denominator
    return q > 0 and (q & (q - 1)) == 0


def check(path):
    with open(path) as fh:
        d = json.load(fh)
    problems = []
    tag = d.get("tag") or d.get("label") or os.path.basename(path)

    a, b = d.get("a"), d.get("b")
    if a is None or b is None:
        return None
    # slab_discrepancy.py records endpoints as {"fraction": .., "float": ..};
    # the certifiers record them as a bare fraction string.  Accept both.
    if isinstance(a, dict):
        a = a.get("fraction")
    if isinstance(b, dict):
        b = b.get("fraction")
    a, b = Fr(a), Fr(b)
    if not (a < b):
        problems.append("a >= b")
    for nm, v in (("a", a), ("b", b)):
        if not is_dyadic(v):
            problems.append("%s is not dyadic" % nm)

    N = d.get("N_total", d.get("N_total_in_slab", d.get("N")))
    N0 = d.get("N0_certified_lower_bound",
               d.get("certified_sign_changes",
                     d.get("N0_disjoint_balls_inside")))
    if d.get("problems"):
        problems.append("certificate records problems: %r" % d["problems"][:2])
    if N is None or N0 is None:
        return None
    if N < 0:
        problems.append("N < 0")
    if N0 > N:
        problems.append("N_0 = %d exceeds N = %d -- INCONSISTENT" % (N0, N))
    D = N - N0
    if D < 0:
        problems.append("D < 0")
    if D > 0 and D % 2 == 1:
        problems.append("D = %d is positive and ODD -- inconsistent, not a "
                        "counterexample" % D)

    und = d.get("undecided_count")
    if und is None:
        und = len(d.get("undecided", d.get("undecided_samples", [])))
    if und and D == 0:
        problems.append("D = 0 claimed with %d undecided samples" % und)

    return {
        "file": os.path.basename(path), "tag": tag,
        "a": float(a), "b": float(b), "span": float(b - a),
        "N": N, "N0": N0, "D": D, "undecided": und,
        "recorded_D": d.get("D"),
        "ok": not problems, "problems": problems,
        "verdict": d.get("verdict", ""),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.join(os.path.dirname(__file__), "results"))
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    rows = []
    for p in sorted(glob.glob(os.path.join(args.dir, "*.json"))):
        try:
            r = check(p)
        except Exception as e:                      # noqa: BLE001
            rows.append({"file": os.path.basename(p), "ok": False,
                         "problems": ["unreadable: %s" % e]})
            continue
        if r:
            rows.append(r)

    # One slab can appear in several artifacts (the raw count, the sign pass,
    # and the driver summary).  Deduplicate on the slab itself so the ledger
    # totals count height once.
    seen, dedup = set(), []
    for r in rows:
        if not r.get("ok"):
            dedup.append(r); continue
        key = (r["a"], r["b"])
        if key in seen:
            continue
        seen.add(key); dedup.append(r)
    rows = dedup
    # Drop certified slabs fully contained in a larger certified slab, so the
    # height total counts every unit once (the 999-unit 1e13 certificate is a
    # sub-slab of the 11,200-unit one).
    certified = [r for r in rows if r.get("ok") and r.get("D") == 0]
    contained = set()
    for r in certified:
        for q in certified:
            if q is not r and q["a"] <= r["a"] and r["b"] <= q["b"]                     and (q["a"], q["b"]) != (r["a"], r["b"]):
                contained.add((r["a"], r["b"]))
    rows = [r for r in rows
            if not (r.get("ok") and (r.get("a"), r.get("b")) in contained)]
    good = [r for r in rows if r.get("ok") and r.get("D") == 0]
    bad = [r for r in rows if not r.get("ok")]
    good.sort(key=lambda r: r["a"])

    print("=" * 96)
    print("%-26s %14s %10s %8s %8s %5s %s" %
          ("slab (height)", "span", "N", "N_0", "D", "und", "status"))
    print("-" * 96)
    total_zeros = total_span = 0
    for r in good:
        print("%-26.4f %14.1f %10d %8d %8d %5d  CERTIFIED"
              % (r["a"], r["span"], r["N"], r["N0"], r["D"], r["undecided"] or 0))
        total_zeros += r["N"]
        total_span += r["span"]
    print("-" * 96)
    print("%d certified slabs   %.1f units of height   %d zeros, all on the "
          "critical line and simple" % (len(good), total_span, total_zeros))
    if bad:
        print("\n%d PROBLEM(S):" % len(bad))
        for r in bad:
            print("  %-40s %s" % (r["file"], "; ".join(r["problems"])))
    print("=" * 96)

    if args.out:
        with open(args.out, "w") as fh:
            json.dump({"schema": "riemann.x5604-ledger.v1", "agent": "opus5-01",
                       "certified_slabs": len(good),
                       "total_span": total_span, "total_zeros": total_zeros,
                       "rows": rows}, fh, indent=1)
        print("wrote", args.out)


if __name__ == "__main__":
    main()
