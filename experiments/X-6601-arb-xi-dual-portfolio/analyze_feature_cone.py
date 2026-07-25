#!/usr/bin/env python3
"""Exact rational replay of the proof-grade Issue #39 value feature table.

The input is an immutable ``riemann.xi-passivity-value-balls.v1`` certificate.
For every exact ordinate block this checker:

* intersects the two directed assemblies for every primitive Re(xi'/xi) value;
* reconstructs scalar, all pairwise A/B, every alternating divided difference,
  and every barycentric Pick row on the eight-node ladder;
* adds matched-pole Pick rows on rational model cells whenever the midpoint Pick
  matrix is not already exactly positive definite;
* constructs the full rational midpoint Pick matrix and checks exact LDL pivots;
* checks every cross-Loewner minor on disjoint increasing node lists;
* emits either a strict negative row, an unresolved escalation target, or an
  exact feasible anchor obstructing every conic portfolio on the declared block.

Only finite rational arithmetic is used after JSON parsing.  The script does not
evaluate a special function or promote any parent RH implication.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

SCHEMA = "riemann.xi-feature-cone-search.v1"
T0 = Fraction(20225875608343121406355, 2**32)


def parse_int(value: object) -> int:
    if isinstance(value, bool):
        raise ValueError("boolean is not an integer")
    return int(value)


def parse_dyadic(raw: dict[str, object]) -> Fraction:
    mantissa = parse_int(raw["mantissa"])
    exponent = parse_int(raw["exponent"])
    return Fraction(mantissa << exponent, 1) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))


def parse_fraction(raw: dict[str, object]) -> Fraction:
    return Fraction(parse_int(raw["numerator"]), parse_int(raw["denominator"]))


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primitive_real_interval(point: dict[str, object]) -> tuple[Fraction, Fraction]:
    via_xi = point["f_via_xi"]["real"]
    via_parts = point["f_via_parts"]["real"]
    lower = max(parse_dyadic(via_xi["lower"]), parse_dyadic(via_parts["lower"]))
    upper = min(parse_dyadic(via_xi["upper"]), parse_dyadic(via_parts["upper"]))
    if lower > upper:
        raise ValueError(f"disjoint directed assemblies at {point['id']}")
    return lower, upper


def interval_linear_score(
    coefficients: tuple[Fraction, ...],
    intervals: list[tuple[Fraction, Fraction]],
) -> tuple[Fraction, Fraction]:
    lower = Fraction(0)
    upper = Fraction(0)
    for coefficient, (left, right) in zip(coefficients, intervals):
        if coefficient >= 0:
            lower += coefficient * left
            upper += coefficient * right
        else:
            lower += coefficient * right
            upper += coefficient * left
    return lower, upper


def two_channel_a(nodes: list[Fraction], i: int, j: int) -> tuple[Fraction, ...]:
    denominator = nodes[j] ** 2 - nodes[i] ** 2
    result = [Fraction(0) for _ in nodes]
    result[i] = 1 / (nodes[i] * denominator)
    result[j] = -1 / (nodes[j] * denominator)
    return tuple(result)


def two_channel_b(nodes: list[Fraction], i: int, j: int) -> tuple[Fraction, ...]:
    denominator = nodes[j] ** 2 - nodes[i] ** 2
    result = [Fraction(0) for _ in nodes]
    result[i] = -nodes[i] / denominator
    result[j] = nodes[j] / denominator
    return tuple(result)


def divided_difference(
    nodes: list[Fraction], indices: tuple[int, ...]
) -> tuple[Fraction, ...]:
    order = len(indices) - 1
    orientation = -1 if (order - 1) % 2 else 1
    squared = [node * node for node in nodes]
    result = [Fraction(0) for _ in nodes]
    for i in indices:
        denominator = Fraction(1)
        for j in indices:
            if i != j:
                denominator *= squared[i] - squared[j]
        result[i] = orientation * nodes[i] / denominator
    return tuple(result)


def barycentric_vector(
    nodes: list[Fraction], indices: tuple[int, ...]
) -> tuple[Fraction, ...]:
    result = [Fraction(0) for _ in nodes]
    for i in indices:
        denominator = Fraction(1)
        for j in indices:
            if i != j:
                denominator *= nodes[i] - nodes[j]
        result[i] = 1 / denominator
    return tuple(result)


def matched_pole_vector(
    nodes: list[Fraction], indices: tuple[int, ...], model_d: Fraction
) -> tuple[Fraction, ...]:
    weights = [Fraction(0) for _ in nodes]
    for i in indices:
        denominator = Fraction(1)
        for j in indices:
            if i != j:
                denominator *= nodes[i] - nodes[j]
        weights[i] = 1 / denominator

    alpha = [Fraction(0) for _ in nodes]
    for i in indices:
        if nodes[i] ** 2 == model_d:
            raise ValueError("matched-pole model hits a node square")
        alpha[i] = nodes[i] / (nodes[i] ** 2 - model_d)

    s0 = sum((weights[i] * alpha[i] for i in indices), Fraction(0))
    s1 = sum((weights[i] * nodes[i] * alpha[i] for i in indices), Fraction(0))
    product = Fraction(1)
    for i in indices:
        product *= nodes[i] ** 2 - model_d

    result = [Fraction(0) for _ in nodes]
    for i in indices:
        result[i] = product * weights[i] * (s1 - s0 * nodes[i])
    if not any(result):
        raise ValueError("matched-pole vector vanished")
    return tuple(result)


def pick_contraction(
    nodes: list[Fraction], vector: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    result: list[Fraction] = []
    for x_i, c_i in zip(nodes, vector):
        inner = sum(
            (c_j / (x_i + x_j) for x_j, c_j in zip(nodes, vector)),
            Fraction(0),
        )
        result.append(2 * c_i * inner)
    return tuple(result)


def pick_matrix(
    nodes: list[Fraction], values: list[Fraction]
) -> list[list[Fraction]]:
    return [
        [
            (values[i] + values[j]) / (nodes[i] + nodes[j])
            for j in range(len(nodes))
        ]
        for i in range(len(nodes))
    ]


def exact_ldl_pivots(matrix: list[list[Fraction]]) -> list[Fraction]:
    size = len(matrix)
    lower = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    diagonal: list[Fraction] = []
    for i in range(size):
        lower[i][i] = Fraction(1)
    for j in range(size):
        pivot = matrix[j][j] - sum(
            (lower[j][k] ** 2 * diagonal[k] for k in range(j)), Fraction(0)
        )
        diagonal.append(pivot)
        if pivot == 0:
            return diagonal
        for i in range(j + 1, size):
            lower[i][j] = (
                matrix[i][j]
                - sum(
                    (
                        lower[i][k] * lower[j][k] * diagonal[k]
                        for k in range(j)
                    ),
                    Fraction(0),
                )
            ) / pivot
    return diagonal


def bareiss_determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    if size == 0:
        return Fraction(1)
    work = [row[:] for row in matrix]
    sign = 1
    previous = Fraction(1)
    for k in range(size - 1):
        if work[k][k] == 0:
            swap = next(
                (i for i in range(k + 1, size) if work[i][k] != 0), None
            )
            if swap is None:
                return Fraction(0)
            work[k], work[swap] = work[swap], work[k]
            sign = -sign
        pivot = work[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                work[i][j] = (
                    work[i][j] * pivot - work[i][k] * work[k][j]
                ) / previous
        previous = pivot
    return sign * work[-1][-1]


def loewner_entry(
    nodes: list[Fraction], values: list[Fraction], i: int, j: int
) -> Fraction:
    return (nodes[i] * values[i] - nodes[j] * values[j]) / (
        nodes[i] ** 2 - nodes[j] ** 2
    )


def analyze(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    groups: dict[Fraction, list[tuple[Fraction, Fraction, Fraction, str]]] = defaultdict(list)
    for point in data["points"]:
        x = parse_fraction(point["x"])
        t = parse_fraction(point["t"])
        lower, upper = primitive_real_interval(point)
        groups[t].append((x, lower, upper, point["id"]))

    total_rows = 0
    unresolved: list[tuple[object, ...]] = []
    negative: list[tuple[object, ...]] = []
    tight: list[tuple[object, ...]] = []
    anchor_failures: list[dict[str, object]] = []
    height_records: list[dict[str, object]] = []

    for t, raw_points in sorted(groups.items()):
        raw_points.sort()
        nodes = [record[0] for record in raw_points]
        intervals = [(record[1], record[2]) for record in raw_points]
        midpoints = [(left + right) / 2 for left, right in intervals]

        rows: list[tuple[str, tuple[Fraction, ...], str]] = []
        for i in range(len(nodes)):
            coefficient = [Fraction(0) for _ in nodes]
            coefficient[i] = Fraction(1)
            rows.append((f"scalar-{i}", tuple(coefficient), "scalar"))
        for i, j in itertools.combinations(range(len(nodes)), 2):
            rows.append((f"A-{i}-{j}", two_channel_a(nodes, i, j), "two-channel-A"))
            rows.append((f"B-{i}-{j}", two_channel_b(nodes, i, j), "two-channel-B/secant"))
        for size in range(3, len(nodes) + 1):
            for indices in itertools.combinations(range(len(nodes)), size):
                label = "-".join(map(str, indices))
                rows.append((f"dd-{label}", divided_difference(nodes, indices), "bernstein-divided-difference"))
        for size in range(2, len(nodes) + 1):
            for indices in itertools.combinations(range(len(nodes)), size):
                label = "-".join(map(str, indices))
                rows.append((f"bary-{label}", pick_contraction(nodes, barycentric_vector(nodes, indices)), "barycentric-pick"))

        local: list[tuple[Fraction, Fraction, Fraction, str, str]] = []

        def evaluate_rows(row_block: list[tuple[str, tuple[Fraction, ...], str]]) -> None:
            nonlocal total_rows
            total_rows += len(row_block)
            for name, coefficients, kind in row_block:
                scale = sum((abs(value) for value in coefficients), Fraction(0))
                if scale == 0:
                    continue
                normalized = tuple(value / scale for value in coefficients)
                lower, upper = interval_linear_score(normalized, intervals)
                midpoint = sum(
                    (value * center for value, center in zip(normalized, midpoints)),
                    Fraction(0),
                )
                record = (upper, lower, midpoint, name, kind)
                local.append(record)
                if upper < 0:
                    negative.append((t,) + record)
                elif lower < 0:
                    unresolved.append((t,) + record)

        evaluate_rows(rows)
        pick = pick_matrix(nodes, midpoints)
        pivots = exact_ldl_pivots(pick)
        pick_positive_definite = len(pivots) == len(nodes) and all(pivot > 0 for pivot in pivots)

        # A positive-definite full Pick anchor subsumes every fixed vector,
        # matched-pole vector, and finite PSD Gram multiplier.  We generate
        # explicit matched-pole cell rows only when this universal anchor fails.
        if not pick_positive_definite:
            model_cells = [
                (nodes[k] ** 2 + nodes[k + 1] ** 2) / 2
                for k in range(len(nodes) - 1)
            ]
            matched: list[tuple[str, tuple[Fraction, ...], str]] = []
            for size in range(2, len(nodes) + 1):
                for indices in itertools.combinations(range(len(nodes)), size):
                    label = "-".join(map(str, indices))
                    for cell, model_d in enumerate(model_cells):
                        vector = matched_pole_vector(nodes, indices, model_d)
                        matched.append((f"matched-{label}-d{cell}", pick_contraction(nodes, vector), "matched-pole-pick"))
            evaluate_rows(matched)

        local.sort(key=lambda record: record[0])
        tight.extend((t,) + record for record in local[:5])
        scalar_positive = all(value > 0 for value in midpoints)
        generated_nonnegative = all(record[2] >= 0 for record in local)

        minimum_minor: Fraction | None = None
        minimum_minor_nodes: tuple[tuple[int, ...], tuple[int, ...]] | None = None
        negative_minor_count = 0
        minor_count = 0
        size = len(nodes)
        for order in range(1, size // 2 + 1):
            for row_indices in itertools.combinations(range(size), order):
                remaining = [index for index in range(size) if index not in row_indices]
                for column_indices in itertools.combinations(remaining, order):
                    matrix = [
                        [
                            loewner_entry(nodes, midpoints, i, j)
                            for j in column_indices
                        ]
                        for i in row_indices
                    ]
                    determinant = bareiss_determinant(matrix)
                    minor_count += 1
                    if minimum_minor is None or determinant < minimum_minor:
                        minimum_minor = determinant
                        minimum_minor_nodes = (row_indices, column_indices)
                    if determinant < 0:
                        negative_minor_count += 1

        feasible_anchor = (
            pick_positive_definite
            and scalar_positive
            and generated_nonnegative
            and negative_minor_count == 0
        )
        offset_index = int((t - T0) * 32)
        if not feasible_anchor:
            anchor_failures.append(
                {
                    "j": offset_index,
                    "pick_positive_definite": pick_positive_definite,
                    "scalar_positive": scalar_positive,
                    "generated_nonnegative": generated_nonnegative,
                    "negative_loewner_minors": negative_minor_count,
                    "minimum_pick_pivot": fraction_json(min(pivots)),
                    "minimum_loewner_minor": fraction_json(minimum_minor),
                }
            )
        height_records.append(
            {
                "j": offset_index,
                "pick_midpoint_positive_definite": pick_positive_definite,
                "minimum_pick_ldl_pivot": fraction_json(min(pivots)),
                "generated_row_count": len(local),
                "generated_midpoints_nonnegative": generated_nonnegative,
                "cross_loewner_minors_checked": minor_count,
                "minimum_cross_loewner_minor": fraction_json(minimum_minor),
                "minimum_cross_loewner_minor_nodes": [
                    list(minimum_minor_nodes[0]),
                    list(minimum_minor_nodes[1]),
                ],
                "feasible_anchor": feasible_anchor,
                "tightest_row": {
                    "id": local[0][3],
                    "kind": local[0][4],
                    "lower": fraction_json(local[0][1]),
                    "upper": fraction_json(local[0][0]),
                    "midpoint": fraction_json(local[0][2]),
                },
            }
        )

    tight.sort(key=lambda record: record[1])
    complete = not anchor_failures
    return {
        "schema": SCHEMA,
        "input": {
            "path": path.name,
            "sha256": sha256(path),
            "producer_precision_bits": data.get("producer", {}).get("precision_bits"),
            "point_count": len(data["points"]),
        },
        "counts": {
            "height_count": len(groups),
            "generated_row_count": total_rows,
            "certified_negative_rows": len(negative),
            "unresolved_rows": len(unresolved),
            "feasible_anchor_heights": sum(record["feasible_anchor"] for record in height_records),
        },
        "conic_result": (
            "NO_SEPARATOR_OVER_DECLARED_VALUE_LIBRARY"
            if complete
            else "SEPARATOR_NOT_FOUND_ANCHOR_INCOMPLETE"
        ),
        "reason": (
            "At every height a rational midpoint lies in every primitive interval, "
            "the full Pick cone, every generated scalar row, and every enumerated "
            "cross-Loewner condition. L-6601 therefore rules out every robustly "
            "negative conic portfolio on the declared value-only table."
            if complete
            else "Some rational midpoints fail exact finite-cone feasibility; the "
            "corresponding near-null blocks require higher precision or direct "
            "separator replay."
        ),
        "tightest_rows": [
            {
                "j": int((t - T0) * 32),
                "id": name,
                "kind": kind,
                "lower": fraction_json(lower),
                "upper": fraction_json(upper),
                "midpoint": fraction_json(midpoint),
            }
            for t, upper, lower, midpoint, name, kind in tight[:30]
        ],
        "anchor_failures": anchor_failures,
        "heights": height_records,
        "proof_boundary": (
            "Exact rational replay of supplied primitive rectangles and a finite "
            "value-only localizer library. Jet-only differential and shifted-"
            "Stieltjes claims require derivative features and are not silently "
            "inferred from value samples. Parent RH implications, special-function "
            "soundness, and independent implementation remain separate gates."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = analyze(args.certificate)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
