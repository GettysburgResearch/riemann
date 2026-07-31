#!/usr/bin/env python3
"""Exact rational checker for L-15302 three-mode source repair."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15301-codimension-two-source-repair.v1"
OUTPUT_SCHEMA = "riemann.x15301-codimension-two-source-repair.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def parse_vector(value: Any, name: str) -> list[Fraction]:
    if not isinstance(value, list) or len(value) != 3:
        raise CertificateError(f"{name} must contain exactly three rationals")
    return [parse_fraction(item, f"{name}[{index}]") for index, item in enumerate(value)]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    if data.get("status") != "DECLARED_THREE_MODE_SOURCE_PACKET":
        raise CertificateError("certificate status does not preserve the proof boundary")
    if data.get("declares_orthonormal_modes") is not True:
        raise CertificateError("finite-Fourier identity requires declared orthonormal modes")

    values = parse_vector(data.get("values_at_zero"), "values_at_zero")
    masses = parse_vector(data.get("integrals"), "integrals")
    eigenvalues = parse_vector(data.get("finite_fourier_eigenvalues"), "finite_fourier_eigenvalues")

    for index, eigenvalue in enumerate(eigenvalues):
        if not 0 <= eigenvalue <= 1:
            raise CertificateError(f"finite_fourier_eigenvalues[{index}] lies outside [0,1]")
        if masses[index] != eigenvalue * values[index]:
            raise CertificateError(f"integral/eigenvalue compatibility fails at mode {index}")

    coefficients = [
        values[1] * masses[2] - values[2] * masses[1],
        values[2] * masses[0] - values[0] * masses[2],
        values[0] * masses[1] - values[1] * masses[0],
    ]
    if all(value == 0 for value in coefficients):
        raise CertificateError("the two source functionals are proportional")

    annihilated_value = sum(coefficients[i] * values[i] for i in range(3))
    annihilated_mass = sum(coefficients[i] * masses[i] for i in range(3))
    if annihilated_value != 0 or annihilated_mass != 0:
        raise CertificateError("internal source-annihilation identity failed")

    norm_squared = sum(value * value for value in coefficients)
    defect_squared = 2 * sum(
        coefficients[i] * coefficients[i] * (1 - eigenvalues[i])
        for i in range(3)
    )
    if norm_squared <= 0 or defect_squared < 0:
        raise CertificateError("invalid norm or Fourier defect")

    result: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "verified": True,
        "status": "EXACT_CODIMENSION_TWO_SOURCE_REPAIR_VERIFIED",
        "coefficients": [fraction_json(value) for value in coefficients],
        "annihilated_value": fraction_json(annihilated_value),
        "annihilated_mass": fraction_json(annihilated_mass),
        "finite_fourier": {
            "norm_squared": fraction_json(norm_squared),
            "defect_squared": fraction_json(defect_squared),
            "normalized_defect_squared": fraction_json(defect_squared / norm_squared),
            "identity": "2 sum_j a_j^2 (1-chi_j)",
        },
        "proof_boundary": (
            "Exact rational algebra only; functional values, orthonormality, source "
            "regularity, and finite-Fourier eigenrelations are declared external gates."
        ),
    }
    result["verification_sha256"] = canonical_sha(result)
    return result


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(load(args.certificate))
        code = 0
    except CertificateError as exc:
        result = {
            "schema": OUTPUT_SCHEMA,
            "verified": False,
            "status": "REJECTED",
            "reason": str(exc),
        }
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
