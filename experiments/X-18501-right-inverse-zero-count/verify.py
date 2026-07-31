#!/usr/bin/env python3
"""Exact verifier for the selected-zero right-inverse count certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x18501-right-inverse-zero-count.v1"


class CertificateError(ValueError):
    pass


def rational(raw: Any, name: str) -> Fraction:
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
    raise CertificateError(f"bad rational at {name}")


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw or not all(isinstance(row, list) for row in raw):
        raise CertificateError(f"{name} must be a nonempty matrix")
    out = [
        [rational(value, f"{name}[{i}][{j}]") for j, value in enumerate(row)]
        for i, row in enumerate(raw)
    ]
    width = len(out[0])
    if width == 0 or any(len(row) != width for row in out):
        raise CertificateError(f"{name} is ragged or empty")
    return out


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def mat_mul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise CertificateError(f"matrix multiplication mismatch: {(ar, ac)} x {(br, bc)}")
    bt = transpose(b)
    return [
        [sum((x * y for x, y in zip(row, col)), Fraction()) for col in bt]
        for row in a
    ]


def mat_add(
    a: list[list[Fraction]],
    b: list[list[Fraction]],
    b_scale: Fraction = Fraction(1),
) -> list[list[Fraction]]:
    if shape(a) != shape(b):
        raise CertificateError("matrix addition dimension mismatch")
    return [
        [x + b_scale * y for x, y in zip(row_a, row_b)]
        for row_a, row_b in zip(a, b)
    ]


def scale(a: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * value for value in row] for row in a]


def identity(n: int) -> list[list[Fraction]]:
    if n <= 0:
        raise CertificateError("identity dimension must be positive")
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def zeros(rows: int, cols: int) -> list[list[Fraction]]:
    return [[Fraction() for _ in range(cols)] for _ in range(rows)]


def require_equal(a: list[list[Fraction]], b: list[list[Fraction]], name: str) -> None:
    if a != b:
        raise CertificateError(f"{name} failed")


def require_square_symmetric(a: list[list[Fraction]], name: str) -> None:
    rows, cols = shape(a)
    if rows != cols:
        raise CertificateError(f"{name} must be square")
    for i in range(rows):
        for j in range(i):
            if a[i][j] != a[j][i]:
                raise CertificateError(f"{name} is not symmetric")


def ldl_pivots(a: list[list[Fraction]], *, strict: bool) -> list[Fraction]:
    require_square_symmetric(a, "Loewner matrix")
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
            raise CertificateError(f"Loewner failure at pivot {i}: {pivot}")
        pivots.append(pivot)
        for j in range(i + 1, n):
            residual = a[j][i] - sum(
                (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)),
                Fraction(),
            )
            if pivot == 0:
                if residual != 0:
                    raise CertificateError("zero pivot with nonzero residual column")
                lower[j][i] = Fraction()
            else:
                lower[j][i] = residual / pivot
    return pivots


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    require_square_symmetric(a, "matrix to invert")
    n = len(a)
    aug = [a[i][:] + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot_row = next((row for row in range(col, n) if aug[row][col] != 0), None)
        if pivot_row is None:
            raise CertificateError("singular matrix")
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        pivot = aug[col][col]
        aug[col] = [value / pivot for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA}")

    g = matrix(data.get("metric_gram"), "metric_gram")
    v = matrix(data.get("selected_evaluation"), "selected_evaluation")
    c = matrix(data.get("right_inverse"), "right_inverse")
    r = matrix(data.get("kernel_basis"), "kernel_basis")
    k_full = matrix(data.get("full_certified_zero_gram"), "full_certified_zero_gram")

    n, n2 = shape(g)
    q, vn = shape(v)
    cn, cq = shape(c)
    rn, d = shape(r)
    if n != n2 or vn != n or cn != n or cq != q or rn != n:
        raise CertificateError("incompatible metric/evaluation/right-inverse/kernel dimensions")
    if d + q != n:
        raise CertificateError("kernel dimension plus evaluation rank must equal ambient dimension")
    if shape(k_full) != (n, n):
        raise CertificateError("full certified-zero Gram has wrong size")

    metric_pivots = ldl_pivots(g, strict=True)
    require_square_symmetric(k_full, "full_certified_zero_gram")

    require_equal(mat_mul(v, c), identity(q), "right-inverse identity")
    require_equal(mat_mul(v, r), zeros(q, d), "kernel basis condition")
    kernel_metric = mat_mul(transpose(r), mat_mul(g, r))
    kernel_pivots = ldl_pivots(kernel_metric, strict=True)

    kernel_metric_inv = inverse(kernel_metric)
    projection_coeff = mat_mul(kernel_metric_inv, mat_mul(transpose(r), mat_mul(g, c)))
    c0 = mat_add(c, mat_mul(r, projection_coeff), Fraction(-1))
    require_equal(mat_mul(v, c0), identity(q), "orthogonalized right-inverse identity")
    require_equal(mat_mul(transpose(r), mat_mul(g, c0)), zeros(d, q), "G-orthogonality")

    c0_metric = mat_mul(transpose(c0), mat_mul(g, c0))
    c0_metric_pivots = ldl_pivots(c0_metric, strict=True)

    lambda_upper = rational(data.get("right_inverse_gram_upper"), "right_inverse_gram_upper")
    if lambda_upper <= 0:
        raise CertificateError("right_inverse_gram_upper must be positive")
    lambda_slack = mat_add(scale(identity(q), lambda_upper), c0_metric, Fraction(-1))
    lambda_slack_pivots = ldl_pivots(lambda_slack, strict=False)

    selected_gram = mat_mul(transpose(v), v)
    domination = mat_add(k_full, selected_gram, Fraction(-1))
    domination_pivots = ldl_pivots(domination, strict=False)

    tail_budget = rational(data.get("omitted_zero_tail_budget"), "omitted_zero_tail_budget")
    beta = rational(data.get("beta"), "beta")
    if tail_budget < 0 or beta <= 0:
        raise CertificateError("tail budget must be nonnegative and beta positive")
    threshold = tail_budget + beta
    if threshold * lambda_upper >= 1:
        raise CertificateError("threshold does not lie below the right-inverse spectral gap")

    selected_complement_floor = mat_add(
        mat_mul(transpose(c0), mat_mul(selected_gram, c0)),
        scale(c0_metric, threshold),
        Fraction(-1),
    )
    selected_floor_pivots = ldl_pivots(selected_complement_floor, strict=True)

    full_complement_floor = mat_add(
        mat_mul(transpose(c0), mat_mul(k_full, c0)),
        scale(c0_metric, threshold),
        Fraction(-1),
    )
    full_floor_pivots = ldl_pivots(full_complement_floor, strict=True)

    return {
        "verified": True,
        "schema": SCHEMA,
        "ambient_dimension": n,
        "selected_zero_coordinates": q,
        "count_upper_bound": d,
        "threshold": fraction_json(threshold),
        "right_inverse_gram_upper": fraction_json(lambda_upper),
        "spectral_gap_lower": fraction_json(Fraction(1, 1) / lambda_upper),
        "metric_ldl_pivots": [fraction_json(x) for x in metric_pivots],
        "kernel_metric_ldl_pivots": [fraction_json(x) for x in kernel_pivots],
        "orthogonal_right_inverse_metric_ldl_pivots": [fraction_json(x) for x in c0_metric_pivots],
        "right_inverse_bound_ldl_pivots": [fraction_json(x) for x in lambda_slack_pivots],
        "zero_gram_domination_ldl_pivots": [fraction_json(x) for x in domination_pivots],
        "selected_complement_floor_ldl_pivots": [fraction_json(x) for x in selected_floor_pivots],
        "full_complement_floor_ldl_pivots": [fraction_json(x) for x in full_floor_pivots],
        "verdict": "CERTIFIED_SELECTED_ZERO_COUNT_AT_MOST_KERNEL_DIMENSION",
        "proof_object_sha256": canonical_sha256(data),
        "proof_boundary": (
            "Exact finite metric/right-inverse/count arithmetic only. "
            "The selected zero provenance, full-zero Gram enclosure, omitted-zero tail budget, "
            "and complete-low-packet capture remain external analytic gates."
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
