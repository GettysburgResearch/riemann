#!/usr/bin/env python3
"""Exact checker for L-9312 one-node Padé/support-gap certificates."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x9310-one-node-pade.v1"
OUTPUT_SCHEMA = "riemann.x9310-one-node-pade-verification.v1"


class CertificateError(ValueError):
    pass


class Interval:
    __slots__ = ("lower", "upper")

    def __init__(self, lower: Fraction, upper: Fraction):
        if lower > upper:
            raise CertificateError("reversed interval")
        self.lower = lower
        self.upper = upper

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, scalar: Fraction) -> "Interval":
        if scalar >= 0:
            return Interval(self.lower * scalar, self.upper * scalar)
        return Interval(self.upper * scalar, self.lower * scalar)

    def midpoint(self) -> Fraction:
        return (self.lower + self.upper) / 2

    def radius(self) -> Fraction:
        return (self.upper - self.lower) / 2


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = raw.get("numerator")
    denominator = raw.get("denominator")
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or denominator <= 0
    ):
        raise CertificateError(f"bad rational at {name}")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        fraction(raw.get("lower"), f"{name}.lower"),
        fraction(raw.get("upper"), f"{name}.upper"),
    )


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fraction_json(value.lower), "upper": fraction_json(value.upper)}


def parse_vector(raw: Any, length: int, name: str) -> list[Fraction] | None:
    if raw is None:
        return None
    if not isinstance(raw, list) or len(raw) != length:
        raise CertificateError(f"{name} must have length {length}")
    return [fraction(item, f"{name}[{i}]") for i, item in enumerate(raw)]


def build_moments(old: list[Interval], b0: Interval, w: Fraction) -> list[Interval]:
    output = [b0]
    for a in old:
        output.append(a.sub(output[-1].scale(w)))
    return output


def hankel(values: list[Interval], size: int, offset: int = 0) -> list[list[Interval]]:
    if 2 * (size - 1) + offset >= len(values):
        raise CertificateError("insufficient moments for Hankel matrix")
    return [[values[i + j + offset] for j in range(size)] for i in range(size)]


def localizer(values: list[Interval], size: int, support: Fraction) -> list[list[Interval]]:
    return [
        [values[i + j + 1].sub(values[i + j].scale(support)) for j in range(size)]
        for i in range(size)
    ]


def quadratic(matrix: list[list[Interval]], vector: list[Fraction]) -> Interval:
    total = Interval(Fraction(0), Fraction(0))
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            total = total.add(value.scale(vector[i] * vector[j]))
    return total


def subtract_diagonal(matrix: list[list[Fraction]], delta: Fraction) -> list[list[Fraction]]:
    return [
        [value - (delta if i == j else 0) for j, value in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def exact_ldl_positive_pivots(matrix: list[list[Fraction]]) -> list[Fraction]:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise CertificateError("matrix must be square")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise CertificateError("matrix must be symmetric")
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = [Fraction(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivots[i] = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivots[i] <= 0:
            raise CertificateError(f"nonpositive exact LDL pivot at index {i}")
        for j in range(i + 1, n):
            numerator = matrix[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivots[i]
    return pivots


def matrix_box_certificate(
    matrix: list[list[Interval]], delta: Fraction
) -> tuple[list[Fraction], Fraction]:
    midpoint = [[value.midpoint() for value in row] for row in matrix]
    radius = [[value.radius() for value in row] for row in matrix]
    pivots = exact_ldl_positive_pivots(subtract_diagonal(midpoint, delta))
    epsilon = max(sum(abs(value) for value in row) for row in radius)
    if epsilon >= delta:
        raise CertificateError("matrix interval radius is not below delta")
    return pivots, epsilon


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot load certificate: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise CertificateError("unsupported certificate schema")

    w = fraction(data.get("w"), "w")
    support = fraction(data.get("support_lower"), "support_lower")
    if w < 0 or support < 0:
        raise CertificateError("w and support_lower must be nonnegative")

    raw_old = data.get("old_moments")
    if not isinstance(raw_old, list) or len(raw_old) < 3 or len(raw_old) % 2 != 1:
        raise CertificateError("old_moments must have odd length at least three")
    old = [interval(item, f"old_moments[{i}]") for i, item in enumerate(raw_old)]
    n = (len(old) - 1) // 2
    size = n + 1

    b0 = interval(data.get("new_b0"), "new_b0")
    moments = build_moments(old, b0, w)
    h0 = hankel(moments, size, 0)
    ha = localizer(moments, size, support)

    lower_q = parse_vector(data.get("lower_witness"), size, "lower_witness")
    upper_q = parse_vector(data.get("upper_witness"), size, "upper_witness")
    lower_value = quadratic(h0, lower_q) if lower_q is not None else None
    upper_value = quadratic(ha, upper_q) if upper_q is not None else None

    pivots_h0: list[Fraction] = []
    pivots_ha: list[Fraction] = []
    epsilon_h0 = Fraction(0)
    epsilon_ha = Fraction(0)
    if lower_value is not None and lower_value.upper < 0:
        verdict = "CERTIFIED_NEGATIVE_LOWER_SQUARE_WITNESS"
    elif upper_value is not None and upper_value.upper < 0:
        verdict = "CERTIFIED_NEGATIVE_SUPPORT_LOCALIZER_WITNESS"
    else:
        delta = fraction(data.get("closure_delta"), "closure_delta")
        if delta <= 0:
            raise CertificateError("closure_delta must be positive")
        try:
            pivots_h0, epsilon_h0 = matrix_box_certificate(h0, delta)
            pivots_ha, epsilon_ha = matrix_box_certificate(ha, delta)
            verdict = "CERTIFIED_POSITIVE_ONE_NODE_PADE_INTERVAL"
        except CertificateError:
            pivots_h0, pivots_ha = [], []
            epsilon_h0 = epsilon_ha = Fraction(0)
            verdict = "UNRESOLVED_ONE_NODE_PADE_INTERVAL"

    return {
        "schema": OUTPUT_SCHEMA,
        "classification": data.get("classification"),
        "analytic_claim": "L-9312",
        "certificate_sha256": file_sha256(path),
        "n": n,
        "matrix_dimension": size,
        "w": fraction_json(w),
        "support_lower": fraction_json(support),
        "new_b0": interval_json(b0),
        "lower_witness_value": interval_json(lower_value) if lower_value else None,
        "upper_witness_value": interval_json(upper_value) if upper_value else None,
        "h0_pivots": [fraction_json(x) for x in pivots_h0],
        "ha_pivots": [fraction_json(x) for x in pivots_ha],
        "h0_box_radius": fraction_json(epsilon_h0),
        "ha_box_radius": fraction_json(epsilon_ha),
        "verdict": verdict,
        "proof_boundary": (
            "Exact Fraction recurrence, interval contraction, rational witness evaluation, "
            "and exact LDL/row-radius closure. The RH implication inherits the direct-xi "
            "positive-measure and declared support-gap gates."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except (CertificateError, OSError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 1 if result["verdict"].startswith("CERTIFIED_NEGATIVE") else 0


if __name__ == "__main__":
    raise SystemExit(main())
