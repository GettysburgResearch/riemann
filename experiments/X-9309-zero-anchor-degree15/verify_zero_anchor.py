#!/usr/bin/env python3
"""Directed zero-anchor contraction and exact degree-15 moment-cone checker."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

BASIS_SCHEMA = "riemann.x9307-simplicial-portfolio-basis.directed-decimal.v1"
OUTPUT_SCHEMA = "riemann.x9309-zero-anchor-degree15.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("reversed rational interval")

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
            raise CertificateError("reversed decimal interval")


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = raw.get("numerator")
    denominator = raw.get("denominator")
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or denominator <= 0
    ):
        raise CertificateError(f"bad rational at {name}")
    return Fraction(numerator, denominator)


def parse_interval(raw: Any, name: str) -> RationalInterval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return RationalInterval(
        fraction(raw.get("lower"), f"{name}.lower"),
        fraction(raw.get("upper"), f"{name}.upper"),
    )


def interval_subset(inner: RationalInterval, outer: RationalInterval) -> bool:
    return outer.lower <= inner.lower <= inner.upper <= outer.upper


def square_interval(value: RationalInterval) -> RationalInterval:
    candidates = (value.lower * value.lower, value.upper * value.upper)
    lower = Fraction(0) if value.lower <= 0 <= value.upper else min(candidates)
    return RationalInterval(lower, max(candidates))


def modulus_square(point: dict[str, Any]) -> RationalInterval:
    rectangle = point.get("xi_rectangle")
    if not isinstance(rectangle, dict):
        raise CertificateError("point xi_rectangle missing")
    return square_interval(parse_interval(rectangle.get("real"), "xi.real")).add(
        square_interval(parse_interval(rectangle.get("imag"), "xi.imag"))
    )


class ExactLogEncloser:
    def __init__(self, terms: int):
        if terms < 64:
            raise CertificateError("at least 64 logarithm terms are required")
        self.terms = terms
        self.log2 = self._unit(Fraction(2))

    def _unit(self, value: Fraction) -> RationalInterval:
        if not (Fraction(1) <= value <= Fraction(2)):
            raise CertificateError("internal logarithm reduction failed")
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

    def __call__(self, value: Fraction) -> RationalInterval:
        if value <= 0:
            raise CertificateError("logarithm argument must be positive")
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


def decimal_to_fraction(value: Decimal) -> Fraction:
    return Fraction(str(value))


def basis_vector(nodes: list[Fraction], degree: int) -> list[Fraction]:
    output: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        output.append(-((-node) ** degree) / denominator)
    return output


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError(f"{path} must contain an object")
    return value


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_basis(path: Path) -> tuple[dict[str, Any], list[RationalInterval]]:
    data = load_json(path)
    if data.get("schema") != BASIS_SCHEMA:
        raise CertificateError("unsupported old basis schema")
    rows = data.get("basis_rows")
    if not isinstance(rows, list) or len(rows) != 15:
        raise CertificateError("expected exactly fifteen old basis rows")
    output: list[RationalInterval] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or exact_int(row.get("degree"), "degree") != index:
            raise CertificateError("old basis degrees must be consecutive")
        try:
            lo = Fraction(row["lower_exact_decimal"])
            hi = Fraction(row["upper_exact_decimal"])
        except (KeyError, ValueError, ZeroDivisionError) as exc:
            raise CertificateError("invalid old basis decimal endpoint") from exc
        output.append(RationalInterval(lo, hi))
    if data.get("verdict") != "CERTIFIED_NONNEGATIVE_ENTIRE_MONOMIAL_POSITIVE_PORTFOLIO_CONE":
        raise CertificateError("old basis table lacks its exact nonnegative verdict")
    return data, output


def zero_point(primitive: dict[str, Any], name: str) -> dict[str, Any]:
    if primitive.get("normalization_id") != NORMALIZATION:
        raise CertificateError(f"{name} normalization mismatch")
    points = primitive.get("points")
    if not isinstance(points, list) or len(points) != 1 or not isinstance(points[0], dict):
        raise CertificateError(f"{name} must contain exactly one point")
    point = points[0]
    x = fraction(point.get("x"), f"{name}.x")
    if x != 0:
        raise CertificateError(f"{name} point is not x=0")
    if point.get("functional_equation_residual_contains_zero") is not True:
        raise CertificateError(f"{name} functional-equation gate failed")
    if modulus_square(point).lower <= 0:
        raise CertificateError(f"{name} does not prove H_T(0)>0")
    return point


def compare_zero_primitives(low: dict[str, Any], high: dict[str, Any]) -> None:
    if exact_int(low.get("precision_bits"), "low.precision_bits") >= exact_int(
        high.get("precision_bits"), "high.precision_bits"
    ):
        raise CertificateError("zero primitive precision order is invalid")
    for field in ("normalization_id", "common_xi_scale_power_of_two", "ordinate"):
        if low.get(field) != high.get(field):
            raise CertificateError(f"zero primitive {field} mismatch")
    low_point = zero_point(low, "low zero primitive")
    high_point = zero_point(high, "high zero primitive")
    for component in ("real", "imag"):
        low_interval = parse_interval(low_point["xi_rectangle"][component], f"low.{component}")
        high_interval = parse_interval(high_point["xi_rectangle"][component], f"high.{component}")
        if not interval_subset(high_interval, low_interval):
            raise CertificateError(f"high-precision {component} interval is not nested")


def deflation_shells(certificate: dict[str, Any]) -> list[tuple[int, Fraction]]:
    windows = certificate.get("count_windows")
    if not isinstance(windows, list) or not windows:
        raise CertificateError("count windows missing")
    ordered = sorted(windows, key=lambda item: fraction(item.get("radius"), "radius"))
    output: list[tuple[int, Fraction]] = []
    previous = 0
    for index, window in enumerate(ordered):
        gate = window.get("gate")
        if not isinstance(gate, dict) or gate.get("status") != "CERTIFIED_TOTAL_ZETA_ZERO_LOWER_BOUND":
            raise CertificateError("total-zero-count semantic gate mismatch")
        count = exact_int(window.get("count_lower"), f"count_windows[{index}].count_lower")
        if count < previous:
            raise CertificateError("count windows are not nested")
        radius = fraction(window.get("radius"), f"count_windows[{index}].radius")
        output.append((count - previous, radius * radius))
        previous = count
    return output


def residual_interval(
    point: dict[str, Any], node: Fraction, shells: list[tuple[int, Fraction]], log: ExactLogEncloser
) -> RationalInterval:
    h = modulus_square(point)
    if h.lower <= 0:
        raise CertificateError("direct-xi modulus interval touches zero")
    residual = RationalInterval(log(h.lower).lower, log(h.upper).upper)
    for count, bound in shells:
        residual = residual.sub(log(node + bound).scale(Fraction(count)))
    return residual


def hankel(values: list[Fraction], size: int, offset: int) -> list[list[Fraction]]:
    return [[values[i + j + offset] for j in range(size)] for i in range(size)]


def subtract_diagonal(matrix: list[list[Fraction]], delta: Fraction) -> list[list[Fraction]]:
    return [
        [value - (delta if i == j else 0) for j, value in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def exact_ldl_positive_pivots(matrix: list[list[Fraction]]) -> list[Fraction]:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise CertificateError("matrix must be square")
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = [Fraction(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivots[i] = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivots[i] <= 0:
            raise CertificateError(f"nonpositive exact LDL pivot at index {i}")
        for j in range(i + 1, n):
            numerator = matrix[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivots[i]
    return pivots


def maximum_row_sum(matrix: list[list[Fraction]]) -> Fraction:
    return max(sum(abs(value) for value in row) for row in matrix)


def solve_linear(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    n = len(matrix)
    augmented = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next((row for row in range(column, n) if augmented[row][column] != 0), None)
        if pivot is None:
            raise CertificateError("singular Schur block")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    x - factor * y for x, y in zip(augmented[row], augmented[column])
                ]
    return [augmented[i][-1] for i in range(n)]


def interval_quadratic(
    lower: list[list[Fraction]], upper: list[list[Fraction]], vector: list[Fraction]
) -> RationalInterval:
    result = RationalInterval(Fraction(0), Fraction(0))
    for i, x in enumerate(vector):
        for j, y in enumerate(vector):
            result = result.add(RationalInterval(lower[i][j], upper[i][j]).scale(x * y))
    return result


def decimal_string(value: Fraction, digits: int = 90) -> str:
    with localcontext() as context:
        context.prec = digits
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def verify(
    old_certificate_path: Path,
    old_basis_path: Path,
    zero_low_path: Path,
    zero_high_path: Path,
    log_terms: int,
    decimal_precision: int,
    delta: Fraction,
) -> dict[str, Any]:
    old_certificate = load_json(old_certificate_path)
    old_basis_data, old_moments = load_basis(old_basis_path)
    zero_low = load_json(zero_low_path)
    zero_high = load_json(zero_high_path)
    compare_zero_primitives(zero_low, zero_high)

    if old_certificate.get("classification") != "RIEMANN_XI_DIRECTED":
        raise CertificateError("old certificate is not directed Riemann-xi data")
    if old_certificate.get("normalization_id") != NORMALIZATION:
        raise CertificateError("old certificate normalization mismatch")
    for field in ("ordinate", "common_xi_scale_power_of_two"):
        if old_certificate.get(field) != zero_high.get(field):
            raise CertificateError(f"zero anchor and old certificate {field} mismatch")
    declared_source = old_basis_data.get("source_certificate_sha256")
    actual_source = file_sha256(old_certificate_path)
    if declared_source and declared_source != actual_source:
        raise CertificateError("old basis is not bound to the supplied old certificate")

    raw_points = old_certificate.get("points")
    if not isinstance(raw_points, list) or len(raw_points) != 16:
        raise CertificateError("expected the sixteen-node old certificate")
    old_points = sorted(raw_points, key=lambda point: fraction(point.get("u"), "point.u"))
    old_nodes = [fraction(point.get("u"), "point.u") for point in old_points]
    if old_nodes[0] <= 0 or any(old_nodes[i] >= old_nodes[i + 1] for i in range(15)):
        raise CertificateError("old nodes must be strictly increasing and positive")

    high_zero_point = zero_point(zero_high, "high zero primitive")
    shells = deflation_shells(old_certificate)
    log = ExactLogEncloser(log_terms)
    nodes = [Fraction(0)] + old_nodes
    residuals = [residual_interval(high_zero_point, Fraction(0), shells, log)] + [
        residual_interval(point, node, shells, log)
        for point, node in zip(old_points, old_nodes)
    ]

    beta0 = basis_vector(nodes, 0)
    if sum(beta0) != 0:
        raise CertificateError("zero-anchor basis vector is not zero sum")
    b0_decimal = DecimalInterval(Decimal(0), Decimal(0))
    for coefficient, residual in zip(beta0, residuals):
        coefficient_decimal = rational_to_decimal_interval(coefficient, decimal_precision)
        residual_decimal = DecimalInterval(
            rational_to_decimal_interval(residual.lower, decimal_precision).lower,
            rational_to_decimal_interval(residual.upper, decimal_precision).upper,
        )
        b0_decimal = decimal_add(
            b0_decimal,
            decimal_multiply(coefficient_decimal, residual_decimal, decimal_precision),
            decimal_precision,
        )
    b0 = RationalInterval(
        decimal_to_fraction(b0_decimal.lower), decimal_to_fraction(b0_decimal.upper)
    )

    new_moments = [b0] + old_moments
    lower_values = [value.lower for value in new_moments]
    upper_values = [value.upper for value in new_moments]
    midpoints = [(lo + hi) / 2 for lo, hi in zip(lower_values, upper_values)]
    radii = [(hi - lo) / 2 for lo, hi in zip(lower_values, upper_values)]

    midpoint_h0 = hankel(midpoints, 8, 0)
    midpoint_h1 = hankel(midpoints, 8, 1)
    radius_h0 = hankel(radii, 8, 0)
    radius_h1 = hankel(radii, 8, 1)
    lower_h0 = hankel(lower_values, 8, 0)
    upper_h0 = hankel(upper_values, 8, 0)

    schur_a = [[midpoints[i + j + 2] for j in range(7)] for i in range(7)]
    schur_v = [midpoints[i + 1] for i in range(7)]
    schur_c = solve_linear(schur_a, schur_v)
    schur_theta = sum(x * y for x, y in zip(schur_v, schur_c))
    schur_vector = [Fraction(1)] + [-value for value in schur_c]
    schur_quadratic = interval_quadratic(lower_h0, upper_h0, schur_vector)

    if schur_quadratic.upper < 0:
        verdict = "CERTIFIED_NEGATIVE_ZERO_ANCHOR_WITNESS"
        positive_proof = None
    else:
        try:
            pivots_h0 = exact_ldl_positive_pivots(subtract_diagonal(midpoint_h0, delta))
            pivots_h1 = exact_ldl_positive_pivots(subtract_diagonal(midpoint_h1, delta))
            epsilon_h0 = maximum_row_sum(radius_h0)
            epsilon_h1 = maximum_row_sum(radius_h1)
            if epsilon_h0 >= delta or epsilon_h1 >= delta:
                raise CertificateError("moment interval radius is not below delta")
            positive_proof = {
                "delta": fraction_json(delta),
                "H0_pivots": [fraction_json(value) for value in pivots_h0],
                "H1_pivots": [fraction_json(value) for value in pivots_h1],
                "H0_radius": fraction_json(epsilon_h0),
                "H1_radius": fraction_json(epsilon_h1),
                "H0_margin": fraction_json(delta - epsilon_h0),
                "H1_margin": fraction_json(delta - epsilon_h1),
            }
            verdict = "CERTIFIED_POSITIVE_FULL_DEGREE15_ZERO_ANCHORED_CONE"
        except CertificateError:
            positive_proof = None
            verdict = "UNRESOLVED_ZERO_ANCHOR_CONE"

    proof_object = {
        "b0": {
            "lower": str(b0_decimal.lower),
            "upper": str(b0_decimal.upper),
        },
        "schur_theta_midpoint": fraction_json(schur_theta),
        "schur_vector": [fraction_json(value) for value in schur_vector],
        "schur_quadratic": {
            "lower": fraction_json(schur_quadratic.lower),
            "upper": fraction_json(schur_quadratic.upper),
        },
        "positive_proof": positive_proof,
    }
    proof_digest = hashlib.sha256(
        json.dumps(proof_object, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()

    return {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "analytic_claim": "L-9311",
        "parent_halfline_claim": "L-9310",
        "ordinate": old_certificate.get("ordinate"),
        "old_node_count": 16,
        "new_node": {"x": {"numerator": 0, "denominator": 1}, "u": {"numerator": 0, "denominator": 1}},
        "degree_bound": 15,
        "old_basis_sha256": file_sha256(old_basis_path),
        "old_certificate_sha256": actual_source,
        "zero_low_sha256": file_sha256(zero_low_path),
        "zero_high_sha256": file_sha256(zero_high_path),
        "zero_precision_bits": [zero_low.get("precision_bits"), zero_high.get("precision_bits")],
        "b0_interval": {"lower": str(b0_decimal.lower), "upper": str(b0_decimal.upper)},
        "b0_width": str(b0_decimal.upper - b0_decimal.lower),
        "schur_theta_midpoint_decimal": decimal_string(schur_theta),
        "schur_midpoint_gap_decimal": decimal_string((b0.lower + b0.upper) / 2 - schur_theta),
        "schur_witness_polynomial_coefficients": [fraction_json(value) for value in schur_vector],
        "schur_witness_quadratic_interval": {
            "lower_decimal": decimal_string(schur_quadratic.lower),
            "upper_decimal": decimal_string(schur_quadratic.upper),
        },
        "positive_proof": positive_proof,
        "exact_proof_object_sha256": proof_digest,
        "verdict": verdict,
        "proof_boundary": (
            "Directed completed-xi rectangles, exact rational logarithm tails, directed Decimal final contraction, "
            "and exact rational moment-matrix verification. The RH implication inherits the parent canonical-product "
            "and total-count-deflation claims."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-certificate", type=Path, required=True)
    parser.add_argument("--old-basis", type=Path, required=True)
    parser.add_argument("--zero-low", type=Path, required=True)
    parser.add_argument("--zero-high", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=220)
    parser.add_argument("--decimal-precision", type=int, default=230)
    parser.add_argument("--delta-numerator", type=int, default=1)
    parser.add_argument("--delta-denominator", type=int, default=100000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.delta_denominator <= 0:
        print(json.dumps({"verified": False, "error": "bad delta denominator"}), file=sys.stderr)
        return 2
    try:
        result = verify(
            args.old_certificate,
            args.old_basis,
            args.zero_low,
            args.zero_high,
            args.log_terms,
            args.decimal_precision,
            Fraction(args.delta_numerator, args.delta_denominator),
        )
    except (OSError, CertificateError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 1 if result["verdict"] == "CERTIFIED_NEGATIVE_ZERO_ANCHOR_WITNESS" else 0


if __name__ == "__main__":
    raise SystemExit(main())
