#!/usr/bin/env python3
"""Exact scalar replay for L-18512/T-18504.

The scalar control is the one-dimensional instance of
    S_W = J_X^* H J_X - R_X^* C^{-1} R_X,
with a coercive residual upper bound.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def frac(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise TypeError("booleans are not valid rational data")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"unsupported rational value: {value!r}")


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify(cert: dict[str, Any]) -> dict[str, Any]:
    if cert.get("schema") != "X-18504-v1":
        raise ValueError("unexpected schema")

    local = frac(cert["local_positive_block"])
    terminal = frac(cert["centered_terminal_block"])
    B = frac(cert["low_block"])
    C = frac(cert["ambient_block"])
    Z = frac(cert["ambient_cross"])
    X = frac(cert["trial_harmonic_solve"])
    h = frac(cert["coercivity_h"])
    M = frac(cert["coercivity_metric"])
    G = frac(cert["packet_metric"])

    if min(C, h, M, G) <= 0:
        raise ValueError("positive blocks and metrics must be strictly positive")
    if B != local + terminal:
        raise ValueError("low block must equal local plus centered-terminal blocks")
    if C < h * M:
        raise ValueError("declared coercivity C >= h M fails")

    residual = Z - C * X
    trial_energy = B - 2 * Z * X + C * X * X
    residual_penalty = residual * residual / (h * M)
    certified_lower = trial_energy - residual_penalty
    exact_schur = B - Z * Z / C

    if certified_lower > exact_schur:
        raise ValueError("purported lower certificate exceeds the exact Schur value")

    # The old separated route keeps only a one-sided lower bound terminal >= 0
    # and charges the harmonic correction independently.
    separated_floor = local + min(terminal, Fraction(0)) - Z * Z / C
    joint_gain = certified_lower - separated_floor

    declared = cert.get("declared_verdict")
    verdict = (
        "CERTIFIED_POSITIVE_COMPLETE_COMPLEMENT"
        if certified_lower > 0
        else "CERTIFIED_NONNEGATIVE_COMPLETE_COMPLEMENT"
        if certified_lower == 0
        else "UNRESOLVED_OR_NEGATIVE_COMPLETE_COMPLEMENT"
    )
    if declared != verdict:
        raise ValueError(f"declared verdict {declared!r} does not match {verdict!r}")

    canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
    return {
        "schema": "X-18504-result-v1",
        "residual": fstr(residual),
        "trial_lift_energy": fstr(trial_energy),
        "residual_penalty_upper": fstr(residual_penalty),
        "certified_direct_floor": fstr(certified_lower / G),
        "exact_schur_floor": fstr(exact_schur / G),
        "separated_floor": fstr(separated_floor / G),
        "joint_improvement": fstr(joint_gain / G),
        "verdict": verdict,
        "certificate_sha256": hashlib.sha256(canonical).hexdigest(),
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py CERTIFICATE.json")
    cert = json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps(verify(cert), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
