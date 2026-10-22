#!/usr/bin/env python3
"""Optimized radix-five annular regression for L-90016 / T-90012."""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "X-90015-annular-endpoint" / "verify.py"
spec = importlib.util.spec_from_file_location("x90015", BASE)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load {BASE}")
x90015 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x90015)

RADIX = 5
ANNULUS = RADIX ** 3


def constants() -> dict:
    mp.mp.dps = 80
    half = mp.mpf("0.5")

    def xi(s):
        return (
            mp.mpf("0.5") * s * (s - 1)
            * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2) * mp.zeta(s)
        )

    zeta_half = mp.zeta(half)
    square_mass = mp.diff(lambda s: mp.log(xi(s)), half, 2)
    q = 1 / mp.sqrt(5)
    moat = (1 + zeta_half) / 2 * (1 - q) * mp.log(5) ** 2
    zero_bound = 4 * (1 + q) * square_mass
    margin = moat + zero_bound
    scaled_margin = mp.sqrt(5) * margin
    if not margin < mp.mpf("-0.062"):
        raise AssertionError("unscaled radix-five margin failed")
    if not scaled_margin < mp.mpf("-0.138"):
        raise AssertionError("scaled radix-five margin failed")
    return {
        "moat": mp.nstr(moat, 60),
        "zero_bound": mp.nstr(zero_bound, 60),
        "margin_upper_bound": mp.nstr(margin, 60),
        "scaled_margin_upper_bound": mp.nstr(scaled_margin, 60),
    }


def value(a: np.ndarray, x: int) -> float:
    q = 1.0 / math.sqrt(5.0)
    return float(
        a[x - 1]
        - (2.0 + q) * a[x // 5 - 1]
        + (1.0 + 2.0 * q) * a[x // 25 - 1]
        - q * a[x // 125 - 1]
    )


def scan(max_x: int) -> dict:
    if max_x < ANNULUS:
        raise ValueError(f"--max-x must be at least {ANNULUS}")
    a, _, _ = x90015.endpoint_sequence(max_x)
    xs = np.arange(ANNULUS, max_x + 1, ANNULUS, dtype=np.int64)
    vals = np.array([value(a, int(x)) for x in xs])
    nonnegative = xs[np.flatnonzero(vals >= 0)]
    if list(map(int, nonnegative)) != [125]:
        raise AssertionError(
            f"unexpected nonnegative radix-five endpoints: {list(map(int, nonnegative[:20]))}"
        )
    if not np.all(vals[xs >= 250] < 0):
        bad = int(xs[(xs >= 250) & (vals >= 0)][0])
        raise AssertionError(f"nonnegative radix-five value after the finite base at X={bad}")
    imax = int(np.argmax(vals))
    imin = int(np.argmin(vals))
    return {
        "max_X": max_x,
        "annulus_factor": ANNULUS,
        "tested_multiples": int(len(xs)),
        "nonnegative_endpoints": [int(x) for x in nonnegative],
        "maximum": {"X": int(xs[imax]), "value": float(vals[imax])},
        "minimum": {"X": int(xs[imin]), "value": float(vals[imin])},
        "last": {"X": int(xs[-1]), "value": float(vals[-1])},
        "all_aligned_endpoints_from_250_negative": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=1_000_000)
    parser.add_argument(
        "--output", type=Path,
        default=HERE / "results" / "verification.json",
    )
    args = parser.parse_args()
    result = {
        "classification": "PASS_RADIX5_FACTOR125_ANNULAR_REGRESSION",
        "constants": constants(),
        "finite": scan(args.max_x),
        "scope": (
            "The constant inequalities and finite scan authenticate L-90016/T-90012; "
            "the scan does not prove RH or the eventual sign."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(args.output)


if __name__ == "__main__":
    main()
