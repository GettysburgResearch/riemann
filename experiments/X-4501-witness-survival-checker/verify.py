#!/usr/bin/env python3
"""Exact checker for quantitative finite-witness survival certificates.

This checker deliberately proves only the quantitative statement encoded by a
certificate: every realization in the declared uncertainty set leaves the
scalar witness score strictly negative.  It does not prove an RH equivalence,
normalization, analytic-domain hypothesis, or the soundness of transcendental
leaf enclosures.  Those are logical gates in the surrounding assurance case.

Supported certificate kinds:

* ``affine-box``: exact support function of independent rational intervals;
* ``affine-polytope-dual``: exact weak-duality certificate for correlated
  rational polytope uncertainty;
* ``pick-disks``: exact fixed-vector compression of a Pick matrix with one
  complex disk enclosure per sampled value.

All arithmetic after JSON parsing uses ``fractions.Fraction``.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
import sys
from typing import Any, Iterable, Sequence

SCHEMA = "riemann.witness-survival.v1"
QUANTITATIVE_STATES = {
    "ELIMINATED_EXACTLY",
    "ENCLOSED",
    "EXHAUSTIVELY_ENUMERATED",
    "TAIL_BOUNDED",
}
CLOSED_GATE_STATES = {"PROVED", "INDEPENDENTLY_VERIFIED"}
NONBLOCKING_GATE_STATES = CLOSED_GATE_STATES | {"SYNTHETIC_CONTROL"}


class CertificateError(ValueError):
    """Raised when a certificate is malformed or fails a proof obligation."""


def as_fraction(value: Any, *, field: str) -> Fraction:
    """Parse an exact rational from an integer or a ``p/q`` string."""

    if isinstance(value, bool):
        raise CertificateError(f"{field}: booleans are not rational values")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            result = Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{field}: invalid rational {value!r}") from exc
        return result
    if isinstance(value, list) and len(value) == 2:
        numerator = as_fraction(value[0], field=f"{field}[0]")
        denominator = as_fraction(value[1], field=f"{field}[1]")
        if numerator.denominator != 1 or denominator.denominator != 1:
            raise CertificateError(f"{field}: pair entries must be integers")
        if denominator == 0:
            raise CertificateError(f"{field}: denominator is zero")
        return Fraction(numerator.numerator, denominator.numerator)
    raise CertificateError(f"{field}: expected integer, rational string, or [p,q]")


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class QComplex:
    re: Fraction
    im: Fraction

    def __add__(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re - other.re, self.im - other.im)

    def __mul__(self, other: "QComplex") -> "QComplex":
        return QComplex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __truediv__(self, other: "QComplex") -> "QComplex":
        denominator = other.abs2()
        if denominator == 0:
            raise CertificateError("complex division by zero")
        return QComplex(
            (self.re * other.re + self.im * other.im) / denominator,
            (self.im * other.re - self.re * other.im) / denominator,
        )

    def conjugate(self) -> "QComplex":
        return QComplex(self.re, -self.im)

    def abs2(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    @staticmethod
    def zero() -> "QComplex":
        return QComplex(Fraction(0), Fraction(0))


def as_complex(value: Any, *, field: str) -> QComplex:
    if not isinstance(value, dict) or set(value) != {"re", "im"}:
        raise CertificateError(f"{field}: expected exactly {{'re','im'}}")
    return QComplex(
        as_fraction(value["re"], field=f"{field}.re"),
        as_fraction(value["im"], field=f"{field}.im"),
    )


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    if len(left) != len(right):
        raise CertificateError("dot-product dimension mismatch")
    return sum((x * y for x, y in zip(left, right)), Fraction(0))


def mat_vec(matrix: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]) -> list[Fraction]:
    return [dot(row, vector) for row in matrix]


def transpose_mat_vec(matrix: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]) -> list[Fraction]:
    if len(matrix) != len(vector):
        raise CertificateError("transpose product dimension mismatch")
    if not matrix:
        return []
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise CertificateError("matrix rows have inconsistent lengths")
    return [
        sum((matrix[row][column] * vector[row] for row in range(len(matrix))), Fraction(0))
        for column in range(width)
    ]


def _manifest(payload: dict[str, Any], used_channels: Iterable[str]) -> dict[str, Any]:
    manifest = payload.get("uncertainty_manifest")
    if not isinstance(manifest, dict):
        raise CertificateError("missing uncertainty_manifest object")

    channels = manifest.get("quantitative_channels")
    if not isinstance(channels, list):
        raise CertificateError("uncertainty_manifest.quantitative_channels must be a list")
    channel_ids: list[str] = []
    for index, record in enumerate(channels):
        if not isinstance(record, dict):
            raise CertificateError(f"quantitative channel {index} is not an object")
        channel_id = record.get("id")
        state = record.get("state")
        if not isinstance(channel_id, str) or not channel_id:
            raise CertificateError(f"quantitative channel {index} has invalid id")
        if state not in QUANTITATIVE_STATES:
            raise CertificateError(f"quantitative channel {channel_id!r} is not soundly closed: {state!r}")
        channel_ids.append(channel_id)
    if len(channel_ids) != len(set(channel_ids)):
        raise CertificateError("duplicate quantitative channel id")

    used = list(used_channels)
    if len(used) != len(set(used)):
        raise CertificateError("the score uses one quantitative channel more than once")
    if set(channel_ids) != set(used):
        missing = sorted(set(channel_ids) - set(used))
        undeclared = sorted(set(used) - set(channel_ids))
        raise CertificateError(
            f"uncertainty closure mismatch: unused_declared={missing}, undeclared_used={undeclared}"
        )

    gates = manifest.get("logical_gates", [])
    if not isinstance(gates, list):
        raise CertificateError("uncertainty_manifest.logical_gates must be a list")
    gate_ids: set[str] = set()
    gate_states: list[str] = []
    for index, record in enumerate(gates):
        if not isinstance(record, dict):
            raise CertificateError(f"logical gate {index} is not an object")
        gate_id = record.get("id")
        state = record.get("state")
        evidence = record.get("evidence")
        if not isinstance(gate_id, str) or not gate_id:
            raise CertificateError(f"logical gate {index} has invalid id")
        if gate_id in gate_ids:
            raise CertificateError(f"duplicate logical gate id {gate_id!r}")
        if state not in NONBLOCKING_GATE_STATES:
            raise CertificateError(f"logical gate {gate_id!r} remains blocking: {state!r}")
        if not isinstance(evidence, str) or not evidence:
            raise CertificateError(f"logical gate {gate_id!r} lacks an evidence locator")
        gate_ids.add(gate_id)
        gate_states.append(state)

    return {
        "quantitative_channels": sorted(channel_ids),
        "logical_gate_count": len(gate_states),
        "logical_manifest_closed": all(state in CLOSED_GATE_STATES for state in gate_states),
        "synthetic_gate_count": sum(state == "SYNTHETIC_CONTROL" for state in gate_states),
    }


def _check_claimed(payload: dict[str, Any], key: str, actual: Fraction) -> None:
    if key not in payload:
        return
    claimed = as_fraction(payload[key], field=key)
    if claimed != actual:
        raise CertificateError(
            f"{key}: claimed {fraction_text(claimed)} but exact reconstruction gives {fraction_text(actual)}"
        )


def verify_affine_box(payload: dict[str, Any]) -> dict[str, Any]:
    nominal = as_fraction(payload.get("nominal"), field="nominal")
    terms = payload.get("terms")
    if not isinstance(terms, list) or not terms:
        raise CertificateError("terms must be a nonempty list")

    upper = nominal
    used_channels: list[str] = []
    contributions: list[dict[str, str]] = []
    for index, term in enumerate(terms):
        if not isinstance(term, dict):
            raise CertificateError(f"terms[{index}] is not an object")
        channel_id = term.get("channel_id")
        if not isinstance(channel_id, str) or not channel_id:
            raise CertificateError(f"terms[{index}].channel_id is invalid")
        coefficient = as_fraction(term.get("coefficient"), field=f"terms[{index}].coefficient")
        center = as_fraction(term.get("center"), field=f"terms[{index}].center")
        radius = as_fraction(term.get("radius"), field=f"terms[{index}].radius")
        if radius < 0:
            raise CertificateError(f"terms[{index}].radius is negative")
        center_part = coefficient * center
        uncertainty_part = abs(coefficient) * radius
        upper += center_part + uncertainty_part
        used_channels.append(channel_id)
        contributions.append(
            {
                "channel_id": channel_id,
                "center_part": fraction_text(center_part),
                "worst_case_increment": fraction_text(uncertainty_part),
            }
        )

    manifest = _manifest(payload, used_channels)
    _check_claimed(payload, "claimed_robust_upper", upper)
    return _result(payload, upper, manifest, {"contributions": contributions})


def verify_affine_polytope_dual(payload: dict[str, Any]) -> dict[str, Any]:
    nominal = as_fraction(payload.get("nominal"), field="nominal")
    objective_raw = payload.get("objective")
    matrix_raw = payload.get("A")
    bounds_raw = payload.get("b")
    dual_raw = payload.get("dual")
    feasible_raw = payload.get("feasible_point")
    if not all(isinstance(x, list) for x in (objective_raw, matrix_raw, bounds_raw, dual_raw, feasible_raw)):
        raise CertificateError("objective, A, b, dual, and feasible_point must be lists")

    objective = [as_fraction(x, field=f"objective[{i}]") for i, x in enumerate(objective_raw)]
    matrix = [
        [as_fraction(x, field=f"A[{i}][{j}]") for j, x in enumerate(row)]
        for i, row in enumerate(matrix_raw)
        if isinstance(row, list)
    ]
    if len(matrix) != len(matrix_raw):
        raise CertificateError("every A row must be a list")
    bounds = [as_fraction(x, field=f"b[{i}]") for i, x in enumerate(bounds_raw)]
    dual = [as_fraction(x, field=f"dual[{i}]") for i, x in enumerate(dual_raw)]
    feasible = [as_fraction(x, field=f"feasible_point[{i}]") for i, x in enumerate(feasible_raw)]

    if not objective:
        raise CertificateError("objective must be nonempty")
    if not matrix or len(matrix) != len(bounds) or len(matrix) != len(dual):
        raise CertificateError("A, b, and dual dimensions disagree")
    if any(len(row) != len(objective) for row in matrix):
        raise CertificateError("A width does not match objective dimension")
    if len(feasible) != len(objective):
        raise CertificateError("feasible_point dimension mismatch")
    if any(value < 0 for value in dual):
        raise CertificateError("dual multipliers must be nonnegative")

    dual_objective = transpose_mat_vec(matrix, dual)
    if dual_objective != objective:
        raise CertificateError("dual equality A^T y = objective fails")
    primal_slacks = [bound - value for value, bound in zip(mat_vec(matrix, feasible), bounds)]
    if any(slack < 0 for slack in primal_slacks):
        raise CertificateError("provided feasible_point violates A u <= b")

    robust_upper = nominal + dot(bounds, dual)
    channel_id = payload.get("channel_id")
    if not isinstance(channel_id, str) or not channel_id:
        raise CertificateError("channel_id is invalid")
    manifest = _manifest(payload, [channel_id])
    _check_claimed(payload, "claimed_robust_upper", robust_upper)
    return _result(
        payload,
        robust_upper,
        manifest,
        {
            "dual_bound": fraction_text(dot(bounds, dual)),
            "minimum_feasible_slack": fraction_text(min(primal_slacks)),
        },
    )


def _pick_coefficients(points: Sequence[QComplex], vector: Sequence[QComplex]) -> list[QComplex]:
    one = QComplex(Fraction(1), Fraction(0))
    coefficients: list[QComplex] = []
    for j, point in enumerate(points):
        accumulated = QComplex.zero()
        for k, other in enumerate(points):
            denominator = point + other.conjugate() - one
            if denominator.abs2() == 0:
                raise CertificateError(f"Pick denominator ({j},{k}) is zero")
            accumulated = accumulated + vector[k] / denominator
        coefficients.append(vector[j].conjugate() * accumulated)
    return coefficients


def pick_midpoint_direct(
    points: Sequence[QComplex], vector: Sequence[QComplex], values: Sequence[QComplex]
) -> Fraction:
    """Exact direct matrix contraction, exposed for regression tests."""

    one = QComplex(Fraction(1), Fraction(0))
    total = QComplex.zero()
    for j, point in enumerate(points):
        for k, other in enumerate(points):
            denominator = point + other.conjugate() - one
            entry = (values[j] + values[k].conjugate()) / denominator
            total = total + vector[j].conjugate() * entry * vector[k]
    if total.im != 0:
        raise CertificateError(f"exact Pick midpoint is not real: imaginary part {total.im}")
    return total.re


def verify_pick_disks(payload: dict[str, Any]) -> dict[str, Any]:
    points_raw = payload.get("points")
    vector_raw = payload.get("vector")
    samples_raw = payload.get("samples")
    if not all(isinstance(x, list) for x in (points_raw, vector_raw, samples_raw)):
        raise CertificateError("points, vector, and samples must be lists")
    if not points_raw or len(points_raw) != len(vector_raw) or len(points_raw) != len(samples_raw):
        raise CertificateError("points, vector, and samples must have equal nonzero length")

    points = [as_complex(value, field=f"points[{i}]") for i, value in enumerate(points_raw)]
    vector = [as_complex(value, field=f"vector[{i}]") for i, value in enumerate(vector_raw)]
    if all(value.abs2() == 0 for value in vector):
        raise CertificateError("Pick vector must be nonzero")
    for i, point in enumerate(points):
        if point.re <= Fraction(1, 2):
            raise CertificateError(f"points[{i}] is not in Re(s)>1/2")

    centers: list[QComplex] = []
    radii: list[Fraction] = []
    magnitude_bounds: list[Fraction] = []
    used_channels: list[str] = []
    for index, sample in enumerate(samples_raw):
        if not isinstance(sample, dict):
            raise CertificateError(f"samples[{index}] is not an object")
        channel_id = sample.get("channel_id")
        if not isinstance(channel_id, str) or not channel_id:
            raise CertificateError(f"samples[{index}].channel_id is invalid")
        center = as_complex(sample.get("center"), field=f"samples[{index}].center")
        radius = as_fraction(sample.get("radius"), field=f"samples[{index}].radius")
        magnitude_bound = as_fraction(
            sample.get("coefficient_abs_upper"), field=f"samples[{index}].coefficient_abs_upper"
        )
        if radius < 0 or magnitude_bound < 0:
            raise CertificateError(f"samples[{index}] has a negative radius or magnitude bound")
        centers.append(center)
        radii.append(radius)
        magnitude_bounds.append(magnitude_bound)
        used_channels.append(channel_id)

    coefficients = _pick_coefficients(points, vector)
    midpoint_complex = QComplex.zero()
    for coefficient, center in zip(coefficients, centers):
        midpoint_complex = midpoint_complex + coefficient * center
    midpoint = 2 * midpoint_complex.re

    uncertainty = Fraction(0)
    coefficient_records: list[dict[str, str]] = []
    for index, (coefficient, bound, radius) in enumerate(
        zip(coefficients, magnitude_bounds, radii)
    ):
        if bound * bound < coefficient.abs2():
            raise CertificateError(
                f"samples[{index}].coefficient_abs_upper is too small: "
                f"{fraction_text(bound * bound)} < |c|^2={fraction_text(coefficient.abs2())}"
            )
        uncertainty += 2 * bound * radius
        coefficient_records.append(
            {
                "re": fraction_text(coefficient.re),
                "im": fraction_text(coefficient.im),
                "abs2": fraction_text(coefficient.abs2()),
                "abs_upper": fraction_text(bound),
            }
        )

    robust_upper = midpoint + uncertainty
    direct_midpoint = pick_midpoint_direct(points, vector, centers)
    if direct_midpoint != midpoint:
        raise CertificateError("compressed Pick identity disagrees with direct contraction")

    manifest = _manifest(payload, used_channels)
    _check_claimed(payload, "claimed_midpoint", midpoint)
    _check_claimed(payload, "claimed_uncertainty_increment", uncertainty)
    _check_claimed(payload, "claimed_robust_upper", robust_upper)
    return _result(
        payload,
        robust_upper,
        manifest,
        {
            "midpoint": fraction_text(midpoint),
            "uncertainty_increment": fraction_text(uncertainty),
            "coefficients": coefficient_records,
        },
    )


def _result(
    payload: dict[str, Any],
    robust_upper: Fraction,
    manifest: dict[str, Any],
    details: dict[str, Any],
) -> dict[str, Any]:
    survives = robust_upper < 0
    if survives and manifest["logical_manifest_closed"]:
        status = "QUANTITATIVE_SURVIVAL_WITH_CLOSED_GATE_MANIFEST"
    elif survives:
        status = "CERTIFIED_QUANTITATIVE_SURVIVAL"
    else:
        status = "NOT_CERTIFIED"
    return {
        "schema": SCHEMA,
        "kind": payload["kind"],
        "status": status,
        "robust_upper": fraction_text(robust_upper),
        "strict_moat": fraction_text(-robust_upper) if survives else "0",
        "manifest": manifest,
        "details": details,
        "interpretation": (
            "Exact rational verification of the declared quantitative uncertainty set only. "
            "A Riemann-hypothesis conclusion additionally requires independent discharge of "
            "the logical gates and soundness of every primitive enclosure."
        ),
    }


def verify_certificate(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise CertificateError("certificate root must be an object")
    if payload.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    kind = payload.get("kind")
    if kind == "affine-box":
        return verify_affine_box(payload)
    if kind == "affine-polytope-dual":
        return verify_affine_polytope_dual(payload)
    if kind == "pick-disks":
        return verify_pick_disks(payload)
    raise CertificateError(f"unsupported certificate kind {kind!r}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--allow-not-certified", action="store_true")
    args = parser.parse_args(argv)

    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify_certificate(payload)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(json.dumps({"status": "REJECTED", "error": str(exc)}, indent=2), file=sys.stderr)
        return 2

    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] == "NOT_CERTIFIED" and not args.allow_not_certified:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
