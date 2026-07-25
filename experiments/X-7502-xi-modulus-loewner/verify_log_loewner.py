#!/usr/bin/env python3
"""Exact checker for logarithmic completed-xi modulus Loewner minors.

The checker uses only integers and fractions.Fraction. It consumes positive
rational intervals for H_T(u)=|xi(1/2+sqrt(u)+iT)|^2 (or a synthetic analogue),
encloses their real logarithms by an exact atanh series, builds value-only
cross-Loewner secant matrices, and encloses their determinants.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.xi-modulus-log-loewner.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


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
        if scalar >= 0:
            return Interval(self.lower * scalar, self.upper * scalar)
        return Interval(self.upper * scalar, self.lower * scalar)

    def mul(self, other: "Interval") -> "Interval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(values), max(values))


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
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def compare_fraction_power_two(value: Fraction, exponent: int) -> int:
    """Return sign(value - 2**exponent) exactly."""
    if exponent >= 0:
        rhs_num, rhs_den = 1 << exponent, 1
    else:
        rhs_num, rhs_den = 1, 1 << (-exponent)
    lhs = value.numerator * rhs_den
    rhs = rhs_num * value.denominator
    return (lhs > rhs) - (lhs < rhs)


def floor_log2(value: Fraction) -> int:
    if value <= 0:
        raise CertificateError("logarithm input must be positive")
    k = value.numerator.bit_length() - value.denominator.bit_length()
    while compare_fraction_power_two(value, k) < 0:
        k -= 1
    while compare_fraction_power_two(value, k + 1) >= 0:
        k += 1
    return k


def log_unit_interval(value: Fraction, terms: int) -> Interval:
    """Enclose log(value) for 1 <= value < 2 by the positive atanh series."""
    if not (Fraction(1) <= value < Fraction(2)):
        raise CertificateError("log_unit_interval requires 1 <= value < 2")
    z = (value - 1) / (value + 1)
    partial = Fraction(0)
    power = z
    z2 = z * z
    for j in range(terms):
        partial += 2 * power / (2 * j + 1)
        power *= z2
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(partial, partial + tail)


def _log2_interval(terms: int) -> Interval:
    # log(2) = 2 atanh(1/3); the unit helper excludes its right endpoint.
    z = Fraction(1, 3)
    partial = Fraction(0)
    power = z
    z2 = z * z
    for j in range(terms):
        partial += 2 * power / (2 * j + 1)
        power *= z2
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(partial, partial + tail)


def log_fraction_interval(
    value: Fraction, terms: int, cached_log2: Interval | None = None
) -> Interval:
    if value <= 0:
        raise CertificateError("logarithm input must be positive")
    if terms < 1:
        raise CertificateError("log_series_terms must be positive")
    k = floor_log2(value)
    if k >= 0:
        y = value / (1 << k)
    else:
        y = value * (1 << (-k))
    if not (Fraction(1) <= y < Fraction(2)):
        raise AssertionError("power-of-two reduction failed")
    unit = log_unit_interval(y, terms)
    l2 = cached_log2 or _log2_interval(terms)
    return unit.add(l2.scale(Fraction(k)))


def log_positive_interval(value: Interval, terms: int, cached_log2: Interval) -> Interval:
    if value.lower <= 0:
        raise CertificateError("H interval must have a strictly positive lower endpoint")
    lower = log_fraction_interval(value.lower, terms, cached_log2).lower
    upper = log_fraction_interval(value.upper, terms, cached_log2).upper
    return Interval(lower, upper)


def determinant_interval(matrix: list[list[Interval]]) -> Interval:
    n = len(matrix)
    if n < 1 or any(len(row) != n for row in matrix):
        raise CertificateError("determinant matrix must be nonempty and square")
    total = Interval(Fraction(0), Fraction(0))
    for permutation in itertools.permutations(range(n)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(n)
            for j in range(i + 1, n)
        )
        term = Interval(Fraction(1), Fraction(1))
        for i, j in enumerate(permutation):
            term = term.mul(matrix[i][j])
        total = total.add(term.scale(Fraction(-1 if inversions % 2 else 1)))
    return total


def parse_points(data: dict[str, Any], terms: int) -> dict[str, dict[str, Any]]:
    raw_points = data.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise CertificateError("points must be a nonempty list")
    l2 = _log2_interval(terms)
    parsed: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"points[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in parsed:
            raise CertificateError(f"invalid or duplicated point id at points[{index}]")
        u = rational(raw.get("u"), f"points[{index}].u")
        if u <= 0:
            raise CertificateError("all Loewner nodes must be positive")
        h = interval(raw.get("h_interval"), f"points[{index}].h_interval")
        g = log_positive_interval(h, terms, l2)
        canonical = {"id": identifier, "u": fj(u), "h_interval": ij(h)}
        digest = canonical_sha(canonical)
        declared = raw.get("point_sha256")
        if declared is not None and declared != digest:
            raise CertificateError(f"point digest mismatch for {identifier}")
        parsed[identifier] = {"u": u, "h": h, "g": g, "sha256": digest}
    return parsed


def row_status(value: Interval) -> str:
    if value.upper < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lower >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("completed-xi normalization mismatch")
    classification = data.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise CertificateError("unsupported classification")
    terms = exact_int(data.get("log_series_terms"), "log_series_terms")
    if not 1 <= terms <= 4096:
        raise CertificateError("log_series_terms must lie in [1,4096]")
    points = parse_points(data, terms)
    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be a nonempty list")

    outputs: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise CertificateError("row ids must be unique nonempty strings")
        seen.add(identifier)
        if raw.get("kind") != "cross-log-loewner-minor":
            raise CertificateError(f"unsupported row kind in {identifier}")
        row_ids = raw.get("row_points")
        col_ids = raw.get("column_points")
        if (
            not isinstance(row_ids, list)
            or not isinstance(col_ids, list)
            or not row_ids
            or len(row_ids) != len(col_ids)
            or len(row_ids) > 4
            or any(item not in points for item in row_ids + col_ids)
        ):
            raise CertificateError(f"bad point lists in {identifier}")
        row_nodes = [points[item]["u"] for item in row_ids]
        col_nodes = [points[item]["u"] for item in col_ids]
        if any(row_nodes[i] >= row_nodes[i + 1] for i in range(len(row_nodes) - 1)):
            raise CertificateError("row nodes must be strictly increasing")
        if any(col_nodes[i] >= col_nodes[i + 1] for i in range(len(col_nodes) - 1)):
            raise CertificateError("column nodes must be strictly increasing")
        if set(row_nodes) & set(col_nodes):
            raise CertificateError("value-only cross-Loewner lists must be disjoint")

        matrix: list[list[Interval]] = []
        for row_id in row_ids:
            row: list[Interval] = []
            for col_id in col_ids:
                u, v = points[row_id]["u"], points[col_id]["u"]
                secant = points[row_id]["g"].sub(points[col_id]["g"]).scale(
                    1 / (u - v)
                )
                row.append(secant)
            matrix.append(row)
        value = determinant_interval(matrix)
        outputs.append(
            {
                "id": identifier,
                "kind": "cross-log-loewner-minor",
                "order": len(row_ids),
                "row_points": row_ids,
                "column_points": col_ids,
                "matrix": [[ij(entry) for entry in row] for row in matrix],
                "determinant_interval": ij(value),
                "status": row_status(value),
            }
        )

    negative = [row for row in outputs if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in outputs if row["status"] == "UNRESOLVED"]
    if classification == "RIEMANN_XI_DIRECTED" and negative:
        verdict = "NEGATIVE_RIEMANN_XI_LOG_LOEWNER_WITNESS_PENDING_ANALYTIC_REVIEW"
    elif classification == "SYNTHETIC_MODEL" and negative:
        verdict = "SYNTHETIC_NEGATIVE_CONTROL"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_ROWS"

    return {
        "schema": SCHEMA,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "log_series_terms": terms,
        "point_count": len(points),
        "point_fingerprints": {
            key: value["sha256"] for key, value in sorted(points.items())
        },
        "rows": outputs,
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "Exact rational logarithm and determinant enclosure only. A Riemann-xi "
            "negative requires directed primitive H intervals, independent production, "
            "and analytic review of L-7504."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
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
