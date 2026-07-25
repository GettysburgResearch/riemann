#!/usr/bin/env python3
"""
X-0004 -- Lehmer pairs: where is RH closest to failing?

Agent: claude-01

RATIONALE (why this is a counterexample-hunting experiment, not zero-scanning)

The de Bruijn-Newman constant Lambda satisfies Lambda >= 0 (Rodgers-Tao 2020)
and RH is equivalent to Lambda <= 0.  So RH holds iff Lambda = 0, i.e. RH is
"barely true": the zeros are exactly on the boundary of failing.  Lower bounds
for Lambda have historically come from *Lehmer pairs* -- pairs of consecutive
zeros that are anomalously close.  A sufficiently extreme Lehmer pair would
certify Lambda > 0 and hence DISPROVE RH.

This experiment therefore does not ask "are the zeros on the line" (X-0001
answers that with certainty in its range).  It asks: **which heights are the
structurally weakest, i.e. the best places to spend expensive certified
search?**  Its output is a ranked target list for later agents.

QUANTITIES

  gamma_n           certified ordinates of on-line zeros (from L-0004 machinery)
  g_n = gamma_{n+1} - gamma_n
  nu_n = g_n * log(gamma_n / (2 pi)) / (2 pi)    normalised gap (mean 1)
  D_n  = g_n^2 * sum_{j != n, n+1} [ (gamma_j-gamma_n)^-2 + (gamma_j-gamma_{n+1})^-2 ]

D_n is the Csordas-Smith-Varga "Lehmer pair" discriminator.  CSV theory turns a
pair with D_n below an explicit threshold into a lower bound for Lambda.

  *** UNVERIFIED CITATION ***  The exact threshold and the resulting bound are
  NOT reproduced here: this agent cannot verify the constants from memory, and
  the project forbids presenting unverified recollection as fact.  See
  OPEN_PROBLEMS Q-0005.  The D_n values computed here are well defined
  independently of that constant and are what a later agent needs.

STATUS OF OUTPUT: EMPIRICAL (the ordinates are certified; D_n is computed from
certified ordinates but with a truncated zero sum, so D_n itself is reported as
a non-rigorous approximation with a stated truncation).

Usage: python3 run.py [T] [step]
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import certzeta as cz  # noqa: E402
import zeros as Zmod  # noqa: E402
from flint import arb  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def main():
    T = sys.argv[1] if len(sys.argv) > 1 else "2000"
    step = sys.argv[2] if len(sys.argv) > 2 else "0.04"
    cz.set_prec(260)

    t0 = time.time()
    zs, undet, nsign = Zmod.certified_zeros(0, T, step, bisect_iters=40)
    scan_s = time.time() - t0
    g = [float(z.mid()) for z in zs]
    print(f"{len(g)} certified on-line zeros up to T={T} in {scan_s:.1f}s "
          f"(undetermined signs: {len(undet)})")

    import math

    pairs = []
    for n in range(len(g) - 1):
        gap = g[n + 1] - g[n]
        nu = gap * math.log(g[n] / (2 * math.pi)) / (2 * math.pi) if g[n] > 7 else None
        s = 0.0
        for j in range(len(g)):
            if j == n or j == n + 1:
                continue
            d1 = g[j] - g[n]
            d2 = g[j] - g[n + 1]
            s += 1.0 / (d1 * d1) + 1.0 / (d2 * d2)
        pairs.append(
            {"n": n, "gamma_n": g[n], "gamma_np1": g[n + 1], "gap": gap,
             "nu": nu, "D": gap * gap * s}
        )

    ranked_nu = sorted([p for p in pairs if p["nu"] is not None],
                       key=lambda p: p["nu"])[:25]
    ranked_D = sorted(pairs, key=lambda p: p["D"])[:25]

    out = {
        "experiment": "X-0004",
        "agent": "claude-01",
        "git_sha": git_sha(),
        "T": T,
        "scan_step": step,
        "prec_bits": 260,
        "n_zeros": len(g),
        "undetermined_signs": len(undet),
        "scan_seconds": round(scan_s, 1),
        "status": "ordinates CERTIFIED (sign-change + bisection); "
                  "D_n EMPIRICAL (zero sum truncated to the computed range)",
        "truncation_note": f"D_n uses only the {len(g)} zeros with 0 < gamma <= {T}; "
                           "the omitted tail is positive, so the reported D_n is a "
                           "LOWER bound for the true D_n -- which is the conservative "
                           "direction for flagging a candidate but the WRONG direction "
                           "for certifying one.",
        "tightest_normalised_gaps": ranked_nu,
        "smallest_D": ranked_D,
        "zeros": [str(z) for z in zs],
    }
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    path = os.path.join(HERE, "results", f"lehmer-T{T}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)

    print("\n tightest normalised gaps (nu = gap / mean spacing):")
    for p in ranked_nu[:10]:
        print(f"   n={p['n']:6d} gamma={p['gamma_n']:14.6f} gap={p['gap']:.6f} "
              f"nu={p['nu']:.4f}  D={p['D']:.4f}")
    print("wrote", path)


if __name__ == "__main__":
    main()
