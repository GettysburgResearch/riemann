#!/usr/bin/env python3
"""Exact checker for leakage normalization, global radical frame, and alias ledger."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x16203-normalization-frame.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer, not Boolean")
    return value


def frac(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not a rational") from exc
    if isinstance(value, list) and len(value) == 2:
        p = integer(value[0], name + "[0]")
        q = integer(value[1], name + "[1]")
        if q == 0:
            raise CertificateError(f"{name} has zero denominator")
        return Fraction(p, q)
    raise CertificateError(f"{name} must be int, fraction string, or [p,q]")


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise CertificateError("determinant requires square matrix")
    a = [row[:] for row in matrix]
    sign = 1
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign *= -1
        pv = a[col][col]
        out *= pv
        for r in range(col + 1, n):
            if not a[r][col]:
                continue
            factor = a[r][col] / pv
            for c in range(col + 1, n):
                a[r][c] -= factor * a[col][c]
    return sign * out


def principal_submatrix(matrix: list[list[Fraction]], indices: tuple[int, ...]) -> list[list[Fraction]]:
    return [[matrix[i][j] for j in indices] for i in indices]


def is_psd(matrix: list[list[Fraction]]) -> bool:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        return False
    for size in range(1, n + 1):
        for indices in combinations(range(n), size):
            if determinant(principal_submatrix(matrix, indices)) < 0:
                return False
    return True


def matmul_transpose(columns: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(columns)
    cols = len(columns[0]) if rows else 0
    if any(len(row) != cols for row in columns):
        raise CertificateError("ragged synthesis matrix")
    return [
        [sum(columns[r][i] * columns[r][j] for r in range(rows)) for j in range(cols)]
        for i in range(cols)
    ]


def identity(n: int, scale: Fraction = Fraction(1)) -> list[list[Fraction]]:
    return [[scale if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def subtract(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def serialize_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_digest(payload: dict[str, Any]) -> str:
    stripped = dict(payload)
    stripped.pop("proof_object_sha256", None)
    data = json.dumps(stripped, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")

    chi = frac(payload.get("chi"), "chi")
    if not (0 < chi < 1):
        raise CertificateError("chi must lie strictly between zero and one")
    positive = payload.get("positive_ray_components")
    negative = payload.get("negative_ray_components")
    if not isinstance(positive, list) or not isinstance(negative, list):
        raise CertificateError("leakage components must be lists")
    pos = [frac(v, f"positive[{i}]") for i, v in enumerate(positive)]
    neg = [frac(v, f"negative[{i}]") for i, v in enumerate(negative)]
    pos_sq = sum(v * v for v in pos)
    neg_sq = sum(v * v for v in neg)
    total_sq = pos_sq + neg_sq
    if pos_sq != neg_sq:
        raise CertificateError("even leakage rays do not have equal energy")
    if total_sq != 1 - chi * chi:
        raise CertificateError("leakage norm does not equal 1-chi^2")
    d = 1 - chi
    expected_ray = d * (1 + chi) / 2
    if pos_sq != expected_ray:
        raise CertificateError("positive-ray amplitude is not d(1+chi)/2")

    raw_d = payload.get("defects")
    raw_q = payload.get("point_values")
    if not isinstance(raw_d, list) or not isinstance(raw_q, list):
        raise CertificateError("defects and point_values must be lists")
    defects = [frac(v, f"defects[{i}]") for i, v in enumerate(raw_d)]
    q = [frac(v, f"point_values[{i}]") for i, v in enumerate(raw_q)]
    if len(defects) != len(q) or len(defects) < 3:
        raise CertificateError("frame lists have incompatible lengths")
    if any(defects[i] >= defects[i + 1] for i in range(len(defects) - 1)):
        raise CertificateError("defects are not strictly increasing")
    if any(v == 0 for v in q):
        raise CertificateError("point value is zero")
    h = len(defects) - 1
    free = h - 1
    denominator = defects[h] - defects[0]
    W = [[Fraction(0) for _ in range(free)] for _ in range(h + 1)]
    A: list[Fraction] = []
    B: list[Fraction] = []
    for j in range(1, h):
        a = (defects[h] - defects[j]) / denominator
        b = (defects[j] - defects[0]) / denominator
        A.append(a)
        B.append(b)
        col = j - 1
        W[0][col] = -a
        W[j][col] = 1
        W[h][col] = -b
        if sum(W[row][col] for row in range(h + 1)) != 0:
            raise CertificateError("zeroth radical constraint failed")
        if sum(defects[row] * W[row][col] for row in range(h + 1)) != 0:
            raise CertificateError("defect radical constraint failed")

    gram_x = matmul_transpose(W)
    if not is_psd(subtract(gram_x, identity(free))):
        raise CertificateError("W^T W is not >= I")
    if not is_psd(subtract(identity(free, Fraction(h)), gram_x)):
        raise CertificateError("W^T W is not <= H I")

    U = [[W[row][col] / q[row] for col in range(free)] for row in range(h + 1)]
    gram_c = matmul_transpose(U)
    q_abs = [abs(v) for v in q]
    q_min, q_max = min(q_abs), max(q_abs)
    lower = Fraction(1, 1) / (q_max * q_max)
    upper = Fraction(h, 1) / (q_min * q_min)
    if not is_psd(subtract(gram_c, identity(free, lower))):
        raise CertificateError("coefficient-frame lower bound failed")
    if not is_psd(subtract(identity(free, upper), gram_c)):
        raise CertificateError("coefficient-frame upper bound failed")

    endpoint = payload.get("endpoint_ledger")
    if not isinstance(endpoint, dict):
        raise CertificateError("endpoint_ledger must be an object")
    p = integer(endpoint.get("p"), "endpoint_ledger.p")
    if p <= 1:
        raise CertificateError("p must exceed one for absolute alias summation")
    derivative_l1 = frac(endpoint.get("derivative_l1_upper"), "derivative_l1_upper")
    zeta_tail = frac(endpoint.get("zeta_tail_upper"), "zeta_tail_upper")
    pi_lower = frac(endpoint.get("pi_lower"), "pi_lower")
    lam = frac(endpoint.get("lambda"), "lambda")
    v = frac(endpoint.get("v"), "v")
    if min(derivative_l1, zeta_tail, pi_lower, lam, v) <= 0:
        raise CertificateError("endpoint ledger bounds must be positive")
    point_bound = zeta_tail * derivative_l1 / ((2 * pi_lower * v) ** p)
    l2_sq_bound = (
        (zeta_tail * derivative_l1) ** 2
        / ((2 * pi_lower) ** (2 * p) * (2 * p - 1) * lam ** (2 * p - 1))
    )
    claimed_point = frac(endpoint.get("claimed_point_bound"), "claimed_point_bound")
    claimed_l2_sq = frac(endpoint.get("claimed_l2_sq_bound"), "claimed_l2_sq_bound")
    if claimed_point < point_bound:
        raise CertificateError("claimed point alias bound is understated")
    if claimed_l2_sq < l2_sq_bound:
        raise CertificateError("claimed L2 alias bound is understated")

    result = {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_NORMALIZATION_AND_FRAME_AUDIT",
        "leakage": {
            "chi": serialize_fraction(chi),
            "d": serialize_fraction(d),
            "positive_ray_norm_squared": serialize_fraction(pos_sq),
            "total_leakage_norm_squared": serialize_fraction(total_sq),
            "sqrt_d_ratio_squared": serialize_fraction(pos_sq / d),
        },
        "frame": {
            "ambient_dimension": h + 1,
            "radical_dimension": free,
            "A": [serialize_fraction(v) for v in A],
            "B": [serialize_fraction(v) for v in B],
            "x_frame_lower_squared": "1",
            "x_frame_upper_squared": str(h),
            "coefficient_frame_lower_squared": serialize_fraction(lower),
            "coefficient_frame_upper_squared": serialize_fraction(upper),
        },
        "endpoint_ledger": {
            "point_alias_bound": serialize_fraction(point_bound),
            "l2_alias_bound_squared": serialize_fraction(l2_sq_bound),
        },
        "proof_boundary": (
            "Finite exact arithmetic only. The certificate validates the algebraic "
            "normalization, radical-frame bounds, and endpoint-ledger formulas; it "
            "does not evaluate a production PSWF, zeta zero, or Weil form."
        ),
    }
    result["proof_object_sha256"] = canonical_digest(result)
    claimed_digest = payload.get("claimed_result_sha256")
    if claimed_digest is not None and claimed_digest != result["proof_object_sha256"]:
        raise CertificateError("claimed result digest mismatch")
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
