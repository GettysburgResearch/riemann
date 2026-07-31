#!/usr/bin/env python3
"""Exact rational verifier for L-15125/T-15108."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.certified-zero-frame-residual.v1"


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


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def matscale(c, a):
    return [[c * x for x in row] for row in a]


def diag(values):
    return [[values[i] if i == j else Fraction(0) for j in range(len(values))] for i in range(len(values))]


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def complement_basis(p):
    n = len(p)
    r = next(i for i, value in enumerate(p) if value != 0)
    cols = []
    for j in range(n):
        if j == r:
            continue
        col = [Fraction(0)] * n
        col[j] = Fraction(1)
        col[r] = -p[j] / p[r]
        cols.append(col)
    return transpose(cols)


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
        d = a[i][i] - sum(ell[i][k] ** 2 * pivots[k] for k in range(i))
        if d <= 0:
            raise ValueError(f"Nonpositive LDL pivot {i}: {d}")
        pivots.append(d)
        for j in range(i + 1, n):
            ell[j][i] = (
                a[j][i]
                - sum(ell[j][k] * ell[i][k] * pivots[k] for k in range(i))
            ) / d
    return pivots


def cauchy_gram(nodes, atoms):
    n = len(nodes)
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for r, weight in atoms:
        if r in nodes:
            raise ValueError("Cauchy atom at node")
        for i in range(n):
            for j in range(n):
                out[i][j] += weight / ((r - nodes[i]) * (r - nodes[j]))
    return out


def target_pin(q, p, c):
    n = len(p)
    qp = matvec(q, p)
    out = [[q[i][j] - c for j in range(n)] for i in range(n)]
    for i in range(n):
        out[i][i] = q[i][i] + (c - qp[i]) / p[i] - c
    return out


def restrict(a, u):
    return matmul(transpose(u), matmul(a, u))


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("Wrong schema")
    nodes = [rat(x) for x in data["nodes"]]
    p = [rat(x) for x in data["p"]]
    metric = [rat(x) for x in data["metric_diagonal"]]
    g = rat(data["frame_floor"])
    rho = rat(data["selected_residual_ratio"])
    omega = rat(data["complete_residual_radius"])
    c = rat(data.get("boundary_scalar", 0))

    n = len(nodes)
    if n < 2 or len(p) != n or len(metric) != n:
        raise ValueError("Dimension mismatch")
    if len(set(nodes)) != n or any(x == 0 for x in p) or sum(p) != 1:
        raise ValueError("Invalid nodes or target")
    if any(x <= 0 for x in metric) or g <= 0 or rho < 0 or omega < 0:
        raise ValueError("Invalid metric or bounds")
    if rho + omega >= g:
        raise ValueError("Final frame/residual ratio does not pass")

    def parse_atoms(rows, positive):
        atoms = []
        for raw in rows:
            r = rat(raw["r"])
            w = rat(raw["weight"])
            if r in nodes or (positive and w <= 0):
                raise ValueError("Invalid atom")
            atoms.append((r, w))
        return atoms

    selected = parse_atoms(data["selected_atoms"], True)
    residual_atoms = parse_atoms(data["residual_atoms"], False)
    qz = cauchy_gram(nodes, selected)
    qrem = cauchy_gram(nodes, residual_atoms)
    z = matvec(qz, p)
    mmat = diag(metric)
    u = complement_basis(p)

    frame_pivots = ldl_positive_pivots(restrict(matsub(qz, matscale(g, mmat)), u))

    coordinate_ratios = []
    for i in range(n):
        value = abs(z[i]) / (abs(p[i]) * metric[i])
        if value > rho:
            raise ValueError(f"Selected coordinate residual failed at {i}")
        coordinate_ratios.append(value)

    selected_pinned = target_pin(qz, p, Fraction(0))
    residual_pinned = target_pin(qrem, p, c)
    plus_pivots = ldl_positive_pivots(
        restrict(matadd(matscale(omega, mmat), residual_pinned), u)
    )
    minus_pivots = ldl_positive_pivots(
        restrict(matsub(matscale(omega, mmat), residual_pinned), u)
    )

    full = matadd(selected_pinned, residual_pinned)
    if any(x != 0 for x in matvec(full, p)):
        raise ValueError("Full target kernel failed")
    full_pivots = ldl_positive_pivots(restrict(full, u))

    canonical_bytes = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical_bytes).hexdigest()
    return {
        "status": "CERTIFIED_ZERO_FRAME_RESIDUAL_ARITHMETIC_COMPLETION",
        "frame_floor": dump_rat(g),
        "selected_coordinate_ratios": [dump_rat(x) for x in coordinate_ratios],
        "selected_frame_ldl_pivots": [dump_rat(x) for x in frame_pivots],
        "complete_residual_radius": dump_rat(omega),
        "residual_plus_ldl_pivots": [dump_rat(x) for x in plus_pivots],
        "residual_minus_ldl_pivots": [dump_rat(x) for x in minus_pivots],
        "final_margin_scalar": dump_rat(g - rho - omega),
        "full_complement_ldl_pivots": [dump_rat(x) for x in full_pivots],
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
