#!/usr/bin/env python3
"""Build directed response moments from a nearest-zero direct-xi certificate."""
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

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

CERT_SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
OUTPUT_SCHEMA = "riemann.x9311-directed-response-moments.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
ZERO_GATE = "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"


class BuildError(ValueError):
    pass


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise BuildError("reversed rational interval")

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
            raise BuildError("reversed decimal interval")


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise BuildError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise BuildError(f"{name} must be integer text") from exc
    raise BuildError(f"{name} must be an integer")


def fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise BuildError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise BuildError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def parse_interval(raw: Any, name: str) -> RationalInterval:
    if not isinstance(raw, dict):
        raise BuildError(f"{name} must be an object")
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
        raise BuildError("point xi_rectangle missing")
    return square_interval(parse_interval(rectangle.get("real"), "xi.real")).add(
        square_interval(parse_interval(rectangle.get("imag"), "xi.imag"))
    )


def polynomial_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def response_polynomial(nodes: list[Fraction], beta: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)]
    for i, coefficient in enumerate(beta):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = polynomial_multiply(term, [node, Fraction(1)])
        out = polynomial_add(out, [-coefficient * value for value in term])
    return out


def basis_vector(nodes: list[Fraction], degree: int) -> list[Fraction]:
    out: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        out.append(-((-node) ** degree) / denominator)
    return out


class ExactLogEncloser:
    def __init__(self, terms: int):
        if terms < 64:
            raise BuildError("at least 64 logarithm terms are required")
        self.terms = terms
        self.log2 = self._unit(Fraction(2))
        self.cache: dict[Fraction, RationalInterval] = {}

    def _unit(self, value: Fraction) -> RationalInterval:
        if not (Fraction(1) <= value <= Fraction(2)):
            raise BuildError("internal logarithm reduction failed")
        z = (value - 1) / (value + 1)
        z2 = z * z
        accumulator = Fraction(1, 2 * self.terms - 1)
        for j in range(self.terms - 2, -1, -1):
            accumulator = Fraction(1, 2 * j + 1) + z2 * accumulator
        lower = 2 * z * accumulator
        tail = (
            Fraction(0)
            if z == 0
            else 2 * z ** (2 * self.terms + 1)
            / ((2 * self.terms + 1) * (1 - z2))
        )
        return RationalInterval(lower, lower + tail)

    @staticmethod
    def _reduce(value: Fraction) -> tuple[Fraction, int]:
        if value <= 0:
            raise BuildError("logarithm argument must be positive")
        exponent = value.numerator.bit_length() - value.denominator.bit_length()
        reduced = value / (Fraction(1 << exponent) if exponent >= 0 else Fraction(1, 1 << (-exponent)))
        if reduced < 1:
            reduced *= 2
            exponent -= 1
        elif reduced >= 2:
            reduced /= 2
            exponent += 1
        if not (1 <= reduced < 2):
            raise BuildError("binary logarithm reduction failed")
        return reduced, exponent

    def __call__(self, value: Fraction) -> RationalInterval:
        cached = self.cache.get(value)
        if cached is not None:
            return cached
        reduced, exponent = self._reduce(value)
        result = self._unit(reduced).add(self.log2.scale(Fraction(exponent)))
        self.cache[value] = result
        return result


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


def decimal_add(left: DecimalInterval, right: DecimalInterval, precision: int) -> DecimalInterval:
    with localcontext() as context:
        context.prec = precision
        context.rounding = ROUND_FLOOR
        lower = left.lower + right.lower
    with localcontext() as context:
        context.prec = precision
        context.rounding = ROUND_CEILING
        upper = left.upper + right.upper
    return DecimalInterval(lower, upper)


def decimal_multiply(left: DecimalInterval, right: DecimalInterval, precision: int) -> DecimalInterval:
    lowers: list[Decimal] = []
    uppers: list[Decimal] = []
    for x in (left.lower, left.upper):
        for y in (right.lower, right.upper):
            with localcontext() as context:
                context.prec = precision
                context.rounding = ROUND_FLOOR
                lowers.append(x * y)
            with localcontext() as context:
                context.prec = precision
                context.rounding = ROUND_CEILING
                uppers.append(x * y)
    return DecimalInterval(min(lowers), max(uppers))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(certificate_path: Path, log_terms: int, decimal_precision: int) -> dict[str, Any]:
    started = time.time()
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    if not isinstance(certificate, dict) or certificate.get("schema") != CERT_SCHEMA:
        raise BuildError("unsupported certificate schema")
    if certificate.get("classification") != "RIEMANN_XI_DIRECTED":
        raise BuildError("certificate is not directed Riemann-xi data")
    if certificate.get("normalization_id") != NORMALIZATION:
        raise BuildError("completed-xi normalization mismatch")

    raw_points = certificate.get("points")
    if not isinstance(raw_points, list) or len(raw_points) < 3:
        raise BuildError("at least three points are required")
    points = sorted(raw_points, key=lambda p: fraction(p.get("u"), "point.u"))
    nodes = [fraction(point.get("u"), "point.u") for point in points]
    if nodes[0] <= 0 or any(nodes[i] >= nodes[i + 1] for i in range(len(nodes) - 1)):
        raise BuildError("nodes must be strictly increasing and positive")

    raw_bins = certificate.get("zero_bins")
    if not isinstance(raw_bins, list) or not raw_bins:
        raise BuildError("zero_bins missing")
    selected_bounds: list[tuple[int, Fraction]] = []
    seen_ids: set[str] = set()
    for index, zero in enumerate(raw_bins):
        if not isinstance(zero, dict) or not isinstance(zero.get("id"), str):
            raise BuildError("bad zero bin")
        if zero["id"] in seen_ids:
            raise BuildError("duplicate zero-bin ID")
        seen_ids.add(zero["id"])
        gate = zero.get("gate")
        if not isinstance(gate, dict) or gate.get("status") != ZERO_GATE:
            raise BuildError("zero-bin semantic gate mismatch")
        count = integer(zero.get("count_lower"), f"zero_bins[{index}].count_lower")
        if count <= 0:
            raise BuildError("zero-bin count must be positive")
        bound = fraction(zero.get("distance_square_upper"), "distance_square_upper")
        if bound <= 0:
            raise BuildError("zero distance-square upper bound must be positive")
        selected_bounds.append((count, bound))

    log = ExactLogEncloser(log_terms)
    residuals: list[RationalInterval] = []
    residual_metadata: list[dict[str, Any]] = []
    for point, node in zip(points, nodes):
        h = modulus_square(point)
        if h.lower <= 0:
            raise BuildError("completed-xi modulus interval touches zero")
        line_product = Fraction(1)
        for count, bound in selected_bounds:
            line_product *= (node + bound) ** count
        value = RationalInterval(log(h.lower).lower, log(h.upper).upper).sub(log(line_product))
        residuals.append(value)
        residual_metadata.append(
            {
                "id": point.get("id"),
                "u": {"numerator": node.numerator, "denominator": node.denominator},
                "selected_factor_count": sum(count for count, _ in selected_bounds),
                "residual_width_decimal": str(
                    rational_to_decimal_interval(value.upper - value.lower, 40).upper
                ),
            }
        )

    decimal_residuals = [
        DecimalInterval(
            rational_to_decimal_interval(value.lower, decimal_precision).lower,
            rational_to_decimal_interval(value.upper, decimal_precision).upper,
        )
        for value in residuals
    ]

    rows: list[dict[str, Any]] = []
    for degree in range(len(nodes) - 1):
        beta = basis_vector(nodes, degree)
        if sum(beta) != 0:
            raise BuildError("basis vector fails zero-sum identity")
        expected = [Fraction(0)] * degree + [Fraction(1)]
        if response_polynomial(nodes, beta) != expected:
            raise BuildError("basis response-polynomial identity failed")
        value = DecimalInterval(Decimal(0), Decimal(0))
        for coefficient, residual in zip(beta, decimal_residuals):
            value = decimal_add(
                value,
                decimal_multiply(
                    rational_to_decimal_interval(coefficient, decimal_precision),
                    residual,
                    decimal_precision,
                ),
                decimal_precision,
            )
        with localcontext() as context:
            context.prec = 50
            beta_l1 = sum(
                Decimal(abs(item.numerator)) / Decimal(item.denominator) for item in beta
            )
        status = (
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
                "beta_l1_decimal": str(beta_l1),
                "status": status,
            }
        )

    return {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "analytic_claims": ["L-9301", "L-9308", "L-9309", "L-9310"],
        "certificate_sha256": sha256(certificate_path),
        "source_certificate_digest": certificate.get("certificate_sha256"),
        "normalization_id": certificate.get("normalization_id"),
        "common_xi_scale_power_of_two": certificate.get("common_xi_scale_power_of_two"),
        "ordinate": certificate.get("ordinate"),
        "node_count": len(nodes),
        "node_ids": [point.get("id") for point in points],
        "selected_zero_count": sum(count for count, _ in selected_bounds),
        "selection_scope": certificate.get("source", {}).get("selection_scope"),
        "response_degree_bound": len(nodes) - 2,
        "log_enclosure": {
            "method": "exact rational atanh-Horner with positive tail and exact binary reduction",
            "terms": log_terms,
        },
        "final_accumulation": {
            "method": "directed Python Decimal multiplication and addition",
            "precision_decimal_digits": decimal_precision,
        },
        "residuals": residual_metadata,
        "basis_rows": rows,
        "negative_rows": sum(row["status"] == "CERTIFIED_NEGATIVE" for row in rows),
        "unresolved_rows": sum(row["status"] == "UNRESOLVED" for row in rows),
        "elapsed_seconds": time.time() - started,
        "proof_boundary": (
            "Exact rational logarithm enclosures, exact basis identities, and directed "
            "decimal contractions over a source-bound nearest-zero certificate."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--log-terms", type=int, default=220)
    parser.add_argument("--decimal-precision", type=int, default=240)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(args.certificate, args.log_terms, args.decimal_precision)
    except (OSError, json.JSONDecodeError, BuildError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"built": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "node_count": result["node_count"],
                "degree_bound": result["response_degree_bound"],
                "negative_rows": result["negative_rows"],
                "unresolved_rows": result["unresolved_rows"],
                "elapsed_seconds": result["elapsed_seconds"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
