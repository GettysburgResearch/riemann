#!/usr/bin/env python3
"""Exact rational verifier for the audited L-14302 Schur--Ritz certificate.

The verifier checks only finite algebra. It assumes an external provenance proof
that the intended exact operator lies in the declared operator-norm ball and
commutes with the declared parity involution, and that the exact Hardy Gram lies
between the supplied rational Loewner bounds.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.prolate-weighted-schur-ritz.v1"


class CertificateError(ValueError):
    pass


def frac(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not a rational string") from exc
    if isinstance(value, dict):
        if set(value) != {"numerator", "denominator"}:
            raise CertificateError(f"{name} fraction object needs exactly numerator and denominator")
        num = value["numerator"]
        den = value["denominator"]
        if isinstance(num, bool) or isinstance(den, bool) or not isinstance(num, int) or not isinstance(den, int):
            raise CertificateError(f"{name} numerator and denominator must be integers")
        try:
            return Fraction(num, den)
        except ZeroDivisionError as exc:
            raise CertificateError(f"{name} has zero denominator") from exc
    raise CertificateError(f"{name} must be an integer, rational string, or fraction object")


def vector(value: Any, name: str, n: int | None = None) -> list[Fraction]:
    if not isinstance(value, list):
        raise CertificateError(f"{name} must be an array")
    if n is not None and len(value) != n:
        raise CertificateError(f"{name} must have length {n}")
    return [frac(x, f"{name}[{i}]") for i, x in enumerate(value)]


def matrix(value: Any, name: str, rows: int | None = None, cols: int | None = None) -> list[list[Fraction]]:
    if not isinstance(value, list):
        raise CertificateError(f"{name} must be an array")
    if rows is not None and len(value) != rows:
        raise CertificateError(f"{name} must have {rows} rows")
    if not value:
        if rows not in (None, 0):
            raise CertificateError(f"{name} is unexpectedly empty")
        if cols not in (None, 0):
            raise CertificateError(f"{name} is unexpectedly empty")
        return []
    width = len(value[0]) if isinstance(value[0], list) else -1
    if width < 0:
        raise CertificateError(f"{name}[0] must be an array")
    if cols is not None and width != cols:
        raise CertificateError(f"{name} must have {cols} columns")
    out: list[list[Fraction]] = []
    for i, row in enumerate(value):
        if not isinstance(row, list) or len(row) != width:
            raise CertificateError(f"{name}[{i}] has inconsistent width")
        out.append([frac(x, f"{name}[{i}][{j}]") for j, x in enumerate(row)])
    return out


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return (len(a), len(a[0]) if a else 0)


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a:
        return []
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise CertificateError(f"matrix multiplication shape mismatch {(ar, ac)} x {(br, bc)}")
    return [[sum((a[i][k] * b[k][j] for k in range(ac)), Fraction(0)) for j in range(bc)] for i in range(ar)]


def matvec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    r, c = shape(a)
    if c != len(x):
        raise CertificateError("matrix-vector shape mismatch")
    return [sum((a[i][j] * x[j] for j in range(c)), Fraction(0)) for i in range(r)]


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    if len(x) != len(y):
        raise CertificateError("dot-product length mismatch")
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def add(a: list[list[Fraction]], b: list[list[Fraction]], scale_b: Fraction = Fraction(1)) -> list[list[Fraction]]:
    if shape(a) != shape(b):
        raise CertificateError("matrix addition shape mismatch")
    return [[a[i][j] + scale_b * b[i][j] for j in range(shape(a)[1])] for i in range(shape(a)[0])]


def scale(a: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in a]


def eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def is_symmetric(a: list[list[Fraction]]) -> bool:
    r, c = shape(a)
    return r == c and all(a[i][j] == a[j][i] for i in range(r) for j in range(c))


def rank(a: list[list[Fraction]]) -> int:
    if not a:
        return 0
    m = [row[:] for row in a]
    r, c = shape(m)
    pivot_row = 0
    for col in range(c):
        pivot = next((i for i in range(pivot_row, r) if m[i][col] != 0), None)
        if pivot is None:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        p = m[pivot_row][col]
        m[pivot_row] = [x / p for x in m[pivot_row]]
        for i in range(r):
            if i == pivot_row or m[i][col] == 0:
                continue
            f = m[i][col]
            m[i] = [m[i][j] - f * m[pivot_row][j] for j in range(c)]
        pivot_row += 1
        if pivot_row == r:
            break
    return pivot_row


def ldl_psd(a: list[list[Fraction]], strict: bool = False) -> bool:
    if not is_symmetric(a):
        return False
    n = len(a)
    if n == 0:
        return True
    l = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    d: list[Fraction] = []
    for j in range(n):
        pivot = a[j][j] - sum((l[j][k] * l[j][k] * d[k] for k in range(j)), Fraction(0))
        if pivot < 0 or (strict and pivot == 0):
            return False
        d.append(pivot)
        for i in range(j + 1, n):
            num = a[i][j] - sum((l[i][k] * l[j][k] * d[k] for k in range(j)), Fraction(0))
            if pivot == 0:
                if num != 0:
                    return False
                l[i][j] = Fraction(0)
            else:
                l[i][j] = num / pivot
    return True


def columns(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return transpose(a)


def gram(b: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(transpose(b), b)


def compress(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(transpose(b), matmul(a, b))


def parity_apply(signs: list[int], x: list[Fraction]) -> list[Fraction]:
    return [Fraction(signs[i]) * x[i] for i in range(len(x))]


def decimal_string(x: Fraction, digits: int = 16) -> str:
    # Display only; all rigorous fields remain exact fractions.
    sign = "-" if x < 0 else ""
    x = abs(x)
    integer = x.numerator // x.denominator
    rem = x.numerator % x.denominator
    out = []
    for _ in range(digits):
        rem *= 10
        out.append(str(rem // x.denominator))
        rem %= x.denominator
    return f"{sign}{integer}." + "".join(out)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA}")

    a0 = matrix(data.get("matrix_midpoint"), "matrix_midpoint")
    n, n2 = shape(a0)
    if n < 2 or n != n2 or not is_symmetric(a0):
        raise CertificateError("matrix_midpoint must be symmetric of dimension at least two")

    signs_raw = data.get("parity_signs")
    if not isinstance(signs_raw, list) or len(signs_raw) != n or any(isinstance(x, bool) or x not in (-1, 1) for x in signs_raw):
        raise CertificateError("parity_signs must be an array of +1/-1 of matrix dimension")
    signs = [int(x) for x in signs_raw]
    for i in range(n):
        for j in range(n):
            if signs[i] != signs[j] and a0[i][j] != 0:
                raise CertificateError("matrix_midpoint does not commute with declared parity")

    p = vector(data.get("projection_vector"), "projection_vector", n)
    s = dot(p, p)
    if s <= 0:
        raise CertificateError("projection_vector must be nonzero")
    if parity_apply(signs, p) != p:
        raise CertificateError("projection_vector must be even")

    n_plus = sum(1 for x in signs if x == 1)
    n_minus = n - n_plus
    bplus = matrix(data.get("even_complement_basis"), "even_complement_basis", rows=n, cols=n_plus - 1)
    bminus = matrix(data.get("odd_basis"), "odd_basis", rows=n, cols=n_minus)

    if rank(bplus) != n_plus - 1:
        raise CertificateError("even_complement_basis is not full column rank")
    if rank(bminus) != n_minus:
        raise CertificateError("odd_basis is not full column rank")
    for col in columns(bplus):
        if parity_apply(signs, col) != col or dot(col, p) != 0:
            raise CertificateError("even_complement_basis must be even and orthogonal to projection_vector")
    for col in columns(bminus):
        if parity_apply(signs, col) != [-x for x in col]:
            raise CertificateError("odd_basis must be odd")

    delta = frac(data.get("operator_radius"), "operator_radius")
    h = frac(data.get("weighted_coercivity"), "weighted_coercivity")
    gminus = frac(data.get("odd_gap"), "odd_gap")
    m = frac(data.get("weighted_lower_vs_ordinary"), "weighted_lower_vs_ordinary")
    b0_bound = frac(data.get("dual_residual_midpoint_bound"), "dual_residual_midpoint_bound")
    eps = frac(data.get("dual_residual_error_bound"), "dual_residual_error_bound")
    tail = frac(data.get("weighted_tail_bound"), "weighted_tail_bound")
    if delta < 0 or h <= 0 or gminus <= 0 or m <= 0 or b0_bound < 0 or eps < 0 or tail < 0:
        raise CertificateError("radii/bounds must have the required nonnegative or positive signs")

    k = n_plus - 1
    gl = matrix(data.get("weighted_gram_lower"), "weighted_gram_lower", rows=k, cols=k)
    gu = matrix(data.get("weighted_gram_upper"), "weighted_gram_upper", rows=k, cols=k)
    if not is_symmetric(gl) or not is_symmetric(gu):
        raise CertificateError("weighted Gram bounds must be symmetric")
    if not ldl_psd(gl, strict=True):
        raise CertificateError("weighted_gram_lower must be positive definite")
    if not ldl_psd(add(gu, gl, Fraction(-1))):
        raise CertificateError("weighted_gram_upper - weighted_gram_lower must be PSD")

    splus = gram(bplus)
    sminus = gram(bminus)
    if not ldl_psd(add(gl, scale(splus, m), Fraction(-1))):
        raise CertificateError("weighted_gram_lower must dominate m times the ordinary Gram")

    mu0 = dot(p, matvec(a0, p)) / s
    u = frac(data.get("rayleigh_upper"), "rayleigh_upper")
    if u < mu0 + delta:
        raise CertificateError("rayleigh_upper must be at least midpoint Rayleigh plus operator radius")

    shifted = add(a0, scale(eye(n), -u))
    even_lmi = add(add(compress(shifted, bplus), scale(splus, -delta)), scale(gu, -h))
    if not ldl_psd(even_lmi):
        raise CertificateError("weighted even-complement coercivity LMI failed")

    odd_lmi = add(add(compress(shifted, bminus), scale(sminus, -delta)), scale(sminus, -gminus))
    if not ldl_psd(odd_lmi):
        raise CertificateError("odd-sector gap LMI failed")

    d0 = matvec(transpose(bplus), matvec(a0, p))
    schur = [[b0_bound * b0_bound] + d0]
    for i in range(k):
        schur.append([d0[i]] + gl[i][:])
    if not ldl_psd(schur):
        raise CertificateError("dual residual Schur certificate failed")

    if eps * eps * m < delta * delta * s:
        raise CertificateError("dual_residual_error_bound is too small for the operator radius")

    dual_total = b0_bound + eps
    distance = tail + dual_total / h
    gap = min(h * m, gminus)

    raw = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    result = {
        "schema": "riemann.prolate-weighted-schur-ritz.verification.v1",
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "dimension": n,
        "midpoint_rayleigh": str(mu0),
        "rayleigh_upper": str(u),
        "simple_even_ground_certified": True,
        "global_spectral_gap_lower": str(gap),
        "dual_residual_total_upper": str(dual_total),
        "weighted_target_line_distance_upper": str(distance),
        "display_truncated_toward_zero": {
            "global_spectral_gap_lower": decimal_string(gap),
            "dual_residual_total_upper": decimal_string(dual_total),
            "weighted_target_line_distance_upper": decimal_string(distance),
        },
        "certificate_gates": {
            "midpoint_parity": "PASS",
            "complete_parity_bases": "PASS",
            "directed_gram_loewner_bounds": "PASS",
            "rayleigh_upper": "PASS",
            "weighted_even_coercivity": "PASS",
            "odd_globality_gap": "PASS",
            "dual_residual_schur": "PASS",
            "operator_radius_dual_budget": "PASS",
        },
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text())
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
