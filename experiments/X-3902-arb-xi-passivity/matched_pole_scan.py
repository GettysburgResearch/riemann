#!/usr/bin/env python3
"""Generate and verify rigorous L-3904 matched-pole Pick scans.

The expensive Arb evaluations are performed once per exact point. Hundreds of
modeled pole vectors are then constructed and contracted with exact rational
arithmetic by the existing X-3902 verifier.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

from matched_pole import (
    amplification_l1,
    isolated_pair_quadratic,
    matched_pole_vector,
    model_overlaps,
    moment,
    vector_norm_squared,
)

SCHEMA = "riemann.xi-matched-pole-scan.v1"

HEIGHTS: tuple[tuple[str, Fraction], ...] = (
    ("optimized", Fraction("4709203636353.6309")),
    ("optimized-curvature-min", Fraction("4709203636353.6409")),
    ("earlier", Fraction("3157430112465.8695095")),
    ("earlier-left40", Fraction("3157430112425.8695095")),
)

NODES: tuple[Fraction, ...] = tuple(
    Fraction(text)
    for text in (
        "0.00001",
        "0.00002",
        "0.00004",
        "0.00008",
        "0.00016",
        "0.00032",
        "0.00064",
        "0.00128",
        "0.00256",
        "0.00512",
        "0.01024",
    )
)

MODEL_FRACTIONS: tuple[Fraction, ...] = (
    Fraction(1, 3),
    Fraction(1, 2),
    Fraction(2, 3),
)
DIMENSIONS: tuple[int, ...] = (3, 4, 5)


def fraction_json(value: Fraction) -> dict[str, str]:
    value = Fraction(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def parse_fraction_json(value: Any) -> Fraction:
    if not isinstance(value, dict):
        raise ValueError("fraction JSON must be an object")
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def approximate(value: Fraction) -> str:
    try:
        return format(float(value), ".17g")
    except OverflowError:
        return "overflow"


def choose_window(gap: int, dimension: int) -> tuple[int, tuple[Fraction, ...]]:
    if not (0 <= gap < len(NODES) - 1):
        raise ValueError("gap is outside the node ladder")
    if dimension < 2 or dimension > len(NODES):
        raise ValueError("invalid dimension")
    start = gap - (dimension - 2) // 2
    start = max(0, min(start, len(NODES) - dimension))
    stop = start + dimension
    if not (start <= gap and gap + 1 < stop):
        raise AssertionError("window does not contain the modeled gap")
    return start, NODES[start:stop]


def exact_channel(
    *,
    height_index: int,
    height_label: str,
    gap: int,
    model_fraction: Fraction,
    dimension: int,
) -> tuple[dict[str, object], dict[str, object]]:
    start, nodes = choose_window(gap, dimension)
    lower = NODES[gap]
    upper = NODES[gap + 1]
    delta = lower + model_fraction * (upper - lower)
    model_d = delta * delta
    vector = matched_pole_vector(nodes, model_d)

    for power in range(dimension - 2):
        if moment(nodes, vector, power) != 0:
            raise AssertionError("moment identity failed before Arb evaluation")
    alpha, beta = model_overlaps(nodes, vector, model_d)
    if alpha != 0 or beta != -1:
        raise AssertionError("matched-pole overlap identity failed")
    if isolated_pair_quadratic(nodes, vector, model_d) != -2 * model_d:
        raise AssertionError("modeled pair identity failed")

    fraction_label = f"{model_fraction.numerator}of{model_fraction.denominator}"
    identifier = f"mp-{height_label}-g{gap:02d}-n{dimension}-{fraction_label}"
    point_ids = [
        f"{height_label}-x{index:02d}"
        for index in range(start, start + dimension)
    ]
    channel: dict[str, object] = {
        "id": identifier,
        "kind": "real-pick-rayleigh",
        "points": point_ids,
        "vector": [fraction_json(value) for value in vector],
        "matched_pole": {
            "claim": "L-3904",
            "height_index": height_index,
            "gap_index": gap,
            "window_start": start,
            "dimension": dimension,
            "model_fraction": fraction_json(model_fraction),
            "model_delta": fraction_json(delta),
            "model_d": fraction_json(model_d),
            "target_pair_value_m1": fraction_json(-2 * model_d),
        },
    }
    metadata: dict[str, object] = {
        "height_label": height_label,
        "height": HEIGHTS[height_index][1],
        "gap": gap,
        "window_start": start,
        "dimension": dimension,
        "model_fraction": model_fraction,
        "model_delta": delta,
        "model_d": model_d,
        "nodes": nodes,
        "vector": vector,
        "norm_squared": vector_norm_squared(vector),
        "amplification_l1": amplification_l1(nodes, vector),
    }
    return channel, metadata


def build_template() -> tuple[dict[str, object], dict[str, dict[str, object]]]:
    points: list[dict[str, object]] = []
    for height_label, height in HEIGHTS:
        for index, node in enumerate(NODES):
            points.append(
                {
                    "id": f"{height_label}-x{index:02d}",
                    "x": fraction_json(node),
                    "t": fraction_json(height),
                }
            )

    channels: list[dict[str, object]] = []
    metadata: dict[str, dict[str, object]] = {}
    for height_index, (height_label, _height) in enumerate(HEIGHTS):
        for gap in range(len(NODES) - 1):
            for model_fraction in MODEL_FRACTIONS:
                for dimension in DIMENSIONS:
                    channel, row = exact_channel(
                        height_index=height_index,
                        height_label=height_label,
                        gap=gap,
                        model_fraction=model_fraction,
                        dimension=dimension,
                    )
                    identifier = str(channel["id"])
                    if identifier in metadata:
                        raise AssertionError("duplicate channel ID")
                    channels.append(channel)
                    metadata[identifier] = row

    template: dict[str, object] = {
        "schema": "riemann.xi-passivity-template.v1",
        "points": points,
        "channels": channels,
        "declared_channel_ids": [str(channel["id"]) for channel in channels],
        "metadata": {
            "experiment_id": "X-3903",
            "claim": "L-3904",
            "purpose": (
                "Rigorous Arb evaluation of exact matched-pole fixed Pick vectors. "
                "Modeled pair scores nominate vectors only; complete intervals decide signs."
            ),
            "height_count": len(HEIGHTS),
            "node_count_per_height": len(NODES),
            "channel_count": len(channels),
            "dimensions": list(DIMENSIONS),
            "model_fractions": [fraction_json(value) for value in MODEL_FRACTIONS],
            "counterexample_candidate": None,
        },
    }
    return template, metadata


def summarize(
    verification: dict[str, Any],
    metadata: dict[str, dict[str, object]],
    precision_bits: int,
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    counts = {
        "CERTIFIED_NEGATIVE": 0,
        "CERTIFIED_NONNEGATIVE": 0,
        "UNRESOLVED_ZERO_TOUCH": 0,
    }
    negative_ids: list[str] = []
    unresolved_ids: list[str] = []

    for channel in verification["channels"]:
        identifier = str(channel["id"])
        status = str(channel["status"])
        if status not in counts:
            raise ValueError(f"unexpected channel status {status!r}")
        counts[status] += 1
        if status == "CERTIFIED_NEGATIVE":
            negative_ids.append(identifier)
        elif status == "UNRESOLVED_ZERO_TOUCH":
            unresolved_ids.append(identifier)

        interval = channel["interval"]
        lower = parse_fraction_json(interval["lower"])
        upper = parse_fraction_json(interval["upper"])
        row_metadata = metadata[identifier]
        norm_squared = Fraction(row_metadata["norm_squared"])
        normalized_lower = lower / norm_squared
        normalized_upper = upper / norm_squared
        model_d = Fraction(row_metadata["model_d"])
        target_normalized = -2 * model_d / norm_squared
        row: dict[str, object] = {
            "id": identifier,
            "status": status,
            "height_label": row_metadata["height_label"],
            "height": fraction_json(Fraction(row_metadata["height"])),
            "gap_index": row_metadata["gap"],
            "dimension": row_metadata["dimension"],
            "window_start": row_metadata["window_start"],
            "model_fraction": fraction_json(Fraction(row_metadata["model_fraction"])),
            "model_delta": fraction_json(Fraction(row_metadata["model_delta"])),
            "model_d": fraction_json(model_d),
            "normalized_interval": {
                "lower": fraction_json(normalized_lower),
                "upper": fraction_json(normalized_upper),
                "lower_approx": approximate(normalized_lower),
                "upper_approx": approximate(normalized_upper),
            },
            "normalized_width": {
                "exact": fraction_json(normalized_upper - normalized_lower),
                "approx": approximate(normalized_upper - normalized_lower),
            },
            "target_pair_normalized_m1": {
                "exact": fraction_json(target_normalized),
                "approx": approximate(target_normalized),
            },
            "amplification_l1": {
                "exact": fraction_json(Fraction(row_metadata["amplification_l1"])),
                "approx": approximate(Fraction(row_metadata["amplification_l1"])),
            },
        }
        rows.append(row)

    rows.sort(key=lambda row: parse_fraction_json(row["normalized_interval"]["upper"]))
    if negative_ids:
        scan_status = "DIRECTED_NEGATIVE_FOUND_PENDING_INDEPENDENT_REPRODUCTION"
    elif unresolved_ids:
        scan_status = "NO_NEGATIVE_UNRESOLVED_CHANNELS_PRESENT"
    else:
        scan_status = "ALL_MATCHED_POLE_CHANNELS_CERTIFIED_NONNEGATIVE"

    return {
        "schema": SCHEMA,
        "status": scan_status,
        "precision_bits": precision_bits,
        "height_count": len(HEIGHTS),
        "point_count": len(HEIGHTS) * len(NODES),
        "channel_count": len(rows),
        "status_counts": counts,
        "negative_channel_ids": negative_ids,
        "unresolved_channel_ids": unresolved_ids,
        "smallest_normalized_upper_bounds": rows[:25],
        "counterexample_candidate": None,
        "promotion_boundary": (
            "A negative channel would be a rigorous nomination only. Independent directed "
            "special-function reproduction and review of D-3201/L-3202/L-3903/L-3904 "
            "are required before candidate allocation."
        ),
    }


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision-bits", type=int, default=160)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--verification", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.precision_bits < 64:
        raise ValueError("precision_bits must be at least 64")

    from produce_certificate import build_certificate

    template, metadata = build_template()
    certificate, verification = build_certificate(template, args.precision_bits)
    summary = summarize(verification, metadata, args.precision_bits)
    write_json(args.certificate, certificate)
    write_json(args.verification, verification)
    write_json(args.summary, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
