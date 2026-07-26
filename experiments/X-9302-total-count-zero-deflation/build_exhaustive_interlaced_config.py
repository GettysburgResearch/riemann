#!/usr/bin/env python3
"""Build every interlaced total-count-deflated row on a primitive point table."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.xi-modulus-zero-deflation-config.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ValueError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ValueError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def ordered_point_ids(primitives: dict[str, Any]) -> list[str]:
    raw = primitives.get("points")
    if not isinstance(raw, list):
        raise ValueError("primitive points must be a list")
    rows: list[tuple[Fraction, str]] = []
    seen: set[str] = set()
    for index, point in enumerate(raw):
        if not isinstance(point, dict):
            raise ValueError(f"point {index} must be an object")
        identifier = point.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise ValueError("point IDs must be nonempty and unique")
        seen.add(identifier)
        x = rational(point.get("x"), f"points[{index}].x")
        if x <= 0:
            raise ValueError("point offsets must be positive")
        rows.append((x * x, identifier))
    rows.sort()
    if any(rows[i][0] == rows[i + 1][0] for i in range(len(rows) - 1)):
        raise ValueError("squared point offsets must be distinct")
    return [identifier for _, identifier in rows]


def build(point_ids: Sequence[str], *, log_terms: int = 256) -> dict[str, Any]:
    identifiers = list(point_ids)
    if len(identifiers) < 4 or len(set(identifiers)) != len(identifiers):
        raise ValueError("at least four unique ordered point IDs are required")
    if log_terms < 32:
        raise ValueError("log_terms must be at least 32")

    rows: list[dict[str, Any]] = []
    for left, right in itertools.combinations(range(len(identifiers)), 2):
        rows.append(
            {
                "id": f"all-m-{left}-{right}",
                "kind": "deflated-monotonicity",
                "left": identifiers[left],
                "right": identifiers[right],
            }
        )

    for order in range(2, min(4, len(identifiers) // 2) + 1):
        for indices in itertools.combinations(range(len(identifiers)), 2 * order):
            row_indices = indices[0::2]
            column_indices = indices[1::2]
            rows.append(
                {
                    "id": f"all-d{order}-" + "-".join(map(str, indices)),
                    "kind": "deflated-cross-loewner-determinant",
                    "rows": [identifiers[index] for index in row_indices],
                    "columns": [identifiers[index] for index in column_indices],
                }
            )

    return {
        "schema": SCHEMA,
        "normalization_id": NORMALIZATION,
        "log_terms": log_terms,
        "point_order": identifiers,
        "rows": rows,
        "row_counts": {
            "monotonicity": len(identifiers) * (len(identifiers) - 1) // 2,
            **{
                f"order_{order}": math.comb(len(identifiers), 2 * order)
                for order in range(2, min(4, len(identifiers) // 2) + 1)
            },
        },
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("--log-terms", type=int, default=256)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    primitives = json.loads(args.primitives.read_text(encoding="utf-8"))
    if not isinstance(primitives, dict):
        raise ValueError("primitive artifact must contain an object")
    result = build(
        ordered_point_ids(primitives),
        log_terms=args.log_terms,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["row_counts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
