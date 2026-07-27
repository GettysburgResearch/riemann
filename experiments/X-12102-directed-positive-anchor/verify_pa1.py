#!/usr/bin/env python3
"""Directed PA-1 contraction and exact two-sided degree-15 cone checker.

This verifier reuses the reviewed interval, logarithm, source-binding, and exact
linear-algebra primitives from X-9309.  It adds the L-12101 positive-anchor
recurrence, full-versus-reduced contraction overlap, both rank-one witness
directions, and a complete H0/H1 interval positive-definiteness gate.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PARENT_PATH = (
    ROOT / "X-9309-zero-anchor-degree15" / "verify_zero_anchor.py"
)
SPEC = importlib.util.spec_from_file_location(
    "x9309_parent_verify", PARENT_PATH
)
assert SPEC is not None and SPEC.loader is not None
parent = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = parent
SPEC.loader.exec_module(parent)

RationalInterval = parent.RationalInterval
CertificateError = parent.CertificateError
NORMALIZATION = parent.NORMALIZATION
OUTPUT_SCHEMA = "riemann.x12102-directed-positive-anchor-pa1.v1"
ANCHOR = Fraction(1)


def positive_point(primitive: dict[str, Any], name: str) -> dict[str, Any]:
    if primitive.get("normalization_id") != NORMALIZATION:
        raise CertificateError(f"{name} normalization mismatch")
    points = primitive.get("points")
    if (
        not isinstance(points, list)
        or len(points) != 1
        or not isinstance(points[0], dict)
    ):
        raise CertificateError(f"{name} must contain exactly one point")
    point = points[0]
    if parent.fraction(point.get("x"), f"{name}.x") != 1:
        raise CertificateError(f"{name} point is not x=1")
    if point.get("functional_equation_residual_contains_zero") is not True:
        raise CertificateError(f"{name} functional-equation gate failed")
    if parent.modulus_square(point).lower <= 0:
        raise CertificateError(f"{name} does not prove H_T(1)>0")
    return point


def compare_primitives(
    low: dict[str, Any], high: dict[str, Any]
) -> None:
    if parent.exact_int(
        low.get("precision_bits"), "low.precision_bits"
    ) >= parent.exact_int(
        high.get("precision_bits"), "high.precision_bits"
    ):
        raise CertificateError("positive-anchor precision order is invalid")
    for field in (
        "normalization_id",
        "common_xi_scale_power_of_two",
        "ordinate",
    ):
        if low.get(field) != high.get(field):
            raise CertificateError(
                f"positive-anchor primitive {field} mismatch"
            )
    low_point = positive_point(low, "low positive-anchor primitive")
    high_point = positive_point(high, "high positive-anchor primitive")
    for component in ("real", "imag"):
        outer = parent.parse_interval(
            low_point["xi_rectangle"][component],
            f"low.{component}",
        )
        inner = parent.parse_interval(
            high_point["xi_rectangle"][component],
            f"high.{component}",
        )
        if not (
            outer.lower <= inner.lower <= inner.upper <= outer.upper
        ):
            raise CertificateError(
                f"high-precision {component} interval is not nested"
            )


def interval_intersection(
    left: RationalInterval, right: RationalInterval
) -> RationalInterval:
    lower = max(left.lower, right.lower)
    upper = min(left.upper, right.upper)
    if lower > upper:
        raise CertificateError(
            "full and reduced positive-anchor contractions are disjoint"
        )
    return RationalInterval(lower, upper)


def interval_json(value: RationalInterval) -> dict[str, object]:
    return {
        "lower": parent.fraction_json(value.lower),
        "upper": parent.fraction_json(value.upper),
        "lower_decimal": parent.decimal_string(value.lower),
        "upper_decimal": parent.decimal_string(value.upper),
    }


def poly_multiply_linear(
    coefficients: list[Fraction], constant: Fraction
) -> list[Fraction]:
    output = [Fraction(0) for _ in range(len(coefficients) + 1)]
    for index, value in enumerate(coefficients):
        output[index] += constant * value
        output[index + 1] += value
    return output


def denominator_polynomial(nodes: list[Fraction]) -> list[Fraction]:
    result = [Fraction(1)]
    for node in nodes:
        result = poly_multiply_linear(result, node)
    return result


def poly_evaluate(
    coefficients: list[Fraction], value: Fraction
) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def poly_divide_linear(
    coefficients: list[Fraction], constant: Fraction
) -> list[Fraction]:
    """Divide a low-to-high polynomial by y+constant exactly."""
    if len(coefficients) < 2:
        raise CertificateError("polynomial is too small for linear division")
    degree = len(coefficients) - 1
    quotient = [Fraction(0) for _ in range(degree)]
    quotient[-1] = coefficients[-1]
    for index in range(degree - 2, -1, -1):
        quotient[index] = (
            coefficients[index + 1]
            - constant * quotient[index + 1]
        )
    remainder = coefficients[0] - constant * quotient[0]
    if remainder != 0:
        raise CertificateError("nonzero polynomial-division remainder")
    return quotient


def poly_add(
    left: list[Fraction], right: list[Fraction]
) -> list[Fraction]:
    size = max(len(left), len(right))
    output = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def reduced_coefficients(
    old_nodes: list[Fraction], reference_index: int = 0
) -> tuple[Fraction, list[Fraction]]:
    denominator = denominator_polynomial(old_nodes)
    at_negative_anchor = poly_evaluate(denominator, -ANCHOR)
    if at_negative_anchor == 0:
        raise CertificateError("positive anchor collides with an old node")
    beta = -Fraction(1, 1) / at_negative_anchor

    numerator = [-value / at_negative_anchor for value in denominator]
    numerator[0] += 1
    gamma_polynomial = poly_divide_linear(numerator, ANCHOR)

    reference_quotient = poly_divide_linear(
        denominator, old_nodes[reference_index]
    )
    reference_term = [
        value / at_negative_anchor for value in reference_quotient
    ]
    reduced = poly_add(gamma_polynomial, reference_term)
    if len(reduced) > 15:
        raise CertificateError(
            "reduced positive-anchor polynomial exceeds degree fourteen"
        )
    reduced += [Fraction(0)] * (15 - len(reduced))

    # Exact polynomial identity from L-12101.
    left = poly_multiply_linear(gamma_polynomial, ANCHOR)
    left = poly_add(
        left,
        [-beta * value for value in denominator],
    )
    if left != [Fraction(1)]:
        raise CertificateError("positive-anchor response identity failed")
    return beta, reduced


def interval_linear_combination(
    coefficients: list[Fraction],
    intervals: list[RationalInterval],
) -> RationalInterval:
    if len(coefficients) != len(intervals):
        raise CertificateError("linear-combination dimension mismatch")
    result = RationalInterval(Fraction(0), Fraction(0))
    for coefficient, interval in zip(coefficients, intervals):
        result = result.add(interval.scale(coefficient))
    return result


def verify(
    old_certificate_path: Path,
    old_basis_path: Path,
    anchor_low_path: Path,
    anchor_high_path: Path,
    log_terms: int,
    delta: Fraction,
) -> dict[str, Any]:
    old_certificate = parent.load_json(old_certificate_path)
    old_basis, old_moments = parent.load_basis(old_basis_path)
    anchor_low = parent.load_json(anchor_low_path)
    anchor_high = parent.load_json(anchor_high_path)
    compare_primitives(anchor_low, anchor_high)

    if old_certificate.get("classification") != "RIEMANN_XI_DIRECTED":
        raise CertificateError(
            "old certificate is not directed Riemann-xi data"
        )
    if old_certificate.get("normalization_id") != NORMALIZATION:
        raise CertificateError("old certificate normalization mismatch")
    for field in ("ordinate", "common_xi_scale_power_of_two"):
        if old_certificate.get(field) != anchor_high.get(field):
            raise CertificateError(
                f"positive anchor and old certificate {field} mismatch"
            )

    old_file_digest = parent.file_sha256(old_certificate_path)
    old_internal_digest = old_certificate.get("certificate_sha256")
    declared_digest = old_basis.get("source_certificate_sha256")
    if declared_digest not in {old_file_digest, old_internal_digest}:
        raise CertificateError(
            "old basis certificate digest matches neither preserved convention"
        )
    source = old_certificate.get("source")
    declared_primitive = old_basis.get("primitive_sha256")
    if (
        not isinstance(source, dict)
        or declared_primitive != source.get("primitive_sha256")
    ):
        raise CertificateError("old basis primitive digest mismatch")
    if old_basis.get("ordinate") != old_certificate.get("ordinate"):
        raise CertificateError("old basis ordinate mismatch")

    raw_points = old_certificate.get("points")
    if not isinstance(raw_points, list) or len(raw_points) != 16:
        raise CertificateError(
            "expected the sixteen-node old certificate"
        )
    old_points = sorted(
        raw_points,
        key=lambda point: parent.fraction(point.get("u"), "point.u"),
    )
    old_nodes = [
        parent.fraction(point.get("u"), "point.u")
        for point in old_points
    ]
    if old_nodes[0] <= 0 or any(
        old_nodes[index] >= old_nodes[index + 1]
        for index in range(15)
    ):
        raise CertificateError(
            "old nodes must be strictly increasing and positive"
        )
    if ANCHOR in set(old_nodes):
        raise CertificateError("positive anchor duplicates an old node")

    shells = parent.deflation_shells(old_certificate)
    log = parent.ExactLogEncloser(log_terms)
    old_residuals = [
        parent.residual_interval(point, node, shells, log)
        for point, node in zip(old_points, old_nodes)
    ]
    anchor_residual = parent.residual_interval(
        positive_point(anchor_high, "high positive-anchor primitive"),
        ANCHOR,
        shells,
        log,
    )

    # Full seventeen-point response-1 contraction.
    full_nodes = old_nodes + [ANCHOR]
    full_residuals = old_residuals + [anchor_residual]
    full_coefficients = parent.basis_vector(full_nodes, 0)
    if sum(full_coefficients) != 0:
        raise CertificateError(
            "positive-anchor full response vector is not zero sum"
        )
    full_b0 = interval_linear_combination(
        full_coefficients, full_residuals
    )

    # Reduced one-new-point contraction from L-12101.
    beta, polynomial = reduced_coefficients(old_nodes, 0)
    point_difference = anchor_residual.sub(old_residuals[0])
    reduced_b0 = point_difference.scale(beta).add(
        interval_linear_combination(polynomial, old_moments)
    )
    b0 = interval_intersection(full_b0, reduced_b0)

    moments = [b0]
    for old_moment in old_moments:
        moments.append(old_moment.sub(moments[-1].scale(ANCHOR)))
    if len(moments) != 16:
        raise CertificateError("positive-anchor moment count mismatch")

    lows = [value.lower for value in moments]
    highs = [value.upper for value in moments]
    mids = [(low + high) / 2 for low, high in zip(lows, highs)]
    radii = [(high - low) / 2 for low, high in zip(lows, highs)]

    midpoint_h0 = parent.hankel(mids, 8, 0)
    midpoint_h1 = parent.hankel(mids, 8, 1)
    radius_h0 = parent.hankel(radii, 8, 0)
    radius_h1 = parent.hankel(radii, 8, 1)
    lower_h0 = parent.hankel(lows, 8, 0)
    upper_h0 = parent.hankel(highs, 8, 0)
    lower_h1 = parent.hankel(lows, 8, 1)
    upper_h1 = parent.hankel(highs, 8, 1)

    z = [(-ANCHOR) ** index for index in range(8)]
    lower_direction = parent.solve_linear(midpoint_h0, z)
    upper_direction = parent.solve_linear(midpoint_h1, z)
    q0 = sum(x * y for x, y in zip(z, lower_direction))
    q1 = sum(x * y for x, y in zip(z, upper_direction))
    if q0 <= 0 or q1 <= 0:
        raise CertificateError("rank-one reference is not positive")
    reference = (b0.lower + b0.upper) / 2
    lower_threshold = reference - 1 / q0
    upper_threshold = reference + 1 / (ANCHOR * q1)

    lower_witness_interval = parent.interval_quadratic(
        lower_h0, upper_h0, lower_direction
    )
    upper_witness_interval = parent.interval_quadratic(
        lower_h1, upper_h1, upper_direction
    )

    positive_proof: dict[str, Any] | None = None
    negative_channel: str | None = None
    if lower_witness_interval.upper < 0:
        verdict = "CERTIFIED_NEGATIVE_PA1_H0_SQUARE"
        negative_channel = "H0"
    elif upper_witness_interval.upper < 0:
        verdict = "CERTIFIED_NEGATIVE_PA1_H1_Y_SQUARE"
        negative_channel = "H1"
    else:
        try:
            h0_pivots = parent.exact_ldl_positive_pivots(
                parent.subtract_diagonal(midpoint_h0, delta)
            )
            h1_pivots = parent.exact_ldl_positive_pivots(
                parent.subtract_diagonal(midpoint_h1, delta)
            )
            h0_radius = parent.maximum_row_sum(radius_h0)
            h1_radius = parent.maximum_row_sum(radius_h1)
            if h0_radius >= delta or h1_radius >= delta:
                raise CertificateError(
                    "positive-anchor moment radius is not below delta"
                )
            positive_proof = {
                "delta": parent.fraction_json(delta),
                "H0_pivots": [
                    parent.fraction_json(value) for value in h0_pivots
                ],
                "H1_pivots": [
                    parent.fraction_json(value) for value in h1_pivots
                ],
                "H0_radius": parent.fraction_json(h0_radius),
                "H1_radius": parent.fraction_json(h1_radius),
                "H0_margin": parent.fraction_json(delta - h0_radius),
                "H1_margin": parent.fraction_json(delta - h1_radius),
            }
            verdict = "CERTIFIED_POSITIVE_FULL_DEGREE15_PA1_CONE"
        except CertificateError:
            verdict = "UNRESOLVED_PA1_CONE"

    proof_object = {
        "full_b0_interval": interval_json(full_b0),
        "reduced_b0_interval": interval_json(reduced_b0),
        "intersection_b0_interval": interval_json(b0),
        "beta": parent.fraction_json(beta),
        "reduced_polynomial": [
            parent.fraction_json(value) for value in polynomial
        ],
        "reference_b0": parent.fraction_json(reference),
        "lower_threshold": parent.fraction_json(lower_threshold),
        "upper_threshold": parent.fraction_json(upper_threshold),
        "lower_direction": [
            parent.fraction_json(value) for value in lower_direction
        ],
        "upper_direction": [
            parent.fraction_json(value) for value in upper_direction
        ],
        "lower_witness_interval": interval_json(lower_witness_interval),
        "upper_witness_interval": interval_json(upper_witness_interval),
        "positive_proof": positive_proof,
    }
    proof_digest = hashlib.sha256(
        json.dumps(
            proof_object,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode("ascii")
    ).hexdigest()

    return {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "analytic_claim": "L-12101",
        "parent_halfline_claim": "L-9310",
        "ordinate": old_certificate.get("ordinate"),
        "old_node_count": 16,
        "new_node": {
            "x": {"numerator": 1, "denominator": 1},
            "u": {"numerator": 1, "denominator": 1},
        },
        "anchor_low_precision": parent.exact_int(
            anchor_low.get("precision_bits"), "low.precision_bits"
        ),
        "anchor_high_precision": parent.exact_int(
            anchor_high.get("precision_bits"), "high.precision_bits"
        ),
        "full_b0_interval": interval_json(full_b0),
        "reduced_b0_interval": interval_json(reduced_b0),
        "intersection_b0_interval": interval_json(b0),
        "full_reduced_overlap": True,
        "lower_schur_threshold": parent.fraction_json(lower_threshold),
        "upper_schur_threshold": parent.fraction_json(upper_threshold),
        "lower_witness_interval": interval_json(lower_witness_interval),
        "upper_witness_interval": interval_json(upper_witness_interval),
        "negative_channel": negative_channel,
        "positive_proof": positive_proof,
        "verdict": verdict,
        "exact_proof_object_sha256": proof_digest,
        "source": {
            "old_certificate_sha256": parent.file_sha256(
                old_certificate_path
            ),
            "old_basis_sha256": parent.file_sha256(old_basis_path),
            "anchor_low_sha256": parent.file_sha256(anchor_low_path),
            "anchor_high_sha256": parent.file_sha256(anchor_high_path),
        },
        "proof_boundary": (
            "This decides only the exact PA-1 table under inherited "
            "direct-xi, response, and count-deflation gates. A negative "
            "requires independent primitive reproduction before promotion."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-certificate", type=Path, required=True)
    parser.add_argument("--old-basis", type=Path, required=True)
    parser.add_argument("--anchor-low", type=Path, required=True)
    parser.add_argument("--anchor-high", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=240)
    parser.add_argument(
        "--delta", type=Fraction, default=Fraction(1, 1_000_000)
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(
            args.old_certificate,
            args.old_basis,
            args.anchor_low,
            args.anchor_high,
            args.log_terms,
            args.delta,
        )
        code = 1 if result["verdict"].startswith("CERTIFIED_NEGATIVE") else 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {
            "schema": OUTPUT_SCHEMA,
            "classification": "REJECTED",
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
