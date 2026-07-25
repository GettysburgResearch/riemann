#!/usr/bin/env python3
"""Exact audit of the PR #71 ordinate and X-5602 binary64 serialization.

Standard-library only.  No zeta evaluation is performed.
"""
from __future__ import annotations

import json
import math
import struct
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

T_NUM = 20225875608341108140435
T_DEN = 1 << 32
REPORTED_DECIMAL = Decimal("4709203636353.162109375")
REPORTED_GAMMA_LO = Decimal("4709203636353.140625")
REPORTED_GAMMA_HI = Decimal("4709203636354.134765625")


def frac_json(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def exact_decimal(x: Fraction, digits: int = 80) -> str:
    getcontext().prec = digits
    return format(Decimal(x.numerator) / Decimal(x.denominator), "f")


def float_fraction(x: float) -> Fraction:
    return Fraction.from_float(x)


def build() -> dict[str, object]:
    exact = Fraction(T_NUM, T_DEN)
    nearest = float(exact)
    nearest_q = float_fraction(nearest)
    reported_q = Fraction(REPORTED_DECIMAL)
    if nearest_q != reported_q:
        raise AssertionError((nearest_q, reported_q))

    ulp_q = float_fraction(math.ulp(nearest))
    difference = exact - nearest_q

    lo = Fraction(REPORTED_GAMMA_LO)
    hi = Fraction(REPORTED_GAMMA_HI)
    reported_gap = hi - lo
    rounded_offset = nearest_q - lo
    exact_offset_using_serialized_lo = exact - lo

    # Each absolute root is serialized by adding two binary64 values near T.
    # Even if the relative root were exact, nearest rounding alone contributes
    # at most ulp/2 to each endpoint and ulp to their difference.
    endpoint_radius = ulp_q / 2
    gap_radius = ulp_q

    # Verify the cited absolute ordinates are exactly on the local binary64 grid.
    for name, value in (("candidate", reported_q), ("gamma_lo", lo), ("gamma_hi", hi)):
        scaled = value / ulp_q
        if scaled.denominator != 1:
            raise AssertionError(f"{name} is not on the binary64 grid: {scaled}")

    return {
        "schema": "riemann.x5603-pr71-exact-ordinate-audit.v1",
        "input": {
            "t_numerator": str(T_NUM),
            "t_denominator": str(T_DEN),
        },
        "exact_ordinate": {
            "fraction": frac_json(exact),
            "decimal": exact_decimal(exact),
        },
        "binary64_ordinate_used_by_strtod": {
            "fraction": frac_json(nearest_q),
            "decimal": exact_decimal(nearest_q),
            "hex": nearest.hex(),
            "packed_hex": struct.pack(">d", nearest).hex(),
        },
        "exact_minus_binary64": {
            "fraction": frac_json(difference),
            "decimal": exact_decimal(difference),
        },
        "binary64_ulp_at_height": {
            "fraction": frac_json(ulp_q),
            "decimal": exact_decimal(ulp_q),
        },
        "reported_gap_from_serialized_endpoints": {
            "gamma_lo": frac_json(lo),
            "gamma_hi": frac_json(hi),
            "gap": frac_json(reported_gap),
            "gap_decimal": exact_decimal(reported_gap),
            "candidate_offset_if_binary64": frac_json(rounded_offset),
            "candidate_offset_for_exact_rational_using_same_serialized_lo": frac_json(exact_offset_using_serialized_lo),
            "candidate_offset_shift": frac_json(difference),
        },
        "serialization_resolution": {
            "endpoint_rounding_radius_at_least": frac_json(endpoint_radius),
            "gap_rounding_radius_at_least": frac_json(gap_radius),
            "note": (
                "These are lower-level serialization limits only. They do not include "
                "Riemann-Siegel truncation, summation, grid, or root-refinement error."
            ),
        },
        "classification": "EXACT_PROVENANCE_MISMATCH_AND_BINARY64_OUTPUT_QUANTIZATION",
        "counterexample_candidate": None,
        "proof_boundary": (
            "This file proves only rational/IEEE-754 facts. It neither confirms nor "
            "refutes the existence of the observed large zero gap."
        ),
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = build()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
