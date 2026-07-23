#!/usr/bin/env python3
"""Build an exact L-2804 certificate from one or more rigorous directed shards.

Unlike assemble_certificate.py, this proof assembler does not require duplicate
precision runs. A single MPFR-directed interval is already an inclusion proof.
Precision escalation remains recommended and is recorded when present.
"""
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
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    ).hexdigest()


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ValueError(f"{name} must be an object")
    numerator, denominator = raw.get("numerator"), raw.get("denominator")
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or denominator <= 0
    ):
        raise ValueError(f"bad {name}")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def assemble(
    vector_data: dict[str, Any],
    alpha_data: dict[str, Any],
    shards: list[dict[str, Any]],
    plan: dict[str, Any],
) -> dict[str, Any]:
    raw_vector = vector_data.get("dyadic_vector")
    if not isinstance(raw_vector, dict):
        raise ValueError("dyadic_vector missing")
    bits = raw_vector.get("scale_bits")
    real = raw_vector.get("real_numerators")
    imag = raw_vector.get("imag_numerators")
    if (
        isinstance(bits, bool)
        or not isinstance(bits, int)
        or bits < 0
        or not isinstance(real, list)
        or not isinstance(imag, list)
        or len(real) != len(imag)
        or not real
        or any(isinstance(x, bool) or not isinstance(x, int) for x in real + imag)
    ):
        raise ValueError("bad dyadic vector")
    vector = {"scale_bits": bits, "real_numerators": real, "imag_numerators": imag}
    vector_sha = canonical_sha(
        {"imag_numerators": imag, "real_numerators": real, "scale_bits": bits}
    )

    carrier = rational(alpha_data.get("carrier"), "alpha carrier")
    alpha_raw = alpha_data.get("alpha_dyadic_interval")
    if not isinstance(alpha_raw, dict):
        raise ValueError("alpha interval missing")
    alpha_bits = alpha_raw.get("scale_bits")
    alpha_lower_num = alpha_raw.get("lower_num")
    alpha_upper_num = alpha_raw.get("upper_num")
    if (
        any(
            isinstance(x, bool) or not isinstance(x, int)
            for x in (alpha_bits, alpha_lower_num, alpha_upper_num)
        )
        or alpha_bits < 0
        or alpha_lower_num > alpha_upper_num
    ):
        raise ValueError("bad alpha interval")
    alpha_lower = Fraction(alpha_lower_num, 1 << alpha_bits)
    alpha_upper = Fraction(alpha_upper_num, 1 << alpha_bits)

    cells = int(plan["cells"])
    cutoff_power10 = int(plan["cutoff_power10"])
    total_segments = int(plan["total_segments"])
    if cells != len(real):
        raise ValueError("vector length does not match cells")
    parameter_object = {
        "carrier": fraction_json(carrier),
        "cells": cells,
        "cutoff_power10": cutoff_power10,
        "total_segments": total_segments,
    }
    parameter_sha = canonical_sha(parameter_object)

    expected_ranges = sorted(
        (
            int(item["segment_start"]),
            int(item["segment_end"]),
            bool(item["include_higher_powers"]),
        )
        for item in plan["shards"]
    )
    by_range: dict[tuple[int, int, bool], list[dict[str, Any]]] = {}
    for shard in shards:
        if shard.get("schema") != "riemann.piecewise-carrier-directed-shard.v1":
            raise ValueError("bad shard schema")
        if shard.get("normalization_sha256") != NORMALIZATION_SHA:
            raise ValueError("normalization mismatch")
        if shard.get("vector_sha256") != vector_sha:
            raise ValueError("vector digest mismatch")
        if shard.get("parameter_sha256") != parameter_sha:
            raise ValueError("parameter digest mismatch")
        key = (
            int(shard["segment_start"]),
            int(shard["segment_end"]),
            bool(shard["include_higher_powers"]),
        )
        by_range.setdefault(key, []).append(shard)
    if sorted(by_range) != expected_ranges:
        raise ValueError("shard ranges do not match plan")

    selected = []
    for key in expected_ranges:
        items = sorted(by_range[key], key=lambda item: int(item["precision_bits"]))
        intervals = []
        for item in items:
            raw = item.get("prime_rayleigh_interval")
            if not isinstance(raw, dict):
                raise ValueError("prime interval missing")
            lower = rational(raw.get("lower"), "prime lower")
            upper = rational(raw.get("upper"), "prime upper")
            if lower > upper:
                raise ValueError("inverted prime interval")
            intervals.append((lower, upper))
        # Every retained directed interval must agree with every other one.
        if max(lo for lo, _ in intervals) > min(hi for _, hi in intervals):
            raise ValueError("precision intervals do not overlap")
        lower = max(lo for lo, _ in intervals)
        upper = min(hi for _, hi in intervals)
        reference = items[-1]
        for item in items:
            for field in ("prime_count", "higher_prime_power_count", "total_terms"):
                if int(item[field]) != int(reference[field]):
                    raise ValueError("precision count mismatch")
        selected.append(
            {
                "segment_start": key[0],
                "segment_end": key[1],
                "include_higher_powers": key[2],
                "prime_count": int(reference["prime_count"]),
                "higher_prime_power_count": int(reference["higher_prime_power_count"]),
                "total_terms": int(reference["total_terms"]),
                "vector_sha256": vector_sha,
                "parameter_sha256": parameter_sha,
                "prime_rayleigh_interval": {
                    "lower": fraction_json(lower),
                    "upper": fraction_json(upper),
                },
                "precision_evidence": [
                    {
                        "precision_bits": int(item["precision_bits"]),
                        "mpfr_version": item["mpfr_version"],
                        "phase_method": item["phase_method"],
                    }
                    for item in items
                ],
            }
        )

    prime_count = sum(item["prime_count"] for item in selected)
    higher_count = sum(item["higher_prime_power_count"] for item in selected)
    total_terms = sum(item["total_terms"] for item in selected)
    expected = plan["expected_counts"]
    if (
        prime_count != int(expected["prime_count"])
        or higher_count != int(expected["higher_prime_power_count"])
        or total_terms != int(expected["total_terms"])
    ):
        raise ValueError("global term counts do not match plan")

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
            "rigorous_directed_interval_count": len(shards),
            "global_counts": {
                "prime_count": prime_count,
                "higher_prime_power_count": higher_count,
                "total_terms": total_terms,
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
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
