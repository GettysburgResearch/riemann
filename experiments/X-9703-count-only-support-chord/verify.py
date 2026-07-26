#!/usr/bin/env python3
"""Exact checker for L-9703 count-only support-gap chord witnesses.

The checker uses only Python integers and fractions after JSON parsing.  It
evaluates no special function and uses no floating-point arithmetic.
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

SCHEMA = "riemann.x9703-count-only-support-chord.v1"
PRODUCTION = "RIEMANN_XI_DIRECTED"
SYNTHETIC = "SYNTHETIC_MODEL"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
COUNT_GATE = "CERTIFIED_TOTAL_ZETA_ZERO_COUNT"


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


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
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


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def unique_integer(value: Interval, name: str) -> int:
    first = ceil_fraction(value.lower)
    last = floor_fraction(value.upper)
    if first != last:
        raise CertificateError(f"{name} does not isolate one integer")
    return first


def validate_sha256(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a SHA-256 hexadecimal digest")
    return value.lower()


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def square_interval(value: Interval) -> Interval:
    upper = max(value.lower * value.lower, value.upper * value.upper)
    if value.lower <= 0 <= value.upper:
        lower = Fraction(0)
    else:
        lower = min(value.lower * value.lower, value.upper * value.upper)
    return Interval(lower, upper)


def modulus_squared(real: Interval, imag: Interval) -> Interval:
    return square_interval(real).add(square_interval(imag))


def _atanh_log_interval(value: Fraction, terms: int) -> Interval:
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


def log_positive_fraction(value: Fraction, terms: int) -> Interval:
    if value <= 0:
        raise CertificateError("logarithm input must be positive")
    exponent = value.numerator.bit_length() - value.denominator.bit_length()

    def power_two(power: int) -> Fraction:
        return (
            Fraction(1 << power, 1)
            if power >= 0
            else Fraction(1, 1 << (-power))
        )

    reduced = value / power_two(exponent)
    while reduced < 1:
        exponent -= 1
        reduced *= 2
    while reduced > 2:
        exponent += 1
        reduced /= 2
    return _atanh_log_interval(reduced, terms).add(
        _atanh_log_interval(Fraction(2), terms).scale(Fraction(exponent))
    )


def log_positive_interval(value: Interval, terms: int) -> Interval:
    if value.lower <= 0:
        raise CertificateError("modulus-square interval touches zero")
    return Interval(
        log_positive_fraction(value.lower, terms).lower,
        log_positive_fraction(value.upper, terms).upper,
    )


def row_status(value: Interval) -> str:
    if value.upper < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lower >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def parse_points(
    data: dict[str, Any], classification: str, terms: int
) -> dict[str, dict[str, Any]]:
    raw_points = data.get("points")
    if not isinstance(raw_points, list) or len(raw_points) < 3:
        raise CertificateError("points must contain at least three entries")

    synthetic_factors: list[tuple[Fraction, int]] = []
    if classification == SYNTHETIC:
        raw_factors = data.get("synthetic_factors")
        if not isinstance(raw_factors, list) or not raw_factors:
            raise CertificateError("synthetic model needs synthetic_factors")
        for index, raw in enumerate(raw_factors):
            if not isinstance(raw, dict):
                raise CertificateError("synthetic factor must be an object")
            y = rational(raw.get("y"), f"synthetic_factors[{index}].y")
            multiplicity = exact_int(
                raw.get("multiplicity", 1),
                f"synthetic_factors[{index}].multiplicity",
            )
            if y < 0 or multiplicity <= 0:
                raise CertificateError("synthetic factor needs y>=0 and multiplicity>0")
            synthetic_factors.append((y, multiplicity))

    points: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"points[{index}] must be an object")
        identifier = raw.get("id")
        u = rational(raw.get("u"), f"points[{index}].u")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in points
            or u <= 0
        ):
            raise CertificateError("point IDs must be unique and nodes positive")

        if classification == SYNTHETIC:
            log_value = Interval(Fraction(0), Fraction(0))
            for y, multiplicity in synthetic_factors:
                log_value = log_value.add(
                    log_positive_fraction(u + y, terms).scale(
                        Fraction(multiplicity)
                    )
                )
        else:
            rectangle = raw.get("xi_rectangle")
            if not isinstance(rectangle, dict):
                raise CertificateError("production point needs xi_rectangle")
            real = interval(rectangle.get("real"), f"points[{index}].real")
            imag = interval(rectangle.get("imag"), f"points[{index}].imag")
            h_value = modulus_squared(real, imag)
            log_value = log_positive_interval(h_value, terms)
            canonical = {
                "id": identifier,
                "u": fj(u),
                "xi_rectangle": {"real": ij(real), "imag": ij(imag)},
            }
            declared = raw.get("point_sha256")
            if declared is not None and validate_sha256(
                declared, "point_sha256"
            ) != canonical_sha(canonical):
                raise CertificateError(f"point digest mismatch for {identifier}")

        points[identifier] = {"u": u, "log_h": log_value}
    return points


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    classification = data.get("classification")
    if classification not in (PRODUCTION, SYNTHETIC):
        raise CertificateError("unsupported classification")
    if data.get("normalization_id") not in (None, NORMALIZATION):
        raise CertificateError("completed-xi normalization mismatch")

    slab = data.get("slab")
    if not isinstance(slab, dict):
        raise CertificateError("slab must be an object")
    lower = rational(slab.get("lower"), "slab.lower")
    upper = rational(slab.get("upper"), "slab.upper")
    target = rational(data.get("target"), "target")
    if not lower < target < upper:
        raise CertificateError("target must lie strictly inside the slab")
    support_gap = min((target - lower) ** 2, (upper - target) ** 2)
    if support_gap <= 0:
        raise CertificateError("support gap must be positive")

    total_count_interval = interval(
        data.get("total_count_interval"), "total_count_interval"
    )
    total_count = unique_integer(total_count_interval, "total_count_interval")
    if total_count < 0:
        raise CertificateError("total count must be nonnegative")
    if classification == PRODUCTION:
        gate = data.get("count_gate")
        if not isinstance(gate, dict) or gate.get("status") != COUNT_GATE:
            raise CertificateError("missing certified total-count gate")
        validate_sha256(gate.get("sha256"), "count_gate.sha256")

    terms = exact_int(data.get("log_terms", 256), "log_terms")
    if terms < 32 or terms > 8192:
        raise CertificateError("log_terms must be between 32 and 8192")
    points = parse_points(data, classification, terms)

    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be a nonempty array")
    outputs: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row_index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{row_index}] must be an object")
        row_id = raw.get("id")
        identifiers = raw.get("points")
        if not isinstance(row_id, str) or not row_id or row_id in seen:
            raise CertificateError("row IDs must be nonempty and unique")
        seen.add(row_id)
        if (
            not isinstance(identifiers, list)
            or len(identifiers) != 3
            or any(identifier not in points for identifier in identifiers)
        ):
            raise CertificateError("each row needs three known point IDs")

        first, middle, last = (points[identifier] for identifier in identifiers)
        u0, u1, u2 = first["u"], middle["u"], last["u"]
        if not 0 < u0 < u1 < u2:
            raise CertificateError("row nodes must satisfy 0<u0<u1<u2")

        l1 = log_positive_fraction(
            (u1 + support_gap) / (u0 + support_gap), terms
        )
        l2 = log_positive_fraction(
            (u2 + support_gap) / (u0 + support_gap), terms
        )
        raw_chord = l1.mul(last["log_h"].sub(first["log_h"])).sub(
            l2.mul(middle["log_h"].sub(first["log_h"]))
        )
        phi0 = l1.mul(log_positive_fraction(u2 / u0, terms)).sub(
            l2.mul(log_positive_fraction(u1 / u0, terms))
        )
        adjusted = raw_chord.sub(phi0.scale(Fraction(total_count)))
        outputs.append(
            {
                "id": row_id,
                "points": identifiers,
                "L1": ij(l1),
                "L2": ij(l2),
                "raw_chord": ij(raw_chord),
                "phi0": ij(phi0),
                "interval": ij(adjusted),
                "status": row_status(adjusted),
            }
        )

    negative = [row for row in outputs if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in outputs if row["status"] == "UNRESOLVED"]
    if classification == PRODUCTION and negative:
        verdict = "NEGATIVE_COUNT_ONLY_SUPPORT_CHORD_PENDING_REVIEW"
    elif classification == SYNTHETIC and negative:
        verdict = "SYNTHETIC_COUNT_ONLY_SEPARATION"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_ROWS"

    canonical = {
        "schema": SCHEMA,
        "classification": classification,
        "slab": {"lower": fj(lower), "upper": fj(upper)},
        "target": fj(target),
        "support_gap": fj(support_gap),
        "total_count": total_count,
        "rows": outputs,
    }
    return {
        **canonical,
        "certificate_sha256": canonical_sha(canonical),
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "The checker proves only finite rational interval contraction.  A "
            "production negative additionally requires an independently reviewed "
            "multiplicity-aware total count, directed completed-xi rectangles, "
            "L-7501/L-9703 review, normalization review, and independent numerical "
            "reproduction."
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
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as error:
        print(json.dumps({"verified": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(text, end="")
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    return 0 if result["verdict"] != "UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
