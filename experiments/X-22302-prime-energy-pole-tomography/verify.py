#!/usr/bin/env python3
"""Exact rational checker for the local pole-tomography inequalities.

This checker validates only the finite algebra used in T-22302: a nonzero
principal part forces inverse-distance growth, and a pole on the integration
line forces divergent local energy.  It contains no zeta or prime data.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x22302-prime-energy-pole-tomography.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
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
            raise CertificateError(f"{name} has zero denominator")
        return Fraction(p, q)
    raise CertificateError(f"{name} must be an integer, string, or [p,q]")


def canonical_sha256(payload: dict[str, Any]) -> str:
    body = dict(payload)
    body.pop("proof_object_sha256", None)
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    if payload.get("classification") != "EXACT_SYNTHETIC_POLE_TOMOGRAPHY":
        raise CertificateError("classification mismatch")

    residue_sq = rational(payload.get("residue_modulus_sq"), "residue_modulus_sq")
    dominance = rational(payload.get("principal_part_dominance"), "principal_part_dominance")
    radius = rational(payload.get("local_radius"), "local_radius")
    if residue_sq <= 0:
        raise CertificateError("residue modulus must be positive")
    if not 0 < dominance <= 1:
        raise CertificateError("dominance must lie in (0,1]")
    if radius <= 0:
        raise CertificateError("local radius must be positive")

    offsets_raw = payload.get("horizontal_offsets")
    if not isinstance(offsets_raw, list) or len(offsets_raw) < 3:
        raise CertificateError("at least three offsets are required")
    offsets = [rational(value, f"horizontal_offsets[{i}]") for i, value in enumerate(offsets_raw)]
    if any(value <= 0 or value > radius for value in offsets):
        raise CertificateError("offsets must lie in (0,local_radius]")
    if any(offsets[i + 1] >= offsets[i] for i in range(len(offsets) - 1)):
        raise CertificateError("offsets must be strictly decreasing")

    # On |t-gamma| <= |a|, a^2+(t-gamma)^2 <= 2a^2.  If the
    # full meromorphic function has modulus at least dominance times the
    # principal-part modulus, the local energy is at least
    # dominance^2 * residue_sq / |a|.
    lower_bounds: list[Fraction] = []
    scaled: list[Fraction] = []
    for offset in offsets:
        lower = dominance * dominance * residue_sq / offset
        lower_bounds.append(lower)
        scaled.append(offset * lower)
    expected_scaled = dominance * dominance * residue_sq
    if any(value != expected_scaled for value in scaled):
        raise CertificateError("inverse-distance scaling reconstruction failed")

    # On the punctured annulus epsilon <= |t-gamma| <= 2 epsilon at the
    # pole line, |F|^2 >= dominance^2 residue_sq/(4 epsilon^2), and the
    # two-sided annulus has total length 2 epsilon.  Hence its energy is at
    # least dominance^2 residue_sq/(2 epsilon).
    eps_raw = payload.get("puncture_scales")
    if not isinstance(eps_raw, list) or len(eps_raw) < 3:
        raise CertificateError("at least three puncture scales are required")
    epsilons = [rational(value, f"puncture_scales[{i}]") for i, value in enumerate(eps_raw)]
    if any(value <= 0 or 2 * value > radius for value in epsilons):
        raise CertificateError("puncture scales exceed the local disk")
    if any(epsilons[i + 1] >= epsilons[i] for i in range(len(epsilons) - 1)):
        raise CertificateError("puncture scales must be strictly decreasing")
    annulus_lower = [dominance * dominance * residue_sq / (2 * eps) for eps in epsilons]
    if any(annulus_lower[i + 1] <= annulus_lower[i] for i in range(len(annulus_lower) - 1)):
        raise CertificateError("punctured-line lower bounds do not diverge")

    claimed = payload.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed result missing")
    if rational(claimed.get("scaled_inverse_distance_constant"), "claimed.scaled_inverse_distance_constant") != expected_scaled:
        raise CertificateError("claimed inverse-distance constant is false")
    if rational(claimed.get("last_annulus_lower"), "claimed.last_annulus_lower") != annulus_lower[-1]:
        raise CertificateError("claimed annulus lower bound is false")

    digest = canonical_sha256(payload)
    declared_digest = payload.get("proof_object_sha256")
    if declared_digest is not None and declared_digest != digest:
        raise CertificateError("proof-object digest mismatch")

    return {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_POLE_TOMOGRAPHY_VERIFIED",
        "offsets": [str(value) for value in offsets],
        "local_energy_lower_bounds": [str(value) for value in lower_bounds],
        "scaled_inverse_distance_constant": str(expected_scaled),
        "puncture_scales": [str(value) for value in epsilons],
        "punctured_line_energy_lower_bounds": [str(value) for value in annulus_lower],
        "proof_object_sha256": digest,
        "proof_boundary": (
            "Exact local meromorphic algebra only. No Riemann zero, prime sum, "
            "or unconditional compact-strip estimate is certified."
        ),
    }


def main() -> int:
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
