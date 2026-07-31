#!/usr/bin/env python3
"""Exact verifier for the robust L-14319 certified-zero S-lemma floor."""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x14312-certified-zero-slemma.v1"
OUTPUT_SCHEMA = "riemann.x14312-certified-zero-slemma-verification.v1"
SYNTHETIC = "SYNTHETIC_MODEL"
PRODUCTION = "RIEMANN_WEIL_DIRECTED"
GATE = "CERTIFIED_RELATIVE_LOEWNER_AND_ZERO_FRAME"


class CertificateError(ValueError):
    """Raised whenever the proof object fails closed."""


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise CertificateError(f"{name} must be integer text") from exc
    raise CertificateError(f"{name} must be an integer")


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} must be rational text") from exc
    if not isinstance(value, dict) or set(value) != {"numerator", "denominator"}:
        raise CertificateError(
            f"{name} must be an integer, rational string, or exact fraction object"
        )
    numerator = exact_int(value["numerator"], f"{name}.numerator")
    denominator = exact_int(value["denominator"], f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    width = None
    out: list[list[Fraction]] = []
    for i, row in enumerate(raw):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        parsed = [rational(x, f"{name}[{i}][{j}]") for j, x in enumerate(row)]
        if width is None:
            width = len(parsed)
        elif len(parsed) != width:
            raise CertificateError(f"{name} is ragged")
        out.append(parsed)
    return out


def vector(raw: Any, name: str, n: int) -> list[Fraction]:
    if not isinstance(raw, list) or len(raw) != n:
        raise CertificateError(f"{name} must have length {n}")
    return [rational(x, f"{name}[{i}]") for i, x in enumerate(raw)]


def require_symmetric_square(value: list[list[Fraction]], name: str) -> None:
    n = len(value)
    if any(len(row) != n for row in value):
        raise CertificateError(f"{name} must be square")
    if any(value[i][j] != value[j][i] for i in range(n) for j in range(n)):
        raise CertificateError(f"{name} must be symmetric")


def add(*terms: tuple[Fraction, list[list[Fraction]]]) -> list[list[Fraction]]:
    if not terms:
        raise CertificateError("matrix sum is empty")
    n = len(terms[0][1])
    if any(len(m) != n or any(len(row) != n for row in m) for _, m in terms):
        raise CertificateError("matrix-sum dimension mismatch")
    return [
        [sum(scale * m[i][j] for scale, m in terms) for j in range(n)]
        for i in range(n)
    ]


def matvec(value: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    if len(value) != len(x) or any(len(row) != len(x) for row in value):
        raise CertificateError("matrix-vector dimension mismatch")
    return [sum(a * b for a, b in zip(row, x)) for row in value]


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    if len(x) != len(y):
        raise CertificateError("dot-product dimension mismatch")
    return sum(a * b for a, b in zip(x, y))


def ldl(
    value: list[list[Fraction]], name: str, *, strict: bool
) -> tuple[list[list[Fraction]], list[Fraction]]:
    """Exact unpivoted LDL for positive (semi)definiteness.

    For a zero pivot, all remaining entries in the transformed pivot column must
    vanish. This is the exact fail-closed condition for a PSD matrix.
    """
    require_symmetric_square(value, name)
    n = len(value)
    lower = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    pivots: list[Fraction] = []
    for j in range(n):
        pivot = value[j][j] - sum(
            lower[j][k] * lower[j][k] * pivots[k] for k in range(j)
        )
        if pivot < 0 or (strict and pivot == 0):
            raise CertificateError(f"{name} has invalid LDL pivot at index {j}")
        pivots.append(pivot)
        for i in range(j + 1, n):
            numerator = value[i][j] - sum(
                lower[i][k] * lower[j][k] * pivots[k] for k in range(j)
            )
            if pivot == 0:
                if numerator != 0:
                    raise CertificateError(
                        f"{name} has a nonzero column beneath zero pivot {j}"
                    )
                lower[i][j] = Fraction(0)
            else:
                lower[i][j] = numerator / pivot
    return lower, pivots


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def valid_sha(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(ch not in string.hexdigits for ch in value)
    ):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    classification = data.get("classification")
    if classification not in {SYNTHETIC, PRODUCTION}:
        raise CertificateError("unsupported classification")
    if classification == PRODUCTION:
        gate = data.get("analytic_gate")
        if not isinstance(gate, dict) or gate.get("status") != GATE:
            raise CertificateError("production certificate lacks the analytic gate")
        valid_sha(gate.get("sha256"), "analytic_gate.sha256")

    a0 = matrix(data.get("form_midpoint"), "form_midpoint")
    j0 = matrix(data.get("visibility_midpoint"), "visibility_midpoint")
    g = matrix(data.get("metric"), "metric")
    require_symmetric_square(a0, "form_midpoint")
    require_symmetric_square(j0, "visibility_midpoint")
    require_symmetric_square(g, "metric")
    n = len(g)
    if len(a0) != n or len(j0) != n:
        raise CertificateError("matrix dimensions differ")

    _, metric_pivots = ldl(g, "metric", strict=True)

    eps_a = rational(data.get("form_radius"), "form_radius")
    eps_j = rational(data.get("visibility_radius"), "visibility_radius")
    delta2 = rational(data.get("visibility_threshold_squared"), "visibility_threshold_squared")
    alpha = rational(data.get("multiplier"), "multiplier")
    floor = rational(data.get("claimed_visible_floor"), "claimed_visible_floor")
    if eps_a < 0 or eps_j < 0:
        raise CertificateError("relative Loewner radii must be nonnegative")
    if alpha < 0:
        raise CertificateError("multiplier must be nonnegative")

    slater = vector(data.get("slater_vector"), "slater_vector", n)
    if dot(slater, matvec(g, slater)) <= 0:
        raise CertificateError("slater_vector must be nonzero in the metric")
    robust_slater_matrix = add(
        (Fraction(1), j0), (-(delta2 + eps_j), g)
    )
    slater_margin = dot(slater, matvec(robust_slater_matrix, slater))
    if slater_margin <= 0:
        raise CertificateError("robust Slater condition failed")

    robust_loss = eps_a + alpha * eps_j
    lmi = add(
        (Fraction(1), a0),
        (-alpha, j0),
        (alpha * delta2 - robust_loss - floor, g),
    )
    _, lmi_pivots = ldl(lmi, "robust S-lemma floor LMI", strict=False)

    diagnostic_vector = data.get("global_negative_vector")
    global_negative_value: Fraction | None = None
    if diagnostic_vector is not None:
        x = vector(diagnostic_vector, "global_negative_vector", n)
        denominator = dot(x, matvec(g, x))
        if denominator <= 0:
            raise CertificateError("global_negative_vector must be nonzero")
        global_negative_value = dot(x, matvec(a0, x)) / denominator

    proof_object = {
        "classification": classification,
        "dimension": n,
        "form_radius": fj(eps_a),
        "visibility_radius": fj(eps_j),
        "visibility_threshold_squared": fj(delta2),
        "multiplier": fj(alpha),
        "claimed_visible_floor": fj(floor),
        "robust_loss": fj(robust_loss),
        "slater_margin": fj(slater_margin),
        "metric_pivots": [fj(x) for x in metric_pivots],
        "lmi_pivots": [fj(x) for x in lmi_pivots],
    }
    result: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "analytic_claim": "L-14319",
        "dimension": n,
        "visible_floor_certified": fj(floor),
        "multiplier": fj(alpha),
        "visibility_threshold_squared": fj(delta2),
        "form_radius": fj(eps_a),
        "visibility_radius": fj(eps_j),
        "robust_loss": fj(robust_loss),
        "robust_slater_margin": fj(slater_margin),
        "metric_pivots": [fj(x) for x in metric_pivots],
        "floor_lmi_pivots": [fj(x) for x in lmi_pivots],
        "exact_proof_object_sha256": canonical_sha(proof_object),
        "verdict": "CERTIFIED_VISIBLE_CONE_LOWER_FLOOR",
        "proof_boundary": (
            "Exact rational verification of the robust S-lemma implication. "
            "A Riemann-Weil interpretation additionally requires the typed "
            "relative-Loewner and certified-zero-frame provenance gate."
        ),
    }
    if global_negative_value is not None:
        result["midpoint_global_diagnostic_rayleigh"] = fj(global_negative_value)
    return result


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
