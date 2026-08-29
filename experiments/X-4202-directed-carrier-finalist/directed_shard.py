#!/usr/bin/env python3
"""Produce one directed fixed-vector prime Rayleigh shard with Python-FLINT/Arb.

The vector is the exact dyadic X-4202 finalist.  Each prime power contributes
one scalar interval after contraction with its exact dyadic autocorrelations;
no interval matrix or eigensolver appears in the proof path.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
from typing import Any, Iterable, Sequence

from flint import arb, ctx, __version__ as flint_version

SCHEMA = "riemann.piecewise-carrier-directed-shard.v1"
EXPERIMENT_ID = "X-4202"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_fraction(value: Any) -> Fraction:
    if not isinstance(value, dict):
        raise ValueError("fraction must be an object")
    numerator = value.get("numerator")
    denominator = value.get("denominator")
    if isinstance(numerator, bool) or isinstance(denominator, bool):
        raise ValueError("boolean fraction field")
    return Fraction(int(numerator), int(denominator))


def arb_fraction(value: Fraction) -> arb:
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def arf_fraction(value: Any) -> Fraction:
    mantissa, exponent = value.man_exp()
    exponent = int(exponent)
    result = Fraction(int(mantissa))
    if exponent >= 0:
        return result * (1 << exponent)
    return result / (1 << (-exponent))


def interval_json(value: arb) -> dict[str, object]:
    lower = arf_fraction(value.lower())
    upper = arf_fraction(value.upper())
    return {
        "lower": {"numerator": str(lower.numerator), "denominator": str(lower.denominator)},
        "upper": {"numerator": str(upper.numerator), "denominator": str(upper.denominator)},
        "width": {
            "numerator": str((upper - lower).numerator),
            "denominator": str((upper - lower).denominator),
        },
    }


def simple_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [index for index in range(2, limit + 1) if sieve[index]]


def segment_primes(low: int, high: int, base_primes: Sequence[int]) -> list[int]:
    if not (2 <= low <= high):
        raise ValueError("require 2 <= low <= high")
    mark = bytearray(b"\x01") * (high - low)
    root = math.isqrt(max(high - 1, 1))
    for prime in base_primes:
        if prime > root:
            break
        start = max(prime * prime, ((low + prime - 1) // prime) * prime)
        if start < high:
            mark[start - low : high - low : prime] = b"\x00" * (
                (high - 1 - start) // prime + 1
            )
    return [low + index for index, flag in enumerate(mark) if flag]


def higher_prime_powers(cutoff: int, base_primes: Sequence[int]) -> Iterable[tuple[int, int]]:
    for prime in base_primes:
        value = prime * prime
        while value <= cutoff:
            yield value, prime
            if value > cutoff // prime:
                break
            value *= prime


def load_finalist(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("schema") != "riemann.piecewise-carrier-finalist.v1":
        raise ValueError("unsupported finalist schema")
    parameters = value.get("parameters")
    if not isinstance(parameters, dict):
        raise ValueError("missing finalist parameters")
    cells = int(parameters["cells"])
    vector = value.get("vector")
    correlations = value.get("autocorrelations")
    if not isinstance(vector, list) or len(vector) != cells:
        raise ValueError("vector length mismatch")
    if not isinstance(correlations, list) or len(correlations) != cells:
        raise ValueError("autocorrelation length mismatch")
    return value


def load_correlations(finalist: dict[str, Any]) -> tuple[list[tuple[arb, arb]], arb]:
    parameters = finalist["parameters"]
    power = int(parameters["autocorrelation_denominator_power"])
    scale = arb(2) ** power
    rows: list[tuple[arb, arb]] = []
    for item in finalist["autocorrelations"]:
        if not isinstance(item, dict):
            raise ValueError("malformed autocorrelation row")
        rows.append(
            (
                arb(int(item["real_numerator"])) / scale,
                arb(int(item["imag_numerator"])) / scale,
            )
        )
    norm = arb_fraction(parse_fraction(finalist["norm_squared"]))
    if not norm.is_positive():
        raise ValueError("nonpositive vector norm")
    return rows, norm


def unique_lag(scaled: arb, *, q: int, cutoff: int, cells: int) -> int:
    if q == cutoff:
        return cells
    lower = int(scaled.lower().floor())
    upper = int(scaled.upper().floor())
    if lower != upper:
        raise ArithmeticError(
            f"working precision does not isolate deposition lag for q={q}: {scaled}"
        )
    if not (0 <= lower <= cells):
        raise ArithmeticError(f"invalid deposition lag {lower} for q={q}")
    return lower


def term_interval(
    q: int,
    prime: int,
    *,
    cutoff: int,
    cells: int,
    carrier: arb,
    log_cutoff: arb,
    correlations: Sequence[tuple[arb, arb]],
) -> arb:
    if not (2 <= prime <= q <= cutoff):
        raise ValueError("invalid prime-power term")
    log_q = arb(q).log()
    log_prime = arb(prime).log()
    scaled = arb(cells) * log_q / log_cutoff
    lag = unique_lag(scaled, q=q, cutoff=cutoff, cells=cells)
    if lag >= cells:
        return arb(0)
    fraction = scaled - lag
    phase = carrier * log_q
    cosine = phase.cos()
    sine = phase.sin()
    amplitude = log_prime / (arb.pi() * arb(q).sqrt())

    real0, imag0 = correlations[lag]
    contracted = (arb(1) - fraction) * (real0 * cosine + imag0 * sine)
    if lag + 1 < cells:
        real1, imag1 = correlations[lag + 1]
        contracted += fraction * (real1 * cosine + imag1 * sine)
    return amplitude * contracted


def total_segments(cutoff: int, segment_size: int) -> int:
    if cutoff < 2 or segment_size < 1:
        raise ValueError("cutoff >= 2 and segment_size >= 1 required")
    return (cutoff - 2) // segment_size + 1


def produce(
    *,
    finalist_path: Path,
    cutoff: int,
    segment_size: int,
    start_segment: int,
    end_segment: int,
    include_higher_powers: bool,
    precision_bits: int,
) -> dict[str, object]:
    if precision_bits < 96:
        raise ValueError("precision_bits must be at least 96")
    ctx.prec = precision_bits
    finalist = load_finalist(finalist_path)
    parameters = finalist["parameters"]
    if int(parameters["cutoff"]) != cutoff:
        raise ValueError("finalist cutoff mismatch")
    cells = int(parameters["cells"])
    carrier_fraction = parse_fraction(parameters["carrier"])
    carrier = arb_fraction(carrier_fraction)
    correlations, norm = load_correlations(finalist)
    log_cutoff = arb(cutoff).log()

    total = total_segments(cutoff, segment_size)
    if not (0 <= start_segment <= end_segment <= total):
        raise ValueError("segment range outside complete stream")
    low = 2 + start_segment * segment_size
    high = min(cutoff + 1, 2 + end_segment * segment_size)
    base_primes = simple_primes(math.isqrt(cutoff))

    prime_sum = arb(0)
    prime_count = 0
    for prime in segment_primes(low, high, base_primes):
        prime_sum += term_interval(
            prime,
            prime,
            cutoff=cutoff,
            cells=cells,
            carrier=carrier,
            log_cutoff=log_cutoff,
            correlations=correlations,
        )
        prime_count += 1

    higher_count = 0
    if include_higher_powers:
        for q, prime in higher_prime_powers(cutoff, base_primes):
            prime_sum += term_interval(
                q,
                prime,
                cutoff=cutoff,
                cells=cells,
                carrier=carrier,
                log_cutoff=log_cutoff,
                correlations=correlations,
            )
            higher_count += 1

    return {
        "schema": SCHEMA,
        "experiment_id": EXPERIMENT_ID,
        "status": "DIRECTED_PRIME_RAYLEIGH_SHARD",
        "parameters": {
            "cutoff": cutoff,
            "cells": cells,
            "carrier": {
                "numerator": str(carrier_fraction.numerator),
                "denominator": str(carrier_fraction.denominator),
            },
            "segment_size": segment_size,
            "total_segments": total,
            "precision_bits": precision_bits,
        },
        "finalist": {
            "path": str(finalist_path),
            "sha256": sha256(finalist_path),
            "norm_squared": interval_json(norm),
        },
        "segment_range": {"start": start_segment, "end": end_segment},
        "integer_coverage": {"low_inclusive": low, "high_exclusive": high},
        "include_higher_prime_powers": include_higher_powers,
        "prime_count": prime_count,
        "higher_prime_power_count": higher_count,
        "total_prime_power_terms": prime_count + higher_count,
        "prime_rayleigh_interval": interval_json(prime_sum),
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "python_flint": flint_version,
        },
        "counterexample_candidate": None,
        "warning": "This is one directed scalar shard. A complete sign requires exact coverage merging and the nonprime correction moat.",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--finalist", type=Path, required=True)
    parser.add_argument("--cutoff", type=int, default=100_000_000_000)
    parser.add_argument("--segment-size", type=int, default=20_000_000)
    parser.add_argument("--start-segment", type=int, default=0)
    parser.add_argument("--end-segment", type=int)
    parser.add_argument("--include-higher-powers", action="store_true")
    parser.add_argument("--precision-bits", type=int, default=160)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    total = total_segments(args.cutoff, args.segment_size)
    end_segment = total if args.end_segment is None else args.end_segment
    result = produce(
        finalist_path=args.finalist,
        cutoff=args.cutoff,
        segment_size=args.segment_size,
        start_segment=args.start_segment,
        end_segment=end_segment,
        include_higher_powers=args.include_higher_powers,
        precision_bits=args.precision_bits,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "segment_range": result["segment_range"],
        "counts": {
            "prime": result["prime_count"],
            "higher": result["higher_prime_power_count"],
        },
        "interval": result["prime_rayleigh_interval"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
