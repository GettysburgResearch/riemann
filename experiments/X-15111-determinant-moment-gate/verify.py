#!/usr/bin/env python3
"""Exact finite checker for the Hilbert--Schmidt determinant moment gate.

This checker verifies a finite self-adjoint spectral model at the formal
regularized-determinant level. It does not evaluate xi and does not certify RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.det2-moment-gate.v1"


def rat(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        n, d = value["numerator"], value["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("malformed rational")
        return Fraction(n, d)
    raise ValueError(f"unsupported rational {value!r}")


def dump_rat(value: Fraction) -> Any:
    if value.denominator == 1:
        return value.numerator
    return {"numerator": value.numerator, "denominator": value.denominator}


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix is not square")
    a = [row[:] for row in matrix]
    det = Fraction(1)
    for k in range(n):
        pivot = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            det = -det
        p = a[k][k]
        det *= p
        for r in range(k + 1, n):
            if a[r][k] == 0:
                continue
            factor = a[r][k] / p
            for c in range(k + 1, n):
                a[r][c] -= factor * a[k][c]
    return det


def require_positive_definite(matrix: list[list[Fraction]], name: str) -> list[Fraction]:
    minors: list[Fraction] = []
    for k in range(1, len(matrix) + 1):
        value = determinant([row[:k] for row in matrix[:k]])
        if value <= 0:
            raise ValueError(f"{name} leading principal minor {k} is not positive: {value}")
        minors.append(value)
    return minors


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    eigenvalues = [rat(x) for x in data["eigenvalues"]]
    if not eigenvalues:
        raise ValueError("empty spectrum")
    max_order = data.get("max_order")
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 8:
        raise ValueError("max_order must be an integer at least 8")

    supplied = {int(k): rat(v) for k, v in data["trace_moments"].items()}
    if set(supplied) != set(range(2, max_order + 1)):
        raise ValueError("trace_moments must contain every order 2..max_order")

    recomputed: dict[int, Fraction] = {}
    for m in range(2, max_order + 1):
        value = sum(lam ** m for lam in eigenvalues)
        recomputed[m] = value
        if supplied[m] != value:
            raise ValueError(f"trace moment mismatch at order {m}")

    if data.get("require_central_even_symmetry", False):
        for m in range(3, max_order + 1, 2):
            if recomputed[m] != 0:
                raise ValueError(f"nonzero odd trace moment at order {m}")

    supplied_log = {int(k): rat(v) for k, v in data["formal_log_coefficients"].items()}
    if set(supplied_log) != set(range(2, max_order + 1)):
        raise ValueError("formal_log_coefficients must contain every order 2..max_order")
    # For log det_2(I+zK): [z^m] = (-1)^(m-1) Tr(K^m)/m.
    for m in range(2, max_order + 1):
        expected = Fraction((-1) ** (m - 1), m) * recomputed[m]
        if supplied_log[m] != expected:
            raise ValueError(f"formal log coefficient mismatch at order {m}")

    hankel_size = data.get("hankel_size")
    if isinstance(hankel_size, bool) or not isinstance(hankel_size, int) or hankel_size < 1:
        raise ValueError("invalid hankel_size")
    # s_r = Tr(K^(2r+2)) is a Stieltjes moment sequence for
    # sum_j lambda_j^2 delta_(lambda_j^2).
    needed = 4 * hankel_size
    if max_order < needed:
        raise ValueError("max_order too small for requested Hankel gates")
    s = {r: recomputed[2 * r + 2] for r in range(2 * hankel_size)}
    h0 = [[s[i + j] for j in range(hankel_size)] for i in range(hankel_size)]
    h1 = [[s[i + j + 1] for j in range(hankel_size)] for i in range(hankel_size)]
    h0_minors = require_positive_definite(h0, "Hankel")
    h1_minors = require_positive_definite(h1, "shifted Hankel")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    return {
        "status": "CERTIFIED_FINITE_DET2_MOMENT_GATE",
        "dimension": len(eigenvalues),
        "max_order": max_order,
        "trace_moments": {str(k): dump_rat(v) for k, v in recomputed.items()},
        "hankel_leading_minors": [dump_rat(x) for x in h0_minors],
        "shifted_hankel_leading_minors": [dump_rat(x) for x in h1_minors],
        "certificate_sha256": digest,
        "scope": "finite formal determinant control only; no xi moment identity",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
