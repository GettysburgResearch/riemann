#!/usr/bin/env python3
"""Exact replay for overlapping interval-count zero-deflation certificates.

The checker has two logically separate layers.

1. Count geometry:
   exact zero counts in arbitrary overlapping ordinate intervals are converted
   into an optimal lower profile for the number of zeros in symmetric windows
   about T. Each profile row carries a primal cell-count witness and an exact
   LP-dual witness.

2. Direct-xi rows:
   the verified profile is converted into shell increments and subtracted from
   log |xi(1/2+sqrt(u)+iT)|^2. All arithmetic after parsing is integer/Fraction
   arithmetic; logarithms use a rational positive atanh series enclosure.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import string
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SCHEMA = "riemann.x9303-interval-count-deflation.v1"
VERIFY_SCHEMA = "riemann.x9303-interval-count-deflation.verification.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
PRODUCTION_COUNT_GATE = "CERTIFIED_EXACT_TOTAL_ZERO_COUNT_ZERO_FREE_ENDPOINTS"
SYNTHETIC_COUNT_GATE = "SYNTHETIC_EXACT_TOTAL_ZERO_COUNT"


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
        values = (self.lower * scalar, self.upper * scalar)
        return Interval(min(values), max(values))

    def mul(self, other: "Interval") -> "Interval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(values), max(values))


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def parse_integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} must be a base-10 integer") from exc
    raise CertificateError(f"{name} must be an integer or integer string")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_integer(raw.get("numerator"), f"{name}.numerator")
    denominator = parse_integer(raw.get("denominator"), f"{name}.denominator")
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


def _atanh_log_interval(y: Fraction, terms: int) -> Interval:
    if not Fraction(1) <= y <= Fraction(2):
        raise CertificateError("internal logarithm range reduction failed")
    if terms < 8:
        raise CertificateError("logarithm term count must be at least 8")
    z = (y - 1) / (y + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lower, lower + tail)


def log_positive_fraction(value: Fraction, terms: int) -> Interval:
    if value <= 0:
        raise CertificateError("logarithm input must be positive")
    exponent = value.numerator.bit_length() - value.denominator.bit_length()

    def power_of_two(k: int) -> Fraction:
        return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))

    reduced = value / power_of_two(exponent)
    while reduced < 1:
        exponent -= 1
        reduced *= 2
    while reduced >= 2:
        exponent += 1
        reduced /= 2
    return _atanh_log_interval(reduced, terms).add(
        _atanh_log_interval(Fraction(2), terms).scale(Fraction(exponent))
    )


def log_positive_interval(value: Interval, terms: int) -> Interval:
    if value.lower <= 0:
        raise CertificateError("modulus-square interval must be strictly positive")
    return Interval(
        log_positive_fraction(value.lower, terms).lower,
        log_positive_fraction(value.upper, terms).upper,
    )


def determinant_interval(matrix: list[list[Interval]]) -> Interval:
    size = len(matrix)
    if size < 1 or any(len(row) != size for row in matrix):
        raise CertificateError("determinant matrix must be nonempty and square")
    result = Interval(Fraction(0), Fraction(0))
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
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


def verify_count_geometry(data: dict[str, Any]) -> tuple[
    Fraction,
    list[Fraction],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    classification = data.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise CertificateError("unsupported classification")
    target = rational(data.get("ordinate"), "ordinate")

    raw_endpoints = data.get("atom_endpoints")
    if not isinstance(raw_endpoints, list) or len(raw_endpoints) < 2:
        raise CertificateError("atom_endpoints must contain at least two values")
    endpoints = [rational(value, f"atom_endpoints[{i}]") for i, value in enumerate(raw_endpoints)]
    if any(endpoints[i] >= endpoints[i + 1] for i in range(len(endpoints) - 1)):
        raise CertificateError("atom endpoints must be strictly increasing")
    cell_count = len(endpoints) - 1

    raw_constraints = data.get("count_constraints")
    if not isinstance(raw_constraints, list) or not raw_constraints:
        raise CertificateError("count_constraints must be nonempty")
    expected_gate = (
        SYNTHETIC_COUNT_GATE
        if classification == "SYNTHETIC_MODEL"
        else PRODUCTION_COUNT_GATE
    )
    constraints: list[dict[str, Any]] = []
    ids: set[str] = set()
    for i, raw in enumerate(raw_constraints):
        if not isinstance(raw, dict):
            raise CertificateError(f"count_constraints[{i}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise CertificateError("count-constraint IDs must be nonempty and unique")
        ids.add(identifier)
        left = exact_int(raw.get("left_endpoint_index"), f"constraint {identifier}.left")
        right = exact_int(raw.get("right_endpoint_index"), f"constraint {identifier}.right")
        if not (0 <= left < right < len(endpoints)):
            raise CertificateError(f"constraint {identifier} has invalid endpoint indices")
        count = exact_int(raw.get("exact_count"), f"constraint {identifier}.exact_count")
        if count < 0:
            raise CertificateError("exact counts must be nonnegative")
        gate = raw.get("gate")
        if not isinstance(gate, dict) or gate.get("status") != expected_gate:
            raise CertificateError(f"constraint {identifier} has the wrong semantic gate")
        gate_sha = validate_sha256(gate.get("sha256"), f"constraint {identifier}.gate.sha256")
        row = [1 if left <= j < right else 0 for j in range(cell_count)]
        constraints.append(
            {
                "id": identifier,
                "left": left,
                "right": right,
                "count": count,
                "row": row,
                "gate_sha256": gate_sha,
            }
        )

    raw_profiles = data.get("profiles")
    if not isinstance(raw_profiles, list) or not raw_profiles:
        raise CertificateError("profiles must be nonempty")
    complete_profile = data.get("complete_breakpoint_profile", False)
    if not isinstance(complete_profile, bool):
        raise CertificateError("complete_breakpoint_profile must be Boolean")
    if complete_profile:
        endpoint_set = set(endpoints)
        if any(2 * target - value not in endpoint_set for value in endpoints):
            raise CertificateError(
                "a complete breakpoint profile requires atom endpoints symmetric about T"
            )
        required_radii = sorted({abs(value - target) for value in endpoints if value != target})
        supplied_radii = [
            rational(raw.get("radius"), f"profiles[{i}].radius")
            for i, raw in enumerate(raw_profiles)
            if isinstance(raw, dict)
        ]
        if supplied_radii != required_radii:
            raise CertificateError(
                "complete breakpoint profile does not list every endpoint radius"
            )
    profiles: list[dict[str, Any]] = []
    last_radius = Fraction(-1)
    last_count = -1
    for i, raw in enumerate(raw_profiles):
        if not isinstance(raw, dict):
            raise CertificateError(f"profiles[{i}] must be an object")
        radius = rational(raw.get("radius"), f"profiles[{i}].radius")
        if radius <= 0 or radius <= last_radius:
            raise CertificateError("profile radii must be strictly increasing and positive")
        lower_boundary, upper_boundary = target - radius, target + radius
        try:
            lower_index = endpoints.index(lower_boundary)
            upper_index = endpoints.index(upper_boundary)
        except ValueError as exc:
            raise CertificateError("every profile boundary must occur in atom_endpoints") from exc
        if lower_index >= upper_index:
            raise CertificateError("profile window is empty")
        objective = [1 if lower_index <= j < upper_index else 0 for j in range(cell_count)]

        forced = exact_int(raw.get("forced_count"), f"profiles[{i}].forced_count")
        if forced < 0 or forced < last_count:
            raise CertificateError("forced counts must be nonnegative and nondecreasing")

        raw_primal = raw.get("primal_cell_counts")
        if not isinstance(raw_primal, list) or len(raw_primal) != cell_count:
            raise CertificateError("primal_cell_counts has the wrong dimension")
        primal = [exact_int(value, f"profiles[{i}].primal[{j}]") for j, value in enumerate(raw_primal)]
        if any(value < 0 for value in primal):
            raise CertificateError("primal cell counts must be nonnegative")
        for constraint in constraints:
            value = sum(a * x for a, x in zip(constraint["row"], primal))
            if value != constraint["count"]:
                raise CertificateError(
                    f"profile {i} primal violates count constraint {constraint['id']}"
                )
        primal_objective = sum(c * x for c, x in zip(objective, primal))
        if primal_objective != forced:
            raise CertificateError("profile primal objective does not match forced_count")

        raw_dual = raw.get("dual_multipliers")
        if not isinstance(raw_dual, list) or len(raw_dual) != len(constraints):
            raise CertificateError("dual_multipliers has the wrong dimension")
        dual = [rational(value, f"profiles[{i}].dual[{j}]") for j, value in enumerate(raw_dual)]
        for cell in range(cell_count):
            column_value = sum(
                multiplier * constraint["row"][cell]
                for multiplier, constraint in zip(dual, constraints)
            )
            if column_value > objective[cell]:
                raise CertificateError(
                    f"profile {i} dual exceeds objective coefficient at cell {cell}"
                )
        dual_objective = sum(
            multiplier * constraint["count"]
            for multiplier, constraint in zip(dual, constraints)
        )
        if dual_objective != forced:
            raise CertificateError("profile dual objective does not match forced_count")

        profiles.append(
            {
                "radius": radius,
                "forced_count": forced,
                "increment": forced - last_count if last_count >= 0 else forced,
                "lower_endpoint_index": lower_index,
                "upper_endpoint_index": upper_index,
                "primal_sha256": canonical_sha(primal),
                "dual_sha256": canonical_sha([fj(value) for value in dual]),
            }
        )
        last_radius, last_count = radius, forced

    return target, endpoints, constraints, profiles


def parse_points(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw_points = data.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise CertificateError("points must be a nonempty list")
    points: dict[str, dict[str, Any]] = {}
    for i, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"points[{i}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in points:
            raise CertificateError("point IDs must be nonempty and unique")
        u = rational(raw.get("u"), f"points[{i}].u")
        if u <= 0:
            raise CertificateError("point nodes must be positive")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise CertificateError("xi_rectangle must be an object")
        real = interval(rectangle.get("real"), f"points[{i}].real")
        imag = interval(rectangle.get("imag"), f"points[{i}].imag")
        canonical = {
            "id": identifier,
            "u": fj(u),
            "xi_rectangle": {"real": ij(real), "imag": ij(imag)},
        }
        digest = canonical_sha(canonical)
        declared = raw.get("point_sha256")
        if declared is not None and validate_sha256(declared, "point_sha256") != digest:
            raise CertificateError(f"point digest mismatch for {identifier}")
        points[identifier] = {
            "u": u,
            "h": modulus_squared(real, imag),
            "sha256": digest,
        }
    return points


def profile_log_value(
    point: dict[str, Any],
    profiles: list[dict[str, Any]],
    terms: int,
    mode: str,
) -> Interval:
    result = log_positive_interval(point["h"], terms)
    u = point["u"]
    if mode == "raw":
        return result
    if mode == "outer":
        outer = profiles[-1]
        explicit = log_positive_fraction(u + outer["radius"] ** 2, terms).scale(
            Fraction(outer["forced_count"])
        )
        return result.sub(explicit)
    if mode != "optimal":
        raise CertificateError(f"unknown profile mode {mode!r}")
    previous = 0
    for profile in profiles:
        increment = profile["forced_count"] - previous
        if increment:
            explicit = log_positive_fraction(
                u + profile["radius"] ** 2, terms
            ).scale(Fraction(increment))
            result = result.sub(explicit)
        previous = profile["forced_count"]
    return result


def secant(
    left: dict[str, Any],
    right: dict[str, Any],
    left_value: Interval,
    right_value: Interval,
) -> Interval:
    denominator = left["u"] - right["u"]
    if denominator == 0:
        raise CertificateError("secant nodes must differ")
    return left_value.sub(right_value).scale(Fraction(1, 1) / denominator)


def loewner_row(
    raw: dict[str, Any],
    points: dict[str, dict[str, Any]],
    profiles: list[dict[str, Any]],
    terms: int,
) -> Interval:
    kind = raw.get("kind")
    modes = {
        "raw-cross-loewner-determinant": "raw",
        "outer-only-cross-loewner-determinant": "outer",
        "optimal-profile-cross-loewner-determinant": "optimal",
    }
    if kind not in modes:
        raise CertificateError(f"unsupported row kind {kind!r}")
    row_ids, column_ids = raw.get("rows"), raw.get("columns")
    if not isinstance(row_ids, list) or not isinstance(column_ids, list):
        raise CertificateError("Loewner rows and columns must be arrays")
    size = len(row_ids)
    if size < 1 or size != len(column_ids) or size > 4:
        raise CertificateError("Loewner determinant order must be between one and four")
    if len(set(row_ids)) != size or len(set(column_ids)) != size:
        raise CertificateError("Loewner node lists must not repeat nodes")
    if set(row_ids) & set(column_ids):
        raise CertificateError("Loewner row and column lists must be disjoint")
    if any(identifier not in points for identifier in row_ids + column_ids):
        raise CertificateError("Loewner row references an unknown point")
    row_nodes = [points[identifier]["u"] for identifier in row_ids]
    column_nodes = [points[identifier]["u"] for identifier in column_ids]
    if any(row_nodes[i] >= row_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner row nodes must be increasing")
    if any(column_nodes[i] >= column_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner column nodes must be increasing")
    mode = modes[kind]
    values = {
        identifier: profile_log_value(points[identifier], profiles, terms, mode)
        for identifier in row_ids + column_ids
    }
    matrix = [
        [
            secant(
                points[row_id],
                points[column_id],
                values[row_id],
                values[column_id],
            )
            for column_id in column_ids
        ]
        for row_id in row_ids
    ]
    return determinant_interval(matrix)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("completed-xi normalization mismatch")
    target, endpoints, constraints, profiles = verify_count_geometry(data)
    terms = exact_int(data.get("log_terms", 256), "log_terms")
    if not 32 <= terms <= 4096:
        raise CertificateError("log_terms must be between 32 and 4096")
    points = parse_points(data)
    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be nonempty")
    outputs = []
    seen: set[str] = set()
    for i, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{i}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise CertificateError("row IDs must be nonempty and unique")
        seen.add(identifier)
        value = loewner_row(raw, points, profiles, terms)
        outputs.append(
            {
                "id": identifier,
                "kind": raw.get("kind"),
                "interval": ij(value),
                "status": row_status(value),
            }
        )

    negative = [
        row
        for row in outputs
        if row["kind"] == "optimal-profile-cross-loewner-determinant"
        and row["status"] == "CERTIFIED_NEGATIVE"
    ]
    unresolved = [row for row in outputs if row["status"] == "UNRESOLVED"]
    classification = data.get("classification")
    if classification == "RIEMANN_XI_DIRECTED" and negative:
        verdict = "NEGATIVE_INTERVAL_COUNT_DEFLATED_XI_WITNESS_PENDING_REVIEW"
    elif classification == "SYNTHETIC_MODEL" and negative:
        verdict = "SYNTHETIC_OVERLAP_COUNT_SEPARATION"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_OPTIMAL_PROFILE_ROW"

    return {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "ordinate": fj(target),
        "atom_endpoint_count": len(endpoints),
        "cell_count": len(endpoints) - 1,
        "constraint_count": len(constraints),
        "profile": [
            {
                "radius": fj(profile["radius"]),
                "forced_count": profile["forced_count"],
                "increment": profile["increment"],
                "primal_sha256": profile["primal_sha256"],
                "dual_sha256": profile["dual_sha256"],
            }
            for profile in profiles
        ],
        "point_fingerprints": {
            identifier: point["sha256"] for identifier, point in sorted(points.items())
        },
        "rows": outputs,
        "certified_negative_optimal_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "proof_boundary": (
            "The checker verifies exact interval-count primal/dual optimality and "
            "rational direct-xi row contraction. A production negative additionally "
            "requires proof-grade exact total-count constraints, directed completed-xi "
            "rectangles, independent primitive reproduction, and analytic review."
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
            raise CertificateError("certificate root must be an object")
        result = verify(data)
        code = 1 if result["certified_negative_optimal_rows"] else 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {
            "schema": VERIFY_SCHEMA,
            "verified": False,
            "verdict": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
