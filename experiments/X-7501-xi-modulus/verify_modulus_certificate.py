#!/usr/bin/env python3
"""Exact checker for direct completed-xi modulus witness certificates.

The checker consumes exact rational complex rectangles.  It evaluates no special
function and uses no floating-point arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.xi-modulus-witness.v1"
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


def square_interval(value: Interval) -> Interval:
    upper = max(value.lower * value.lower, value.upper * value.upper)
    if value.lower <= 0 <= value.upper:
        lower = Fraction(0)
    else:
        lower = min(value.lower * value.lower, value.upper * value.upper)
    return Interval(lower, upper)


def modulus_squared(real: Interval, imag: Interval) -> Interval:
    return square_interval(real).add(square_interval(imag))


def canonical_sha(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def divided_difference(points: list[tuple[Fraction, Interval]]) -> Interval:
    if not points:
        raise CertificateError("empty divided-difference point list")
    result = Interval(Fraction(0), Fraction(0))
    for i, (u_i, value_i) in enumerate(points):
        denominator = Fraction(1)
        for j, (u_j, _) in enumerate(points):
            if i != j:
                denominator *= u_i - u_j
        if denominator == 0:
            raise CertificateError("repeated divided-difference node")
        result = result.add(value_i.scale(1 / denominator))
    return result


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def parse_points(data: dict[str, Any]) -> tuple[Fraction, dict[str, dict[str, Any]]]:
    ordinate = rational(data.get("ordinate"), "ordinate")
    raw_points = data.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise CertificateError("points must be a nonempty list")
    parsed: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"points[{index}] must be an object")
        point_id = raw.get("id")
        if not isinstance(point_id, str) or not point_id or point_id in parsed:
            raise CertificateError(f"invalid or duplicated point id at points[{index}]")
        x = rational(raw.get("x"), f"points[{index}].x")
        if x < 0:
            raise CertificateError("horizontal offset must be nonnegative")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise CertificateError("xi_rectangle must be an object")
        real = interval(rectangle.get("real"), f"points[{index}].xi_rectangle.real")
        imag = interval(rectangle.get("imag"), f"points[{index}].xi_rectangle.imag")
        h = modulus_squared(real, imag)
        canonical = {
            "id": point_id,
            "x": fj(x),
            "xi_rectangle": {"real": ij(real), "imag": ij(imag)},
        }
        declared_sha = raw.get("point_sha256")
        digest = canonical_sha(canonical)
        if declared_sha is not None and declared_sha != digest:
            raise CertificateError(f"point digest mismatch for {point_id}")
        parsed[point_id] = {
            "x": x,
            "u": x * x,
            "real": real,
            "imag": imag,
            "h": h,
            "sha256": digest,
        }
    return ordinate, parsed


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

    ordinate, points = parse_points(data)
    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be a nonempty list")

    outputs: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{index}] must be an object")
        row_id = raw.get("id")
        kind = raw.get("kind")
        if not isinstance(row_id, str) or not row_id:
            raise CertificateError("row id must be a nonempty string")

        if kind == "monotonicity":
            left_id, right_id = raw.get("left"), raw.get("right")
            if left_id not in points or right_id not in points:
                raise CertificateError(f"unknown monotonicity point in {row_id}")
            left, right = points[left_id], points[right_id]
            if not left["u"] < right["u"]:
                raise CertificateError("monotonicity nodes must be increasing")
            value = right["h"].sub(left["h"])
            detail = {"left": left_id, "right": right_id}

        elif kind == "divided_difference":
            ids = raw.get("points")
            if not isinstance(ids, list) or not ids or any(item not in points for item in ids):
                raise CertificateError(f"bad divided-difference points in {row_id}")
            node_values = [(points[item]["u"], points[item]["h"]) for item in ids]
            if any(node_values[i][0] >= node_values[i + 1][0] for i in range(len(node_values) - 1)):
                raise CertificateError("divided-difference nodes must be strictly increasing")
            value = divided_difference(node_values)
            detail = {"points": ids, "order": len(ids) - 1}

        elif kind == "log_concavity_integer_power":
            left_id, middle_id, right_id = raw.get("left"), raw.get("middle"), raw.get("right")
            if left_id not in points or middle_id not in points or right_id not in points:
                raise CertificateError(f"unknown log-concavity point in {row_id}")
            left, middle, right = points[left_id], points[middle_id], points[right_id]
            u0, u1, u2 = left["u"], middle["u"], right["u"]
            if not u0 < u1 < u2:
                raise CertificateError("log-concavity nodes must be increasing")
            d01, d12 = u1 - u0, u2 - u1
            scale = lcm(d01.denominator, d12.denominator)
            c_exp = int(d01 * scale)
            b_exp = int(d12 * scale)
            common = math.gcd(b_exp, c_exp)
            b_exp //= common
            c_exp //= common
            a_exp = b_exp + c_exp
            lhs = middle["h"].pow_nonnegative(a_exp)
            rhs = left["h"].pow_nonnegative(b_exp).mul(
                right["h"].pow_nonnegative(c_exp)
            )
            value = lhs.sub(rhs)
            detail = {
                "left": left_id,
                "middle": middle_id,
                "right": right_id,
                "exponents": {"A": a_exp, "B": b_exp, "C": c_exp},
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
        verdict = "NEGATIVE_RIEMANN_XI_MODULUS_WITNESS_PENDING_ANALYTIC_REVIEW"
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
        "ordinate": fj(ordinate),
        "point_count": len(points),
        "point_fingerprints": {key: value["sha256"] for key, value in sorted(points.items())},
        "rows": outputs,
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "The checker proves exact rectangle contraction only. A Riemann-xi negative "
            "requires a directed completed-xi producer, precision reproduction, and "
            "independent review of L-7501 and the normalization."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["verdict"] != "UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
