#!/usr/bin/env python3
"""Validate and summarize the source-bound PR71 nearest-zero ladder."""
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

COUNTS = (2, 4, 8, 16, 32, 64, 96, 128)
SUMMARY_SCHEMA = "riemann.x9301-pr71-production-summary.v4"
BLOCK_SCHEMA = "riemann.x9301-pr71-hardy-zero-block.v1"
GLOBAL_NEAREST_SCOPE = "CERTIFIED_GLOBAL_NEAREST_CRITICAL_LINE_ZEROS"


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
            return int(value, 10)
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


def row_interval(row: dict[str, Any]) -> tuple[Fraction, Fraction]:
    raw = row.get("interval")
    if not isinstance(raw, dict):
        raise SummaryError("row interval must be an object")
    lower = rational(raw.get("lower"), "row.interval.lower")
    upper = rational(raw.get("upper"), "row.interval.upper")
    if lower > upper:
        raise SummaryError("row interval is reversed")
    return lower, upper


def outward_scientific(value: Fraction, *, upper: bool) -> str:
    with localcontext() as context:
        context.prec = 18
        context.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        decimal = Decimal(value.numerator) / Decimal(value.denominator)
        return format(decimal, ".17E").lower()


def validate_certificate_digest(certificate: dict[str, Any]) -> str:
    claimed = certificate.get("certificate_sha256")
    if not isinstance(claimed, str):
        raise SummaryError("certificate lacks certificate_sha256")
    body = dict(certificate)
    body.pop("certificate_sha256")
    if canonical_sha(body) != claimed:
        raise SummaryError("certificate_sha256 mismatch")
    return claimed


def row_map(verification: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = verification.get("rows")
    if not isinstance(raw, list) or not raw:
        raise SummaryError("verification rows must be nonempty")
    result: dict[str, dict[str, Any]] = {}
    for row in raw:
        if (
            not isinstance(row, dict)
            or not isinstance(row.get("id"), str)
            or row["id"] in result
        ):
            raise SummaryError("malformed or duplicate verification row")
        result[row["id"]] = row
    return result


def summarize(
    root: Path,
    zero_block: dict[str, Any],
    low_precision: int,
    high_precision: int,
    counts: tuple[int, ...] = COUNTS,
) -> dict[str, Any]:
    if not counts or any(
        count <= 0 or (index and count <= counts[index - 1])
        for index, count in enumerate(counts)
    ):
        raise SummaryError("nearest-zero counts must be positive and increasing")
    if (
        zero_block.get("schema") != BLOCK_SCHEMA
        or zero_block.get("classification")
        != "CERTIFIED_CRITICAL_LINE_ZERO_BLOCK"
    ):
        raise SummaryError("zero block is not proof-classified")
    zero_block_sha = canonical_sha(zero_block)
    raw_zeros = zero_block.get("zeros")
    if not isinstance(raw_zeros, list) or not raw_zeros:
        raise SummaryError("zero block must contain zeros")
    all_zero_indices = {
        integer(item.get("zero_index"), "zero_index")
        for item in raw_zeros
        if isinstance(item, dict)
    }
    if len(all_zero_indices) != len(raw_zeros):
        raise SummaryError("zero block has malformed or duplicate indices")

    rungs: list[dict[str, Any]] = []
    previous_selected: set[int] = set()
    previous_determinants: dict[str, tuple[Fraction, Fraction]] | None = None
    row_ids: set[str] | None = None
    all_strictly_positive = True
    all_determinants_descend = True

    for count in counts:
        low_certificate = load(
            root / f"nearest-{count}-certificate-p{low_precision}.json"
        )
        high_certificate = load(
            root / f"nearest-{count}-certificate-p{high_precision}.json"
        )
        low_verification = load(
            root / f"nearest-{count}-verification-p{low_precision}.json"
        )
        high_verification = load(
            root / f"nearest-{count}-verification-p{high_precision}.json"
        )
        comparison = load(
            root
            / (
                f"nearest-{count}-precision-comparison-"
                f"p{low_precision}-p{high_precision}.json"
            )
        )

        low_certificate_sha = validate_certificate_digest(low_certificate)
        high_certificate_sha = validate_certificate_digest(high_certificate)
        for certificate in (low_certificate, high_certificate):
            source = certificate.get("source")
            if (
                not isinstance(source, dict)
                or source.get("zero_block_sha256") != zero_block_sha
                or source.get("nearest_count") != count
                or source.get("selection_scope") != GLOBAL_NEAREST_SCOPE
            ):
                raise SummaryError(f"rung {count} has inconsistent source metadata")

        for verification, certificate_sha in (
            (low_verification, low_certificate_sha),
            (high_verification, high_certificate_sha),
        ):
            if (
                verification.get("source_artifacts_verified") is not True
                or verification.get("certificate_sha256") != certificate_sha
                or verification.get("certified_negative_rows") != 0
            ):
                raise SummaryError(f"rung {count} failed source-bound verification")

        if (
            comparison.get("all_high_intervals_nested") is not True
            or comparison.get("low_artifact_sha256")
            != canonical_sha(low_certificate)
            or comparison.get("high_artifact_sha256")
            != canonical_sha(high_certificate)
        ):
            raise SummaryError(f"rung {count} failed precision nesting")

        selected_raw = high_certificate["source"].get("selected_zero_indices")
        if (
            not isinstance(selected_raw, list)
            or len(selected_raw) != count
            or any(isinstance(value, bool) or not isinstance(value, int) for value in selected_raw)
        ):
            raise SummaryError(f"rung {count} has malformed selected-zero indices")
        selected = set(selected_raw)
        if (
            len(selected) != count
            or not selected <= all_zero_indices
            or not previous_selected < selected
        ):
            raise SummaryError("nearest-zero selected sets are not strictly cumulative")
        previous_selected = selected

        rows = row_map(high_verification)
        if row_ids is None:
            row_ids = set(rows)
        elif set(rows) != row_ids:
            raise SummaryError("row set changes across ladder")
        strict_rows = 0
        for row in rows.values():
            lower, _ = row_interval(row)
            if lower > 0 and row.get("status") == "CERTIFIED_NONNEGATIVE":
                strict_rows += 1
            else:
                all_strictly_positive = False

        determinants = {
            identifier: row_interval(row)
            for identifier, row in rows.items()
            if row.get("kind") == "deflated-cross-loewner-determinant"
        }
        if previous_determinants is not None:
            if set(determinants) != set(previous_determinants):
                raise SummaryError("determinant row set changes across ladder")
            for identifier, current in determinants.items():
                if not current[1] < previous_determinants[identifier][0]:
                    all_determinants_descend = False
        previous_determinants = determinants

        tightest = min(rows.values(), key=lambda row: row_interval(row)[0])
        tight_lower, tight_upper = row_interval(tightest)
        rungs.append(
            {
                "nearest_count": count,
                "selected_zero_count": len(selected),
                "low_precision_bits": low_precision,
                "low_unresolved_rows": low_verification.get("unresolved_rows"),
                "high_precision_bits": high_precision,
                "high_verdict": high_verification.get("verdict"),
                "high_strictly_positive_rows": strict_rows,
                "high_unresolved_rows": high_verification.get("unresolved_rows"),
                "tightest_row_id": tightest["id"],
                "tightest_row_interval": tightest["interval"],
                "tightest_row_interval_sha256": canonical_sha(tightest["interval"]),
                "tightest_row_lower_scientific": outward_scientific(
                    tight_lower, upper=False
                ),
                "tightest_row_upper_scientific": outward_scientific(
                    tight_upper, upper=True
                ),
                "high_certificate_artifact_sha256": canonical_sha(high_certificate),
                "high_verification_artifact_sha256": canonical_sha(high_verification),
            }
        )

    if len(previous_selected) != counts[-1]:
        raise SummaryError("final rung does not use the requested nearest prefix")
    if not all_strictly_positive:
        raise SummaryError("at least one high-precision row is not strictly positive")
    if not all_determinants_descend:
        raise SummaryError("determinant ladder is not rigorously strictly descending")
    assert row_ids is not None
    result = {
        "schema": SUMMARY_SCHEMA,
        "target": zero_block.get("target"),
        "zero_block_artifact_sha256": zero_block_sha,
        "zero_block_precision_bits": integer(
            zero_block.get("precision_bits"), "zero_block.precision_bits"
        ),
        "certified_zero_ball_count": len(all_zero_indices),
        "low_precision_bits": low_precision,
        "high_precision_bits": high_precision,
        "declared_row_count": len(row_ids),
        "ladder_rungs": rungs,
        "closed_cell_count": len(row_ids) * len(rungs),
        "selection_scope": GLOBAL_NEAREST_SCOPE,
        "final_selected_zero_count": len(previous_selected),
        "guard_zero_ball_count": len(all_zero_indices) - len(previous_selected),
        "all_high_precision_rows_strictly_positive": True,
        "all_determinant_intervals_strictly_descending": True,
        "final_rung_uses_requested_nearest_prefix": True,
        "finite_table_status": "CERTIFIED_POSITIVE_FIXED_PR71_TABLE",
        "counterexample_nomination": None,
        "scope_warning": (
            f"This closes only the declared ordinate, nine-point grid, "
            f"{len(row_ids)} rows, and {len(rungs)} cumulative globally-nearest "
            "zero rungs. It is not a proof of RH. "
            "Independent backend reproduction and review of L-9301 remain external."
        ),
    }
    result["summary_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--zero-block", type=Path, required=True)
    parser.add_argument("--low-precision", type=int, default=384)
    parser.add_argument("--high-precision", type=int, default=512)
    parser.add_argument("--counts", type=int, nargs="+", default=list(COUNTS))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = summarize(
            args.root,
            load(args.zero_block),
            args.low_precision,
            args.high_precision,
            tuple(args.counts),
        )
        code = 0
    except (OSError, json.JSONDecodeError, SummaryError, KeyError) as exc:
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
