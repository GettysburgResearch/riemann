#!/usr/bin/env python3
"""Directed Arb endpoint signs; requires python-flint==0.9.0."""
from __future__ import annotations

import argparse
import json
import platform
from fractions import Fraction
from pathlib import Path

import flint
from flint import acb, arb, ctx


ENDPOINT_SIGNS = {14: -1, 15: 1, 20: 1, 21: 1, 22: -1,
                  25: -1, 26: 1, 30: 1, 31: -1, 32: -1, 33: 1,
                  37: 1, 38: -1, 40: -1, 41: 1, 43: 1, 44: -1,
                  48: -1, 49: 1, Fraction(99, 2): 1, 50: -1,
                  52: -1, 53: 1, 56: 1, 57: -1, 59: -1, 60: 1,
                  Fraction(121, 2): 1, 61: -1, 65: -1, 66: 1,
                  67: 1, 68: -1}
ANCHORS = ((14, 15), (21, 22), (25, 26), (30, 31), (32, 33),
           (37, 38), (40, 41), (43, 44), (48, 49), (Fraction(99, 2), 50),
           (52, 53), (56, 57), (59, 60), (Fraction(121, 2), 61),
           (65, 66), (67, 68))


def exact_json(value: int | Fraction) -> int | str:
    """Keep integer values numeric and nonintegral values exact rational strings."""
    value = Fraction(value)
    return value.numerator if value.denominator == 1 else str(value)


def certificate(precision: int) -> dict:
    if precision < 96:
        raise ValueError("Use at least 96 bits for these endpoint certificates")
    ctx.prec = precision
    records = []
    for t, sign in ENDPOINT_SIGNS.items():
        rational_t = Fraction(t)
        ball_t = arb(rational_t.numerator) / rational_t.denominator
        # Exact rational inputs; all subsequent operations enclose their values.
        theta = acb(arb(1) / 4, ball_t / 2).lgamma().imag
        theta -= (ball_t / 2) * arb.pi().log()
        z = acb(arb(1) / 2, ball_t).zeta() * acb(0, theta).exp()
        proved_sign = (z.real > 0) if sign > 0 else (z.real < 0)
        if not proved_sign or not z.imag.contains(0):
            raise RuntimeError(f"Uncertified Hardy-Z endpoint at t={t}: {z}")
        records.append({"t": exact_json(t), "sign": sign,
                        "real_enclosure": str(z.real),
                        "imaginary_enclosure": str(z.imag)})
    for left, right in ANCHORS:
        if ENDPOINT_SIGNS[left] == ENDPOINT_SIGNS[right]:
            raise RuntimeError("Anchor endpoints must have opposite signs")
    return {"status": "DIRECTED_INTERVAL_ENDPOINT_CERTIFICATE",
            "python": platform.python_version(), "python_flint": flint.__version__,
            "precision_bits": precision, "endpoints": records,
            "critical_ordinate_intervals": [[exact_json(a), exact_json(b)] for a, b in ANCHORS],
            "critical_squared_ordinate_intervals": [[exact_json(a*a), exact_json(b*b)] for a, b in ANCHORS],
            "scope": "Existence of at least one critical-line zero in each open interval; no simplicity or completeness claim"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = certificate(args.precision)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
