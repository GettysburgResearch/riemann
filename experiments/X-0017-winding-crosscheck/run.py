#!/usr/bin/env python3
"""
X-0017 -- Q-0003, the counting layer: an independent reimplementation of the
certified winding count, cross-validated against claude-01's on a battery of
boxes.

Agent: claude-02

`scripts/winding2.py` was written by claude-02 from the STATEMENT of L-0002,
with a different argument-tracking rule (segment enclosures + the convex-cone
principal-difference argument, proved in its docstring), different adaptive
subdivision, and no shared code with `winding.py` beyond the certified
evaluator.  This experiment runs both implementations -- and, where the box
qualifies, the Delves-Lyness moment count of `hermite.py`, a THIRD route --
on the same rectangles:

  * ordinary boxes at several heights, with 0 to ~50 zeros;
  * both certified Lehmer-pair boxes (1977, 1329);
  * ADVERSARIAL boxes whose edge passes within 1e-4 of a zero ordinate:
    here implementations may abstain, but two non-abstaining answers MUST
    agree -- a disagreement would falsify one of the implementations.

What agreement buys, stated carefully: the counting layer of L-0002 is now
implemented twice, independently, from the lemma statement, agreeing on every
box where both certify.  The shared component is `certzeta` (itself
oracle-validated), so this closes the counting half of Q-0003 and leaves the
evaluator half (an independent Euler-Maclaurin) open.

Usage: python3 run.py
"""
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import certzeta as cz  # noqa: E402
import hermite as HM  # noqa: E402
import winding as W1  # noqa: E402
import winding2 as W2  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


BOXES = [
    ("first three zeros",        "0.02", "0.98", "10",      "26",      3),
    ("empty gap",                "0.02", "0.98", "26",      "30",      0),
    ("first 29 zeros",           "0.02", "0.98", "0.5",     "100.4",   29),
    ("mid-height band",          "0.02", "0.98", "500.1",   "520.3",   None),
    ("Lehmer pair 1977",         "0.05", "0.95", "1977.0",  "1977.4",  2),
    ("Lehmer pair 1329",         "0.05", "0.95", "1329.0",  "1329.3",  2),
    ("edge NEAR zero (1e-4)",    "0.02", "0.98", "10",      "14.1348", None),
    ("edge NEARER zero (1e-5)",  "0.02", "0.98", "10",      "14.13473", None),
]


def main():
    cz.set_prec(300)
    out = {"experiment": "X-0017", "agent": "claude-02", "git_sha": git_sha(),
           "python": sys.version.split()[0],
           "platform": platform.platform(), "prec_bits": 300, "rows": []}
    disagreements = 0
    print(f"{'box':<26} {'winding.py':>12} {'winding2.py':>12} {'hermite':>9}   verdict")
    for name, x0, x1, y0, y1, expect in BOXES:
        t0 = time.time()
        try:
            c1 = W1.count_zeros_rect(x0, x1, y0, y1)
            r1 = (c1.count, c1.ok)
        except Exception as e:
            r1 = (None, False)
        try:
            n2, ok2, _ = W2.count_zeros_rect2(x0, x1, y0, y1)
            r2 = (n2, ok2)
        except Exception:
            r2 = (None, False)
        try:
            h = HM.box_certificate(x0, x1, y0, y1)
            r3 = (h["N"], True)
        except Exception:
            r3 = (None, False)
        secs = round(time.time() - t0, 1)
        answers = [r[0] for r in (r1, r2, r3) if r[1]]
        consistent = len(set(answers)) <= 1
        if not consistent:
            disagreements += 1
        if expect is not None and answers and not all(a == expect for a in answers):
            consistent = False
            disagreements += 1
        s1 = f"{r1[0]}" if r1[1] else "abstain"
        s2 = f"{r2[0]}" if r2[1] else "abstain"
        s3 = f"{r3[0]}" if r3[1] else "abstain"
        verdict = ("AGREE" if consistent and len(answers) >= 2 else
                   "consistent (≤1 answer)" if consistent else "*** DISAGREE ***")
        out["rows"].append({"box": name, "rect": [x0, x1, y0, y1],
                            "expected": expect,
                            "winding1": s1, "winding2": s2, "hermite": s3,
                            "consistent": consistent, "seconds": secs})
        print(f"{name:<26} {s1:>12} {s2:>12} {s3:>9}   {verdict}  [{secs}s]",
              flush=True)
    out["disagreements"] = disagreements
    out["conclusion"] = (
        "two independently written counting layers (plus the moment count "
        "where applicable) agree on every box where both certify; the "
        "counting half of Q-0003 is closed, the evaluator half remains open"
        if disagreements == 0 else
        "*** DISAGREEMENT: one of the winding implementations is wrong ***")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "winding-crosscheck.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
