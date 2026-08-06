#!/usr/bin/env python3
"""Exact checker for the synthetic r-adic screw-renormalization identities."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x20202-r-adic-screw.synthetic.v1"


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


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA}")
    r = integer(data.get("r"), "r")
    if r < 2:
        raise CertificateError("r must be at least two")

    raw_ys = data.get("lerch_y")
    if not isinstance(raw_ys, list) or not raw_ys:
        raise CertificateError("lerch_y must be a nonempty array")
    lerch_rows: list[dict[str, object]] = []
    for index, raw in enumerate(raw_ys):
        y = fraction(raw, f"lerch_y[{index}]")
        if not 0 < y < 1:
            raise CertificateError("every Lerch y must lie strictly between zero and one")
        numerator = r * r * (1 - y) - (1 - y**r)
        lower = r * (r - 1) * (1 - y)
        if numerator < lower or lower <= 0:
            raise CertificateError("Lerch positivity inequality failed")
        lerch_rows.append(
            {
                "y": fraction_json(y),
                "numerator": fraction_json(numerator),
                "lower_bound": fraction_json(lower),
            }
        )

    raw_exponents = data.get("prime_exponents")
    if not isinstance(raw_exponents, list) or not raw_exponents:
        raise CertificateError("prime_exponents must be a nonempty array")
    threshold = Fraction(2, r + 1)
    exponent_rows: list[dict[str, object]] = []
    for index, raw in enumerate(raw_exponents):
        if not isinstance(raw, dict):
            raise CertificateError(f"prime_exponents[{index}] must be an object")
        u = fraction(raw.get("u"), f"prime_exponents[{index}].u")
        declared = raw.get("sign")
        if declared not in ("negative", "zero", "positive"):
            raise CertificateError("prime exponent sign must be negative, zero, or positive")
        value = (r * r - 1) * u - 2 * (r - 1)
        actual = "negative" if value < 0 else "positive" if value > 0 else "zero"
        if actual != declared:
            raise CertificateError("prime exponent sign declaration mismatch")
        exponent_rows.append(
            {
                "u": fraction_json(u),
                "weight_log_n": fraction_json(value),
                "sign": actual,
            }
        )

    mixture = data.get("mixture")
    if not isinstance(mixture, dict):
        raise CertificateError("mixture must be an object")
    raw_dilations = mixture.get("dilations")
    raw_coefficients = mixture.get("coefficients")
    raw_descendants = mixture.get("descendant_multiplicities")
    if not all(isinstance(value, list) for value in (raw_dilations, raw_coefficients, raw_descendants)):
        raise CertificateError("mixture arrays missing")
    if not (len(raw_dilations) == len(raw_coefficients) == len(raw_descendants) > 0):
        raise CertificateError("mixture arrays have incompatible lengths")
    dilations = [integer(value, f"mixture.dilations[{i}]") for i, value in enumerate(raw_dilations)]
    coefficients = [fraction(value, f"mixture.coefficients[{i}]") for i, value in enumerate(raw_coefficients)]
    descendants = [integer(value, f"mixture.descendant_multiplicities[{i}]") for i, value in enumerate(raw_descendants)]
    parent = integer(mixture.get("parent_multiplicity"), "mixture.parent_multiplicity")
    if parent <= 0 or any(value < 2 for value in dilations):
        raise CertificateError("invalid parent or dilation")
    if any(value <= 0 for value in coefficients) or any(value < 0 for value in descendants):
        raise CertificateError("mixture coefficients must be positive and multiplicities nonnegative")
    total_weight = sum(coefficient * dilation * dilation for coefficient, dilation in zip(coefficients, dilations))
    descendant_weight = sum(
        coefficient * dilation * dilation * multiplicity
        for coefficient, dilation, multiplicity in zip(coefficients, dilations, descendants)
    )
    if descendant_weight != total_weight * parent:
        raise CertificateError("mixture residue balance failed")
    if max(descendants) < parent:
        raise CertificateError("weighted-average descendant conclusion failed")

    cocycle = data.get("cocycle")
    if not isinstance(cocycle, dict):
        raise CertificateError("cocycle must be an object")
    cocycle_r = integer(cocycle.get("r"), "cocycle.r")
    cocycle_s = integer(cocycle.get("s"), "cocycle.s")
    if cocycle_r < 2 or cocycle_s < 2:
        raise CertificateError("cocycle dilations must be at least two")
    psi_t = fraction(cocycle.get("psi_t"), "cocycle.psi_t")
    psi_st = fraction(cocycle.get("psi_st"), "cocycle.psi_st")
    psi_rst = fraction(cocycle.get("psi_rst"), "cocycle.psi_rst")
    direct = (cocycle_r * cocycle_s) ** 2 * psi_t - psi_rst
    decomposed = (
        cocycle_r * cocycle_r * (cocycle_s * cocycle_s * psi_t - psi_st)
        + cocycle_r * cocycle_r * psi_st
        - psi_rst
    )
    if direct != decomposed:
        raise CertificateError("dilation cocycle failed")
    expected = fraction(cocycle.get("expected_value"), "cocycle.expected_value")
    if direct != expected:
        raise CertificateError("declared cocycle value mismatch")

    result: dict[str, Any] = {
        "schema": "riemann.x20202-r-adic-screw.verification.v1",
        "verified": True,
        "r": r,
        "negative_prefix_exponent": fraction_json(threshold),
        "lerch_rows": lerch_rows,
        "prime_exponent_rows": exponent_rows,
        "mixture_weight": fraction_json(total_weight),
        "mixture_parent_multiplicity": parent,
        "mixture_max_descendant_multiplicity": max(descendants),
        "cocycle_value": fraction_json(direct),
        "verdict": "EXACT_R_ADIC_RENORMALIZATION_ALGEBRA_VERIFIED",
        "proof_boundary": (
            "Synthetic exact algebra only; no zeta, xi, prime-stream, Landau, "
            "or RH sign is certified."
        ),
    }
    result["proof_object_sha256"] = canonical_digest(result)
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