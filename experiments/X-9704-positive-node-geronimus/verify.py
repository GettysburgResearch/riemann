#!/usr/bin/env python3
"""Exact checker for L-9704 positive-node Geronimus Schur gates.

The checker evaluates no special function and uses no floating point.  It
consumes exact rational intervals for the old response moments and the one new
scalar b0, constructs the adapted Hankel/localizing pencils, and either:

* proves the entire next-degree half-line polynomial cone positive by exact
  rational LDL plus an interval row-radius budget; or
* freezes the two midpoint Schur directions and certifies an explicit
  P=q(y)^2 or P=y q(y)^2 negative interval.

Discovery arithmetic and production of b0 remain outside this trust boundary.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.x9704-positive-node-geronimus.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
PRODUCTION = "RIEMANN_XI_DIRECTED"
SYNTHETIC = "SYNTHETIC_MODEL"
EMPIRICAL = "EMPIRICAL_MIDPOINT"
PRODUCTION_GATE = "CERTIFIED_SHARED_DIRECT_XI_COUNT_PROFILE"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    @property
    def midpoint(self) -> Fraction:
        return (self.lower + self.upper) / 2

    @property
    def radius(self) -> Fraction:
        return (self.upper - self.lower) / 2

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def scale(self, scalar: Fraction) -> "Interval":
        a = scalar * self.lower
        b = scalar * self.upper
        return Interval(min(a, b), max(a, b))


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rat(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = raw.get("numerator")
    denominator = raw.get("denominator")
    if isinstance(numerator, str):
        try:
            numerator = int(numerator)
        except ValueError as error:
            raise CertificateError(f"{name}.numerator is not integer text") from error
    if isinstance(denominator, str):
        try:
            denominator = int(denominator)
        except ValueError as error:
            raise CertificateError(f"{name}.denominator is not integer text") from error
    numerator = exact_int(numerator, f"{name}.numerator")
    denominator = exact_int(denominator, f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        rat(raw.get("lower"), f"{name}.lower"),
        rat(raw.get("upper"), f"{name}.upper"),
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
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a SHA-256 hexadecimal digest")
    return value.lower()


def zero_matrix(size: int, value: Fraction = Fraction(0)) -> list[list[Fraction]]:
    return [[value for _ in range(size)] for _ in range(size)]


def interval_matrix(size: int) -> list[list[Interval]]:
    zero = Interval(Fraction(0), Fraction(0))
    return [[zero for _ in range(size)] for _ in range(size)]


def ldl_positive_definite(matrix: list[list[Fraction]]) -> list[Fraction]:
    size = len(matrix)
    if size < 1 or any(len(row) != size for row in matrix):
        raise CertificateError("LDL matrix must be nonempty and square")
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(size)):
        raise CertificateError("LDL matrix must be symmetric")
    lower = zero_matrix(size)
    pivots = [Fraction(0) for _ in range(size)]
    for i in range(size):
        pivot = matrix[i][i]
        for k in range(i):
            pivot -= lower[i][k] * lower[i][k] * pivots[k]
        if pivot <= 0:
            raise CertificateError(f"nonpositive LDL pivot at index {i}")
        pivots[i] = pivot
        lower[i][i] = Fraction(1)
        for j in range(i + 1, size):
            value = matrix[j][i]
            for k in range(i):
                value -= lower[j][k] * lower[i][k] * pivots[k]
            lower[j][i] = value / pivot
    return pivots


def solve(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    size = len(matrix)
    if size < 1 or len(vector) != size or any(len(row) != size for row in matrix):
        raise CertificateError("linear solve dimension mismatch")
    augmented = [list(row) + [vector[i]] for i, row in enumerate(matrix)]
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if augmented[row][column] != 0),
            None,
        )
        if pivot_row is None:
            raise CertificateError("singular midpoint Schur block")
        if pivot_row != column:
            augmented[column], augmented[pivot_row] = (
                augmented[pivot_row],
                augmented[column],
            )
        pivot = augmented[column][column]
        augmented[column] = [entry / pivot for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    left - factor * right
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return [augmented[i][-1] for i in range(size)]


def contract(matrix: list[list[Interval]], vector: list[Fraction]) -> Interval:
    size = len(matrix)
    if len(vector) != size:
        raise CertificateError("quadratic contraction dimension mismatch")
    result = Interval(Fraction(0), Fraction(0))
    for i in range(size):
        for j in range(size):
            coefficient = vector[i] * vector[j]
            if coefficient:
                result = result.add(matrix[i][j].scale(coefficient))
    return result


def matrix_midpoint_radius(
    matrix: list[list[Interval]],
) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    mid = [[entry.midpoint for entry in row] for row in matrix]
    radius = [[entry.radius for entry in row] for row in matrix]
    return mid, radius


def maximum_row_sum(matrix: list[list[Fraction]]) -> Fraction:
    return max((sum(abs(entry) for entry in row) for row in matrix), default=Fraction(0))


def shifted(matrix: list[list[Fraction]], delta: Fraction) -> list[list[Fraction]]:
    return [
        [entry - (delta if i == j else 0) for j, entry in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def build_adapted_matrices(
    moments: list[Interval], b0: Interval, w: Fraction
) -> tuple[list[list[Interval]], list[list[Interval]]]:
    # len(moments)=2m+1 contains a_0,...,a_(2m)
    if len(moments) < 3 or len(moments) % 2 != 1:
        raise CertificateError("old_moments length must be odd and at least three")
    m = (len(moments) - 1) // 2
    size = m + 1
    g0 = interval_matrix(size)
    g1 = interval_matrix(size)
    g0[0][0] = b0
    g1[0][0] = moments[0].add(b0.scale(-w))
    for index in range(m):
        g0[0][index + 1] = moments[index]
        g0[index + 1][0] = moments[index]
        g1[0][index + 1] = moments[index + 1]
        g1[index + 1][0] = moments[index + 1]
    for i in range(m):
        for j in range(m):
            g0[i + 1][j + 1] = moments[i + j + 1].add(
                moments[i + j].scale(w)
            )
            g1[i + 1][j + 1] = moments[i + j + 2].add(
                moments[i + j + 1].scale(w)
            )
    return g0, g1


def schur_diagnostics(
    matrix: list[list[Interval]], orientation: str
) -> tuple[Fraction, list[Fraction], Interval]:
    mid, _ = matrix_midpoint_radius(matrix)
    lower_block = [row[1:] for row in mid[1:]]
    cross = mid[0][1:]
    direction = solve(lower_block, cross)
    vector = [Fraction(1)] + [-value for value in direction]
    value = contract(matrix, vector)
    theta = sum(cross[i] * direction[i] for i in range(len(direction)))
    if orientation not in ("lower", "upper-localizing"):
        raise CertificateError("unknown Schur orientation")
    return theta, vector, value


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    classification = data.get("classification")
    if classification not in (PRODUCTION, SYNTHETIC, EMPIRICAL):
        raise CertificateError("unsupported classification")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("completed-xi normalization mismatch")

    w = rat(data.get("w"), "w")
    if w <= 0:
        raise CertificateError("w must be positive")

    raw_moments = data.get("old_moments")
    if not isinstance(raw_moments, list):
        raise CertificateError("old_moments must be an array")
    moments = [
        interval(raw, f"old_moments[{index}]")
        for index, raw in enumerate(raw_moments)
    ]
    b0 = interval(data.get("b0_interval"), "b0_interval")
    delta0 = rat(data.get("delta0"), "delta0")
    delta1 = rat(data.get("delta1"), "delta1")
    if delta0 <= 0 or delta1 <= 0:
        raise CertificateError("delta0 and delta1 must be positive")

    if classification == PRODUCTION:
        gate = data.get("source_gate")
        if not isinstance(gate, dict) or gate.get("status") != PRODUCTION_GATE:
            raise CertificateError("production source gate is missing or invalid")
        for field in (
            "old_basis_sha256",
            "old_primitive_sha256",
            "count_profile_sha256",
            "new_primitive_sha256",
        ):
            validate_sha256(gate.get(field), f"source_gate.{field}")

    g0, g1 = build_adapted_matrices(moments, b0, w)
    m0, r0 = matrix_midpoint_radius(g0)
    m1, r1 = matrix_midpoint_radius(g1)
    radius0 = maximum_row_sum(r0)
    radius1 = maximum_row_sum(r1)

    closure0 = False
    closure1 = False
    pivots0: list[Fraction] = []
    pivots1: list[Fraction] = []
    try:
        pivots0 = ldl_positive_definite(shifted(m0, delta0))
        closure0 = radius0 < delta0
    except CertificateError:
        closure0 = False
    try:
        pivots1 = ldl_positive_definite(shifted(m1, delta1))
        closure1 = radius1 < delta1
    except CertificateError:
        closure1 = False

    lower_boundary, lower_vector, lower_witness = schur_diagnostics(g0, "lower")
    local_boundary, upper_vector, upper_witness = schur_diagnostics(
        g1, "upper-localizing"
    )

    negative_rows: list[dict[str, Any]] = []
    if lower_witness.upper < 0:
        negative_rows.append(
            {
                "kind": "square",
                "adapted_vector": [fj(value) for value in lower_vector],
                "interval": ij(lower_witness),
                "response": "q(y)^2",
            }
        )
    if upper_witness.upper < 0:
        negative_rows.append(
            {
                "kind": "y-square",
                "adapted_vector": [fj(value) for value in upper_vector],
                "interval": ij(upper_witness),
                "response": "y*q(y)^2",
            }
        )

    if negative_rows:
        verdict = (
            "NEGATIVE_POSITIVE_NODE_RESPONSE_WITNESS_PENDING_REVIEW"
            if classification == PRODUCTION
            else "NEGATIVE_SYNTHETIC_OR_EMPIRICAL_WITNESS"
        )
    elif closure0 and closure1:
        verdict = "CERTIFIED_POSITIVE_FULL_NEXT_DEGREE_HALF_LINE_CONE"
    else:
        verdict = "UNRESOLVED"

    canonical = {
        "schema": SCHEMA,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "w": fj(w),
        "old_degree": len(moments) - 1,
        "new_degree": len(moments),
        "b0_interval": ij(b0),
        "delta0": fj(delta0),
        "delta1": fj(delta1),
        "g0_maximum_row_radius": fj(radius0),
        "g1_maximum_row_radius": fj(radius1),
        "g0_robust_positive": closure0,
        "g1_robust_positive": closure1,
        "g0_ldl_pivots": [fj(value) for value in pivots0],
        "g1_ldl_pivots": [fj(value) for value in pivots1],
        "lower_schur_midpoint_boundary": fj(lower_boundary),
        "localizing_schur_midpoint_boundary": fj(local_boundary),
        "lower_schur_witness_interval": ij(lower_witness),
        "upper_schur_witness_interval": ij(upper_witness),
        "negative_rows": negative_rows,
        "verdict": verdict,
        "proof_boundary": (
            "Finite exact rational interval algebra only. A production negative "
            "also requires independent validation of the direct-xi primitives, "
            "count profile, normalization, L-9704, and inherited response theorems."
        ),
    }
    canonical["certificate_sha256"] = canonical_sha(canonical)
    return canonical


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
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as error:
        print(json.dumps({"verified": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(text, end="")
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    return 1 if result["verdict"] == "UNRESOLVED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
