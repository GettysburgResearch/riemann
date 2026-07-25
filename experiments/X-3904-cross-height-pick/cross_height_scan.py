#!/usr/bin/env python3
"""Rigorous finite Arb scan of exact cross-height matched-pole Pick packets."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

from arb_value_producer import build_certificate
from cross_height import Gaussian, fraction_json, matched_pole_vector, parse_fraction
from verify_cross_height_certificate import verify_certificate

SCHEMA = "riemann.xi-cross-height-pick-scan.v1"

CENTERS: tuple[tuple[str, Fraction], ...] = (
    ("optimized", Fraction(20225875608343121406355, 1 << 32)),
    ("optimized-right001", Fraction(20225875608343164356028, 1 << 32)),
    ("earlier", Fraction(13561059072446511459506, 1 << 32)),
    ("earlier-left40", Fraction(13561059072274712767666, 1 << 32)),
)


def binary_json(value: Fraction) -> dict[str, str | int]:
    value = Fraction(value)
    denominator = value.denominator
    if denominator & (denominator - 1):
        raise ValueError(f"{value} is not dyadic")
    exponent = -(denominator.bit_length() - 1)
    mantissa = value.numerator
    while mantissa and mantissa % 2 == 0:
        mantissa //= 2
        exponent += 1
    return {"mantissa": str(mantissa), "exponent": exponent}


def vector_json(vector: Sequence[Gaussian]) -> list[dict[str, dict[str, str]]]:
    return [value.to_json() for value in vector]


def add_point(
    registry: dict[tuple[Fraction, Fraction], str],
    rows: list[dict[str, object]],
    x: Fraction,
    t: Fraction,
) -> str:
    key = (Fraction(x), Fraction(t))
    if key in registry:
        return registry[key]
    identifier = f"p{len(rows):04d}"
    registry[key] = identifier
    rows.append({"id": identifier, "x": binary_json(key[0]), "t": binary_json(key[1])})
    return identifier


def add_packet(
    *,
    center_label: str,
    center: Fraction,
    tag: str,
    x_values: Sequence[Fraction],
    y_values: Sequence[Fraction],
    delta: Fraction,
    point_registry: dict[tuple[Fraction, Fraction], str],
    points: list[dict[str, object]],
    channels: list[dict[str, object]],
) -> None:
    if len(x_values) != len(y_values):
        raise ValueError("x/y length mismatch")
    relative_nodes = [Gaussian(x, y) for x, y in zip(x_values, y_values)]
    model_d = delta * delta
    vector = matched_pole_vector(relative_nodes, model_d)
    point_ids = [
        add_point(point_registry, points, x, center + y)
        for x, y in zip(x_values, y_values)
    ]
    identifier = f"ch-{center_label}-{tag}"
    channels.append({
        "id": identifier,
        "kind": "complex-matched-pole-rayleigh",
        "points": point_ids,
        "vector": vector_json(vector),
        "model_center_t": fraction_json(center),
        "model_d": fraction_json(model_d),
        "packet": {
            "claim": "L-3905",
            "x_values": [fraction_json(value) for value in x_values],
            "y_values": [fraction_json(value) for value in y_values],
            "model_delta": fraction_json(delta),
        },
    })


def build_template(precision_bits: int) -> dict[str, object]:
    if precision_bits < 96:
        raise ValueError("precision_bits must be at least 96")
    points: list[dict[str, object]] = []
    channels: list[dict[str, object]] = []
    registry: dict[tuple[Fraction, Fraction], str] = {}

    for center_label, center in CENTERS:
        for exponent in range(20, 13, -1):
            xs = [
                Fraction(1, 1 << exponent),
                Fraction(1, 1 << (exponent - 1)),
                Fraction(1, 1 << (exponent - 2)),
            ]
            for numerator in (1, 2, 3):
                model_fraction = Fraction(numerator, 4)
                delta = xs[0] + model_fraction * (xs[1] - xs[0])
                patterns = (
                    ("sym", [-2 * delta, Fraction(0), 2 * delta]),
                    ("fan", [Fraction(0), -2 * delta, 4 * delta]),
                )
                for pattern_name, y_values in patterns:
                    add_packet(
                        center_label=center_label,
                        center=center,
                        tag=f"n3-e{exponent}-f{numerator}-{pattern_name}",
                        x_values=xs,
                        y_values=y_values,
                        delta=delta,
                        point_registry=registry,
                        points=points,
                        channels=channels,
                    )

        for exponent in range(20, 15, -1):
            xs = [Fraction(1, 1 << (exponent - offset)) for offset in range(5)]
            delta = (xs[0] + xs[1]) / 2
            patterns = (
                ("centeralt", [Fraction(0), -2 * delta, 2 * delta, -4 * delta, 4 * delta]),
                ("fan", [Fraction(0), -2 * delta, 4 * delta, -6 * delta, 8 * delta]),
            )
            for pattern_name, y_values in patterns:
                add_packet(
                    center_label=center_label,
                    center=center,
                    tag=f"n5-e{exponent}-{pattern_name}",
                    x_values=xs,
                    y_values=y_values,
                    delta=delta,
                    point_registry=registry,
                    points=points,
                    channels=channels,
                )

    return {
        "precision_bits": precision_bits,
        "series_cap": 3,
        "points": points,
        "channels": channels,
        "declared_channel_ids": [str(channel["id"]) for channel in channels],
    }


def interval_from_json(raw: Any) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise ValueError("interval must be an object")
    return parse_fraction(raw["lower"], "lower"), parse_fraction(raw["upper"], "upper")


def summarize(verification: dict[str, Any], precision_bits: int) -> dict[str, object]:
    counts = {
        "CERTIFIED_NEGATIVE": 0,
        "CERTIFIED_NONNEGATIVE": 0,
        "UNRESOLVED_ZERO_TOUCH": 0,
    }
    rows: list[dict[str, object]] = []
    for channel in verification["channels"]:
        status = str(channel["status"])
        counts[status] += 1
        lower, upper = interval_from_json(channel["normalized_interval"])
        rows.append({
            "id": channel["id"],
            "status": status,
            "normalized_lower": fraction_json(lower),
            "normalized_upper": fraction_json(upper),
            "normalized_lower_approx": format(float(lower), ".17g"),
            "normalized_upper_approx": format(float(upper), ".17g"),
            "modeled_pair_normalized": channel["modeled_pair_normalized"],
            "normalized_primitive_rectangle_l1_amplification": channel[
                "normalized_primitive_rectangle_l1_amplification"
            ],
        })
    rows.sort(key=lambda row: parse_fraction(row["normalized_upper"], "normalized_upper"))
    negative = [str(row["id"]) for row in rows if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [str(row["id"]) for row in rows if row["status"] == "UNRESOLVED_ZERO_TOUCH"]
    return {
        "schema": SCHEMA,
        "status": (
            "DIRECTED_NEGATIVE_FOUND_PENDING_INDEPENDENT_REPRODUCTION"
            if negative else
            "NO_NEGATIVE_UNRESOLVED_CHANNELS_PRESENT"
            if unresolved else
            "ALL_CROSS_HEIGHT_CHANNELS_CERTIFIED_NONNEGATIVE"
        ),
        "precision_bits": precision_bits,
        "center_count": len(CENTERS),
        "point_count": verification["point_count"],
        "channel_count": verification["channel_count"],
        "status_counts": counts,
        "negative_channel_ids": negative,
        "unresolved_channel_ids": unresolved,
        "smallest_normalized_upper_bounds": rows[:30],
        "counterexample_candidate": None,
        "promotion_boundary": (
            "A negative direct interval is a rigorous nomination only; independent directed "
            "special-function reproduction and review of D-3201/L-3202/L-3905 are required."
        ),
    }


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision-bits", type=int, default=160)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--verification", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args(argv)

    config = build_template(args.precision_bits)
    certificate = build_certificate(config)
    verification = verify_certificate(certificate)
    summary = summarize(verification, args.precision_bits)
    write_json(args.certificate, certificate)
    write_json(args.verification, verification)
    write_json(args.summary, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
