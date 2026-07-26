#!/usr/bin/env python3
"""Exact rational verifier for the L-9310 half-line SOS moment certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x9307-simplicial-portfolio-basis.directed-decimal.v1"
OUTPUT_SCHEMA = "riemann.x9308-halfline-sos-moment-closure.v1"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def fraction_json_string(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def decimal_string(value: Fraction, digits: int = 80) -> str:
    getcontext().prec = digits
    return str(Decimal(value.numerator) / Decimal(value.denominator))


def parse_decimal_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, str) or not value:
        raise CertificateError(f"{name} must be a nonempty exact decimal string")
    try:
        parsed = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid exact decimal at {name}") from exc
    return parsed


def load_basis(path: Path) -> tuple[dict[str, Any], list[Fraction], list[Fraction]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot load basis file: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise CertificateError("unsupported basis schema")
    rows = data.get("basis_rows")
    if not isinstance(rows, list) or not rows:
        raise CertificateError("basis_rows must be nonempty")
    lower: list[Fraction] = []
    upper: list[Fraction] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise CertificateError(f"basis_rows[{index}] must be an object")
        degree = exact_int(row.get("degree"), f"basis_rows[{index}].degree")
        if degree != index:
            raise CertificateError("basis degrees must be consecutive from zero")
        lo = parse_decimal_fraction(
            row.get("lower_exact_decimal"),
            f"basis_rows[{index}].lower_exact_decimal",
        )
        hi = parse_decimal_fraction(
            row.get("upper_exact_decimal"),
            f"basis_rows[{index}].upper_exact_decimal",
        )
        if lo > hi:
            raise CertificateError("basis interval is reversed")
        lower.append(lo)
        upper.append(hi)
    if int(data.get("basis_row_count", -1)) != len(rows):
        raise CertificateError("basis_row_count mismatch")
    return data, lower, upper


def hankel(values: list[Fraction], size: int, offset: int = 0) -> list[list[Fraction]]:
    if size < 1:
        return []
    if 2 * (size - 1) + offset >= len(values):
        raise CertificateError("insufficient moments for Hankel matrix")
    return [
        [values[i + j + offset] for j in range(size)]
        for i in range(size)
    ]


def subtract_diagonal(
    matrix: list[list[Fraction]], delta: Fraction
) -> list[list[Fraction]]:
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
                lower[j][k] * lower[i][k] * pivots[k]
                for k in range(i)
            )
            lower[j][i] = numerator / pivots[i]
    return pivots


def maximum_row_sum(matrix: list[list[Fraction]]) -> Fraction:
    if not matrix:
        return Fraction(0)
    return max(sum(abs(value) for value in row) for row in matrix)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path, delta: Fraction) -> dict[str, Any]:
    if delta <= 0:
        raise CertificateError("delta must be positive")
    data, lower, upper = load_basis(path)
    degree = len(lower) - 1
    midpoints = [(lo + hi) / 2 for lo, hi in zip(lower, upper)]
    radii = [(hi - lo) / 2 for lo, hi in zip(lower, upper)]

    if degree % 2 == 0:
        m = degree // 2
        h0_size = m + 1
        h1_size = m
    else:
        m = (degree - 1) // 2
        h0_size = m + 1
        h1_size = m + 1

    midpoint_h0 = hankel(midpoints, h0_size, 0)
    midpoint_h1 = hankel(midpoints, h1_size, 1)
    radius_h0 = hankel(radii, h0_size, 0)
    radius_h1 = hankel(radii, h1_size, 1)

    pivots_h0 = exact_ldl_positive_pivots(subtract_diagonal(midpoint_h0, delta))
    pivots_h1 = exact_ldl_positive_pivots(subtract_diagonal(midpoint_h1, delta))
    epsilon_h0 = maximum_row_sum(radius_h0)
    epsilon_h1 = maximum_row_sum(radius_h1)
    if epsilon_h0 >= delta or epsilon_h1 >= delta:
        raise CertificateError("interval-box row radius is not below delta")

    proof_object = {
        "delta": fraction_json_string(delta),
        "H0_pivots": [fraction_json_string(value) for value in pivots_h0],
        "H1_pivots": [fraction_json_string(value) for value in pivots_h1],
        "H0_radius": fraction_json_string(epsilon_h0),
        "H1_radius": fraction_json_string(epsilon_h1),
    }
    proof_digest = hashlib.sha256(
        json.dumps(
            proof_object,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode("ascii")
    ).hexdigest()

    return {
        "schema": OUTPUT_SCHEMA,
        "classification": data.get("classification"),
        "analytic_claim": "L-9310",
        "parent_basis_claim": "L-9309",
        "basis_source_sha256": file_sha256(path),
        "basis_source_git_blob_sha1": "174db078d3442e89d3be458a306b1122025cfd51",
        "basis_source_certificate_sha256": data.get("source_certificate_sha256"),
        "primitive_sha256": data.get("primitive_sha256"),
        "total_count_sha256": data.get("total_count_sha256"),
        "degree_bound": degree,
        "delta": fraction_json(delta),
        "h0_dimension": h0_size,
        "h1_dimension": h1_size,
        "h0_pivot_decimals": [decimal_string(value) for value in pivots_h0],
        "h1_pivot_decimals": [decimal_string(value) for value in pivots_h1],
        "h0_maximum_row_radius": fraction_json(epsilon_h0),
        "h1_maximum_row_radius": fraction_json(epsilon_h1),
        "h0_maximum_row_radius_decimal": decimal_string(epsilon_h0),
        "h1_maximum_row_radius_decimal": decimal_string(epsilon_h1),
        "h0_uniform_positive_margin": fraction_json(delta - epsilon_h0),
        "h1_uniform_positive_margin": fraction_json(delta - epsilon_h1),
        "h0_uniform_positive_margin_decimal": decimal_string(delta - epsilon_h0),
        "h1_uniform_positive_margin_decimal": decimal_string(delta - epsilon_h1),
        "exact_proof_object_sha256": proof_digest,
        "verdict": "CERTIFIED_POSITIVE_FULL_HALF_LINE_NONNEGATIVE_POLYNOMIAL_CONE",
        "scope": (
            "Every nonzero real polynomial response P of degree at most the stated "
            "bound and nonnegative on [0,infinity) has strictly positive residual "
            "for every exact basis value admitted by the directed interval box."
        ),
        "proof_boundary": (
            "Exact rational LDL and exact interval row-radius arithmetic. The RH "
            "interpretation inherits the direct-xi canonical product, L-9308/L-9309, "
            "and the atomized total-zero-count conversion."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("basis", type=Path)
    parser.add_argument("--delta-numerator", type=int, default=1)
    parser.add_argument("--delta-denominator", type=int, default=100000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.delta_denominator <= 0:
        print(json.dumps({"verified": False, "error": "bad delta denominator"}, indent=2), file=sys.stderr)
        return 2
    try:
        result = verify(
            args.basis,
            Fraction(args.delta_numerator, args.delta_denominator),
        )
    except (OSError, CertificateError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
