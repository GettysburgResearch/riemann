#!/usr/bin/env python3
"""Exact rational checker for omitted D-0801 archimedean/pole corrections.

The checker implements the universal bound proved in L-2802 for an equal-cell
piecewise carrier with cutoff c=10**n, K cells, and exact rational carrier T.
It uses only Python integers and fractions.Fraction. It does *not* certify the
prime-side interval supplied by another producer, nor the Guinand--Weil
normalization. Its role is to combine a separately certified leading-margin
interval with a rigorous radius enclosing the omitted exact archimedean and
pole corrections.
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

SCHEMA = "riemann.piecewise-carrier-correction-budget.v1"


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


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fraction_json(value.lower), "upper": fraction_json(value.upper)}


def correction_budget(*, cutoff_power10: int, cells: int, carrier: Fraction) -> dict[str, Fraction | int]:
    """Return the exact rational L-2802 correction budget.

    The proof uses only the coarse certified inequalities

        3 < pi,
        2*n < log(10**n) < 3*n,
        log(x) < bit_length(ceil(x))  for x >= 1.

    The four returned radii respectively cover the central Fourier mass, the
    remote Fourier tail, the pointwise digamma asymptotic, and the pole term.
    """
    n = cutoff_power10
    K = cells
    T = carrier
    if n < 1:
        raise CertificateError("cutoff_power10 must be positive")
    if K < 1:
        raise CertificateError("cells must be positive")
    if T < 10:
        raise CertificateError("carrier must be at least 10")

    # L=log(c)>2*n implies the Fourier-bound crossover u0=2K/L is < K/n.
    # The central/tail split requires u0<T/2.
    if 2 * K >= n * T:
        raise CertificateError("carrier is too small for the certified central/tail split")

    # Upper integer logarithm surrogates. Since log(2)<1, log(x) is strictly
    # below the binary bit length of ceil(x) for every x>=1.
    ratio_upper = T * Fraction(3 * n, 4 * K)
    if ratio_upper <= 1:
        raise CertificateError("log-ratio upper argument must exceed one")
    log_ratio_upper = ceil_fraction(ratio_upper).bit_length()
    log_T_upper = ceil_fraction(T).bit_length()
    log_3T2_upper = ceil_fraction(Fraction(3, 2) * T).bit_length()

    # L-2802, central part. M1 bounds E_mu[|u|; |u|<=T/2].
    first_moment = Fraction(K * K, 3 * n) * (1 + 2 * log_ratio_upper)
    central = Fraction(2, 3) * first_moment / T

    # L-2802, tail part after integrating (constant + logarithm)/u^2.
    tail_bracket = 30 + 2 * log_3T2_upper + 2 * log_T_upper
    tail = Fraction(2 * K * K, 9 * n) * tail_bracket / T

    # Binet's formula gives a much smaller term; 1/T is a deliberately coarse
    # rational majorant that avoids importing any transcendental constant.
    pointwise = Fraction(1, 1) / T

    c = 10**n
    sqrt_c_upper = isqrt(c - 1) + 1
    pole = Fraction(2 * K * K * sqrt_c_upper, 3 * n) / (T * T)

    total = central + tail + pointwise + pole
    return {
        "central": central,
        "tail": tail,
        "pointwise": pointwise,
        "pole": pole,
        "total": total,
        "log_ratio_upper": log_ratio_upper,
        "log_T_upper": log_T_upper,
        "log_3T2_upper": log_3T2_upper,
        "sqrt_c_upper": sqrt_c_upper,
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    n = exact_int(data.get("cutoff_power10"), "cutoff_power10")
    K = exact_int(data.get("cells"), "cells")
    T = rational(data.get("carrier"), "carrier")
    budget = correction_budget(cutoff_power10=n, cells=K, carrier=T)
    radius = budget["total"]
    assert isinstance(radius, Fraction)

    result: dict[str, Any] = {
        "schema": SCHEMA,
        "cutoff": f"10^{n}",
        "cells": K,
        "carrier": fraction_json(T),
        "correction_budget": {
            "central": fraction_json(budget["central"]),
            "tail": fraction_json(budget["tail"]),
            "pointwise": fraction_json(budget["pointwise"]),
            "pole": fraction_json(budget["pole"]),
            "total": fraction_json(radius),
        },
        "integer_majorants": {
            "log_ratio_upper": budget["log_ratio_upper"],
            "log_T_upper": budget["log_T_upper"],
            "log_3T2_upper": budget["log_3T2_upper"],
            "sqrt_cutoff_upper": budget["sqrt_c_upper"],
        },
        "scope_warning": (
            "This proves only the L-2802 archimedean-plus-pole correction radius. "
            "A separate directed producer must certify the leading prime margin, "
            "the exact test normalization, and every phase enclosure."
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
    if result.get("certified_negative"):
        return 0
    if result.get("certified_positive"):
        return 0
    return 1 if "leading_margin_interval" in result else 0


if __name__ == "__main__":
    raise SystemExit(main())
