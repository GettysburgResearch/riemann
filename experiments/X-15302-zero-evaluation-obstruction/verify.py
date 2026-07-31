#!/usr/bin/env python3
"""Exact rational checker for L-15304 zero-evaluation packet obstruction."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15302-zero-evaluation-obstruction.v1"
OUTPUT_SCHEMA = "riemann.x15302-zero-evaluation-obstruction.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def parse_matrix(value: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(value, list) or not value:
        raise CertificateError(f"{name} must be a nonempty square matrix")
    n = len(value)
    matrix: list[list[Fraction]] = []
    for i, row in enumerate(value):
        if not isinstance(row, list) or len(row) != n:
            raise CertificateError(f"{name} must be square")
        matrix.append([
            parse_fraction(item, f"{name}[{i}][{j}]")
            for j, item in enumerate(row)
        ])
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                raise CertificateError(f"{name} is not symmetric")
    return matrix


def subtract_scaled(left: list[list[Fraction]], right: list[list[Fraction]], scale: Fraction) -> list[list[Fraction]]:
    if len(left) != len(right):
        raise CertificateError("matrix dimension mismatch")
    return [
        [left[i][j] - scale * right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def exact_ldl_positive(matrix: list[list[Fraction]], name: str) -> list[Fraction]:
    n = len(matrix)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = [Fraction(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivots[i] = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivots[i] <= 0:
            raise CertificateError(f"{name} has nonpositive LDL pivot {i}")
        for j in range(i + 1, n):
            numerator = matrix[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivots[i]
    return pivots


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    if data.get("status") != "DECLARED_CERTIFIED_ZERO_EVALUATION_PACKET":
        raise CertificateError("status does not preserve the proof boundary")
    if data.get("certified_zero_gate") is not True:
        raise CertificateError("zero set lacks its certified-zero gate")
    if data.get("common_hardy_metric") is not True:
        raise CertificateError("packet, tail, and approximation must use one Hardy metric")

    metric = parse_matrix(data.get("metric_gram"), "metric_gram")
    evaluation = parse_matrix(data.get("evaluation_gram"), "evaluation_gram")
    if len(metric) != len(evaluation):
        raise CertificateError("metric/evaluation dimension mismatch")

    sigma2 = parse_fraction(data.get("sigma_lower_squared"), "sigma_lower_squared")
    operator2 = parse_fraction(data.get("evaluation_operator_upper_squared"), "evaluation_operator_upper_squared")
    quotient = parse_fraction(data.get("quotient_lower"), "quotient_lower")
    tail = parse_fraction(data.get("tail_upper"), "tail_upper")
    claimed = parse_fraction(data.get("distance_lower"), "distance_lower")
    if min(sigma2, operator2, quotient, tail) < 0 or operator2 == 0:
        raise CertificateError("invalid nonnegative scalar data")

    metric_pivots = exact_ldl_positive(metric, "metric_gram")
    singular_pivots = exact_ldl_positive(
        subtract_scaled(evaluation, metric, sigma2),
        "evaluation_gram - sigma^2 metric_gram",
    )
    if quotient * quotient * operator2 > sigma2:
        raise CertificateError("quotient lower is not justified by squared bounds")
    distance = quotient - tail
    if distance <= 0:
        raise CertificateError("obstruction distance is not strictly positive")
    if claimed != distance:
        raise CertificateError("claimed distance lower mismatch")

    result: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "verified": True,
        "status": "CERTIFIED_POSITIVE_RADICAL_APPROXIMATION_OBSTRUCTION",
        "dimension": len(metric),
        "metric_ldl_pivots": [fraction_json(value) for value in metric_pivots],
        "singular_floor_ldl_pivots": [fraction_json(value) for value in singular_pivots],
        "sigma_lower_squared": fraction_json(sigma2),
        "evaluation_operator_upper_squared": fraction_json(operator2),
        "quotient_lower": fraction_json(quotient),
        "tail_upper": fraction_json(tail),
        "distance_lower": fraction_json(distance),
        "proof_boundary": (
            "The finite rational singular-value and distance implication is exact. "
            "The zero identities, evaluation intervals, and Hardy operator bound are external gates."
        ),
    }
    result["verification_sha256"] = canonical_sha(result)
    return result


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(load(args.certificate))
        code = 0
    except CertificateError as exc:
        result = {"schema": OUTPUT_SCHEMA, "verified": False, "status": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
