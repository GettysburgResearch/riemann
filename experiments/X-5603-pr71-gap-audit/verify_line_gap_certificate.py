#!/usr/bin/env python3
"""Exact checker for X-5603 line-gap discrepancy certificates.

The FLINT producer supplies outward dyadic balls for two consecutive Hardy-Z
zeros, exact dyadic interior endpoints, and outward balls for the total zero
counts N(a), N(b).  This checker uses only Python integers and Fraction.

It does not evaluate zeta or verify FLINT's Platt/Turing implementation.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x5603-line-gap-discrepancy.v1"
VERIFY_SCHEMA = "riemann.x5603-line-gap-discrepancy.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a base-10 integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def parse_binary(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    mantissa = parse_int(value.get("mantissa"), f"{name}.mantissa")
    exponent = parse_int(value.get("exponent"), f"{name}.exponent")
    return Fraction(mantissa << exponent, 1) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))


def parse_interval(value: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    lower = parse_binary(value.get("lower"), f"{name}.lower")
    upper = parse_binary(value.get("upper"), f"{name}.upper")
    if lower > upper:
        raise CertificateError(f"{name} lower endpoint exceeds upper endpoint")
    return lower, upper


def require_exact_interval(value: Any, name: str) -> Fraction:
    lower, upper = parse_interval(value, name)
    if lower != upper:
        raise CertificateError(f"{name} is not exact")
    return lower


def unique_integer(interval: tuple[Fraction, Fraction], name: str) -> int:
    lower, upper = interval
    # ceil(lower) and floor(upper), without float conversion.
    ceil_lower = -((-lower.numerator) // lower.denominator)
    floor_upper = upper.numerator // upper.denominator
    if ceil_lower != floor_upper:
        raise CertificateError(f"{name} does not contain a unique integer")
    return ceil_lower


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def verify(data: dict[str, Any]) -> dict[str, object]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    target = parse_fraction(data.get("target"), "target")
    lower_zero = parse_interval(data.get("lower_hardy_zero_ball"), "lower_hardy_zero_ball")
    upper_zero = parse_interval(data.get("upper_hardy_zero_ball"), "upper_hardy_zero_ball")
    a = require_exact_interval(data.get("interior_slab_lower_exact"), "interior_slab_lower_exact")
    b = require_exact_interval(data.get("interior_slab_upper_exact"), "interior_slab_upper_exact")

    if not lower_zero[1] < a:
        raise CertificateError("lower Hardy-Z ball is not strictly below the slab")
    if not a < target < b:
        raise CertificateError("exact target is not strictly inside the slab")
    if not b < upper_zero[0]:
        raise CertificateError("upper Hardy-Z ball is not strictly above the slab")

    lower_index = parse_int(data.get("lower_hardy_zero_index"), "lower_hardy_zero_index")
    upper_index = parse_int(data.get("upper_hardy_zero_index"), "upper_hardy_zero_index")
    if upper_index != lower_index + 1:
        raise CertificateError("Hardy-Z zero indices are not consecutive")

    n_lower_interval = parse_interval(data.get("N_lower_ball"), "N_lower_ball")
    n_upper_interval = parse_interval(data.get("N_upper_ball"), "N_upper_ball")
    n_lower = unique_integer(n_lower_interval, "N_lower_ball")
    n_upper = unique_integer(n_upper_interval, "N_upper_ball")
    if parse_int(data.get("N_lower"), "N_lower") != n_lower:
        raise CertificateError("N_lower field does not match its ball")
    if parse_int(data.get("N_upper"), "N_upper") != n_upper:
        raise CertificateError("N_upper field does not match its ball")

    discrepancy = n_upper - n_lower
    claimed_discrepancy = parse_int(
        data.get("total_zero_discrepancy_in_line_empty_slab"),
        "total_zero_discrepancy_in_line_empty_slab",
    )
    if discrepancy != claimed_discrepancy:
        raise CertificateError("claimed discrepancy mismatch")
    if discrepancy < 0:
        raise CertificateError("zero count decreased across the slab")
    if discrepancy > 0 and discrepancy % 2:
        raise CertificateError("positive line-empty discrepancy must be even")

    if discrepancy == 0:
        status = "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB"
        candidate = None
    else:
        status = "CERTIFIED_OFF_CRITICAL_ZERO_IN_LINE_EMPTY_SLAB_PENDING_PRIMITIVE_REPRODUCTION"
        candidate = "PENDING_INDEPENDENT_REPRODUCTION_AND_ANALYTIC_REVIEW"

    claimed_status = data.get("classification")
    producer_expected = (
        "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB"
        if discrepancy == 0
        else "CERTIFIED_OFF_CRITICAL_ZERO_IN_LINE_EMPTY_SLAB"
    )
    if claimed_status != producer_expected:
        raise CertificateError("producer classification mismatch")

    return {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": status,
        "counterexample_candidate": candidate,
        "target": fraction_json(target),
        "slab": {"lower": fraction_json(a), "upper": fraction_json(b)},
        "lower_hardy_zero_index": str(lower_index),
        "upper_hardy_zero_index": str(upper_index),
        "N_lower": str(n_lower),
        "N_upper": str(n_upper),
        "total_zero_discrepancy": str(discrepancy),
        "proof_boundary": (
            "This checker proves the finite interval/count arithmetic from supplied "
            "outward balls. It does not independently evaluate Hardy Z, zeta, or "
            "Turing counts; a positive discrepancy requires an independent primitive "
            "backend and analytic/API review before project-level promotion."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": VERIFY_SCHEMA, "verified": False, "status": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
