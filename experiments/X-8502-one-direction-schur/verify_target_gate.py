#!/usr/bin/env python3
"""Exact checker for the L-8502 one-direction Schur target gate.

The checker binds the completed X-2805 fixed-vector verdict to a deliberately
coarse set of *conditional* complement, residual, and operator targets.  It
verifies only the exact finite arithmetic implication.  It rejects any input
that claims those three targets have already been proved.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

VERDICT_SCHEMA = "riemann.piecewise-carrier-fixed-vector.v1"
GATE_SCHEMA = "riemann.one-direction-schur-target.v1"
VERIFY_SCHEMA = "riemann.one-direction-schur-target.verification.v1"

EXPECTED_VECTOR = "3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297"
EXPECTED_PARAMETER = "ac28f01b3804426fb19275c7cf0588226292d848b7b4d62bb983fd9ac7ad3e34"
EXPECTED_NORMALIZATION = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"
EXPECTED_COUNTS = {
    "prime_count": 4_118_054_813,
    "higher_prime_power_count": 28_156,
    "total_terms": 4_118_082_969,
    "shards": 50,
    "total_segments": 5000,
    "higher_power_streams": 1,
}


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
            raise CertificateError(f"{name} is not a base-10 integer") from exc
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
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(raw, dict):
        raise CertificateError(f"{path}: root must be an object")
    return raw


def verify(verdict: dict[str, Any], gate: dict[str, Any]) -> dict[str, Any]:
    if verdict.get("schema") != VERDICT_SCHEMA:
        raise CertificateError("wrong fixed-vector verdict schema")
    if verdict.get("verdict") != "CERTIFIED_POSITIVE_FIXED_VECTOR":
        raise CertificateError("source verdict is not CERTIFIED_POSITIVE_FIXED_VECTOR")
    if verdict.get("certified_positive") is not True:
        raise CertificateError("source positive flag is missing")
    if verdict.get("certified_negative") is not False:
        raise CertificateError("source negative flag is inconsistent")

    for key, expected in (
        ("vector_sha256", EXPECTED_VECTOR),
        ("parameter_sha256", EXPECTED_PARAMETER),
        ("normalization_sha256", EXPECTED_NORMALIZATION),
    ):
        if verdict.get(key) != expected:
            raise CertificateError(f"source {key} mismatch")

    coverage = verdict.get("coverage")
    if not isinstance(coverage, dict):
        raise CertificateError("source coverage must be an object")
    for key, expected in EXPECTED_COUNTS.items():
        if parse_int(coverage.get(key), f"coverage.{key}") != expected:
            raise CertificateError(f"coverage.{key} mismatch")

    interval = verdict.get("full_exact_quadratic_interval")
    if not isinstance(interval, dict):
        raise CertificateError("missing full exact quadratic interval")
    raw_lower = parse_fraction(interval.get("lower"), "full_interval.lower")
    raw_upper = parse_fraction(interval.get("upper"), "full_interval.upper")
    if raw_lower <= 0 or raw_lower > raw_upper:
        raise CertificateError("source full interval is not strictly positive")
    norm = parse_fraction(verdict.get("vector_norm_squared"), "vector_norm_squared")
    if norm <= 0:
        raise CertificateError("vector norm must be positive")
    normalized_lower = raw_lower / norm

    if gate.get("schema") != GATE_SCHEMA:
        raise CertificateError("wrong gate schema")
    if gate.get("gate_status") != "CONDITIONAL_TARGETS_NOT_YET_PROVED":
        raise CertificateError(
            "gate_status must explicitly say CONDITIONAL_TARGETS_NOT_YET_PROVED"
        )
    if gate.get("claims_whole_matrix_certificate") is not False:
        raise CertificateError("conditional gate must not claim a whole-matrix certificate")

    a_baseline = parse_fraction(gate.get("directional_baseline"), "directional_baseline")
    beta = parse_fraction(gate.get("complement_lower_target"), "complement_lower_target")
    residual = parse_fraction(gate.get("residual_upper_target"), "residual_upper_target")
    delta = parse_fraction(gate.get("operator_moat_target"), "operator_moat_target")
    if min(a_baseline, beta, residual, delta) < 0:
        raise CertificateError("all target quantities must be nonnegative")
    if not normalized_lower > a_baseline:
        raise CertificateError("the fixed direction does not clear the declared baseline")
    if not beta > delta:
        raise CertificateError("complement target must exceed operator moat")

    coarse_margin = a_baseline * (beta - delta) - (residual + delta) ** 2
    actual_margin = normalized_lower * (beta - delta) - (residual + delta) ** 2
    if coarse_margin <= 0:
        raise CertificateError("declared coarse Schur targets do not imply positivity")
    if actual_margin <= 0:
        raise CertificateError("actual fixed-direction lower endpoint does not clear gate")

    source_body = dict(verdict)
    source_sha = canonical_sha(source_body)
    result: dict[str, Any] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": "CONDITIONAL_WHOLE_MATRIX_TARGET_GATE_VERIFIED",
        "source": {
            "schema": VERDICT_SCHEMA,
            "canonical_sha256": source_sha,
            "vector_sha256": EXPECTED_VECTOR,
            "parameter_sha256": EXPECTED_PARAMETER,
            "normalization_sha256": EXPECTED_NORMALIZATION,
            "coverage": EXPECTED_COUNTS,
        },
        "fixed_direction": {
            "raw_lower": fraction_json(raw_lower),
            "raw_upper": fraction_json(raw_upper),
            "norm_squared": fraction_json(norm),
            "normalized_lower": fraction_json(normalized_lower),
            "declared_baseline": fraction_json(a_baseline),
            "clears_baseline": True,
        },
        "conditional_targets": {
            "complement_lower": fraction_json(beta),
            "residual_upper": fraction_json(residual),
            "operator_moat_upper": fraction_json(delta),
            "coarse_schur_margin": fraction_json(coarse_margin),
            "actual_endpoint_schur_margin": fraction_json(actual_margin),
        },
        "unproved_gates": [
            "complement lower bound for the chosen reference matrix",
            "normalized reference residual bound",
            "complete operator-norm distance from the exact matrix",
        ],
        "proof_boundary": (
            "The X-2805 fixed-direction interval and the displayed rational Schur "
            "implication are checked exactly.  This artifact deliberately does not "
            "assert that beta, residual, or operator targets have been proved."
        ),
    }
    result["verification_sha256"] = canonical_sha(result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("verdict", type=Path)
    parser.add_argument("gate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify(load_json(args.verdict), load_json(args.gate))
        code = 0
    except CertificateError as exc:
        result = {
            "schema": VERIFY_SCHEMA,
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
