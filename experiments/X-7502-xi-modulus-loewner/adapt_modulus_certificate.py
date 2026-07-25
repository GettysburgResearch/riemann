#!/usr/bin/env python3
"""Adapt an X-7501 direct-xi modulus certificate to L-7504 log-Loewner rows."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SOURCE_SCHEMA = "riemann.xi-modulus-witness.v1"
TARGET_SCHEMA = "riemann.xi-modulus-log-loewner.v1"


class AdapterError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AdapterError(f"{path} must contain an object")
    return value


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AdapterError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise AdapterError(f"{name} must be an object")
    n = exact_int(raw.get("numerator"), f"{name}.numerator")
    d = exact_int(raw.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise AdapterError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise AdapterError(f"{name} must be an object")
    lo = rational(raw.get("lower"), f"{name}.lower")
    hi = rational(raw.get("upper"), f"{name}.upper")
    if lo > hi:
        raise AdapterError(f"reversed interval at {name}")
    return lo, hi


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: tuple[Fraction, Fraction]) -> dict[str, dict[str, int]]:
    return {"lower": fj(value[0]), "upper": fj(value[1])}


def square(value: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    lo, hi = value
    upper = max(lo * lo, hi * hi)
    lower = Fraction(0) if lo <= 0 <= hi else min(lo * lo, hi * hi)
    return lower, upper


def add(
    a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return a[0] + b[0], a[1] + b[1]


def adapt(source: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    if source.get("schema") != SOURCE_SCHEMA:
        raise AdapterError("unsupported source schema")
    if manifest.get("schema") != "riemann.xi-modulus-log-loewner-manifest.v1":
        raise AdapterError("unsupported row manifest schema")
    if source.get("normalization_id") != manifest.get("normalization_id"):
        raise AdapterError("normalization mismatch")
    terms = exact_int(manifest.get("log_series_terms"), "log_series_terms")
    raw_points = source.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise AdapterError("source points must be a nonempty list")
    points = []
    identifiers = set()
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str):
            raise AdapterError(f"malformed source point {index}")
        identifier = raw["id"]
        if identifier in identifiers:
            raise AdapterError("duplicate source point id")
        identifiers.add(identifier)
        x = rational(raw.get("x"), f"points[{index}].x")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise AdapterError("source point lacks xi_rectangle")
        real = interval(rectangle.get("real"), f"points[{index}].real")
        imag = interval(rectangle.get("imag"), f"points[{index}].imag")
        h = add(square(real), square(imag))
        points.append({"id": identifier, "u": fj(x * x), "h_interval": ij(h)})
    rows = manifest.get("rows")
    if not isinstance(rows, list) or not rows:
        raise AdapterError("manifest rows must be nonempty")
    for row in rows:
        if not isinstance(row, dict):
            raise AdapterError("malformed row")
        ids = row.get("row_points", []) + row.get("column_points", [])
        if any(identifier not in identifiers for identifier in ids):
            raise AdapterError("manifest references an unknown point")
    return {
        "schema": TARGET_SCHEMA,
        "classification": source.get("classification"),
        "normalization_id": source.get("normalization_id"),
        "log_series_terms": terms,
        "source_certificate_sha256": source.get("certificate_sha256"),
        "points": points,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = adapt(load(args.source), load(args.manifest))
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {"point_count": len(result["points"]), "row_count": len(result["rows"])},
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
