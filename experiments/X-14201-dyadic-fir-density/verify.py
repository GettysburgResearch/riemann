#!/usr/bin/env python3
"""Exact synthetic checker for the dyadic FIR refinement identities.

This checker uses only integers and fractions.Fraction. It verifies finite
algebra behind T-14201; it does not evaluate the Riemann zeta function and
cannot create an RH candidate by itself.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.dyadic-fir-density.synthetic.v1"


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
            raise CertificateError(f"{name} must be a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def vector_json(values: Sequence[Fraction]) -> list[dict[str, str]]:
    return [fraction_json(value) for value in values]


def psi(t: Fraction, sign: int) -> Fraction:
    if sign not in (-1, 1):
        raise CertificateError("psi_quadratic_sign must be +1 or -1")
    return sign * t * t


def screw_form(c: Sequence[Fraction], h: Fraction, sign: int) -> Fraction:
    return -sum(
        c[i] * c[j] * psi(Fraction(i - j) * h, sign)
        for i in range(len(c))
        for j in range(len(c))
    )


def increment_vector(c: Sequence[Fraction]) -> list[Fraction]:
    if len(c) < 2:
        raise CertificateError("coefficient vector must have length at least two")
    if sum(c) != 0:
        raise CertificateError("coefficient vector must sum exactly to zero")
    return [sum(c[: j + 1]) for j in range(len(c) - 1)]


def increment_matrix(n: int, h: Fraction, sign: int) -> list[list[Fraction]]:
    if n <= 0:
        raise CertificateError("matrix dimension must be positive")
    return [
        [
            psi(Fraction(i - j + 1) * h, sign)
            + psi(Fraction(i - j - 1) * h, sign)
            - 2 * psi(Fraction(i - j) * h, sign)
            for j in range(n)
        ]
        for i in range(n)
    ]


def quadratic(matrix: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]) -> Fraction:
    n = len(vector)
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise CertificateError("matrix and vector dimensions do not match")
    return sum(vector[i] * matrix[i][j] * vector[j] for i in range(n) for j in range(n))


def refine_coefficients(c: Sequence[Fraction], factor: int) -> list[Fraction]:
    if factor < 2:
        raise CertificateError("refinement factor must be at least two")
    refined = [Fraction(0)] * (factor * (len(c) - 1) + 1)
    for index, coefficient in enumerate(c):
        refined[factor * index] = coefficient
    return refined


def parse_vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or len(raw) < 2:
        raise CertificateError(f"{name} must be an array of length at least two")
    return [fraction(value, f"{name}[{index}]") for index, value in enumerate(raw)]


def verify_case(raw: dict[str, Any], sign: int) -> dict[str, Any]:
    case_id = raw.get("id")
    if not isinstance(case_id, str) or not case_id:
        raise CertificateError("case id must be a nonempty string")
    h = fraction(raw.get("h"), f"{case_id}.h")
    if h <= 0:
        raise CertificateError("grid spacing must be positive")
    c = parse_vector(raw.get("coefficients"), f"{case_id}.coefficients")
    b = increment_vector(c)
    form = screw_form(c, h, sign)
    matrix = increment_matrix(len(b), h, sign)
    matrix_form = quadratic(matrix, b)
    if form != matrix_form:
        raise AssertionError("increment Toeplitz identity failed")

    expected = fraction(raw.get("expected_form"), f"{case_id}.expected_form")
    if form != expected:
        raise CertificateError(f"case {case_id}: expected form mismatch")
    expected_status = raw.get("expected_status")
    status = "NEGATIVE" if form < 0 else "POSITIVE" if form > 0 else "ZERO"
    if expected_status != status:
        raise CertificateError(f"case {case_id}: expected status mismatch")

    refinement = raw.get("refinement")
    refinement_output = None
    if refinement is not None:
        if not isinstance(refinement, dict):
            raise CertificateError("refinement must be an object")
        factor = integer(refinement.get("factor"), f"{case_id}.refinement.factor")
        refined_h = h / factor
        refined_c = refine_coefficients(c, factor)
        refined_b = increment_vector(refined_c)
        refined_form = screw_form(refined_c, refined_h, sign)
        refined_matrix_form = quadratic(
            increment_matrix(len(refined_b), refined_h, sign), refined_b
        )
        if refined_form != form or refined_matrix_form != form:
            raise CertificateError("physical-grid refinement did not preserve the form")
        refinement_output = {
            "factor": factor,
            "h": fraction_json(refined_h),
            "coefficients": vector_json(refined_c),
            "increment_vector": vector_json(refined_b),
            "form": fraction_json(refined_form),
        }

    return {
        "id": case_id,
        "h": fraction_json(h),
        "coefficients": vector_json(c),
        "increment_vector": vector_json(b),
        "form": fraction_json(form),
        "status": status,
        "refinement": refinement_output,
    }


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    sign = integer(data.get("psi_quadratic_sign"), "psi_quadratic_sign")
    if sign not in (-1, 1):
        raise CertificateError("psi_quadratic_sign must be +1 or -1")
    raw_cases = data.get("cases")
    if not isinstance(raw_cases, list) or not raw_cases:
        raise CertificateError("cases must be a nonempty array")
    seen: set[str] = set()
    outputs = []
    for index, raw in enumerate(raw_cases):
        if not isinstance(raw, dict):
            raise CertificateError(f"cases[{index}] must be an object")
        case_id = raw.get("id")
        if case_id in seen:
            raise CertificateError("case ids must be unique")
        seen.add(case_id)
        outputs.append(verify_case(raw, sign))
    return {
        "schema": SCHEMA,
        "status": "EXACT_SYNTHETIC_DYADIC_FIR_REPLAY",
        "psi_quadratic_sign": sign,
        "cases": outputs,
        "proof_boundary": (
            "finite rational screw/Toeplitz algebra only; no Riemann-zeta or "
            "prime-power evaluation"
        ),
    }


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify_certificate(load(args.certificate))
    except CertificateError as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
