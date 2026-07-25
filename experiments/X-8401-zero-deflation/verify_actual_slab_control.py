#!/usr/bin/env python3
"""Standard-library replay of the actual total-slab-count deflation control."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def rational(raw: dict[str, str]) -> Fraction:
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


def interval(raw: dict[str, object]) -> tuple[Fraction, Fraction]:
    lower, upper = rational(raw["lower"]), rational(raw["upper"])
    if lower > upper:
        raise ValueError("reversed interval")
    return lower, upper


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    if data.get("schema") != "riemann.zero-deflation.actual-slab-control.v1":
        raise SystemExit("wrong schema")

    lower_t = rational(data["slab"]["lower"])
    upper_t = rational(data["slab"]["upper"])
    lower_count = int(data["slab"]["N_lower"])
    upper_count = int(data["slab"]["N_upper"])
    count_difference = int(data["slab"]["count_difference"])
    if not (
        lower_t < upper_t
        and count_difference == upper_count - lower_count
        and count_difference > 0
    ):
        raise SystemExit("bad slab count")
    if interval(data["slab"]["N_lower_ball"]) != (
        Fraction(lower_count),
        Fraction(lower_count),
    ) or interval(data["slab"]["N_upper_ball"]) != (
        Fraction(upper_count),
        Fraction(upper_count),
    ):
        raise SystemExit("nonexact count balls")
    if any(rational(value) <= 0 for value in data["slab"]["endpoint_zeta_abs_lower"]):
        raise SystemExit("endpoint zero gate failed")

    x = rational(data["sample"]["x"])
    sample_t = rational(data["sample"]["t"])
    xi_lower, xi_upper = interval(data["f_via_xi"]["real"])
    parts_lower, parts_upper = interval(data["f_via_parts"]["real"])
    f_lower, f_upper = max(xi_lower, parts_lower), min(xi_upper, parts_upper)
    if f_lower > f_upper or (f_lower, f_upper) != interval(data["f_real_intersection"]):
        raise SystemExit("bad F intersection")
    if rational(data["zeta_abs_lower"]) <= 0 or rational(data["xi_abs_lower"]) <= 0:
        raise SystemExit("sample denominator gate failed")

    distance = max(abs(sample_t - lower_t), abs(sample_t - upper_t))
    subtraction = count_difference * x / (x * x + distance * distance)
    residual = (f_lower - subtraction, f_upper - subtraction)
    if subtraction != rational(data["subtracted_poisson_lower"]):
        raise SystemExit("false subtraction")
    if residual != interval(data["residual_interval"]):
        raise SystemExit("false residual")
    if residual[0] <= 0 or data["status"] != "CERTIFIED_POSITIVE_SLAB_COUNT_CONTROL":
        raise SystemExit("wrong result")

    print(
        json.dumps(
            {
                "verified": True,
                "count_difference": count_difference,
                "subtracted_lower": str(subtraction),
                "residual_lower": str(residual[0]),
                "residual_upper": str(residual[1]),
                "status": data["status"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
