#!/usr/bin/env python3
"""Directed all-cone L-9309 replay from one committed PR #103 certificate.

The logarithm layer uses exact rational atanh-Horner partial sums with an exact
positive tail. The large final linear contractions are accelerated by converting
exact rational interval endpoints to Decimal with directed rounding and then
using directed Decimal multiplication/addition. Every emitted finite decimal is
an exact rational endpoint.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("reversed rational interval")

    def add(self, other: "RationalInterval") -> "RationalInterval":
        return RationalInterval(self.lower + other.lower, self.upper + other.upper)

    def sub(self, other: "RationalInterval") -> "RationalInterval":
        return RationalInterval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, scalar: Fraction) -> "RationalInterval":
        if scalar >= 0:
            return RationalInterval(self.lower * scalar, self.upper * scalar)
        return RationalInterval(self.upper * scalar, self.lower * scalar)


@dataclass(frozen=True)
class DecimalInterval:
    lower: Decimal
    upper: Decimal

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("reversed decimal interval")


def fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ValueError(f"{name} must be an object")
    numerator = raw.get("numerator")
    denominator = raw.get("denominator")
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or denominator <= 0
    ):
        raise ValueError(f"bad rational at {name}")
    return Fraction(numerator, denominator)


def parse_interval(raw: Any, name: str) -> RationalInterval:
    if not isinstance(raw, dict):
        raise ValueError(f"{name} must be an object")
    return RationalInterval(
        fraction(raw.get("lower"), f"{name}.lower"),
        fraction(raw.get("upper"), f"{name}.upper"),
    )


def square_interval(value: RationalInterval) -> RationalInterval:
    candidates = (value.lower * value.lower, value.upper * value.upper)
    lower = Fraction(0) if value.lower <= 0 <= value.upper else min(candidates)
    return RationalInterval(lower, max(candidates))


def modulus_square(point: dict[str, Any]) -> RationalInterval:
    rectangle = point.get("xi_rectangle")
    if not isinstance(rectangle, dict):
        raise ValueError("point xi_rectangle missing")
    return square_interval(parse_interval(rectangle.get("real"), "xi.real")).add(
        square_interval(parse_interval(rectangle.get("imag"), "xi.imag"))
    )


def polynomial_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
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


def basis_vector(nodes: list[Fraction], degree: int) -> list[Fraction]:
    output: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        output.append(-((-node) ** degree) / denominator)
    return output


class ExactLogEncloser:
    def __init__(self, terms: int):
        if terms < 32:
            raise ValueError("at least 32 logarithm terms are required")
        self.terms = terms
        self.log2 = self._unit(Fraction(2))

    def _unit(self, value: Fraction) -> RationalInterval:
        if not (Fraction(1) <= value <= Fraction(2)):
            raise ValueError("internal log reduction failed")
        z = (value - 1) / (value + 1)
        z_squared = z * z
        # Horner evaluation of sum z^(2j+1)/(2j+1), from j=0 to N-1.
        accumulator = Fraction(1, 2 * self.terms - 1)
        for j in range(self.terms - 2, -1, -1):
            accumulator = Fraction(1, 2 * j + 1) + z_squared * accumulator
        lower = 2 * z * accumulator
        if z == 0:
            tail = Fraction(0)
        else:
            tail = (
                2
                * z ** (2 * self.terms + 1)
                / ((2 * self.terms + 1) * (1 - z_squared))
            )
        return RationalInterval(lower, lower + tail)

    def __call__(self, value: Fraction) -> RationalInterval:
        if value <= 0:
            raise ValueError("log argument must be positive")
        reduced = value
        exponent = 0
        while reduced >= 2:
            reduced /= 2
            exponent += 1
        while reduced < 1:
            reduced *= 2
            exponent -= 1
        return self._unit(reduced).add(self.log2.scale(Fraction(exponent)))


def rational_to_decimal_interval(value: Fraction, precision: int) -> DecimalInterval:
    with localcontext() as context:
        context.prec = precision
        context.rounding = ROUND_FLOOR
        lower = Decimal(value.numerator) / Decimal(value.denominator)
    with localcontext() as context:
        context.prec = precision
        context.rounding = ROUND_CEILING
        upper = Decimal(value.numerator) / Decimal(value.denominator)
    return DecimalInterval(lower, upper)


def decimal_add(
    left: DecimalInterval, right: DecimalInterval, precision: int
) -> DecimalInterval:
    with localcontext() as context:
        context.prec = precision
        context.rounding = ROUND_FLOOR
        lower = left.lower + right.lower
    with localcontext() as context:
        context.prec = precision
        context.rounding = ROUND_CEILING
        upper = left.upper + right.upper
    return DecimalInterval(lower, upper)


def decimal_multiply(
    left: DecimalInterval, right: DecimalInterval, precision: int
) -> DecimalInterval:
    lower_candidates: list[Decimal] = []
    upper_candidates: list[Decimal] = []
    for x in (left.lower, left.upper):
        for y in (right.lower, right.upper):
            with localcontext() as context:
                context.prec = precision
                context.rounding = ROUND_FLOOR
                lower_candidates.append(x * y)
            with localcontext() as context:
                context.prec = precision
                context.rounding = ROUND_CEILING
                upper_candidates.append(x * y)
    return DecimalInterval(min(lower_candidates), max(upper_candidates))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=150)
    parser.add_argument("--decimal-precision", type=int, default=170)
    args = parser.parse_args()
    started = time.time()

    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    if certificate.get("classification") != "RIEMANN_XI_DIRECTED":
        raise ValueError("expected a directed Riemann-xi certificate")
    if certificate.get("normalization_id") != "riemann-xi-standard-half-s-sminus1-v1":
        raise ValueError("completed-xi normalization mismatch")

    raw_points = certificate.get("points")
    if not isinstance(raw_points, list) or len(raw_points) < 2:
        raise ValueError("certificate points missing")
    points = sorted(raw_points, key=lambda point: fraction(point["u"], "point.u"))
    nodes = [fraction(point["u"], "point.u") for point in points]
    if any(nodes[index] >= nodes[index + 1] for index in range(len(nodes) - 1)):
        raise ValueError("nodes must be strictly increasing")

    raw_windows = certificate.get("count_windows")
    if not isinstance(raw_windows, list) or not raw_windows:
        raise ValueError("count windows missing")
    windows = sorted(raw_windows, key=lambda item: fraction(item["radius"], "radius"))
    shells: list[tuple[int, Fraction]] = []
    previous_count = 0
    for index, window in enumerate(windows):
        gate = window.get("gate")
        if not isinstance(gate, dict) or gate.get("status") != "CERTIFIED_TOTAL_ZETA_ZERO_LOWER_BOUND":
            raise ValueError("count semantic gate mismatch")
        count = window.get("count_lower")
        if isinstance(count, bool) or not isinstance(count, int) or count < previous_count:
            raise ValueError("count_lower must be nondecreasing integers")
        radius = fraction(window.get("radius"), f"count_windows[{index}].radius")
        shells.append((count - previous_count, radius * radius))
        previous_count = count

    log_enclose = ExactLogEncloser(args.log_terms)
    exact_residuals: list[RationalInterval] = []
    for point, node in zip(points, nodes):
        h_interval = modulus_square(point)
        residual = RationalInterval(
            log_enclose(h_interval.lower).lower,
            log_enclose(h_interval.upper).upper,
        )
        for count_increment, bound in shells:
            residual = residual.sub(
                log_enclose(node + bound).scale(Fraction(count_increment))
            )
        exact_residuals.append(residual)

    decimal_residuals = [
        DecimalInterval(
            rational_to_decimal_interval(value.lower, args.decimal_precision).lower,
            rational_to_decimal_interval(value.upper, args.decimal_precision).upper,
        )
        for value in exact_residuals
    ]

    rows = []
    for degree in range(len(nodes) - 1):
        beta = basis_vector(nodes, degree)
        if sum(beta) != 0:
            raise ValueError("basis vector fails zero-sum identity")
        expected = [Fraction(0)] * degree + [Fraction(1)]
        if response_polynomial(nodes, beta) != expected:
            raise ValueError("basis response-polynomial identity failed")
        value = DecimalInterval(Decimal(0), Decimal(0))
        for coefficient, residual in zip(beta, decimal_residuals):
            value = decimal_add(
                value,
                decimal_multiply(
                    rational_to_decimal_interval(coefficient, args.decimal_precision),
                    residual,
                    args.decimal_precision,
                ),
                args.decimal_precision,
            )
        row_status = (
            "CERTIFIED_NEGATIVE"
            if value.upper < 0
            else "CERTIFIED_NONNEGATIVE"
            if value.lower >= 0
            else "UNRESOLVED"
        )
        rows.append(
            {
                "degree": degree,
                "response_polynomial": "1" if degree == 0 else f"y^{degree}",
                "lower_exact_decimal": str(value.lower),
                "upper_exact_decimal": str(value.upper),
                "width_exact_decimal": str(value.upper - value.lower),
                "status": row_status,
            }
        )

    negative_count = sum(row["status"] == "CERTIFIED_NEGATIVE" for row in rows)
    unresolved_count = sum(row["status"] == "UNRESOLVED" for row in rows)
    if negative_count:
        verdict = "CERTIFIED_NEGATIVE_L9308_BASIS_WITNESS"
    elif unresolved_count:
        verdict = "UNRESOLVED_MONOMIAL_POSITIVE_PORTFOLIO_CONE"
    else:
        verdict = "CERTIFIED_NONNEGATIVE_ENTIRE_MONOMIAL_POSITIVE_PORTFOLIO_CONE"

    source = certificate.get("source", {})
    output = {
        "schema": "riemann.x9307-simplicial-portfolio-basis.directed-decimal.v1",
        "classification": "RIEMANN_XI_DIRECTED",
        "analytic_claim": "L-9309",
        "parent_response_claim": "L-9308",
        "source_file_sha256": sha256(args.certificate),
        "source_certificate_sha256": certificate.get("certificate_sha256"),
        "primitive_sha256": source.get("primitive_sha256"),
        "total_count_sha256": source.get("total_count_sha256"),
        "ordinate": certificate.get("ordinate"),
        "primitive_shift": source.get("primitive_ordinate_shift_from_count_center"),
        "node_ids": [point["id"] for point in points],
        "node_count": len(nodes),
        "basis_row_count": len(rows),
        "log_enclosure": {
            "method": "exact rational atanh-Horner series with positive tail",
            "terms": args.log_terms,
        },
        "final_accumulation": {
            "method": (
                "Python Decimal exact-integer conversion with ROUND_FLOOR/ROUND_CEILING "
                "at every division, multiplication, and addition"
            ),
            "precision_decimal_digits": args.decimal_precision,
        },
        "basis_rows": rows,
        "certified_negative_rows": negative_count,
        "unresolved_rows": unresolved_count,
        "verdict": verdict,
        "scope": (
            "By L-9309 these basis rows decide every normalized L-9308 portfolio "
            "whose response polynomial has nonnegative monomial coefficients, "
            "including every such portfolio on any subset of the declared nodes."
        ),
        "proof_boundary": (
            "The finite interval construction is directed standard-library arithmetic "
            "over the committed PR #103 certificate. The RH implication inherits "
            "L-7501/L-7502/L-9308/L-9309 and the atomized total-count conversion. "
            "This does not close mixed-coefficient polynomials merely nonnegative on "
            "[0,infinity), other shifts, or other node tables."
        ),
        "elapsed_seconds": time.time() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "verdict": verdict,
                "basis_row_count": len(rows),
                "negative_rows": negative_count,
                "unresolved_rows": unresolved_count,
                "tightest": min(rows, key=lambda row: Decimal(row["lower_exact_decimal"])),
                "elapsed_seconds": output["elapsed_seconds"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
