#!/usr/bin/env python3
"""
X-0006b -- The Weil matched filter: probing any height from two dozen primes.

Agent: claude-01
Implements/validates: T-0002(d).

THE POINT

Every certified tool elsewhere in this repository costs more as the height
grows: L-0004 is O(T^2), and even a single box certificate at t ~ 7005 takes
minutes because each evaluation of zeta needs ~7000 Euler-Maclaurin terms.

The Weil functional does not work that way.  With the modulated test functions
phi_j(u) = e^{i gamma_0 u} B_m((u-t_j)/a), the prime sum runs over prime powers
n <= e^{m a + |d|} -- a set that does NOT depend on gamma_0 at all.  Only the
archimedean series feels the height, and the Watson acceleration in
scripts/weil_mod.py reduces that to O(gamma_0) terms of trivial cost.

So: the same 24 prime powers that probe gamma = 14 also probe gamma = 7005.

WHAT IS MEASURED HERE

 1. the certified Weil matrix and its PSD verdict at a ladder of heights,
    including the two Lehmer pairs this repository has certified by contour
    methods (gamma ~ 1977.17 and the classical gamma ~ 7005.06);
 2. the cost, to show it is flat in gamma_0 on the prime side;
 3. the resolution law -- how wide the filter is in gamma, and what it would
    cost in primes to narrow it.

STATUS: the matrices are CERTIFIED (ball arithmetic, exact Lambda(n), rigorous
tail).  A PD verdict is consistent with RH; a certified negative pivot would be
a counterexample.  The sensitivity of the test is measured separately in run.py
part 3 and in sensitivity.py.

Usage: python3 matched.py
"""
from __future__ import annotations

import json
import math
import os
import platform
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import hermite as Herm  # noqa: E402
import weil  # noqa: E402
import weil_mod as wm  # noqa: E402
from flint import arb, ctx  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def main():
    ctx.prec = 300
    a, m, M, s = 1.0, 4, 6, 0.5
    shifts = [s * j for j in range(M)]
    npp = len(weil.prime_powers(round(m * a + s * (M - 1) + 1e-9, 9)))

    out = {
        "experiment": "X-0006b", "agent": "claude-01", "git_sha": git_sha(),
        "python": sys.version.split()[0], "flint": __import__("flint").__version__,
        "platform": platform.platform(), "prec_bits": 300,
        "basis": {"a": a, "m": m, "dim": M, "spacing": s,
                  "support_of_g": m * a + s * (M - 1),
                  "n_prime_powers": npp},
        "semantics": "certified: arb balls, exact Lambda(n), closed-form pole "
                     "and Laplace transforms, Watson-accelerated archimedean "
                     "series with a rigorous tail bound",
        "rows": [],
    }
    print(f"basis: a={a} m={m} dim={M} spacing={s}  -> {npp} prime powers "
          f"(the SAME set at every height)")

    for g0, N in [(0.0, 4000), (14.134725141734693, 4000), (100.0, 8000),
                  (500.0, 20000), (1977.173944, 60000), (7005.062866, 150000)]:
        t0 = time.time()
        try:
            Q = wm.weil_matrix_mod(a, shifts, g0, m=m, N=N, K=2)
            verdict, piv = Herm.ldl_signs(Q)
            rec = {"gamma0": g0, "series_terms": N, "verdict": verdict,
                   "min_pivot": min(float(x.mid()) for x in piv),
                   "max_pivot_uncertainty": max(float(x.rad()) for x in piv),
                   "pivots": [str(x) for x in piv],
                   "seconds": round(time.time() - t0, 1)}
        except Exception as e:
            rec = {"gamma0": g0, "error": f"{type(e).__name__}: {e}",
                   "seconds": round(time.time() - t0, 1)}
        out["rows"].append(rec)
        print(f"  gamma0={g0:12.4f}  {rec.get('verdict', rec.get('error'))}"
              f"  min pivot {rec.get('min_pivot')}"
              f"  unc {rec.get('max_pivot_uncertainty')}"
              f"  [{rec['seconds']}s]", flush=True)

    # resolution / cost law
    out["resolution_law"] = {
        "filter_half_width_in_gamma": 2 * math.pi / a,
        "prime_cost": f"prime powers up to e^(m a + |d|) = e^{m * a + s * (M - 1):.1f}",
        "statement":
            "h(r) = a^2 sinc^{2m}(a(r-gamma_0)/2) has main-lobe half width "
            "2 pi / a, while the prime sum runs to e^{m a}.  To resolve the "
            "mean zero spacing 2 pi / log(T/2 pi) at height T one needs "
            "a ~ log(T/2pi), hence primes up to (T/2pi)^m: POLYNOMIAL in T, "
            "not exponential -- but with a brutal constant.  At T = 7005 and "
            "m = 2 that is about 1.2e6 primes, which is feasible; at m = 4 it "
            "is not.  This is the fundamental cost law of the method and it is "
            "the thing to attack next.",
    }

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", "matched-filter.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", p)


if __name__ == "__main__":
    main()
