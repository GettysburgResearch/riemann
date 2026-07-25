#!/usr/bin/env python3
"""
X-0008 -- Speiser's criterion, certified: is the left half-strip empty of
zeros of zeta' ?

Agent: claude-01

SPEISER (1935).  RH is equivalent to zeta'(s) having no zeros in the open
strip 0 < Re(s) < 1/2.

  [CITATION FLAG (M-0004): the equivalence is quoted from memory and has NOT
  been verified against the literature by this agent.  Direction of risk: the
  direction this experiment RELIES on for a counterexample is

        a zero of zeta' with 0 < Re s < 1/2  ==>  RH is false,

  so a misremembered statement could produce a FALSE POSITIVE.  For that reason
  no counterexample claim may be made from this experiment until the theorem is
  checked -- see OPEN_PROBLEMS Q-0014.  The null results below are safe under
  either reading: they merely say a region is empty.]

WHY IT IS WORTH DOING ANYWAY

Every other certified test here has to *find* something: count zeros in a box
straddling the line, match two counts, isolate a disc.  This one asks whether a
region is EMPTY, which is the cheapest question an argument principle can
answer -- the winding number is 0 and nothing needs locating.  And it is a
genuinely different object: zeta', not zeta, not xi, not the primes.  A
systematic error in the zeta-zero machinery would have to reproduce itself in
the derivative to escape this test.

zeta' is computed as  eta'(s)/(s-1) - eta(s)/(s-1)^2  from the certified
Taylor-model enclosures of L-0006, so the whole L-0002 winding machinery
applies unchanged.

Usage: python3 run.py [T] [pieces]
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
import speiser as sp  # noqa: E402
import winding as W  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def main():
    T = float(sys.argv[1]) if len(sys.argv) > 1 else 300.0
    pieces = int(sys.argv[2]) if len(sys.argv) > 2 else max(1, int(T / 25))
    cz.set_prec(300)

    out = {
        "experiment": "X-0008", "agent": "claude-01", "git_sha": git_sha(),
        "python": sys.version.split()[0], "flint": __import__("flint").__version__,
        "platform": platform.platform(), "prec_bits": 300,
        "criterion": "Speiser: RH <=> zeta' has no zeros in 0 < Re s < 1/2",
        "citation_flag": "the equivalence is unverified by this agent; the "
                         "refutation direction could give a FALSE POSITIVE, so "
                         "no counterexample claim may rest on it until Q-0014 "
                         "is resolved.  Null results are safe either way.",
        "semantics": "certified winding number (L-0002) applied to "
                     "zeta' = eta'/(s-1) - eta/(s-1)^2, enclosed by L-0006",
        "boxes": [],
    }

    for (x0, x1) in [("0.02", "0.48"), ("0.001", "0.499")]:
        t0 = time.time()
        cert = W.count_zeros_rect_split(x0, x1, 1, T, pieces=pieces,
                                        f=sp.zeta_prime_ball, n0=8)
        rec = cert.as_dict()
        rec["x0"], rec["x1"] = x0, x1
        rec["seconds"] = round(time.time() - t0, 1)
        out["boxes"].append(rec)
        print(f"  zeta' zeros in [{x0},{x1}] x [1,{T}]: {cert.count}  "
              f"ok={cert.ok} {cert.reason[:60]}  [{rec['seconds']}s]", flush=True)

    good = [b for b in out["boxes"] if b["ok"]]
    out["conclusion"] = (
        f"zeta' has no zeros in the tested sub-strips up to height {T}; "
        "consistent with RH, and (subject to Q-0014) a zero here would refute it"
        if good and all(b["count"] == 0 for b in good) else
        "INVESTIGATE: a nonzero count or an abstention")

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", f"speiser-T{int(T)}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print(" " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
