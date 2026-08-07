#!/usr/bin/env python3
"""Exact synthetic verifier for the RBC(K) certificate schema.

This verifies only abstract rational arithmetic and incidence bookkeeping. It
contains no zeta, prime, or Möbius computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


class VerificationError(ValueError):
    pass


def require_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerificationError(f"{name} must be an integer")
    return value


def frac(obj: Any, name: str) -> Fraction:
    if not isinstance(obj, dict) or set(obj) != {"num", "den"}:
        raise VerificationError(f"{name} must be {{num,den}}")
    n = require_int(obj["num"], f"{name}.num")
    d = require_int(obj["den"], f"{name}.den")
    if d <= 0:
        raise VerificationError(f"{name}.den must be positive")
    return Fraction(n, d)


def canonical_digest(payload: dict[str, Any]) -> str:
    body = dict(payload)
    body.pop("claimed_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("schema") != "X-24901-RBC-SYNTHETIC-v1":
        raise VerificationError("wrong schema")

    K = require_int(payload.get("K"), "K")
    if K < 4:
        raise VerificationError("K must be at least 4")

    R = require_int(payload.get("euler_order"), "euler_order")
    if R < K**3:
        raise VerificationError("Euler order must be at least K^3")

    delta = frac(payload.get("delta"), "delta")
    if not (Fraction(0) < delta < Fraction(1)):
        raise VerificationError("delta must lie in (0,1)")

    lower_scale = frac(payload.get("lower_scale"), "lower_scale")
    if lower_scale > 1 - delta:
        raise VerificationError("declared lower scale violates reserve")

    theta = frac(payload.get("returned_target_fraction"), "returned_target_fraction")
    if not (Fraction(0) <= theta < Fraction(1)):
        raise VerificationError("strict reflected reserve requires theta<1")
    reserve = 1 - theta

    self_routes = require_int(payload.get("same_scale_target_routes"), "same_scale_target_routes")
    if self_routes != 0:
        raise VerificationError("same-scale target is hidden on reserve RHS")

    q = require_int(payload.get("max_simultaneous_paid_coordinates"), "max_simultaneous_paid_coordinates")
    if q < 0:
        raise VerificationError("negative charge count")
    rate = Fraction(q, K)

    depth_rows = []
    for j in range(1, K - 1):
        ell = K - j - 1
        eta = Fraction(ell, K * K)
        exponent = Fraction(1, 2) - R * eta
        if exponent >= 0:
            raise VerificationError(f"non-top row j={j} is not Euler-small")
        depth_rows.append({
            "j": j,
            "ell": ell,
            "eta": f"{eta.numerator}/{eta.denominator}",
            "amplitude_exponent": f"{exponent.numerator}/{exponent.denominator}",
        })

    if payload.get("top_row_euler_closed") is not False:
        raise VerificationError("top row must remain open")

    faces = payload.get("faces")
    if not isinstance(faces, list) or not faces:
        raise VerificationError("faces must be a nonempty list")
    incidence: dict[str, int] = {}
    physical = set(payload.get("physical_faces", []))
    if not all(isinstance(x, str) for x in physical):
        raise VerificationError("physical face IDs must be strings")

    for idx, row in enumerate(faces):
        if not isinstance(row, dict):
            raise VerificationError(f"faces[{idx}] must be an object")
        face_id = row.get("face")
        if not isinstance(face_id, str):
            raise VerificationError(f"faces[{idx}].face must be a string")
        sign = require_int(row.get("sign"), f"faces[{idx}].sign")
        if sign not in (-1, 1):
            raise VerificationError("face signs must be +/-1")
        incidence[face_id] = incidence.get(face_id, 0) + sign

    uncancelled_internal = {
        face_id: total
        for face_id, total in incidence.items()
        if face_id not in physical and total != 0
    }
    if uncancelled_internal:
        raise VerificationError(f"uncancelled internal faces: {uncancelled_internal}")

    missing_physical = physical.difference(incidence)
    if missing_physical:
        raise VerificationError(f"declared physical faces absent: {sorted(missing_physical)}")

    digest = canonical_digest(payload)
    claimed = payload.get("claimed_sha256")
    if claimed is not None and claimed != digest:
        raise VerificationError("claimed SHA-256 mismatch")

    return {
        "classification": "EXACT_SYNTHETIC_RBC_SCHEMA_REGRESSION",
        "K": K,
        "euler_order": R,
        "reserve": f"{reserve.numerator}/{reserve.denominator}",
        "delta": f"{delta.numerator}/{delta.denominator}",
        "lower_scale": f"{lower_scale.numerator}/{lower_scale.denominator}",
        "charge_rate": f"{rate.numerator}/{rate.denominator}",
        "non_top_rows": depth_rows,
        "physical_face_count": len(physical),
        "internal_face_count": len(incidence) - len(physical),
        "proof_object_sha256": digest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.certificate.read_text())
    result = verify(payload)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
