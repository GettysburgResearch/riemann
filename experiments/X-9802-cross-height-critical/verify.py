#!/usr/bin/env python3
"""Exact checker for rational cross-height logarithmic direct-xi portfolios.

The checker uses only integers and fractions.Fraction. It reconstructs the
low-degree numerator of the one-zero response derivative, verifies an exhaustive
set of rational Sturm root isolators, proves a nonnegative response interval at
every critical point, and contracts the finite direct-xi logarithmic portfolio.
It evaluates no special function and uses no floating-point arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SCHEMA = "riemann.cross-height-log-critical.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
PRODUCTION = "RIEMANN_XI_DIRECTED"
SYNTHETIC = "SYNTHETIC_MODEL"
CRITICAL_GATE = "EXHAUSTIVE_STURM_CRITICAL_VALUES"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def scale(self, scalar: Fraction) -> "Interval":
        values = (self.lower * scalar, self.upper * scalar)
        return Interval(min(values), max(values))


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise CertificateError(f"{name} must be integer text") from exc
    raise CertificateError(f"{name} must be an integer")


def rational(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(value.get("numerator"), f"{name}.numerator")
    denominator = exact_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(value: Any, name: str, *, positive: bool = False) -> Interval:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    result = Interval(
        rational(value.get("lower"), f"{name}.lower"),
        rational(value.get("upper"), f"{name}.upper"),
    )
    if positive and result.lower <= 0:
        raise CertificateError(f"{name} must have a strictly positive lower endpoint")
    return result


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_digest(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a SHA-256 hexadecimal digest")
    return value.lower()


# Polynomials are ascending Fraction coefficient arrays.
def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    result = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return trim([value * scalar for value in poly])


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def poly_derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) <= 1:
        return [Fraction(0)]
    return trim([Fraction(index) * poly[index] for index in range(1, len(poly))])


def poly_eval(poly: list[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def poly_divmod(
    numerator: list[Fraction], denominator: list[Fraction]
) -> tuple[list[Fraction], list[Fraction]]:
    numerator = trim(numerator[:])
    denominator = trim(denominator[:])
    if denominator == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0) for _ in range(len(numerator) - len(denominator) + 1)]
    remainder = numerator[:]
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + shift] -= coefficient * value
        trim(remainder)
    return trim(quotient), trim(remainder)


def sturm_sequence(poly: list[Fraction]) -> list[list[Fraction]]:
    poly = trim(poly[:])
    if poly == [0]:
        raise CertificateError("zero polynomial has no Sturm sequence")
    derivative = poly_derivative(poly)
    if derivative == [0]:
        return [poly]
    sequence = [poly, derivative]
    while True:
        _, remainder = poly_divmod(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append(poly_scale(remainder, Fraction(-1)))
    return sequence


def sign(value: Fraction) -> int:
    return 1 if value > 0 else (-1 if value < 0 else 0)


def variations(signs: list[int]) -> int:
    clean = [value for value in signs if value]
    return sum(left != right for left, right in zip(clean, clean[1:]))


def variation_at(sequence: list[list[Fraction]], value: Fraction) -> int:
    return variations([sign(poly_eval(poly, value)) for poly in sequence])


def sign_at_infinity(poly: list[Fraction], positive: bool) -> int:
    result = sign(poly[-1])
    if not positive and (len(poly) - 1) % 2:
        result = -result
    return result


def total_real_roots(sequence: list[list[Fraction]]) -> int:
    minus = variations([sign_at_infinity(poly, False) for poly in sequence])
    plus = variations([sign_at_infinity(poly, True) for poly in sequence])
    return minus - plus


def roots_between(
    sequence: list[list[Fraction]], polynomial: list[Fraction], lower: Fraction, upper: Fraction
) -> int:
    if not lower < upper:
        raise CertificateError("root interval endpoints must increase")
    if poly_eval(polynomial, lower) == 0 or poly_eval(polynomial, upper) == 0:
        raise CertificateError("root interval endpoint is itself a derivative root")
    return variation_at(sequence, lower) - variation_at(sequence, upper)


def polynomial_json(poly: list[Fraction]) -> list[dict[str, int]]:
    return [fj(value) for value in poly]


def atanh_log_interval(value: Fraction, terms: int) -> Interval:
    if not Fraction(1) <= value <= Fraction(2):
        raise CertificateError("internal logarithm range reduction failed")
    z = (value - 1) / (value + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for index in range(terms):
        partial += power / (2 * index + 1)
        power *= z2
    lower = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lower, lower + tail)


def power_of_two(exponent: int) -> Fraction:
    return Fraction(1 << exponent) if exponent >= 0 else Fraction(1, 1 << (-exponent))


def log_positive_fraction(
    value: Fraction, terms: int, log_two: Interval | None = None
) -> Interval:
    if value <= 0:
        raise CertificateError("logarithm input must be positive")
    exponent = value.numerator.bit_length() - value.denominator.bit_length()
    reduced = value / power_of_two(exponent)
    while reduced < 1:
        exponent -= 1
        reduced *= 2
    while reduced >= 2:
        exponent += 1
        reduced /= 2
    result = atanh_log_interval(reduced, terms)
    log_two = log_two or atanh_log_interval(Fraction(2), terms)
    return result.add(log_two.scale(Fraction(exponent)))


def log_positive_interval(value: Interval, terms: int, log_two: Interval) -> Interval:
    if value.lower <= 0:
        raise CertificateError("logarithm interval must be strictly positive")
    lower = log_positive_fraction(value.lower, terms, log_two).lower
    upper = log_positive_fraction(value.upper, terms, log_two).upper
    return Interval(lower, upper)


def quadratic_range(
    offset: Fraction, node: Fraction, lower: Fraction, upper: Fraction
) -> Interval:
    left = (lower - offset) ** 2 + node
    right = (upper - offset) ** 2 + node
    minimum = node if lower <= offset <= upper else min(left, right)
    return Interval(minimum, max(left, right))


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    classification = data.get("classification")
    if classification not in (PRODUCTION, SYNTHETIC):
        raise CertificateError("unsupported classification")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("normalization mismatch")
    origin = rational(data.get("origin"), "origin")

    raw_heights = data.get("heights")
    if not isinstance(raw_heights, list) or not raw_heights:
        raise CertificateError("heights must be a nonempty array")
    heights: dict[str, dict[str, Any]] = {}
    for height_index, raw_height in enumerate(raw_heights):
        if not isinstance(raw_height, dict):
            raise CertificateError(f"heights[{height_index}] must be an object")
        identifier = raw_height.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in heights:
            raise CertificateError("height IDs must be nonempty and unique")
        ordinate = rational(raw_height.get("ordinate"), f"height {identifier}.ordinate")
        source_sha = raw_height.get("source_sha256")
        if classification == PRODUCTION:
            source_sha = validate_digest(source_sha, f"height {identifier}.source_sha256")
        scale = exact_int(
            raw_height.get("common_xi_scale_power_of_two", 0),
            f"height {identifier}.common_xi_scale_power_of_two",
        )
        raw_points = raw_height.get("points")
        if not isinstance(raw_points, list) or not raw_points:
            raise CertificateError(f"height {identifier} has no points")
        points: dict[str, dict[str, Any]] = {}
        for point_index, raw_point in enumerate(raw_points):
            if not isinstance(raw_point, dict):
                raise CertificateError("point must be an object")
            point_id = raw_point.get("id")
            if not isinstance(point_id, str) or not point_id or point_id in points:
                raise CertificateError("point IDs must be nonempty and unique per height")
            node = rational(raw_point.get("u"), f"height {identifier} point {point_id}.u")
            if node <= 0:
                raise CertificateError("all squared horizontal nodes must be positive")
            h_value = interval(
                raw_point.get("h_interval"),
                f"height {identifier} point {point_id}.h_interval",
                positive=True,
            )
            points[point_id] = {"u": node, "h": h_value}
        heights[identifier] = {
            "ordinate": ordinate,
            "offset": ordinate - origin,
            "scale": scale,
            "source_sha256": source_sha,
            "points": points,
        }

    raw_terms = data.get("terms")
    if not isinstance(raw_terms, list) or not raw_terms:
        raise CertificateError("terms must be a nonempty array")
    terms: list[dict[str, Any]] = []
    sums = {identifier: Fraction(0) for identifier in heights}
    seen: set[tuple[str, str]] = set()
    for term_index, raw_term in enumerate(raw_terms):
        if not isinstance(raw_term, dict):
            raise CertificateError(f"terms[{term_index}] must be an object")
        height_id = raw_term.get("height")
        point_id = raw_term.get("point")
        if height_id not in heights or point_id not in heights[height_id]["points"]:
            raise CertificateError("term references an unknown height or point")
        key = (height_id, point_id)
        if key in seen:
            raise CertificateError("duplicate height/point term")
        seen.add(key)
        beta = rational(raw_term.get("beta"), f"terms[{term_index}].beta")
        if beta == 0:
            raise CertificateError("zero coefficient terms must be omitted")
        sums[height_id] += beta
        point = heights[height_id]["points"][point_id]
        terms.append(
            {
                "height": height_id,
                "point": point_id,
                "beta": beta,
                "offset": heights[height_id]["offset"],
                "u": point["u"],
                "h": point["h"],
            }
        )
    if any(value != 0 for value in sums.values()):
        raise CertificateError("coefficients must sum to zero separately at every height")

    # Build distinct quadratic factors and the exact derivative numerator.
    quadratics = [
        [term["offset"] ** 2 + term["u"], -2 * term["offset"], Fraction(1)]
        for term in terms
    ]
    full_denominator = [Fraction(1)]
    for quadratic in quadratics:
        full_denominator = poly_mul(full_denominator, quadratic)
    derivative_numerator = [Fraction(0)]
    for index, (term, quadratic) in enumerate(zip(terms, quadratics)):
        quotient, remainder = poly_divmod(full_denominator, quadratic)
        if remainder != [0]:
            raise CertificateError("internal quadratic denominator division failed")
        contribution = poly_mul(poly_derivative(quadratic), quotient)
        derivative_numerator = poly_add(
            derivative_numerator, poly_scale(contribution, term["beta"])
        )
    derivative_numerator = trim(derivative_numerator)

    critical = data.get("critical_certificate")
    if not isinstance(critical, dict) or critical.get("status") != CRITICAL_GATE:
        raise CertificateError("missing exhaustive critical-value gate")
    terms_count = exact_int(critical.get("log_terms", 64), "critical_certificate.log_terms")
    if terms_count < 16 or terms_count > 2048:
        raise CertificateError("log_terms must lie between 16 and 2048")
    log_two = atanh_log_interval(Fraction(2), terms_count)
    raw_root_intervals = critical.get("root_intervals", [])
    if not isinstance(raw_root_intervals, list):
        raise CertificateError("root_intervals must be an array")

    root_outputs: list[dict[str, Any]] = []
    if derivative_numerator == [0]:
        if raw_root_intervals:
            raise CertificateError("identically zero derivative must not declare roots")
        real_root_count = 0
    else:
        sequence = sturm_sequence(derivative_numerator)
        real_root_count = total_real_roots(sequence)
        previous_upper: Fraction | None = None
        counted = 0
        for root_index, raw_interval in enumerate(raw_root_intervals):
            if not isinstance(raw_interval, dict):
                raise CertificateError("root interval must be an object")
            lower = rational(raw_interval.get("lower"), f"root_intervals[{root_index}].lower")
            upper = rational(raw_interval.get("upper"), f"root_intervals[{root_index}].upper")
            if previous_upper is not None and previous_upper >= lower:
                raise CertificateError("root intervals overlap or touch")
            previous_upper = upper
            root_count = roots_between(sequence, derivative_numerator, lower, upper)
            if root_count != 1:
                raise CertificateError("each root interval must isolate exactly one root")
            counted += root_count
            response = Interval(Fraction(0), Fraction(0))
            for term in terms:
                q_range = quadratic_range(term["offset"], term["u"], lower, upper)
                log_range = log_positive_interval(q_range, terms_count, log_two)
                response = response.add(log_range.scale(term["beta"]))
            if response.lower < 0:
                raise CertificateError("critical response interval has a negative lower endpoint")
            root_outputs.append(
                {
                    "root_index": root_index,
                    "isolator": {"lower": fj(lower), "upper": fj(upper)},
                    "response_interval": ij(response),
                    "status": "CERTIFIED_NONNEGATIVE",
                }
            )
        if counted != real_root_count:
            raise CertificateError("root intervals do not exhaust all real derivative roots")

    # Contract the finite direct-xi logarithmic row.
    portfolio = Interval(Fraction(0), Fraction(0))
    for term in terms:
        log_h = log_positive_interval(term["h"], terms_count, log_two)
        portfolio = portfolio.add(log_h.scale(term["beta"]))
    if portfolio.upper < 0:
        finite_status = "CERTIFIED_NEGATIVE"
    elif portfolio.lower >= 0:
        finite_status = "CERTIFIED_NONNEGATIVE"
    else:
        finite_status = "UNRESOLVED"
    if classification == PRODUCTION and finite_status == "CERTIFIED_NEGATIVE":
        verdict = "NEGATIVE_RATIONAL_CROSS_HEIGHT_LOG_WITNESS_PENDING_REVIEW"
    elif classification == SYNTHETIC and finite_status == "CERTIFIED_NEGATIVE":
        verdict = "SYNTHETIC_STRICT_SEPARATION"
    elif finite_status == "UNRESOLVED":
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_PORTFOLIO"

    proof_object = {
        "origin": fj(origin),
        "height_coefficient_sums": {
            identifier: fj(value) for identifier, value in sorted(sums.items())
        },
        "derivative_numerator": polynomial_json(derivative_numerator),
        "derivative_degree": len(derivative_numerator) - 1,
        "distinct_real_derivative_roots": real_root_count,
        "root_intervals": [row["isolator"] for row in root_outputs],
        "critical_response_intervals": [
            row["response_interval"] for row in root_outputs
        ],
        "critical_gate": CRITICAL_GATE,
        "log_terms": terms_count,
    }
    return {
        "schema": SCHEMA,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "height_count": len(heights),
        "term_count": len(terms),
        "height_coefficient_sums": {
            identifier: fj(value) for identifier, value in sorted(sums.items())
        },
        "response_certificate": {
            "derivative_degree": len(derivative_numerator) - 1,
            "derivative_numerator_coefficients_ascending": polynomial_json(
                derivative_numerator
            ),
            "distinct_real_derivative_roots": real_root_count,
            "critical_points": root_outputs,
            "globally_nonnegative": True,
            "proof_object_sha256": canonical_sha(proof_object),
        },
        "portfolio_interval": ij(portfolio),
        "finite_status": finite_status,
        "verdict": verdict,
        "source_fingerprints": {
            identifier: {
                "source_sha256": height["source_sha256"],
                "common_xi_scale_power_of_two": height["scale"],
            }
            for identifier, height in sorted(heights.items())
        },
        "scope_warning": (
            "The checker proves exact derivative-root coverage, rational logarithm "
            "bounds and finite interval contraction only. A production negative "
            "additionally requires review of L-7501/L-9802, independent completed-xi "
            "reproduction and normalization audit."
        ),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level certificate must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verdict": "REJECTED", "error": str(exc)}, indent=2))
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(text, end="")
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    return 1 if result["verdict"] == "UNRESOLVED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
