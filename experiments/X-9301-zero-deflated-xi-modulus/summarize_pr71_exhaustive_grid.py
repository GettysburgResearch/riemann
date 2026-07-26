#!/usr/bin/env python3
"""Replay and compactly summarize every disjoint minor on the PR71 grid."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SUMMARY_SCHEMA = "riemann.x9301-pr71-exhaustive-grid-summary.v1"
COUNTS = (2, 4, 8, 16, 32, 64, 96, 128, 160, 192, 224, 256)


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


class ExhaustiveError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ExhaustiveError(f"{path} must contain an object")
    return value


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ExhaustiveError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise ExhaustiveError(f"{name} must be integer text") from exc
    raise ExhaustiveError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ExhaustiveError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ExhaustiveError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def row_interval(row: dict[str, Any]) -> tuple[Fraction, Fraction]:
    raw = row.get("interval")
    if not isinstance(raw, dict):
        raise ExhaustiveError("row interval must be an object")
    lower = rational(raw.get("lower"), "row.interval.lower")
    upper = rational(raw.get("upper"), "row.interval.upper")
    if lower > upper:
        raise ExhaustiveError("row interval is reversed")
    return lower, upper


def outward_scientific(value: Fraction, *, upper: bool) -> str:
    with localcontext() as context:
        context.prec = 18
        context.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        decimal = Decimal(value.numerator) / Decimal(value.denominator)
        return format(decimal, ".17E").lower()


def ordered_point_ids(primitive: dict[str, Any]) -> tuple[str, ...]:
    raw_points = primitive.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise ExhaustiveError("primitive points must be nonempty")
    parsed: list[tuple[Fraction, str]] = []
    seen: set[str] = set()
    for index, point in enumerate(raw_points):
        if not isinstance(point, dict):
            raise ExhaustiveError(f"primitive point {index} must be an object")
        identifier = point.get("id")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in seen
        ):
            raise ExhaustiveError("primitive point IDs must be nonempty and unique")
        seen.add(identifier)
        x = rational(point.get("x"), f"primitive point {identifier}.x")
        if x <= 0:
            raise ExhaustiveError("primitive horizontal offsets must be positive")
        parsed.append((x * x, identifier))
    parsed.sort()
    if any(parsed[index][0] == parsed[index + 1][0] for index in range(len(parsed) - 1)):
        raise ExhaustiveError("primitive squared nodes must be distinct")
    return tuple(identifier for _, identifier in parsed)


def determinant_pattern(
    rows: tuple[str, ...], columns: tuple[str, ...]
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    return (rows, columns) if rows < columns else (columns, rows)


def generate_exhaustive_rows(point_ids: tuple[str, ...]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for left_index, right_index in itertools.combinations(range(len(point_ids)), 2):
        left, right = point_ids[left_index], point_ids[right_index]
        rows.append(
            {
                "id": f"m-{left}-{right}",
                "kind": "deflated-monotonicity",
                "left": left,
                "right": right,
            }
        )
    for order in range(2, min(4, len(point_ids) // 2) + 1):
        for row_indices in itertools.combinations(range(len(point_ids)), order):
            remaining = tuple(
                index for index in range(len(point_ids)) if index not in row_indices
            )
            for column_indices in itertools.combinations(remaining, order):
                if row_indices > column_indices:
                    continue
                row_ids = tuple(point_ids[index] for index in row_indices)
                column_ids = tuple(point_ids[index] for index in column_indices)
                rows.append(
                    {
                        "id": (
                            f"d{order}-r{'_'.join(row_ids)}"
                            f"-c{'_'.join(column_ids)}"
                        ),
                        "kind": "deflated-cross-loewner-determinant",
                        "rows": list(row_ids),
                        "columns": list(column_ids),
                    }
                )
    validate_exhaustive_coverage(rows, point_ids)
    return rows


def validate_exhaustive_coverage(
    rows: list[dict[str, Any]], point_ids: tuple[str, ...]
) -> dict[int, int]:
    node_rank = {identifier: index for index, identifier in enumerate(point_ids)}
    expected: dict[int, set[Any]] = {
        1: {
            (point_ids[left], point_ids[right])
            for left, right in itertools.combinations(range(len(point_ids)), 2)
        }
    }
    for order in range(2, min(4, len(point_ids) // 2) + 1):
        patterns: set[Any] = set()
        for union in itertools.combinations(point_ids, 2 * order):
            for row_ids in itertools.combinations(union, order):
                row_set = set(row_ids)
                column_ids = tuple(item for item in union if item not in row_set)
                patterns.add(determinant_pattern(tuple(row_ids), column_ids))
        expected[order] = patterns

    actual: dict[int, set[Any]] = {order: set() for order in expected}
    row_ids_seen: set[str] = set()
    for row in rows:
        identifier = row.get("id")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in row_ids_seen
        ):
            raise ExhaustiveError("row IDs must be nonempty and unique")
        row_ids_seen.add(identifier)
        kind = row.get("kind")
        if kind == "deflated-monotonicity":
            left, right = row.get("left"), row.get("right")
            if left not in node_rank or right not in node_rank:
                raise ExhaustiveError("monotonicity row references an unknown node")
            if node_rank[left] >= node_rank[right]:
                raise ExhaustiveError("monotonicity nodes must be increasing")
            order = 1
            pattern: Any = (left, right)
        elif kind == "deflated-cross-loewner-determinant":
            raw_rows, raw_columns = row.get("rows"), row.get("columns")
            if not isinstance(raw_rows, list) or not isinstance(raw_columns, list):
                raise ExhaustiveError("determinant nodes must be lists")
            order = len(raw_rows)
            if order not in expected or len(raw_columns) != order:
                raise ExhaustiveError("determinant order is outside exhaustive scope")
            row_tuple, column_tuple = tuple(raw_rows), tuple(raw_columns)
            if (
                len(set(row_tuple)) != order
                or len(set(column_tuple)) != order
                or set(row_tuple) & set(column_tuple)
                or any(item not in node_rank for item in row_tuple + column_tuple)
                or tuple(sorted(row_tuple, key=node_rank.get)) != row_tuple
                or tuple(sorted(column_tuple, key=node_rank.get)) != column_tuple
            ):
                raise ExhaustiveError("determinant nodes are not valid disjoint lists")
            pattern = determinant_pattern(row_tuple, column_tuple)
        else:
            raise ExhaustiveError(f"unsupported exhaustive row kind {kind!r}")
        if pattern in actual[order]:
            raise ExhaustiveError("duplicate mathematical row pattern")
        actual[order].add(pattern)

    if actual != expected:
        raise ExhaustiveError("row set does not exactly cover the exhaustive grid")
    return {order: len(patterns) for order, patterns in sorted(actual.items())}


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


def verification_rows(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw_rows = result.get("rows")
    if not isinstance(raw_rows, list):
        raise ExhaustiveError("verification rows must be a list")
    mapped: dict[str, dict[str, Any]] = {}
    for row in raw_rows:
        if (
            not isinstance(row, dict)
            or not isinstance(row.get("id"), str)
            or row["id"] in mapped
        ):
            raise ExhaustiveError("verification rows are malformed or duplicated")
        mapped[row["id"]] = row
    return mapped


def summarize(
    low_primitive: dict[str, Any],
    high_primitive: dict[str, Any],
    zero_block: dict[str, Any],
    counts: tuple[int, ...] = COUNTS,
) -> dict[str, Any]:
    if not counts or any(
        count <= 0 or (index and count <= counts[index - 1])
        for index, count in enumerate(counts)
    ):
        raise ExhaustiveError("counts must be positive and strictly increasing")
    low_precision = integer(low_primitive.get("precision_bits"), "low precision")
    high_precision = integer(high_primitive.get("precision_bits"), "high precision")
    if low_precision >= high_precision:
        raise ExhaustiveError("primitive precisions must be strictly increasing")
    point_ids = ordered_point_ids(high_primitive)
    if ordered_point_ids(low_primitive) != point_ids:
        raise ExhaustiveError("primitive point grids differ")

    rows = generate_exhaustive_rows(point_ids)
    row_counts = validate_exhaustive_coverage(rows, point_ids)
    config = {
        "schema": BUILD.CONFIG_SCHEMA,
        "normalization_id": BUILD.NORMALIZATION,
        "log_terms": 256,
        "rows": rows,
    }
    previous_selected: set[int] = set()
    previous_determinants: dict[str, tuple[Fraction, Fraction]] | None = None
    determinant_descent = True
    all_high_strictly_positive = True
    rungs: list[dict[str, Any]] = []

    for count in counts:
        low_certificate = BUILD.build(
            low_primitive, zero_block, config, count
        )
        high_certificate = BUILD.build(
            high_primitive, zero_block, config, count
        )
        low_result = source_bound_verify(
            low_certificate, low_primitive, zero_block
        )
        high_result = source_bound_verify(
            high_certificate, high_primitive, zero_block
        )
        comparison = COMPARE.compare(low_certificate, high_certificate)
        if comparison.get("all_high_intervals_nested") is not True:
            raise ExhaustiveError(f"precision nesting failed at rung {count}")

        high_rows = verification_rows(high_result)
        if len(high_rows) != len(rows):
            raise ExhaustiveError("verification row count differs from exhaustive set")
        selected_raw = high_certificate["source"].get("selected_zero_indices")
        if not isinstance(selected_raw, list):
            raise ExhaustiveError("selected zero indices must be a list")
        selected = {
            integer(value, "selected zero index") for value in selected_raw
        }
        if len(selected) != count or not previous_selected < selected:
            raise ExhaustiveError("globally-nearest selections are not cumulative")
        previous_selected = selected

        statuses_by_order: dict[int, dict[str, int]] = {}
        strict_positive = 0
        for row in high_rows.values():
            order = (
                1
                if row.get("kind") == "deflated-monotonicity"
                else integer(row.get("order"), "row order")
            )
            bucket = statuses_by_order.setdefault(
                order, {"positive": 0, "negative": 0, "unresolved": 0}
            )
            lower, upper = row_interval(row)
            if lower > 0 and row.get("status") == "CERTIFIED_NONNEGATIVE":
                bucket["positive"] += 1
                strict_positive += 1
            elif upper < 0 and row.get("status") == "CERTIFIED_NEGATIVE":
                bucket["negative"] += 1
            else:
                bucket["unresolved"] += 1
        if strict_positive != len(rows):
            all_high_strictly_positive = False

        determinants = {
            identifier: row_interval(row)
            for identifier, row in high_rows.items()
            if row.get("kind") == "deflated-cross-loewner-determinant"
        }
        if previous_determinants is not None:
            if set(determinants) != set(previous_determinants):
                raise ExhaustiveError("determinant row set changes across rungs")
            for identifier, current in determinants.items():
                if not current[1] < previous_determinants[identifier][0]:
                    determinant_descent = False
        previous_determinants = determinants

        tightest = min(high_rows.values(), key=lambda row: row_interval(row)[0])
        tight_lower, tight_upper = row_interval(tightest)
        interval_map = {
            identifier: high_rows[identifier]["interval"]
            for identifier in sorted(high_rows)
        }
        rungs.append(
            {
                "nearest_count": count,
                "selected_zero_indices_sha256": canonical_sha(sorted(selected)),
                "selection_guard": high_certificate["source"]["selection_guard"],
                "low_unresolved_rows": low_result["unresolved_rows"],
                "high_strictly_positive_rows": strict_positive,
                "high_negative_rows": high_result["certified_negative_rows"],
                "high_unresolved_rows": high_result["unresolved_rows"],
                "statuses_by_order": {
                    str(order): status
                    for order, status in sorted(statuses_by_order.items())
                },
                "all_high_intervals_nested": True,
                "high_row_intervals_sha256": canonical_sha(interval_map),
                "low_certificate_sha256": low_certificate["certificate_sha256"],
                "high_certificate_sha256": high_certificate["certificate_sha256"],
                "low_verification_sha256": low_result["verification_sha256"],
                "high_verification_sha256": high_result["verification_sha256"],
                "tightest_row": {
                    key: tightest[key]
                    for key in ("id", "kind", "rows", "columns", "order")
                    if key in tightest
                },
                "tightest_row_interval": tightest["interval"],
                "tightest_row_lower_scientific": outward_scientific(
                    tight_lower, upper=False
                ),
                "tightest_row_upper_scientific": outward_scientific(
                    tight_upper, upper=True
                ),
            }
        )

    determinant_count = sum(
        count for order, count in row_counts.items() if order > 1
    )
    expected_counts = {
        1: math.comb(len(point_ids), 2),
        **{
            order: (
                math.comb(len(point_ids), 2 * order)
                * math.comb(2 * order, order)
                // 2
            )
            for order in range(2, min(4, len(point_ids) // 2) + 1)
        },
    }
    if row_counts != expected_counts:
        raise ExhaustiveError("exhaustive row counts fail the closed formula")

    if all_high_strictly_positive:
        finite_status = "CERTIFIED_POSITIVE_EXHAUSTIVE_DISJOINT_PR71_GRID"
        counterexample_nomination = None
    elif any(rung["high_negative_rows"] for rung in rungs):
        finite_status = "NEGATIVE_EXHAUSTIVE_GRID_ROW_PENDING_REVIEW"
        counterexample_nomination = "PENDING_INDEPENDENT_REPRODUCTION"
    else:
        finite_status = "UNRESOLVED_EXHAUSTIVE_DISJOINT_PR71_GRID"
        counterexample_nomination = None

    result = {
        "schema": SUMMARY_SCHEMA,
        "target": zero_block.get("target"),
        "point_ids_in_increasing_u_order": list(point_ids),
        "point_count": len(point_ids),
        "low_precision_bits": low_precision,
        "high_precision_bits": high_precision,
        "zero_block_artifact_sha256": canonical_sha(zero_block),
        "zero_block_precision_bits": integer(
            zero_block.get("precision_bits"), "zero-block precision"
        ),
        "certified_zero_ball_count": len(zero_block.get("zeros", [])),
        "final_selected_zero_count": counts[-1],
        "selection_scope": BUILD.GLOBAL_NEAREST_SCOPE,
        "transpose_equivalent_determinants_deduplicated": True,
        "derivative_or_overlapping_minors_in_scope": False,
        "coverage_verified": True,
        "row_count_by_order": {
            str(order): count for order, count in sorted(row_counts.items())
        },
        "monotonicity_row_count": row_counts[1],
        "determinant_row_count": determinant_count,
        "row_count_per_rung": len(rows),
        "row_specification_sha256": canonical_sha(rows),
        "ladder_rungs": rungs,
        "closed_cell_count": len(rows) * len(rungs),
        "all_high_precision_rows_strictly_positive": all_high_strictly_positive,
        "all_determinant_intervals_strictly_descending": determinant_descent,
        "finite_table_status": finite_status,
        "counterexample_nomination": counterexample_nomination,
        "scope_warning": (
            "This exhausts only derivative-free disjoint cross-Loewner minors "
            "through order four on the fixed nine-node PR71 grid. It does not "
            "cover derivative/principal minors, other nodes or ordinates, and "
            "it is not a proof of RH. Independent backend reproduction and "
            "review of proposed L-9301 remain external."
        ),
    }
    result["summary_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low_primitive", type=Path)
    parser.add_argument("high_primitive", type=Path)
    parser.add_argument("zero_block", type=Path)
    parser.add_argument("--counts", type=int, nargs="+", default=list(COUNTS))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = summarize(
            load(args.low_primitive),
            load(args.high_primitive),
            load(args.zero_block),
            tuple(args.counts),
        )
        code = 0 if result["counterexample_nomination"] is None else 1
    except (
        OSError,
        json.JSONDecodeError,
        ExhaustiveError,
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
