#!/usr/bin/env python3
"""Exact checker for sharded fixed-vector D-0801 carrier certificates.

The checker composes:
- one exact dyadic complex vector;
- a directed interval for the leading scalar alpha(T);
- directed shard intervals for v^* S_shard v;
- closed segment-coverage metadata and exactly one higher-power stream;
- the exact rational L-2803 correction radius recomputed from parameters.

It uses integers, fractions.Fraction, JSON, and SHA-256 only. It does not prove
that a producer correctly enumerated primes inside a declared segment or that a
reported interval encloses the analytic prime contribution. It also does not
close D-0801 admissibility or Guinand--Weil normalization gates.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Sequence

from verify_variation_budget import variation_budget

SCHEMA = "riemann.piecewise-carrier-fixed-vector.v1"


class CertificateError(ValueError):
    """Malformed or quantitatively incomplete certificate."""


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def subtract(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale_nonnegative(self, scalar: Fraction) -> "Interval":
        if scalar < 0:
            raise CertificateError("scale_nonnegative requires a nonnegative scalar")
        return Interval(self.lower * scalar, self.upper * scalar)

    def widen(self, radius: Fraction) -> "Interval":
        if radius < 0:
            raise CertificateError("widening radius must be nonnegative")
        return Interval(self.lower - radius, self.upper + radius)


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def exact_bool(value: Any, name: str) -> bool:
    if not isinstance(value, bool):
        raise CertificateError(f"{name} must be a boolean")
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


def canonical_sha256(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def parse_vector(
    raw: Any, cells: int
) -> tuple[list[Fraction], list[Fraction], Fraction, str]:
    if not isinstance(raw, dict):
        raise CertificateError("vector must be an object")
    bits = exact_int(raw.get("scale_bits"), "vector.scale_bits")
    if bits < 0:
        raise CertificateError("vector.scale_bits must be nonnegative")
    real = raw.get("real_numerators")
    imag = raw.get("imag_numerators")
    if not isinstance(real, list) or not isinstance(imag, list):
        raise CertificateError("vector numerator fields must be lists")
    if len(real) != cells or len(imag) != cells:
        raise CertificateError(f"vector lists must both have length {cells}")
    real_ints = [
        exact_int(x, f"vector.real_numerators[{i}]") for i, x in enumerate(real)
    ]
    imag_ints = [
        exact_int(x, f"vector.imag_numerators[{i}]") for i, x in enumerate(imag)
    ]
    denominator = 1 << bits
    real_values = [Fraction(x, denominator) for x in real_ints]
    imag_values = [Fraction(x, denominator) for x in imag_ints]
    norm_squared = sum(x * x + y * y for x, y in zip(real_values, imag_values))
    if norm_squared == 0:
        raise CertificateError("vector must be nonzero")
    canonical = {
        "imag_numerators": imag_ints,
        "real_numerators": real_ints,
        "scale_bits": bits,
    }
    return real_values, imag_values, norm_squared, canonical_sha256(canonical)


def parameter_fingerprint(
    *, cutoff_power10: int, cells: int, carrier: Fraction, total_segments: int
) -> str:
    canonical = {
        "carrier": fraction_json(carrier),
        "cells": cells,
        "cutoff_power10": cutoff_power10,
        "total_segments": total_segments,
    }
    return canonical_sha256(canonical)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")

    n = exact_int(data.get("cutoff_power10"), "cutoff_power10")
    cells = exact_int(data.get("cells"), "cells")
    total_segments = exact_int(data.get("total_segments"), "total_segments")
    if n < 1:
        raise CertificateError("cutoff_power10 must be positive")
    if cells < 1:
        raise CertificateError("cells must be positive")
    if total_segments < 1:
        raise CertificateError("total_segments must be positive")
    carrier = rational(data.get("carrier"), "carrier")
    if carrier <= 0:
        raise CertificateError("carrier must be positive")

    _, _, norm_squared, vector_digest = parse_vector(data.get("vector"), cells)
    if data.get("vector_sha256") != vector_digest:
        raise CertificateError(
            "top-level vector_sha256 does not match the canonical vector"
        )

    parameter_digest = parameter_fingerprint(
        cutoff_power10=n,
        cells=cells,
        carrier=carrier,
        total_segments=total_segments,
    )
    if data.get("parameter_sha256") != parameter_digest:
        raise CertificateError("top-level parameter_sha256 does not match parameters")

    alpha = interval(data.get("alpha_interval"), "alpha_interval")
    shards = data.get("shards")
    if not isinstance(shards, list) or not shards:
        raise CertificateError("shards must be a nonempty list")

    parsed = []
    for index, shard in enumerate(shards):
        if not isinstance(shard, dict):
            raise CertificateError(f"shards[{index}] must be an object")
        start = exact_int(
            shard.get("segment_start"), f"shards[{index}].segment_start"
        )
        end = exact_int(shard.get("segment_end"), f"shards[{index}].segment_end")
        if not (0 <= start < end <= total_segments):
            raise CertificateError(f"invalid segment range in shards[{index}]")
        if shard.get("vector_sha256") != vector_digest:
            raise CertificateError(f"vector digest mismatch in shards[{index}]")
        if shard.get("parameter_sha256") != parameter_digest:
            raise CertificateError(f"parameter digest mismatch in shards[{index}]")
        include_higher = exact_bool(
            shard.get("include_higher_powers"),
            f"shards[{index}].include_higher_powers",
        )
        prime_count = exact_int(
            shard.get("prime_count"), f"shards[{index}].prime_count"
        )
        higher_count = exact_int(
            shard.get("higher_prime_power_count"),
            f"shards[{index}].higher_prime_power_count",
        )
        total_terms = exact_int(
            shard.get("total_terms"), f"shards[{index}].total_terms"
        )
        if prime_count < 0 or higher_count < 0 or total_terms < 0:
            raise CertificateError(f"negative count in shards[{index}]")
        if total_terms != prime_count + higher_count:
            raise CertificateError(f"term-count mismatch in shards[{index}]")
        if not include_higher and higher_count != 0:
            raise CertificateError(
                f"shards[{index}] has higher-power terms without the inclusion flag"
            )
        rayleigh = interval(
            shard.get("prime_rayleigh_interval"),
            f"shards[{index}].prime_rayleigh_interval",
        )
        parsed.append(
            (
                start,
                end,
                include_higher,
                prime_count,
                higher_count,
                total_terms,
                rayleigh,
            )
        )

    parsed.sort(key=lambda item: item[0])
    cursor = 0
    higher_streams = 0
    prime_total = Interval(Fraction(0), Fraction(0))
    prime_count_total = 0
    higher_count_total = 0
    term_total = 0
    for (
        start,
        end,
        include_higher,
        prime_count,
        higher_count,
        total_terms,
        rayleigh,
    ) in parsed:
        if start != cursor:
            raise CertificateError(
                f"segment coverage gap or overlap at {cursor}: "
                f"next shard starts at {start}"
            )
        cursor = end
        higher_streams += int(include_higher)
        prime_total = prime_total.add(rayleigh)
        prime_count_total += prime_count
        higher_count_total += higher_count
        term_total += total_terms
    if cursor != total_segments:
        raise CertificateError(
            f"segment coverage ends at {cursor}, expected {total_segments}"
        )
    if higher_streams != 1:
        raise CertificateError("exactly one shard must include higher prime powers")

    alpha_quadratic = alpha.scale_nonnegative(norm_squared)
    leading = alpha_quadratic.subtract(prime_total)
    budget = variation_budget(cutoff_power10=n, cells=cells, carrier=carrier)
    correction_per_unit = budget["total"]
    assert isinstance(correction_per_unit, Fraction)
    correction_quadratic = correction_per_unit * norm_squared
    full = leading.widen(correction_quadratic)
    positive = full.lower > 0
    negative = full.upper < 0

    return {
        "schema": SCHEMA,
        "cutoff": f"10^{n}",
        "cells": cells,
        "carrier": fraction_json(carrier),
        "vector_sha256": vector_digest,
        "parameter_sha256": parameter_digest,
        "vector_norm_squared": fraction_json(norm_squared),
        "coverage": {
            "total_segments": total_segments,
            "shards": len(parsed),
            "higher_power_streams": higher_streams,
            "prime_count": prime_count_total,
            "higher_prime_power_count": higher_count_total,
            "total_terms": term_total,
        },
        "alpha_interval": interval_json(alpha),
        "prime_rayleigh_interval": interval_json(prime_total),
        "leading_quadratic_interval": interval_json(leading),
        "correction_radius_per_unit_norm": fraction_json(correction_per_unit),
        "correction_quadratic_radius": fraction_json(correction_quadratic),
        "full_exact_quadratic_interval": interval_json(full),
        "certified_positive": positive,
        "certified_negative": negative,
        "verdict": (
            "CERTIFIED_POSITIVE_FIXED_VECTOR"
            if positive
            else "CERTIFIED_NEGATIVE_FIXED_VECTOR"
            if negative
            else "UNRESOLVED"
        ),
        "scope_warning": (
            "Exact composition and declared segment coverage only. The checker "
            "does not prove prime enumeration inside a segment, analytic interval "
            "provenance, D-0801 admissibility, or the Guinand--Weil normalization."
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
    return 0 if result["certified_positive"] or result["certified_negative"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
