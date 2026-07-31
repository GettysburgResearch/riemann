#!/usr/bin/env python3
"""Exact verifier for the L-14308 block Temple--Schur lower floor.

After JSON parsing, the trust boundary uses only Python integers and
fractions.Fraction. It performs no floating-point arithmetic or eigensolve.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x14304-block-temple-floor.v1"
OUTPUT_SCHEMA = "riemann.x14304-block-temple-floor-verification.v1"
PRODUCTION = "RIEMANN_WEIL_DIRECTED"
SYNTHETIC = "SYNTHETIC_MODEL"
RADIUS_GATE = "CERTIFIED_OPERATOR_NORM_RADIUS"


class CertificateError(ValueError):
    """Raised when a certificate fails closed."""


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise CertificateError(f"{name} must be integer text") from exc
    raise CertificateError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if isinstance(raw, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(raw, int):
        return Fraction(raw)
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an integer or rational object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def valid_sha256(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    rows: list[list[Fraction]] = []
    width: int | None = None
    for i, row in enumerate(raw):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        parsed = [rational(value, f"{name}[{i}][{j}]") for j, value in enumerate(row)]
        if width is None:
            width = len(parsed)
        elif len(parsed) != width:
            raise CertificateError(f"{name} is ragged")
        rows.append(parsed)
    return rows


def require_square_symmetric(value: list[list[Fraction]], name: str) -> None:
    n = len(value)
    if any(len(row) != n for row in value):
        raise CertificateError(f"{name} must be square")
    if any(value[i][j] != value[j][i] for i in range(n) for j in range(n)):
        raise CertificateError(f"{name} must be symmetric")


def eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(value: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*value)]


def subtract(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(left) != len(right) or any(len(x) != len(y) for x, y in zip(left, right)):
        raise CertificateError("matrix subtraction dimension mismatch")
    return [[x - y for x, y in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def scale(value: list[list[Fraction]], scalar: Fraction) -> list[list[Fraction]]:
    return [[scalar * entry for entry in row] for row in value]


def multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    if not left or not right or len(left[0]) != len(right):
        raise CertificateError("matrix multiplication dimension mismatch")
    right_t = transpose(right)
    return [
        [sum(x * y for x, y in zip(row, column)) for column in right_t]
        for row in left
    ]


def ldl_positive_definite(
    value: list[list[Fraction]], name: str
) -> tuple[list[list[Fraction]], list[Fraction]]:
    require_square_symmetric(value, name)
    n = len(value)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = [Fraction(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivots[i] = value[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivots[i] <= 0:
            raise CertificateError(f"{name} has nonpositive LDL pivot at index {i}")
        for j in range(i + 1, n):
            numerator = value[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivots[i]
    return lower, pivots


def ldl_solve(
    lower: list[list[Fraction]], pivots: list[Fraction], rhs: list[Fraction]
) -> list[Fraction]:
    n = len(pivots)
    if len(rhs) != n:
        raise CertificateError("LDL solve dimension mismatch")
    forward = [Fraction(0) for _ in range(n)]
    for i in range(n):
        forward[i] = rhs[i] - sum(lower[i][k] * forward[k] for k in range(i))
    diagonal = [forward[i] / pivots[i] for i in range(n)]
    solution = [Fraction(0) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        solution[i] = diagonal[i] - sum(
            lower[j][i] * solution[j] for j in range(i + 1, n)
        )
    return solution


def solve_columns(
    lower: list[list[Fraction]], pivots: list[Fraction], rhs: list[list[Fraction]]
) -> list[list[Fraction]]:
    columns = transpose(rhs)
    solved = [ldl_solve(lower, pivots, column) for column in columns]
    return transpose(solved)


def matrix_json(value: list[list[Fraction]]) -> list[list[dict[str, str]]]:
    return [[fj(entry) for entry in row] for row in value]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    classification = data.get("classification")
    if classification not in {SYNTHETIC, PRODUCTION}:
        raise CertificateError("unsupported classification")

    blocks = data.get("blocks")
    if not isinstance(blocks, dict):
        raise CertificateError("blocks must be an object")
    b = matrix(blocks.get("B"), "blocks.B")
    r = matrix(blocks.get("R"), "blocks.R")
    c = matrix(blocks.get("C"), "blocks.C")
    m = matrix(blocks.get("M"), "blocks.M")
    require_square_symmetric(b, "blocks.B")
    require_square_symmetric(c, "blocks.C")
    require_square_symmetric(m, "blocks.M")
    low_dimension = len(b)
    complement_dimension = len(c)
    if len(m) != complement_dimension:
        raise CertificateError("C and M dimensions differ")
    if len(r) != complement_dimension or any(
        len(row) != low_dimension for row in r
    ):
        raise CertificateError(
            "R must have shape complement_dimension x low_dimension"
        )

    gamma = rational(data.get("gamma"), "gamma")
    h = rational(data.get("h"), "h")
    claimed_floor = rational(
        data.get("claimed_midpoint_floor"), "claimed_midpoint_floor"
    )
    operator_radius = rational(data.get("operator_radius"), "operator_radius")
    if h <= 0:
        raise CertificateError("h must be positive")
    if operator_radius < 0:
        raise CertificateError("operator_radius must be nonnegative")
    if classification == PRODUCTION:
        gate = data.get("operator_radius_gate")
        if not isinstance(gate, dict) or gate.get("status") != RADIUS_GATE:
            raise CertificateError(
                "production certificate lacks the operator-radius gate"
            )
        valid_sha256(gate.get("sha256"), "operator_radius_gate.sha256")

    m_lower, m_pivots = ldl_positive_definite(m, "blocks.M")
    complement_slack = subtract(
        subtract(c, scale(eye(complement_dimension), gamma)), scale(m, h)
    )
    _, complement_pivots = ldl_positive_definite(
        complement_slack, "complement coercivity slack"
    )

    solved = solve_columns(m_lower, m_pivots, r)
    correction = multiply(transpose(r), solved)
    corrected_low = subtract(b, scale(correction, Fraction(1, 1) / h))
    corrected_slack = subtract(
        corrected_low, scale(eye(low_dimension), claimed_floor)
    )
    _, corrected_pivots = ldl_positive_definite(
        corrected_slack, "corrected low-block floor slack"
    )
    if gamma < claimed_floor:
        raise CertificateError("gamma lies below the claimed midpoint floor")

    ambient_floor = claimed_floor - operator_radius
    scalar_diagnostics: dict[str, Any] | None = None
    if low_dimension == 1:
        dual_residual_squared = correction[0][0]
        scalar_diagnostics = {
            "dual_residual_squared": fj(dual_residual_squared),
            "energy_penalty": fj(dual_residual_squared / h),
            "distance_ratio_squared": fj(dual_residual_squared / (h * h)),
            "corrected_low_scalar": fj(corrected_low[0][0]),
        }

    proof_object = {
        "classification": classification,
        "low_dimension": low_dimension,
        "complement_dimension": complement_dimension,
        "gamma": fj(gamma),
        "h": fj(h),
        "claimed_midpoint_floor": fj(claimed_floor),
        "operator_radius": fj(operator_radius),
        "M_pivots": [fj(value) for value in m_pivots],
        "complement_slack_pivots": [fj(value) for value in complement_pivots],
        "corrected_low_block": matrix_json(corrected_low),
        "corrected_floor_pivots": [fj(value) for value in corrected_pivots],
    }
    digest = canonical_sha(proof_object)
    verdict = (
        "CERTIFIED_NONNEGATIVE_AMBIENT_FLOOR"
        if ambient_floor >= 0
        else "CERTIFIED_AMBIENT_LOWER_FLOOR"
    )
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "analytic_claim": "L-14308",
        "low_dimension": low_dimension,
        "complement_dimension": complement_dimension,
        "gamma": fj(gamma),
        "h": fj(h),
        "claimed_midpoint_floor": fj(claimed_floor),
        "operator_radius": fj(operator_radius),
        "certified_ambient_floor": fj(ambient_floor),
        "M_pivots": [fj(value) for value in m_pivots],
        "complement_slack_pivots": [fj(value) for value in complement_pivots],
        "corrected_low_block": matrix_json(corrected_low),
        "corrected_floor_pivots": [fj(value) for value in corrected_pivots],
        "scalar_diagnostics": scalar_diagnostics,
        "exact_proof_object_sha256": digest,
        "verdict": verdict,
        "proof_boundary": (
            "Exact rational block algebra. Any RIEMANN_WEIL_DIRECTED interpretation "
            "also requires the separately bound ambient operator/form radius and "
            "the analytic/domain gates of L-14308."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(raw)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(
            json.dumps({"verified": False, "error": str(exc)}, indent=2),
            file=sys.stderr,
        )
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
