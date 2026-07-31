#!/usr/bin/env python3
"""Exact scalar verifier for the L-14320 separated-zero frame floor."""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x14313-separated-zero-frame.v1"
OUTPUT_SCHEMA = "riemann.x14313-separated-zero-frame-verification.v1"
SYNTHETIC = "SYNTHETIC_MODEL"
PRODUCTION = "RIEMANN_WEIL_DIRECTED"
GATE = "CERTIFIED_SEPARATED_ZERO_HARDY_KERNEL_BOUNDS"


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
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} must be rational text") from exc
    if not isinstance(value, dict) or set(value) != {"numerator", "denominator"}:
        raise CertificateError(f"{name} must be an exact rational")
    numerator = exact_int(value["numerator"], f"{name}.numerator")
    denominator = exact_int(value["denominator"], f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def valid_sha(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(ch not in string.hexdigits for ch in value)
    ):
        raise CertificateError(f"{name} must be a SHA-256 digest")
    return value.lower()


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
        if not isinstance(gate, dict) or gate.get("status") != GATE:
            raise CertificateError("production certificate lacks the analytic gate")
        valid_sha(gate.get("sha256"), "analytic_gate.sha256")

    d_lower = rational(data.get("diagonal_lower"), "diagonal_lower")
    r_upper = rational(data.get("relative_row_sum_upper"), "relative_row_sum_upper")
    epsilon = rational(data.get("entry_tail_upper"), "entry_tail_upper")
    claimed = rational(data.get("claimed_frame_floor"), "claimed_frame_floor")
    m = exact_int(data.get("zero_count"), "zero_count")

    if d_lower <= 0:
        raise CertificateError("diagonal_lower must be positive")
    if r_upper < 0 or r_upper >= 1:
        raise CertificateError("relative_row_sum_upper must lie in [0,1)")
    if epsilon < 0:
        raise CertificateError("entry_tail_upper must be nonnegative")
    if m <= 0:
        raise CertificateError("zero_count must be positive")

    formula = d_lower * (1 - r_upper) - m * epsilon
    if formula <= 0:
        raise CertificateError("the directed frame floor is not positive")
    if claimed > formula:
        raise CertificateError("claimed frame floor exceeds the directed formula")

    proof = {
        "classification": classification,
        "diagonal_lower": fj(d_lower),
        "relative_row_sum_upper": fj(r_upper),
        "entry_tail_upper": fj(epsilon),
        "zero_count": m,
        "formula_frame_floor": fj(formula),
        "claimed_frame_floor": fj(claimed),
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "analytic_claim": "L-14320",
        "zero_count": m,
        "diagonal_lower": fj(d_lower),
        "relative_row_sum_upper": fj(r_upper),
        "entry_tail_upper": fj(epsilon),
        "formula_frame_floor": fj(formula),
        "claimed_frame_floor": fj(claimed),
        "floor_moat": fj(formula - claimed),
        "exact_proof_object_sha256": canonical_sha(proof),
        "verdict": "CERTIFIED_SEPARATED_ZERO_FRAME_FLOOR",
        "proof_boundary": (
            "Exact rational scalar composition. Production use inherits the "
            "certified-zero separation, reciprocal-Hardy normalization, and "
            "directed analytic-bound gate."
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
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
