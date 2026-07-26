#!/usr/bin/env python3
"""Exploratory high-order midpoint ranking on a source-bound deflated grid."""
from __future__ import annotations

import argparse
import hashlib
import heapq
import importlib.util
import itertools
import json
import math
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SCHEMA = "riemann.x9301-dense-high-order-midpoint-ranking.v2"
ROUNDING_SAFETY_FACTOR = 64.0


def import_local(name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


BUILD = import_local("build_pr71_nearest_certificate")
VERIFY = import_local("verify_zero_deflated_modulus")
SCREEN = import_local("summarize_dense_order2_screen")


class RankingError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RankingError(f"{path} must contain an object")
    return value


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def parity(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def signed_permutations(order: int) -> tuple[tuple[tuple[int, ...], int], ...]:
    return tuple(
        (permutation, parity(permutation))
        for permutation in itertools.permutations(range(order))
    )


def determinant_and_permanent_scale(
    matrix: list[list[float]],
    permutations: tuple[tuple[tuple[int, ...], int], ...] | None = None,
) -> tuple[float, float]:
    order = len(matrix)
    if (
        order < 1
        or any(len(row) != order for row in matrix)
        or any(not math.isfinite(value) for row in matrix for value in row)
    ):
        raise RankingError("matrix must be finite, square, and nonempty")
    permutations = permutations or signed_permutations(order)
    terms = [
        math.prod(matrix[row][permutation[row]] for row in range(order))
        for permutation, _ in permutations
    ]
    determinant = math.fsum(
        sign * term for term, (_, sign) in zip(terms, permutations)
    )
    scale = math.fsum(abs(term) for term in terms)
    return determinant, scale


def decimal_value(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def decimal_determinant_and_permanent_scale(
    matrix: list[list[Decimal]],
    permutations: tuple[tuple[tuple[int, ...], int], ...],
) -> tuple[Decimal, Decimal]:
    order = len(matrix)
    if order < 1 or any(len(row) != order for row in matrix):
        raise RankingError("matrix must be square and nonempty")
    terms = [
        math.prod(
            (matrix[row][permutation[row]] for row in range(order)),
            start=Decimal(1),
        )
        for permutation, _ in permutations
    ]
    determinant = sum(
        (
            Decimal(sign) * term
            for term, (_, sign) in zip(terms, permutations)
        ),
        start=Decimal(0),
    )
    scale = sum((abs(term) for term in terms), start=Decimal(0))
    return determinant, scale


def partition_count(node_count: int, order: int) -> int:
    if 2 * order > node_count:
        return 0
    return math.comb(node_count, 2 * order) * math.comb(2 * order - 1, order - 1)


def disjoint_partitions(
    node_count: int, order: int
) -> Iterable[tuple[tuple[int, ...], tuple[int, ...]]]:
    for union_indices in itertools.combinations(range(node_count), 2 * order):
        first = union_indices[0]
        for row_tail in itertools.combinations(union_indices[1:], order - 1):
            rows = (first, *row_tail)
            row_set = set(rows)
            columns = tuple(
                index for index in union_indices if index not in row_set
            )
            yield rows, columns


def relative_vandermonde(indices: tuple[int, ...], nodes: list[Fraction]) -> float:
    factors = [
        float(
            (nodes[indices[right]] - nodes[indices[left]])
            / (nodes[indices[right]] + nodes[indices[left]])
        )
        for left in range(len(indices))
        for right in range(left + 1, len(indices))
    ]
    return math.prod(factors)


def decimal_relative_vandermonde(
    indices: tuple[int, ...], nodes: list[Fraction]
) -> Decimal:
    return math.prod(
        (
            decimal_value(
                (nodes[indices[right]] - nodes[indices[left]])
                / (nodes[indices[right]] + nodes[indices[left]])
            )
            for left in range(len(indices))
            for right in range(left + 1, len(indices))
        ),
        start=Decimal(1),
    )


def sparse_source_certificate(
    primitive: dict[str, Any],
    zero_block: dict[str, Any],
    nearest_count: int,
) -> dict[str, Any]:
    point_ids = SCREEN.ordered_point_ids(primitive)
    if len(point_ids) < 4:
        raise RankingError("at least four nodes are required")
    config = {
        "schema": BUILD.CONFIG_SCHEMA,
        "normalization_id": BUILD.NORMALIZATION,
        "log_terms": 256,
        "rows": [
            {
                "id": "source-binding-anchor",
                "kind": "deflated-cross-loewner-determinant",
                "rows": list(point_ids[:2]),
                "columns": list(point_ids[2:4]),
            }
        ],
    }
    certificate = BUILD.build(primitive, zero_block, config, nearest_count)
    VERIFY.verify_source_artifacts(certificate, primitive, zero_block)
    return certificate


def push_smallest(
    heap: list[tuple[Any, int, dict[str, Any]]],
    score: Any,
    serial: int,
    entry: dict[str, Any],
    limit: int,
) -> None:
    item = (-score, serial, entry)
    if len(heap) < limit:
        heapq.heappush(heap, item)
    elif score < -heap[0][0]:
        heapq.heapreplace(heap, item)


def rank_order(
    order: int,
    point_ids: tuple[str, ...],
    nodes: list[Fraction],
    secants: list[list[Any]],
    top_k: int,
    decimal_digits: int,
) -> dict[str, Any]:
    permutations = signed_permutations(order)
    expected = partition_count(len(point_ids), order)
    top_adjusted: list[tuple[Any, int, dict[str, Any]]] = []
    top_eta: list[tuple[Any, int, dict[str, Any]]] = []
    negative_count = 0
    robust_negative_count = 0
    most_negative: list[tuple[Any, int, dict[str, Any]]] = []
    observed = 0
    geometry_cache: dict[tuple[int, ...], Any] = {}
    if decimal_digits:
        epsilon_bound: Any = (
            Decimal(ROUNDING_SAFETY_FACTOR * len(permutations))
            * Decimal(10) ** (8 - decimal_digits)
        )
        zero: Any = Decimal(0)
    else:
        epsilon_bound = (
            ROUNDING_SAFETY_FACTOR
            * len(permutations)
            * sys.float_info.epsilon
        )
        zero = 0.0

    for serial, (rows, columns) in enumerate(
        disjoint_partitions(len(point_ids), order)
    ):
        matrix = [[secants[row][column] for column in columns] for row in rows]
        if decimal_digits:
            determinant, scale = decimal_determinant_and_permanent_scale(
                matrix, permutations
            )
        else:
            determinant, scale = determinant_and_permanent_scale(
                matrix, permutations
            )
        if rows not in geometry_cache:
            geometry_cache[rows] = (
                decimal_relative_vandermonde(rows, nodes)
                if decimal_digits
                else relative_vandermonde(rows, nodes)
            )
        if columns not in geometry_cache:
            geometry_cache[columns] = (
                decimal_relative_vandermonde(columns, nodes)
                if decimal_digits
                else relative_vandermonde(columns, nodes)
            )
        geometry = geometry_cache[rows] * geometry_cache[columns]
        eta = determinant / scale if scale else zero
        adjusted = eta / geometry
        entry = {
            "rows": [point_ids[index] for index in rows],
            "columns": [point_ids[index] for index in columns],
            "determinant_midpoint": f"{determinant:.17e}",
            "permanent_normalized_midpoint": f"{eta:.17e}",
            "geometry_adjusted_midpoint": f"{adjusted:.17e}",
            "roundoff_eta_bound": f"{epsilon_bound:.17e}",
        }
        push_smallest(top_adjusted, adjusted, serial, entry, top_k)
        push_smallest(top_eta, eta, serial, entry, top_k)
        if eta < zero:
            negative_count += 1
            push_smallest(most_negative, eta, serial, entry, top_k)
            if eta < -epsilon_bound:
                robust_negative_count += 1
        observed += 1

    if observed != expected:
        raise RankingError(
            f"order {order} coverage mismatch: expected {expected}, got {observed}"
        )

    def sorted_entries(
        heap: list[tuple[Any, int, dict[str, Any]]],
        key: str,
    ) -> list[dict[str, Any]]:
        return sorted(
            (item[2] for item in heap),
            key=lambda entry: Decimal(entry[key]),
        )

    return {
        "order": order,
        "pattern_count": observed,
        "coverage_formula": (
            f"binomial({len(point_ids)}, {2 * order}) * "
            f"binomial({2 * order - 1}, {order - 1})"
        ),
        "permutation_term_count": len(permutations),
        "midpoint_decimal_digits": decimal_digits or None,
        "negative_midpoint_count": negative_count,
        "negative_beyond_roundoff_bound_count": robust_negative_count,
        "top_geometry_adjusted": sorted_entries(
            top_adjusted, "geometry_adjusted_midpoint"
        ),
        "top_permanent_normalized": sorted_entries(
            top_eta, "permanent_normalized_midpoint"
        ),
        "most_negative": sorted_entries(
            most_negative, "permanent_normalized_midpoint"
        ),
    }


def summarize(
    primitive: dict[str, Any],
    zero_block: dict[str, Any],
    nearest_count: int,
    orders: tuple[int, ...],
    top_k: int,
    decimal_digits: int = 0,
) -> dict[str, Any]:
    if (
        nearest_count <= 0
        or top_k <= 0
        or not orders
        or any(order < 2 or order > 4 for order in orders)
        or len(set(orders)) != len(orders)
        or (decimal_digits != 0 and decimal_digits < 32)
    ):
        raise RankingError("invalid nearest count, top-k, or orders")
    certificate = sparse_source_certificate(
        primitive, zero_block, nearest_count
    )
    point_ids = SCREEN.ordered_point_ids(primitive)
    points = VERIFY.parse_points(certificate, require_digests=True)
    target = SCREEN.rational(certificate["ordinate"], "certificate.ordinate")
    bins = VERIFY.parse_zero_bins(
        certificate, target, "RIEMANN_XI_DIRECTED"
    )
    terms = SCREEN.integer(certificate.get("log_terms"), "log_terms")
    values = {
        identifier: VERIFY.deflated_log_value(points[identifier], bins, terms)
        for identifier in point_ids
    }
    nodes = [points[identifier]["u"] for identifier in point_ids]
    fraction_secants: list[list[Fraction | None]] = [
        [None] * len(point_ids) for _ in point_ids
    ]
    for left, right in itertools.combinations(range(len(point_ids)), 2):
        value = VERIFY.secant(
            points[point_ids[left]],
            points[point_ids[right]],
            values[point_ids[left]],
            values[point_ids[right]],
        )
        entry = (value.lower + value.upper) / 2
        fraction_secants[left][right] = entry
        fraction_secants[right][left] = entry

    if decimal_digits:
        with localcontext() as context:
            context.prec = decimal_digits
            secants: list[list[Any]] = [
                [
                    decimal_value(value) if value is not None else Decimal("NaN")
                    for value in row
                ]
                for row in fraction_secants
            ]
            ranked_orders = [
                rank_order(
                    order,
                    point_ids,
                    nodes,
                    secants,
                    top_k,
                    decimal_digits,
                )
                for order in orders
            ]
    else:
        secants = [
            [
                float(value) if value is not None else math.nan
                for value in row
            ]
            for row in fraction_secants
        ]
        ranked_orders = [
            rank_order(order, point_ids, nodes, secants, top_k, 0)
            for order in orders
        ]
    robust_count = sum(
        item["negative_beyond_roundoff_bound_count"]
        for item in ranked_orders
    )
    result = {
        "schema": SCHEMA,
        "classification": (
            f"EXPLORATORY_DECIMAL_{decimal_digits}_MIDPOINT_ONLY"
            if decimal_digits
            else "EXPLORATORY_BINARY64_MIDPOINT_ONLY"
        ),
        "target": certificate["ordinate"],
        "precision_bits": primitive["precision_bits"],
        "nearest_count": nearest_count,
        "midpoint_decimal_digits": decimal_digits or None,
        "selection_scope": certificate["source"]["selection_scope"],
        "point_ids_in_increasing_u_order": list(point_ids),
        "point_count": len(point_ids),
        "orders": ranked_orders,
        "total_pattern_count": sum(item["pattern_count"] for item in ranked_orders),
        "robust_negative_midpoint_count": robust_count,
        "counterexample_nomination": (
            "REQUIRES_DIRECTED_INTERVAL_REPLAY" if robust_count else None
        ),
        "primitive_artifact_sha256": canonical_sha(primitive),
        "zero_block_artifact_sha256": canonical_sha(zero_block),
        "source_binding_certificate_sha256": certificate["certificate_sha256"],
        "proof_boundary": (
            "The primitive and zero source binding is exact, but every ranked "
            + (
                f"determinant uses {decimal_digits}-digit Decimal midpoints. "
                if decimal_digits
                else "determinant uses binary64 midpoints. "
            )
            + "No midpoint sign is a proof. "
            "The stated roundoff bound covers straightforward product/sum "
            "roundoff only and is a nomination threshold, not interval arithmetic."
        ),
    }
    result["summary_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitive", type=Path)
    parser.add_argument("zero_block", type=Path)
    parser.add_argument("--nearest-count", type=int, default=256)
    parser.add_argument("--orders", type=int, nargs="+", default=[3])
    parser.add_argument("--top-k", type=int, default=20)
    parser.add_argument("--decimal-digits", type=int, default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = summarize(
            load(args.primitive),
            load(args.zero_block),
            args.nearest_count,
            tuple(args.orders),
            args.top_k,
            args.decimal_digits,
        )
        code = 1 if result["counterexample_nomination"] else 0
    except (
        OSError,
        json.JSONDecodeError,
        RankingError,
        SCREEN.ScreenError,
        BUILD.BuildError,
        VERIFY.CertificateError,
        KeyError,
        OverflowError,
        ZeroDivisionError,
    ) as exc:
        result = {"schema": SCHEMA, "ranked": False, "error": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
