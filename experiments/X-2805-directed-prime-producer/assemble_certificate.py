#!/usr/bin/env python3
"""Pair precision-escalated directed shards and build an L-2804 certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

NORMALIZATION_SHA = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"
SCHEMA = "riemann.piecewise-carrier-fixed-vector.v1"


def canonical_sha(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ValueError(f"{name} must be an object")
    numerator = raw.get("numerator")
    denominator = raw.get("denominator")
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or denominator <= 0
    ):
        raise ValueError(f"bad {name}")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise ValueError(f"{name} must be an object")
    lower = rational(raw.get("lower"), f"{name}.lower")
    upper = rational(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise ValueError(f"inverted {name}")
    return lower, upper


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def vector_fields(data: dict[str, Any]) -> tuple[dict[str, Any], str]:
    raw = data.get("dyadic_vector", data.get("vector"))
    if not isinstance(raw, dict):
        raise ValueError("vector object missing")
    bits = raw.get("scale_bits")
    real = raw.get("real_numerators")
    imag = raw.get("imag_numerators")
    if (
        isinstance(bits, bool)
        or not isinstance(bits, int)
        or bits < 0
        or not isinstance(real, list)
        or not isinstance(imag, list)
        or len(real) != len(imag)
        or not real
    ):
        raise ValueError("bad vector")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in real + imag):
        raise ValueError("bad vector numerator")
    canonical = {
        "imag_numerators": imag,
        "real_numerators": real,
        "scale_bits": bits,
    }
    return {
        "scale_bits": bits,
        "real_numerators": real,
        "imag_numerators": imag,
    }, canonical_sha(canonical)


def alpha_fields(
    data: dict[str, Any],
) -> tuple[tuple[Fraction, Fraction], Fraction]:
    raw = data.get("alpha_dyadic_interval")
    if not isinstance(raw, dict):
        raise ValueError("alpha interval missing")
    bits = raw.get("scale_bits")
    lower = raw.get("lower_num")
    upper = raw.get("upper_num")
    if (
        any(isinstance(x, bool) or not isinstance(x, int) for x in (bits, lower, upper))
        or bits < 0
        or lower > upper
    ):
        raise ValueError("bad alpha dyadic interval")
    carrier = rational(data.get("carrier"), "alpha.carrier")
    return (Fraction(lower, 1 << bits), Fraction(upper, 1 << bits)), carrier


def assemble(
    vector_data: dict[str, Any],
    alpha_data: dict[str, Any],
    shard_data: list[dict[str, Any]],
    plan: dict[str, Any],
) -> dict[str, Any]:
    vector, vector_sha = vector_fields(vector_data)
    (alpha_lower, alpha_upper), carrier = alpha_fields(alpha_data)

    cutoff_power10 = plan["cutoff_power10"]
    cells = plan["cells"]
    total_segments = plan["total_segments"]
    if len(vector["real_numerators"]) != cells:
        raise ValueError("vector length/cells mismatch")

    parameter_object = {
        "carrier": fraction_json(carrier),
        "cells": cells,
        "cutoff_power10": cutoff_power10,
        "total_segments": total_segments,
    }
    parameter_sha = canonical_sha(parameter_object)

    groups: dict[tuple[int, int, bool], list[dict[str, Any]]] = {}
    for shard in shard_data:
        if shard.get("schema") != "riemann.piecewise-carrier-directed-shard.v1":
            raise ValueError("bad shard schema")
        if shard.get("normalization_sha256") != NORMALIZATION_SHA:
            raise ValueError("normalization mismatch")
        if shard.get("vector_sha256") != vector_sha:
            raise ValueError("vector mismatch")
        if shard.get("parameter_sha256") != parameter_sha:
            raise ValueError("parameter mismatch")
        key = (
            shard["segment_start"],
            shard["segment_end"],
            bool(shard["include_higher_powers"]),
        )
        groups.setdefault(key, []).append(shard)

    expected_ranges = {
        (
            item["segment_start"],
            item["segment_end"],
            bool(item["include_higher_powers"]),
        )
        for item in plan["shards"]
    }
    if set(groups) != expected_ranges:
        raise ValueError("shard range set does not match plan")

    selected: list[dict[str, Any]] = []
    for key, items in sorted(groups.items()):
        items.sort(key=lambda item: item["precision_bits"])
        if len(items) < 2 or len({item["precision_bits"] for item in items}) < 2:
            raise ValueError("each range needs two precisions")
        intervals = [
            interval(item["prime_rayleigh_interval"], "prime interval")
            for item in items
        ]
        for index in range(1, len(items)):
            previous_width = intervals[index - 1][1] - intervals[index - 1][0]
            current_width = intervals[index][1] - intervals[index][0]
            if current_width > previous_width:
                raise ValueError("higher precision widened interval")
            if max(intervals[index][0], intervals[index - 1][0]) > min(
                intervals[index][1], intervals[index - 1][1]
            ):
                raise ValueError("precision intervals do not overlap")

        lower = max(bounds[0] for bounds in intervals)
        upper = min(bounds[1] for bounds in intervals)
        reference = items[-1]
        for item in items:
            for field in (
                "prime_count",
                "higher_prime_power_count",
                "total_terms",
            ):
                if item[field] != reference[field]:
                    raise ValueError("precision term-count mismatch")

        selected.append(
            {
                "segment_start": key[0],
                "segment_end": key[1],
                "include_higher_powers": key[2],
                "prime_count": reference["prime_count"],
                "higher_prime_power_count": reference[
                    "higher_prime_power_count"
                ],
                "total_terms": reference["total_terms"],
                "vector_sha256": vector_sha,
                "parameter_sha256": parameter_sha,
                "prime_rayleigh_interval": {
                    "lower": fraction_json(lower),
                    "upper": fraction_json(upper),
                },
                "precision_evidence": [
                    {
                        "precision_bits": item["precision_bits"],
                        "mpfr_version": item["mpfr_version"],
                    }
                    for item in items
                ],
            }
        )

    prime_total = sum(item["prime_count"] for item in selected)
    higher_total = sum(item["higher_prime_power_count"] for item in selected)
    term_total = sum(item["total_terms"] for item in selected)
    expected_counts = plan.get("expected_counts", {})
    if expected_counts and (
        prime_total != expected_counts["prime_count"]
        or higher_total != expected_counts["higher_prime_power_count"]
        or term_total != expected_counts["total_terms"]
    ):
        raise ValueError("global count mismatch")

    return {
        "schema": SCHEMA,
        "cutoff_power10": cutoff_power10,
        "cells": cells,
        "total_segments": total_segments,
        "carrier": fraction_json(carrier),
        "normalization_sha256": NORMALIZATION_SHA,
        "vector": vector,
        "vector_sha256": vector_sha,
        "parameter_sha256": parameter_sha,
        "alpha_interval": {
            "lower": fraction_json(alpha_lower),
            "upper": fraction_json(alpha_upper),
        },
        "shards": selected,
        "producer_evidence": {
            "precision_pair_required": True,
            "global_counts": {
                "prime_count": prime_total,
                "higher_prime_power_count": higher_total,
                "total_terms": term_total,
            },
            "normalization_sha256": NORMALIZATION_SHA,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vector", type=Path, required=True)
    parser.add_argument("--alpha", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--shard", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = assemble(
        load(args.vector),
        load(args.alpha),
        [load(path) for path in args.shard],
        load(args.plan),
    )
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
