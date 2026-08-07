#!/usr/bin/env python3
"""Exact rational regression for endpoint convolution/polar cancellation."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15403-endpoint-pole-cancellation.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    n = integer(value.get("numerator"), f"{name}.numerator")
    d = integer(value.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    raw_profile = data.get("profile")
    if not isinstance(raw_profile, list) or not raw_profile:
        raise CertificateError("profile must be a nonempty array")
    profile = [frac(x, f"profile[{i}]") for i, x in enumerate(raw_profile)]

    q = frac(data.get("laplace_ratio"), "laplace_ratio")
    if not 0 < q < 1:
        raise CertificateError("laplace_ratio must lie strictly between zero and one")

    n = len(profile)
    convolution = [Fraction(0) for _ in range(2 * n - 1)]
    for i, x in enumerate(profile):
        for j, y in enumerate(profile):
            convolution[i + j] += x * y

    laplace_profile = sum((q**i) * x for i, x in enumerate(profile))
    pole_hankel = sum((q**u) * c for u, c in enumerate(convolution))
    if pole_hankel != laplace_profile * laplace_profile:
        raise CertificateError("rank-one convolution identity failed")

    claimed = data.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError("claimed must be an object")
    if frac(claimed.get("pole_hankel"), "claimed.pole_hankel") != pole_hankel:
        raise CertificateError("claimed pole_hankel mismatch")

    scale = frac(data.get("pole_scale"), "pole_scale")
    if scale <= 0:
        raise CertificateError("pole_scale must be positive")
    prime_main = 2 * scale * pole_hankel
    polar_main = -2 * scale * laplace_profile * laplace_profile
    if prime_main + polar_main != 0:
        raise CertificateError("prime/polar cancellation failed")

    raw_discrepancy = data.get("discrepancy_weights")
    if not isinstance(raw_discrepancy, list) or len(raw_discrepancy) != len(convolution):
        raise CertificateError("discrepancy_weights must match the convolution length")
    discrepancy_weights = [
        frac(x, f"discrepancy_weights[{i}]") for i, x in enumerate(raw_discrepancy)
    ]
    discrepancy_value = 2 * sum(
        discrepancy_weights[u] * convolution[u] for u in range(len(convolution))
    )
    if frac(claimed.get("discrepancy_value"), "claimed.discrepancy_value") != discrepancy_value:
        raise CertificateError("claimed discrepancy_value mismatch")

    return {
        "schema": SCHEMA,
        "status": "EXACT_ENDPOINT_POLE_CANCELLATION",
        "profile_length": n,
        "convolution": [fj(x) for x in convolution],
        "laplace_profile": fj(laplace_profile),
        "pole_hankel": fj(pole_hankel),
        "prime_main": fj(prime_main),
        "polar_main": fj(polar_main),
        "cancelled_main": fj(prime_main + polar_main),
        "discrepancy_value": fj(discrepancy_value),
        "proof_boundary": "finite rational convolution regression; not a prime or zeta computation",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
