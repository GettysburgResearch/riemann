#!/usr/bin/env python3
"""Exact rational checker for finite Li-coefficient interval certificates.

Supported methods:
- local: combine dyadic intervals in the finite recurrence of L-0401;
- cauchy_dft: widen an exact sampled DFT interval by L-0402's alias bound.

The checker uses integers and fractions.Fraction only.  It verifies interval
propagation, not the analytic provenance of supplied enclosures.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
from typing import Any, Sequence

SCHEMA = "riemann.li-dyadic.v1"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def scale(self, scalar: int | Fraction) -> "Interval":
        scalar = Fraction(scalar)
        if scalar >= 0:
            return Interval(scalar * self.lower, scalar * self.upper)
        return Interval(scalar * self.upper, scalar * self.lower)

    def widen(self, radius: Fraction) -> "Interval":
        if radius < 0:
            raise CertificateError("widening radius must be nonnegative")
        return Interval(self.lower - radius, self.upper + radius)


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def dyadic_value(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    bits = exact_int(raw.get("scale_bits"), f"{name}.scale_bits")
    if bits < 0:
        raise CertificateError(f"{name}.scale_bits must be nonnegative")
    return Fraction(numerator, 1 << bits)


def dyadic_interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    lo = exact_int(raw.get("lower_num"), f"{name}.lower_num")
    hi = exact_int(raw.get("upper_num"), f"{name}.upper_num")
    bits = exact_int(raw.get("scale_bits"), f"{name}.scale_bits")
    if bits < 0:
        raise CertificateError(f"{name}.scale_bits must be nonnegative")
    denominator = 1 << bits
    return Interval(Fraction(lo, denominator), Fraction(hi, denominator))


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fraction_json(value.lower), "upper": fraction_json(value.upper)}


def verify_local(data: dict[str, Any], n: int) -> tuple[Interval, dict[str, Any]]:
    raw = data.get("local")
    if not isinstance(raw, dict):
        raise CertificateError("local object is required")
    a1 = dyadic_interval(raw.get("a1"), "local.a1")
    entries = raw.get("B")
    if not isinstance(entries, list):
        raise CertificateError("local.B must be a list")

    table: dict[int, Interval] = {}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise CertificateError(f"local.B[{index}] must be an object")
        k = exact_int(entry.get("k"), f"local.B[{index}].k")
        if not 2 <= k <= n:
            raise CertificateError(f"local.B[{index}].k must satisfy 2 <= k <= {n}")
        if k in table:
            raise CertificateError(f"duplicate B_{k} interval")
        table[k] = dyadic_interval(entry.get("interval"), f"local.B[{index}].interval")

    expected = set(range(2, n + 1))
    missing = sorted(expected - table.keys())
    extra = sorted(table.keys() - expected)
    if missing or extra:
        raise CertificateError(f"local B mismatch: missing={missing}, extra={extra}")

    total = a1.scale(n)
    for k in range(2, n + 1):
        total = total.add(table[k].scale(math.comb(n, k)))
    return total, {
        "method": "local",
        "formula": "n*a1 + sum_{k=2}^n binom(n,k)*B_k",
    }


def verify_cauchy(data: dict[str, Any], n: int) -> tuple[Interval, dict[str, Any]]:
    raw = data.get("cauchy_dft")
    if not isinstance(raw, dict):
        raise CertificateError("cauchy_dft object is required")
    sample_count = exact_int(raw.get("sample_count"), "cauchy_dft.sample_count")
    if sample_count < n:
        raise CertificateError("sample_count must be at least n")

    r = dyadic_value(raw.get("radius_inner"), "cauchy_dft.radius_inner")
    R = dyadic_value(raw.get("radius_outer"), "cauchy_dft.radius_outer")
    if not (0 < r < R < 1):
        raise CertificateError("radii must satisfy 0 < r < R < 1")

    dft_real = dyadic_interval(raw.get("dft_real"), "cauchy_dft.dft_real")
    dft_imag = dyadic_interval(raw.get("dft_imag"), "cauchy_dft.dft_imag")
    if not (dft_imag.lower <= 0 <= dft_imag.upper):
        raise CertificateError("dft_imag must contain zero")

    outer_bound = dyadic_value(
        raw.get("outer_max_abs_upper"), "cauchy_dft.outer_max_abs_upper"
    )
    if outer_bound < 0:
        raise CertificateError("outer_max_abs_upper must be nonnegative")

    m = n - 1
    ratio_power = (r / R) ** sample_count
    alias_bound = outer_bound * ratio_power / (R**m) / (1 - ratio_power)
    result = dft_real.widen(alias_bound)
    return result, {
        "method": "cauchy_dft",
        "coefficient_power_m": m,
        "sample_count": sample_count,
        "radius_inner": fraction_json(r),
        "radius_outer": fraction_json(R),
        "outer_max_abs_upper": fraction_json(outer_bound),
        "alias_bound": fraction_json(alias_bound),
        "dft_real_interval": interval_json(dft_real),
        "dft_imag_interval": interval_json(dft_imag),
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    n = exact_int(data.get("n"), "n")
    if n < 1:
        raise CertificateError("n must be positive")

    method = data.get("method")
    if method == "local":
        enclosure, details = verify_local(data, n)
    elif method == "cauchy_dft":
        enclosure, details = verify_cauchy(data, n)
    else:
        raise CertificateError("method must be 'local' or 'cauchy_dft'")

    certified_negative = enclosure.upper < 0
    return {
        "schema": SCHEMA,
        "n": n,
        "certified_negative": certified_negative,
        "lambda_interval": interval_json(enclosure),
        "details": details,
        "interpretation": (
            f"The supplied intervals imply lambda_{n} < 0 exactly."
            if certified_negative
            else f"The supplied intervals do not prove lambda_{n} < 0."
        ),
        "scope_warning": (
            "Exact rational propagation only: an independent analytic producer "
            "must prove every enclosure, Cauchy analyticity premise, and the "
            "normalization linking the data to the standard Li coefficient."
        ),
    }


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
    return 0 if result["certified_negative"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
