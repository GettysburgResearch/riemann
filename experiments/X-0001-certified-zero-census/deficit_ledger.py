#!/usr/bin/env python3
"""
X-0001b -- The deficit ledger (M-0005 / Q-0011).

Agent: claude-01

L-0004 compares two certified integers for a box: N_box, the argument-principle
count, and m, the number of certified sign changes of the Hardy function.  Their
agreement proves RH in that box.  Everything interesting lives in the
DIFFERENCE:

    deficit(band) = N_box(band) - m(band)

which is 0 wherever RH holds and exactly 2 at the first off-critical pair (a
zero and its mirror are both in the box, but they produce no sign change).
There is no noise in this quantity: it is the difference of two integers, each
certified.  It is either 0 or it is a discovery.

This script builds the ledger per height band from the certificates already
emitted by run.py, so it costs nothing to run and can be regenerated whenever
the census is extended.

Usage: python3 deficit_ledger.py [results/census-T500.json ...]
"""
from __future__ import annotations

import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def ordinate(s: str) -> float:
    return float(s.split(" ")[0].lstrip("["))


def main():
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "results", "census-T*.json")))
    ledgers = []
    for path in paths:
        with open(path) as fh:
            d = json.load(fh)
        subs = d.get("A_subboxes") or []
        zs = [ordinate(z) for z in d.get("B_zero_enclosures", [])]
        if not subs or not zs:
            continue
        rows = []
        total_def = 0
        for s in subs:
            lo, hi = float(s["y0"]), float(s["y1"])
            nbox = s["count"]
            m = sum(1 for z in zs if lo < z <= hi)
            deficit = (nbox - m) if nbox is not None else None
            if deficit:
                total_def += deficit
            rows.append({"band": [lo, hi], "N_box": nbox, "sign_changes": m,
                         "deficit": deficit})
        ledgers.append({"source": os.path.basename(path), "T": d.get("T"),
                        "bands": rows,
                        "total_deficit": total_def,
                        "max_abs_deficit": max((abs(r["deficit"]) for r in rows
                                                if r["deficit"] is not None),
                                               default=None)})
        print(f"\n{os.path.basename(path)}   ({len(rows)} bands)")
        print(f"{'band':>22}  {'N_box':>6} {'m':>6} {'deficit':>8}")
        for r in rows:
            flag = "   <== ALERT" if r["deficit"] else ""
            print(f"  [{r['band'][0]:8.2f},{r['band'][1]:8.2f}]  "
                  f"{str(r['N_box']):>6} {r['sign_changes']:>6} "
                  f"{str(r['deficit']):>8}{flag}")
        print(f"  total deficit: {total_def}   "
              f"({'no off-critical zero in this range' if total_def == 0 else 'INVESTIGATE'})")

    out = {"experiment": "X-0001b", "agent": "claude-01",
           "quantity": "deficit = N_box - (certified sign changes) per height band",
           "semantics": "difference of two CERTIFIED integers; exactly 0 under RH, "
                        "exactly 2 at an off-critical pair; no noise",
           "ledgers": ledgers}
    path = os.path.join(HERE, "results", "deficit-ledger.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote", path)


if __name__ == "__main__":
    main()
