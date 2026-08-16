#!/usr/bin/env python3
"""Exact checker for the synthetic curvature-corrected prime-transport identity."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x20203-curvature-transport.synthetic.v1"


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


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA}")
    raw_barrier = data.get("quadratic_barrier")
    if not isinstance(raw_barrier, dict):
        raise CertificateError("quadratic_barrier must be an object")
    c2 = fraction(raw_barrier.get("c2"), "quadratic_barrier.c2")
    c1 = fraction(raw_barrier.get("c1"), "quadratic_barrier.c1")
    c0 = fraction(raw_barrier.get("c0"), "quadratic_barrier.c0")
    if c2 <= 0:
        raise CertificateError("the quadratic barrier must be strictly convex")

    def h(x: Fraction) -> Fraction:
        return c2 * x * x / 2 + c1 * x + c0

    def hp(x: Fraction) -> Fraction:
        return c2 * x + c1

    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be a nonempty array")
    seen: set[str] = set()
    rows: list[dict[str, object]] = []
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise CertificateError("row IDs must be unique and nonempty")
        seen.add(identifier)
        A = fraction(raw.get("A"), f"rows[{index}].A")
        tau = fraction(raw.get("tau"), f"rows[{index}].tau")
        T = fraction(raw.get("T"), f"rows[{index}].T")
        B = fraction(raw.get("B"), f"rows[{index}].B")
        if hp(tau) != A:
            raise CertificateError(f"{identifier}: A is not H'(tau)")
        h_star = A * tau - h(tau)
        reserve = h_star - B
        bregman = h(T) - h(tau) - A * (T - tau)
        if bregman < 0:
            raise CertificateError(f"{identifier}: negative Bregman divergence")
        direct = A * T - B - h(T)
        if direct != reserve - bregman:
            raise CertificateError(f"{identifier}: primal/dual identity failed")
        epsilon = A - hp(T)
        square_bound = epsilon * epsilon / (2 * c2)
        if bregman != square_bound:
            raise CertificateError(
                f"{identifier}: quadratic strong-convexity bound should be exact"
            )
        status = (
            "CERTIFIED_POSITIVE"
            if direct > 0
            else "CERTIFIED_NEGATIVE"
            if direct < 0
            else "CERTIFIED_ZERO"
        )
        if raw.get("expected_status") != status:
            raise CertificateError(f"{identifier}: expected status mismatch")
        rows.append(
            {
                "id": identifier,
                "reserve": fj(reserve),
                "bregman_penalty": fj(bregman),
                "centered_mass_error": fj(epsilon),
                "square_penalty": fj(square_bound),
                "direct_margin": fj(direct),
                "status": status,
            }
        )

    raw_blocks = data.get("transport_blocks")
    if not isinstance(raw_blocks, list) or not raw_blocks:
        raise CertificateError("transport_blocks must be a nonempty array")
    blocks: list[dict[str, object]] = []
    for index, raw in enumerate(raw_blocks):
        if not isinstance(raw, dict):
            raise CertificateError(f"transport_blocks[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier:
            raise CertificateError("transport block ID must be nonempty")
        left = fraction(raw.get("A_left"), f"transport_blocks[{index}].A_left")
        right = fraction(raw.get("A_right"), f"transport_blocks[{index}].A_right")
        atom = fraction(
            raw.get("atom_location"), f"transport_blocks[{index}].atom_location"
        )
        b_increment = fraction(
            raw.get("B_increment"), f"transport_blocks[{index}].B_increment"
        )
        if not left < right:
            raise CertificateError("transport mass interval must be increasing")
        mass = right - left
        if b_increment != mass * atom:
            raise CertificateError("B increment does not match atom mass/location")

        def hstar(A: Fraction) -> Fraction:
            return (A - c1) * (A - c1) / (2 * c2) - c0

        reserve_increment = hstar(right) - hstar(left) - b_increment
        transport_integral = (
            ((right - c1) ** 2 - (left - c1) ** 2) / (2 * c2)
            - atom * mass
        )
        if reserve_increment != transport_integral:
            raise CertificateError("transport recurrence failed")
        blocks.append(
            {
                "id": identifier,
                "mass": fj(mass),
                "reserve_increment": fj(reserve_increment),
                "transport_integral": fj(transport_integral),
            }
        )

    result: dict[str, Any] = {
        "schema": "riemann.x20203-curvature-transport.verification.v1",
        "verified": True,
        "barrier_curvature": fj(c2),
        "rows": rows,
        "transport_blocks": blocks,
        "verdict": "EXACT_CURVATURE_CORRECTED_TRANSPORT_ALGEBRA_VERIFIED",
        "proof_boundary": (
            "Synthetic exact quadratic-barrier algebra only; no prime stream, "
            "Selberg estimate, cofinal transport bound, or RH claim is certified."
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
