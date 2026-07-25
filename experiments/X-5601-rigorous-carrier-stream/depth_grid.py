#!/usr/bin/env python3
"""Q-5604 — how small can the D-0801 leading margin get, as a function of the
distance above the Nyquist barrier and of the cell count?

Agent: opus5-01   Issue: #55

C-5601 says the barrier sits at `Delta = ell_T`, i.e. `c = T/(2 pi)`.  The
question this driver answers is what happens *past* it, and how the answer
depends on `K`.  Both axes are swept at a fixed, cheap cutoff `c = 10^9`
(50,851,223 terms, 3.5 s per stream), by moving the carrier down: taking
`T = 2 pi 10^m` puts the deficit at `Delta - ell_T = (9-m) log(10)/(2 pi)`.

The low-carrier regime is a *calibration* regime, not a search: RH is verified
far above `T = 6.3e9`, so the leading margin is known in advance to be
nonnegative and any negative output would be a bug.  What the sweep measures is
the method's sensitivity — how close to zero the exact form can be driven when
the family is given enough support — and therefore what it would cost to run the
same configuration at a carrier above the verified height.

Per-grid-point margins use `numpy.linalg.eigvalsh` and are NOMINATIONS.  The
extreme point is re-run through the full L-5602 certificate.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time

import numpy as np
from mpmath import mp, mpf, log, pi as mp_pi

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analyze_stream as A                                    # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff-power10", type=int, default=9)
    ap.add_argument("--carrier-num", type=int, default=6283185307)
    ap.add_argument("--carrier-dens", type=int, nargs="*",
                    default=[1000000, 100000, 10000, 1000, 100, 10, 1])
    ap.add_argument("--cells", type=int, nargs="*", default=[1024, 2048, 4096])
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--out", default="depth-grid.json")
    args = ap.parse_args()

    mp.dps = 40
    L = mpf(args.cutoff_power10) * log(mpf(10))
    delta = float(L / (2 * mp_pi))

    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for den in args.carrier_dens:
            T = mpf(args.carrier_num) / den
            ell = float(log(T / (2 * mp_pi)) / (2 * mp_pi))
            for k in args.cells:
                t0 = time.time()
                out = os.path.join(tmp, "s.json")
                subprocess.run(
                    [os.path.join(HERE, "carrier_stream"),
                     "--cutoff-power10", str(args.cutoff_power10),
                     "--cells", str(k), "--carrier-num", str(args.carrier_num),
                     "--carrier-den", str(den), "--threads", str(args.threads),
                     "--out", out], check=True,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                st = A.load_stream(out)
                mat = A.toeplitz_matrix(st)
                lam = float(np.linalg.eigvalsh(mat)[-1])
                errs = A.lag_error_bounds(st)
                gate = A.correction_gate(st["cutoff"], k, args.carrier_num, den)
                b_ok = gate["b_le_1_over_20"]
                rows.append({
                    "carrier": float(T), "carrier_den": den, "cells": k,
                    "Delta": delta, "ell_T": ell, "deficit": delta - ell,
                    "lambda_max_floating": lam,
                    "leading_margin_floating": ell - lam,
                    "stream_error_sum": float(sum(errs)),
                    "gate_B_total": gate["B_total_float"],
                    "b_le_1_over_20": b_ok,
                    "resolvable_against_gate":
                        abs(ell - lam) > gate["B_total_float"],
                    "seconds": round(time.time() - t0, 1),
                })
                print(f'  T={float(T):.2f} K={k} deficit={delta-ell:+.4f} '
                      f'margin={ell-lam:.6g} gate={gate["B_total_float"]:.3g} '
                      f'({rows[-1]["seconds"]}s)', flush=True)

    best = min(rows, key=lambda r: abs(r["leading_margin_floating"]))
    res = {
        "schema": "riemann.x5601-depth-grid.v1",
        "agent": "opus5-01",
        "classification": "grid margins are EMPIRICAL nominations; RH is "
                          "verified far above these carriers, so a negative "
                          "leading margin here would indicate a bug, not a "
                          "counterexample",
        "cutoff": 10 ** args.cutoff_power10,
        "Delta": delta,
        "smallest_margin": best,
        "rows": rows,
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()
