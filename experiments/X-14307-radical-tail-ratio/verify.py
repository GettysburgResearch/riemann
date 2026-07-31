#!/usr/bin/env python3
"""Exact finite checker for directed radical-tail/coercivity ratio packets.

The checker does not evaluate zeta, the Weil form, Gaussian tails, or a prolate
symbol.  It verifies exact source-polynomial normalization and contracts already
proof-gated rational upper/lower bounds for the two ratios in T-14303.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x14307-radical-tail-ratio.v1"
OUTPUT_SCHEMA = "riemann.x14307-radical-tail-ratio-verification.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def fraction(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    num = integer(raw.get("numerator"), f"{name}.numerator")
    den = integer(raw.get("denominator"), f"{name}.denominator")
    if den <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(num, den)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in poly]


def verify_source(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise CertificateError("source must be an object")
    coeffs_raw = raw.get("polynomial_in_z")
    if not isinstance(coeffs_raw, list) or len(coeffs_raw) != 3:
        raise CertificateError("source.polynomial_in_z must have degree at most two")
    coeffs = [fraction(value, f"source.polynomial_in_z[{i}]") for i, value in enumerate(coeffs_raw)]

    # Fourier images for e^{-pi x^2} times 1, z=pi x^2, and z^2.
    images = [
        [Fraction(1)],
        [Fraction(1, 2), Fraction(-1)],
        [Fraction(3, 4), Fraction(-3), Fraction(1)],
    ]
    transformed = [Fraction(0)]
    for coefficient, image in zip(coeffs, images):
        transformed = poly_add(transformed, poly_scale(image, coefficient))
    transformed += [Fraction(0)] * (3 - len(transformed))

    if transformed != coeffs:
        raise CertificateError("source polynomial is not Fourier invariant")
    if coeffs[0] != 0:
        raise CertificateError("source fails f(0)=0")
    if transformed[0] != 0:
        raise CertificateError("source fails integral f=hat f(0)=0")
    if all(value == 0 for value in coeffs):
        raise CertificateError("source polynomial is zero")

    return {
        "polynomial_in_z": [fj(value) for value in coeffs],
        "fourier_image": [fj(value) for value in transformed],
        "f_at_zero": fj(coeffs[0]),
        "integral": fj(transformed[0]),
        "verified": True,
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")

    source = verify_source(data.get("source"))
    tail_upper = fraction(data.get("tail_residual_upper"), "tail_residual_upper")
    coercivity_lower = fraction(data.get("coercivity_lower"), "coercivity_lower")
    norm2_lower = fraction(data.get("trial_norm_squared_lower"), "trial_norm_squared_lower")
    if tail_upper < 0:
        raise CertificateError("tail upper bound must be nonnegative")
    if coercivity_lower <= 0:
        raise CertificateError("coercivity lower bound must be positive")
    if norm2_lower <= 0:
        raise CertificateError("trial norm-square lower bound must be positive")

    linear = tail_upper / coercivity_lower
    squared = tail_upper * tail_upper / (coercivity_lower * norm2_lower)

    declared_linear = fraction(data.get("declared_linear_ratio_upper"), "declared_linear_ratio_upper")
    declared_squared = fraction(data.get("declared_squared_ratio_upper"), "declared_squared_ratio_upper")
    if linear > declared_linear:
        raise CertificateError("declared linear ratio does not contain exact contraction")
    if squared > declared_squared:
        raise CertificateError("declared squared ratio does not contain exact contraction")

    linear_target = fraction(data.get("linear_target"), "linear_target")
    squared_target = fraction(data.get("squared_target"), "squared_target")
    linear_ok = linear <= linear_target
    squared_ok = squared <= squared_target
    verdict = (
        "CERTIFIED_BOTH_RATIO_TARGETS"
        if linear_ok and squared_ok
        else "CERTIFIED_SQUARED_RATIO_TARGET"
        if squared_ok
        else "UNRESOLVED_RATIO_TARGETS"
    )

    proof_object = {
        "source": source,
        "tail_residual_upper": fj(tail_upper),
        "coercivity_lower": fj(coercivity_lower),
        "trial_norm_squared_lower": fj(norm2_lower),
        "linear_ratio_upper": fj(linear),
        "squared_ratio_upper": fj(squared),
        "linear_target": fj(linear_target),
        "squared_target": fj(squared_target),
        "verdict": verdict,
    }
    digest = hashlib.sha256(
        json.dumps(proof_object, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": data.get("classification"),
        "analytic_claim": "T-14303",
        "certificate_sha256": sha256(path),
        **proof_object,
        "exact_proof_object_sha256": digest,
        "proof_boundary": (
            "Exact Fraction-only source-polynomial and ratio contraction. Analytic "
            "production must separately prove the radical, tail, symbol, form-domain, "
            "and coercivity input bounds."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except (OSError, json.JSONDecodeError, CertificateError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["verdict"] != "UNRESOLVED_RATIO_TARGETS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
