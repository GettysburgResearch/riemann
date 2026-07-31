#!/usr/bin/env python3
"""Exact verifier for canonical weighted-deficit complement augmentation."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x18901-deficit-complement.v1"


class CertificateError(ValueError):
    pass


def q(raw: Any, name: str) -> Fraction:
    if isinstance(raw, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(raw, int):
        return Fraction(raw)
    if isinstance(raw, dict):
        num = raw.get("numerator")
        den = raw.get("denominator")
        if (
            isinstance(num, int)
            and not isinstance(num, bool)
            and isinstance(den, int)
            and not isinstance(den, bool)
            and den > 0
        ):
            return Fraction(num, den)
    raise CertificateError(f"invalid rational at {name}")


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw or not all(isinstance(row, list) for row in raw):
        raise CertificateError(f"{name} must be a nonempty matrix")
    width = len(raw[0])
    if width == 0 or any(len(row) != width for row in raw):
        raise CertificateError(f"{name} must be non-ragged with positive width")
    return [[q(value, f"{name}[{i}][{j}]") for j, value in enumerate(row)] for i, row in enumerate(raw)]


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise CertificateError(f"matrix multiplication mismatch: {(ar, ac)} x {(br, bc)}")
    bt = transpose(b)
    return [
        [sum((x * y for x, y in zip(row, col)), Fraction()) for col in bt]
        for row in a
    ]


def add(a: list[list[Fraction]], b: list[list[Fraction]], scale_b: Fraction = Fraction(1)) -> list[list[Fraction]]:
    if shape(a) != shape(b):
        raise CertificateError("matrix addition dimension mismatch")
    return [[x + scale_b * y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(a: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in a]


def concat_columns(*blocks: list[list[Fraction]]) -> list[list[Fraction]]:
    if not blocks:
        raise CertificateError("no blocks to concatenate")
    n = len(blocks[0])
    if any(len(block) != n for block in blocks):
        raise CertificateError("basis row dimensions differ")
    return [sum((block[i] for block in blocks), []) for i in range(n)]


def restrict(a: list[list[Fraction]], basis: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(transpose(basis), matmul(a, basis))


def cross(a: list[list[Fraction]], left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(transpose(left), matmul(a, right))


def zero_matrix(a: list[list[Fraction]], name: str) -> None:
    if any(value != 0 for row in a for value in row):
        raise CertificateError(f"{name} is not exactly zero")


def require_symmetric(a: list[list[Fraction]], name: str) -> None:
    n, m = shape(a)
    if n != m:
        raise CertificateError(f"{name} must be square")
    for i in range(n):
        for j in range(i):
            if a[i][j] != a[j][i]:
                raise CertificateError(f"{name} is not symmetric")


def ldl_pivots(a: list[list[Fraction]], *, strict: bool, name: str) -> list[Fraction]:
    require_symmetric(a, name)
    n = len(a)
    lower = [[Fraction() for _ in range(n)] for _ in range(n)]
    pivots: list[Fraction] = []
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivot = a[i][i] - sum(
            (lower[i][k] * lower[i][k] * pivots[k] for k in range(i)),
            Fraction(),
        )
        if pivot < 0 or (strict and pivot == 0):
            relation = "positive definite" if strict else "positive semidefinite"
            raise CertificateError(f"{name} is not {relation}: pivot {i} is {pivot}")
        pivots.append(pivot)
        for j in range(i + 1, n):
            residual = a[j][i] - sum(
                (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)),
                Fraction(),
            )
            if pivot == 0:
                if residual != 0:
                    raise CertificateError(f"{name}: zero pivot {i} has nonzero residual")
                lower[j][i] = Fraction()
            else:
                lower[j][i] = residual / pivot
    return pivots


def fraction_json(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA}")

    metric = matrix(data.get("metric"), "metric")
    operator = matrix(data.get("operator"), "operator")
    deficit = matrix(data.get("deficit"), "deficit")
    u0 = matrix(data.get("initial_packet_basis"), "initial_packet_basis")
    w = matrix(data.get("augmentation_basis"), "augmentation_basis")
    c = matrix(data.get("complement_basis"), "complement_basis")

    n, n2 = shape(metric)
    if n != n2:
        raise CertificateError("metric must be square")
    for a, name in ((metric, "metric"), (operator, "operator"), (deficit, "deficit")):
        if shape(a) != (n, n):
            raise CertificateError(f"{name} must have shape {(n, n)}")
        require_symmetric(a, name)
    for basis, name in ((u0, "initial packet"), (w, "augmentation"), (c, "complement")):
        if len(basis) != n:
            raise CertificateError(f"{name} has wrong ambient row dimension")

    metric_pivots = ldl_pivots(metric, strict=True, name="metric")
    deficit_pivots = ldl_pivots(deficit, strict=False, name="deficit")

    g = q(data.get("lower_model_level"), "lower_model_level")
    gamma = q(data.get("target_floor"), "target_floor")
    if not (g > gamma > 0):
        raise CertificateError("require lower_model_level > target_floor > 0")
    theta = g - gamma

    lower_model = add(add(operator, scale(metric, g), Fraction(-1)), deficit)
    lower_model_pivots = ldl_pivots(lower_model, strict=False, name="operator lower-model slack")

    zero_matrix(cross(metric, u0, w), "initial/augmentation metric cross")
    zero_matrix(cross(metric, u0, c), "initial/complement metric cross")
    zero_matrix(cross(metric, w, c), "augmentation/complement metric cross")

    u0_gram_pivots = ldl_pivots(restrict(metric, u0), strict=True, name="initial packet Gram")
    w_gram_pivots = ldl_pivots(restrict(metric, w), strict=True, name="augmentation Gram")
    c_gram_pivots = ldl_pivots(restrict(metric, c), strict=True, name="complement Gram")

    total = concat_columns(u0, w, c)
    if shape(total) != (n, n):
        raise CertificateError("basis dimensions do not sum to the ambient dimension")
    total_gram_pivots = ldl_pivots(restrict(metric, total), strict=True, name="complete basis Gram")

    zero_matrix(cross(deficit, w, c), "deficit high/safe cross")
    high_slack = add(restrict(deficit, w), scale(restrict(metric, w), theta), Fraction(-1))
    safe_slack = add(scale(restrict(metric, c), theta), restrict(deficit, c), Fraction(-1))
    high_pivots = ldl_pivots(high_slack, strict=True, name="augmentation high-deficit slack")
    safe_pivots = ldl_pivots(safe_slack, strict=False, name="complement safe-deficit slack")

    final_floor = add(restrict(operator, c), scale(restrict(metric, c), gamma), Fraction(-1))
    final_floor_pivots = ldl_pivots(final_floor, strict=False, name="final complement floor")

    return {
        "verified": True,
        "schema": SCHEMA,
        "ambient_dimension": n,
        "initial_packet_dimension": shape(u0)[1],
        "augmentation_rank": shape(w)[1],
        "complement_dimension": shape(c)[1],
        "danger_threshold": fraction_json(theta),
        "target_floor": fraction_json(gamma),
        "metric_ldl_pivots": [fraction_json(x) for x in metric_pivots],
        "deficit_ldl_pivots": [fraction_json(x) for x in deficit_pivots],
        "lower_model_slack_ldl_pivots": [fraction_json(x) for x in lower_model_pivots],
        "initial_packet_gram_ldl_pivots": [fraction_json(x) for x in u0_gram_pivots],
        "augmentation_gram_ldl_pivots": [fraction_json(x) for x in w_gram_pivots],
        "complement_gram_ldl_pivots": [fraction_json(x) for x in c_gram_pivots],
        "complete_basis_gram_ldl_pivots": [fraction_json(x) for x in total_gram_pivots],
        "augmentation_high_deficit_ldl_pivots": [fraction_json(x) for x in high_pivots],
        "complement_safe_deficit_ldl_pivots": [fraction_json(x) for x in safe_pivots],
        "final_complement_floor_ldl_pivots": [fraction_json(x) for x in final_floor_pivots],
        "proof_object_sha256": canonical_sha256(data),
        "verdict": "CERTIFIED_CANONICAL_AUGMENTED_COMPLEMENT_FLOOR",
        "proof_boundary": (
            "Exact finite metric, lower-model, spectral-augmentation, and complement-floor "
            "arithmetic only. The complete lower symbol/deficit model and any assertion that "
            "the unaugmented cardinal-radical packet already contains the augmentation remain "
            "external analytic gates."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(raw)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
