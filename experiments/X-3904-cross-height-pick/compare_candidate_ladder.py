#!/usr/bin/env python3
"""Require nested intervals and identical frozen metadata for one candidate ladder."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def parse_fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ValueError(f"{name} must be an object")
    numerator = raw.get("numerator")
    denominator = raw.get("denominator")
    if isinstance(numerator, bool) or isinstance(denominator, bool):
        raise ValueError(f"{name} contains bool")
    numerator = int(numerator)
    denominator = int(denominator)
    if denominator <= 0:
        raise ValueError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def channel(data: dict[str, Any]) -> dict[str, Any]:
    rows = data.get("channels")
    if not isinstance(rows, list) or len(rows) != 1 or not isinstance(rows[0], dict):
        raise ValueError("verification must contain exactly one channel")
    return rows[0]


def compare(files: list[Path]) -> dict[str, object]:
    if len(files) < 2:
        raise ValueError("at least two precision levels are required")
    rows = []
    previous_lower = previous_upper = None
    reference_id = reference_vector = reference_points = None
    for path in files:
        data = load(path)
        if not data.get("verified"):
            raise ValueError(f"{path} is not a verified certificate")
        row = channel(data)
        identifier = row.get("id")
        vector_sha = row.get("vector_sha256")
        points = row.get("points")
        if reference_id is None:
            reference_id, reference_vector, reference_points = identifier, vector_sha, points
        elif (identifier, vector_sha, points) != (reference_id, reference_vector, reference_points):
            raise ValueError("candidate identity changed across precision levels")
        raw = row.get("normalized_interval")
        if not isinstance(raw, dict):
            raise ValueError("normalized interval missing")
        lower = parse_fraction(raw.get("lower"), "lower")
        upper = parse_fraction(raw.get("upper"), "upper")
        if lower > upper:
            raise ValueError("inverted interval")
        if previous_lower is not None and not (
            previous_lower <= lower <= upper <= previous_upper
        ):
            raise ValueError("higher-precision interval is not nested")
        previous_lower, previous_upper = lower, upper
        rows.append(
            {
                "file": str(path),
                "status": row.get("status"),
                "lower": raw["lower"],
                "upper": raw["upper"],
                "width": {
                    "numerator": str((upper - lower).numerator),
                    "denominator": str((upper - lower).denominator),
                },
            }
        )
    return {
        "schema": "riemann.xi-complex-pick-candidate-ladder.v1",
        "verified": True,
        "candidate_id": reference_id,
        "vector_sha256": reference_vector,
        "point_count": len(reference_points),
        "precision_levels": rows,
        "all_intervals_nested": True,
        "final_status": rows[-1]["status"],
        "counterexample_candidate": None,
        "proof_boundary": (
            "Nesting and identity only. A negative final interval remains pending independent "
            "directed special-function reproduction and review of D-3201/L-3202."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("verification", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = compare(args.verification)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
