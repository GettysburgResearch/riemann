#!/usr/bin/env python3
"""Exact algebra checker for L-22101 and R-22102.

This checker contains no prime or zeta data.  It verifies the formal finite-
difference coefficients, the three polynomial moments, the exact pole-model
factor, and the narrow-window diagonal scaling.
"""
from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x22101-prime-ramp-wavelet.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer, not Boolean")
    return value


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not rational") from exc
    if isinstance(value, list) and len(value) == 2:
        p = integer(value[0], name + "[0]")
        q = integer(value[1], name + "[1]")
        if q == 0:
            raise CertificateError(f"{name} denominator is zero")
        return Fraction(p, q)
    raise CertificateError(f"{name} must be an integer, fraction string, or [p,q]")


def derived_coefficients() -> dict[tuple[int, int], Fraction]:
    # Outer translation x -> x-1, then Delta_1^3, then I-2T_h.
    base = {0: Fraction(1), 1: Fraction(-3), 2: Fraction(3), 3: Fraction(-1)}
    result: dict[tuple[int, int], Fraction] = {}
    for k, coefficient in base.items():
        result[(k + 1, 0)] = result.get((k + 1, 0), Fraction()) + coefficient
        result[(k + 1, 1)] = result.get((k + 1, 1), Fraction()) - 2 * coefficient
    return result


def moment_polynomial(
    coefficients: dict[tuple[int, int], Fraction], degree: int
) -> dict[int, Fraction]:
    # Shift is n + m*h. Return coefficients of h^r.
    result: dict[int, Fraction] = defaultdict(Fraction)
    for (n, m), coefficient in coefficients.items():
        for r in range(degree + 1):
            result[r] += (
                coefficient
                * comb(degree, r)
                * Fraction(n ** (degree - r))
                * Fraction(m**r)
            )
    return dict(result)


def canonical_json_sha256(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return sha256(encoded).hexdigest()


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")

    derived = derived_coefficients()
    raw_rows = payload.get("expected_coefficients")
    if not isinstance(raw_rows, list) or len(raw_rows) != len(derived):
        raise CertificateError("expected_coefficients has the wrong size")
    declared: dict[tuple[int, int], Fraction] = {}
    for index, row in enumerate(raw_rows):
        if not isinstance(row, dict):
            raise CertificateError(f"coefficient row {index} is not an object")
        key = (
            integer(row.get("integer_shift"), f"row[{index}].integer_shift"),
            integer(row.get("h_shift"), f"row[{index}].h_shift"),
        )
        if key in declared:
            raise CertificateError("duplicate formal shift")
        declared[key] = rational(row.get("coefficient"), f"row[{index}].coefficient")
    if declared != derived:
        raise CertificateError("declared finite-difference expansion is false")

    moments: dict[str, dict[str, str]] = {}
    for degree in range(4):
        polynomial = moment_polynomial(derived, degree)
        moments[str(degree)] = {str(k): str(v) for k, v in sorted(polynomial.items())}
        if degree <= 2 and any(polynomial.values()):
            raise CertificateError(f"degree-{degree} moment does not vanish")
    if moments["3"].get("0") != "6":
        raise CertificateError("third finite difference normalization changed")

    # At the exponential pole model exp(x/2), T_h has eigenvalue exp(-h/2)=1/2.
    pole_shift_eigenvalue = rational(
        payload.get("pole_shift_eigenvalue"), "pole_shift_eigenvalue"
    )
    if pole_shift_eigenvalue != Fraction(1, 2):
        raise CertificateError("h=log 4 pole eigenvalue must be 1/2")
    pole_factor = 1 - 2 * pole_shift_eigenvalue
    if pole_factor != 0:
        raise CertificateError("continuous pole model is not annihilated")

    phi_l2_sq = rational(payload.get("phi_l2_sq"), "phi_l2_sq")
    if phi_l2_sq != Fraction(2, 3):
        raise CertificateError("triangular L2 normalization mismatch")
    component_coefficients_raw = payload.get("component_coefficients")
    if not isinstance(component_coefficients_raw, list):
        raise CertificateError("component_coefficients must be a list")
    component_coefficients = [
        rational(value, f"component_coefficients[{index}]")
        for index, value in enumerate(component_coefficients_raw)
    ]
    if component_coefficients != [Fraction(1), Fraction(-2), Fraction(-1), Fraction(2)]:
        raise CertificateError("narrow safe-window components changed")
    coefficient_square_sum = sum(value * value for value in component_coefficients)
    if coefficient_square_sum != 10:
        raise CertificateError("component square sum must be 10")
    narrow_l2_prefactor = coefficient_square_sum * phi_l2_sq
    if narrow_l2_prefactor != Fraction(20, 3):
        raise CertificateError("narrow L2 prefactor must be 20/3")

    alpha = rational(payload.get("resolution_exponent"), "resolution_exponent")
    if alpha <= 0:
        raise CertificateError("resolution exponent must be positive")
    diagonal_hardy_exponent = alpha / 2
    declared_exponent = rational(
        payload.get("claimed_diagonal_hardy_exponent"),
        "claimed_diagonal_hardy_exponent",
    )
    if declared_exponent != diagonal_hardy_exponent:
        raise CertificateError("claimed diagonal exponent is false")

    proof = {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_ALGEBRA",
        "coefficients": [
            {
                "integer_shift": key[0],
                "h_shift": key[1],
                "coefficient": str(value),
            }
            for key, value in sorted(derived.items())
        ],
        "formal_moments": moments,
        "pole_model_factor": str(pole_factor),
        "narrow_l2_prefactor": str(narrow_l2_prefactor),
        "resolution_exponent": str(alpha),
        "diagonal_hardy_exponent": str(diagonal_hardy_exponent),
        "proof_boundary": (
            "Exact finite-difference and scaling algebra only. No prime, zeta, "
            "PNT, or semiprime estimate is evaluated by this checker."
        ),
    }
    proof["proof_object_sha256"] = canonical_json_sha256(proof)
    return proof


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(payload)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": SCHEMA, "classification": "REJECTED", "reason": str(exc)}
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
