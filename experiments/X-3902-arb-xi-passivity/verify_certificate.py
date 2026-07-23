#!/usr/bin/env python3
"""Exact checker for rigorous xi'/xi passivity certificates.

The producer supplies only exact rational/dyadic points and outward binary
rectangles for primitive evaluations. This checker uses Python integers and
``fractions.Fraction`` only. It reconstructs assembly intersections,
functional-equation gates, every exact contraction coefficient, and every
reported sign.

The checker does *not* evaluate zeta, xi, gamma, or any transcendental
function. Those primitive enclosures remain the responsibility of an Arb (or
other directed-ball) producer and must be independently reproduced before a
counterexample is accepted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

SCHEMA = "riemann.xi-passivity-balls.v1"
VERIFY_SCHEMA = "riemann.xi-passivity-balls.verification.v1"


class CertificateError(ValueError):
    """Raised when a certificate is malformed or mathematically inconsistent."""


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a base-10 integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def parse_binary(value: Any, name: str) -> Fraction:
    """Parse ``mantissa * 2**exponent`` exactly."""
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    mantissa = parse_int(value.get("mantissa"), f"{name}.mantissa")
    exponent = parse_int(value.get("exponent"), f"{name}.exponent")
    if exponent >= 0:
        return Fraction(mantissa << exponent, 1)
    return Fraction(mantissa, 1 << (-exponent))


def binary_json(value: Fraction) -> dict[str, str | int]:
    """Serialize a dyadic fraction canonically as mantissa times a power of two."""
    denominator = value.denominator
    if denominator & (denominator - 1):
        raise CertificateError("binary endpoint is not dyadic")
    exponent = -(denominator.bit_length() - 1)
    mantissa = value.numerator
    while mantissa and mantissa % 2 == 0:
        mantissa //= 2
        exponent += 1
    return {"mantissa": str(mantissa), "exponent": exponent}


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    @classmethod
    def parse(cls, value: Any, name: str) -> "Interval":
        if not isinstance(value, dict):
            raise CertificateError(f"{name} must be an object")

        def endpoint(raw: Any, endpoint_name: str) -> Fraction:
            if not isinstance(raw, dict):
                raise CertificateError(f"{endpoint_name} must be an object")
            if "mantissa" in raw or "exponent" in raw:
                return parse_binary(raw, endpoint_name)
            return parse_fraction(raw, endpoint_name)

        return cls(
            endpoint(value.get("lower"), f"{name}.lower"),
            endpoint(value.get("upper"), f"{name}.upper"),
        )

    @classmethod
    def exact(cls, value: Fraction) -> "Interval":
        return cls(value, value)

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def subtract(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, coefficient: Fraction) -> "Interval":
        if coefficient >= 0:
            return Interval(self.lower * coefficient, self.upper * coefficient)
        return Interval(self.upper * coefficient, self.lower * coefficient)

    def multiply(self, other: "Interval") -> "Interval":
        products = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(products), max(products))

    def intersect(self, other: "Interval") -> "Interval":
        lower = max(self.lower, other.lower)
        upper = min(self.upper, other.upper)
        if lower > upper:
            raise CertificateError("independent assembly intervals are disjoint")
        return Interval(lower, upper)

    def contains_zero(self) -> bool:
        return self.lower <= 0 <= self.upper

    def status_nonnegative_under_rh(self) -> str:
        """Classify a score whose RH-allowed region is [0,+infinity)."""
        if self.upper < 0:
            return "CERTIFIED_NEGATIVE"
        if self.lower >= 0:
            return "CERTIFIED_NONNEGATIVE"
        return "UNRESOLVED_ZERO_TOUCH"

    def to_json(self) -> dict[str, object]:
        result: dict[str, object] = {
            "lower": fraction_json(self.lower),
            "upper": fraction_json(self.upper),
        }
        if self.lower.denominator & (self.lower.denominator - 1) == 0:
            result["lower_binary"] = binary_json(self.lower)
        if self.upper.denominator & (self.upper.denominator - 1) == 0:
            result["upper_binary"] = binary_json(self.upper)
        return result


@dataclass(frozen=True)
class ComplexRectangle:
    real: Interval
    imag: Interval

    @classmethod
    def parse(cls, value: Any, name: str) -> "ComplexRectangle":
        if not isinstance(value, dict):
            raise CertificateError(f"{name} must be an object")
        return cls(
            Interval.parse(value.get("real"), f"{name}.real"),
            Interval.parse(value.get("imag"), f"{name}.imag"),
        )

    def intersect(self, other: "ComplexRectangle") -> "ComplexRectangle":
        return ComplexRectangle(self.real.intersect(other.real), self.imag.intersect(other.imag))

    def add(self, other: "ComplexRectangle") -> "ComplexRectangle":
        return ComplexRectangle(self.real.add(other.real), self.imag.add(other.imag))

    def contains_zero(self) -> bool:
        return self.real.contains_zero() and self.imag.contains_zero()

    def to_json(self) -> dict[str, object]:
        return {"real": self.real.to_json(), "imag": self.imag.to_json()}


@dataclass(frozen=True)
class Point:
    identifier: str
    x: Fraction
    t: Fraction
    f: ComplexRectangle
    reflected_f: ComplexRectangle
    zeta_abs_lower: Fraction
    reflected_zeta_abs_lower: Fraction


def sum_scaled(terms: Iterable[tuple[Fraction, Interval]]) -> Interval:
    total = Interval.exact(Fraction(0))
    for coefficient, interval in terms:
        total = total.add(interval.scale(coefficient))
    return total


def point_from_json(raw: Any, index: int) -> Point:
    name = f"points[{index}]"
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    identifier = raw.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise CertificateError(f"{name}.id must be a nonempty string")
    x = parse_fraction(raw.get("x"), f"{name}.x")
    t = parse_fraction(raw.get("t"), f"{name}.t")
    if x <= 0:
        raise CertificateError(f"{name} is not strictly right of the critical line")

    via_xi = ComplexRectangle.parse(raw.get("f_via_xi"), f"{name}.f_via_xi")
    via_parts = ComplexRectangle.parse(raw.get("f_via_parts"), f"{name}.f_via_parts")
    f = via_xi.intersect(via_parts)

    reflected = raw.get("reflected")
    if not isinstance(reflected, dict):
        raise CertificateError(f"{name}.reflected must be an object")
    reflected_x = parse_fraction(reflected.get("x"), f"{name}.reflected.x")
    reflected_t = parse_fraction(reflected.get("t"), f"{name}.reflected.t")
    if reflected_x != -x or reflected_t != -t:
        raise CertificateError(f"{name}.reflected is not the exact point 1-s")
    reflected_xi = ComplexRectangle.parse(
        reflected.get("f_via_xi"), f"{name}.reflected.f_via_xi"
    )
    reflected_parts = ComplexRectangle.parse(
        reflected.get("f_via_parts"), f"{name}.reflected.f_via_parts"
    )
    reflected_f = reflected_xi.intersect(reflected_parts)

    zeta_abs_lower = parse_binary(raw.get("zeta_abs_lower"), f"{name}.zeta_abs_lower")
    reflected_zeta_abs_lower = parse_binary(
        reflected.get("zeta_abs_lower"), f"{name}.reflected.zeta_abs_lower"
    )
    if zeta_abs_lower <= 0 or reflected_zeta_abs_lower <= 0:
        raise CertificateError(f"{name} has a zeta denominator ball touching zero")

    residual = f.add(reflected_f)
    if not residual.contains_zero():
        raise CertificateError(f"{name} fails the completed-xi functional equation gate")

    claimed = raw.get("claimed_intersection")
    if claimed is not None:
        claimed_rectangle = ComplexRectangle.parse(claimed, f"{name}.claimed_intersection")
        if claimed_rectangle != f:
            raise CertificateError(f"{name}.claimed_intersection mismatch")

    return Point(
        identifier=identifier,
        x=x,
        t=t,
        f=f,
        reflected_f=reflected_f,
        zeta_abs_lower=zeta_abs_lower,
        reflected_zeta_abs_lower=reflected_zeta_abs_lower,
    )


def require_point(points: dict[str, Point], identifier: Any, name: str) -> Point:
    if not isinstance(identifier, str) or identifier not in points:
        raise CertificateError(f"{name} references an unknown point")
    return points[identifier]


def require_same_height(selected: Sequence[Point], name: str) -> None:
    if not selected:
        raise CertificateError(f"{name} has no points")
    if any(point.t != selected[0].t for point in selected[1:]):
        raise CertificateError(f"{name} mixes different ordinates")


def scalar_channel(channel: dict[str, Any], points: dict[str, Point], name: str) -> tuple[Interval, dict[str, object]]:
    point = require_point(points, channel.get("point"), f"{name}.point")
    return point.f.real, {"point": point.identifier, "coefficient": fraction_json(Fraction(1))}


def two_channel(channel: dict[str, Any], points: dict[str, Point], name: str, kind: str) -> tuple[Interval, dict[str, object]]:
    ids = channel.get("points")
    if not isinstance(ids, list) or len(ids) != 2:
        raise CertificateError(f"{name}.points must contain exactly two IDs")
    p1 = require_point(points, ids[0], f"{name}.points[0]")
    p2 = require_point(points, ids[1], f"{name}.points[1]")
    require_same_height([p1, p2], name)
    if not p1.x < p2.x:
        raise CertificateError(f"{name} requires 0 < x1 < x2")
    denominator = p2.x * p2.x - p1.x * p1.x
    if kind == "two-channel-A":
        c1 = Fraction(1, 1) / (p1.x * denominator)
        c2 = -Fraction(1, 1) / (p2.x * denominator)
    else:
        c1 = -p1.x / denominator
        c2 = p2.x / denominator
    interval = sum_scaled([(c1, p1.f.real), (c2, p2.f.real)])
    return interval, {
        "points": [p1.identifier, p2.identifier],
        "coefficients": [fraction_json(c1), fraction_json(c2)],
    }


def divided_difference_channel(
    channel: dict[str, Any], points: dict[str, Point], name: str
) -> tuple[Interval, dict[str, object]]:
    ids = channel.get("points")
    if not isinstance(ids, list) or len(ids) < 2:
        raise CertificateError(f"{name}.points must contain at least two IDs")
    selected = [require_point(points, identifier, f"{name}.points") for identifier in ids]
    require_same_height(selected, name)
    nodes = [point.x * point.x for point in selected]
    if nodes != sorted(nodes) or len(set(nodes)) != len(nodes):
        raise CertificateError(f"{name} requires strictly increasing squared offsets")
    order = len(nodes) - 1
    orientation = -1 if (order - 1) % 2 else 1
    coefficients: list[Fraction] = []
    for index, point in enumerate(selected):
        denominator = Fraction(1)
        for j, node in enumerate(nodes):
            if j != index:
                denominator *= nodes[index] - node
        coefficients.append(Fraction(orientation) * point.x / denominator)
    interval = sum_scaled(
        (coefficient, point.f.real)
        for coefficient, point in zip(coefficients, selected)
    )
    return interval, {
        "points": [point.identifier for point in selected],
        "order": order,
        "orientation": orientation,
        "coefficients": [fraction_json(value) for value in coefficients],
    }


def real_pick_channel(
    channel: dict[str, Any], points: dict[str, Point], name: str
) -> tuple[Interval, dict[str, object]]:
    ids = channel.get("points")
    vector_raw = channel.get("vector")
    if not isinstance(ids, list) or not isinstance(vector_raw, list) or len(ids) != len(vector_raw):
        raise CertificateError(f"{name} requires equally sized point and vector arrays")
    if not ids:
        raise CertificateError(f"{name} has an empty vector")
    selected = [require_point(points, identifier, f"{name}.points") for identifier in ids]
    require_same_height(selected, name)
    vector = [parse_fraction(value, f"{name}.vector[{index}]") for index, value in enumerate(vector_raw)]
    if all(value == 0 for value in vector):
        raise CertificateError(f"{name}.vector is zero")
    coefficients: list[Fraction] = []
    for point_j, c_j in zip(selected, vector):
        inner = Fraction(0)
        for point_k, c_k in zip(selected, vector):
            inner += c_k / (point_j.x + point_k.x)
        coefficients.append(2 * c_j * inner)
    interval = sum_scaled(
        (coefficient, point.f.real)
        for coefficient, point in zip(coefficients, selected)
    )
    return interval, {
        "points": [point.identifier for point in selected],
        "vector": [fraction_json(value) for value in vector],
        "contracted_coefficients": [fraction_json(value) for value in coefficients],
    }


def evaluate_channel(channel: Any, index: int, points: dict[str, Point]) -> dict[str, object]:
    name = f"channels[{index}]"
    if not isinstance(channel, dict):
        raise CertificateError(f"{name} must be an object")
    identifier = channel.get("id")
    kind = channel.get("kind")
    if not isinstance(identifier, str) or not identifier:
        raise CertificateError(f"{name}.id must be a nonempty string")
    if kind == "scalar":
        interval, reconstruction = scalar_channel(channel, points, name)
    elif kind in {"two-channel-A", "two-channel-B", "secant"}:
        interval, reconstruction = two_channel(channel, points, name, kind)
    elif kind == "bernstein-divided-difference":
        interval, reconstruction = divided_difference_channel(channel, points, name)
    elif kind == "real-pick-rayleigh":
        interval, reconstruction = real_pick_channel(channel, points, name)
    else:
        raise CertificateError(f"{name}.kind is unsupported")

    status = interval.status_nonnegative_under_rh()
    claimed_status = channel.get("claimed_status")
    if claimed_status is not None and claimed_status != status:
        raise CertificateError(f"{name}.claimed_status mismatch")
    claimed_interval = channel.get("claimed_interval")
    if claimed_interval is not None and Interval.parse(claimed_interval, f"{name}.claimed_interval") != interval:
        raise CertificateError(f"{name}.claimed_interval mismatch")
    return {
        "id": identifier,
        "kind": kind,
        "interval": interval.to_json(),
        "status": status,
        "reconstruction": reconstruction,
    }


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verify_certificate(data: dict[str, Any]) -> dict[str, object]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    points_raw = data.get("points")
    channels_raw = data.get("channels")
    declared_ids = data.get("declared_channel_ids")
    if not isinstance(points_raw, list) or not isinstance(channels_raw, list):
        raise CertificateError("points and channels must be arrays")
    if not isinstance(declared_ids, list) or not all(isinstance(value, str) for value in declared_ids):
        raise CertificateError("declared_channel_ids must be an array of strings")

    points: dict[str, Point] = {}
    point_summaries: list[dict[str, object]] = []
    for index, raw in enumerate(points_raw):
        point = point_from_json(raw, index)
        if point.identifier in points:
            raise CertificateError("duplicate point ID")
        points[point.identifier] = point
        residual = point.f.add(point.reflected_f)
        point_summaries.append(
            {
                "id": point.identifier,
                "x": fraction_json(point.x),
                "t": fraction_json(point.t),
                "f_intersection": point.f.to_json(),
                "functional_equation_residual": residual.to_json(),
                "zeta_abs_lower": fraction_json(point.zeta_abs_lower),
                "reflected_zeta_abs_lower": fraction_json(point.reflected_zeta_abs_lower),
            }
        )

    channel_results = [
        evaluate_channel(channel, index, points) for index, channel in enumerate(channels_raw)
    ]
    actual_ids = [result["id"] for result in channel_results]
    if len(set(actual_ids)) != len(actual_ids):
        raise CertificateError("duplicate channel ID")
    if declared_ids != actual_ids:
        raise CertificateError(
            "declared_channel_ids must exactly equal the ordered used channel IDs"
        )

    negative = [result["id"] for result in channel_results if result["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [result["id"] for result in channel_results if result["status"] == "UNRESOLVED_ZERO_TOUCH"]
    status = "CERTIFIED_NEGATIVE_WITNESS_PENDING_INDEPENDENT_REPRODUCTION" if negative else (
        "NO_NEGATIVE_CHANNEL_UNRESOLVED_PRESENT" if unresolved else "CERTIFIED_NONNEGATIVE_CONTROLS_ONLY"
    )
    result: dict[str, object] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": status,
        "point_count": len(points),
        "channel_count": len(channel_results),
        "negative_channels": negative,
        "unresolved_channels": unresolved,
        "points": point_summaries,
        "channels": channel_results,
        "proof_boundary": (
            "This checker verifies exact contraction and strict signs from the supplied "
            "primitive outward rectangles. It does not independently evaluate xi, zeta, "
            "or the analytic RH implication. Any negative requires an independent directed "
            "special-function reproduction and review of the named logical gates."
        ),
    }
    result["verification_sha256"] = canonical_digest(result)
    claimed_digest = data.get("certificate_sha256")
    if claimed_digest is not None:
        body = dict(data)
        body.pop("certificate_sha256", None)
        if claimed_digest != canonical_digest(body):
            raise CertificateError("certificate_sha256 mismatch")
        result["certificate_sha256"] = claimed_digest
    return result


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify_certificate(load_json(args.certificate))
    except CertificateError as exc:
        result = {"schema": VERIFY_SCHEMA, "verified": False, "status": "REJECTED", "reason": str(exc)}
        text = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
