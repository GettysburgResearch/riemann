#!/usr/bin/env python3
"""Exactly decide the full L-9308 monomial-positive portfolio cone via L-9309.

For n fixed positive nodes, the cone has n-1 exact extreme rays corresponding
to response polynomials 1,y,...,y^(n-2). This checker contracts only those
basis rows against committed directed xi rectangles and exact count shells.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

import search as kernel


def source_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(value: kernel.Interval) -> dict[str, dict[str, int]]:
    return {"lower": fraction_json(value.lo), "upper": fraction_json(value.hi)}


def decimal_string(value: Fraction, digits: int = 70) -> str:
    getcontext().prec = digits + 15
    return str(Decimal(value.numerator) / Decimal(value.denominator))


def basis_vector(nodes: list[Fraction], degree: int) -> list[Fraction]:
    output = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        output.append(-((-node) ** degree) / denominator)
    return output


def status(value: kernel.Interval) -> str:
    if value.hi < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lo >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--xi", type=Path, required=True)
    parser.add_argument("--complete-result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=360)
    args = parser.parse_args()

    xi_data = json.loads(args.xi.read_text(encoding="utf-8"))
    complete = json.loads(args.complete_result.read_text(encoding="utf-8"))
    points = sorted(xi_data["points"], key=lambda point: kernel.frac(point["x"]))
    nodes = [kernel.frac(point["x"]) ** 2 for point in points]
    log_h = [
        kernel.log_interval(kernel.modulus_square(point), args.log_terms)
        for point in points
    ]

    shells = [
        (
            int(shell["count_increment"]),
            kernel.frac(shell["distance_square_upper"]),
        )
        for shell in complete["atomized_shifted_minimum"]["deflation_shells"]
    ]

    residual_intervals: list[kernel.Interval] = []
    for index, node in enumerate(nodes):
        residual = log_h[index]
        for count, bound in shells:
            residual = residual.sub(
                kernel.log_fraction(node + bound, args.log_terms).scale(
                    Fraction(count)
                )
            )
        residual_intervals.append(residual)

    rows = []
    for degree in range(len(nodes) - 1):
        beta = basis_vector(nodes, degree)
        if sum(beta) != 0:
            raise RuntimeError("basis vector fails zero-sum identity")
        polynomial = kernel.response_polynomial(nodes, beta)
        expected = [Fraction(0)] * degree + [Fraction(1)]
        if polynomial != expected:
            raise RuntimeError("basis response-polynomial identity failed")
        value = kernel.exact_objective(tuple(range(len(nodes))), beta, residual_intervals)
        rows.append(
            {
                "degree": degree,
                "response_polynomial": f"y^{degree}" if degree else "1",
                "beta": [fraction_json(entry) for entry in beta],
                "interval": interval_json(value),
                "lower_decimal": decimal_string(value.lo),
                "upper_decimal": decimal_string(value.hi),
                "status": status(value),
            }
        )

    negatives = [row for row in rows if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in rows if row["status"] == "UNRESOLVED"]
    if negatives:
        verdict = "CERTIFIED_NEGATIVE_L9308_BASIS_WITNESS"
    elif unresolved:
        verdict = "UNRESOLVED_MONOMIAL_POSITIVE_PORTFOLIO_CONE"
    else:
        verdict = "CERTIFIED_NONNEGATIVE_ENTIRE_MONOMIAL_POSITIVE_PORTFOLIO_CONE"

    output = {
        "schema": "riemann.x9307-simplicial-portfolio-basis.v1",
        "analytic_claim": "L-9309",
        "parent_response_claim": "L-9308",
        "xi_source_sha256": source_sha256(args.xi),
        "complete_result_sha256": source_sha256(args.complete_result),
        "ordinate": xi_data["ordinate"],
        "point_ids": [point["id"] for point in points],
        "point_count": len(points),
        "basis_row_count": len(rows),
        "shell_count": len(shells),
        "basis_rows": rows,
        "certified_negative_rows": len(negatives),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope": (
            "By L-9309, these basis rows decide every normalized portfolio whose "
            "L-9308 response polynomial has nonnegative monomial coefficients, "
            "including every such portfolio supported on any subset of these nodes."
        ),
        "proof_boundary": (
            "Finite algebra and interval contraction are exact. The RH implication "
            "inherits the direct-xi canonical-product and atomized count-deflation "
            "gates, and any negative requires independent primitive/count reproduction."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "verdict": verdict,
                "basis_row_count": len(rows),
                "negative_rows": len(negatives),
                "unresolved_rows": len(unresolved),
                "tightest": min(rows, key=lambda row: Fraction(
                    row["interval"]["upper"]["numerator"],
                    row["interval"]["upper"]["denominator"],
                )),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
