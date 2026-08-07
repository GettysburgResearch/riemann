#!/usr/bin/env python3
"""Exact checker for L-15126 one-sided selected-zero residual completion."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.one-sided-selected-residual.v1"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if (
            isinstance(n, bool)
            or isinstance(d, bool)
            or not isinstance(n, int)
            or not isinstance(d, int)
            or d == 0
        ):
            raise ValueError("bad rational")
        return Fraction(n, d)
    raise ValueError("bad rational")


def dump(x: Fraction) -> Any:
    if x.denominator == 1:
        return x.numerator
    return {"numerator": x.numerator, "denominator": x.denominator}


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def scale(s, a):
    return [[s * x for x in row] for row in a]


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


def restrict(a, u):
    return matmul(transpose(u), matmul(a, u))


def ldl_positive_pivots(a):
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("matrix is not square")
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise ValueError("matrix is not symmetric")
    ell = [[Fraction(0)] * n for _ in range(n)]
    pivots = []
    for i in range(n):
        ell[i][i] = Fraction(1)
        d = a[i][i] - sum(ell[i][k] * ell[i][k] * pivots[k] for k in range(i))
        if d <= 0:
            raise ValueError(f"nonpositive pivot {i}: {d}")
        pivots.append(d)
        for j in range(i + 1, n):
            ell[j][i] = (
                a[j][i]
                - sum(ell[j][k] * ell[i][k] * pivots[k] for k in range(i))
            ) / d
    return pivots


def parse_matrix(obj, n):
    a = [[rat(x) for x in row] for row in obj]
    if len(a) != n or any(len(row) != n for row in a):
        raise ValueError("dimension mismatch")
    return a


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")

    p = [rat(x) for x in data["p"]]
    n = len(p)
    if n < 2 or all(value == 0 for value in p):
        raise ValueError("bad target")

    selected = parse_matrix(data["selected_pinned"], n)
    residual = parse_matrix(data["residual_pinned"], n)
    metric = parse_matrix(data["metric"], n)
    selected_floor = rat(data["selected_floor"])
    negative_radius = rat(data["residual_negative_radius"])
    witness = [rat(x) for x in data["absolute_witness"]]

    if len(witness) != n:
        raise ValueError("bad witness dimension")
    if selected_floor <= 0 or negative_radius < 0 or negative_radius >= selected_floor:
        raise ValueError("invalid scalar moat")
    if matvec(selected, p) != [0] * n or matvec(residual, p) != [0] * n:
        raise ValueError("target-kernel identity failed")

    u = complement_basis(p)
    selected_lmi = restrict(sub(selected, scale(selected_floor, metric)), u)
    residual_lmi = restrict(add(residual, scale(negative_radius, metric)), u)
    full_lmi = restrict(add(selected, residual), u)

    selected_pivots = ldl_positive_pivots(selected_lmi)
    residual_pivots = ldl_positive_pivots(residual_lmi)
    full_pivots = ldl_positive_pivots(full_lmi)

    mw = matvec(metric, witness)
    rw = matvec(residual, witness)
    denominator = sum(witness[i] * mw[i] for i in range(n))
    numerator = abs(sum(witness[i] * rw[i] for i in range(n)))
    if denominator <= 0:
        raise ValueError("nonpositive witness metric")
    absolute_lower = numerator / denominator
    if absolute_lower <= selected_floor:
        raise ValueError("absolute-norm separation witness failed")

    digest = hashlib.sha256(
        json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    return {
        "status": "CERTIFIED_ONE_SIDED_RESIDUAL_COMPLETION",
        "selected_floor": dump(selected_floor),
        "residual_negative_radius": dump(negative_radius),
        "strict_margin": dump(selected_floor - negative_radius),
        "selected_ldl_pivots": [dump(x) for x in selected_pivots],
        "residual_lower_ldl_pivots": [dump(x) for x in residual_pivots],
        "full_ldl_pivots": [dump(x) for x in full_pivots],
        "absolute_residual_radius_lower_witness": dump(absolute_lower),
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
