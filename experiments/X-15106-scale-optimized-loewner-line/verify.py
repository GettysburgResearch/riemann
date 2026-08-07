#!/usr/bin/env python3
"""Exact checker for L-15120 scale-optimized canonical-ray completion."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.scale-optimized-canonical-line.v1"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("Boolean is not a rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("Boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("Malformed rational")
        return Fraction(n, d)
    raise ValueError(f"Unsupported rational: {x!r}")


def dump_rat(x: Fraction) -> Any:
    if x.denominator == 1:
        return x.numerator
    return {"numerator": x.numerator, "denominator": x.denominator}


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def matscale(s, a):
    return [[s * x for x in row] for row in a]


def eye(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def ldl_positive_pivots(a):
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Matrix is not square")
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise ValueError("Matrix is not symmetric")
    ell = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        ell[i][i] = Fraction(1)
        d = a[i][i] - sum(ell[i][k] * ell[i][k] * pivots[k] for k in range(i))
        if d <= 0:
            raise ValueError(f"Nonpositive LDL pivot {i}: {d}")
        pivots.append(d)
        for j in range(i + 1, n):
            ell[j][i] = (
                a[j][i]
                - sum(ell[j][k] * ell[i][k] * pivots[k] for k in range(i))
            ) / d
    return pivots


def complement_basis(p):
    n = len(p)
    r = next(i for i, value in enumerate(p) if value != 0)
    columns = []
    for j in range(n):
        if j == r:
            continue
        col = [Fraction(0)] * n
        col[j] = Fraction(1)
        col[r] = -p[j] / p[r]
        columns.append(col)
    return transpose(columns)


def canonical_matrix(nodes, p):
    n = len(nodes)
    g = []
    for i in range(n):
        g.append(
            -sum(
                (Fraction(1) + p[j] / p[i]) / (nodes[i] - nodes[j])
                for j in range(n)
                if j != i
            )
        )
    q = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                q[i][j] = (g[i] - g[j]) / (nodes[i] - nodes[j])
    for i in range(n):
        q[i][i] = -sum(q[i][j] * p[j] for j in range(n) if j != i) / p[i]
    return g, q


def target_pinned_matrix(nodes, p, beta, c):
    n = len(nodes)
    raw = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                raw[i][j] = (beta[i] - beta[j]) / (nodes[i] - nodes[j])
    raw_p = matvec(raw, p)
    t = [[raw[i][j] - c for j in range(n)] for i in range(n)]
    for i in range(n):
        t[i][i] = raw[i][i] + (c - raw_p[i]) / p[i] - c
    return t


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("Wrong schema")
    nodes = [rat(x) for x in data["nodes"]]
    p = [rat(x) for x in data["p"]]
    beta = [rat(x) for x in data["beta"]]
    a = rat(data["canonical_scale"])
    c = rat(data["boundary_scalar"])
    moat = rat(data["canonical_moat_lower"])

    n = len(nodes)
    if n < 2 or len(p) != n or len(beta) != n:
        raise ValueError("Dimension mismatch")
    if len(set(nodes)) != n:
        raise ValueError("Nodes are not distinct")
    if any(value == 0 for value in p):
        raise ValueError("Target coordinate is zero")
    if sum(p) != 1:
        raise ValueError("Target is not normalized")
    if a <= 0 or moat <= 0:
        raise ValueError("Scale and moat must be positive")

    g, qcan = canonical_matrix(nodes, p)
    if any(value != 0 for value in matvec(qcan, p)):
        raise ValueError("Canonical kernel identity failed")

    u = complement_basis(p)
    qcan_minus = matsub(qcan, matscale(moat, eye(n)))
    moat_form = matmul(transpose(u), matmul(qcan_minus, u))
    moat_pivots = ldl_positive_pivots(moat_form)

    tmat = target_pinned_matrix(nodes, p, beta, c)
    if any(value != 0 for value in matvec(tmat, p)):
        raise ValueError("Arithmetic target-pinning identity failed")

    difference = matsub(tmat, matscale(a, qcan))
    error = max(sum(abs(x) for x in row) for row in difference)
    if error >= a * moat:
        raise ValueError(f"Canonical-ray moat failed: {error} >= {a * moat}")

    restricted_t = matmul(transpose(u), matmul(tmat, u))
    arithmetic_pivots = ldl_positive_pivots(restricted_t)

    unscaled = matsub(tmat, qcan)
    unscaled_error = max(sum(abs(x) for x in row) for row in unscaled)

    canonical_bytes = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical_bytes).hexdigest()
    return {
        "status": "CERTIFIED_SCALE_OPTIMIZED_ARITHMETIC_COMPLETION",
        "canonical_source": [dump_rat(x) for x in g],
        "canonical_moat_lower": dump_rat(moat),
        "canonical_moat_ldl_pivots": [dump_rat(x) for x in moat_pivots],
        "canonical_scale": dump_rat(a),
        "boundary_scalar": dump_rat(c),
        "scaled_difference_row_bound": dump_rat(error),
        "scaled_moat": dump_rat(a * moat),
        "arithmetic_complement_ldl_pivots": [dump_rat(x) for x in arithmetic_pivots],
        "unscaled_difference_row_bound": dump_rat(unscaled_error),
        "certificate_sha256": digest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
