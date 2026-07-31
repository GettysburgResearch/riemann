#!/usr/bin/env python3
"""Exact scalar verifier for the L-14311 multiband symbol floor."""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x14306-multiband-symbol-floor.v1"
OUTPUT_SCHEMA = "riemann.x14306-multiband-symbol-floor-verification.v1"
SYNTHETIC = "SYNTHETIC_MODEL"
PRODUCTION = "RIEMANN_WEIL_DIRECTED"
GATE = "CERTIFIED_COMPLETE_SYMBOL_SUBLEVEL_COVER"


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


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an integer or rational object")
    numerator = exact_int(value.get("numerator"), f"{name}.numerator")
    denominator = exact_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def valid_sha(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in string.hexdigits for character in value)
    ):
        raise CertificateError(f"{name} must be a SHA-256 digest")
    return value.lower()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    classification = data.get("classification")
    if classification not in {SYNTHETIC, PRODUCTION}:
        raise CertificateError("unsupported classification")
    if classification == PRODUCTION:
        gate = data.get("symbol_cover_gate")
        if not isinstance(gate, dict) or gate.get("status") != GATE:
            raise CertificateError(
                "production certificate lacks the symbol-cover gate"
            )
        valid_sha(gate.get("sha256"), "symbol_cover_gate.sha256")

    measure = rational(data.get("bad_measure_upper"), "bad_measure_upper")
    eta = rational(data.get("eta"), "eta")
    pi_lower = rational(data.get("pi_lower"), "pi_lower")
    global_lower = rational(
        data.get("global_symbol_lower"), "global_symbol_lower"
    )
    good_lower = rational(data.get("good_symbol_lower"), "good_symbol_lower")
    claimed_floor = rational(
        data.get("claimed_complement_floor"), "claimed_complement_floor"
    )
    rank_cap = exact_int(data.get("rank_cap"), "rank_cap")

    if measure < 0:
        raise CertificateError("bad_measure_upper must be nonnegative")
    if not Fraction(0) < eta < Fraction(1):
        raise CertificateError("eta must lie strictly between zero and one")
    if pi_lower <= 0:
        raise CertificateError("pi_lower must be positive")
    if global_lower > good_lower:
        raise CertificateError(
            "global_symbol_lower must not exceed good_symbol_lower"
        )
    if rank_cap < 0:
        raise CertificateError("rank_cap must be nonnegative")

    required_rank = ceil_fraction(measure / (pi_lower * eta))
    if rank_cap < required_rank:
        raise CertificateError("rank_cap is below the multiband trace bound")

    formula_floor = (
        -Fraction(2, 1) / pi_lower
        + (Fraction(1) - eta) * good_lower
        + eta * global_lower
    )
    if formula_floor < claimed_floor:
        raise CertificateError(
            "claimed floor exceeds the certified multiband floor"
        )

    proof_object = {
        "classification": classification,
        "bad_measure_upper": fj(measure),
        "eta": fj(eta),
        "pi_lower": fj(pi_lower),
        "global_symbol_lower": fj(global_lower),
        "good_symbol_lower": fj(good_lower),
        "claimed_complement_floor": fj(claimed_floor),
        "certified_formula_floor": fj(formula_floor),
        "required_rank_cap": required_rank,
        "declared_rank_cap": rank_cap,
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "analytic_claim": "L-14311",
        "bad_measure_upper": fj(measure),
        "eta": fj(eta),
        "pi_lower": fj(pi_lower),
        "global_symbol_lower": fj(global_lower),
        "good_symbol_lower": fj(good_lower),
        "required_rank_cap": required_rank,
        "declared_rank_cap": rank_cap,
        "certified_formula_floor": fj(formula_floor),
        "claimed_complement_floor": fj(claimed_floor),
        "floor_moat": fj(formula_floor - claimed_floor),
        "exact_proof_object_sha256": canonical_sha(proof_object),
        "verdict": "CERTIFIED_MULTIBAND_GENERALIZED_PROLATE_COMPLEMENT_FLOOR",
        "proof_boundary": (
            "Exact rational trace and floor arithmetic. Production use inherits "
            "the complete directed symbol-sublevel cover, infinite-frequency tail, "
            "normalization, and packet-containment gates."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        output = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(
            json.dumps({"verified": False, "error": str(exc)}, indent=2),
            file=sys.stderr,
        )
        return 2
    text = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
