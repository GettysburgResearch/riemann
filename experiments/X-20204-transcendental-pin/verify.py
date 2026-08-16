#!/usr/bin/env python3
"""Exact symbolic checker for the transcendental-pin algebra of T-20206."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x20204-transcendental-pin.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} must be a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def ramp(lambdas: list[Fraction], s: Fraction) -> Fraction:
    return sum(
        value * max(Fraction(0), Fraction(k) - s)
        for k, value in enumerate(lambdas, start=1)
    )


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA}")
    degree = integer(data.get("degree"), "degree")
    if degree < 2:
        raise CertificateError("degree must be at least two")
    raw_lambda = data.get("base_lambda")
    if not isinstance(raw_lambda, list) or len(raw_lambda) != degree:
        raise CertificateError("base_lambda has wrong length")
    base_lambda = [
        fraction(value, f"base_lambda[{i}]") for i, value in enumerate(raw_lambda)
    ]

    pin = data.get("pin")
    if not isinstance(pin, dict):
        raise CertificateError("pin must be an object")
    if pin.get("tap") != 1:
        raise CertificateError("the transcendental pin must be attached only to tap one")
    if pin.get("symbol") != f"exp(-{degree})":
        raise CertificateError("pin symbol/degree mismatch")
    if pin.get("classification") != "POSITIVE_TRANSCENDENTAL_OVER_ALGEBARIC_BASE":
        raise CertificateError("pin transcendence gate missing")

    residue = data.get("residue")
    if not isinstance(residue, dict):
        raise CertificateError("residue must be an object")
    parent = integer(residue.get("parent_multiplicity"), "parent_multiplicity")
    raw_descendants = residue.get("descendant_multiplicities")
    if parent <= 0 or not isinstance(raw_descendants, list) or len(raw_descendants) != degree - 1:
        raise CertificateError("invalid residue multiplicities")
    descendants = [
        integer(value, f"descendant_multiplicities[{i}]")
        for i, value in enumerate(raw_descendants)
    ]
    if any(value < 0 for value in descendants):
        raise CertificateError("multiplicities must be nonnegative")

    algebraic_part = base_lambda[0] * parent
    for k, (coefficient, multiplicity) in enumerate(
        zip(base_lambda[1:], descendants), start=2
    ):
        algebraic_part += k * k * coefficient * multiplicity
    transcendental_coefficient = parent
    if transcendental_coefficient <= 0:
        raise CertificateError("pin residue coefficient must be nonzero")

    expected_algebraic = fraction(
        residue.get("expected_algebraic_part"), "expected_algebraic_part"
    )
    if algebraic_part != expected_algebraic:
        raise CertificateError("algebraic residue part mismatch")

    ramp_check = data.get("ramp")
    if not isinstance(ramp_check, dict):
        raise CertificateError("ramp block missing")
    s = fraction(ramp_check.get("s"), "ramp.s")
    expected_base = fraction(ramp_check.get("base_value"), "ramp.base_value")
    expected_pin_coefficient = fraction(
        ramp_check.get("pin_coefficient"), "ramp.pin_coefficient"
    )
    base_value = ramp(base_lambda, s)
    pin_coefficient = max(Fraction(0), Fraction(1) - s)
    if base_value != expected_base or pin_coefficient != expected_pin_coefficient:
        raise CertificateError("pinned ramp declaration mismatch")

    support = data.get("critical_support")
    if not isinstance(support, dict):
        raise CertificateError("critical_support missing")
    full_exponent = fraction(support.get("full_exponent"), "full_exponent")
    pin_exponent = fraction(support.get("pin_exponent"), "pin_exponent")
    if full_exponent != 2 or pin_exponent != Fraction(2, degree):
        raise CertificateError("critical support exponent mismatch")

    result: dict[str, Any] = {
        "schema": "riemann.x20204-transcendental-pin.verification.v1",
        "verified": True,
        "degree": degree,
        "pin_symbol": pin["symbol"],
        "residue_formal_pair": {
            "algebraic_part": fj(algebraic_part),
            "transcendental_coefficient": str(transcendental_coefficient),
        },
        "residue_cannot_vanish": True,
        "ramp_at_s": {
            "s": fj(s),
            "base_value": fj(base_value),
            "pin_coefficient": fj(pin_coefficient),
        },
        "critical_full_prime_exponent": fj(full_exponent),
        "critical_pin_prime_exponent": fj(pin_exponent),
        "verdict": "EXACT_TRANSCENDENTAL_PIN_ALGEBRA_VERIFIED",
        "proof_boundary": (
            "The checker treats the pin as a typed transcendental symbol. "
            "Lindemann--Weierstrass and the Landau/pole theorem remain analytic dependencies; "
            "no zeta sign is certified."
        ),
    }
    result["proof_object_sha256"] = digest(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
