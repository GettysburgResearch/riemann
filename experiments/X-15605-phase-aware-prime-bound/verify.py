#!/usr/bin/env python3
"""Exact scalar checker for L-15613/T-15604 phase-aware prime bands."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15605-phase-aware-prime-bound.v1"


def is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def frac(obj: Any, name: str) -> Fraction:
    if not isinstance(obj, dict):
        raise ValueError(f"{name} must be a rational object")
    num = obj.get("numerator")
    den = obj.get("denominator")
    if not is_int(num) or not is_int(den) or den <= 0:
        raise ValueError(f"{name} has invalid numerator/denominator")
    return Fraction(num, den)


def interval(obj: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(obj, dict):
        raise ValueError(f"{name} must be an interval object")
    lo = frac(obj.get("lower"), f"{name}.lower")
    hi = frac(obj.get("upper"), f"{name}.upper")
    if lo > hi:
        raise ValueError(f"{name} has reversed endpoints")
    return lo, hi


def dump_frac(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical_sha256(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("unsupported schema")
    classification = data.get("classification")
    if classification not in {"SYNTHETIC_MODEL", "RIEMANN_DIRECTED"}:
        raise ValueError("invalid classification")

    prime_lo, prime_hi = interval(data.get("prime_interval"), "prime_interval")
    phase_lo, phase_hi = interval(data.get("phase_interval"), "phase_interval")

    shells = data.get("shells")
    if not isinstance(shells, list):
        raise ValueError("shells must be a list")

    shell_budget = Fraction(0)
    normalized_shells: list[dict[str, Any]] = []
    last_right: Fraction | None = None
    for index, row in enumerate(shells):
        if not isinstance(row, dict):
            raise ValueError(f"shell {index} must be an object")
        left = frac(row.get("left"), f"shell[{index}].left")
        right = frac(row.get("right"), f"shell[{index}].right")
        if left < 0 or left >= right:
            raise ValueError(f"shell {index} has invalid range")
        if last_right is not None and left < last_right:
            raise ValueError("shells overlap or are out of order")
        last_right = right

        count_upper = frac(row.get("count_upper"), f"shell[{index}].count_upper")
        selected = row.get("selected_multiplicity")
        envelope = frac(row.get("transform_envelope_upper"), f"shell[{index}].envelope")
        if count_upper < 0 or envelope < 0:
            raise ValueError("negative shell bound")
        if not is_int(selected) or selected < 0:
            raise ValueError("selected multiplicity must be a nonnegative integer")
        if Fraction(selected) > count_upper:
            raise ValueError("selected multiplicity exceeds shell count upper bound")
        residual_count = count_upper - selected
        contribution = 2 * residual_count * envelope
        shell_budget += contribution
        normalized_shells.append(
            {
                "left": dump_frac(left),
                "right": dump_frac(right),
                "count_upper": dump_frac(count_upper),
                "selected_multiplicity": selected,
                "transform_envelope_upper": dump_frac(envelope),
                "residual_contribution": dump_frac(contribution),
            }
        )

    high = data.get("high_zero_tail")
    if not isinstance(high, dict):
        raise ValueError("high_zero_tail must be an object")
    transform_constant = frac(high.get("transform_constant_upper"), "high.transform_constant")
    zero_moment = frac(high.get("zero_moment_upper"), "high.zero_moment")
    if transform_constant < 0 or zero_moment < 0:
        raise ValueError("negative high-zero tail input")
    high_budget = 2 * transform_constant * zero_moment

    trivial_budget = frac(data.get("trivial_tail_upper"), "trivial_tail_upper")
    arithmetic_radius = frac(data.get("additional_radius"), "additional_radius")
    if trivial_budget < 0 or arithmetic_radius < 0:
        raise ValueError("negative residual radius")

    total_budget = shell_budget + high_budget + trivial_budget + arithmetic_radius
    residual_lo = prime_lo - phase_hi
    residual_hi = prime_hi - phase_lo

    if residual_lo > total_budget:
        verdict = "CERTIFIED_OFFLINE_ZERO_BOUND_VIOLATION_POSITIVE"
    elif residual_hi < -total_budget:
        verdict = "CERTIFIED_OFFLINE_ZERO_BOUND_VIOLATION_NEGATIVE"
    elif residual_lo >= -total_budget and residual_hi <= total_budget:
        verdict = "FINITE_VALUE_CONSISTENT_WITH_RH_BOUND"
    else:
        verdict = "UNRESOLVED_BOUNDARY_OVERLAP"

    proof_object = {
        "schema": SCHEMA,
        "classification": classification,
        "prime_interval": {"lower": dump_frac(prime_lo), "upper": dump_frac(prime_hi)},
        "phase_interval": {"lower": dump_frac(phase_lo), "upper": dump_frac(phase_hi)},
        "shells": normalized_shells,
        "shell_budget": dump_frac(shell_budget),
        "high_zero_budget": dump_frac(high_budget),
        "trivial_tail_upper": dump_frac(trivial_budget),
        "additional_radius": dump_frac(arithmetic_radius),
        "total_budget": dump_frac(total_budget),
        "residual_interval": {"lower": dump_frac(residual_lo), "upper": dump_frac(residual_hi)},
        "verdict": verdict,
        "proof_boundary": (
            "Exact rational contraction only. RIEMANN_DIRECTED use additionally requires "
            "the explicit-formula normalization, complete prime-power manifest, actual "
            "selected zero certificates, transform envelopes, and zero-count majorants."
        ),
    }
    proof_object["exact_proof_object_sha256"] = canonical_sha256(proof_object)
    return proof_object


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = verify(data)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
