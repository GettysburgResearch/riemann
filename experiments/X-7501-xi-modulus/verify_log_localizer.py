#!/usr/bin/env python3
"""Exact checker for L-7503 integer-power logarithmic divided differences."""
from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from pathlib import Path
from typing import Any

from verify_modulus_certificate import (
    CertificateError,
    Interval,
    NORMALIZATION,
    ij,
    parse_points,
)

SCHEMA = "riemann.xi-modulus-witness.v1"


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def primitive_oriented_coefficients(nodes: list[Fraction]) -> list[int]:
    n = len(nodes) - 1
    if n < 1:
        raise CertificateError("a logarithmic localizer needs at least two nodes")
    if any(nodes[i] >= nodes[i + 1] for i in range(n)):
        raise CertificateError("localizer nodes must be strictly increasing")
    orientation = 1 if (n - 1) % 2 == 0 else -1
    rational_coefficients: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= node - other
        rational_coefficients.append(Fraction(orientation, 1) / denominator)
    common_denominator = 1
    for coefficient in rational_coefficients:
        common_denominator = lcm(common_denominator, coefficient.denominator)
    integers = [int(coefficient * common_denominator) for coefficient in rational_coefficients]
    common_gcd = reduce(math.gcd, (abs(value) for value in integers if value), 0)
    if common_gcd <= 0:
        raise CertificateError("zero localizer coefficient vector")
    integers = [value // common_gcd for value in integers]
    if sum(integers) != 0:
        raise CertificateError("localizer coefficients do not annihilate constants")
    return integers


def product_interval(values: list[Interval], powers: list[int], positive: bool) -> Interval:
    result = Interval(Fraction(1), Fraction(1))
    for value, power in zip(values, powers):
        exponent = power if positive else -power
        if exponent > 0:
            result = result.mul(value.pow_nonnegative(exponent))
    return result


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
    raw_rows = data.get("log_rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("log_rows must be a nonempty list")

    outputs: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"log_rows[{index}] must be an object")
        identifier = raw.get("id")
        ids = raw.get("points")
        if not isinstance(identifier, str) or not identifier:
            raise CertificateError("localizer row ID must be nonempty")
        if not isinstance(ids, list) or len(ids) < 2 or any(item not in points for item in ids):
            raise CertificateError(f"bad point list in {identifier}")
        nodes = [points[item]["u"] for item in ids]
        values = [points[item]["h"] for item in ids]
        coefficients = primitive_oriented_coefficients(nodes)
        left = product_interval(values, coefficients, True)
        right = product_interval(values, coefficients, False)
        difference = left.sub(right)
        outputs.append(
            {
                "id": identifier,
                "order": len(ids) - 1,
                "points": ids,
                "primitive_integer_coefficients": coefficients,
                "coefficient_sum": sum(coefficients),
                "left_product_interval": ij(left),
                "right_product_interval": ij(right),
                "difference_interval": ij(difference),
                "status": row_status(difference),
            }
        )

    negative = [row for row in outputs if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in outputs if row["status"] == "UNRESOLVED"]
    if classification == "RIEMANN_XI_DIRECTED" and negative:
        verdict = "NEGATIVE_RIEMANN_XI_LOG_LOCALIZER_PENDING_ANALYTIC_REVIEW"
    elif classification == "SYNTHETIC_MODEL" and negative:
        verdict = "SYNTHETIC_NEGATIVE_CONTROL"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_LOG_ROWS"

    return {
        "schema": "riemann.xi-modulus-log-localizer-verification.v1",
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "ordinate": {
            "numerator": ordinate.numerator,
            "denominator": ordinate.denominator,
        },
        "rows": outputs,
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "Exact rectangle contraction only. A Riemann-xi negative requires directed "
            "primitive reproduction and independent review of L-7501--L-7503."
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
