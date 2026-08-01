#!/usr/bin/env python3
"""Exact verifier for the actual finite-jet relative det_2 Ward pullback.

The verifier checks, with rational arithmetic only, that the nonlinear
counterterm

    q_l = delta_l^raw + Tr(A^l) - Tr(K^l),   K=A-D,

makes the corrected one-contour scalar coefficient equal Tr(K^l), and that the
order-four relative determinant coefficient equals the complete noncommutative
contact polynomial.

This is a finite algebraic checker. It does not evaluate the Riemann contour
maps and does not certify RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.actual-relative-ward.v1"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("malformed rational")
        return Fraction(n, d)
    raise ValueError(f"unsupported rational: {x!r}")


def dump_rat(x: Fraction) -> Any:
    return x.numerator if x.denominator == 1 else {
        "numerator": x.numerator,
        "denominator": x.denominator,
    }


def matrix(data: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(data, list) or not data or not all(isinstance(r, list) for r in data):
        raise ValueError(f"{name} must be a nonempty matrix")
    n = len(data)
    if any(len(r) != n for r in data):
        raise ValueError(f"{name} must be square")
    out = [[rat(x) for x in r] for r in data]
    if any(out[i][j] != out[j][i] for i in range(n) for j in range(n)):
        raise ValueError(f"{name} must be symmetric")
    return out


def eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def sub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def power(a: list[list[Fraction]], n: int) -> list[list[Fraction]]:
    if n < 0:
        raise ValueError("negative matrix power")
    out = eye(len(a))
    base = a
    m = n
    while m:
        if m & 1:
            out = mul(out, base)
        base = mul(base, base)
        m //= 2
    return out


def trace(a: list[list[Fraction]]) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def word_trace(*letters: list[list[Fraction]]) -> Fraction:
    out = eye(len(letters[0]))
    for a in letters:
        out = mul(out, a)
    return trace(out)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    A = matrix(data.get("raw_operator"), "raw_operator")
    D = matrix(data.get("jet_operator"), "jet_operator")
    if len(A) != len(D):
        raise ValueError("dimension mismatch")
    K = sub(A, D)

    max_order = data.get("max_order")
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 4:
        raise ValueError("max_order must be an integer at least 4")

    raw_defects = {int(k): rat(v) for k, v in data.get("raw_diagonal_defects", {}).items()}
    supplied_total = {int(k): rat(v) for k, v in data.get("nonlinear_counterterms", {}).items()}
    expected_orders = set(range(2, max_order + 1))
    if set(raw_defects) != expected_orders or set(supplied_total) != expected_orders:
        raise ValueError("defect and counterterm ledgers must contain every order")

    raw_moments: dict[int, Fraction] = {}
    renorm_moments: dict[int, Fraction] = {}
    relative: dict[int, Fraction] = {}
    corrected: dict[int, Fraction] = {}

    for ell in range(2, max_order + 1):
        a = trace(power(A, ell))
        k = trace(power(K, ell))
        q_rel = a - k
        q_total = raw_defects[ell] + q_rel
        raw_scalar = a + raw_defects[ell]
        corrected_scalar = raw_scalar - q_total
        if supplied_total[ell] != q_total:
            raise ValueError(f"nonlinear counterterm mismatch at order {ell}")
        if corrected_scalar != k:
            raise ValueError(f"corrected scalar mismatch at order {ell}")
        raw_moments[ell] = a
        renorm_moments[ell] = k
        relative[ell] = q_rel
        corrected[ell] = corrected_scalar

    a3d = word_trace(A, A, A, D)
    a2d2 = word_trace(A, A, D, D)
    adad = word_trace(A, D, A, D)
    ad3 = word_trace(A, D, D, D)
    d4 = trace(power(D, 4))
    ward4 = 4 * a3d - 4 * a2d2 - 2 * adad + 4 * ad3 - d4
    if ward4 != relative[4]:
        raise ValueError("order-four contact polynomial does not equal relative determinant coefficient")

    C = rat(data.get("hilbert_schmidt_upper"))
    radius = rat(data.get("series_radius"))
    if C <= 0 or radius <= 0 or C * radius >= 1:
        raise ValueError("invalid majorant parameters")
    majorant = 2 * C * C * radius / (1 - C * radius)
    for ell in range(2, max_order + 1):
        if abs(raw_moments[ell]) > C ** ell:
            raise ValueError(f"raw moment exceeds declared C^ell at order {ell}")
        if abs(renorm_moments[ell]) > C ** ell:
            raise ValueError(f"renormalized moment exceeds declared C^ell at order {ell}")
        if abs(relative[ell]) > 2 * C ** ell:
            raise ValueError(f"relative coefficient exceeds 2 C^ell at order {ell}")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    return {
        "status": "CERTIFIED_ACTUAL_RELATIVE_WARD_PULLBACK",
        "dimension": len(A),
        "max_order": max_order,
        "raw_trace_moments": {str(k): dump_rat(v) for k, v in raw_moments.items()},
        "renormalized_trace_moments": {str(k): dump_rat(v) for k, v in renorm_moments.items()},
        "relative_ward_coefficients": {str(k): dump_rat(v) for k, v in relative.items()},
        "corrected_scalar_coefficients": {str(k): dump_rat(v) for k, v in corrected.items()},
        "order_four_components": {
            "Tr_A3D": dump_rat(a3d),
            "Tr_A2D2": dump_rat(a2d2),
            "Tr_ADAD": dump_rat(adad),
            "Tr_AD3": dump_rat(ad3),
            "Tr_D4": dump_rat(d4),
            "ward_order_four": dump_rat(ward4),
        },
        "relative_series_majorant": dump_rat(majorant),
        "certificate_sha256": digest,
        "scope": "finite nonlinear Ward amendment only; no proof that the manuscript's linear counterterm already equals it",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    result = verify(json.loads(args.certificate.read_text()))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
