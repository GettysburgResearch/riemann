#!/usr/bin/env python3
"""Exact rational checker for L-15305 certified-zero Gram/tail floors."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15303-certified-zero-tail-floor.v1"
OUTPUT_SCHEMA = "riemann.x15303-certified-zero-tail-floor.verification.v1"


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
    encoded = json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    if data.get("status") != "DECLARED_CERTIFIED_ZERO_GRAM_TAIL_PACKET":
        raise CertificateError("status does not preserve the proof boundary")
    for gate in (
        "complete_zero_block_gate",
        "critical_line_gate",
        "autocorrelation_nonnegative_gate",
        "tail_coverage_gate",
        "common_metric_gate",
    ):
        if data.get(gate) is not True:
            raise CertificateError(f"blocking source gate: {gate}")

    metric = parse_matrix(data.get("metric_gram"), "metric_gram")
    known = parse_matrix(data.get("known_zero_gram_lower"), "known_zero_gram_lower")
    if len(metric) != len(known):
        raise CertificateError("metric/known Gram dimension mismatch")

    conjugate_factor = parse_int(data.get("conjugate_factor"), "conjugate_factor")
    if conjugate_factor not in (1, 2):
        raise CertificateError("conjugate_factor must be one or two")
    cells = data.get("tail_cells")
    if not isinstance(cells, list):
        raise CertificateError("tail_cells must be a list")
    listed = Fraction(0)
    seen_ids: set[str] = set()
    for index, cell in enumerate(cells):
        if not isinstance(cell, dict):
            raise CertificateError(f"tail_cells[{index}] must be an object")
        cell_id = cell.get("id")
        if not isinstance(cell_id, str) or not cell_id or cell_id in seen_ids:
            raise CertificateError("tail cell IDs must be unique nonempty strings")
        seen_ids.add(cell_id)
        count = parse_int(cell.get("count_upper"), f"tail_cells[{index}].count_upper")
        envelope = parse_fraction(
            cell.get("envelope_upper"), f"tail_cells[{index}].envelope_upper"
        )
        if count < 0 or envelope < 0:
            raise CertificateError("tail counts and envelopes must be nonnegative")
        listed += conjugate_factor * count * envelope

    remainder = parse_fraction(data.get("analytic_remainder"), "analytic_remainder")
    budget = parse_fraction(data.get("tail_budget_upper"), "tail_budget_upper")
    requested = parse_fraction(data.get("requested_floor"), "requested_floor")
    if min(remainder, budget, requested) < 0:
        raise CertificateError("tail and floor scalars must be nonnegative")
    composed = listed + remainder
    if composed > budget:
        raise CertificateError("composed tail exceeds declared budget")

    shifted = [
        [
            known[i][j] - (budget + requested) * metric[i][j]
            for j in range(len(metric))
        ]
        for i in range(len(metric))
    ]
    pivots = exact_ldl_positive(
        metric, "metric_gram"
    )
    floor_pivots = exact_ldl_positive(
        shifted, "known_zero_gram_lower - (tail_budget+floor) metric"
    )

    result: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "verified": True,
        "status": "CERTIFIED_POSITIVE_VISIBLE_ZERO_GRAM_FLOOR",
        "dimension": len(metric),
        "tail": {
            "listed_cell_sum": fraction_json(listed),
            "analytic_remainder": fraction_json(remainder),
            "composed_upper": fraction_json(composed),
            "declared_budget": fraction_json(budget),
            "budget_slack": fraction_json(budget - composed),
        },
        "requested_floor": fraction_json(requested),
        "metric_ldl_pivots": [fraction_json(value) for value in pivots],
        "floor_ldl_pivots": [fraction_json(value) for value in floor_pivots],
        "proof_boundary": (
            "The matrix and rational tail composition are checked exactly. "
            "Zero completeness, critical-line identity, autocorrelation positivity, "
            "and analytic tail envelopes are external source gates."
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
        result = {
            "schema": OUTPUT_SCHEMA,
            "verified": False,
            "status": "REJECTED",
            "reason": str(exc),
        }
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
