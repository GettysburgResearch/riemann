#!/usr/bin/env python3
"""Exact algebra for one positive-node extension of direct-xi response moments.

This module performs no xi, zeta, logarithm, or floating-point evaluation. It
consumes the directed old monomial-moment table, takes exact rational midpoints
for discovery, derives the two Schur gates for an added rational node w>0, and
exports the exact reduced one-new-point replay coefficients.

The midpoint gates are discovery objects. A mathematical verdict requires a
directed interval for the new primitive and contraction with the original old
moment intervals, as described by L-9314/L-9315.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path
from typing import Any, Iterable, Sequence

BASIS_SCHEMA = "riemann.x9307-simplicial-portfolio-basis.directed-decimal.v1"
OUTPUT_SCHEMA = "riemann.x9312-positive-anchor-gate.midpoint-rational.v1"


class GateError(ValueError):
    """Malformed input or singular exact gate."""


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise GateError("reversed interval")

    @property
    def midpoint(self) -> Fraction:
        return (self.lower + self.upper) / 2

    @property
    def width(self) -> Fraction:
        return self.upper - self.lower


def parse_anchor(text: str) -> Fraction:
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise GateError(f"invalid rational anchor {text!r}") from exc
    if value <= 0:
        raise GateError("anchor must be positive")
    return value


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def decimal_string(value: Fraction, digits: int = 70) -> str:
    with localcontext() as ctx:
        ctx.prec = digits
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def load_basis(path: Path) -> tuple[dict[str, Any], list[Interval]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GateError(f"cannot load {path}: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema") != BASIS_SCHEMA:
        raise GateError("unsupported basis schema")
    rows = data.get("basis_rows")
    if not isinstance(rows, list) or len(rows) < 3:
        raise GateError("basis_rows must contain at least three rows")
    intervals: list[Interval] = []
    for expected, row in enumerate(rows):
        if not isinstance(row, dict) or row.get("degree") != expected:
            raise GateError("basis rows must have consecutive degrees")
        try:
            intervals.append(
                Interval(
                    Fraction(row["lower_exact_decimal"]),
                    Fraction(row["upper_exact_decimal"]),
                )
            )
        except (KeyError, ValueError, ZeroDivisionError) as exc:
            raise GateError("invalid exact decimal endpoint") from exc
    return data, intervals


def exact_solve(
    matrix: Sequence[Sequence[Fraction]], rhs: Sequence[Fraction]
) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or len(rhs) != n or any(len(row) != n for row in matrix):
        raise GateError("exact_solve dimension mismatch")
    augmented = [list(matrix[i]) + [rhs[i]] for i in range(n)]
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if augmented[row][column]), None
        )
        if pivot is None:
            raise GateError("singular exact matrix")
        if pivot != column:
            augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        for j in range(column, n + 1):
            augmented[column][j] /= pivot_value
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                for j in range(column, n + 1):
                    augmented[row][j] -= factor * augmented[column][j]
    return [augmented[i][n] for i in range(n)]


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    if len(left) != len(right):
        raise GateError("dot dimension mismatch")
    return sum((x * y for x, y in zip(left, right)), Fraction(0))


def ldl_pivots(matrix: Sequence[Sequence[Fraction]]) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise GateError("LDL matrix must be square")
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = [Fraction(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivots[i] = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivots[i] <= 0:
            raise GateError(f"nonpositive exact LDL pivot {i}")
        for j in range(i + 1, n):
            numerator = matrix[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivots[i]
    return pivots


def positive_anchor_gate(
    old_moments: Sequence[Fraction], anchor: Fraction
) -> dict[str, Any]:
    """Return the exact midpoint Schur gate for a degree-2m old table."""
    if anchor <= 0:
        raise GateError("anchor must be positive")
    if len(old_moments) < 3 or len(old_moments) % 2 == 0:
        raise GateError("expected an odd number 2m+1 of old moments")
    m = (len(old_moments) - 1) // 2
    a = list(old_moments)

    r0 = a[:m]
    c0 = [
        [a[i + j + 1] + anchor * a[i + j] for j in range(m)]
        for i in range(m)
    ]
    r1 = a[1 : m + 1]
    c1 = [
        [a[i + j + 2] + anchor * a[i + j + 1] for j in range(m)]
        for i in range(m)
    ]

    pivots0 = ldl_pivots(c0)
    pivots1 = ldl_pivots(c1)
    solve0 = exact_solve(c0, r0)
    solve1 = exact_solve(c1, r1)
    lower = dot(r0, solve0)
    upper = (a[0] - dot(r1, solve1)) / anchor
    if lower > upper:
        raise GateError("empty positive-anchor Schur interval")

    return {
        "m": m,
        "lower": lower,
        "upper": upper,
        "lower_solve": solve0,
        "upper_solve": solve1,
        "c0_pivots": pivots0,
        "c1_pivots": pivots1,
    }


def augmented_moments(
    old_moments: Sequence[Fraction], anchor: Fraction, b0: Fraction
) -> list[Fraction]:
    result = [b0]
    for value in old_moments:
        result.append(value - anchor * result[-1])
    return result


def polynomial_multiply(
    left: Sequence[Fraction], right: Sequence[Fraction]
) -> list[Fraction]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
    return output


def polynomial_add(
    left: Sequence[Fraction], right: Sequence[Fraction]
) -> list[Fraction]:
    output = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        output[i] += value
    for i, value in enumerate(right):
        output[i] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def response_polynomial(
    nodes: Sequence[Fraction], beta: Sequence[Fraction]
) -> list[Fraction]:
    if len(nodes) != len(beta):
        raise GateError("response vector length mismatch")
    output = [Fraction(0)]
    for i, coefficient in enumerate(beta):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = polynomial_multiply(term, [node, Fraction(1)])
        output = polynomial_add(output, [-coefficient * value for value in term])
    return output


def response_basis_vector(
    nodes: Sequence[Fraction], degree: int
) -> list[Fraction]:
    if degree < 0 or degree > len(nodes) - 2:
        raise GateError("response degree outside zero-sum range")
    output: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        output.append(-((-node) ** degree) / denominator)
    return output


def reduced_replay(
    nodes: Sequence[Fraction], anchor: Fraction, reference_index: int = 0
) -> dict[str, Any]:
    """Return exact one-new-point replay coefficients for response 1."""
    if anchor <= 0 or anchor in nodes:
        raise GateError("anchor must be positive and distinct from old nodes")
    if not (0 <= reference_index < len(nodes)):
        raise GateError("reference index outside node list")
    augmented = [anchor, *nodes]
    beta = response_basis_vector(augmented, 0)
    beta_anchor = beta[0]
    old_beta = beta[1:]
    gamma = list(old_beta)
    gamma[reference_index] += beta_anchor
    if sum(gamma, Fraction(0)) != 0:
        raise AssertionError("reduced old vector is not zero-sum")
    polynomial = response_polynomial(nodes, gamma)
    if len(polynomial) > len(nodes) - 1:
        raise AssertionError("reduced response degree is too large")
    return {
        "beta_anchor": beta_anchor,
        "augmented_beta": beta,
        "old_zero_sum_beta": gamma,
        "old_response_coefficients": polynomial,
        "reference_index": reference_index,
    }


def infer_nodes(data: dict[str, Any]) -> list[Fraction]:
    ids = data.get("node_ids")
    if not isinstance(ids, list) or len(ids) < 2:
        raise GateError("basis node_ids missing")
    nodes: list[Fraction] = []
    for item in ids:
        if not isinstance(item, str) or not item.startswith("x-"):
            raise GateError("only x-k dyadic node IDs are supported")
        try:
            bit = int(item[2:])
        except ValueError as exc:
            raise GateError("malformed x-k node ID") from exc
        if bit < 0:
            raise GateError("negative x bit")
        nodes.append(Fraction(1, 1 << (2 * bit)))
    if len(set(nodes)) != len(nodes):
        raise GateError("duplicate inferred node")
    return nodes


def build_result(
    data: dict[str, Any], intervals: Sequence[Interval], anchor: Fraction
) -> dict[str, Any]:
    midpoints = [value.midpoint for value in intervals]
    gate = positive_anchor_gate(midpoints, anchor)
    nodes = infer_nodes(data)
    replay = reduced_replay(nodes, anchor)
    beta_abs = abs(replay["beta_anchor"])
    old_width = sum(
        abs(coefficient) * interval.width
        for coefficient, interval in zip(
            replay["old_response_coefficients"], intervals
        )
    )
    gate_width = gate["upper"] - gate["lower"]

    return {
        "schema": OUTPUT_SCHEMA,
        "classification": (
            "EXACT_RATIONAL_ALGEBRA_ON_DIRECTED_MOMENT_MIDPOINTS_DISCOVERY_ONLY"
        ),
        "analytic_claims": ["L-9314", "L-9315"],
        "anchor": fraction_json(anchor),
        "old_degree": len(midpoints) - 1,
        "new_degree": len(midpoints),
        "gate": {
            "lower": fraction_json(gate["lower"]),
            "upper": fraction_json(gate["upper"]),
            "width": fraction_json(gate_width),
            "lower_decimal": decimal_string(gate["lower"]),
            "upper_decimal": decimal_string(gate["upper"]),
            "width_decimal": decimal_string(gate_width),
        },
        "adapted_blocks": {
            "c0_exact_ldl_pivots": [
                fraction_json(x) for x in gate["c0_pivots"]
            ],
            "c1_exact_ldl_pivots": [
                fraction_json(x) for x in gate["c1_pivots"]
            ],
            "lower_schur_solve": [
                fraction_json(x) for x in gate["lower_solve"]
            ],
            "upper_schur_solve": [
                fraction_json(x) for x in gate["upper_solve"]
            ],
        },
        "reduced_replay": {
            "reference_node_id": data["node_ids"][replay["reference_index"]],
            "reference_u": fraction_json(nodes[replay["reference_index"]]),
            "beta_anchor": fraction_json(replay["beta_anchor"]),
            "beta_anchor_decimal": decimal_string(replay["beta_anchor"]),
            "old_response_coefficients": [
                fraction_json(value)
                for value in replay["old_response_coefficients"]
            ],
            "old_moment_box_width_bound": fraction_json(old_width),
            "old_moment_box_width_decimal": decimal_string(old_width),
            "gate_width_in_new_primitive_units": fraction_json(
                gate_width / beta_abs
            ),
            "gate_width_in_new_primitive_units_decimal": decimal_string(
                gate_width / beta_abs
            ),
        },
        "source": {
            "basis_schema": data.get("schema"),
            "basis_proof_object_sha256": data.get("proof_object_sha256"),
            "primitive_sha256": data.get("primitive_sha256"),
            "ordinate": data.get("ordinate"),
            "primitive_shift": data.get("primitive_shift"),
        },
        "proof_boundary": (
            "The recurrence, Schur gates, and reduced coefficients are exact. "
            "The displayed gate uses exact midpoints of directed old-moment "
            "intervals and is a discovery ranking only. A counterexample requires "
            "a directed new direct-xi rectangle and an exact interval contraction "
            "strictly outside the gate."
        ),
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("basis", type=Path)
    parser.add_argument(
        "--anchor", required=True, help="positive rational u node, e.g. 4 or 3/2"
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    data, intervals = load_basis(args.basis)
    result = build_result(data, intervals, parse_anchor(args.anchor))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
