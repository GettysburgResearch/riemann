#!/usr/bin/env python3
"""Empirical sparse cross-height exchange/LP search on direct-xi primitives.

This is discovery code only. It reads exact primitive rectangles but optimizes
rectangle midpoints in ordinary floating arithmetic. Every output direction
must be frozen and passed through verify.py before it is considered globally
RH-valid, and then through directed primitive contraction before any sign claim.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
from scipy.optimize import linprog

PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class SearchError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise SearchError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value)
    raise SearchError(f"{name} must be an integer")


def fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise SearchError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise SearchError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def midpoint(value: Any, name: str) -> mp.mpf:
    if not isinstance(value, dict):
        raise SearchError(f"{name} must be an object")
    lower = fraction(value.get("lower"), f"{name}.lower")
    upper = fraction(value.get("upper"), f"{name}.upper")
    return (
        mp.mpf(lower.numerator) / lower.denominator
        + mp.mpf(upper.numerator) / upper.denominator
    ) / 2


def load_primitive(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text())
    if (
        not isinstance(data, dict)
        or data.get("schema") != PRIMITIVE_SCHEMA
        or data.get("normalization_id") != NORMALIZATION
    ):
        raise SearchError(f"{path} has the wrong schema/normalization")
    points = {}
    for raw in data.get("points", []):
        if not isinstance(raw, dict):
            continue
        identifier = raw.get("id")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(identifier, str) or not isinstance(rectangle, dict):
            continue
        x = fraction(raw.get("x"), f"{path}:{identifier}.x")
        real = midpoint(rectangle.get("real"), f"{path}:{identifier}.real")
        imag = midpoint(rectangle.get("imag"), f"{path}:{identifier}.imag")
        h = real * real + imag * imag
        if h <= 0:
            raise SearchError(f"nonpositive modulus midpoint at {path}:{identifier}")
        points[identifier] = {
            "x": x,
            "u": x * x,
            "log_h": mp.log(h),
        }
    return {
        "ordinate": fraction(data.get("ordinate"), f"{path}.ordinate"),
        "points": points,
    }


def response_row(value: float, offsets: list[float], nodes: list[float]) -> np.ndarray:
    return np.asarray(
        [np.log((value - offset) ** 2 + node) for offset in offsets for node in nodes],
        dtype=float,
    )


def make_grid(offsets: list[float], dense_points: int, tail: float) -> np.ndarray:
    pieces = [
        np.linspace(-tail, tail, dense_points),
        np.linspace(-2.0, 2.0, dense_points),
        np.linspace(-0.75, 0.75, dense_points),
    ]
    pieces.extend(
        np.linspace(offset - 0.75, offset + 0.75, dense_points)
        for offset in offsets
    )
    pieces.append(np.asarray([-10 * tail, -3 * tail, 3 * tail, 10 * tail]))
    return np.unique(np.concatenate(pieces))


def search_support(
    point_ids: tuple[str, ...],
    tables: list[dict[str, Any]],
    origin: Fraction,
    dense_points: int,
    tail: float,
) -> list[dict[str, Any]]:
    height_count = len(tables)
    size = len(point_ids)
    offsets = [float(table["ordinate"] - origin) for table in tables]
    nodes = [float(tables[0]["points"][identifier]["u"]) for identifier in point_ids]
    objective = np.asarray(
        [
            float(table["points"][identifier]["log_h"])
            for table in tables
            for identifier in point_ids
        ],
        dtype=float,
    )
    grid = make_grid(offsets, dense_points, tail)
    response = np.vstack([response_row(value, offsets, nodes) for value in grid])
    moment = np.tile(np.asarray(nodes), height_count)

    equalities = np.zeros((height_count + 1, height_count * size))
    targets = np.zeros(height_count + 1)
    for height_index in range(height_count):
        equalities[height_index, height_index * size : (height_index + 1) * size] = 1

    results = []
    for coordinate in range(height_count * size):
        for fixed_value in (-1.0, 1.0):
            equalities[-1, :] = 0
            equalities[-1, coordinate] = 1
            targets[-1] = fixed_value
            inequalities = np.vstack((-response, -moment))
            bounds = np.zeros(len(grid) + 1)
            solved = linprog(
                objective,
                A_ub=inequalities,
                b_ub=bounds,
                A_eq=equalities,
                b_eq=targets,
                bounds=[(None, None)] * (height_count * size),
                method="highs",
            )
            if not solved.success:
                continue
            direction = solved.x
            sampled = response @ direction
            results.append(
                {
                    "point_ids": list(point_ids),
                    "fixed_coordinate": coordinate,
                    "fixed_value": fixed_value,
                    "objective_midpoint": float(solved.fun),
                    "minimum_sampled_response": float(sampled.min()),
                    "minimum_sampled_at": float(grid[int(sampled.argmin())]),
                    "leading_even_asymptotic_coefficient": float(moment @ direction),
                    "coefficients_by_height": [
                        direction[index * size : (index + 1) * size].tolist()
                        for index in range(height_count)
                    ],
                }
            )
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minus", type=Path, required=True)
    parser.add_argument("--center", type=Path, required=True)
    parser.add_argument("--plus", type=Path, required=True)
    parser.add_argument("--support-size", type=int, default=3)
    parser.add_argument("--dense-points", type=int, default=1201)
    parser.add_argument("--tail", type=float, default=10.0)
    parser.add_argument("--top", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.support_size < 2 or args.dense_points < 101 or args.top < 1:
        raise SystemExit("support-size>=2, dense-points>=101 and top>=1 are required")

    mp.mp.dps = 100
    tables = [load_primitive(path) for path in (args.minus, args.center, args.plus)]
    common = set(tables[0]["points"])
    for table in tables[1:]:
        common &= set(table["points"])
    point_ids = sorted(common, key=lambda identifier: tables[0]["points"][identifier]["u"])
    if len(point_ids) < args.support_size:
        raise SearchError("too few shared point IDs")
    origin = tables[1]["ordinate"]

    rows = []
    for support in itertools.combinations(point_ids, args.support_size):
        rows.extend(
            search_support(
                support,
                tables,
                origin,
                args.dense_points,
                args.tail,
            )
        )
    rows.sort(key=lambda row: row["objective_midpoint"])
    output = {
        "schema": "riemann.x9802-sparse-exchange-reconnaissance.v1",
        "classification": "EMPIRICAL_GRID_LP_ONLY",
        "normalization_id": NORMALIZATION,
        "source_files": [str(args.minus), str(args.center), str(args.plus)],
        "origin": {"numerator": origin.numerator, "denominator": origin.denominator},
        "shared_point_count": len(point_ids),
        "support_size": args.support_size,
        "support_count": sum(1 for _ in itertools.combinations(point_ids, args.support_size)),
        "directions_solved": len(rows),
        "top_rows": rows[: args.top],
        "warning": (
            "A sampled-grid LP direction is not globally valid. Freeze promising "
            "directions to exact rationals, isolate every derivative root, and run "
            "X-9802 before interpreting the direct-xi sign."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: output[key] for key in ("support_count", "directions_solved")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
