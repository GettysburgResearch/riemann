#!/usr/bin/env python3
"""Exact algebra checker for the L-15101--L-15103 radical bridge.

This checker uses only Python integers, fractions.Fraction, JSON, and SHA-256.
It does not evaluate zeta, Xi, prolate functions, or the Weil form.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15101-radical-hermite-bridge.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer, not Boolean")
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
            raise CertificateError(f"{name} is not a rational string") from exc
    if isinstance(value, list) and len(value) == 2:
        numerator = integer(value[0], name + "[0]")
        denominator = integer(value[1], name + "[1]")
        if denominator == 0:
            raise CertificateError(f"{name} has zero denominator")
        return Fraction(numerator, denominator)
    raise CertificateError(
        f"{name} must be an integer, rational string, or [numerator,denominator]"
    )


def vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list):
        raise CertificateError(f"{name} must be a list")
    return [rational(value, f"{name}[{index}]") for index, value in enumerate(raw)]


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty square matrix")
    rows = [vector(row, f"{name}[{index}]") for index, row in enumerate(raw)]
    size = len(rows)
    if any(len(row) != size for row in rows):
        raise CertificateError(f"{name} must be square")
    if any(rows[i][j] != rows[j][i] for i in range(size) for j in range(size)):
        raise CertificateError(f"{name} must be symmetric")
    return rows


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    if len(left) != len(right):
        raise CertificateError("vector dimensions differ")
    return [a + b for a, b in zip(left, right)]


def matvec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    if len(a) != len(x):
        raise CertificateError("matrix/vector dimensions differ")
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    if len(left) != len(right):
        raise CertificateError("vector dimensions differ")
    return sum(a * b for a, b in zip(left, right))


def bilinear(
    a: list[list[Fraction]], left: list[Fraction], right: list[Fraction]
) -> Fraction:
    return dot(left, matvec(a, right))


def canonical_digest(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def verify_gaussian(payload: dict[str, Any]) -> dict[str, str]:
    if not isinstance(payload, dict):
        raise CertificateError("gaussian_moments must be an object")
    m2 = rational(payload.get("normalized_second_moment"), "normalized_second_moment")
    m4 = rational(payload.get("normalized_fourth_moment"), "normalized_fourth_moment")
    cancellation = 2 * m4 - 3 * m2
    if cancellation != 0:
        raise CertificateError("Hermite Gaussian moment cancellation failed")
    return {
        "normalized_second_moment": str(m2),
        "normalized_fourth_moment": str(m4),
        "two_m4_minus_three_m2": str(cancellation),
    }


def verify_radical(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise CertificateError("radical_decomposition must be an object")
    q = matrix(payload.get("matrix"), "radical_decomposition.matrix")
    r = vector(payload.get("radical"), "radical_decomposition.radical")
    p = vector(payload.get("local"), "radical_decomposition.local")
    t = vector(payload.get("tail"), "radical_decomposition.tail")
    if any(len(item) != len(q) for item in (r, p, t)):
        raise CertificateError("radical vectors have the wrong dimension")
    if add(p, t) != r:
        raise CertificateError("local plus tail does not equal the radical vector")
    qr = matvec(q, r)
    if any(value != 0 for value in qr):
        raise CertificateError("declared radical vector is not in the matrix kernel")
    qpp = bilinear(q, p, p)
    qtt = bilinear(q, t, t)
    qpt = bilinear(q, p, t)
    qtp = bilinear(q, t, p)
    if not (qpp == qtt == -qpt == -qtp):
        raise CertificateError("radical localization energy identities failed")
    if add(matvec(q, p), matvec(q, t)) != [Fraction(0)] * len(q):
        raise CertificateError("transverse radical residual identity failed")
    return {
        "kernel_product": [str(value) for value in qr],
        "q_local_local": str(qpp),
        "q_tail_tail": str(qtt),
        "q_local_tail": str(qpt),
        "q_tail_local": str(qtp),
        "matrix_residual_identity": "Q*local = -Q*tail",
    }


def verify_prolate(payload: dict[str, Any]) -> dict[str, str]:
    if not isinstance(payload, dict):
        raise CertificateError("prolate_repair must be an object")
    epsilon = rational(payload.get("initial_value"), "prolate_repair.initial_value")
    initial_integral = rational(
        payload.get("initial_integral"), "prolate_repair.initial_integral"
    )
    a0 = rational(payload.get("mode0_value"), "prolate_repair.mode0_value")
    a2 = rational(payload.get("mode2_value"), "prolate_repair.mode2_value")
    theta0 = rational(payload.get("theta0"), "prolate_repair.theta0")
    theta2 = rational(payload.get("theta2"), "prolate_repair.theta2")
    if initial_integral != 0:
        raise CertificateError("the two-sign formula expects zero initial integral")
    if a0 == 0 or a2 == 0:
        raise CertificateError("prolate mode values at zero must be nonzero")
    if theta0 == theta2:
        raise CertificateError("signed prolate eigenvalues must be distinct")
    alpha = epsilon * theta2 / (a0 * (theta0 - theta2))
    beta = -epsilon * theta0 / (a2 * (theta0 - theta2))
    corrected_value = epsilon + alpha * a0 + beta * a2
    corrected_integral = (
        initial_integral + alpha * theta0 * a0 + beta * theta2 * a2
    )
    if corrected_value != 0 or corrected_integral != 0:
        raise CertificateError("two-sign prolate correction did not close both constraints")
    return {
        "alpha": str(alpha),
        "beta": str(beta),
        "corrected_value": str(corrected_value),
        "corrected_integral_common_scale": str(corrected_integral),
    }


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "classification": "EXACT_FINITE_ALGEBRA",
        "gaussian_moments": verify_gaussian(payload.get("gaussian_moments")),
        "radical_decomposition": verify_radical(payload.get("radical_decomposition")),
        "prolate_repair": verify_prolate(payload.get("prolate_repair")),
        "proof_boundary": (
            "The checker verifies exact algebra only. It does not verify the imported "
            "Weil-radical theorem, the E-map normalization, any prolate eigenfunction, "
            "the continuum spectral gap, or the Riemann hypothesis."
        ),
    }
    result["exact_proof_object_sha256"] = canonical_digest(result)
    return result


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
