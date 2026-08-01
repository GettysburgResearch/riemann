#!/usr/bin/env python3
"""Exact verifier for L-15632's line-centered Schur perturbation theorem.

The checker uses only integers and fractions.Fraction.  It reconstructs both
2 x 2 block LMIs, the line-centered harmonic minimizer, the PR #191 residual
short, the exact actual Schur value, and the theorem's rational lower bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def frac(obj: dict[str, str]) -> Fraction:
    if not isinstance(obj, dict):
        raise TypeError("fraction must be an object")
    return Fraction(int(obj["numerator"]), int(obj["denominator"]))


def as_json(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def psd2(a: Fraction, b: Fraction, c: Fraction) -> bool:
    """PSD test for [[a,b],[b,c]] over exact rationals."""
    return a >= 0 and c >= 0 and a * c - b * b >= 0


def verify(data: dict[str, Any], raw: bytes) -> dict[str, Any]:
    if data.get("schema") != "riemann.x15613-line-centered-schur.v1":
        raise ValueError("unsupported schema")

    D = frac(data["D"])
    G = frac(data["G"])
    M = frac(data["M"])
    h = frac(data["h"])
    ell = frac(data["ell"])
    eps = frac(data["epsilon"])
    sqrt_ratio = frac(data["sqrt_ell_over_h"])

    B0 = frac(data["line_centered"]["B"])
    Z0 = frac(data["line_centered"]["Z"])
    C0 = frac(data["line_centered"]["C"])

    eB = frac(data["perturbation"]["B"])
    eZ = frac(data["perturbation"]["Z"])
    eC = frac(data["perturbation"]["C"])

    if min(D, G, M, h) <= 0:
        raise ValueError("metrics and h must be strictly positive")
    if ell < 0 or eps < 0 or eps >= h:
        raise ValueError("invalid ell/epsilon range")
    if sqrt_ratio < 0 or sqrt_ratio * sqrt_ratio != ell / h:
        raise ValueError("declared square root does not equal ell/h")

    # Line-centered block, floor, and upper packet compression.
    if not psd2(B0, Z0, C0):
        raise ValueError("line-centered block is not PSD")
    if C0 < h * M:
        raise ValueError("line-centered ambient floor fails")
    if B0 > ell * D:
        raise ValueError("line-centered low upper bound fails")

    # Relative perturbation LMI: -eps diag(D,M) <= E <= eps diag(D,M).
    if not psd2(eps * D - eB, -eZ, eps * M - eC):
        raise ValueError("upper relative perturbation LMI fails")
    if not psd2(eps * D + eB, eZ, eps * M + eC):
        raise ValueError("lower relative perturbation LMI fails")

    B = B0 + eB
    Z = Z0 + eZ
    C = C0 + eC
    if C <= 0 or C < (h - eps) * M:
        raise ValueError("actual ambient block is not coercive")

    line_schur = B0 - Z0 * Z0 / C0
    if line_schur < 0:
        raise ValueError("line-centered Schur complement is negative")

    x0 = Z0 / C0
    x0_metric = x0 * x0 * M
    if x0_metric > (ell / h) * D:
        raise ValueError("line-centered harmonic minimizer bound fails")

    residual = Z - C * x0
    trial_energy = B - 2 * Z * x0 + C * x0 * x0
    direct_lower = trial_energy - residual * residual / ((h - eps) * M)
    actual_schur = B - Z * Z / C
    if actual_schur < direct_lower:
        raise ValueError("PR #191 direct lower matrix exceeds exact Schur value")

    eta = eps * (1 + ell / h) + (
        eps * eps / (h - eps) * (1 + sqrt_ratio) * (1 + sqrt_ratio)
    )
    theorem_lower = -eta * D
    if direct_lower < theorem_lower:
        raise ValueError("L-15632 direct lower bound fails")
    if actual_schur < theorem_lower:
        raise ValueError("L-15632 Schur lower bound fails")

    q = D / G
    normalized_negative = max(-actual_schur / G, Fraction(0))
    normalized_bound = q * eta
    if normalized_negative > normalized_bound:
        raise ValueError("normalized negative-part bound fails")

    return {
        "schema": "riemann.x15613-line-centered-schur.result.v1",
        "classification": "EXACT_LINE_CENTERED_SCHUR_PERTURBATION_PASSES",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "line_centered_schur": as_json(line_schur),
        "line_centered_trial_solve": as_json(x0),
        "actual_residual": as_json(residual),
        "trial_energy": as_json(trial_energy),
        "direct_lower": as_json(direct_lower),
        "actual_schur": as_json(actual_schur),
        "eta": as_json(eta),
        "theorem_lower": as_json(theorem_lower),
        "normalized_negative_part": as_json(normalized_negative),
        "normalized_bound": as_json(normalized_bound),
        "strict_bound_slack": as_json(normalized_bound - normalized_negative),
        "verdict": "PASS_EXACT_L15632_SOFT_SCHUR_BOUND",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    raw = args.certificate.read_bytes()
    data = json.loads(raw)
    result = verify(data, raw)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(encoded, end="")
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
