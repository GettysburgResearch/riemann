#!/usr/bin/env python3
"""Q-5602 — certified-margin scan over the carrier at a fixed cutoff.

Agent: opus5-01   Issue: #55

The cutoff ladder of O-5601 shows the D-0801 margin shrinking smoothly and
predictably with `c`.  The carrier is the interesting parameter: the prime side
is an oscillatory function of `T`, and a carrier where `lambda_max(S_K)` comes
anomalously close to `ell_T` is a window in which the zeros conspire — exactly
what a counterexample search wants to find.

This driver runs one complete directed stream per carrier and records the
floating margin `ell_T - lambda_max(S_K)`.  Those per-carrier values are
**nominations only**; the minimum-margin carrier is then re-run through the full
L-5602 certificate, which is the only number allowed to carry a sign claim.

Carriers are exact rationals `num/den` so the producer's exact-rational carrier
path is used throughout.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile

import numpy as np
from mpmath import mp, mpf, log, pi as mp_pi

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analyze_stream as A                                    # noqa: E402


def ell_of(num: int, den: int) -> float:
    mp.dps = 40
    return float(log(mpf(num) / mpf(den) / (2 * mp_pi)) / (2 * mp_pi))


def one_carrier(num, den, power10, cells, threads, tmp):
    out = os.path.join(tmp, "s.json")
    subprocess.run([os.path.join(HERE, "carrier_stream"),
                    "--cutoff-power10", str(power10), "--cells", str(cells),
                    "--carrier-num", str(num), "--carrier-den", str(den),
                    "--threads", str(threads), "--out", out], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    st = A.load_stream(out)
    mat = A.toeplitz_matrix(st)
    lam = float(np.linalg.eigvalsh(mat)[-1])
    return st, lam


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff-power10", type=int, default=8)
    ap.add_argument("--cells", type=int, default=1024)
    ap.add_argument("--base-num", type=int, default=94184072727073)
    ap.add_argument("--den", type=int, default=20)
    ap.add_argument("--step-num", type=int, default=4)       # 0.2 in T
    ap.add_argument("--count", type=int, default=256)
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--out", default="carrier-scan.json")
    args = ap.parse_args()

    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for m in range(args.count):
            num = args.base_num + m * args.step_num
            st, lam = one_carrier(num, args.den, args.cutoff_power10,
                                  args.cells, args.threads, tmp)
            ell = ell_of(num, args.den)
            rows.append({"m": m, "num": num, "carrier": num / args.den,
                         "ell_T": ell, "lambda_max": lam,
                         "margin_floating": ell - lam})
            if m % 16 == 0:
                print(f"  m={m:4d} T={num/args.den:.2f} "
                      f"margin={ell - lam:.9g}", flush=True)

    margins = np.array([r["margin_floating"] for r in rows])
    best = int(np.argmin(margins))
    worst = int(np.argmax(margins))

    # certify the extreme carrier properly
    with tempfile.TemporaryDirectory() as tmp:
        num = rows[best]["num"]
        out = os.path.join(tmp, "best.json")
        subprocess.run([os.path.join(HERE, "carrier_stream"),
                        "--cutoff-power10", str(args.cutoff_power10),
                        "--cells", str(args.cells),
                        "--carrier-num", str(num), "--carrier-den", str(args.den),
                        "--threads", str(args.threads), "--out", out], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cert_path = os.path.join(tmp, "cert.json")
        subprocess.run([sys.executable, os.path.join(HERE, "analyze_stream.py"),
                        out, "--grid-log2", "20", "--freeze-bits", "64",
                        "--out", cert_path], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with open(cert_path) as fh:
            cert = json.load(fh)
        cert.pop("frozen_vectors", None)

    res = {
        "schema": "riemann.x5601-carrier-scan.v1",
        "agent": "opus5-01",
        "classification": "per-carrier margins are EMPIRICAL nominations; "
                          "only 'certified_minimum' carries a sign claim",
        "cutoff": 10 ** args.cutoff_power10,
        "cells": args.cells,
        "carrier_denominator": args.den,
        "carrier_step": args.step_num / args.den,
        "carriers_scanned": args.count,
        "carrier_range": [rows[0]["carrier"], rows[-1]["carrier"]],
        "margin_min": float(margins.min()),
        "margin_max": float(margins.max()),
        "margin_mean": float(margins.mean()),
        "margin_std": float(margins.std()),
        "min_at": rows[best],
        "max_at": rows[worst],
        "certified_minimum": {
            "carrier": f'{rows[best]["num"]}/{args.den}',
            "lambda_max_upper_certified": cert["lambda_max_upper_certified"],
            "universal_margin_lower": cert["universal_margin_lower"],
            "universal_positivity_certified": cert["universal_positivity_certified"],
            "correction_gate": cert["correction_gate"],
        },
        "rows": rows,
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    show = {k: v for k, v in res.items() if k != "rows"}
    print(json.dumps(show, indent=1))


if __name__ == "__main__":
    main()
