#!/usr/bin/env python3
"""
X-0001 -- Certified zero census of zeta in the critical strip up to height T.

Agent: claude-01

Three independent certified computations, all in ball arithmetic:

  (A) ARGUMENT PRINCIPLE.  Number of zeros of the entire function xi inside
      the rectangle [0,1] x [0,T], via a rigorous winding number (L-0002).
      Call it  N_box.

  (B) SIGN CHANGES.  Number of certified sign changes of the real Hardy
      function Z on (0, T], each of which proves (IVT) a zero of zeta exactly
      ON the critical line.  Call it  N_line.

  (C) OFF-LINE EXCLUSION.  Certified winding number on the off-critical
      rectangles [1/2 + d, 1] x [0, T] for a decreasing sequence of d.  A
      count of 0 proves there is NO zero with Re(s) >= 1/2 + d and 0 <= t <= T.

If N_box == N_line then every zero in the box is on the critical line and is
simple, which is a computer-assisted PROOF of RH in that range, and hence a
certified NEGATIVE result for the counterexample search.  (C) is a weaker but
methodologically independent statement that also directly bounds where a
counterexample can live.

Usage:  python3 run.py [T] [step] [prec]
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
import winding as W  # noqa: E402
import zeros as Zmod  # noqa: E402
from flint import arb, ctx  # noqa: E402


def git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=HERE, text=True
        ).strip()
    except Exception:
        return "unknown"


def main():
    T = arb(sys.argv[1] if len(sys.argv) > 1 else "100")
    step = sys.argv[2] if len(sys.argv) > 2 else "0.05"
    prec = int(sys.argv[3] if len(sys.argv) > 3 else 300)
    cz.set_prec(prec)

    result = {
        "experiment": "X-0001",
        "agent": "claude-01",
        "question": "How many zeros does zeta have in [0,1]x[0,T], how many are "
        "certifiably on the critical line, and which off-critical rectangles are "
        "certifiably zero-free?",
        "T": str(T),
        "step": step,
        "prec_bits": prec,
        "git_sha": git_sha(),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "flint": __import__("flint").__version__,
        "semantics": "arb/acb ball arithmetic; all enclosures rigorous; "
        "zeta via self-implemented Euler-Maclaurin with proved remainder (L-0001)",
    }

    # ---- (A) argument principle -------------------------------------------
    t0 = time.time()
    pieces = max(1, int(float(T) / 25))
    certA = W.count_zeros_rect_split(0, 1, 0, T, pieces=pieces, f=cz.xi_ball, n0=8)
    result["A_argument_principle"] = certA.as_dict()
    result["A_subboxes"] = certA.subboxes
    result["A_seconds"] = round(time.time() - t0, 2)
    N_box = certA.count
    print(f"(A) N_box = {N_box}   ok={certA.ok} {certA.reason}  "
          f"[{result['A_seconds']}s]")

    # ---- (B) certified on-line zeros --------------------------------------
    t0 = time.time()
    zs, undet, nsign = Zmod.certified_zeros(0, T, step, bisect_iters=50)
    result["B_sign_changes"] = nsign
    result["B_undetermined_points"] = len(undet)
    result["B_seconds"] = round(time.time() - t0, 2)
    result["B_zero_enclosures"] = [str(z) for z in zs]
    print(f"(B) N_line = {nsign}   undetermined={len(undet)}  "
          f"[{result['B_seconds']}s]")

    result["RH_verified_in_range"] = bool(
        certA.ok and N_box is not None and N_box == nsign
    )
    result["all_zeros_simple_in_range"] = result["RH_verified_in_range"]

    # ---- (C) off-critical zero-free rectangles ----------------------------
    offline = []
    for d in ["0.25", "0.1", "0.05", "0.02", "0.01"]:
        t0 = time.time()
        x0 = arb("0.5") + arb(d)
        c = W.count_zeros_rect_split(
            x0, 1, 0, T, pieces=pieces, f=cz.xi_ball, n0=8
        )
        rec = c.as_dict()
        rec["delta"] = d
        rec["seconds"] = round(time.time() - t0, 2)
        offline.append(rec)
        print(f"(C) delta={d}: count={c.count} ok={c.ok} {c.reason} "
              f"[{rec['seconds']}s]")
        if not c.ok:
            break
    result["C_offline_boxes"] = offline
    best = [r for r in offline if r["ok"] and r["count"] == 0]
    result["C_certified_zero_free_halfwidth"] = (
        min(float(r["delta"]) for r in best) if best else None
    )

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    out = os.path.join(HERE, "results", f"census-T{str(T).split('.')[0]}.json")
    with open(out, "w") as fh:
        json.dump(result, fh, indent=1)
    print("wrote", out)

    print("\nSUMMARY")
    print(f"  zeros in [0,1]x[0,{T}]         : {N_box}  (certified)")
    print(f"  certified on-line sign changes : {nsign}")
    print(f"  RH certified in this range     : {result['RH_verified_in_range']}")
    print(f"  no zero with |Re-1/2| >= delta : delta = "
          f"{result['C_certified_zero_free_halfwidth']}")


if __name__ == "__main__":
    main()
