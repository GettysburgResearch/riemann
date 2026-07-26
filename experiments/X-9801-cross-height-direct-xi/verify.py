#!/usr/bin/env python3
"""Exact checker for cross-height algebraic direct-xi product witnesses.

The checker evaluates no special function and uses no floating-point arithmetic.
For each height it requires an integer exponent vector of sum zero. It rebuilds

    A(z) = product_{n_rj>0} ((z-(T_r-O))^2+u_rj)^n_rj,
    B(z) = product_{n_rj<0} ((z-(T_r-O))^2+u_rj)^(-n_rj),

and proves A(z)-B(z)>0 on the real line by an exact Sturm no-real-root
certificate. It then contracts the corresponding product inequality from exact
nonnegative intervals for H_T(u)=|xi(1/2+sqrt(u)+iT)|^2.
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

SCHEMA = "riemann.cross-height-direct-xi-algebraic.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
PRODUCTION = "RIEMANN_XI_DIRECTED"
SYNTHETIC = "SYNTHETIC_MODEL"
POLYNOMIAL_GATE = "STRICT_POSITIVE_NO_REAL_ROOT_STURM"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def mul(self, other: "Interval") -> "Interval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(values), max(values))

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def pow_nonnegative(self, exponent: int) -> "Interval":
        if exponent < 0:
            raise CertificateError("negative interval exponent")
        if self.lower < 0:
            raise CertificateError("power input must be nonnegative")
        return Interval(self.lower**exponent, self.upper**exponent)


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


def interval(value: Any, name: str) -> Interval:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    result = Interval(
        rational(value.get("lower"), f"{name}.lower"),
        rational(value.get("upper"), f"{name}.upper"),
    )
    if result.lower < 0:
        raise CertificateError(f"{name} must be nonnegative")
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


# Polynomials are ascending coefficient arrays over Fraction.
def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def poly_sub(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return poly_add(left, [-value for value in right])


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_pow(base: list[Fraction], exponent: int) -> list[Fraction]:
    if exponent < 0:
        raise CertificateError("negative polynomial exponent")
    out = [Fraction(1)]
    factor = base[:]
    power = exponent
    while power:
        if power & 1:
            out = poly_mul(out, factor)
        power >>= 1
        if power:
            factor = poly_mul(factor, factor)
    return out


def poly_derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) <= 1:
        return [Fraction(0)]
    return trim([Fraction(index) * poly[index] for index in range(1, len(poly))])


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
        raise CertificateError("zero polynomial has no strict positivity certificate")
    derivative = poly_derivative(poly)
    if derivative == [0]:
        return [poly]
    sequence = [poly, derivative]
    while sequence[-1] != [0]:
        _, remainder = poly_divmod(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append([-value for value in remainder])
    return sequence


def sign_at_infinity(poly: list[Fraction], positive: bool) -> int:
    leading = poly[-1]
    sign = 1 if leading > 0 else -1
    if not positive and (len(poly) - 1) % 2:
        sign = -sign
    return sign


def variations(signs: list[int]) -> int:
    clean = [value for value in signs if value != 0]
    return sum(left != right for left, right in zip(clean, clean[1:]))


def distinct_real_root_count(poly: list[Fraction]) -> int:
    sequence = sturm_sequence(poly)
    at_minus = variations([sign_at_infinity(item, False) for item in sequence])
    at_plus = variations([sign_at_infinity(item, True) for item in sequence])
    count = at_minus - at_plus
    if count < 0:
        raise CertificateError("internal Sturm count became negative")
    return count


def evaluate_poly(poly: list[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def polynomial_json(poly: list[Fraction]) -> list[dict[str, int]]:
    return [fj(value) for value in poly]


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
        scale = exact_int(
            raw_height.get("common_xi_scale_power_of_two", 0),
            f"height {identifier}.common_xi_scale_power_of_two",
        )
        source_sha = raw_height.get("source_sha256")
        if classification == PRODUCTION:
            source_sha = validate_digest(source_sha, f"height {identifier}.source_sha256")
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
            u = rational(raw_point.get("u"), f"height {identifier} point {point_id}.u")
            if u <= 0:
                raise CertificateError("all squared horizontal nodes must be positive")
            h_interval = interval(
                raw_point.get("h_interval"),
                f"height {identifier} point {point_id}.h_interval",
            )
            points[point_id] = {"u": u, "h": h_interval}
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
    seen: set[tuple[str, str]] = set()
    sums = {identifier: 0 for identifier in heights}
    for term_index, raw in enumerate(raw_terms):
        if not isinstance(raw, dict):
            raise CertificateError(f"terms[{term_index}] must be an object")
        height_id = raw.get("height")
        point_id = raw.get("point")
        if height_id not in heights or point_id not in heights[height_id]["points"]:
            raise CertificateError("term references an unknown height or point")
        key = (height_id, point_id)
        if key in seen:
            raise CertificateError("duplicate height/point term")
        seen.add(key)
        exponent = exact_int(raw.get("exponent"), f"terms[{term_index}].exponent")
        if exponent == 0:
            raise CertificateError("zero exponent terms must be omitted")
        sums[height_id] += exponent
        terms.append(
            {
                "height": height_id,
                "point": point_id,
                "exponent": exponent,
                "u": heights[height_id]["points"][point_id]["u"],
                "h": heights[height_id]["points"][point_id]["h"],
                "offset": heights[height_id]["offset"],
            }
        )
    if any(total != 0 for total in sums.values()):
        raise CertificateError("exponents must sum to zero separately at every height")

    positive_poly = [Fraction(1)]
    negative_poly = [Fraction(1)]
    left_interval = Interval(Fraction(1), Fraction(1))
    right_interval = Interval(Fraction(1), Fraction(1))
    for term in terms:
        offset = term["offset"]
        quadratic = [offset * offset + term["u"], -2 * offset, Fraction(1)]
        exponent = term["exponent"]
        if exponent > 0:
            positive_poly = poly_mul(positive_poly, poly_pow(quadratic, exponent))
            left_interval = left_interval.mul(term["h"].pow_nonnegative(exponent))
        else:
            power = -exponent
            negative_poly = poly_mul(negative_poly, poly_pow(quadratic, power))
            right_interval = right_interval.mul(term["h"].pow_nonnegative(power))

    response_poly = poly_sub(positive_poly, negative_poly)
    roots = distinct_real_root_count(response_poly)
    value_at_origin = evaluate_poly(response_poly, Fraction(0))
    strict_positive = roots == 0 and value_at_origin > 0
    gate = data.get("polynomial_gate")
    if not isinstance(gate, dict) or gate.get("status") != POLYNOMIAL_GATE:
        raise CertificateError("missing strict Sturm polynomial gate")
    if not strict_positive:
        raise CertificateError(
            "reconstructed response polynomial is not certified strictly positive"
        )

    final_interval = left_interval.sub(right_interval)
    if final_interval.upper < 0:
        status = "CERTIFIED_NEGATIVE"
    elif final_interval.lower >= 0:
        status = "CERTIFIED_NONNEGATIVE"
    else:
        status = "UNRESOLVED"
    if classification == PRODUCTION and status == "CERTIFIED_NEGATIVE":
        verdict = "NEGATIVE_CROSS_HEIGHT_DIRECT_XI_WITNESS_PENDING_REVIEW"
    elif classification == SYNTHETIC and status == "CERTIFIED_NEGATIVE":
        verdict = "SYNTHETIC_STRICT_SEPARATION"
    elif status == "UNRESOLVED":
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_PORTFOLIO"

    proof_object = {
        "origin": fj(origin),
        "height_exponent_sums": sums,
        "positive_product_polynomial": polynomial_json(positive_poly),
        "negative_product_polynomial": polynomial_json(negative_poly),
        "response_polynomial": polynomial_json(response_poly),
        "response_degree": len(response_poly) - 1,
        "distinct_real_roots": roots,
        "response_at_origin": fj(value_at_origin),
        "polynomial_gate": POLYNOMIAL_GATE,
    }
    return {
        "schema": SCHEMA,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "height_count": len(heights),
        "term_count": len(terms),
        "height_exponent_sums": sums,
        "polynomial": {
            "degree": len(response_poly) - 1,
            "distinct_real_roots": roots,
            "value_at_origin": fj(value_at_origin),
            "coefficients_ascending": polynomial_json(response_poly),
            "strictly_positive_on_real_line": strict_positive,
            "proof_object_sha256": canonical_sha(proof_object),
        },
        "left_product_interval": ij(left_interval),
        "right_product_interval": ij(right_interval),
        "difference_interval": ij(final_interval),
        "status": status,
        "verdict": verdict,
        "source_fingerprints": {
            identifier: {
                "source_sha256": height["source_sha256"],
                "common_xi_scale_power_of_two": height["scale"],
            }
            for identifier, height in sorted(heights.items())
        },
        "scope_warning": (
            "The checker proves exact polynomial positivity and exact interval "
            "contraction only. A production negative additionally requires review of "
            "L-9801, independent completed-xi reproduction, and normalization audit."
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
