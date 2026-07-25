#!/usr/bin/env python3
"""Exact checker for certified-zero-deflated direct-xi modulus witnesses.

The checker evaluates no special function and uses no floating-point arithmetic.
It consumes exact rational rectangles for completed-xi values, exact rational
ordinates/nodes, and externally certified lower counts for pairwise-disjoint
critical-line zero bins.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import string
import sys
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
PRODUCTION_GATE = "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"
SYNTHETIC_GATE = "SYNTHETIC_CRITICAL_LINE_ZERO_COUNT"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, scalar: Fraction) -> "Interval":
        a, b = self.lower * scalar, self.upper * scalar
        return Interval(min(a, b), max(a, b))

    def mul(self, other: "Interval") -> "Interval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(values), max(values))

    def pow_nonnegative(self, exponent: int) -> "Interval":
        if exponent < 0:
            raise CertificateError("negative interval exponent")
        if self.lower < 0:
            raise CertificateError("pow_nonnegative requires a nonnegative interval")
        return Interval(self.lower**exponent, self.upper**exponent)


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        rational(raw.get("lower"), f"{name}.lower"),
        rational(raw.get("upper"), f"{name}.upper"),
    )


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_sha256(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(ch not in string.hexdigits for ch in value)
    ):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def square_interval(value: Interval) -> Interval:
    upper = max(value.lower * value.lower, value.upper * value.upper)
    if value.lower <= 0 <= value.upper:
        lower = Fraction(0)
    else:
        lower = min(value.lower * value.lower, value.upper * value.upper)
    return Interval(lower, upper)


def modulus_squared(real: Interval, imag: Interval) -> Interval:
    return square_interval(real).add(square_interval(imag))


def _atanh_log_interval(y: Fraction, terms: int) -> Interval:
    """Enclose log(y) for 1 <= y <= 2 by a positive atanh series."""
    if not (Fraction(1) <= y <= Fraction(2)):
        raise CertificateError("internal logarithm range-reduction failure")
    if terms < 8:
        raise CertificateError("logarithm term count must be at least 8")
    z = (y - 1) / (y + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lower, lower + tail)


def log_positive_fraction(value: Fraction, terms: int) -> Interval:
    """Return a rigorous rational enclosure of log(value), value > 0."""
    if value <= 0:
        raise CertificateError("logarithm input must be positive")

    numerator, denominator = value.numerator, value.denominator
    exponent = numerator.bit_length() - denominator.bit_length()

    def power_of_two(k: int) -> Fraction:
        if k >= 0:
            return Fraction(1 << k, 1)
        return Fraction(1, 1 << (-k))

    reduced = value / power_of_two(exponent)
    while reduced < 1:
        exponent -= 1
        reduced *= 2
    while reduced >= 2:
        exponent += 1
        reduced /= 2

    reduced_log = _atanh_log_interval(reduced, terms)
    log_two = _atanh_log_interval(Fraction(2), terms)
    return reduced_log.add(log_two.scale(Fraction(exponent)))


def log_positive_interval(value: Interval, terms: int) -> Interval:
    if value.lower <= 0:
        raise CertificateError("modulus-square interval must have positive lower endpoint")
    lower = log_positive_fraction(value.lower, terms).lower
    upper = log_positive_fraction(value.upper, terms).upper
    return Interval(lower, upper)


def determinant_interval(matrix: list[list[Interval]]) -> Interval:
    size = len(matrix)
    if size < 1 or any(len(row) != size for row in matrix):
        raise CertificateError("determinant matrix must be nonempty and square")
    result = Interval(Fraction(0), Fraction(0))
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            1
            for i in range(size)
            for j in range(i + 1, size)
            if permutation[i] > permutation[j]
        )
        term = Interval(Fraction(1), Fraction(1))
        for row, column in enumerate(permutation):
            term = term.mul(matrix[row][column])
        result = result.add(term.scale(Fraction(-1 if inversions % 2 else 1)))
    return result


def row_status(value: Interval) -> str:
    if value.upper < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lower >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def parse_points(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw_points = data.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise CertificateError("points must be a nonempty list")
    points: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"points[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in points:
            raise CertificateError(f"invalid or duplicate point id at points[{index}]")
        u = rational(raw.get("u"), f"points[{index}].u")
        if u <= 0:
            raise CertificateError("all squared horizontal nodes must be positive")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise CertificateError(f"points[{index}].xi_rectangle must be an object")
        real = interval(rectangle.get("real"), f"points[{index}].xi_rectangle.real")
        imag = interval(rectangle.get("imag"), f"points[{index}].xi_rectangle.imag")
        h = modulus_squared(real, imag)
        canonical = {
            "id": identifier,
            "u": fj(u),
            "xi_rectangle": {"real": ij(real), "imag": ij(imag)},
        }
        digest = canonical_sha(canonical)
        declared = raw.get("point_sha256")
        if declared is not None and validate_sha256(declared, "point_sha256") != digest:
            raise CertificateError(f"point digest mismatch for {identifier}")
        points[identifier] = {
            "u": u,
            "real": real,
            "imag": imag,
            "h": h,
            "sha256": digest,
        }
    return points


def parse_zero_bins(
    data: dict[str, Any], ordinate: Fraction, classification: str
) -> list[dict[str, Any]]:
    raw_bins = data.get("zero_bins")
    if not isinstance(raw_bins, list) or not raw_bins:
        raise CertificateError("zero_bins must be a nonempty list")

    bins: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_bins):
        if not isinstance(raw, dict):
            raise CertificateError(f"zero_bins[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier:
            raise CertificateError("zero-bin id must be a nonempty string")
        lower = rational(raw.get("lower_ordinate"), f"zero_bins[{index}].lower_ordinate")
        upper = rational(raw.get("upper_ordinate"), f"zero_bins[{index}].upper_ordinate")
        if lower > upper:
            raise CertificateError("zero-bin endpoints are reversed")
        count = exact_int(raw.get("count_lower"), f"zero_bins[{index}].count_lower")
        if count <= 0:
            raise CertificateError("zero-bin lower count must be positive")
        gate = raw.get("gate")
        if not isinstance(gate, dict):
            raise CertificateError("zero-bin gate must be an object")
        expected_status = (
            SYNTHETIC_GATE if classification == "SYNTHETIC_MODEL" else PRODUCTION_GATE
        )
        if gate.get("status") != expected_status:
            raise CertificateError(
                f"zero-bin gate status must equal {expected_status!r}"
            )
        gate_sha = validate_sha256(gate.get("sha256"), "zero-bin gate sha256")
        distance_lower = ordinate - lower
        distance_upper = ordinate - upper
        b_value = max(distance_lower * distance_lower, distance_upper * distance_upper)
        bins.append(
            {
                "id": identifier,
                "lower": lower,
                "upper": upper,
                "count": count,
                "B": b_value,
                "gate_sha256": gate_sha,
            }
        )

    bins.sort(key=lambda item: (item["lower"], item["upper"], item["id"]))
    if len({item["id"] for item in bins}) != len(bins):
        raise CertificateError("duplicate zero-bin id")
    for left, right in zip(bins, bins[1:]):
        if left["upper"] >= right["lower"]:
            raise CertificateError("zero bins overlap or touch")
    return bins


def raw_log_value(point: dict[str, Any], terms: int) -> Interval:
    return log_positive_interval(point["h"], terms)


def deflated_log_value(
    point: dict[str, Any], bins: list[dict[str, Any]], terms: int
) -> Interval:
    result = raw_log_value(point, terms)
    u = point["u"]
    for zero_bin in bins:
        explicit = log_positive_fraction(u + zero_bin["B"], terms).scale(
            Fraction(zero_bin["count"])
        )
        result = result.sub(explicit)
    return result


def secant(
    left: dict[str, Any],
    right: dict[str, Any],
    left_value: Interval,
    right_value: Interval,
) -> Interval:
    denominator = left["u"] - right["u"]
    if denominator == 0:
        raise CertificateError("secant nodes must be distinct")
    return left_value.sub(right_value).scale(Fraction(1, 1) / denominator)


def monotonicity_product(
    left: dict[str, Any],
    right: dict[str, Any],
    bins: list[dict[str, Any]],
) -> Interval:
    if not left["u"] < right["u"]:
        raise CertificateError("monotonicity nodes must be increasing")
    left_factor = Fraction(1)
    right_factor = Fraction(1)
    for zero_bin in bins:
        left_factor *= (left["u"] + zero_bin["B"]) ** zero_bin["count"]
        right_factor *= (right["u"] + zero_bin["B"]) ** zero_bin["count"]
    return right["h"].scale(left_factor).sub(left["h"].scale(right_factor))


def loewner_determinant(
    point_ids_rows: list[str],
    point_ids_columns: list[str],
    points: dict[str, dict[str, Any]],
    bins: list[dict[str, Any]],
    terms: int,
    deflated: bool,
) -> Interval:
    size = len(point_ids_rows)
    if size < 1 or size != len(point_ids_columns) or size > 4:
        raise CertificateError("Loewner determinant order must be between one and four")
    if len(set(point_ids_rows)) != size or len(set(point_ids_columns)) != size:
        raise CertificateError("Loewner row and column lists must not repeat nodes")
    if set(point_ids_rows) & set(point_ids_columns):
        raise CertificateError("Loewner row and column lists must be disjoint")
    if any(identifier not in points for identifier in point_ids_rows + point_ids_columns):
        raise CertificateError("Loewner row references an unknown point")

    row_nodes = [points[identifier]["u"] for identifier in point_ids_rows]
    column_nodes = [points[identifier]["u"] for identifier in point_ids_columns]
    if any(row_nodes[i] >= row_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner row nodes must be strictly increasing")
    if any(column_nodes[i] >= column_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner column nodes must be strictly increasing")

    identifiers = point_ids_rows + point_ids_columns
    values: dict[str, Interval] = {}
    for identifier in identifiers:
        values[identifier] = (
            deflated_log_value(points[identifier], bins, terms)
            if deflated
            else raw_log_value(points[identifier], terms)
        )

    matrix: list[list[Interval]] = []
    for row_id in point_ids_rows:
        matrix_row = []
        for column_id in point_ids_columns:
            matrix_row.append(
                secant(
                    points[row_id],
                    points[column_id],
                    values[row_id],
                    values[column_id],
                )
            )
        matrix.append(matrix_row)
    return determinant_interval(matrix)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("completed-xi normalization mismatch")
    classification = data.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise CertificateError("unsupported classification")
    ordinate = rational(data.get("ordinate"), "ordinate")
    terms = exact_int(data.get("log_terms", 256), "log_terms")
    if terms < 32 or terms > 4096:
        raise CertificateError("log_terms must be between 32 and 4096")

    points = parse_points(data)
    bins = parse_zero_bins(data, ordinate, classification)
    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be a nonempty list")

    outputs: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{index}] must be an object")
        row_id = raw.get("id")
        kind = raw.get("kind")
        if not isinstance(row_id, str) or not row_id or row_id in seen_ids:
            raise CertificateError("row id must be nonempty and unique")
        seen_ids.add(row_id)

        if kind in ("raw-monotonicity", "deflated-monotonicity"):
            left_id, right_id = raw.get("left"), raw.get("right")
            if left_id not in points or right_id not in points:
                raise CertificateError(f"unknown monotonicity point in {row_id}")
            left, right = points[left_id], points[right_id]
            if not left["u"] < right["u"]:
                raise CertificateError("monotonicity nodes must be increasing")
            if kind == "raw-monotonicity":
                value = right["h"].sub(left["h"])
            else:
                value = monotonicity_product(left, right, bins)
            detail = {"left": left_id, "right": right_id}

        elif kind in (
            "raw-cross-loewner-determinant",
            "deflated-cross-loewner-determinant",
        ):
            row_ids, column_ids = raw.get("rows"), raw.get("columns")
            if not isinstance(row_ids, list) or not isinstance(column_ids, list):
                raise CertificateError("Loewner rows and columns must be arrays")
            value = loewner_determinant(
                row_ids,
                column_ids,
                points,
                bins,
                terms,
                deflated=kind.startswith("deflated"),
            )
            detail = {
                "rows": row_ids,
                "columns": column_ids,
                "order": len(row_ids),
            }
        else:
            raise CertificateError(f"unsupported row kind {kind!r}")

        outputs.append(
            {
                "id": row_id,
                "kind": kind,
                **detail,
                "interval": ij(value),
                "status": row_status(value),
            }
        )

    negative = [row for row in outputs if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in outputs if row["status"] == "UNRESOLVED"]
    if classification == "RIEMANN_XI_DIRECTED" and negative:
        verdict = "NEGATIVE_ZERO_DEFLATED_XI_MODULUS_WITNESS_PENDING_REVIEW"
    elif classification == "SYNTHETIC_MODEL" and negative:
        verdict = "SYNTHETIC_ZERO_DEFLATION_SEPARATION"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_ROWS"

    return {
        "schema": SCHEMA,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "ordinate": fj(ordinate),
        "point_count": len(points),
        "zero_bins": [
            {
                "id": item["id"],
                "lower_ordinate": fj(item["lower"]),
                "upper_ordinate": fj(item["upper"]),
                "count_lower": item["count"],
                "distance_square_upper": fj(item["B"]),
                "gate_sha256": item["gate_sha256"],
            }
            for item in bins
        ],
        "point_fingerprints": {
            identifier: point["sha256"] for identifier, point in sorted(points.items())
        },
        "rows": outputs,
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "The checker proves exact rectangle contraction and zero-bin algebra only. "
            "A Riemann-xi negative also requires proof-grade completed-xi rectangles, "
            "independent validation of every critical-line zero-count gate, and "
            "independent review of L-9301 and the completed-xi normalization."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["verdict"] != "UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
