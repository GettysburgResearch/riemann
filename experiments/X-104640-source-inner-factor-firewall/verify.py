#!/usr/bin/env python3
"""Exact finite replay for T-104640.

This checks only the algebraic identities and finite-dimensional projection
statements in the packet.  It does not prove the analytic Xi asymptotics, the
microscopic model-space estimate, more than ninety percent, or RH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import functools
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Q = Fraction


def poly_add(a: list[Q], b: list[Q]) -> list[Q]:
    n = max(len(a), len(b))
    out = [Q(0) for _ in range(n)]
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a: list[Q], c: Q) -> list[Q]:
    return [c * x for x in a]


def apply_diag_poly(poly: list[Q], vector: list[Q]) -> list[Q]:
    """Apply p(X) when X w^k = k w^k."""
    out: list[Q] = []
    for k, coeff in enumerate(vector):
        value = sum(a * Q(k) ** j for j, a in enumerate(poly))
        out.append(coeff * value)
    return out


def vec_add(a: list[Q], b: list[Q]) -> list[Q]:
    return [x + y for x, y in zip(a, b, strict=True)]


def vec_scale(c: Q, a: list[Q]) -> list[Q]:
    return [c * x for x in a]


def dot(a: list[Q], b: list[Q]) -> Q:
    return sum((x * y for x, y in zip(a, b, strict=True)), Q(0))


def mat_vec(a: list[list[Q]], x: list[Q]) -> list[Q]:
    return [dot(row, x) for row in a]


def inverse(a: list[list[Q]]) -> list[list[Q]]:
    n = len(a)
    aug = [
        row[:] + [Q(int(i == j)) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            f = aug[r][col]
            if f:
                aug[r] = [
                    x - f * y for x, y in zip(aug[r], aug[col], strict=True)
                ]
    return [row[n:] for row in aug]


def norm2(v: Iterable[Q]) -> Q:
    return sum((x * x for x in v), Q(0))


def canonical_hash(payload: dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def run() -> dict[str, object]:
    checks = 0

    # L-104637 polynomial Bezout identity.
    x = [Q(0), Q(1)]
    one_minus_x = [Q(1), Q(-1)]
    two_minus_x = [Q(2), Q(-1)]
    a_poly = [
        Q(11, 2),
        Q(-25, 2),
        Q(15),
        Q(-10),
        Q(7, 2),
        Q(-1, 2),
    ]
    lhs = poly_add(
        poly_mul(x, a_poly),
        poly_scale(poly_mul(two_minus_x, functools_reduce(poly_mul, [one_minus_x] * 5)), Q(1, 2)),
    )
    assert lhs == [Q(1)]
    checks += 1

    # Exact c+cos(nt) frozen-source fixture in the w=e^{-int} coordinate.
    c = Q(2)
    h = [Q(1, 2), c, Q(1, 2)]
    xh = apply_diag_poly(x, h)
    r0 = apply_diag_poly(two_minus_x, h)
    one_minus_x_5 = functools_reduce(poly_mul, [one_minus_x] * 5)
    h5 = apply_diag_poly(one_minus_x_5, h)
    c5 = apply_diag_poly(x, h5)
    r5 = apply_diag_poly(two_minus_x, h5)

    assert xh == [Q(0), c, Q(1)]
    assert r0 == [Q(1), c, Q(0)]
    assert h5 == [Q(1, 2), Q(0), Q(-1, 2)]
    assert c5 == [Q(0), Q(0), Q(-1)]
    assert r5 == [Q(1), Q(0), Q(0)]
    checks += 5

    # Apply the exact 2x2 polynomial matrix M(X) to d=(Xh,R5).
    m11 = poly_mul(two_minus_x, a_poly)
    m12 = poly_scale(two_minus_x, Q(1, 2))
    m21 = one_minus_x_5
    m22 = [Q(0)]
    n1 = vec_add(apply_diag_poly(m11, xh), apply_diag_poly(m12, r5))
    n2 = vec_add(apply_diag_poly(m21, xh), apply_diag_poly(m22, r5))
    assert n1 == r0
    assert n2 == c5
    checks += 2

    # Product quotient: D=w(c+w), N=-w^2(1+cw).
    den = poly_mul(xh, r5)
    num = poly_mul(r0, c5)
    assert den == [Q(0), c, Q(1)]
    assert num == [Q(0), Q(0), Q(-1), -c]
    checks += 2

    # In z=e^{int}, U=-(z+c)/(z(cz+1)).
    # For c=2, numerator zero -2 lies outside, denominator zeros 0 and -1/2 lie inside.
    assert abs(-c) > 1
    assert abs(-Q(1, 1) / c) < 1
    checks += 2

    # Grade-zero collapse.  Domain dimension one; ambient Hilbert space Q^8.
    source = [Q(1) for _ in range(8)]
    p_a_source = source[:7] + [Q(0)]
    d_diag = [Q(i) for i in range(1, 9)]
    z_cols: list[list[Q]] = []
    for r in range(7):
        z_cols.append(
            [
                (d_diag[i] ** r if i < 7 else Q(0)) * source[i]
                for i in range(8)
            ]
        )
    assert z_cols[0] == p_a_source
    checks += 1

    g = [[dot(z_cols[s], z_cols[r]) for s in range(7)] for r in range(7)]
    b = [dot(z_cols[r], source) for r in range(7)]
    e0 = [Q(1)] + [Q(0)] * 6
    assert b == mat_vec(g, e0)
    checks += 1

    exact_residual = norm2(vec_add(source, vec_scale(Q(-1), p_a_source)))
    assert exact_residual == 1
    checks += 1

    tau = Q(1, 10)
    g_tau = [
        [g[i][j] + (tau if i == j else Q(0)) for j in range(7)]
        for i in range(7)
    ]
    inv = inverse(g_tau)
    c_tau = mat_vec(inv, b)
    y = [Q(0) for _ in range(8)]
    for coeff, z in zip(c_tau, z_cols, strict=True):
        y = vec_add(y, vec_scale(coeff, z))
    direct_ridge = norm2(vec_add(source, vec_scale(Q(-1), y)))

    inv_e0 = mat_vec(inv, e0)
    g_inv_e0 = mat_vec(g, inv_e0)
    ridge_excess = tau * tau * dot(inv_e0, g_inv_e0)
    assert direct_ridge == exact_residual + ridge_excess
    assert ridge_excess > 0
    checks += 2

    # Exact budget constants inherited by the topological unit spectrum.
    sharp = Q(1001, 1000) * Q(21, 1000) + Q(17, 25000)
    self_contained = Q(1001, 1000) * Q(13, 500) + Q(13, 4000)
    assert sharp == Q(21701, 1_000_000)
    assert self_contained == Q(7319, 250_000)
    checks += 2

    payload: dict[str, object] = {
        "schema": "riemann.x104640.source-inner-factor-firewall.v1",
        "classification": "PASS_T104640_SOURCE_INNER_FACTOR_FIREWALL",
        "finite_checks": checks,
        "bezout_identity_verified": True,
        "frozen_source_transport_zero_residual_verified": True,
        "countermodel_numerator_inner_degree": 0,
        "countermodel_denominator_inner_degree": 2,
        "countermodel_canonical_charge_per_period": 2,
        "grade_zero_is_exact_model_projection": True,
        "higher_krylov_grades_create_new_source_leverage": False,
        "ridge_excess_positive": True,
        "sharp_topological_threshold": {
            "numerator": sharp.numerator,
            "denominator": sharp.denominator,
        },
        "self_contained_topological_threshold": {
            "numerator": self_contained.numerator,
            "denominator": self_contained.denominator,
        },
        "universal_source_to_inner_promotion_proved": False,
        "selfkrylov104636_proved": False,
        "more_than_ninety_percent_established": False,
        "rh_established": False,
    }
    payload["proof_object_sha256"] = canonical_hash(payload)
    return payload


def functools_reduce(function, iterable):
    return functools.reduce(function, iterable)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"checks={payload['finite_checks']}")
    print("more_than_ninety_percent_established=false")
    print("rh_established=false")


if __name__ == "__main__":
    main()
