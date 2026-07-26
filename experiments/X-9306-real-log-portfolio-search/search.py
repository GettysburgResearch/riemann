#!/usr/bin/env python3
"""Search and exactly replay L-9308 logarithmic portfolios on committed PR #103 data.

Discovery uses scipy/HiGHS. Every retained candidate is rounded to exact rational
coefficients, repaired into the monomial-positive response cone, and replayed
with Fraction-only logarithm enclosures against the committed directed xi balls
and exact atomized zero-count shells.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import linprog


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lo - other.hi, self.hi - other.lo)

    def scale(self, scalar: Fraction) -> "Interval":
        if scalar >= 0:
            return Interval(self.lo * scalar, self.hi * scalar)
        return Interval(self.hi * scalar, self.lo * scalar)


def frac(raw: dict[str, Any]) -> Fraction:
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


def parse_interval(raw: dict[str, Any]) -> Interval:
    return Interval(frac(raw["lower"]), frac(raw["upper"]))


def square_interval(value: Interval) -> Interval:
    upper = max(value.lo * value.lo, value.hi * value.hi)
    lower = Fraction(0) if value.lo <= 0 <= value.hi else min(value.lo * value.lo, value.hi * value.hi)
    return Interval(lower, upper)


def modulus_square(point: dict[str, Any]) -> Interval:
    rectangle = point["xi_rectangle"]
    return square_interval(parse_interval(rectangle["real"])).add(
        square_interval(parse_interval(rectangle["imag"]))
    )


def midpoint(value: Interval) -> Fraction:
    return (value.lo + value.hi) / 2


def log_unit_interval(x: Fraction, terms: int) -> Interval:
    if not (Fraction(1) <= x <= Fraction(2)):
        raise ValueError("internal logarithm reduction failed")
    z = (x - 1) / (x + 1)
    z2 = z * z
    power = z
    total = Fraction(0)
    for j in range(terms):
        total += power / (2 * j + 1)
        power *= z2
    lower = 2 * total
    tail = Fraction(0) if z == 0 else 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lower, lower + tail)


def log_fraction(x: Fraction, terms: int) -> Interval:
    if x <= 0:
        raise ValueError("logarithm argument must be positive")
    reduced = x
    exponent = 0
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    return log_unit_interval(reduced, terms).add(
        log_unit_interval(Fraction(2), terms).scale(Fraction(exponent))
    )


def log_interval(value: Interval, terms: int) -> Interval:
    if value.lo <= 0:
        raise ValueError("modulus-square interval touches zero")
    return Interval(log_fraction(value.lo, terms).lo, log_fraction(value.hi, terms).hi)


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
    return output


def polynomial_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * max(len(left), len(right))
    for i, x in enumerate(left):
        output[i] += x
    for i, x in enumerate(right):
        output[i] += x
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def response_polynomial(nodes: list[Fraction], beta: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)]
    for i, coefficient in enumerate(beta):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = polynomial_multiply(term, [node, Fraction(1)])
        output = polynomial_add(output, [-coefficient * value for value in term])
    return output


def coefficient_matrix(nodes: list[Fraction]) -> np.ndarray:
    columns: list[list[Fraction]] = []
    for i in range(len(nodes)):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = polynomial_multiply(term, [node, Fraction(1)])
        columns.append([-value for value in term])
    matrix = np.zeros((max(map(len, columns)), len(nodes)), dtype=float)
    for column, values in enumerate(columns):
        for row, value in enumerate(values):
            matrix[row, column] = float(value)
    return matrix


def rationalize_and_repair(
    nodes: list[Fraction], floating_beta: np.ndarray, max_denominator: int = 1 << 26
) -> tuple[list[Fraction], list[Fraction]] | None:
    beta = [Fraction(float(value)).limit_denominator(max_denominator) for value in floating_beta]
    beta[-1] = -sum(beta[:-1])
    polynomial = response_polynomial(nodes, beta)

    # The safe endpoint row G(u_max)-G(u_min) has a response polynomial with
    # strictly positive coefficients. Mix in the least exact amount needed to
    # repair small rationalization defects.
    safe = [Fraction(-1)] + [Fraction(0)] * (len(nodes) - 2) + [Fraction(1)]
    safe_polynomial = response_polynomial(nodes, safe)
    repair = Fraction(0)
    for value, safe_value in itertools.zip_longest(
        polynomial, safe_polynomial, fillvalue=Fraction(0)
    ):
        if value < 0:
            if safe_value <= 0:
                return None
            repair = max(repair, -value / safe_value)
    if repair:
        repair += Fraction(1, max_denominator)
        beta = [value + repair * safe_value for value, safe_value in zip(beta, safe)]
        polynomial = response_polynomial(nodes, beta)
    if any(value < 0 for value in polynomial):
        return None

    normalization = sum(polynomial)  # P_beta(1)
    if normalization <= 0:
        return None
    beta = [value / normalization for value in beta]
    polynomial = response_polynomial(nodes, beta)
    return beta, polynomial


def exact_objective(
    indices: tuple[int, ...], beta: list[Fraction], residual_intervals: list[Interval]
) -> Interval:
    output = Interval(Fraction(0), Fraction(0))
    for index, coefficient in zip(indices, beta):
        output = output.add(residual_intervals[index].scale(coefficient))
    return output


def candidate_subsets(point_count: int):
    yield tuple(range(point_count))
    for size in (3, 4):
        yield from itertools.combinations(range(point_count), size)
    for size in range(5, min(point_count, 10) + 1):
        for start in range(point_count - size + 1):
            yield tuple(range(start, start + size))


def decimal_string(value: Fraction, digits: int = 55) -> str:
    getcontext().prec = digits + 15
    return str(Decimal(value.numerator) / Decimal(value.denominator))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--xi", type=Path, required=True)
    parser.add_argument("--complete-result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=320)
    parser.add_argument("--top", type=int, default=30)
    args = parser.parse_args()

    xi_data = json.loads(args.xi.read_text(encoding="utf-8"))
    complete = json.loads(args.complete_result.read_text(encoding="utf-8"))
    points = sorted(
        xi_data["points"],
        key=lambda point: frac(point["x"]),
    )
    nodes = [frac(point["x"]) ** 2 for point in points]
    h_intervals = [modulus_square(point) for point in points]
    log_h = [log_interval(value, args.log_terms) for value in h_intervals]

    shell_data = complete["atomized_shifted_minimum"]["deflation_shells"]
    shells = [
        (int(shell["count_increment"]), frac(shell["distance_square_upper"]))
        for shell in shell_data
    ]

    # The exact shell subtraction is linear in beta, so cache one residual
    # interval per primitive before searching thousands of portfolios.
    residual_intervals: list[Interval] = []
    for index, node in enumerate(nodes):
        residual = log_h[index]
        for count, bound in shells:
            residual = residual.sub(log_fraction(node + bound, args.log_terms).scale(Fraction(count)))
        residual_intervals.append(residual)

    def floating_log(value: Fraction) -> float:
        return math.log(value.numerator) - math.log(value.denominator)

    objective = np.array(
        [floating_log(midpoint(value)) for value in residual_intervals], dtype=float
    )

    retained = []
    seen: set[tuple[int, ...]] = set()
    for indices in candidate_subsets(len(nodes)):
        if indices in seen:
            continue
        seen.add(indices)
        selected_nodes = [nodes[index] for index in indices]
        response_matrix = coefficient_matrix(selected_nodes)
        equalities = np.vstack(
            [np.ones(len(indices)), response_matrix.sum(axis=0)]
        )
        result = linprog(
            objective[list(indices)],
            A_ub=-response_matrix,
            b_ub=np.zeros(response_matrix.shape[0]),
            A_eq=equalities,
            b_eq=np.array([0.0, 1.0]),
            bounds=[(None, None)] * len(indices),
            method="highs",
        )
        if not result.success:
            continue
        frozen = rationalize_and_repair(selected_nodes, result.x)
        if frozen is None:
            continue
        beta, polynomial = frozen
        exact = exact_objective(indices, beta, residual_intervals)
        retained.append(
            {
                "indices": indices,
                "ids": [points[index]["id"] for index in indices],
                "midpoint_objective": float(result.fun),
                "beta": beta,
                "polynomial": polynomial,
                "interval": exact,
            }
        )

    retained.sort(key=lambda item: (item["interval"].hi, item["interval"].lo))
    rows = []
    for item in retained[: args.top]:
        exact = item["interval"]
        status = (
            "CERTIFIED_NEGATIVE"
            if exact.hi < 0
            else "CERTIFIED_POSITIVE"
            if exact.lo > 0
            else "UNRESOLVED"
        )
        rows.append(
            {
                "point_ids": item["ids"],
                "midpoint_objective": repr(item["midpoint_objective"]),
                "beta": [
                    {"numerator": value.numerator, "denominator": value.denominator}
                    for value in item["beta"]
                ],
                "response_polynomial_coefficients": [
                    {"numerator": value.numerator, "denominator": value.denominator}
                    for value in item["polynomial"]
                ],
                "interval": {
                    "lower": {
                        "numerator": exact.lo.numerator,
                        "denominator": exact.lo.denominator,
                    },
                    "upper": {
                        "numerator": exact.hi.numerator,
                        "denominator": exact.hi.denominator,
                    },
                },
                "lower_decimal": decimal_string(exact.lo),
                "upper_decimal": decimal_string(exact.hi),
                "status": status,
            }
        )

    negative_count = sum(row["status"] == "CERTIFIED_NEGATIVE" for row in rows)
    output = {
        "schema": "riemann.x9306-real-log-portfolio-search.v1",
        "xi_source_sha256": file_sha256(args.xi),
        "complete_result_sha256": file_sha256(args.complete_result),
        "ordinate": xi_data["ordinate"],
        "point_count": len(points),
        "shell_count": len(shells),
        "subsets_solved": len(retained),
        "top_rows": rows,
        "certified_negative_rows": negative_count,
        "verdict": (
            "CERTIFIED_NEGATIVE_PORTFOLIO_FOUND"
            if negative_count
            else "NO_NEGATIVE_IN_SEARCHED_MONOMIAL_POSITIVE_PORTFOLIOS"
        ),
        "proof_boundary": (
            "Every listed interval is exact for its frozen rational beta and the committed "
            "directed xi rectangles and atomized count shells. Exhaustiveness is only over "
            "the enumerated subset families and the monomial-positive L-9308 cone."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "verdict": output["verdict"],
                "subsets_solved": output["subsets_solved"],
                "best": rows[0] if rows else None,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
