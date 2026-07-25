#!/usr/bin/env python3
"""Append exact eight-node barycentric Pick channels to an Arb feature table.

The primitive special-function rectangles are left unchanged. This producer
only reconstructs the exact rational vector

    c_i = 1 / product_{j != i} (x_i-x_j)

up to one primitive integer scale and appends one ``real-pick-rayleigh``
channel at each *complete* exact ordinate found in the supplied X-3902 table.
It therefore supports both the full 65-height grid and a focused one-height
precision ladder. The independent ``verify_value_certificate.py`` checker
remains responsible for the final outward interval and sign.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from pathlib import Path
from typing import Any, Iterable, Sequence

SCHEMA = "riemann.xi-passivity-value-balls.v1"
X_BITS = (17, 15, 13, 11, 10, 9, 7, 5)
T_MIN = -32
T_MAX = 32
CHANNEL_PREFIX = "bary8"


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value, 10)
    raise ValueError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ValueError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction | int) -> dict[str, str]:
    value = Fraction(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def point_id(t_index: int, x_bits: int) -> str:
    return f"t_{'m' if t_index < 0 else 'p'}{abs(t_index)}_x{x_bits}"


def barycentric_weights(nodes: Sequence[Fraction]) -> tuple[Fraction, ...]:
    if len(nodes) < 2 or len(set(nodes)) != len(nodes):
        raise ValueError("nodes must be distinct and contain at least two values")
    result: list[Fraction] = []
    for index, node in enumerate(nodes):
        denominator = Fraction(1)
        for other_index, other in enumerate(nodes):
            if index != other_index:
                denominator *= node - other
        result.append(1 / denominator)
    return tuple(result)


def primitive_integer_scale(values: Iterable[Fraction]) -> tuple[int, ...]:
    fractions = tuple(Fraction(value) for value in values)
    denominator = 1
    for value in fractions:
        denominator = lcm(denominator, value.denominator)
    integers = [
        value.numerator * (denominator // value.denominator)
        for value in fractions
    ]
    common = reduce(gcd, (abs(value) for value in integers if value), 0)
    if common == 0:
        raise ValueError("zero vector")
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    if first > 0:
        integers = [-value for value in integers]
    return tuple(integers)


def exact_vector() -> tuple[int, ...]:
    nodes = tuple(Fraction(1, 1 << bits) for bits in X_BITS)
    return primitive_integer_scale(barycentric_weights(nodes))


def verify_vector(vector: Sequence[int]) -> None:
    nodes = tuple(Fraction(1, 1 << bits) for bits in X_BITS)
    if len(vector) != len(nodes) or not any(vector):
        raise ValueError("invalid barycentric vector")
    # Ordinary barycentric weights annihilate all polynomials of degree <= n-2.
    for power in range(len(nodes) - 1):
        value = sum(Fraction(vector[i]) * nodes[i] ** power for i in range(len(nodes)))
        if value != 0:
            raise ValueError(f"moment {power} did not cancel: {value}")
    leading = sum(
        Fraction(vector[i]) * nodes[i] ** (len(nodes) - 1)
        for i in range(len(nodes))
    )
    if leading == 0:
        raise ValueError("leading barycentric moment unexpectedly vanished")


def complete_t_indices(point_map: dict[str, dict[str, Any]]) -> tuple[int, ...]:
    indices = tuple(
        t_index
        for t_index in range(T_MIN, T_MAX + 1)
        if all(point_id(t_index, bits) in point_map for bits in X_BITS)
    )
    if not indices:
        raise ValueError("the feature table contains no complete eight-node ordinate")
    # Reject partially present rows: they are more likely a truncated artifact than
    # an intentional focused producer.
    for t_index in range(T_MIN, T_MAX + 1):
        present = sum(point_id(t_index, bits) in point_map for bits in X_BITS)
        if present not in (0, len(X_BITS)):
            raise ValueError(f"ordinate {t_index} is incomplete ({present}/{len(X_BITS)} points)")
    return indices


def augment(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA!r}")
    points_raw = data.get("points")
    channels = data.get("channels")
    declared = data.get("declared_channel_ids")
    if not isinstance(points_raw, list) or not isinstance(channels, list):
        raise ValueError("points and channels must be arrays")
    if not isinstance(declared, list) or not all(isinstance(item, str) for item in declared):
        raise ValueError("declared_channel_ids must be an array of strings")

    point_map: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(points_raw):
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str):
            raise ValueError(f"points[{index}] is malformed")
        identifier = raw["id"]
        if identifier in point_map:
            raise ValueError(f"duplicate point ID {identifier}")
        point_map[identifier] = raw

    existing_ids = {
        channel.get("id")
        for channel in channels
        if isinstance(channel, dict) and isinstance(channel.get("id"), str)
    }
    vector = exact_vector()
    verify_vector(vector)
    vector_json = [fraction_json(value) for value in vector]
    t_indices = complete_t_indices(point_map)

    appended: list[str] = []
    for t_index in t_indices:
        identifiers = [point_id(t_index, bits) for bits in X_BITS]
        selected = []
        for identifier, bits in zip(identifiers, X_BITS):
            raw = point_map[identifier]
            x = parse_fraction(raw.get("x"), f"point {identifier}.x")
            if x != Fraction(1, 1 << bits):
                raise ValueError(f"point {identifier} has unexpected x={x}")
            selected.append(raw)
        heights = {
            parse_fraction(raw.get("t"), f"point {raw['id']}.t")
            for raw in selected
        }
        if len(heights) != 1:
            raise ValueError(f"row {t_index} mixes ordinates")

        channel_id = f"{CHANNEL_PREFIX}_t_{'m' if t_index < 0 else 'p'}{abs(t_index)}"
        if channel_id in existing_ids:
            raise ValueError(f"channel {channel_id} already exists")
        channels.append(
            {
                "id": channel_id,
                "kind": "real-pick-rayleigh",
                "points": identifiers,
                "vector": vector_json,
                "construction": {
                    "kind": "primitive-integer-barycentric",
                    "x_bits": list(X_BITS),
                    "moment_cancellations": list(range(len(X_BITS) - 1)),
                },
            }
        )
        declared.append(channel_id)
        existing_ids.add(channel_id)
        appended.append(channel_id)

    data.pop("certificate_sha256", None)
    data["barycentric_extension"] = {
        "schema": "riemann.xi-barycentric-grid-extension.v1",
        "vector": [str(value) for value in vector],
        "x_bits": list(X_BITS),
        "t_indices": list(t_indices),
        "channel_ids": appended,
        "exact_moment_cancellations": list(range(len(X_BITS) - 1)),
        "proof_boundary": (
            "This extension contains exact rational channel data only. Primitive "
            "xi'/xi rectangles and final signs are supplied and checked elsewhere."
        ),
    }
    return data


def self_test() -> None:
    expected = (
        -4260607557632,
        5816828559360,
        -1715672285184,
        189885604480,
        -31899582000,
        1466028564,
        -767715,
        127,
    )
    vector = exact_vector()
    if vector != expected:
        raise AssertionError((vector, expected))
    verify_vector(vector)
    # Focused-grid detection.
    dummy = {
        point_id(1, bits): {
            "id": point_id(1, bits),
            "x": fraction_json(Fraction(1, 1 << bits)),
            "t": fraction_json(Fraction(123)),
        }
        for bits in X_BITS
    }
    if complete_t_indices(dummy) != (1,):
        raise AssertionError("focused ordinate detection failed")
    print("exact eight-node barycentric vector, seven moments, and focused row verified")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, nargs="?")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.input is None:
        parser.error("input is required unless --self-test is used")
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("certificate root must be an object")
    result = augment(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
