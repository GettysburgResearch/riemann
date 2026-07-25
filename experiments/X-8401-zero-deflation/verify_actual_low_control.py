#!/usr/bin/env python3
"""Standard-library replay of the actual first-zero scalar-deflation control."""
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
    if data.get("schema") != "riemann.zero-deflation.actual-low-control.v1":
        raise SystemExit("wrong schema")

    x = rational(data["sample"]["x"])
    sample_t = rational(data["sample"]["t"])
    zero_lower = rational(data["critical_line_zero_bin"]["lower"])
    zero_upper = rational(data["critical_line_zero_bin"]["upper"])
    if not (
        x > 0
        and zero_lower <= sample_t <= zero_upper
        and data["critical_line_zero_bin"]["count_lower"] == 1
    ):
        raise SystemExit("bad sample/bin")

    xi_lower, xi_upper = interval(data["f_via_xi"]["real"])
    parts_lower, parts_upper = interval(data["f_via_parts"]["real"])
    f_lower, f_upper = max(xi_lower, parts_lower), min(xi_upper, parts_upper)
    if f_lower > f_upper:
        raise SystemExit("disjoint F assemblies")
    if (f_lower, f_upper) != interval(data["f_real_intersection"]):
        raise SystemExit("false F intersection")
    if rational(data["zeta_abs_lower"]) <= 0 or rational(data["xi_abs_lower"]) <= 0:
        raise SystemExit("denominator gate failed")

    distance = max(abs(sample_t - zero_lower), abs(sample_t - zero_upper))
    subtraction = x / (x * x + distance * distance)
    residual = (f_lower - subtraction, f_upper - subtraction)
    if subtraction != rational(data["subtracted_poisson_lower"]):
        raise SystemExit("false subtraction")
    if residual != interval(data["residual_interval"]):
        raise SystemExit("false residual")
    if residual[0] <= 0 or data["status"] != "CERTIFIED_POSITIVE_NUMERICAL_CONTROL":
        raise SystemExit("wrong sign/status")

    print(
        json.dumps(
            {
                "verified": True,
                "residual_lower": str(residual[0]),
                "residual_upper": str(residual[1]),
                "subtracted_lower": str(subtraction),
                "status": data["status"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
