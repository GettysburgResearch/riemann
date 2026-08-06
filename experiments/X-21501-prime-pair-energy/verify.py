#!/usr/bin/env python3
"""Exact rational checker for the finite prime-pair Gram identity of L-21502.

This checker is a synthetic algebra consumer. Production locations such as
``log n`` require a directed transcendental producer and immutable prime-power
manifest; they are not manufactured by this script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x21501-prime-pair-energy.v1"
OUTPUT_SCHEMA = "riemann.x21501-prime-pair-energy.verification.v1"


class CertificateError(ValueError):
    pass


def q(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name}: Boolean is not rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name}: invalid rational") from exc
    if isinstance(value, list) and len(value) == 2:
        p = q(value[0], f"{name}[0]")
        r = q(value[1], f"{name}[1]")
        if p.denominator != 1 or r.denominator != 1 or r == 0:
            raise CertificateError(f"{name}: [p,q] needs integer p and nonzero q")
        return Fraction(p.numerator, r.numerator)
    raise CertificateError(f"{name}: rational required")


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def parse_segments(payload: dict[str, Any]) -> list[tuple[Fraction, Fraction, Fraction]]:
    raw = payload.get("window_segments")
    if not isinstance(raw, list) or not raw:
        raise CertificateError("window_segments must be nonempty")
    result: list[tuple[Fraction, Fraction, Fraction]] = []
    previous: Fraction | None = None
    for index, row in enumerate(raw):
        if not isinstance(row, dict):
            raise CertificateError(f"window_segments[{index}] must be an object")
        lower = q(row.get("lower"), f"segments[{index}].lower")
        upper = q(row.get("upper"), f"segments[{index}].upper")
        value = q(row.get("value"), f"segments[{index}].value")
        if lower >= upper:
            raise CertificateError("segment endpoints must increase")
        if previous is not None and lower < previous:
            raise CertificateError("segments overlap or are unordered")
        previous = upper
        if value != 0:
            result.append((lower, upper, value))
    if not result:
        raise CertificateError("window is identically zero")
    return result


def parse_atoms(payload: dict[str, Any]) -> list[tuple[Fraction, Fraction]]:
    raw = payload.get("atoms")
    if not isinstance(raw, list) or not raw:
        raise CertificateError("atoms must be nonempty")
    result: list[tuple[Fraction, Fraction]] = []
    for index, row in enumerate(raw):
        if not isinstance(row, dict):
            raise CertificateError(f"atoms[{index}] must be an object")
        location = q(row.get("location"), f"atoms[{index}].location")
        weight = q(row.get("weight"), f"atoms[{index}].weight")
        if weight == 0:
            raise CertificateError("zero-weight atoms must be omitted")
        result.append((location, weight))
    return result


def window_value(
    value: Fraction, segments: list[tuple[Fraction, Fraction, Fraction]]
) -> Fraction:
    for lower, upper, height in segments:
        if lower < value < upper:
            return height
    return Fraction(0)


def direct_energy(
    segments: list[tuple[Fraction, Fraction, Fraction]],
    atoms: list[tuple[Fraction, Fraction]],
    cutoff: Fraction,
) -> Fraction:
    points = {cutoff}
    for location, _ in atoms:
        for lower, upper, _ in segments:
            points.add(location + lower)
            points.add(location + upper)
    ordered = sorted(points)
    if len(ordered) < 2:
        return Fraction(0)
    total = Fraction(0)
    for left, right in zip(ordered, ordered[1:]):
        if left >= cutoff:
            break
        right = min(right, cutoff)
        if right <= left:
            continue
        midpoint = (left + right) / 2
        signal = sum(
            weight * window_value(midpoint - location, segments)
            for location, weight in atoms
        )
        total += (right - left) * signal * signal
    return total


def kernel_entry(
    segments: list[tuple[Fraction, Fraction, Fraction]],
    left_location: Fraction,
    right_location: Fraction,
    cutoff: Fraction,
) -> Fraction:
    total = Fraction(0)
    for a, b, value_a in segments:
        for c, d, value_b in segments:
            lower = max(left_location + a, right_location + c)
            upper = min(left_location + b, right_location + d, cutoff)
            if upper > lower:
                total += (upper - lower) * value_a * value_b
    return total


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    classification = payload.get("classification")
    if classification not in {"SYNTHETIC_MODEL", "DIRECTED_PRIME_LOCATIONS"}:
        raise CertificateError("unsupported classification")
    segments = parse_segments(payload)
    atoms = parse_atoms(payload)
    cutoff = q(payload.get("cutoff"), "cutoff")

    matrix = [
        [kernel_entry(segments, u, v, cutoff) for v, _ in atoms]
        for u, _ in atoms
    ]
    if any(matrix[i][j] != matrix[j][i] for i in range(len(atoms)) for j in range(len(atoms))):
        raise CertificateError("kernel reconstruction is not symmetric")

    weights = [weight for _, weight in atoms]
    pair_energy = sum(
        weights[i] * weights[j] * matrix[i][j]
        for i in range(len(atoms))
        for j in range(len(atoms))
    )
    direct = direct_energy(segments, atoms, cutoff)
    if pair_energy != direct:
        raise CertificateError("direct and pairwise energies disagree")

    diagonal = sum(weights[i] ** 2 * matrix[i][i] for i in range(len(atoms)))
    off_diagonal = pair_energy - diagonal
    if pair_energy < 0:
        raise CertificateError("Gram energy became negative")

    claimed = payload.get("claimed")
    reconstructed = {
        "energy": text(pair_energy),
        "diagonal": text(diagonal),
        "off_diagonal": text(off_diagonal),
    }
    if claimed is not None:
        if not isinstance(claimed, dict):
            raise CertificateError("claimed must be an object")
        for key, value in reconstructed.items():
            if q(claimed.get(key), f"claimed.{key}") != Fraction(value):
                raise CertificateError(f"claimed {key} mismatch")

    proof_object = {
        "segments": [[text(x), text(y), text(z)] for x, y, z in segments],
        "atoms": [[text(x), text(y)] for x, y in atoms],
        "cutoff": text(cutoff),
        "kernel": [[text(value) for value in row] for row in matrix],
        **reconstructed,
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "verified": True,
        "atom_count": len(atoms),
        "kernel_matrix": proof_object["kernel"],
        "direct_energy": text(direct),
        "pairwise_energy": text(pair_energy),
        "diagonal_energy": text(diagonal),
        "off_diagonal_energy": text(off_diagonal),
        "exact_proof_object_sha256": canonical_sha(proof_object),
        "proof_boundary": (
            "Exact rational piecewise-constant Gram algebra only. A production "
            "certificate needs directed logarithmic prime locations, the actual "
            "piecewise-linear L-21501 window, and immutable prime manifests."
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
    except (OSError, json.JSONDecodeError, CertificateError, ValueError) as exc:
        result = {"schema": OUTPUT_SCHEMA, "verified": False, "reason": str(exc)}
        code = 2
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
