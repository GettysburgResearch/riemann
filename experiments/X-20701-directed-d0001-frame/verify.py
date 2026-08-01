#!/usr/bin/env python3
"""Exact rational consumer for X-20701 directed D-0001 frame balls."""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

SCHEMA = "riemann.x20701.d0001-frame.balls.v1"
RESULT_SCHEMA = "riemann.x20701.d0001-frame.result.v1"


class VerificationError(RuntimeError):
    pass


def require_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise VerificationError(f"{name} must not be bool")
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise VerificationError(f"{name} must be an integer") from exc


def binary_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise VerificationError(f"{name} must be an object")
    mantissa = require_int(value.get("mantissa"), f"{name}.mantissa")
    exponent = require_int(value.get("exponent"), f"{name}.exponent")
    if exponent >= 0:
        return Fraction(mantissa << exponent)
    return Fraction(mantissa, 1 << (-exponent))


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise VerificationError(f"reversed interval [{self.lo},{self.hi}]")

    @classmethod
    def point(cls, value: int | Fraction) -> "Interval":
        q = Fraction(value)
        return cls(q, q)

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: "Interval") -> "Interval":
        return self + (-other)

    def __mul__(self, other: "Interval") -> "Interval":
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(products), max(products))

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise VerificationError(f"division by zero-containing interval {self}")
        return Interval(min(Fraction(1, 1) / self.lo, Fraction(1, 1) / self.hi),
                        max(Fraction(1, 1) / self.lo, Fraction(1, 1) / self.hi))

    def __truediv__(self, other: "Interval") -> "Interval":
        return self * other.reciprocal()

    def square(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            return Interval(Fraction(0), max(self.lo * self.lo, self.hi * self.hi))
        return Interval(min(self.lo * self.lo, self.hi * self.hi),
                        max(self.lo * self.lo, self.hi * self.hi))

    def overlaps(self, other: "Interval") -> bool:
        return max(self.lo, other.lo) <= min(self.hi, other.hi)

    def contains_interval(self, other: "Interval") -> bool:
        return self.lo <= other.lo and other.hi <= self.hi


def parse_interval(value: Any, name: str) -> Interval:
    if not isinstance(value, dict):
        raise VerificationError(f"{name} must be an interval object")
    return Interval(binary_fraction(value.get("lower"), f"{name}.lower"),
                    binary_fraction(value.get("upper"), f"{name}.upper"))


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def dot(row: Sequence[Interval], vector: Sequence[Interval]) -> Interval:
    if len(row) != len(vector):
        raise VerificationError("dot-product dimension mismatch")
    total = Interval.point(0)
    for left, right in zip(row, vector):
        total = total + left * right
    return total


def mat_quad(matrix: Sequence[Sequence[Interval]], left: Sequence[Interval], right: Sequence[Interval]) -> Interval:
    if len(matrix) != len(left) or any(len(row) != len(right) for row in matrix):
        raise VerificationError("matrix quadratic dimension mismatch")
    total = Interval.point(0)
    for i in range(len(left)):
        for j in range(len(right)):
            total = total + left[i] * matrix[i][j] * right[j]
    return total


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction, digits: int = 18) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    q, r = divmod(value.numerator, value.denominator)
    out = [str(q), "."]
    for _ in range(digits):
        r *= 10
        digit, r = divmod(r, value.denominator)
        out.append(str(digit))
    return sign + "".join(out)


def interval_result(value: Interval) -> dict[str, str]:
    return {
        "lower": fraction_text(value.lo),
        "upper": fraction_text(value.hi),
        "lower_decimal": decimal_text(value.lo),
        "upper_decimal": decimal_text(value.hi),
    }


def require_overlap(claimed_raw: Any, recomputed: Interval, name: str) -> None:
    claimed = parse_interval(claimed_raw, name)
    if not claimed.overlaps(recomputed):
        raise VerificationError(f"{name} does not overlap exact replay")


def replay_level(raw: dict[str, Any]) -> dict[str, object]:
    identifier = raw.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise VerificationError("level ID must be nonempty")
    if require_int(raw.get("N"), f"{identifier}.N") != 1:
        raise VerificationError("X-20701 currently accepts N=1 only")
    c = require_int(raw.get("c"), f"{identifier}.c")
    if c < 2:
        raise VerificationError("cutoff must be >=2")

    r_raw = raw.get("near_kernel_integer")
    if not isinstance(r_raw, list) or len(r_raw) != 2:
        raise VerificationError("near-kernel vector must have dimension two")
    r_int = [require_int(value, f"{identifier}.r") for value in r_raw]
    if r_int == [0, 0]:
        raise VerificationError("zero near-kernel vector")
    r = [Interval.point(value) for value in r_int]
    w = [Interval.point(-r_int[1]), Interval.point(r_int[0])]

    matrix_raw = raw.get("matrix_even")
    if not isinstance(matrix_raw, list) or len(matrix_raw) != 2 or any(not isinstance(row, list) or len(row) != 2 for row in matrix_raw):
        raise VerificationError("matrix_even must be 2x2")
    matrix = [[parse_interval(matrix_raw[i][j], f"{identifier}.A[{i},{j}]") for j in range(2)] for i in range(2)]
    if not matrix[0][1].overlaps(matrix[1][0]):
        raise VerificationError("matrix symmetry intervals are disjoint")

    z_raw = raw.get("first_zero_row")
    y_raw = raw.get("second_zero_row")
    if not isinstance(z_raw, list) or not isinstance(y_raw, list) or len(z_raw) != 2 or len(y_raw) != 2:
        raise VerificationError("zero rows must have dimension two")
    z = [parse_interval(value, f"{identifier}.zrow") for value in z_raw]
    y = [parse_interval(value, f"{identifier}.yrow") for value in y_raw]

    zr = dot(z, r)
    zw = dot(z, w)
    if zw.lo <= 0 <= zw.hi:
        raise VerificationError("first-frame denominator touches zero")
    alpha = -zr / zw
    k = [r[i] + alpha * w[i] for i in range(2)]
    graph_metric = dot(k, k)
    if graph_metric.lo <= 0:
        raise VerificationError("graph metric is not strictly positive")

    conditional = dot(y, k)
    selected = conditional.square()
    selected_ratio = selected / graph_metric
    if selected_ratio.lo <= 0:
        raise VerificationError("conditional second frame has no strict floor")

    complement = mat_quad(matrix, w, w)
    if complement.lo <= 0:
        raise VerificationError("positive-sector block is not strictly positive")
    cross = mat_quad(matrix, w, k)
    kernel_raw = mat_quad(matrix, k, k)
    schur = kernel_raw - cross.square() / complement
    schur_ratio = schur / graph_metric
    residual = schur - selected
    residual_ratio = residual / graph_metric
    nu_upper = max(Fraction(0), -residual_ratio.lo)
    margin_lower = selected_ratio.lo - nu_upper
    if margin_lower <= 0:
        raise VerificationError(f"{identifier}: conditional-frame margin did not separate zero")
    if schur_ratio.lo <= 0:
        raise VerificationError(f"{identifier}: full Schur ratio did not separate zero")

    t = cross / complement
    lambda_trace = Interval.point(2) + alpha.square() + (t - alpha).square()
    lambda_upper = lambda_trace.hi
    if lambda_upper < 1:
        raise VerificationError("invalid triangular metric endpoint")

    diagnostics = raw.get("derived_diagnostics")
    if not isinstance(diagnostics, dict):
        raise VerificationError("missing producer diagnostics")
    for key, value in (
        ("alpha", alpha),
        ("conditional_evaluation", conditional),
        ("graph_metric", graph_metric),
        ("selected_frame_ratio", selected_ratio),
        ("positive_sector_block", complement),
        ("raw_kernel", kernel_raw),
        ("cross", cross),
        ("schur", schur),
        ("schur_ratio", schur_ratio),
        ("joint_corrected_residual_ratio", residual_ratio),
    ):
        require_overlap(diagnostics.get(key), value, f"{identifier}.{key}")

    # Every retained level is strictly positive, so the Issue #207 cofinal term
    # Lambda * (nu-sigma^2)_+ is exactly zero at the certified level.
    cofinal_term = Fraction(0)
    return {
        "id": identifier,
        "c": c,
        "first_zero_index": require_int(raw.get("first_zero_index"), "first_zero_index"),
        "second_zero_index": require_int(raw.get("second_zero_index"), "second_zero_index"),
        "first_frame_denominator": interval_result(zw),
        "graph_metric": interval_result(graph_metric),
        "selected_frame_ratio": interval_result(selected_ratio),
        "joint_corrected_residual_ratio": interval_result(residual_ratio),
        "joint_negative_endpoint_upper": fraction_text(nu_upper),
        "conditional_margin_lower": fraction_text(margin_lower),
        "conditional_margin_lower_decimal": decimal_text(margin_lower),
        "full_schur_ratio": interval_result(schur_ratio),
        "triangular_metric_inflation_upper": fraction_text(lambda_upper),
        "issue_207_term_upper": fraction_text(cofinal_term),
        "assembly_radius": "0",
        "verdict": "CERTIFIED_POSITIVE_ACTUAL_D0001_CONDITIONAL_FRAME_LEVEL",
    }


def verify_certificate(value: dict[str, Any]) -> dict[str, object]:
    if value.get("schema") != SCHEMA:
        raise VerificationError("unexpected certificate schema")
    expected_digest = value.get("certificate_sha256")
    if not isinstance(expected_digest, str):
        raise VerificationError("missing certificate digest")
    without = dict(value)
    without.pop("certificate_sha256", None)
    if canonical_digest(without) != expected_digest:
        raise VerificationError("certificate digest mismatch")

    census = value.get("zero_census")
    if not isinstance(census, dict) or require_int(census.get("N_25"), "N_25") != 2:
        raise VerificationError("the first-two-zero census gate is missing")
    zeros = census.get("zeros")
    if not isinstance(zeros, list) or len(zeros) < 2:
        raise VerificationError("at least two zero balls are required")
    intervals = [parse_interval(item.get("gamma"), f"zero[{i}].gamma") for i, item in enumerate(zeros)]
    if not intervals[0].hi < intervals[1].lo:
        raise VerificationError("selected zero intervals are not disjoint and ordered")

    levels_raw = value.get("levels")
    if not isinstance(levels_raw, list) or not levels_raw:
        raise VerificationError("certificate has no levels")
    results = [replay_level(level) for level in levels_raw]
    cutoffs = [require_int(item["c"], "result.c") for item in results]
    if cutoffs != sorted(set(cutoffs)):
        raise VerificationError("cutoff ladder must be strictly increasing")

    result: dict[str, object] = {
        "schema": RESULT_SCHEMA,
        "certificate_sha256": expected_digest,
        "precision_bits": require_int(value.get("producer", {}).get("precision_bits"), "precision_bits"),
        "level_count": len(results),
        "cutoff_min": cutoffs[0],
        "cutoff_max": cutoffs[-1],
        "all_levels_certified_positive": True,
        "all_issue_207_terms_zero": True,
        "levels": results,
        "classification": "DIRECTED_ACTUAL_ZETA_DATA_FINITE_LADDER",
        "scope": (
            "These are actual cutoff-free D-0001 finite Weil blocks with actual "
            "critical-line zero frames. They are not yet the complete augmented "
            "Suzuki low packets required for the global T-14302 implication."
        ),
    }
    result["verification_sha256"] = canonical_digest(result)
    return result


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationError("JSON root must be an object")
    return value


def primitive_intervals(level: dict[str, Any]) -> Iterable[tuple[str, Interval]]:
    identifier = str(level.get("id"))
    for name in ("first_zero_row", "second_zero_row"):
        raw = level.get(name)
        if not isinstance(raw, list):
            raise VerificationError(f"{identifier}.{name} missing")
        for i, value in enumerate(raw):
            yield f"{identifier}.{name}[{i}]", parse_interval(value, f"{identifier}.{name}[{i}]")
    raw_matrix = level.get("matrix_even")
    if not isinstance(raw_matrix, list):
        raise VerificationError(f"{identifier}.matrix_even missing")
    for i, row in enumerate(raw_matrix):
        for j, value in enumerate(row):
            yield f"{identifier}.matrix[{i},{j}]", parse_interval(value, f"{identifier}.matrix[{i},{j}]")


def compare_certificates(low: dict[str, Any], high: dict[str, Any]) -> dict[str, object]:
    if low.get("schema") != SCHEMA or high.get("schema") != SCHEMA:
        raise VerificationError("comparison schema mismatch")
    low_levels = low.get("levels")
    high_levels = high.get("levels")
    if not isinstance(low_levels, list) or not isinstance(high_levels, list) or len(low_levels) != len(high_levels):
        raise VerificationError("precision ladders have different level counts")
    checked = 0
    for lo_level, hi_level in zip(low_levels, high_levels):
        if lo_level.get("id") != hi_level.get("id") or lo_level.get("near_kernel_integer") != hi_level.get("near_kernel_integer"):
            raise VerificationError("level identity or frozen vector drift")
        lo_items = list(primitive_intervals(lo_level))
        hi_items = list(primitive_intervals(hi_level))
        if [name for name, _ in lo_items] != [name for name, _ in hi_items]:
            raise VerificationError("primitive manifest drift")
        for (name, lo_interval), (_, hi_interval) in zip(lo_items, hi_items):
            if not lo_interval.contains_interval(hi_interval):
                raise VerificationError(f"higher-precision interval widened at {name}")
            checked += 1
    return {
        "schema": "riemann.x20701.d0001-frame.precision-comparison.v1",
        "low_precision_bits": require_int(low.get("producer", {}).get("precision_bits"), "low precision"),
        "high_precision_bits": require_int(high.get("producer", {}).get("precision_bits"), "high precision"),
        "level_count": len(low_levels),
        "primitive_intervals_checked": checked,
        "verdict": "HIGH_PRECISION_PRIMITIVES_CONTAINED_IN_LOW_PRECISION_PRIMITIVES",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path, nargs="?")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", nargs=2, metavar=("LOW", "HIGH"), type=Path)
    args = parser.parse_args()
    if args.compare:
        result = compare_certificates(load(args.compare[0]), load(args.compare[1]))
    else:
        if args.certificate is None:
            parser.error("certificate is required unless --compare is used")
        result = verify_certificate(load(args.certificate))
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
