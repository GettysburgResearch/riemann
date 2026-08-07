#!/usr/bin/env python3
"""Exact checker for L-15138/T-15116 target transgression.

The checker verifies finite rational coefficient identities only. It does not
evaluate xi or certify the Riemann-specific Schatten limits.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.target-transgression.v1"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if isinstance(n, bool) or isinstance(d, bool) or not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("malformed rational")
        return Fraction(n, d)
    raise ValueError(f"unsupported rational: {x!r}")


def out(x: Fraction) -> Any:
    return x.numerator if x.denominator == 1 else {
        "numerator": x.numerator, "denominator": x.denominator
    }


def mat(data: Any) -> list[list[Fraction]]:
    if not isinstance(data, list) or not data:
        raise ValueError("matrix must be a nonempty list")
    A = [[rat(x) for x in row] for row in data]
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("matrix must be square")
    return A


def mm(A: list[list[Fraction]], B: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mpow(A: list[list[Fraction]], n: int) -> list[list[Fraction]]:
    m = len(A)
    R = [[Fraction(int(i == j)) for j in range(m)] for i in range(m)]
    X = A
    while n:
        if n & 1:
            R = mm(R, X)
        X = mm(X, X)
        n //= 2
    return R


def trace(A: list[list[Fraction]]) -> Fraction:
    return sum(A[i][i] for i in range(len(A)))


def frob2(A: list[list[Fraction]], B: list[list[Fraction]]) -> Fraction:
    return sum((A[i][j] - B[i][j]) ** 2 for i in range(len(A)) for j in range(len(A)))


def even_phase(order: int) -> Fraction:
    if order % 2 or order < 2:
        raise ValueError("this checker retains even orders only")
    return Fraction((-1) ** ((order - 2) // 2))


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    A, K = mat(data["raw_matrix"]), mat(data["renormalized_matrix"])
    if len(A) != len(K):
        raise ValueError("matrix dimension mismatch")
    orders = data.get("orders")
    if not isinstance(orders, list) or not orders or any(isinstance(q, bool) or not isinstance(q, int) for q in orders):
        raise ValueError("invalid orders")
    if sorted(set(orders)) != orders or any(q < 2 or q % 2 for q in orders):
        raise ValueError("orders must be increasing distinct even integers")

    linear = {int(k): rat(v) for k, v in data["linear_coefficients"].items()}
    supplied_defect = {int(k): rat(v) for k, v in data["target_defects"].items()}
    supplied_ratio = {int(k): rat(v) for k, v in data["log_ratio_coefficients"].items()}
    if set(linear) != set(orders) or set(supplied_defect) != set(orders) or set(supplied_ratio) != set(orders):
        raise ValueError("coefficient key mismatch")

    raw, ren, defects, ratios = {}, {}, {}, {}
    for q in orders:
        raw[q] = trace(mpow(A, q))
        ren[q] = trace(mpow(K, q))
        defects[q] = linear[q] - ren[q]
        ratios[q] = even_phase(q) * defects[q] / q
        if supplied_defect[q] != defects[q]:
            raise ValueError(f"target defect mismatch at order {q}")
        if supplied_ratio[q] != ratios[q]:
            raise ValueError(f"log-ratio coefficient mismatch at order {q}")

    C = rat(data["hilbert_schmidt_radius"])
    eps = rat(data["difference_s2_upper"])
    if C <= 0 or eps < 0:
        raise ValueError("invalid norm bounds")
    if sum(x*x for row in A for x in row) > C*C or sum(x*x for row in K for x in row) > C*C:
        raise ValueError("Hilbert-Schmidt radius too small")
    if frob2(A, K) > eps*eps:
        raise ValueError("difference S2 upper bound too small")

    if 4 not in orders:
        raise ValueError("order four is required")
    power_bound = Fraction(4) * C ** 3 * eps
    if abs(raw[4] - ren[4]) > power_bound:
        raise ValueError("quartic power-trace stability bound failed")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    return {
        "status": "CERTIFIED_TARGET_TRANSGRESSION_IDENTITY",
        "dimension": len(A),
        "raw_trace_moments": {str(k): out(v) for k, v in raw.items()},
        "renormalized_trace_moments": {str(k): out(v) for k, v in ren.items()},
        "target_defects": {str(k): out(v) for k, v in defects.items()},
        "log_ratio_coefficients": {str(k): out(v) for k, v in ratios.items()},
        "quartic_ratio_exponent": out(ratios[4]),
        "quartic_power_trace_bound": out(power_bound),
        "certificate_sha256": digest,
        "scope": "finite exact transgression only; no xi evaluation or Riemann Schatten limit",
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("certificate", type=Path)
    args = p.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
