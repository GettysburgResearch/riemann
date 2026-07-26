#!/usr/bin/env python3
"""Exact negative-witness checker for one positive-anchor b0 interval.

The checker derives rational Schur witness directions from exact midpoints of the
old directed moment boxes, then contracts those fixed directions against the
full old boxes and the supplied directed b0 interval. A strict negative upper
endpoint is a rigorous finite separation. A nonnegative result in these two
fixed directions does not by itself prove positivity of the complete new cone.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
import sys
from typing import Any, Iterable

from positive_anchor import (
    GateError,
    Interval as MomentInterval,
    fraction_json,
    load_basis,
    parse_anchor,
    positive_anchor_gate,
)

SCHEMA = "riemann.x9312-positive-anchor-b0.v1"
OUTPUT_SCHEMA = "riemann.x9312-positive-anchor-schur-witness.v1"


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise GateError("reversed candidate interval")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def scale(self, scalar: Fraction) -> "Interval":
        if scalar >= 0:
            return Interval(self.lower * scalar, self.upper * scalar)
        return Interval(self.upper * scalar, self.lower * scalar)


def parse_fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise GateError(f"{name} must be an object")
    num, den = raw.get("numerator"), raw.get("denominator")
    if (
        isinstance(num, bool)
        or not isinstance(num, int)
        or isinstance(den, bool)
        or not isinstance(den, int)
        or den <= 0
    ):
        raise GateError(f"bad rational at {name}")
    return Fraction(num, den)


def parse_interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise GateError(f"{name} must be an object")
    return Interval(
        parse_fraction(raw.get("lower"), f"{name}.lower"),
        parse_fraction(raw.get("upper"), f"{name}.upper"),
    )


def as_interval(value: MomentInterval) -> Interval:
    return Interval(value.lower, value.upper)


def linear_combination(
    coefficients: Iterable[Fraction], values: Iterable[Interval]
) -> Interval:
    result = Interval(Fraction(0), Fraction(0))
    for coefficient, value in zip(coefficients, values):
        result = result.add(value.scale(coefficient))
    return result


def verify(
    basis_data: dict[str, Any],
    moments: list[MomentInterval],
    candidate: dict[str, Any],
) -> dict[str, Any]:
    if candidate.get("schema") != SCHEMA:
        raise GateError(f"candidate schema must equal {SCHEMA}")
    anchor = parse_fraction(candidate.get("anchor"), "anchor")
    if anchor <= 0:
        raise GateError("anchor must be positive")
    b0 = parse_interval(candidate.get("b0_interval"), "b0_interval")

    midpoint_moments = [value.midpoint for value in moments]
    gate = positive_anchor_gate(midpoint_moments, anchor)
    m = gate["m"]
    x0 = gate["lower_solve"]
    x1 = gate["upper_solve"]
    a = [as_interval(value) for value in moments]

    lower_value = b0
    lower_value = lower_value.add(
        linear_combination([-2 * value for value in x0], a[:m])
    )
    for i in range(m):
        for j in range(m):
            entry = a[i + j + 1].add(a[i + j].scale(anchor))
            lower_value = lower_value.add(entry.scale(x0[i] * x0[j]))

    upper_value = a[0].add(b0.scale(-anchor))
    upper_value = upper_value.add(
        linear_combination([-2 * value for value in x1], a[1 : m + 1])
    )
    for i in range(m):
        for j in range(m):
            entry = a[i + j + 2].add(a[i + j + 1].scale(anchor))
            upper_value = upper_value.add(entry.scale(x1[i] * x1[j]))

    lower_negative = lower_value.upper < 0
    upper_negative = upper_value.upper < 0
    if lower_negative and upper_negative:
        verdict = "CERTIFIED_NEGATIVE_BOTH_SCHUR_SQUARES"
    elif lower_negative:
        verdict = "CERTIFIED_NEGATIVE_LOWER_SQUARE"
    elif upper_negative:
        verdict = "CERTIFIED_NEGATIVE_UPPER_Y_SQUARE"
    else:
        verdict = "NO_CERTIFIED_NEGATIVE_FROM_MIDPOINT_SCHUR_DIRECTIONS"

    return {
        "schema": OUTPUT_SCHEMA,
        "anchor": fraction_json(anchor),
        "b0_interval": {
            "lower": fraction_json(b0.lower),
            "upper": fraction_json(b0.upper),
        },
        "midpoint_gate": {
            "lower": fraction_json(gate["lower"]),
            "upper": fraction_json(gate["upper"]),
        },
        "lower_square_interval": {
            "lower": fraction_json(lower_value.lower),
            "upper": fraction_json(lower_value.upper),
        },
        "upper_y_square_interval": {
            "lower": fraction_json(upper_value.lower),
            "upper": fraction_json(upper_value.upper),
        },
        "lower_witness_adapted_coefficients": [
            fraction_json(Fraction(1)),
            *[fraction_json(-value) for value in x0],
        ],
        "upper_witness_adapted_coefficients": [
            fraction_json(Fraction(1)),
            *[fraction_json(-value) for value in x1],
        ],
        "verdict": verdict,
        "certified_negative": lower_negative or upper_negative,
        "counterexample_candidate": None,
        "scope_warning": (
            "A strict negative interval is an exact finite response separation, but "
            "RH promotion still inherits L-9308 and the direct-xi/count-deflation "
            "theorem chain. A nonnegative result here does not prove the full new "
            "cone positive."
        ),
        "source": {
            "basis_schema": basis_data.get("schema"),
            "primitive_sha256": basis_data.get("primitive_sha256"),
            "ordinate": basis_data.get("ordinate"),
            "primitive_shift": basis_data.get("primitive_shift"),
        },
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("basis", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        basis_data, moments = load_basis(args.basis)
        candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
        if not isinstance(candidate, dict):
            raise GateError("candidate file must contain an object")
        result = verify(basis_data, moments, candidate)
    except (OSError, json.JSONDecodeError, GateError, ZeroDivisionError) as exc:
        print(
            json.dumps({"verified": False, "error": str(exc)}, indent=2),
            file=sys.stderr,
        )
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0 if result["certified_negative"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
