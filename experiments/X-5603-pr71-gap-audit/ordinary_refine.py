#!/usr/bin/env python3
"""Ordinary high-precision refinement of the two line zeros around PR #71.

This is a deterministic discovery/provenance tool, not directed arithmetic.
The final proof route is flint_line_gap_discrepancy.c.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

T_NUM = 20225875608341108140435
T_DEN = 1 << 32
ROOT_BRACKETS = (
    ("4709203636353.13", "4709203636353.15"),
    ("4709203636354.12", "4709203636354.15"),
)


def false_position(a: mp.mpf, b: mp.mpf, steps: int = 5):
    fa = mp.siegelz(a)
    fb = mp.siegelz(b)
    if fa * fb >= 0:
        raise ValueError("initial interval does not have opposite signs")
    for _ in range(steps):
        x = (a * fb - b * fa) / (fb - fa)
        fx = mp.siegelz(x)
        if fa * fx <= 0:
            b, fb = x, fx
        else:
            a, fa = x, fx
    return a, b, fa, fb


def bisect(a: mp.mpf, b: mp.mpf, fa: mp.mpf, fb: mp.mpf, steps: int = 24):
    for _ in range(steps):
        mid = (a + b) / 2
        fm = mp.siegelz(mid)
        if fa * fm <= 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return a, b, fa, fb


def text(x: mp.mpf, digits: int = 50) -> str:
    return mp.nstr(x, digits)


def build() -> dict[str, object]:
    mp.mp.dps = 25
    refined = []
    for left, right in ROOT_BRACKETS:
        a, b, fa, fb = false_position(mp.mpf(left), mp.mpf(right))
        a, b, fa, fb = bisect(a, b, fa, fb)
        refined.append((a, b, fa, fb))

    target = mp.mpf(T_NUM) / T_DEN
    lower_mid = (refined[0][0] + refined[0][1]) / 2
    upper_mid = (refined[1][0] + refined[1][1]) / 2
    gap = upper_mid - lower_mid
    normalized = gap * mp.log(target / (2 * mp.pi)) / (2 * mp.pi)

    def root_json(item):
        a, b, fa, fb = item
        return {
            "lower": text(a),
            "upper": text(b),
            "width": text(b - a, 20),
            "Z_lower": text(fa, 20),
            "Z_upper": text(fb, 20),
            "midpoint": text((a + b) / 2),
        }

    return {
        "schema": "riemann.x5603-pr71-ordinary-root-refinement.v1",
        "classification": "EMPIRICAL_HIGH_PRECISION_NOT_DIRECTED",
        "backend": "mpmath.siegelz ordinary arbitrary precision",
        "working_decimal_digits": 25,
        "algorithm": "5 false-position steps followed by 24 bisections per root",
        "exact_target": {
            "numerator": str(T_NUM),
            "denominator": str(T_DEN),
            "decimal": text(target),
        },
        "lower_line_zero": root_json(refined[0]),
        "upper_line_zero": root_json(refined[1]),
        "geometry_from_bracket_midpoints": {
            "target_minus_lower": text(target - lower_mid),
            "upper_minus_target": text(upper_mid - target),
            "gap": text(gap),
            "gap_in_local_mean_spacings": text(normalized),
        },
        "counterexample_candidate": None,
        "proof_boundary": (
            "The sign brackets use ordinary mpmath arithmetic and are not interval "
            "certificates. They correct the binary64 provenance and nominate the exact "
            "slab for the independent FLINT Platt/Turing producer."
        ),
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = build()
    raw = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(raw, encoding="utf-8")
    else:
        print(raw, end="")


if __name__ == "__main__":
    main()
