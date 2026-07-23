#!/usr/bin/env python3
"""Exact rational specialization of the L-0901 carrier correction bound.

The checker replaces every transcendental quantity in the L-0901 target
formula by an elementary rational majorant or minorant. It uses Python integers
and fractions.Fraction only. It does not certify the prime-side interval,
D-0801 admissibility, or the Guinand--Weil normalization.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from math import isqrt
from pathlib import Path
import sys
from typing import Any, Sequence

SCHEMA = "riemann.piecewise-carrier-variation-budget.v1"


class CertificateError(ValueError):
    """Malformed or out-of-domain certificate."""


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def widen(self, radius: Fraction) -> "Interval":
        if radius < 0:
            raise CertificateError("radius must be nonnegative")
        return Interval(self.lower - radius, self.upper + radius)


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        rational(raw.get("lower"), f"{name}.lower"),
        rational(raw.get("upper"), f"{name}.upper"),
    )


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fraction_json(value.lower), "upper": fraction_json(value.upper)}


def variation_budget(
    *, cutoff_power10: int, cells: int, carrier: Fraction
) -> dict[str, Fraction | int]:
    """Rationally upper-bound the L-0901 operator correction.

    The proof uses `pi>3`, `log(10)>2`, `log(2)<7/10`, and
    `sqrt(10**n)<ceil(sqrt(10**n))`. If
    `m=ceil(log_2(cells))`, then `log(cells)<7*m/10`.
    """
    n = cutoff_power10
    K = cells
    T = carrier
    if n < 1:
        raise CertificateError("cutoff_power10 must be positive")
    if K < 1:
        raise CertificateError("cells must be positive")
    if T <= 0:
        raise CertificateError("carrier must be positive")

    log2_cells_ceiling = (K - 1).bit_length()
    log_cells_upper = Fraction(7 * log2_cells_ceiling, 10)
    log_cutoff_lower = 2 * n
    pi_lower = 3
    sqrt_cutoff_upper = isqrt(10**n - 1) + 1

    arch_numerator = (
        Fraction(K, log_cutoff_lower) * (log_cells_upper + 2)
        + 6 * K
        + 5
        + Fraction(1, log_cutoff_lower)
    )
    arch = arch_numerator / (pi_lower * T)
    pole = (
        Fraction(4 * sqrt_cutoff_upper * K * K, pi_lower * log_cutoff_lower)
        / (T * T)
    )
    total = arch + pole
    return {
        "archimedean": arch,
        "pole": pole,
        "total": total,
        "log2_cells_ceiling": log2_cells_ceiling,
        "log_cells_upper": log_cells_upper,
        "log_cutoff_lower": log_cutoff_lower,
        "pi_lower": pi_lower,
        "sqrt_cutoff_upper": sqrt_cutoff_upper,
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    n = exact_int(data.get("cutoff_power10"), "cutoff_power10")
    K = exact_int(data.get("cells"), "cells")
    T = rational(data.get("carrier"), "carrier")
    budget = variation_budget(cutoff_power10=n, cells=K, carrier=T)
    radius = budget["total"]
    assert isinstance(radius, Fraction)

    result: dict[str, Any] = {
        "schema": SCHEMA,
        "cutoff": f"10^{n}",
        "cells": K,
        "carrier": fraction_json(T),
        "correction_budget": {
            "archimedean": fraction_json(budget["archimedean"]),
            "pole": fraction_json(budget["pole"]),
            "total": fraction_json(radius),
        },
        "rational_majorants": {
            "log2_cells_ceiling": budget["log2_cells_ceiling"],
            "log_cells_upper": fraction_json(budget["log_cells_upper"]),
            "log_cutoff_lower": budget["log_cutoff_lower"],
            "pi_lower": budget["pi_lower"],
            "sqrt_cutoff_upper": budget["sqrt_cutoff_upper"],
        },
        "scope_warning": (
            "This exact arithmetic specializes the proposed L-0901 operator "
            "bound. It does not certify the complete prime margin, D-0801 "
            "admissibility, or the Guinand--Weil normalization."
        ),
    }

    raw_margin = data.get("leading_margin_interval")
    if raw_margin is not None:
        leading = interval(raw_margin, "leading_margin_interval")
        full = leading.widen(radius)
        positive = full.lower > 0
        negative = full.upper < 0
        result.update(
            {
                "leading_margin_interval": interval_json(leading),
                "full_exact_margin_interval": interval_json(full),
                "certified_positive": positive,
                "certified_negative": negative,
                "verdict": (
                    "CERTIFIED_POSITIVE"
                    if positive
                    else "CERTIFIED_NEGATIVE"
                    if negative
                    else "UNRESOLVED"
                ),
            }
        )
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    if result.get("certified_negative") or result.get("certified_positive"):
        return 0
    return 1 if "leading_margin_interval" in result else 0


if __name__ == "__main__":
    raise SystemExit(main())
