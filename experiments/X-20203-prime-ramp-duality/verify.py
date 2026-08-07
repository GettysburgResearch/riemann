#!/usr/bin/env python3
"""Exact checker for the prime-ramp/autocorrelation identities of L-20208--L-20210."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x20203-prime-ramp.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be bool")
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


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def autocorrelation(q: list[Fraction]) -> list[Fraction]:
    n = len(q)
    return [
        sum(q[j + lag] * q[j] for j in range(n - lag))
        for lag in range(n)
    ] + [Fraction(0)]


def factor_coefficients(q: list[Fraction]) -> list[Fraction]:
    n = len(q)
    q_ext = [Fraction(0)] + q + [Fraction(0)]
    # A(z)=(1-z)Q(z): a_j=q_j-q_(j-1).
    return [q_ext[j + 1] - q_ext[j] for j in range(n + 1)]


def factor_autocorrelation(a: list[Fraction]) -> list[Fraction]:
    n = len(a) - 1
    return [
        sum(a[j + lag] * a[j] for j in range(n + 1 - lag))
        for lag in range(n + 1)
    ]


def ramp(lambdas: list[Fraction], s: Fraction) -> Fraction:
    return sum(
        coefficient * max(Fraction(0), Fraction(k) - s)
        for k, coefficient in enumerate(lambdas, start=1)
    )


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA}")
    raw_q = data.get("q")
    if not isinstance(raw_q, list) or not raw_q:
        raise CertificateError("q must be a nonempty array")
    q = [fraction(value, f"q[{i}]") for i, value in enumerate(raw_q)]
    if not any(q):
        raise CertificateError("q must be nonzero")
    n = len(q)

    a = factor_coefficients(q)
    c = factor_autocorrelation(a)
    lambdas = [-2 * c[k] for k in range(1, n + 1)]
    constant = c[0]
    if constant != sum(lambdas):
        raise CertificateError("constant/FIR coefficient identity failed")

    declared_lambda = data.get("lambda")
    if not isinstance(declared_lambda, list) or len(declared_lambda) != n:
        raise CertificateError("lambda must have the same length as q")
    parsed_lambda = [
        fraction(value, f"lambda[{i}]") for i, value in enumerate(declared_lambda)
    ]
    if parsed_lambda != lambdas:
        raise CertificateError("declared lambda vector mismatch")

    d = autocorrelation(q)
    integer_ramp = [ramp(lambdas, Fraction(m)) for m in range(n + 1)]
    if integer_ramp != [2 * value for value in d]:
        raise CertificateError("integer ramp/autocorrelation identity failed")

    l0 = ramp(lambdas, Fraction(0))
    lhalf = ramp(lambdas, Fraction(1, 2))
    plus_square = Fraction(1, 2) * sum(
        (q[j] + (q[j - 1] if j else 0)) ** 2
        for j in range(n + 1)
        if j < n or q[n - 1] != 0
    )
    # The preceding comprehension needs q_N=0 on its final row.
    plus_square = Fraction(1, 2) * sum(
        ((q[j] if j < n else 0) + (q[j - 1] if j > 0 else 0)) ** 2
        for j in range(n + 1)
    )
    if l0 != 2 * sum(value * value for value in q):
        raise CertificateError("L(0) norm identity failed")
    if lhalf != plus_square or lhalf <= 0:
        raise CertificateError("strict half-knot square identity failed")

    raw_samples = data.get("samples")
    if not isinstance(raw_samples, list) or not raw_samples:
        raise CertificateError("samples must be a nonempty array")
    sample_rows: list[dict[str, object]] = []
    for index, raw in enumerate(raw_samples):
        if not isinstance(raw, dict):
            raise CertificateError(f"samples[{index}] must be an object")
        s = fraction(raw.get("s"), f"samples[{index}].s")
        expected = fraction(raw.get("value"), f"samples[{index}].value")
        if not 0 <= s <= n:
            raise CertificateError("sample outside ramp support")
        value = ramp(lambdas, s)
        if value != expected:
            raise CertificateError("sample ramp value mismatch")
        m = min(int(s), n - 1) if s < n else n
        if s == n:
            interpolated = 2 * d[n]
        else:
            theta = s - m
            interpolated = 2 * ((1 - theta) * d[m] + theta * d[m + 1])
        if value != interpolated:
            raise CertificateError("sample interpolation identity failed")
        sample_rows.append({"s": fj(s), "value": fj(value)})

    declared_ratio = fraction(data.get("half_ratio"), "half_ratio")
    if declared_ratio != lhalf / l0:
        raise CertificateError("half-ratio declaration mismatch")

    result: dict[str, Any] = {
        "schema": "riemann.x20203-prime-ramp.verification.v1",
        "verified": True,
        "degree": n,
        "factor_coefficients": [fj(value) for value in a],
        "lambda": [fj(value) for value in lambdas],
        "q_autocorrelation": [fj(value) for value in d],
        "integer_ramp": [fj(value) for value in integer_ramp],
        "L0": fj(l0),
        "Lhalf": fj(lhalf),
        "half_ratio": fj(lhalf / l0),
        "samples": sample_rows,
        "verdict": "EXACT_PRIME_RAMP_AUTOCORRELATION_IDENTITIES_VERIFIED",
        "proof_boundary": (
            "Synthetic exact algebra only; no zeta prime stream, cofinal sign, "
            "or RH conclusion is certified."
        ),
    }
    result["proof_object_sha256"] = digest(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
