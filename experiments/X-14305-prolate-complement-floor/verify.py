#!/usr/bin/env python3
"""Exact scalar verifier for the L-14310 prolate complement floor."""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x14305-prolate-complement-floor.v1"
OUTPUT_SCHEMA = "riemann.x14305-prolate-complement-floor-verification.v1"
SYNTHETIC = "SYNTHETIC_MODEL"
PRODUCTION = "RIEMANN_WEIL_DIRECTED"
ANALYTIC_GATE = "CERTIFIED_SUZUKI_PERTURBATION_AND_CONSTANT_BOUNDS"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise CertificateError(f"{name} must be integer text") from exc
    raise CertificateError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if isinstance(raw, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(raw, int):
        return Fraction(raw)
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an integer or rational object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def validate_sha(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    classification = data.get("classification")
    if classification not in {SYNTHETIC, PRODUCTION}:
        raise CertificateError("unsupported classification")
    if classification == PRODUCTION:
        gate = data.get("analytic_gate")
        if not isinstance(gate, dict) or gate.get("status") != ANALYTIC_GATE:
            raise CertificateError("production certificate lacks its analytic gate")
        validate_sha(gate.get("sha256"), "analytic_gate.sha256")

    omega_upper = rational(data.get("omega_upper"), "omega_upper")
    log_omega_lower = rational(data.get("log_omega_lower"), "log_omega_lower")
    eta = rational(data.get("eta"), "eta")
    pi_lower = rational(data.get("pi_lower"), "pi_lower")
    c0_lower = rational(data.get("C0_lower"), "C0_lower")
    kappa_upper = rational(data.get("kappa_upper"), "kappa_upper")
    claimed_floor = rational(
        data.get("claimed_complement_floor"), "claimed_complement_floor"
    )
    rank_cap = exact_int(data.get("rank_cap"), "rank_cap")

    if omega_upper <= 1:
        raise CertificateError("omega_upper must exceed one")
    if log_omega_lower <= 0:
        raise CertificateError("log_omega_lower must be positive")
    if not Fraction(0) < eta < Fraction(1):
        raise CertificateError("eta must lie strictly between zero and one")
    if pi_lower <= 0:
        raise CertificateError("pi_lower must be positive")
    if kappa_upper < 0:
        raise CertificateError("kappa_upper must be nonnegative")
    if rank_cap < 0:
        raise CertificateError("rank_cap must be nonnegative")

    required_rank = ceil_fraction(2 * omega_upper / (pi_lower * eta))
    if rank_cap < required_rank:
        raise CertificateError("rank_cap is below the trace bound")

    floor_lower = (
        c0_lower
        - Fraction(2, 1) / pi_lower
        + (Fraction(1) - eta) * log_omega_lower
        - kappa_upper
    )
    if floor_lower < claimed_floor:
        raise CertificateError(
            "claimed complement floor exceeds the certified scalar bound"
        )

    proof_object = {
        "classification": classification,
        "omega_upper": fj(omega_upper),
        "log_omega_lower": fj(log_omega_lower),
        "eta": fj(eta),
        "pi_lower": fj(pi_lower),
        "C0_lower": fj(c0_lower),
        "kappa_upper": fj(kappa_upper),
        "claimed_complement_floor": fj(claimed_floor),
        "certified_formula_floor": fj(floor_lower),
        "required_rank_cap": required_rank,
        "declared_rank_cap": rank_cap,
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "analytic_claim": "L-14310",
        "omega_upper": fj(omega_upper),
        "log_omega_lower": fj(log_omega_lower),
        "eta": fj(eta),
        "pi_lower": fj(pi_lower),
        "C0_lower": fj(c0_lower),
        "kappa_upper": fj(kappa_upper),
        "required_rank_cap": required_rank,
        "declared_rank_cap": rank_cap,
        "certified_formula_floor": fj(floor_lower),
        "claimed_complement_floor": fj(claimed_floor),
        "floor_moat": fj(floor_lower - claimed_floor),
        "exact_proof_object_sha256": canonical_sha(proof_object),
        "verdict": "CERTIFIED_COMPLETE_PROLATE_COMPLEMENT_FLOOR",
        "proof_boundary": (
            "Exact rational evaluation of the L-14310 scalar and trace inequalities. "
            "Production use inherits the external normalization, perturbation-majorant, "
            "and prolate-packet containment gates."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(raw)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(
            json.dumps({"verified": False, "error": str(exc)}, indent=2),
            file=sys.stderr,
        )
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
