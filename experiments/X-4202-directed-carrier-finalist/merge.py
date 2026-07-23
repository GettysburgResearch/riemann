#!/usr/bin/env python3
"""Merge complete X-4202 directed shards and classify one fixed vector exactly.

All shard intervals are parsed as exact rational endpoints.  The merger trusts
neither traversal order nor floating summaries: it reconstructs contiguous
coverage, the unique higher-prime-power stream, exact count identities, the
leading scalar interval, and the parent PR #51 nonprime correction moat.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable, Sequence

from flint import arb, ctx, __version__ as flint_version

SHARD_SCHEMA = "riemann.piecewise-carrier-directed-shard.v1"
RESULT_SCHEMA = "riemann.piecewise-carrier-directed-result.v1"
EXPECTED_PRIME_COUNT = 4_118_054_813
EXPECTED_HIGHER_COUNT = 28_156
CORRECTION_RADIUS_UNIT = Fraction(1, 4_000_000_000)


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


def parse_interval(value: Any) -> tuple[Fraction, Fraction]:
    if not isinstance(value, dict):
        raise ValueError("interval must be an object")
    lower = parse_fraction(value["lower"])
    upper = parse_fraction(value["upper"])
    if lower > upper:
        raise ValueError("reversed interval")
    return lower, upper


def fraction_json(value: Fraction) -> dict[str, str]:
    value = Fraction(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def interval_json(lower: Fraction, upper: Fraction) -> dict[str, object]:
    if lower > upper:
        raise ValueError("reversed interval")
    return {
        "lower": fraction_json(lower),
        "upper": fraction_json(upper),
        "width": fraction_json(upper - lower),
    }


def arf_fraction(value: Any) -> Fraction:
    mantissa, exponent = value.man_exp()
    exponent = int(exponent)
    result = Fraction(int(mantissa))
    if exponent >= 0:
        return result * (1 << exponent)
    return result / (1 << (-exponent))


def arb_interval(value: arb) -> tuple[Fraction, Fraction]:
    return arf_fraction(value.lower()), arf_fraction(value.upper())


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: JSON root must be an object")
    return value


def validate_correction_certificate(path: Path) -> dict[str, object]:
    value = load_json(path)
    text = path.read_text(encoding="utf-8")
    if "100000000000" not in text or "1024" not in text or "4709203636353.65" not in text:
        raise ValueError("correction certificate does not bind the target parameters")
    # PR #51's exact checker proves the stronger component bound and in
    # particular the public rational moat below 1/(4e9).  The merger records the
    # immutable source artifact and uses only this weaker exact corollary.
    return {
        "path": str(path),
        "sha256": sha256(path),
        "unit_vector_radius": fraction_json(CORRECTION_RADIUS_UNIT),
        "dependency": "L-4202/L-4203 and X-4201 on stacked PR #51",
        "source_schema": value.get("schema"),
    }


def merge(
    shard_paths: Sequence[Path],
    *,
    correction_certificate: Path,
    precision_bits: int,
) -> dict[str, object]:
    if not shard_paths:
        raise ValueError("at least one shard is required")
    if precision_bits < 128:
        raise ValueError("precision_bits must be at least 128")
    ctx.prec = precision_bits

    shards: list[tuple[Path, dict[str, Any]]] = []
    for path in shard_paths:
        value = load_json(path)
        if value.get("schema") != SHARD_SCHEMA:
            raise ValueError(f"{path}: unsupported shard schema")
        shards.append((path, value))

    reference = shards[0][1]
    reference_parameters = reference["parameters"]
    reference_finalist = reference["finalist"]
    keys = ("cutoff", "cells", "carrier", "segment_size", "total_segments", "precision_bits")
    for path, value in shards:
        if any(value["parameters"].get(key) != reference_parameters.get(key) for key in keys):
            raise ValueError(f"{path}: parameter mismatch")
        if value["finalist"].get("sha256") != reference_finalist.get("sha256"):
            raise ValueError(f"{path}: finalist digest mismatch")

    ordered = sorted(shards, key=lambda row: int(row[1]["segment_range"]["start"]))
    cursor = 0
    prime_count = 0
    higher_count = 0
    lower_sum = Fraction(0)
    upper_sum = Fraction(0)
    shard_manifest: list[dict[str, object]] = []
    higher_streams = 0
    for path, value in ordered:
        start = int(value["segment_range"]["start"])
        end = int(value["segment_range"]["end"])
        if start != cursor or end < start:
            raise ValueError(f"coverage gap/overlap before {path}: expected {cursor}, got {start}")
        cursor = end
        interval_lower, interval_upper = parse_interval(value["prime_rayleigh_interval"])
        lower_sum += interval_lower
        upper_sum += interval_upper
        prime_count += int(value["prime_count"])
        higher_count += int(value["higher_prime_power_count"])
        include_higher = bool(value["include_higher_prime_powers"])
        higher_streams += int(include_higher)
        if int(value["total_prime_power_terms"]) != int(value["prime_count"]) + int(value["higher_prime_power_count"]):
            raise ValueError(f"{path}: term count identity failed")
        shard_manifest.append(
            {
                "path": str(path),
                "sha256": sha256(path),
                "segment_range": {"start": start, "end": end},
                "include_higher_prime_powers": include_higher,
                "prime_count": int(value["prime_count"]),
                "higher_prime_power_count": int(value["higher_prime_power_count"]),
            }
        )

    if cursor != int(reference_parameters["total_segments"]):
        raise ValueError("shards do not cover the complete segment range")
    if higher_streams != 1:
        raise ValueError("exactly one shard must include higher prime powers")
    cutoff = int(reference_parameters["cutoff"])
    cells = int(reference_parameters["cells"])
    if cutoff == 100_000_000_000 and cells == 1024:
        if prime_count != EXPECTED_PRIME_COUNT or higher_count != EXPECTED_HIGHER_COUNT:
            raise ValueError(
                "target count mismatch: "
                f"primes={prime_count}, higher={higher_count}"
            )

    norm_lower, norm_upper = parse_interval(reference_finalist["norm_squared"])
    if norm_lower <= 0:
        raise ValueError("finalist norm does not exclude zero")
    carrier_fraction = parse_fraction(reference_parameters["carrier"])
    carrier = arb(carrier_fraction.numerator) / carrier_fraction.denominator
    alpha = (carrier / (arb(2) * arb.pi())).log() / (arb(2) * arb.pi())
    alpha_lower, alpha_upper = arb_interval(alpha)
    leading_lower = alpha_lower * norm_lower - upper_sum
    leading_upper = alpha_upper * norm_upper - lower_sum

    correction = validate_correction_certificate(correction_certificate)
    correction_lower = -CORRECTION_RADIUS_UNIT * norm_upper
    correction_upper = CORRECTION_RADIUS_UNIT * norm_upper
    full_lower = leading_lower + correction_lower
    full_upper = leading_upper + correction_upper
    if full_upper < 0:
        status = "CERTIFIED_NEGATIVE_PENDING_INDEPENDENT_REPRODUCTION"
    elif full_lower > 0:
        status = "CERTIFIED_POSITIVE_FIXED_VECTOR"
    else:
        status = "UNRESOLVED_ZERO_TOUCH"

    normalized_lower = full_lower / norm_upper
    normalized_upper = full_upper / norm_lower
    return {
        "schema": RESULT_SCHEMA,
        "experiment_id": "X-4202",
        "status": status,
        "parameters": reference_parameters,
        "finalist": reference_finalist,
        "coverage": {
            "shards": len(ordered),
            "prime_count": prime_count,
            "higher_prime_power_count": higher_count,
            "total_prime_power_terms": prime_count + higher_count,
            "manifest": shard_manifest,
        },
        "prime_rayleigh_interval": interval_json(lower_sum, upper_sum),
        "leading_scalar_interval": interval_json(alpha_lower, alpha_upper),
        "leading_fixed_vector_interval": interval_json(leading_lower, leading_upper),
        "correction": correction,
        "full_fixed_vector_interval": interval_json(full_lower, full_upper),
        "normalized_full_interval": interval_json(normalized_lower, normalized_upper),
        "merger": {
            "precision_bits": precision_bits,
            "python_flint": flint_version,
        },
        "counterexample_candidate": None,
        "promotion_boundary": (
            "A negative upper endpoint would remain pending independent directed "
            "special-function reproduction and review of D-0801/L-0801/L-4202/L-4203."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--correction-certificate", type=Path, required=True)
    parser.add_argument("--precision-bits", type=int, default=192)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = merge(
        args.shards,
        correction_certificate=args.correction_certificate,
        precision_bits=args.precision_bits,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "counts": result["coverage"],
        "normalized_full_interval": result["normalized_full_interval"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
