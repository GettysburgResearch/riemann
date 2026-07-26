#!/usr/bin/env python3
"""Source-bound dense-node order-two screen for a PR71-neighborhood ordinate."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SUMMARY_SCHEMA = "riemann.x9301-dense-order2-screen.v1"


def import_local(name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


BUILD = import_local("build_pr71_nearest_certificate")
VERIFY = import_local("verify_zero_deflated_modulus")
COMPARE = import_local("compare_x9301_precision")


class ScreenError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ScreenError(f"{path} must contain an object")
    return value


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ScreenError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise ScreenError(f"{name} must be integer text") from exc
    raise ScreenError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ScreenError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ScreenError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise ScreenError(f"{name} must be an object")
    lower = rational(raw.get("lower"), f"{name}.lower")
    upper = rational(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise ScreenError(f"{name} is reversed")
    return lower, upper


def scientific(value: Fraction) -> str:
    with localcontext() as context:
        context.prec = 18
        return format(
            Decimal(value.numerator) / Decimal(value.denominator), ".17E"
        ).lower()


def ordered_point_ids(primitive: dict[str, Any]) -> tuple[str, ...]:
    raw_points = primitive.get("points")
    if not isinstance(raw_points, list) or len(raw_points) < 4:
        raise ScreenError("primitive must contain at least four points")
    parsed: list[tuple[Fraction, str]] = []
    seen: set[str] = set()
    for index, point in enumerate(raw_points):
        if not isinstance(point, dict):
            raise ScreenError(f"primitive point {index} must be an object")
        identifier = point.get("id")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in seen
        ):
            raise ScreenError("primitive point IDs must be nonempty and unique")
        seen.add(identifier)
        x = rational(point.get("x"), f"primitive point {identifier}.x")
        if x <= 0:
            raise ScreenError("horizontal offsets must be positive")
        parsed.append((x * x, identifier))
    parsed.sort()
    if any(parsed[index][0] == parsed[index + 1][0] for index in range(len(parsed) - 1)):
        raise ScreenError("squared horizontal nodes must be distinct")
    return tuple(identifier for _, identifier in parsed)


def generate_order2_rows(point_ids: tuple[str, ...]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for union_indices in itertools.combinations(range(len(point_ids)), 4):
        first = union_indices[0]
        for partner in union_indices[1:]:
            row_indices = (first, partner)
            column_indices = tuple(
                index for index in union_indices if index not in row_indices
            )
            row_ids = [point_ids[index] for index in row_indices]
            column_ids = [point_ids[index] for index in column_indices]
            rows.append(
                {
                    "id": (
                        f"d2-r{'_'.join(row_ids)}-c{'_'.join(column_ids)}"
                    ),
                    "kind": "deflated-cross-loewner-determinant",
                    "rows": row_ids,
                    "columns": column_ids,
                }
            )
    expected = 3 * len(tuple(itertools.combinations(point_ids, 4)))
    if len(rows) != expected or len({row["id"] for row in rows}) != expected:
        raise ScreenError("order-two generator failed exact coverage")
    return rows


def source_bound_verify(
    certificate: dict[str, Any],
    primitive: dict[str, Any],
    zero_block: dict[str, Any],
) -> dict[str, Any]:
    bindings = VERIFY.verify_source_artifacts(certificate, primitive, zero_block)
    result = VERIFY.verify(certificate)
    result["source_artifacts"] = bindings
    result["source_artifacts_verified"] = True
    if result["certified_negative_rows"]:
        result["verdict"] = (
            "NEGATIVE_ZERO_DEFLATED_XI_MODULUS_WITNESS_PENDING_REVIEW"
        )
    result.pop("verification_sha256", None)
    result["verification_sha256"] = VERIFY.canonical_sha(result)
    return result


def row_map(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw_rows = result.get("rows")
    if not isinstance(raw_rows, list):
        raise ScreenError("verification rows must be a list")
    mapped: dict[str, dict[str, Any]] = {}
    for row in raw_rows:
        if (
            not isinstance(row, dict)
            or not isinstance(row.get("id"), str)
            or row["id"] in mapped
        ):
            raise ScreenError("verification rows are malformed or duplicated")
        mapped[row["id"]] = row
    return mapped


def midpoint(value: VERIFY.Interval) -> Fraction:
    return (value.lower + value.upper) / 2


def ranking_entry(
    spec: dict[str, Any],
    verified: dict[str, Any],
    points: dict[str, dict[str, Any]],
    secants: dict[tuple[str, str], Fraction],
) -> dict[str, Any]:
    row_ids, column_ids = spec["rows"], spec["columns"]

    def secant_mid(left: str, right: str) -> Fraction:
        key = tuple(sorted((left, right)))
        if key not in secants:
            raise ScreenError("missing cached secant midpoint")
        return secants[key]

    a = secant_mid(row_ids[0], column_ids[0])
    b = secant_mid(row_ids[0], column_ids[1])
    c = secant_mid(row_ids[1], column_ids[0])
    d = secant_mid(row_ids[1], column_ids[1])
    determinant_midpoint = midpoint(
        VERIFY.Interval(*interval(verified["interval"], "row.interval"))
    )
    permanent_scale = abs(a * d) + abs(b * c)
    eta = (
        determinant_midpoint / permanent_scale
        if permanent_scale
        else Fraction(0)
    )
    row_u = [points[identifier]["u"] for identifier in row_ids]
    column_u = [points[identifier]["u"] for identifier in column_ids]
    row_delta = (row_u[1] - row_u[0]) / (row_u[1] + row_u[0])
    column_delta = (column_u[1] - column_u[0]) / (
        column_u[1] + column_u[0]
    )
    geometry_adjusted_eta = eta / (row_delta * column_delta)
    lower, upper = interval(verified["interval"], "row.interval")
    return {
        "id": spec["id"],
        "rows": row_ids,
        "columns": column_ids,
        "status": verified["status"],
        "interval_sha256": canonical_sha(verified["interval"]),
        "lower_scientific": scientific(lower),
        "upper_scientific": scientific(upper),
        "midpoint_scientific": scientific(determinant_midpoint),
        "permanent_normalized_midpoint": scientific(eta),
        "geometry_adjusted_midpoint": scientific(geometry_adjusted_eta),
        "_raw_midpoint": determinant_midpoint,
        "_adjusted_eta": geometry_adjusted_eta,
    }


def summarize(
    low_primitive: dict[str, Any],
    high_primitive: dict[str, Any],
    zero_block: dict[str, Any],
    nearest_count: int,
    top_k: int = 20,
) -> dict[str, Any]:
    if nearest_count <= 0 or top_k <= 0:
        raise ScreenError("nearest_count and top_k must be positive")
    point_ids = ordered_point_ids(high_primitive)
    if ordered_point_ids(low_primitive) != point_ids:
        raise ScreenError("primitive point grids differ")
    rows = generate_order2_rows(point_ids)
    config = {
        "schema": BUILD.CONFIG_SCHEMA,
        "normalization_id": BUILD.NORMALIZATION,
        "log_terms": 256,
        "rows": rows,
    }
    low_certificate = BUILD.build(
        low_primitive, zero_block, config, nearest_count
    )
    high_certificate = BUILD.build(
        high_primitive, zero_block, config, nearest_count
    )
    low_result = source_bound_verify(
        low_certificate, low_primitive, zero_block
    )
    high_result = source_bound_verify(
        high_certificate, high_primitive, zero_block
    )
    comparison = COMPARE.compare(low_certificate, high_certificate)
    if comparison.get("all_high_intervals_nested") is not True:
        raise ScreenError("precision nesting failed")

    high_rows = row_map(high_result)
    if set(high_rows) != {row["id"] for row in rows}:
        raise ScreenError("verification rows differ from generated coverage")
    points = VERIFY.parse_points(high_certificate, require_digests=True)
    bins = VERIFY.parse_zero_bins(
        high_certificate,
        rational(high_certificate["ordinate"], "certificate.ordinate"),
        "RIEMANN_XI_DIRECTED",
    )
    terms = integer(high_certificate.get("log_terms"), "log_terms")
    values = {
        identifier: VERIFY.deflated_log_value(point, bins, terms)
        for identifier, point in points.items()
    }
    secants: dict[tuple[str, str], Fraction] = {}
    for left, right in itertools.combinations(point_ids, 2):
        value = VERIFY.secant(
            points[left], points[right], values[left], values[right]
        )
        secants[tuple(sorted((left, right)))] = midpoint(value)

    specs = {row["id"]: row for row in rows}
    ranked = [
        ranking_entry(specs[identifier], verified, points, secants)
        for identifier, verified in high_rows.items()
    ]
    status_counts = {
        status: sum(row["status"] == status for row in ranked)
        for status in ("CERTIFIED_NEGATIVE", "UNRESOLVED", "CERTIFIED_NONNEGATIVE")
    }

    def public(row: dict[str, Any]) -> dict[str, Any]:
        return {key: value for key, value in row.items() if not key.startswith("_")}

    by_adjusted = sorted(ranked, key=lambda row: row["_adjusted_eta"])
    by_raw = sorted(ranked, key=lambda row: row["_raw_midpoint"])
    anomalous = [
        public(row)
        for row in ranked
        if row["status"] != "CERTIFIED_NONNEGATIVE"
    ]
    interval_stream = {
        identifier: high_rows[identifier]["interval"]
        for identifier in sorted(high_rows)
    }
    if status_counts["CERTIFIED_NEGATIVE"]:
        verdict = "NEGATIVE_DENSE_ORDER2_ROW_PENDING_REVIEW"
        nomination = "PENDING_384_512_REPLAY"
    elif status_counts["UNRESOLVED"]:
        verdict = "UNRESOLVED_DENSE_ORDER2_SCREEN"
        nomination = None
    else:
        verdict = "NO_NEGATIVE_IN_DENSE_ORDER2_SCREEN"
        nomination = None

    result = {
        "schema": SUMMARY_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "target": high_certificate["ordinate"],
        "point_ids_in_increasing_u_order": list(point_ids),
        "point_count": len(point_ids),
        "order2_row_count": len(rows),
        "coverage_formula": f"3 * binomial({len(point_ids)}, 4)",
        "row_specification_sha256": canonical_sha(rows),
        "nearest_count": nearest_count,
        "selection_scope": high_certificate["source"]["selection_scope"],
        "selection_guard_sha256": canonical_sha(
            high_certificate["source"]["selection_guard"]
        ),
        "zero_block_artifact_sha256": canonical_sha(zero_block),
        "low_precision_bits": integer(
            low_primitive.get("precision_bits"), "low precision"
        ),
        "high_precision_bits": integer(
            high_primitive.get("precision_bits"), "high precision"
        ),
        "all_high_intervals_nested": True,
        "status_counts": status_counts,
        "verdict": verdict,
        "counterexample_nomination": nomination,
        "top_geometry_adjusted_rows": [
            public(row) for row in by_adjusted[:top_k]
        ],
        "top_raw_rows": [public(row) for row in by_raw[:top_k]],
        "nonpositive_or_unresolved_rows": anomalous,
        "high_row_interval_stream_sha256": canonical_sha(interval_stream),
        "low_certificate_sha256": low_certificate["certificate_sha256"],
        "high_certificate_sha256": high_certificate["certificate_sha256"],
        "low_verification_sha256": low_result["verification_sha256"],
        "high_verification_sha256": high_result["verification_sha256"],
        "proof_boundary": (
            "All row signs and precision nesting are exact. Ranking metrics use "
            "interval midpoints and are heuristic only. A negative requires "
            "384/512-bit replay, independent xi reproduction, and analytic review."
        ),
    }
    result["summary_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low_primitive", type=Path)
    parser.add_argument("high_primitive", type=Path)
    parser.add_argument("zero_block", type=Path)
    parser.add_argument("--nearest-count", type=int, default=256)
    parser.add_argument("--top-k", type=int, default=20)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = summarize(
            load(args.low_primitive),
            load(args.high_primitive),
            load(args.zero_block),
            args.nearest_count,
            args.top_k,
        )
        code = 1 if result["counterexample_nomination"] else 0
    except (
        OSError,
        json.JSONDecodeError,
        ScreenError,
        BUILD.BuildError,
        VERIFY.CertificateError,
        COMPARE.ComparisonError,
        KeyError,
        ZeroDivisionError,
    ) as exc:
        result = {"schema": SUMMARY_SCHEMA, "verified": False, "error": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
