#!/usr/bin/env python3
"""Exact arithmetic checker for the L-8505 fast coefficient operator budget."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "riemann.fast-toeplitz-operator-budget.v1"
VERIFY_SCHEMA = "riemann.fast-toeplitz-operator-budget.verification.v1"
ARITHMETIC_CONTRACT = (
    "x86 binary80 nearest basic arithmetic; binary128 segment-relative phase; "
    "MPFR setup; M=32768 R=3; two-hat coefficient deposits; balanced pairwise "
    "summation; zero guarded support-boundary events"
)


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not an integer") from exc
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


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    if data.get("arithmetic_contract") != ARITHMETIC_CONTRACT:
        raise CertificateError("arithmetic contract mismatch")
    if data.get("status") != "STATIC_CONDITIONAL_BUDGET_NOT_A_PRODUCTION_RUN":
        raise CertificateError("status must preserve the conditional proof boundary")
    if data.get("claims_complete_coefficient_run") is not False:
        raise CertificateError("static budget must not claim a completed coefficient run")

    term_count = parse_int(data.get("term_count_upper"), "term_count_upper")
    hardware_units = parse_int(data.get("hardware_units_per_term"), "hardware_units_per_term")
    mantissa_bits = parse_int(data.get("binary80_mantissa_bits"), "binary80_mantissa_bits")
    pairwise_depth = parse_int(data.get("pairwise_depth"), "pairwise_depth")
    amplitude_sum = parse_int(data.get("amplitude_sum_upper"), "amplitude_sum_upper")
    guarded_boundaries = parse_int(
        data.get("guarded_support_boundary_count"),
        "guarded_support_boundary_count",
    )
    phase_location = parse_fraction(data.get("phase_location_budget"), "phase_location_budget")
    phase_taylor = parse_fraction(data.get("phase_taylor_budget"), "phase_taylor_budget")
    algebraic = parse_fraction(data.get("algebraic_budget"), "algebraic_budget")
    threshold = parse_fraction(data.get("required_upper"), "required_upper")

    if term_count <= 0 or hardware_units <= 0 or mantissa_bits < 2:
        raise CertificateError("invalid hardware budget parameters")
    if not (0 < pairwise_depth < (1 << mantissa_bits)):
        raise CertificateError("invalid pairwise depth")
    if amplitude_sum <= 0:
        raise CertificateError("amplitude sum must be positive")
    if guarded_boundaries != 0:
        raise CertificateError("guarded support-boundary events require directed fallback")
    if min(phase_location, phase_taylor, algebraic, threshold) <= 0:
        raise CertificateError("all rational budgets and threshold must be positive")

    unit_roundoff = Fraction(1, 1 << mantissa_bits)
    hardware = term_count * hardware_units * unit_roundoff
    gamma = pairwise_depth * unit_roundoff / (1 - pairwise_depth * unit_roundoff)
    pairwise = gamma * amplitude_sum
    total = hardware + pairwise + phase_location + phase_taylor + algebraic
    if not total < threshold:
        raise CertificateError("complete fast operator budget does not clear required upper")

    claimed = data.get("claimed_total")
    if claimed is not None and parse_fraction(claimed, "claimed_total") != total:
        raise CertificateError("claimed_total mismatch")

    result: dict[str, Any] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": "STATIC_OPERATOR_BUDGET_VERIFIED",
        "components": {
            "hardware_term_sum": fraction_json(hardware),
            "pairwise_sum": fraction_json(pairwise),
            "phase_location": fraction_json(phase_location),
            "phase_taylor": fraction_json(phase_taylor),
            "algebraic": fraction_json(algebraic),
            "total": fraction_json(total),
            "required_upper": fraction_json(threshold),
        },
        "parameters": {
            "term_count_upper": term_count,
            "hardware_units_per_term": hardware_units,
            "binary80_mantissa_bits": mantissa_bits,
            "pairwise_depth": pairwise_depth,
            "amplitude_sum_upper": amplitude_sum,
            "guarded_support_boundary_count": guarded_boundaries,
        },
        "proof_boundary": (
            "This checks the static L-8505 rational operator budget under the exact "
            "declared arithmetic contract.  It does not assert that the coefficient "
            "producer has run or that its source follows the reviewed operation order."
        ),
    }
    result["verification_sha256"] = canonical_sha(result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {
            "schema": VERIFY_SCHEMA,
            "verified": False,
            "status": "REJECTED",
            "reason": str(exc),
        }
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
