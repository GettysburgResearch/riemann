#!/usr/bin/env python3
"""Decide a complete degree-bounded half-line response cone from directed moments."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

MOMENT_SCHEMA = "riemann.x9311-directed-response-moments.v1"
OUTPUT_SCHEMA = "riemann.x9311-full-halfline-cone-verification.v1"


class VerificationError(ValueError):
    pass


class Interval:
    __slots__ = ("lower", "upper")

    def __init__(self, lower: Fraction, upper: Fraction):
        if lower > upper:
            raise VerificationError("reversed interval")
        self.lower = lower
        self.upper = upper

    def midpoint(self) -> Fraction:
        return (self.lower + self.upper) / 2

    def radius(self) -> Fraction:
        return (self.upper - self.lower) / 2

    def scale(self, scalar: Fraction) -> "Interval":
        if scalar >= 0:
            return Interval(self.lower * scalar, self.upper * scalar)
        return Interval(self.upper * scalar, self.lower * scalar)

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)


def parse_decimal(value: Any, name: str) -> Fraction:
    if not isinstance(value, str) or not value:
        raise VerificationError(f"{name} must be an exact decimal string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise VerificationError(f"invalid exact decimal at {name}") from exc


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def interval_json(value: Interval) -> dict[str, dict[str, str]]:
    return {"lower": fraction_json(value.lower), "upper": fraction_json(value.upper)}


def load_moments(path: Path) -> tuple[dict[str, Any], list[Interval]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != MOMENT_SCHEMA:
        raise VerificationError("unsupported moment schema")
    rows = data.get("basis_rows")
    if not isinstance(rows, list) or len(rows) < 3:
        raise VerificationError("basis_rows missing")
    moments: list[Interval] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or row.get("degree") != index:
            raise VerificationError("basis degrees must be consecutive")
        lower = parse_decimal(row.get("lower_exact_decimal"), f"row[{index}].lower")
        upper = parse_decimal(row.get("upper_exact_decimal"), f"row[{index}].upper")
        moments.append(Interval(lower, upper))
    if data.get("response_degree_bound") != len(moments) - 1:
        raise VerificationError("response_degree_bound mismatch")
    return data, moments


def hankel(values: list[Interval], size: int, offset: int) -> list[list[Interval]]:
    if size < 1 or 2 * (size - 1) + offset >= len(values):
        raise VerificationError("insufficient moments for Hankel matrix")
    return [[values[i + j + offset] for j in range(size)] for i in range(size)]


def exact_ldl_positive_pivots(matrix: list[list[Fraction]]) -> list[Fraction]:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise VerificationError("matrix must be square")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise VerificationError("matrix must be symmetric")
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = [Fraction(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivots[i] = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivots[i] <= 0:
            raise VerificationError(f"nonpositive exact LDL pivot at index {i}")
        for j in range(i + 1, n):
            numerator = matrix[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivots[i]
    return pivots


def midpoint_matrix(matrix: list[list[Interval]]) -> list[list[Fraction]]:
    return [[entry.midpoint() for entry in row] for row in matrix]


def box_radius(matrix: list[list[Interval]]) -> Fraction:
    return max(sum(entry.radius() for entry in row) for row in matrix)


def subtract_diagonal(matrix: list[list[Fraction]], amount: Fraction) -> list[list[Fraction]]:
    return [
        [entry - (amount if i == j else 0) for j, entry in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def positive_box_certificate(matrix: list[list[Interval]]) -> tuple[list[Fraction], Fraction]:
    epsilon = box_radius(matrix)
    pivots = exact_ldl_positive_pivots(subtract_diagonal(midpoint_matrix(matrix), epsilon))
    return pivots, epsilon


def interval_quadratic(matrix: list[list[Interval]], vector: list[Fraction]) -> Interval:
    total = Interval(Fraction(0), Fraction(0))
    for i, row in enumerate(matrix):
        for j, entry in enumerate(row):
            total = total.add(entry.scale(vector[i] * vector[j]))
    return total


def gcd_all(values: list[int]) -> int:
    result = 0
    for value in values:
        result = math.gcd(result, abs(value))
    return max(result, 1)


def discover_negative_witness(
    matrix: list[list[Interval]], denominator_bits: int = 120
) -> tuple[list[Fraction] | None, Interval | None, float]:
    try:
        import numpy as np
    except ImportError as exc:
        raise VerificationError("numpy is required only for negative-direction discovery") from exc
    midpoint = np.array(
        [[float(entry.midpoint()) for entry in row] for row in matrix], dtype=float
    )
    eigenvalues, eigenvectors = np.linalg.eigh(midpoint)
    minimum = float(eigenvalues[0])
    if not math.isfinite(minimum) or minimum >= 0:
        return None, None, minimum
    scale = 1 << denominator_bits
    integers = [int(round(float(value) * scale)) for value in eigenvectors[:, 0]]
    divisor = gcd_all(integers)
    integers = [value // divisor for value in integers]
    if not any(integers):
        raise VerificationError("rationalized witness vanished")
    vector = [Fraction(value) for value in integers]
    value = interval_quadratic(matrix, vector)
    return vector, value, minimum


def vector_json(vector: list[Fraction] | None) -> list[dict[str, str]] | None:
    return [fraction_json(value) for value in vector] if vector is not None else None


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path) -> dict[str, Any]:
    data, moments = load_moments(path)
    degree = len(moments) - 1
    if degree % 2 == 0:
        half = degree // 2
        h0_size = half + 1
        h1_size = half
    else:
        half = (degree - 1) // 2
        h0_size = half + 1
        h1_size = half + 1
    h0 = hankel(moments, h0_size, 0)
    h1 = hankel(moments, h1_size, 1)

    h0_pivots: list[Fraction] = []
    h1_pivots: list[Fraction] = []
    h0_epsilon = box_radius(h0)
    h1_epsilon = box_radius(h1)
    h0_positive = h1_positive = False
    try:
        h0_pivots, h0_epsilon = positive_box_certificate(h0)
        h0_positive = True
    except VerificationError:
        pass
    try:
        h1_pivots, h1_epsilon = positive_box_certificate(h1)
        h1_positive = True
    except VerificationError:
        pass

    h0_witness = h1_witness = None
    h0_value = h1_value = None
    h0_min = h1_min = float("nan")
    if not h0_positive:
        h0_witness, h0_value, h0_min = discover_negative_witness(h0)
    if not h1_positive:
        h1_witness, h1_value, h1_min = discover_negative_witness(h1)

    if h0_value is not None and h0_value.upper < 0:
        verdict = "CERTIFIED_NEGATIVE_DEGREE18_SQUARE_WITNESS"
        witness_kind = "q(y)^2"
    elif h1_value is not None and h1_value.upper < 0:
        verdict = "CERTIFIED_NEGATIVE_DEGREE18_Y_SQUARE_WITNESS"
        witness_kind = "y*q(y)^2"
    elif h0_positive and h1_positive:
        verdict = "CERTIFIED_POSITIVE_FULL_DEGREE18_HALF_LINE_CONE"
        witness_kind = None
    else:
        verdict = "UNRESOLVED_DEGREE18_HALF_LINE_CONE"
        witness_kind = None

    proof_object = {
        "degree": degree,
        "h0_size": h0_size,
        "h1_size": h1_size,
        "h0_pivots": [fraction_json(value) for value in h0_pivots],
        "h1_pivots": [fraction_json(value) for value in h1_pivots],
        "h0_box_radius": fraction_json(h0_epsilon),
        "h1_box_radius": fraction_json(h1_epsilon),
        "h0_witness": vector_json(h0_witness),
        "h1_witness": vector_json(h1_witness),
        "h0_witness_value": interval_json(h0_value) if h0_value else None,
        "h1_witness_value": interval_json(h1_value) if h1_value else None,
    }
    proof_digest = hashlib.sha256(
        json.dumps(proof_object, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()

    return {
        "schema": OUTPUT_SCHEMA,
        "classification": data.get("classification"),
        "analytic_claim": "L-9310",
        "moment_source_sha256": file_sha256(path),
        "certificate_sha256": data.get("certificate_sha256"),
        "ordinate": data.get("ordinate"),
        "selected_zero_count": data.get("selected_zero_count"),
        "node_count": data.get("node_count"),
        "degree_bound": degree,
        "h0_dimension": h0_size,
        "h1_dimension": h1_size,
        "h0_box_radius": fraction_json(h0_epsilon),
        "h1_box_radius": fraction_json(h1_epsilon),
        "h0_exact_ldl_pivots": [fraction_json(value) for value in h0_pivots],
        "h1_exact_ldl_pivots": [fraction_json(value) for value in h1_pivots],
        "h0_discovery_minimum_eigenvalue": h0_min,
        "h1_discovery_minimum_eigenvalue": h1_min,
        "h0_witness_coefficients": vector_json(h0_witness),
        "h1_witness_coefficients": vector_json(h1_witness),
        "h0_witness_interval": interval_json(h0_value) if h0_value else None,
        "h1_witness_interval": interval_json(h1_value) if h1_value else None,
        "witness_response": witness_kind,
        "exact_proof_object_sha256": proof_digest,
        "verdict": verdict,
        "counterexample_nomination": (
            "PENDING_INDEPENDENT_REPRODUCTION" if verdict.startswith("CERTIFIED_NEGATIVE") else None
        ),
        "scope": (
            "The two moment matrices decide every real response polynomial of degree "
            "at most the stated bound that is nonnegative on [0,infinity)."
        ),
        "proof_boundary": (
            "Positive closure uses exact rational LDL on midpoint-minus-complete-box-radius. "
            "Negative discovery may use numpy, but promotion uses only the emitted rational "
            "vector and exact interval quadratic contraction."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("moments", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = verify(args.moments)
    except (OSError, json.JSONDecodeError, VerificationError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "degree_bound": result["degree_bound"],
                "h0_dimension": result["h0_dimension"],
                "h1_dimension": result["h1_dimension"],
                "h0_discovery_minimum_eigenvalue": result["h0_discovery_minimum_eigenvalue"],
                "h1_discovery_minimum_eigenvalue": result["h1_discovery_minimum_eigenvalue"],
                "exact_proof_object_sha256": result["exact_proof_object_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 1 if result["verdict"].startswith("CERTIFIED_NEGATIVE") else 0


if __name__ == "__main__":
    raise SystemExit(main())
