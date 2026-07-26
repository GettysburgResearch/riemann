#!/usr/bin/env python3
"""Compactly audit and summarize the retained PR71-neighborhood screens."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SCHEMA = "riemann.x9301-pr71-ordinate-screen-summary.v1"
DENSE_SCHEMA = "riemann.x9301-dense-order2-screen.v1"
RANKING_SCHEMA = "riemann.x9301-dense-high-order-midpoint-ranking.v3"

DENSE_TARGETS = (
    ("upper-mirror-jp15", "upper PR71-gap mirror", 20225875608345134672275),
    ("positive-control-jm5", "validated positive near-null control", 20225875608342450317715),
    ("directed-jp12", "directed main-gap near-null", 20225875608344732019091),
    ("distinct-gap-jm26", "distinct-gap edge", 20225875608339631745427),
    ("max-mass-jm25", "maximum local line-zero mass", 20225875608339765963155),
    ("near-zero-jm16", "near-zero deflation stress target", 20225875608340973922707),
    ("directed-jm29", "directed second-gap alternative", 20225875608339229092243),
)

BROAD_TARGETS = (
    ("pr71-baseline", "PR71 baseline", 20225875608341108140435),
    ("upper-mirror-jp15", "upper PR71-gap mirror", 20225875608345134672275),
    ("distinct-gap-jm26", "distinct-gap edge", 20225875608339631745427),
    ("max-mass-jm25", "maximum local line-zero mass", 20225875608339765963155),
)


class SummaryError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SummaryError(f"{path} must contain an object")
    return value


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise SummaryError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise SummaryError(f"{name} must be integer text") from exc
    raise SummaryError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise SummaryError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise SummaryError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def outward_scientific(value: Fraction, *, upper: bool) -> str:
    with localcontext() as context:
        context.prec = 18
        context.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        decimal = Decimal(value.numerator) / Decimal(value.denominator)
        return format(decimal, ".17E").lower()


def parse_directed_summary(
    summary: dict[str, Any],
    expected_numerator: int,
    expected_points: int,
    expected_rows: int,
) -> dict[str, Any]:
    target = summary.get("target")
    if (
        summary.get("schema") != DENSE_SCHEMA
        or summary.get("all_high_intervals_nested") is not True
        or summary.get("counterexample_nomination") is not None
        or integer(summary.get("point_count"), "point_count") != expected_points
        or integer(summary.get("order2_row_count"), "order2_row_count") != expected_rows
        or integer(target.get("numerator") if isinstance(target, dict) else None, "target numerator")
        != expected_numerator
        or integer(target.get("denominator") if isinstance(target, dict) else None, "target denominator")
        != 1 << 32
    ):
        raise SummaryError("directed order-two summary contract mismatch")
    counts = summary.get("status_counts")
    if not isinstance(counts, dict) or (
        integer(counts.get("CERTIFIED_NEGATIVE"), "negative count") != 0
        or integer(counts.get("UNRESOLVED"), "unresolved count") != 0
        or integer(counts.get("CERTIFIED_NONNEGATIVE"), "positive count")
        != expected_rows
    ):
        raise SummaryError("directed order-two status counts mismatch")
    top = summary.get("top_geometry_adjusted_rows")
    if not isinstance(top, list) or not top or not isinstance(top[0], dict):
        raise SummaryError("directed order-two ranking is missing")
    return {
        "target": target,
        "point_count": expected_points,
        "row_count": expected_rows,
        "tightest_geometry_row": top[0],
        "summary_artifact_sha256": canonical_sha(summary),
    }


def parse_ranking(
    ranking: dict[str, Any],
    expected_numerator: int,
    expected_precision: int,
) -> dict[str, Any]:
    target = ranking.get("target")
    if (
        ranking.get("schema") != RANKING_SCHEMA
        or integer(ranking.get("precision_bits"), "ranking precision") != expected_precision
        or integer(target.get("numerator") if isinstance(target, dict) else None, "ranking target numerator")
        != expected_numerator
        or integer(target.get("denominator") if isinstance(target, dict) else None, "ranking target denominator")
        != 1 << 32
        or ranking.get("counterexample_nomination") is not None
        or integer(ranking.get("robust_negative_midpoint_count"), "robust negatives") != 0
    ):
        raise SummaryError("high-order ranking contract mismatch")
    raw_orders = ranking.get("orders")
    if not isinstance(raw_orders, list):
        raise SummaryError("high-order ranking orders must be a list")
    orders = {
        integer(item.get("order"), "ranking order"): item
        for item in raw_orders
        if isinstance(item, dict)
    }
    if set(orders) != {3, 4}:
        raise SummaryError("high-order ranking must contain orders three and four")
    if (
        integer(orders[3].get("pattern_count"), "order-three count") != 17160
        or integer(orders[4].get("pattern_count"), "order-four count") != 45045
        or integer(orders[3].get("negative_beyond_input_uncertainty_count"), "order-three robust count") != 0
        or integer(orders[4].get("negative_beyond_input_uncertainty_count"), "order-four robust count") != 0
    ):
        raise SummaryError("high-order coverage or robust count mismatch")
    return {
        "precision_bits": expected_precision,
        "pattern_count": 62205,
        "order3_negative_midpoint_count": integer(
            orders[3].get("negative_midpoint_count"), "order-three negative midpoint count"
        ),
        "order4_negative_midpoint_count": integer(
            orders[4].get("negative_midpoint_count"), "order-four negative midpoint count"
        ),
        "negative_beyond_input_uncertainty_count": 0,
        "ranking_artifact_sha256": canonical_sha(ranking),
    }


def parse_replay(
    low: dict[str, Any],
    high: dict[str, Any],
    comparison: dict[str, Any],
    expected_low_status: str,
) -> dict[str, Any]:
    for name, verification in (("low", low), ("high", high)):
        rows = verification.get("rows")
        if (
            verification.get("source_artifacts_verified") is not True
            or integer(verification.get("certified_negative_rows"), f"{name} negatives") != 0
            or not isinstance(rows, list)
            or len(rows) != 1
            or not isinstance(rows[0], dict)
        ):
            raise SummaryError(f"{name} candidate verification contract mismatch")
    low_row = low["rows"][0]
    high_row = high["rows"][0]
    if (
        low_row.get("id") != high_row.get("id")
        or low_row.get("status") != expected_low_status
        or high_row.get("status") != "CERTIFIED_NONNEGATIVE"
        or comparison.get("all_high_intervals_nested") is not True
        or integer(comparison.get("nested_row_intervals"), "nested rows") != 1
    ):
        raise SummaryError("candidate replay status or nesting mismatch")
    raw_interval = high_row.get("interval")
    if not isinstance(raw_interval, dict):
        raise SummaryError("high candidate interval is missing")
    lower = rational(raw_interval.get("lower"), "candidate lower")
    upper = rational(raw_interval.get("upper"), "candidate upper")
    if lower <= 0 or lower > upper:
        raise SummaryError("high candidate interval must be strictly positive")
    return {
        "row_id": high_row["id"],
        "low_status": low_row["status"],
        "high_status": high_row["status"],
        "high_lower_scientific": outward_scientific(lower, upper=False),
        "high_upper_scientific": outward_scientific(upper, upper=True),
        "all_high_intervals_nested": True,
        "low_verification_sha256": canonical_sha(low),
        "high_verification_sha256": canonical_sha(high),
        "comparison_sha256": canonical_sha(comparison),
    }


def summarize(root: Path) -> dict[str, Any]:
    dense_root = root / "results" / "pr71-ordinate-screen"
    broad_root = root / "results" / "pr71-ordinate-screen-broad"

    dense_entries = []
    for slug, label, numerator in DENSE_TARGETS:
        parsed = parse_directed_summary(
            load(dense_root / slug / "summary.json"), numerator, 16, 5460
        )
        parsed.update({"slug": slug, "label": label})
        dense_entries.append(parsed)

    broad_entries = []
    p256_entries = []
    p512_entries = []
    for slug, label, numerator in BROAD_TARGETS:
        parsed = parse_directed_summary(
            load(broad_root / slug / "summary.json"), numerator, 20, 14535
        )
        parsed.update({"slug": slug, "label": label})
        broad_entries.append(parsed)
        low_rank = parse_ranking(
            load(broad_root / slug / "sparse-broad-order3-4-midpoint-d160.json"),
            numerator,
            256,
        )
        low_rank.update({"slug": slug, "label": label})
        p256_entries.append(low_rank)
        high_rank = parse_ranking(
            load(
                broad_root
                / slug
                / "sparse-broad-p512"
                / "order3-4-midpoint-d200.json"
            ),
            numerator,
            512,
        )
        high_rank.update({"slug": slug, "label": label})
        p512_entries.append(high_rank)

    baseline = broad_root / "pr71-baseline"
    order3_replay = parse_replay(
        load(baseline / "order3-candidate" / "verification-p384.json"),
        load(baseline / "order3-candidate" / "verification-p512.json"),
        load(
            baseline
            / "order3-candidate"
            / "precision-comparison-p384-p512.json"
        ),
        "CERTIFIED_NONNEGATIVE",
    )
    order4_replay = parse_replay(
        load(baseline / "order4-candidate" / "verification-p384.json"),
        load(baseline / "order4-candidate" / "verification-p512.json"),
        load(
            baseline
            / "order4-candidate"
            / "precision-comparison-p384-p512.json"
        ),
        "UNRESOLVED",
    )

    result = {
        "schema": SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED_AND_EXPLORATORY_MIDPOINT",
        "nearest_count": 256,
        "selection_scope": "CERTIFIED_GLOBAL_NEAREST_CRITICAL_LINE_ZEROS",
        "dense_16_node_order2": {
            "targets": dense_entries,
            "target_count": len(dense_entries),
            "directed_row_count": sum(item["row_count"] for item in dense_entries),
            "negative_rows": 0,
            "unresolved_rows": 0,
        },
        "broad_20_node_order2": {
            "targets": broad_entries,
            "target_count": len(broad_entries),
            "directed_row_count": sum(item["row_count"] for item in broad_entries),
            "negative_rows": 0,
            "unresolved_rows": 0,
        },
        "sparse_broad_high_order": {
            "p256_rankings": p256_entries,
            "p512_rankings": p512_entries,
            "p512_pattern_count": sum(item["pattern_count"] for item in p512_entries),
            "p512_negative_midpoints": 0,
            "p512_robust_negatives": 0,
        },
        "directed_candidate_replays": {
            "dense_order3": order3_replay,
            "broad_order4": order4_replay,
        },
        "counterexample_nomination": None,
        "verdict": "NO_NEGATIVE_IN_RETAINED_PR71_NEIGHBORHOOD_SCREENS",
        "proof_boundary": (
            "The order-two signs and two sparse candidate replays are exact "
            "source-bound interval results. High-order table rankings are "
            "midpoint screens with conservative input-uncertainty bounds, not "
            "proofs of all high-order signs."
        ),
    }
    result["summary_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = summarize(args.root)
        code = 0
    except (OSError, json.JSONDecodeError, SummaryError, KeyError) as exc:
        result = {"schema": SCHEMA, "verified": False, "error": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
