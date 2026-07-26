#!/usr/bin/env python3
"""Exact checker for L-9307 support-gap chord and Hausdorff moment witnesses.

The checker uses only Python integers and fractions after JSON parsing. It
performs no special-function evaluation and no floating-point arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import string
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SCHEMA = "riemann.x9305-support-gap-hausdorff.v1"
PRODUCTION = "RIEMANN_XI_DIRECTED"
SYNTHETIC = "SYNTHETIC_MODEL"
SUPPORT_GATE = "CERTIFIED_COMPLETE_SLAB_SUPPORT_GAP"


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


def validate_sha256(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


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
    if terms < 16 or terms > 8192:
        raise CertificateError("log_terms must be between 16 and 8192")

    exponent = value.numerator.bit_length() - value.denominator.bit_length()

    def power_two(power: int) -> Fraction:
        return Fraction(1 << power, 1) if power >= 0 else Fraction(1, 1 << (-power))

    reduced = value / power_two(exponent)
    while reduced < 1:
        exponent -= 1
        reduced *= 2
    while reduced > 2:
        exponent += 1
        reduced /= 2

    reduced_log = _atanh_log_interval(reduced, terms)
    log_two = _atanh_log_interval(Fraction(2), terms)
    return reduced_log.add(log_two.scale(Fraction(exponent)))


def row_status(value: Interval) -> str:
    if value.upper < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lower >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def parse_values(
    data: dict[str, Any], classification: str, terms: int
) -> dict[str, dict[str, Any]]:
    raw_values = data.get("values")
    if not isinstance(raw_values, list) or len(raw_values) < 3:
        raise CertificateError("values must contain at least three nodes")

    synthetic_factors: list[tuple[Fraction, int]] = []
    if classification == SYNTHETIC:
        raw_factors = data.get("synthetic_factors")
        if not isinstance(raw_factors, list) or not raw_factors:
            raise CertificateError("synthetic model needs nonempty synthetic_factors")
        for index, raw in enumerate(raw_factors):
            if not isinstance(raw, dict):
                raise CertificateError("synthetic factor must be an object")
            y = rational(raw.get("y"), f"synthetic_factors[{index}].y")
            multiplicity = exact_int(
                raw.get("multiplicity", 1),
                f"synthetic_factors[{index}].multiplicity",
            )
            if y <= 0 or multiplicity <= 0:
                raise CertificateError("synthetic factors need y>0 and multiplicity>0")
            synthetic_factors.append((y, multiplicity))

    values: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(raw_values):
        if not isinstance(raw, dict):
            raise CertificateError(f"values[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in values:
            raise CertificateError("value IDs must be nonempty and unique")
        u = rational(raw.get("u"), f"values[{index}].u")
        if u < 0:
            raise CertificateError("value nodes must be nonnegative")

        if classification == SYNTHETIC and raw.get("residual_log") is None:
            result = Interval(Fraction(0), Fraction(0))
            for y, multiplicity in synthetic_factors:
                result = result.add(
                    log_positive_fraction(u + y, terms).scale(Fraction(multiplicity))
                )
            residual_log = result
        else:
            residual_log = interval(
                raw.get("residual_log"), f"values[{index}].residual_log"
            )
        values[identifier] = {"u": u, "residual_log": residual_log}
    return values


def parse_derivatives(data: dict[str, Any]) -> tuple[Fraction, dict[int, Interval]] | None:
    raw_base = data.get("derivative_base")
    if raw_base is None:
        return None
    if not isinstance(raw_base, dict):
        raise CertificateError("derivative_base must be an object")
    u = rational(raw_base.get("u"), "derivative_base.u")
    if u < 0:
        raise CertificateError("derivative base must be nonnegative")
    raw_derivatives = raw_base.get("derivatives")
    if not isinstance(raw_derivatives, list) or not raw_derivatives:
        raise CertificateError("derivatives must be a nonempty list")
    derivatives: dict[int, Interval] = {}
    for index, raw in enumerate(raw_derivatives):
        if not isinstance(raw, dict):
            raise CertificateError("derivative row must be an object")
        order = exact_int(raw.get("order"), f"derivatives[{index}].order")
        if order < 1 or order in derivatives:
            raise CertificateError("derivative orders must be unique positive integers")
        derivatives[order] = interval(
            raw.get("interval"), f"derivatives[{index}].interval"
        )
    return u, derivatives


def moment_b(
    order: int,
    base_u: Fraction,
    support_gap: Fraction,
    derivatives: dict[int, Interval],
) -> Interval:
    if order not in derivatives:
        raise CertificateError(f"missing derivative order {order}")
    sign = Fraction(1 if (order + 1) % 2 == 0 else -1)
    moment = derivatives[order].scale(sign / math.factorial(order - 1))
    return moment.scale((base_u + support_gap) ** order)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    classification = data.get("classification")
    if classification not in (PRODUCTION, SYNTHETIC):
        raise CertificateError("unsupported classification")
    support_gap = rational(data.get("support_gap"), "support_gap")
    if support_gap <= 0:
        raise CertificateError("support_gap must be positive")
    terms = exact_int(data.get("log_terms", 256), "log_terms")
    if terms < 16 or terms > 8192:
        raise CertificateError("log_terms must be between 16 and 8192")

    if classification == PRODUCTION:
        gate = data.get("support_gate")
        if not isinstance(gate, dict) or gate.get("status") != SUPPORT_GATE:
            raise CertificateError("missing certified complete-slab support gate")
        validate_sha256(gate.get("sha256"), "support_gate.sha256")

    values = parse_values(data, classification, terms)
    derivative_data = parse_derivatives(data)
    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be nonempty")

    outputs: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row_index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{row_index}] must be an object")
        row_id = raw.get("id")
        kind = raw.get("kind")
        if not isinstance(row_id, str) or not row_id or row_id in seen:
            raise CertificateError("row IDs must be nonempty and unique")
        seen.add(row_id)

        if kind == "support-gap-chord":
            nodes = raw.get("nodes")
            if (
                not isinstance(nodes, list)
                or len(nodes) != 3
                or any(node not in values for node in nodes)
            ):
                raise CertificateError("chord row needs three known node IDs")
            first, middle, last = (values[node] for node in nodes)
            u0, u1, u2 = first["u"], middle["u"], last["u"]
            if not u0 < u1 < u2:
                raise CertificateError("chord nodes must be strictly increasing")
            l1 = log_positive_fraction((u1 + support_gap) / (u0 + support_gap), terms)
            l2 = log_positive_fraction((u2 + support_gap) / (u0 + support_gap), terms)
            delta1 = middle["residual_log"].sub(first["residual_log"])
            delta2 = last["residual_log"].sub(first["residual_log"])
            value = l1.mul(delta2).sub(l2.mul(delta1))
            detail = {"nodes": nodes, "L1": ij(l1), "L2": ij(l2)}

        elif kind == "hausdorff-finite-difference":
            if derivative_data is None:
                raise CertificateError("moment row requires derivative_base")
            n = exact_int(raw.get("n"), f"rows[{row_index}].n")
            k = exact_int(raw.get("k"), f"rows[{row_index}].k")
            if n < 1 or k < 0:
                raise CertificateError("finite-difference row needs n>=1 and k>=0")
            base_u, derivatives = derivative_data
            value = Interval(Fraction(0), Fraction(0))
            moments = []
            for j in range(k + 1):
                order = n + j
                b = moment_b(order, base_u, support_gap, derivatives)
                coefficient = Fraction(((-1) ** j) * math.comb(k, j))
                value = value.add(b.scale(coefficient))
                moments.append({"order": order, "B": ij(b)})
            detail = {"n": n, "k": k, "moments": moments}

        elif kind in (
            "hausdorff-hankel-rayleigh",
            "hausdorff-one-minus-q-rayleigh",
        ):
            if derivative_data is None:
                raise CertificateError("moment Rayleigh row requires derivative_base")
            r = exact_int(raw.get("r", 0), f"rows[{row_index}].r")
            raw_vector = raw.get("vector")
            if r < 0 or not isinstance(raw_vector, list) or not raw_vector:
                raise CertificateError("Rayleigh row needs r>=0 and nonempty vector")
            vector = [
                rational(item, f"rows[{row_index}].vector[{index}]")
                for index, item in enumerate(raw_vector)
            ]
            base_u, derivatives = derivative_data
            value = Interval(Fraction(0), Fraction(0))
            dimension = len(vector)
            for i in range(dimension):
                for j in range(dimension):
                    order = r + 1 + i + j
                    entry = moment_b(order, base_u, support_gap, derivatives)
                    if kind == "hausdorff-one-minus-q-rayleigh":
                        entry = entry.sub(
                            moment_b(order + 1, base_u, support_gap, derivatives)
                        )
                    value = value.add(entry.scale(vector[i] * vector[j]))
            detail = {"r": r, "vector": [fj(item) for item in vector]}

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
    if classification == PRODUCTION and negative:
        verdict = "NEGATIVE_SUPPORT_GAP_RH_WITNESS_PENDING_REVIEW"
    elif classification == SYNTHETIC and negative:
        verdict = "SYNTHETIC_SUPPORT_GAP_SEPARATION"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_ROWS"

    canonical = {
        "schema": SCHEMA,
        "classification": classification,
        "support_gap": fj(support_gap),
        "rows": outputs,
    }
    return {
        **canonical,
        "certificate_sha256": canonical_sha(canonical),
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "This checker verifies finite rational interval contraction only. "
            "A production negative additionally requires a complete slab count/isolation "
            "gate, directed selected-factor residuals or logarithmic jets, completed-xi "
            "normalization review, and independent numerical reproduction."
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
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(text, end="")
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    return 0 if result["verdict"] != "UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
