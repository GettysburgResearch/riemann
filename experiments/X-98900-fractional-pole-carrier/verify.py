#!/usr/bin/env python3
"""Exact finite verifier for the T98900 pole-rate and phase-port firewalls."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x98900.fractional-pole-phase.v1"
OUT = "riemann.x98900.fractional-pole-phase.result.v1"


class VerificationError(ValueError):
    pass


def frac(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise VerificationError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise VerificationError(f"{name} is not rational text") from exc
    raise VerificationError(f"{name} must be an integer or rational string")


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise VerificationError("unsupported schema")
    theta = frac(data.get("theta"), "theta")
    if not 0 < theta < Fraction(1, 192):
        raise VerificationError("theta must lie in (0,1/192)")

    local_factor = frac(data.get("local_dyadic_factor_at_one"), "local_dyadic_factor_at_one")
    if local_factor != Fraction(3, 8):
        raise VerificationError("the local factor at s=1 must be 3/8")

    actual_rate = Fraction(1, 2)
    claimed_rate = 96 * theta
    if not actual_rate > claimed_rate:
        raise VerificationError("pole rate does not contradict the claimed rate")

    P = data.get("phase_fixture", {})
    if P.get("prime") != 3 or P.get("endpoint") != 3 or P.get("phase") != "pi/log(3)":
        raise VerificationError("wrong phase fixture")

    C = Fraction(2 + 2, 3) - Fraction(4, 3) / 3
    A_zero = Fraction(1) - Fraction(1, 3)
    A_phase = Fraction(1) + Fraction(1, 3)
    det_zero = C * C - A_zero * A_zero
    det_phase = C * C - A_phase * A_phase

    if C != Fraction(8, 9):
        raise VerificationError("Tao diagonal reconstruction failed")
    if det_zero < 0:
        raise VerificationError("unphased port should be PSD")
    if det_phase >= 0:
        raise VerificationError("phased separator disappeared")

    expected = data.get("expected", {})
    actual = {
        "actual_energy_exponent": fstr(actual_rate),
        "claimed_energy_exponent": fstr(claimed_rate),
        "rate_gap": fstr(actual_rate - claimed_rate),
        "tao_diagonal": fstr(C),
        "unphased_offdiagonal": fstr(A_zero),
        "phased_offdiagonal": fstr(A_phase),
        "unphased_determinant": fstr(det_zero),
        "phased_determinant": fstr(det_phase),
    }
    if expected != actual:
        raise VerificationError(f"expected values mismatch: {expected!r} != {actual!r}")

    proof = {
        "schema": OUT,
        "theta": fstr(theta),
        "local_dyadic_factor_at_one": fstr(local_factor),
        **actual,
        "verdict": "PASS_X98900_FRACTIONAL_POLE_AND_PHASE_FIREWALLS",
        "proof_boundary": (
            "Exact rate comparison and exact one-prime phase separator. "
            "The analytic Hankel asymptotic is proved in L-98900, not by this finite checker."
        ),
    }
    proof["proof_object_sha256"] = canonical_sha(proof)
    return proof


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path, nargs="?", default=Path(__file__).parent / "certificates" / "control.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise VerificationError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, VerificationError) as exc:
        parser.error(str(exc))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
