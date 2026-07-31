#!/usr/bin/env python3
"""Exact verifier for X-20501: conditional simple-line frame on the complete kernel.

Standard library only. All arithmetic uses fractions.Fraction.
The retained proof object is real-rational; the theorem permits complex Hermitian data.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


class VerificationError(ValueError):
    """Fail-closed certificate rejection."""


def reject(condition: bool, message: str) -> None:
    if condition:
        raise VerificationError(message)


def parse_fraction(value: Any) -> Fraction:
    reject(isinstance(value, bool), "booleans are not rational numbers")
    if isinstance(value, int):
        return Fraction(value)
    reject(not isinstance(value, str), f"expected rational string, got {type(value).__name__}")
    try:
        return Fraction(value.strip())
    except (ValueError, ZeroDivisionError) as exc:
        raise VerificationError(f"invalid rational {value!r}") from exc


Matrix = list[list[Fraction]]


def parse_matrix(raw: Any, *, label: str, nonempty: bool = True) -> Matrix:
    reject(not isinstance(raw, list), f"{label} must be a matrix")
    if nonempty:
        reject(not raw, f"{label} must be nonempty")
    if not raw:
        return []
    reject(any(not isinstance(row, list) for row in raw), f"{label} rows must be lists")
    width = len(raw[0])
    reject(width == 0, f"{label} must have nonempty rows")
    reject(any(len(row) != width for row in raw), f"{label} is ragged")
    return [[parse_fraction(x) for x in row] for row in raw]


def shape(a: Matrix) -> tuple[int, int]:
    return (len(a), len(a[0]) if a else 0)


def zeros(m: int, n: int) -> Matrix:
    return [[Fraction(0) for _ in range(n)] for _ in range(m)]


def identity(n: int) -> Matrix:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def transpose(a: Matrix) -> Matrix:
    m, n = shape(a)
    return [[a[i][j] for i in range(m)] for j in range(n)]


def add(a: Matrix, b: Matrix) -> Matrix:
    reject(shape(a) != shape(b), "matrix addition shape mismatch")
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    reject(shape(a) != shape(b), "matrix subtraction shape mismatch")
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    ma, na = shape(a)
    mb, nb = shape(b)
    reject(na != mb, f"matrix multiplication mismatch {shape(a)} x {shape(b)}")
    return [[sum(a[i][k] * b[k][j] for k in range(na)) for j in range(nb)] for i in range(ma)]


def hstack(a: Matrix, b: Matrix) -> Matrix:
    reject(len(a) != len(b), "horizontal block row mismatch")
    return [ra + rb for ra, rb in zip(a, b)]


def vstack(a: Matrix, b: Matrix) -> Matrix:
    if a and b:
        reject(len(a[0]) != len(b[0]), "vertical block column mismatch")
    return [row[:] for row in a] + [row[:] for row in b]


def block_diag(a: Matrix, b: Matrix) -> Matrix:
    ma, na = shape(a)
    mb, nb = shape(b)
    out = zeros(ma + mb, na + nb)
    for i in range(ma):
        for j in range(na):
            out[i][j] = a[i][j]
    for i in range(mb):
        for j in range(nb):
            out[ma + i][na + j] = b[i][j]
    return out


def symmetric(a: Matrix) -> bool:
    m, n = shape(a)
    return m == n and all(a[i][j] == a[j][i] for i in range(n) for j in range(n))


def determinant(a: Matrix) -> Fraction:
    n, m = shape(a)
    reject(n != m, "determinant requires square matrix")
    work = [row[:] for row in a]
    det = Fraction(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            det = -det
        pv = work[col][col]
        det *= pv
        for row in range(col + 1, n):
            if work[row][col] == 0:
                continue
            factor = work[row][col] / pv
            for k in range(col, n):
                work[row][k] -= factor * work[col][k]
    return det


def inverse(a: Matrix) -> Matrix:
    n, m = shape(a)
    reject(n != m, "inverse requires square matrix")
    aug = [a[i][:] + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col] != 0), None)
        reject(pivot is None, "matrix is singular")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [aug[row][k] - factor * aug[col][k] for k in range(2 * n)]
    return [row[n:] for row in aug]


def principal_submatrix(a: Matrix, indices: tuple[int, ...]) -> Matrix:
    return [[a[i][j] for j in indices] for i in indices]


def is_psd(a: Matrix) -> bool:
    if not symmetric(a):
        return False
    n, _ = shape(a)
    for size in range(1, n + 1):
        for indices in itertools.combinations(range(n), size):
            if determinant(principal_submatrix(a, indices)) < 0:
                return False
    return True


def is_pd(a: Matrix) -> bool:
    if not symmetric(a):
        return False
    n, _ = shape(a)
    for k in range(1, n + 1):
        if determinant([row[:k] for row in a[:k]]) <= 0:
            return False
    return True


def restrict(form: Matrix, basis: Matrix) -> Matrix:
    return matmul(transpose(basis), matmul(form, basis))


def matrix_equal(a: Matrix, b: Matrix, message: str) -> None:
    reject(a != b, message)


def fraction_json(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def matrix_json(a: Matrix) -> list[list[dict[str, int]]]:
    return [[fraction_json(x) for x in row] for row in a]


def canonical_json_bytes(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def verify(cert: dict[str, Any]) -> dict[str, Any]:
    expected = {
        "schema", "metric_R", "metric_W", "evaluation_Z", "evaluation_Y",
        "residual_U", "complement", "claimed",
    }
    reject(set(cert) != expected, "certificate top-level fields mismatch")
    reject(cert["schema"] != "riemann.x20501-conditional-line-frame.v1", "unsupported schema")

    g_r = parse_matrix(cert["metric_R"], label="metric_R")
    g_w = parse_matrix(cert["metric_W"], label="metric_W")
    reject(not is_pd(g_r) or not is_pd(g_w), "packet metrics must be positive definite")
    r, _ = shape(g_r)
    w, _ = shape(g_w)

    z = cert["evaluation_Z"]
    reject(not isinstance(z, dict) or set(z) != {"R", "W"}, "evaluation_Z fields mismatch")
    a = parse_matrix(z["R"], label="evaluation_Z.R")
    b = parse_matrix(z["W"], label="evaluation_Z.W")
    reject(shape(a) != (w, r) or shape(b) != (w, w), "first frame dimensions mismatch")
    b_inv = inverse(b)

    y = cert["evaluation_Y"]
    reject(not isinstance(y, dict) or set(y) != {"R", "W", "weight", "hardy_gram"},
           "evaluation_Y fields mismatch")
    c = parse_matrix(y["R"], label="evaluation_Y.R")
    d = parse_matrix(y["W"], label="evaluation_Y.W")
    m_y = parse_matrix(y["weight"], label="evaluation_Y.weight")
    h_y = parse_matrix(y["hardy_gram"], label="evaluation_Y.hardy_gram")
    reject(shape(c) != (r, r) or shape(d) != (r, w), "second frame dimensions mismatch")
    reject(shape(m_y) != (r, r) or not is_pd(m_y), "line-zero weight must be positive definite")
    reject(shape(h_y) != (r, r) or not is_pd(h_y), "Hardy representer Gram must be positive definite")

    graph_w = scale(Fraction(-1), matmul(b_inv, a))
    j = vstack(identity(r), graph_w)
    s = sub(c, matmul(d, matmul(b_inv, a)))
    full_eval = vstack(hstack(a, b), hstack(c, d))
    full_det = determinant(full_eval)
    factor_det = Fraction((-1) ** (r * w)) * determinant(b) * determinant(s)
    reject(full_det == 0 or full_det != factor_det, "conditional determinant factorization failed")

    g_u = block_diag(g_r, g_w)
    g_k = restrict(g_u, j)
    reject(not is_pd(g_k), "graph metric is not positive definite")
    frame_k = matmul(transpose(s), matmul(m_y, s))

    residual_u = parse_matrix(cert["residual_U"], label="residual_U")
    reject(shape(residual_u) != (r + w, r + w) or not symmetric(residual_u),
           "residual_U must be symmetric on U")
    residual_k = restrict(residual_u, j)

    comp = cert["complement"]
    reject(not isinstance(comp, dict) or set(comp) != {"C", "cross"}, "complement fields mismatch")
    c_comp = parse_matrix(comp["C"], label="complement.C")
    z_cross = parse_matrix(comp["cross"], label="complement.cross")
    q, _ = shape(c_comp)
    reject(not is_pd(c_comp), "complement C must be positive definite")
    reject(shape(z_cross) != (q, r + w), "complement cross dimensions mismatch")
    cross_k = restrict(matmul(transpose(z_cross), matmul(inverse(c_comp), z_cross)), j)

    claimed = cert["claimed"]
    expected_claimed = {
        "conditional_S", "graph_metric", "full_evaluation_determinant",
        "frame_lower", "residual_negative_bound", "schur_cross_bound",
        "corrected_floor", "hardy_tail_floor",
    }
    reject(not isinstance(claimed, dict) or set(claimed) != expected_claimed,
           "claimed fields mismatch")
    matrix_equal(s, parse_matrix(claimed["conditional_S"], label="claimed.conditional_S"),
                 "conditional evaluation matrix mismatch")
    matrix_equal(g_k, parse_matrix(claimed["graph_metric"], label="claimed.graph_metric"),
                 "graph metric mismatch")
    reject(full_det != parse_fraction(claimed["full_evaluation_determinant"]),
           "full evaluation determinant mismatch")

    sigma2 = parse_fraction(claimed["frame_lower"])
    omega = parse_fraction(claimed["residual_negative_bound"])
    chi = parse_fraction(claimed["schur_cross_bound"])
    floor = parse_fraction(claimed["corrected_floor"])
    theta2 = parse_fraction(claimed["hardy_tail_floor"])
    reject(min(sigma2, omega, chi, theta2) < 0, "bounds must be nonnegative")

    reject(not is_psd(sub(frame_k, scale(sigma2, g_k))), "frame lower LMI failed")
    reject(not is_psd(add(residual_k, scale(omega, g_k))), "one-sided residual LMI failed")
    reject(not is_psd(sub(scale(chi, g_k), cross_k)), "Schur cross upper LMI failed")

    complete_k = add(frame_k, residual_k)
    corrected_k = sub(complete_k, cross_k)
    reject(not is_psd(sub(corrected_k, scale(floor, g_k))), "corrected kernel floor LMI failed")
    reject(floor != sigma2 - omega - chi, "claimed floor is not the exact scalar composition")
    reject(floor <= 0, "retained control must have strict positive corrected floor")

    hardy_lower_k = matmul(transpose(s), matmul(inverse(h_y), s))
    reject(not is_psd(sub(hardy_lower_k, scale(theta2, g_k))),
           "Hardy interpolation lower LMI failed")

    proof_sha = hashlib.sha256(canonical_json_bytes(cert)).hexdigest()
    return {
        "schema": "riemann.x20501-conditional-line-frame.result.v1",
        "verified": True,
        "verdict": "CERTIFIED_CONDITIONAL_LINE_FRAME_KERNEL_FLOOR",
        "dimensions": {"R": r, "W": w, "kernel": r, "selected_Z": w, "selected_Y": r},
        "graph_map": matrix_json(j),
        "conditional_evaluation": matrix_json(s),
        "full_evaluation_determinant": fraction_json(full_det),
        "graph_metric": matrix_json(g_k),
        "selected_frame_matrix": matrix_json(frame_k),
        "frame_lower": fraction_json(sigma2),
        "residual_restriction": matrix_json(residual_k),
        "residual_negative_bound": fraction_json(omega),
        "schur_cross_restriction": matrix_json(cross_k),
        "schur_cross_bound": fraction_json(chi),
        "corrected_kernel_matrix": matrix_json(corrected_k),
        "corrected_floor": fraction_json(floor),
        "hardy_interpolation_matrix": matrix_json(hardy_lower_k),
        "hardy_tail_floor": fraction_json(theta2),
        "proof_object_sha256": proof_sha,
        "proof_boundary": (
            "Exact finite graph, conditional evaluation Schur complement, one-sided residual, "
            "positive-complement correction, and RKHS interpolation arithmetic only. "
            "The Riemann application still requires directed evaluation matrices, a complete "
            "one-sided omitted-zero residual LMI, and a cofinal positive moat."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        reject(not isinstance(raw, dict), "certificate root must be an object")
        result = verify(raw)
    except (OSError, json.JSONDecodeError, VerificationError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, sort_keys=True))
        return 1
    rendered = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
