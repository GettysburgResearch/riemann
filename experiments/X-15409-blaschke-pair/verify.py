#!/usr/bin/env python3
"""Exact checker for the Blaschke-pair Hankel/Toeplitz formulas."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15409-blaschke-pair.synthetic.v1"


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
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def verify_case(raw: Any, index: int) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise CertificateError(f"cases[{index}] must be an object")
    name = raw.get("name")
    if not isinstance(name, str) or not name:
        raise CertificateError(f"cases[{index}].name must be a nonempty string")

    delta = frac(raw.get("delta"), f"cases[{index}].delta")
    omega = frac(raw.get("omega"), f"cases[{index}].omega")
    if not Fraction(0) < omega < delta < Fraction(1, 2):
        raise CertificateError(
            f"cases[{index}] must satisfy 0 < omega < delta < 1/2"
        )

    y_minus = delta - omega
    y_plus = delta + omega
    norm = (y_plus - y_minus) / (y_plus + y_minus)
    if norm != omega / delta:
        raise CertificateError("internal Blaschke-ratio identity failed")
    norm_squared = norm * norm
    toeplitz_floor = 1 - norm_squared
    factored_floor = 4 * y_minus * y_plus / (y_minus + y_plus) ** 2
    if toeplitz_floor != factored_floor:
        raise CertificateError("internal Toeplitz-floor factorization failed")

    claimed = raw.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError(f"cases[{index}].claimed must be an object")
    expected = {
        "y_minus": y_minus,
        "y_plus": y_plus,
        "hankel_norm": norm,
        "hankel_norm_squared": norm_squared,
        "toeplitz_floor": toeplitz_floor,
    }
    for key, actual in expected.items():
        supplied = frac(claimed.get(key), f"cases[{index}].claimed.{key}")
        if supplied != actual:
            raise CertificateError(f"cases[{index}] claimed {key} mismatch")

    return {
        "name": name,
        "delta": fj(delta),
        "omega": fj(omega),
        "y_minus": fj(y_minus),
        "y_plus": fj(y_plus),
        "hankel_norm": fj(norm),
        "hankel_norm_squared": fj(norm_squared),
        "toeplitz_floor": fj(toeplitz_floor),
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    raw_cases = data.get("cases")
    if not isinstance(raw_cases, list) or len(raw_cases) < 2:
        raise CertificateError("cases must contain at least two entries")

    names: set[str] = set()
    results = []
    for index, raw in enumerate(raw_cases):
        result = verify_case(raw, index)
        if result["name"] in names:
            raise CertificateError("case names must be unique")
        names.add(result["name"])
        results.append(result)

    norms = [frac(item["claimed"]["hankel_norm"], "case norm") for item in raw_cases]
    omegas = [frac(item["omega"], "case omega") for item in raw_cases]
    deltas = [frac(item["delta"], "case delta") for item in raw_cases]
    if len(set(deltas)) == 1:
        ordered = sorted(zip(omegas, norms))
        if any(ordered[j][1] >= ordered[j + 1][1] for j in range(len(ordered) - 1)):
            raise CertificateError("Hankel norms must increase strictly with omega")

    return {
        "schema": SCHEMA,
        "status": "EXACT_BLASCHKE_PAIR_HANKEL_PRESSURE",
        "cases": results,
        "identity": {
            "hankel_norm": "omega/delta",
            "toeplitz_floor": "1-(omega/delta)^2",
        },
        "proof_boundary": (
            "exact rational isolated-pair algebra only; no Riemann zero is "
            "located and the full scattering regular-factor limit is not "
            "numerically evaluated"
        ),
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
