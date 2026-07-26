#!/usr/bin/env python3
"""Exact checker for certified-zero-deflated direct-xi modulus witnesses.

The checker evaluates no special function and uses no floating-point arithmetic.
It consumes exact rational rectangles for completed-xi values, exact rational
ordinates/nodes, and externally certified lower counts for pairwise-disjoint
critical-line zero bins.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import string
import sys
from functools import lru_cache
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
PRODUCTION_GATE = "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"
SYNTHETIC_GATE = "SYNTHETIC_CRITICAL_LINE_ZERO_COUNT"
PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
GAP_SCHEMA = "riemann.x5603-line-gap-discrepancy.v1"
BLOCK_SCHEMA = "riemann.x9301-pr71-hardy-zero-block.v1"


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

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, scalar: Fraction) -> "Interval":
        a, b = self.lower * scalar, self.upper * scalar
        return Interval(min(a, b), max(a, b))

    def mul(self, other: "Interval") -> "Interval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(values), max(values))

    def pow_nonnegative(self, exponent: int) -> "Interval":
        if exponent < 0:
            raise CertificateError("negative interval exponent")
        if self.lower < 0:
            raise CertificateError("pow_nonnegative requires a nonnegative interval")
        return Interval(self.lower**exponent, self.upper**exponent)


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def artifact_int(value: Any, name: str) -> int:
    """Parse producer integers, which are serialized as numbers or strings."""
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} must be integer text") from exc
    raise CertificateError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def artifact_rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = artifact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = artifact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        rational(raw.get("lower"), f"{name}.lower"),
        rational(raw.get("upper"), f"{name}.upper"),
    )


def artifact_interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        artifact_rational(raw.get("lower"), f"{name}.lower"),
        artifact_rational(raw.get("upper"), f"{name}.upper"),
    )


def binary_value(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    mantissa = artifact_int(raw.get("mantissa"), f"{name}.mantissa")
    exponent = artifact_int(raw.get("exponent"), f"{name}.exponent")
    return (
        Fraction(mantissa << exponent)
        if exponent >= 0
        else Fraction(mantissa, 1 << (-exponent))
    )


def binary_interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    result = Interval(
        binary_value(raw.get("lower"), f"{name}.lower"),
        binary_value(raw.get("upper"), f"{name}.upper"),
    )
    return result


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_sha256(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(ch not in string.hexdigits for ch in value)
    ):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def square_interval(value: Interval) -> Interval:
    upper = max(value.lower * value.lower, value.upper * value.upper)
    if value.lower <= 0 <= value.upper:
        lower = Fraction(0)
    else:
        lower = min(value.lower * value.lower, value.upper * value.upper)
    return Interval(lower, upper)


def modulus_squared(real: Interval, imag: Interval) -> Interval:
    return square_interval(real).add(square_interval(imag))


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise CertificateError("internal nonpositive fixed-point denominator")
    return -((-numerator) // denominator)


@lru_cache(maxsize=None)
def _atanh_log_interval(y: Fraction, terms: int) -> Interval:
    """Enclose log(y), 1 <= y <= 2, with outward dyadic arithmetic.

    Direct ``Fraction`` summation makes the denominator grow at every one of
    the hundreds of series terms. Fixed-point interval operations preserve the
    same positive-series and tail proof while keeping every intermediate at a
    bounded bit size.
    """
    if not (Fraction(1) <= y <= Fraction(2)):
        raise CertificateError("internal logarithm range-reduction failure")
    if terms < 8:
        raise CertificateError("logarithm term count must be at least 8")
    z = (y - 1) / (y + 1)
    scale = 1 << (4 * terms + 32)
    z_lower = (z.numerator * scale) // z.denominator
    z_upper = _ceil_div(z.numerator * scale, z.denominator)
    z2 = z * z
    z2_lower = (z2.numerator * scale) // z2.denominator
    z2_upper = _ceil_div(z2.numerator * scale, z2.denominator)
    power_lower, power_upper = z_lower, z_upper
    partial_lower = 0
    partial_upper = 0
    for j in range(terms):
        odd = 2 * j + 1
        partial_lower += (2 * power_lower) // odd
        partial_upper += _ceil_div(2 * power_upper, odd)
        power_lower = (power_lower * z2_lower) // scale
        power_upper = _ceil_div(power_upper * z2_upper, scale)

    # power now encloses z ** (2*terms+1). Since z <= 1/3, the remaining
    # positive series is bounded by
    #   2 z^(2N+1) / ((2N+1) (1-z^2)).
    one_minus_z2_lower = scale - z2_upper
    tail_upper = _ceil_div(
        2 * power_upper * scale,
        (2 * terms + 1) * one_minus_z2_lower,
    )
    return Interval(
        Fraction(partial_lower, scale),
        Fraction(partial_upper + tail_upper, scale),
    )


def log_positive_fraction(value: Fraction, terms: int) -> Interval:
    """Return a rigorous rational enclosure of log(value), value > 0."""
    if value <= 0:
        raise CertificateError("logarithm input must be positive")

    numerator, denominator = value.numerator, value.denominator
    exponent = numerator.bit_length() - denominator.bit_length()

    def power_of_two(k: int) -> Fraction:
        if k >= 0:
            return Fraction(1 << k, 1)
        return Fraction(1, 1 << (-k))

    reduced = value / power_of_two(exponent)
    while reduced < 1:
        exponent -= 1
        reduced *= 2
    while reduced >= 2:
        exponent += 1
        reduced /= 2

    reduced_log = _atanh_log_interval(reduced, terms)
    log_two = _atanh_log_interval(Fraction(2), terms)
    return reduced_log.add(log_two.scale(Fraction(exponent)))


def log_positive_interval(value: Interval, terms: int) -> Interval:
    if value.lower <= 0:
        raise CertificateError("modulus-square interval must have positive lower endpoint")
    lower = log_positive_fraction(value.lower, terms).lower
    upper = log_positive_fraction(value.upper, terms).upper
    return Interval(lower, upper)


def determinant_interval(matrix: list[list[Interval]]) -> Interval:
    size = len(matrix)
    if size < 1 or any(len(row) != size for row in matrix):
        raise CertificateError("determinant matrix must be nonempty and square")
    result = Interval(Fraction(0), Fraction(0))
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            1
            for i in range(size)
            for j in range(i + 1, size)
            if permutation[i] > permutation[j]
        )
        term = Interval(Fraction(1), Fraction(1))
        for row, column in enumerate(permutation):
            term = term.mul(matrix[row][column])
        result = result.add(term.scale(Fraction(-1 if inversions % 2 else 1)))
    return result


def row_status(value: Interval) -> str:
    if value.upper < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lower >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def parse_points(
    data: dict[str, Any], *, require_digests: bool
) -> dict[str, dict[str, Any]]:
    raw_points = data.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise CertificateError("points must be a nonempty list")
    points: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"points[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in points:
            raise CertificateError(f"invalid or duplicate point id at points[{index}]")
        u = rational(raw.get("u"), f"points[{index}].u")
        if u <= 0:
            raise CertificateError("all squared horizontal nodes must be positive")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise CertificateError(f"points[{index}].xi_rectangle must be an object")
        real = interval(rectangle.get("real"), f"points[{index}].xi_rectangle.real")
        imag = interval(rectangle.get("imag"), f"points[{index}].xi_rectangle.imag")
        h = modulus_squared(real, imag)
        canonical = {
            "id": identifier,
            "u": fj(u),
            "xi_rectangle": {"real": ij(real), "imag": ij(imag)},
        }
        digest = canonical_sha(canonical)
        declared = raw.get("point_sha256")
        if require_digests and declared is None:
            raise CertificateError(
                f"production point {identifier} must carry point_sha256"
            )
        if declared is not None and validate_sha256(declared, "point_sha256") != digest:
            raise CertificateError(f"point digest mismatch for {identifier}")
        points[identifier] = {
            "u": u,
            "real": real,
            "imag": imag,
            "h": h,
            "sha256": digest,
        }
    return points


def validate_production_source(data: dict[str, Any]) -> dict[str, str]:
    source = data.get("source")
    if not isinstance(source, dict):
        raise CertificateError("production certificate must bind source artifacts")
    primitive_sha = validate_sha256(
        source.get("primitive_sha256"), "source.primitive_sha256"
    )
    common_scale = exact_int(
        data.get("common_xi_scale_power_of_two", 0),
        "common_xi_scale_power_of_two",
    )
    source_scale = exact_int(
        source.get("primitive_common_xi_scale_power_of_two", 0),
        "source.primitive_common_xi_scale_power_of_two",
    )
    if source_scale != common_scale:
        raise CertificateError("primitive common xi scale metadata mismatch")
    gap_sha = source.get("gap_sha256")
    block_sha = source.get("zero_block_sha256")
    if (gap_sha is None) == (block_sha is None):
        raise CertificateError(
            "production source must bind exactly one gap or zero-block artifact"
        )
    if gap_sha is not None:
        return {
            "kind": "gap",
            "primitive_sha256": primitive_sha,
            "zero_sha256": validate_sha256(gap_sha, "source.gap_sha256"),
        }
    return {
        "kind": "zero-block",
        "primitive_sha256": primitive_sha,
        "zero_sha256": validate_sha256(
            block_sha, "source.zero_block_sha256"
        ),
    }


def _primitive_projection(
    primitive_artifact: dict[str, Any],
) -> tuple[Fraction, dict[str, str]]:
    artifact_ordinate = artifact_rational(
        primitive_artifact.get("ordinate"), "primitive_artifact.ordinate"
    )
    raw_points = primitive_artifact.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise CertificateError("primitive artifact points must be nonempty")
    projected: dict[str, str] = {}
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"primitive artifact point {index} must be an object")
        identifier = raw.get("id")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in projected
        ):
            raise CertificateError("primitive artifact point IDs must be unique")
        if raw.get("functional_equation_residual_contains_zero") is not True:
            raise CertificateError(
                f"primitive artifact point {identifier} failed functional-equation gate"
            )
        x = artifact_rational(raw.get("x"), f"primitive point {identifier}.x")
        if x <= 0:
            raise CertificateError("primitive horizontal offsets must be positive")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise CertificateError(f"primitive point {identifier} lacks xi_rectangle")
        real = artifact_interval(
            rectangle.get("real"), f"primitive point {identifier}.real"
        )
        imag = artifact_interval(
            rectangle.get("imag"), f"primitive point {identifier}.imag"
        )
        canonical = {
            "id": identifier,
            "u": fj(x * x),
            "xi_rectangle": {"real": ij(real), "imag": ij(imag)},
        }
        projected[identifier] = canonical_sha(canonical)
    return artifact_ordinate, projected


def _compare_primitive_projection(
    data: dict[str, Any], primitive_artifact: dict[str, Any]
) -> None:
    artifact_ordinate, expected_points = _primitive_projection(primitive_artifact)
    certificate_ordinate = rational(data.get("ordinate"), "ordinate")
    if certificate_ordinate != artifact_ordinate:
        raise CertificateError("certificate ordinate differs from primitive artifact")
    certificate_points = parse_points(data, require_digests=True)
    if set(certificate_points) != set(expected_points):
        raise CertificateError("certificate point set differs from primitive artifact")
    for identifier, expected_sha in expected_points.items():
        if certificate_points[identifier]["sha256"] != expected_sha:
            raise CertificateError(
                f"certificate point {identifier} differs from primitive artifact"
            )


def _expected_gap_bins(
    data: dict[str, Any], gap: dict[str, Any], gap_sha: str
) -> list[dict[str, Any]]:
    classification = gap.get("classification")
    if classification not in (
        "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB",
        "CERTIFIED_OFF_CRITICAL_ZERO_IN_LINE_EMPTY_SLAB",
    ):
        raise CertificateError("gap artifact is not proof-classified")
    source = data.get("source")
    if not isinstance(source, dict) or source.get("gap_classification") != classification:
        raise CertificateError("gap classification metadata mismatch")
    ordinate = rational(data.get("ordinate"), "ordinate")
    if artifact_rational(gap.get("target"), "gap.target") != ordinate:
        raise CertificateError("gap artifact ordinate mismatch")
    lower = binary_interval(
        gap.get("lower_hardy_zero_ball"), "gap.lower_hardy_zero_ball"
    )
    upper = binary_interval(
        gap.get("upper_hardy_zero_ball"), "gap.upper_hardy_zero_ball"
    )
    if not (lower.upper < ordinate < upper.lower):
        raise CertificateError("gap Hardy-zero balls do not strictly bracket target")
    expected = [
        {
            "id": "pr71-lower-hardy-zero",
            "lower": lower.lower,
            "upper": lower.upper,
            "count": 1,
            "B": max((ordinate - lower.lower) ** 2, (ordinate - lower.upper) ** 2),
            "gate_sha256": hashlib.sha256(
                (gap_sha + ":lower").encode("ascii")
            ).hexdigest(),
        },
        {
            "id": "pr71-upper-hardy-zero",
            "lower": upper.lower,
            "upper": upper.upper,
            "count": 1,
            "B": max((ordinate - upper.lower) ** 2, (ordinate - upper.upper) ** 2),
            "gate_sha256": hashlib.sha256(
                (gap_sha + ":upper").encode("ascii")
            ).hexdigest(),
        },
    ]
    return sorted(expected, key=lambda item: (item["lower"], item["upper"], item["id"]))


def _expected_block_bins(
    data: dict[str, Any], block: dict[str, Any], block_sha: str
) -> list[dict[str, Any]]:
    if block.get("classification") != "CERTIFIED_CRITICAL_LINE_ZERO_BLOCK":
        raise CertificateError("zero-block artifact is not proof-classified")
    ordinate = rational(data.get("ordinate"), "ordinate")
    if artifact_rational(block.get("target"), "zero_block.target") != ordinate:
        raise CertificateError("zero-block artifact ordinate mismatch")
    source = data.get("source")
    if not isinstance(source, dict):
        raise CertificateError("production certificate must bind source artifacts")
    block_precision = artifact_int(
        block.get("precision_bits"), "zero_block.precision_bits"
    )
    if artifact_int(
        source.get("zero_block_precision_bits"),
        "source.zero_block_precision_bits",
    ) != block_precision:
        raise CertificateError("zero-block precision metadata mismatch")
    nearest_count = exact_int(source.get("nearest_count"), "source.nearest_count")
    if nearest_count <= 0:
        raise CertificateError("source.nearest_count must be positive")

    raw_zeros = block.get("zeros")
    if not isinstance(raw_zeros, list) or len(raw_zeros) < nearest_count:
        raise CertificateError("zero-block artifact has insufficient zero balls")
    returned_count = artifact_int(
        block.get("returned_count"), "zero_block.returned_count"
    )
    if returned_count != len(raw_zeros):
        raise CertificateError("zero-block returned_count mismatch")
    parsed: list[dict[str, Any]] = []
    previous_upper: Fraction | None = None
    seen_indices: set[int] = set()
    for position, raw in enumerate(raw_zeros):
        if not isinstance(raw, dict):
            raise CertificateError(f"zero-block zero {position} must be an object")
        if "local_index" in raw and artifact_int(
            raw.get("local_index"), f"zero_block.zeros[{position}].local_index"
        ) != position:
            raise CertificateError("zero-block local indices are not consecutive")
        zero_index = artifact_int(
            raw.get("zero_index"), f"zero_block.zeros[{position}].zero_index"
        )
        if zero_index in seen_indices:
            raise CertificateError("duplicate zero index in zero-block artifact")
        seen_indices.add(zero_index)
        ball = binary_interval(
            raw.get("ball"), f"zero_block.zeros[{position}].ball"
        )
        if previous_upper is not None and previous_upper >= ball.lower:
            raise CertificateError("zero-block balls overlap, touch, or are unordered")
        previous_upper = ball.upper
        parsed.append(
            {
                "index": zero_index,
                "lower": ball.lower,
                "upper": ball.upper,
                "B": max(
                    (ordinate - ball.lower) ** 2,
                    (ordinate - ball.upper) ** 2,
                ),
            }
        )

    selected = sorted(parsed, key=lambda item: (item["B"], item["index"]))[
        :nearest_count
    ]
    declared_indices = source.get("selected_zero_indices")
    if (
        not isinstance(declared_indices, list)
        or any(isinstance(value, bool) or not isinstance(value, int) for value in declared_indices)
        or declared_indices != [item["index"] for item in selected]
    ):
        raise CertificateError("selected zero indices differ from zero-block artifact")
    expected = [
        {
            "id": f"pr71-zero-{item['index']}",
            "lower": item["lower"],
            "upper": item["upper"],
            "count": 1,
            "B": item["B"],
            "gate_sha256": hashlib.sha256(
                f"{block_sha}:{item['index']}".encode("ascii")
            ).hexdigest(),
        }
        for item in selected
    ]
    return sorted(expected, key=lambda item: (item["lower"], item["upper"], item["id"]))


def _compare_zero_projection(
    data: dict[str, Any], zero_artifact: dict[str, Any], kind: str, zero_sha: str
) -> None:
    ordinate = rational(data.get("ordinate"), "ordinate")
    actual = parse_zero_bins(data, ordinate, "RIEMANN_XI_DIRECTED")
    expected = (
        _expected_gap_bins(data, zero_artifact, zero_sha)
        if kind == "gap"
        else _expected_block_bins(data, zero_artifact, zero_sha)
    )
    if len(actual) != len(expected):
        raise CertificateError(f"certificate zero bins differ from {kind} artifact")
    fields = ("id", "lower", "upper", "count", "B", "gate_sha256")
    for actual_bin, expected_bin in zip(actual, expected):
        if any(actual_bin[field] != expected_bin[field] for field in fields):
            raise CertificateError(
                f"certificate zero bin {actual_bin['id']} differs from {kind} artifact"
            )


def verify_source_artifacts(
    data: dict[str, Any],
    primitive_artifact: dict[str, Any],
    zero_artifact: dict[str, Any],
) -> dict[str, str]:
    """Reconstruct every proof-relevant certificate field from producer outputs."""
    source = validate_production_source(data)
    if primitive_artifact.get("schema") != PRIMITIVE_SCHEMA:
        raise CertificateError("primitive artifact schema mismatch")
    if primitive_artifact.get("normalization_id") != NORMALIZATION:
        raise CertificateError("primitive artifact normalization mismatch")
    artifact_scale = exact_int(
        primitive_artifact.get("common_xi_scale_power_of_two", 0),
        "primitive_artifact.common_xi_scale_power_of_two",
    )
    certificate_scale = exact_int(
        data.get("common_xi_scale_power_of_two", 0),
        "common_xi_scale_power_of_two",
    )
    if artifact_scale != certificate_scale:
        raise CertificateError("primitive artifact common xi scale mismatch")
    expected_zero_schema = GAP_SCHEMA if source["kind"] == "gap" else BLOCK_SCHEMA
    if zero_artifact.get("schema") != expected_zero_schema:
        raise CertificateError(f"{source['kind']} artifact schema mismatch")
    primitive_sha = canonical_sha(primitive_artifact)
    zero_sha = canonical_sha(zero_artifact)
    if primitive_sha != source["primitive_sha256"]:
        raise CertificateError("primitive artifact digest does not match certificate")
    if zero_sha != source["zero_sha256"]:
        raise CertificateError(
            f"{source['kind']} artifact digest does not match certificate"
        )
    _compare_primitive_projection(data, primitive_artifact)
    _compare_zero_projection(data, zero_artifact, source["kind"], zero_sha)
    return {
        "primitive_sha256": primitive_sha,
        f"{source['kind']}_sha256": zero_sha,
    }


def parse_zero_bins(
    data: dict[str, Any], ordinate: Fraction, classification: str
) -> list[dict[str, Any]]:
    raw_bins = data.get("zero_bins")
    if not isinstance(raw_bins, list) or not raw_bins:
        raise CertificateError("zero_bins must be a nonempty list")

    bins: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_bins):
        if not isinstance(raw, dict):
            raise CertificateError(f"zero_bins[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier:
            raise CertificateError("zero-bin id must be a nonempty string")
        lower = rational(raw.get("lower_ordinate"), f"zero_bins[{index}].lower_ordinate")
        upper = rational(raw.get("upper_ordinate"), f"zero_bins[{index}].upper_ordinate")
        if lower > upper:
            raise CertificateError("zero-bin endpoints are reversed")
        count = exact_int(raw.get("count_lower"), f"zero_bins[{index}].count_lower")
        if count <= 0:
            raise CertificateError("zero-bin lower count must be positive")
        gate = raw.get("gate")
        if not isinstance(gate, dict):
            raise CertificateError("zero-bin gate must be an object")
        expected_status = (
            SYNTHETIC_GATE if classification == "SYNTHETIC_MODEL" else PRODUCTION_GATE
        )
        if gate.get("status") != expected_status:
            raise CertificateError(
                f"zero-bin gate status must equal {expected_status!r}"
            )
        gate_sha = validate_sha256(gate.get("sha256"), "zero-bin gate sha256")
        distance_lower = ordinate - lower
        distance_upper = ordinate - upper
        b_value = max(distance_lower * distance_lower, distance_upper * distance_upper)
        bins.append(
            {
                "id": identifier,
                "lower": lower,
                "upper": upper,
                "count": count,
                "B": b_value,
                "gate_sha256": gate_sha,
            }
        )

    bins.sort(key=lambda item: (item["lower"], item["upper"], item["id"]))
    if len({item["id"] for item in bins}) != len(bins):
        raise CertificateError("duplicate zero-bin id")
    for left, right in zip(bins, bins[1:]):
        if left["upper"] >= right["lower"]:
            raise CertificateError("zero bins overlap or touch")
    return bins


def raw_log_value(point: dict[str, Any], terms: int) -> Interval:
    return log_positive_interval(point["h"], terms)


def deflated_log_value(
    point: dict[str, Any], bins: list[dict[str, Any]], terms: int
) -> Interval:
    result = raw_log_value(point, terms)
    u = point["u"]
    for zero_bin in bins:
        explicit = log_positive_fraction(u + zero_bin["B"], terms).scale(
            Fraction(zero_bin["count"])
        )
        result = result.sub(explicit)
    return result


def secant(
    left: dict[str, Any],
    right: dict[str, Any],
    left_value: Interval,
    right_value: Interval,
) -> Interval:
    denominator = left["u"] - right["u"]
    if denominator == 0:
        raise CertificateError("secant nodes must be distinct")
    return left_value.sub(right_value).scale(Fraction(1, 1) / denominator)


def monotonicity_product(
    left: dict[str, Any],
    right: dict[str, Any],
    bins: list[dict[str, Any]],
    factor_cache: dict[Fraction, Fraction] | None = None,
) -> Interval:
    if not left["u"] < right["u"]:
        raise CertificateError("monotonicity nodes must be increasing")

    def factor(point: dict[str, Any]) -> Fraction:
        u = point["u"]
        if factor_cache is not None and u in factor_cache:
            return factor_cache[u]
        result = Fraction(1)
        for zero_bin in bins:
            result *= (u + zero_bin["B"]) ** zero_bin["count"]
        if factor_cache is not None:
            factor_cache[u] = result
        return result

    left_factor = factor(left)
    right_factor = factor(right)
    return right["h"].scale(left_factor).sub(left["h"].scale(right_factor))


def loewner_determinant(
    point_ids_rows: list[str],
    point_ids_columns: list[str],
    points: dict[str, dict[str, Any]],
    bins: list[dict[str, Any]],
    terms: int,
    deflated: bool,
    value_cache: dict[tuple[bool, str], Interval] | None = None,
) -> Interval:
    size = len(point_ids_rows)
    if size < 1 or size != len(point_ids_columns) or size > 4:
        raise CertificateError("Loewner determinant order must be between one and four")
    if len(set(point_ids_rows)) != size or len(set(point_ids_columns)) != size:
        raise CertificateError("Loewner row and column lists must not repeat nodes")
    if set(point_ids_rows) & set(point_ids_columns):
        raise CertificateError("Loewner row and column lists must be disjoint")
    if any(identifier not in points for identifier in point_ids_rows + point_ids_columns):
        raise CertificateError("Loewner row references an unknown point")

    row_nodes = [points[identifier]["u"] for identifier in point_ids_rows]
    column_nodes = [points[identifier]["u"] for identifier in point_ids_columns]
    if any(row_nodes[i] >= row_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner row nodes must be strictly increasing")
    if any(column_nodes[i] >= column_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner column nodes must be strictly increasing")

    identifiers = point_ids_rows + point_ids_columns
    values: dict[str, Interval] = {}
    for identifier in identifiers:
        key = (deflated, identifier)
        if value_cache is not None and key in value_cache:
            values[identifier] = value_cache[key]
            continue
        value = (
            deflated_log_value(points[identifier], bins, terms)
            if deflated
            else raw_log_value(points[identifier], terms)
        )
        values[identifier] = value
        if value_cache is not None:
            value_cache[key] = value

    matrix: list[list[Interval]] = []
    for row_id in point_ids_rows:
        matrix_row = []
        for column_id in point_ids_columns:
            matrix_row.append(
                secant(
                    points[row_id],
                    points[column_id],
                    values[row_id],
                    values[column_id],
                )
            )
        matrix.append(matrix_row)
    return determinant_interval(matrix)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("completed-xi normalization mismatch")
    classification = data.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise CertificateError("unsupported classification")
    common_scale = exact_int(
        data.get("common_xi_scale_power_of_two", 0),
        "common_xi_scale_power_of_two",
    )
    ordinate = rational(data.get("ordinate"), "ordinate")
    terms = exact_int(data.get("log_terms", 256), "log_terms")
    if terms < 32 or terms > 4096:
        raise CertificateError("log_terms must be between 32 and 4096")

    claimed_certificate_sha = data.get("certificate_sha256")
    if classification == "RIEMANN_XI_DIRECTED" and claimed_certificate_sha is None:
        raise CertificateError("production certificate must carry certificate_sha256")
    if claimed_certificate_sha is not None:
        claimed_certificate_sha = validate_sha256(
            claimed_certificate_sha, "certificate_sha256"
        )
        certificate_body = dict(data)
        certificate_body.pop("certificate_sha256", None)
        if canonical_sha(certificate_body) != claimed_certificate_sha:
            raise CertificateError("certificate_sha256 mismatch")
    if classification == "RIEMANN_XI_DIRECTED":
        validate_production_source(data)

    points = parse_points(
        data, require_digests=classification == "RIEMANN_XI_DIRECTED"
    )
    bins = parse_zero_bins(data, ordinate, classification)
    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be a nonempty list")

    outputs: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    factor_cache: dict[Fraction, Fraction] = {}
    log_value_cache: dict[tuple[bool, str], Interval] = {}
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{index}] must be an object")
        row_id = raw.get("id")
        kind = raw.get("kind")
        if not isinstance(row_id, str) or not row_id or row_id in seen_ids:
            raise CertificateError("row id must be nonempty and unique")
        seen_ids.add(row_id)

        if kind in ("raw-monotonicity", "deflated-monotonicity"):
            left_id, right_id = raw.get("left"), raw.get("right")
            if left_id not in points or right_id not in points:
                raise CertificateError(f"unknown monotonicity point in {row_id}")
            left, right = points[left_id], points[right_id]
            if not left["u"] < right["u"]:
                raise CertificateError("monotonicity nodes must be increasing")
            if kind == "raw-monotonicity":
                value = right["h"].sub(left["h"])
            else:
                value = monotonicity_product(
                    left, right, bins, factor_cache=factor_cache
                )
            detail = {"left": left_id, "right": right_id}

        elif kind in (
            "raw-cross-loewner-determinant",
            "deflated-cross-loewner-determinant",
        ):
            row_ids, column_ids = raw.get("rows"), raw.get("columns")
            if not isinstance(row_ids, list) or not isinstance(column_ids, list):
                raise CertificateError("Loewner rows and columns must be arrays")
            value = loewner_determinant(
                row_ids,
                column_ids,
                points,
                bins,
                terms,
                deflated=kind.startswith("deflated"),
                value_cache=log_value_cache,
            )
            detail = {
                "rows": row_ids,
                "columns": column_ids,
                "order": len(row_ids),
            }
        else:
            raise CertificateError(f"unsupported row kind {kind!r}")

        outputs.append(
            {
                "id": row_id,
                "kind": kind,
                **detail,
                "interval": ij(value),
                "status": row_status(value),
            }
        )

    negative = [row for row in outputs if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in outputs if row["status"] == "UNRESOLVED"]
    if classification == "RIEMANN_XI_DIRECTED" and negative:
        verdict = "NEGATIVE_ZERO_DEFLATED_XI_ARITHMETIC_REPLAY"
    elif classification == "SYNTHETIC_MODEL" and negative:
        verdict = "SYNTHETIC_ZERO_DEFLATION_SEPARATION"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_ROWS"

    result = {
        "schema": SCHEMA,
        "verified": True,
        "source_artifacts_verified": False,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "common_xi_scale_power_of_two": common_scale,
        "ordinate": fj(ordinate),
        "point_count": len(points),
        "zero_bins": [
            {
                "id": item["id"],
                "lower_ordinate": fj(item["lower"]),
                "upper_ordinate": fj(item["upper"]),
                "count_lower": item["count"],
                "distance_square_upper": fj(item["B"]),
                "gate_sha256": item["gate_sha256"],
            }
            for item in bins
        ],
        "point_fingerprints": {
            identifier: point["sha256"] for identifier, point in sorted(points.items())
        },
        "rows": outputs,
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "The checker proves exact rectangle contraction and zero-bin algebra only. "
            "A production CLI replay additionally requires the primitive and zero "
            "artifacts whose digests are bound by the certificate. A negative still "
            "requires independent backend reproduction and review of L-9301 and the "
            "completed-xi normalization. One exact common power-of-two scale may be "
            "applied to every xi rectangle because it cancels from logarithmic "
            "secants and multiplies both sides of every algebraic row by the same "
            "positive factor."
        ),
    }
    if claimed_certificate_sha is not None:
        result["certificate_sha256"] = claimed_certificate_sha
    result["verification_sha256"] = canonical_sha(result)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--primitive-artifact", type=Path)
    parser.add_argument("--zero-artifact", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        source_artifacts: dict[str, str] | None = None
        if data.get("classification") == "RIEMANN_XI_DIRECTED":
            if args.primitive_artifact is None or args.zero_artifact is None:
                raise CertificateError(
                    "production replay requires --primitive-artifact and "
                    "--zero-artifact"
                )
            primitive_artifact = json.loads(
                args.primitive_artifact.read_text(encoding="utf-8")
            )
            zero_artifact = json.loads(
                args.zero_artifact.read_text(encoding="utf-8")
            )
            if not isinstance(primitive_artifact, dict) or not isinstance(
                zero_artifact, dict
            ):
                raise CertificateError("source artifacts must contain JSON objects")
            # Reconstruct source-derived fields before starting the expensive
            # exact logarithm and determinant replay.
            source_artifacts = verify_source_artifacts(
                data, primitive_artifact, zero_artifact
            )
        result = verify(data)
        if source_artifacts is not None:
            result["source_artifacts"] = source_artifacts
            result["source_artifacts_verified"] = True
            if result["certified_negative_rows"]:
                result["verdict"] = (
                    "NEGATIVE_ZERO_DEFLATED_XI_MODULUS_WITNESS_PENDING_REVIEW"
                )
            result.pop("verification_sha256", None)
            result["verification_sha256"] = canonical_sha(result)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 1 if result["unresolved_rows"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
