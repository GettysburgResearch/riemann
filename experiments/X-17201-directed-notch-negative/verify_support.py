#!/usr/bin/env python3
"""Exact-rational checker for one small frozen support interval.

This is intentionally slow.  It is useful for sign checks and producer
regressions, not for the large 10^7 discovery manifest.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from filter_core import (
    Q,
    directed_q_interval,
    log_integer_interval,
    manifest_digest,
    prime_power_events,
    qtext,
    standard_spec,
)
from rh_bound import certificate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", default="10")
    parser.add_argument("--radius", default="1/1000000")
    parser.add_argument("--cutoff", type=int, default=10_000)
    parser.add_argument("--dyadic-level", type=int, default=3)
    parser.add_argument("--notches", type=int, default=2)
    parser.add_argument("--highpass-order", type=int, default=0)
    parser.add_argument("--highpass-delta-power", type=int, default=6)
    parser.add_argument("--log-terms", type=int, default=64)
    parser.add_argument("--sqrt-bits", type=int, default=128)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    center = Q(args.x)
    radius = Q(args.radius)
    if radius < 0:
        raise SystemExit("radius must be nonnegative")
    x_interval = center - radius, center + radius
    spec = standard_spec(
        dyadic_level=args.dyadic_level,
        notch_count=args.notches,
        highpass_order=args.highpass_order,
        highpass_delta=Q(1, 1 << args.highpass_delta_power),
    )

    # A deterministic all-integer cutoff completeness check.
    next_log = log_integer_interval(args.cutoff + 1, args.log_terms)
    required_log_upper = x_interval[1] - spec.support_min
    if next_log[0] <= required_log_upper:
        raise SystemExit(
            "cutoff is not proved complete: increase it until "
            "log(cutoff+1)_lower > x_upper-support_min"
        )

    events = prime_power_events(args.cutoff)
    q_interval, used = directed_q_interval(
        x_interval,
        spec,
        events,
        log_terms=args.log_terms,
        sqrt_bits=args.sqrt_bits,
    )
    rh = certificate(spec)
    b = Q(int(rh["B_G"]["numerator"]), int(rh["B_G"]["denominator"]))
    inf_abs = Q(0)
    sign = 0
    if q_interval[0] > 0:
        inf_abs = q_interval[0]
        sign = 1
    elif q_interval[1] < 0:
        inf_abs = -q_interval[1]
        sign = -1

    result = {
        "classification": "EXACT_RATIONAL_OUTWARD_INTERVAL",
        "x_interval": [qtext(x_interval[0]), qtext(x_interval[1])],
        "x_interval_decimal": [float(x_interval[0]), float(x_interval[1])],
        "filter": rh["filter"],
        "manifest": {
            "cutoff": args.cutoff,
            "prime_power_count": len(events),
            "used_count": used,
            "sha256": manifest_digest(events),
            "cutoff_completeness": {
                "log_cutoff_plus_one_lower": qtext(next_log[0]),
                "required_strict_lower_bound": qtext(required_log_upper),
                "proved": True,
            },
        },
        "arithmetic": {
            "log_atanh_terms": args.log_terms,
            "reciprocal_sqrt_bits": args.sqrt_bits,
            "spline_term_count_before_knot_aggregation": 3 ** len(spec.widths),
        },
        "Q_interval": [qtext(q_interval[0]), qtext(q_interval[1])],
        "Q_interval_decimal": [float(q_interval[0]), float(q_interval[1])],
        "sign": sign,
        "inf_abs_lower": qtext(inf_abs),
        "inf_abs_lower_decimal": float(inf_abs),
        "B_G": rh["B_G"],
        "strict_exceedance": bool(inf_abs > b),
        "verdict": "EXACT_SIGN_ONLY" if sign else "UNRESOLVED",
        "proof_boundary": (
            "The finite prime/window interval is exact rational and outward. The RH "
            "comparison inherits the explicit-formula and HSW source dependencies "
            "declared by rh_bound.py."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
