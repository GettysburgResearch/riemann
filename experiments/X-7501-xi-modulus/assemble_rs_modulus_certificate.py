#!/usr/bin/env python3
"""Bind FLINT Riemann--Siegel xi primitives to the exact X-7501 row manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
CERTIFICATE_SCHEMA = "riemann.xi-modulus-witness.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class AssemblyError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssemblyError(f"{path} must contain an object")
    return value


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AssemblyError(f"{name} must be an integer")
    return value


def binary_fraction(raw: Any, name: str) -> dict[str, int]:
    if not isinstance(raw, dict):
        raise AssemblyError(f"{name} must be an object")
    mantissa = exact_int(raw.get("mantissa"), f"{name}.mantissa")
    exponent = exact_int(raw.get("exponent"), f"{name}.exponent")
    if exponent >= 0:
        numerator, denominator = mantissa << exponent, 1
    else:
        numerator, denominator = mantissa, 1 << (-exponent)
        while numerator and numerator % 2 == 0:
            numerator //= 2
            denominator //= 2
    return {"numerator": numerator, "denominator": denominator}


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def point_map(points: Any, name: str) -> dict[str, dict[str, Any]]:
    if not isinstance(points, list) or not points:
        raise AssemblyError(f"{name} must be a nonempty list")
    result: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(points):
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str):
            raise AssemblyError(f"malformed {name}[{index}]")
        identifier = raw["id"]
        if not identifier or identifier in result:
            raise AssemblyError(f"invalid or duplicate point ID {identifier!r}")
        result[identifier] = raw
    return result


def assemble(primitives: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    if primitives.get("schema") != PRIMITIVE_SCHEMA:
        raise AssemblyError("unsupported primitive schema")
    if primitives.get("normalization_id") != NORMALIZATION:
        raise AssemblyError("primitive normalization mismatch")

    expected_ordinate = binary_fraction(config.get("ordinate"), "config.ordinate")
    if primitives.get("ordinate") != expected_ordinate:
        raise AssemblyError("ordinate mismatch")

    primitive_points = point_map(primitives.get("points"), "primitives.points")
    config_points = point_map(config.get("points"), "config.points")
    if set(primitive_points) != set(config_points):
        raise AssemblyError("primitive and config point sets differ")

    points = []
    for identifier in sorted(
        config_points, key=lambda item: int(item.split("-")[-1]), reverse=True
    ):
        primitive = primitive_points[identifier]
        expected_x = binary_fraction(
            config_points[identifier].get("x"), f"config.{identifier}.x"
        )
        if primitive.get("x") != expected_x:
            raise AssemblyError(f"horizontal coordinate mismatch for {identifier}")
        if primitive.get("functional_equation_residual_contains_zero") is not True:
            raise AssemblyError(f"functional-equation gate failed for {identifier}")
        rectangle = primitive.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise AssemblyError(f"missing xi rectangle for {identifier}")
        canonical = {"id": identifier, "x": expected_x, "xi_rectangle": rectangle}
        points.append(
            {
                **canonical,
                "point_sha256": canonical_digest(canonical),
                "functional_equation_reflected_rectangle": primitive.get(
                    "functional_equation_reflected_rectangle"
                ),
                "functional_equation_residual_contains_zero": True,
                "relative_accuracy_bits": primitive.get("relative_accuracy_bits"),
            }
        )

    rows = config.get("rows")
    log_rows = config.get("log_rows")
    if not isinstance(rows, list) or not rows:
        raise AssemblyError("config rows must be a nonempty list")
    if not isinstance(log_rows, list) or not log_rows:
        raise AssemblyError("config log_rows must be a nonempty list")

    certificate: dict[str, Any] = {
        "schema": CERTIFICATE_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "ordinate": expected_ordinate,
        "points": points,
        "rows": rows,
        "log_rows": log_rows,
        "producer": {
            "backend": primitives.get("backend"),
            "precision_bits": exact_int(
                primitives.get("precision_bits"), "primitives.precision_bits"
            ),
            "primitive_schema": PRIMITIVE_SCHEMA,
            "division_by_xi": False,
            "functional_equation_gate": "xi(s) overlaps xi(1-s)",
        },
    }
    certificate["certificate_sha256"] = canonical_digest(certificate)
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    certificate = assemble(load(args.primitives), load(args.config))
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": certificate["schema"],
                "point_count": len(certificate["points"]),
                "row_count": len(certificate["rows"]),
                "log_row_count": len(certificate["log_rows"]),
                "certificate_sha256": certificate["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
