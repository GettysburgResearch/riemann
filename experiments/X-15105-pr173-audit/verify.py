#!/usr/bin/env python3
"""Exact standard-library regressions for L-15111, R-15103, and L-15112."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path


def poly_mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a: list[F], b: list[F]) -> list[F]:
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def interpolation_polynomial(nodes: list[F], p: list[F]) -> list[F]:
    """Ascending coefficients of sum_i p_i prod_(k!=i)(lambda_k-s)."""
    out = [F(0)]
    for i, pi in enumerate(p):
        term = [F(1)]
        for j, lam in enumerate(nodes):
            if i != j:
                term = poly_mul(term, [lam, F(-1)])
        out = poly_add(out, [pi * x for x in term])
    return out


def determinant(matrix: list[list[F]]) -> F:
    n = len(matrix)
    a = [[F(x) for x in row] for row in matrix]
    sign = 1
    value = F(1)
    for k in range(n):
        pivot_row = next((i for i in range(k, n) if a[i][k] != 0), None)
        if pivot_row is None:
            return F(0)
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        value *= pivot
        for i in range(k + 1, n):
            factor = a[i][k] / pivot
            for j in range(k + 1, n):
                a[i][j] -= factor * a[k][j]
    return sign * value


def principal_minors(matrix: list[list[F]]) -> dict[str, F]:
    n = len(matrix)
    out: dict[str, F] = {}
    for size in range(1, n + 1):
        for indices in itertools.combinations(range(n), size):
            sub = [[matrix[i][j] for j in indices] for i in indices]
            out[",".join(str(i) for i in indices)] = determinant(sub)
    return out


def dot(x: list[int | F], y: list[int | F]) -> F:
    return sum((F(a) * F(b) for a, b in zip(x, y)), F(0))


def b_value(p: list[F], x: list[int]) -> F:
    return sum((F(xi * xi) / pi for xi, pi in zip(x, p)), F(0)) - F(sum(x) ** 2)


def leading_minors(matrix: list[list[F]]) -> list[F]:
    return [determinant([row[:k] for row in matrix[:k]]) for k in range(1, len(matrix) + 1)]


def encode(value: F) -> str:
    return str(value)


def main() -> int:
    nodes3 = [F(-1), F(0), F(1)]
    p3 = [F(-1), F(3), F(-1)]
    poly3 = interpolation_polynomial(nodes3, p3)
    assert poly3 == [F(-3), F(0), F(1)]
    assert p3[0] * p3[1] < 0 and p3[1] * p3[2] < 0

    q3 = [
        [F(2), F(1), F(1)],
        [F(1), F(2, 3), F(1)],
        [F(1), F(1), F(2)],
    ]
    q3p = [sum((q3[i][j] * p3[j] for j in range(3)), F(0)) for i in range(3)]
    assert q3p == [F(0), F(0), F(0)]
    minors3 = principal_minors(q3)
    assert all(value >= 0 for value in minors3.values())
    assert minors3["0,1,2"] == 0

    nodes4 = [F(0), F(1), F(2), F(3)]
    p4 = [F(5, 64), F(-9, 64), F(35, 64), F(33, 64)]
    poly4 = interpolation_polynomial(nodes4, p4)
    assert poly4 == [F(15, 32), F(-43, 16), F(7, 2), F(-1)]
    assert sum(p4, F(0)) == 1

    x_plus = [-5, -3, -1, 1]
    x_minus = [-3, 5, -3, 5]
    assert dot(p4, x_plus) == 0
    assert dot(p4, x_minus) == 0
    b_plus = b_value(p4, x_plus)
    b_minus = b_value(p4, x_minus)
    assert b_plus == F(226112, 1155) > 0
    assert b_minus == F(-47248, 3465) < 0

    good_leading = leading_minors(q3)
    assert good_leading == [F(2), F(1, 3), F(0)]

    bad = [
        [F(1), F(0), F(0)],
        [F(0), F(0), F(0)],
        [F(0), F(0), F(-1)],
    ]
    bad_leading = leading_minors(bad)
    assert bad_leading == [F(1), F(0), F(0)]

    result = {
        "schema": "riemann.pr173-exact-audit.v1",
        "gap_counterexample": {
            "nodes": [encode(x) for x in nodes3],
            "p": [encode(x) for x in p3],
            "P_ascending": [encode(x) for x in poly3],
            "same_sign_adjacent_pairs": 0,
            "real_roots": "+-sqrt(3)",
            "canonical_Q": [[encode(x) for x in row] for row in q3],
            "Qp": [encode(x) for x in q3p],
            "principal_minors": {k: encode(v) for k, v in minors3.items()},
        },
        "scalar_counterexample": {
            "nodes": [encode(x) for x in nodes4],
            "p": [encode(x) for x in p4],
            "P_ascending": [encode(x) for x in poly4],
            "P_factorization": "-(s-1/4)(s-3/4)(s-5/2)",
            "x_plus": x_plus,
            "b_plus": encode(b_plus),
            "x_minus": x_minus,
            "b_minus": encode(b_minus),
            "p_dot_x_plus": encode(dot(p4, x_plus)),
            "p_dot_x_minus": encode(dot(p4, x_minus)),
        },
        "leading_minors": {
            "valid_corank_one_example": [encode(x) for x in good_leading],
            "nonnegative_only_counterexample": [encode(x) for x in bad_leading],
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_digest"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).resolve().parent / "results" / "exact-audit.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
