#!/usr/bin/env python3
"""Exact fixed-vector checker for arbitrary-height complex Pick certificates.

The producer supplies exact rational points, two outward rectangles for
``F=xi'/xi``, denominator lower bounds, and one frozen Gaussian-rational vector.
This checker intersects the primitive rectangles and contracts the Pick matrix
symbolically before interval propagation:

    v* K v = 2 Re sum_j c_j F_j,
    c_j = conj(v_j) sum_k v_k/(s_j+conj(s_k)-1).

It proves only the exact contraction and sign implied by the supplied primitive
rectangles.  It does not independently evaluate a special function or prove the
parent RH implication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.xi-cross-pick-balls.v1"
VERIFY_SCHEMA = "riemann.xi-cross-pick-verification.v1"


class CertificateError(ValueError):
    pass


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name}: boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name}: invalid rational") from exc
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        denominator = int(value["denominator"])
        if denominator == 0:
            raise CertificateError(f"{name}: zero denominator")
        return Fraction(int(value["numerator"]), denominator)
    raise CertificateError(f"{name}: exact rational required")


def dyadic(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict) or set(value) != {"mantissa", "exponent"}:
        raise CertificateError(f"{name}: dyadic endpoint required")
    mantissa = int(value["mantissa"])
    exponent = int(value["exponent"])
    return (
        Fraction(mantissa << exponent, 1)
        if exponent >= 0
        else Fraction(mantissa, 1 << (-exponent))
    )


def interval(value: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(value, dict) or set(value) != {"lower", "upper"}:
        raise CertificateError(f"{name}: interval required")
    lower = dyadic(value["lower"], f"{name}.lower")
    upper = dyadic(value["upper"], f"{name}.upper")
    if lower > upper:
        raise CertificateError(f"{name}: reversed interval")
    return lower, upper


def intersection(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
    name: str,
) -> tuple[Fraction, Fraction]:
    lower = max(left[0], right[0])
    upper = min(left[1], right[1])
    if lower > upper:
        raise CertificateError(f"{name}: directed assemblies are disjoint")
    return lower, upper


def scale_interval(
    coefficient: Fraction, value: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    if coefficient >= 0:
        return coefficient * value[0], coefficient * value[1]
    return coefficient * value[1], coefficient * value[0]


@dataclass(frozen=True)
class QComplex:
    re: Fraction
    im: Fraction

    def __add__(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re + other.re, self.im + other.im)

    def __mul__(self, other: "QComplex") -> "QComplex":
        return QComplex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conjugate(self) -> "QComplex":
        return QComplex(self.re, -self.im)

    def inverse(self) -> "QComplex":
        denominator = self.re * self.re + self.im * self.im
        if denominator == 0:
            raise CertificateError("complex division by zero")
        return QComplex(self.re / denominator, -self.im / denominator)

    def __truediv__(self, other: "QComplex") -> "QComplex":
        return self * other.inverse()

    def abs2(self) -> Fraction:
        return self.re * self.re + self.im * self.im


ZERO = QComplex(Fraction(0), Fraction(0))


def parse_complex(value: Any, name: str) -> QComplex:
    if not isinstance(value, dict) or set(value) != {"re", "im"}:
        raise CertificateError(f"{name}: exact complex value required")
    return QComplex(
        rational(value["re"], f"{name}.re"),
        rational(value["im"], f"{name}.im"),
    )


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def interval_json(
    value: tuple[Fraction, Fraction]
) -> dict[str, dict[str, str]]:
    return {
        "lower": fraction_json(value[0]),
        "upper": fraction_json(value[1]),
    }


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(payload: dict[str, Any]) -> dict[str, object]:
    if payload.get("schema") != SCHEMA:
        raise CertificateError("wrong schema")
    points_raw = payload.get("points")
    channel = payload.get("channel")
    if not isinstance(points_raw, list) or not isinstance(channel, dict):
        raise CertificateError("points and channel are required")

    points: dict[
        str,
        tuple[
            Fraction,
            Fraction,
            tuple[Fraction, Fraction],
            tuple[Fraction, Fraction],
        ],
    ] = {}
    for index, point in enumerate(points_raw):
        if not isinstance(point, dict):
            raise CertificateError(f"points[{index}] is not an object")
        identifier = point.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in points:
            raise CertificateError("invalid or duplicate point ID")
        x = rational(point.get("x"), f"points[{index}].x")
        t = rational(point.get("t"), f"points[{index}].t")
        if x <= 0:
            raise CertificateError("every point must lie in the open half-plane")
        via_xi = point.get("f_via_xi")
        via_parts = point.get("f_via_parts")
        if not isinstance(via_xi, dict) or not isinstance(via_parts, dict):
            raise CertificateError("both directed assemblies are required")
        real = intersection(
            interval(via_xi["real"], f"{identifier}.via_xi.real"),
            interval(via_parts["real"], f"{identifier}.via_parts.real"),
            f"{identifier}.real",
        )
        imag = intersection(
            interval(via_xi["imag"], f"{identifier}.via_xi.imag"),
            interval(via_parts["imag"], f"{identifier}.via_parts.imag"),
            f"{identifier}.imag",
        )
        if "zeta_abs_lower" in point:
            zeta_lower = dyadic(
                point["zeta_abs_lower"], f"{identifier}.zeta_abs_lower"
            )
            if zeta_lower <= 0:
                raise CertificateError("zeta denominator lower bound is not positive")
        points[identifier] = x, t, real, imag

    identifiers = channel.get("points")
    vector_raw = channel.get("vector")
    if (
        not isinstance(identifiers, list)
        or not isinstance(vector_raw, list)
        or len(identifiers) != len(vector_raw)
        or not identifiers
    ):
        raise CertificateError("channel point/vector arrays disagree")
    selected = []
    for identifier in identifiers:
        if identifier not in points:
            raise CertificateError(f"unknown channel point {identifier!r}")
        selected.append(points[identifier])
    vector = [
        parse_complex(value, f"vector[{index}]")
        for index, value in enumerate(vector_raw)
    ]
    if not any(value.abs2() for value in vector):
        raise CertificateError("zero vector")

    coefficients: list[QComplex] = []
    for j, (x_j, t_j, _, _) in enumerate(selected):
        inner = ZERO
        for k, (x_k, t_k, _, _) in enumerate(selected):
            denominator = QComplex(x_j + x_k, t_j - t_k)
            inner = inner + vector[k] / denominator
        coefficients.append(vector[j].conjugate() * inner)

    lower = Fraction(0)
    upper = Fraction(0)
    terms = []
    for identifier, coefficient, (_, _, real, imag) in zip(
        identifiers, coefficients, selected
    ):
        # 2 Re((a+ib)(r+ii)) = 2(ar-bi).
        real_term = scale_interval(2 * coefficient.re, real)
        imag_term = scale_interval(-2 * coefficient.im, imag)
        term = real_term[0] + imag_term[0], real_term[1] + imag_term[1]
        lower += term[0]
        upper += term[1]
        terms.append(
            {
                "point": identifier,
                "coefficient": {
                    "re": fraction_json(coefficient.re),
                    "im": fraction_json(coefficient.im),
                },
                "term": interval_json(term),
            }
        )

    norm_squared = sum((value.abs2() for value in vector), Fraction(0))
    normalized = lower / norm_squared, upper / norm_squared
    status = (
        "CERTIFIED_NEGATIVE"
        if upper < 0
        else (
            "CERTIFIED_POSITIVE"
            if lower > 0
            else "UNRESOLVED_ZERO_TOUCH"
        )
    )
    result: dict[str, object] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": status,
        "point_count": len(selected),
        "raw_interval": interval_json((lower, upper)),
        "normalized_interval": interval_json(normalized),
        "vector_norm_squared": fraction_json(norm_squared),
        "terms": terms,
        "proof_boundary": (
            "Exact contraction and interval propagation from supplied primitive "
            "rectangles only. Parent xi normalization, RH implication, and "
            "independent directed reproduction remain separate gates."
        ),
    }
    result["verification_sha256"] = canonical_digest(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(payload)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        raise SystemExit(f"REJECTED: {exc}") from exc
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
