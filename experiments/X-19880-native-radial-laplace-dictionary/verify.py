#!/usr/bin/env python3
"""Exact finite regression for the native-to-radial Laplace dictionary.

The continuous theorem L-19880 is proved analytically in its claim card.  This
checker verifies a discrete geometric-Laplace analogue, source allocation,
interval additivity, and the common-column PSD slack with Fraction arithmetic.
It does not evaluate zeta and does not prove SONTR, NRMA, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x19880-native-radial-laplace-dictionary.v1"
OUTPUT_SCHEMA = "riemann.x19880-native-radial-laplace-verification.v1"


class CertificateError(ValueError):
    pass


def rat(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} must be rational text") from exc
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        n = value["numerator"]
        d = value["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise CertificateError(f"{name} fraction entries must not be Boolean")
        try:
            n_i = int(n)
            d_i = int(d)
        except (ValueError, TypeError) as exc:
            raise CertificateError(f"{name} fraction entries must be integers") from exc
        if d_i <= 0:
            raise CertificateError(f"{name}.denominator must be positive")
        return Fraction(n_i, d_i)
    raise CertificateError(f"{name} must be an exact rational")


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def zero_matrix(n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def add_scaled_outer(
    matrix: list[list[Fraction]], coefficient: Fraction, vector: list[Fraction]
) -> None:
    n = len(vector)
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise CertificateError("outer-product dimension mismatch")
    for i in range(n):
        for j in range(n):
            matrix[i][j] += coefficient * vector[i] * vector[j]


def subtract(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise CertificateError("matrix dimension mismatch")
    return [[x - y for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def ldl_psd(matrix: list[list[Fraction]], name: str) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise CertificateError(f"{name} must be nonempty and square")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise CertificateError(f"{name} must be symmetric")
    lower = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    pivots: list[Fraction] = []
    for j in range(n):
        pivot = matrix[j][j] - sum(
            lower[j][k] * lower[j][k] * pivots[k] for k in range(j)
        )
        if pivot < 0:
            raise CertificateError(f"{name} has negative LDL pivot at {j}")
        pivots.append(pivot)
        for i in range(j + 1, n):
            numerator = matrix[i][j] - sum(
                lower[i][k] * lower[j][k] * pivots[k] for k in range(j)
            )
            if pivot == 0:
                if numerator != 0:
                    raise CertificateError(
                        f"{name} has nonzero entry below zero pivot {j}"
                    )
                lower[i][j] = Fraction(0)
            else:
                lower[i][j] = numerator / pivot
    return pivots


def prime_power_base(n: int) -> int | None:
    """Return the unique prime base when n is a prime power, else None."""
    if n < 2:
        return None
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            while remaining % p == 0:
                remaining //= p
            if remaining != 1:
                return None
            return p
        p += 1 if p == 2 else 2
    return n


def radix_four_ancestors(q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    k = 0
    value = q
    while True:
        out.append((k, value))
        if value % 4 != 0:
            break
        value //= 4
        k += 1
    return out


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def matrix_json(matrix: list[list[Fraction]]) -> list[list[dict[str, str]]]:
    return [[fj(x) for x in row] for row in matrix]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")

    z = rat(data.get("geometric_parameter"), "geometric_parameter")
    if not 0 < z < 1:
        raise CertificateError("geometric_parameter must lie in (0,1)")

    interval_weights_raw = data.get("interval_weights")
    if not isinstance(interval_weights_raw, list) or not interval_weights_raw:
        raise CertificateError("interval_weights must be a nonempty list")
    interval_weights = [
        rat(value, f"interval_weights[{i}]")
        for i, value in enumerate(interval_weights_raw)
    ]
    if any(x < 0 for x in interval_weights):
        raise CertificateError("interval weights must be nonnegative")
    if sum(interval_weights) != 1:
        raise CertificateError("interval weights must sum exactly to one")

    modes = data.get("modes")
    if not isinstance(modes, list) or not modes:
        raise CertificateError("modes must be a nonempty list")

    dimension: int | None = None
    full: list[list[Fraction]] | None = None
    used: list[list[Fraction]] | None = None
    slack: list[list[Fraction]] | None = None
    mode_records: list[dict[str, Any]] = []

    for index, raw in enumerate(modes):
        if not isinstance(raw, dict):
            raise CertificateError(f"modes[{index}] must be an object")
        u_raw = raw.get("activation_index")
        if isinstance(u_raw, bool) or not isinstance(u_raw, int) or u_raw < 0:
            raise CertificateError(
                f"modes[{index}].activation_index must be a nonnegative integer"
            )
        u = u_raw
        ramp_weight = rat(raw.get("ramp_weight"), f"modes[{index}].ramp_weight")
        if ramp_weight <= 0:
            raise CertificateError("ramp weights must be positive")
        feature_raw = raw.get("feature")
        if not isinstance(feature_raw, list) or not feature_raw:
            raise CertificateError(f"modes[{index}].feature must be a nonempty list")
        feature = [
            rat(v, f"modes[{index}].feature[{j}]")
            for j, v in enumerate(feature_raw)
        ]
        if dimension is None:
            dimension = len(feature)
            full = zero_matrix(dimension)
            used = zero_matrix(dimension)
            slack = zero_matrix(dimension)
        elif len(feature) != dimension:
            raise CertificateError("all feature columns must have the same dimension")

        owners_raw = raw.get("owner_fractions")
        if not isinstance(owners_raw, list) or not owners_raw:
            raise CertificateError(f"modes[{index}].owner_fractions must be nonempty")
        owners = [
            rat(v, f"modes[{index}].owner_fractions[{j}]")
            for j, v in enumerate(owners_raw)
        ]
        if any(v < 0 for v in owners):
            raise CertificateError("owner fractions must be nonnegative")
        owner_total = sum(owners)
        if owner_total > 1:
            raise CertificateError("source owners over-allocate one native mode")

        transformed_full = ramp_weight * z**u
        transformed_used = transformed_full * owner_total
        transformed_slack = transformed_full * (1 - owner_total)

        assert full is not None and used is not None and slack is not None
        add_scaled_outer(full, transformed_full, feature)
        add_scaled_outer(used, transformed_used, feature)
        add_scaled_outer(slack, transformed_slack, feature)

        refined = [transformed_slack * weight for weight in interval_weights]
        if sum(refined) != transformed_slack:
            raise CertificateError("interval refinement failed")

        mode_records.append(
            {
                "activation_index": u,
                "ramp_weight": fj(ramp_weight),
                "geometric_laplace_value": fj(transformed_full),
                "owner_total": fj(owner_total),
                "used_value": fj(transformed_used),
                "slack_value": fj(transformed_slack),
                "interval_slack_values": [fj(v) for v in refined],
            }
        )

    assert dimension is not None and full is not None and used is not None and slack is not None
    reconstructed_slack = subtract(full, used)
    if reconstructed_slack != slack:
        raise CertificateError("full minus used does not equal the slack Gram")
    pivots = ldl_psd(slack, "slack Gram")

    claimed_raw = data.get("claimed_slack_matrix")
    if claimed_raw is not None:
        if not isinstance(claimed_raw, list) or len(claimed_raw) != dimension:
            raise CertificateError("claimed_slack_matrix has wrong dimension")
        claimed = [
            [rat(v, f"claimed_slack_matrix[{i}][{j}]") for j, v in enumerate(row)]
            for i, row in enumerate(claimed_raw)
        ]
        if any(len(row) != dimension for row in claimed):
            raise CertificateError("claimed_slack_matrix must be square")
        if claimed != slack:
            raise CertificateError("claimed_slack_matrix does not match the reconstructed Gram")

    radix_raw = data.get("radix_four_columns", [])
    if not isinstance(radix_raw, list):
        raise CertificateError("radix_four_columns must be a list")
    radix_records: list[dict[str, Any]] = []
    for i, raw in enumerate(radix_raw):
        if not isinstance(raw, dict):
            raise CertificateError(f"radix_four_columns[{i}] must be an object")
        q = raw.get("q")
        expected_zero = raw.get("expected_y4_zero")
        if isinstance(q, bool) or not isinstance(q, int) or q < 2:
            raise CertificateError(f"radix_four_columns[{i}].q must be an integer >=2")
        if not isinstance(expected_zero, bool):
            raise CertificateError(
                f"radix_four_columns[{i}].expected_y4_zero must be Boolean"
            )
        ancestors = radix_four_ancestors(q)
        visible = [
            {"power": k, "ordinary_column": value, "prime_base": prime_power_base(value)}
            for k, value in ancestors
            if prime_power_base(value) is not None
        ]
        actual_zero = len(visible) == 0
        if actual_zero != expected_zero:
            raise CertificateError(
                f"radix-four visibility mismatch for q={q}: expected {expected_zero}, got {actual_zero}"
            )
        radix_records.append(
            {
                "q": q,
                "expected_y4_zero": expected_zero,
                "ancestors": [
                    {"power": k, "ordinary_column": value} for k, value in ancestors
                ],
                "prime_power_ancestors": visible,
                "prime_radial_null_gauge": actual_zero,
            }
        )

    proof = {
        "geometric_parameter": fj(z),
        "interval_weights": [fj(v) for v in interval_weights],
        "dimension": dimension,
        "modes": mode_records,
        "full_matrix": matrix_json(full),
        "used_matrix": matrix_json(used),
        "slack_matrix": matrix_json(slack),
        "slack_ldl_pivots": [fj(v) for v in pivots],
        "radix_four_columns": radix_records,
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "analytic_claim": "L-19880",
        "classification": "SYNTHETIC_EXACT_DISCRETE_ANALOGUE",
        "dimension": dimension,
        "mode_count": len(modes),
        "geometric_parameter": fj(z),
        "interval_weights": [fj(v) for v in interval_weights],
        "modes": mode_records,
        "full_matrix": matrix_json(full),
        "used_matrix": matrix_json(used),
        "slack_matrix": matrix_json(slack),
        "slack_ldl_pivots": [fj(v) for v in pivots],
        "radix_four_columns": radix_records,
        "proof_object_sha256": canonical_sha(proof),
        "verdict": "PASS_EXACT_NATIVE_RADIAL_DICTIONARY_ANALOGUE",
        "proof_boundary": (
            "Fraction-only regression of the geometric-Laplace ramp identity, "
            "source ownership, interval refinement, and common-column PSD slack. "
            "It does not certify the continuous integral theorem, SONTR, NRMA, or RH."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(raw)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
