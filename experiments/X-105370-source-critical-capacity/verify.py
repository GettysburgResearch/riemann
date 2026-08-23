#!/usr/bin/env python3
"""Exact rational replay for L-105370, L-105372 and T-105371.

The checker authenticates finite polynomial/source-moment identities and exact
matrix capacity fixtures. It does not evaluate Xi or prove any RH-bearing gate.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

Q = Fraction


def derivative(p: list[Q]) -> list[Q]:
    return [Q(i) * p[i] for i in range(1, len(p))] or [Q(0)]


def evaluate(p: list[Q], x: Q) -> Q:
    value = Q(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def series_ratio(p: list[Q], q: list[Q], count: int) -> list[Q]:
    """First count coefficients of P(t)/Q(t), assuming Q(0)!=0."""
    assert q and q[0] != 0
    out: list[Q] = []
    for n in range(count):
        rhs = p[n] if n < len(p) else Q(0)
        rhs -= sum((q[j] * out[n - j] for j in range(1, min(n, len(q) - 1) + 1)), Q(0))
        out.append(rhs / q[0])
    return out


def zeros(rows: int, cols: int) -> list[list[Q]]:
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def identity(n: int) -> list[list[Q]]:
    return [[Q(1) if i == j else Q(0) for j in range(n)] for i in range(n)]


def add(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(c: Q, a: list[list[Q]]) -> list[list[Q]]:
    return [[c * x for x in row] for row in a]


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [
        [sum((a[i][r] * b[r][j] for r in range(len(b))), Q(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def trace(a: list[list[Q]]) -> Q:
    return sum((a[i][i] for i in range(len(a))), Q(0))


def determinant(a: list[list[Q]]) -> Q:
    m = [row[:] for row in a]
    n = len(m)
    det = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            det = -det
        pv = m[col][col]
        det *= pv
        for r in range(col + 1, n):
            if m[r][col] == 0:
                continue
            factor = m[r][col] / pv
            for j in range(col, n):
                m[r][j] -= factor * m[col][j]
    return det


def inverse(a: list[list[Q]]) -> list[list[Q]]:
    n = len(a)
    aug = [a[i][:] + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        assert pivot is not None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r == col or aug[r][col] == 0:
                continue
            factor = aug[r][col]
            aug[r] = [x - factor * y for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def moment_matrix(moments: list[Q], k: int, shift: int) -> list[list[Q]]:
    return [[moments[r + s + shift] for s in range(k)] for r in range(k)]


def atom_moments(atoms: list[tuple[Q, Q]], count: int) -> list[Q]:
    """Atoms are (weight, location)."""
    return [sum((w * s**n for w, s in atoms), Q(0)) for n in range(count)]


def check_polynomial_source_splits() -> int:
    checks = 0

    # Odd cubic F=z^3-3z. Critical points +/-1 have rho=-1/3.
    f_odd = [Q(0), Q(-3), Q(0), Q(1)]
    df_odd = derivative(f_odd)
    ddf_odd = derivative(df_odd)
    for c in (Q(-1), Q(1)):
        assert evaluate(df_odd, c) == 0
        assert evaluate(f_odd, c) / evaluate(ddf_odd, c) == Q(-1, 3)
        checks += 1
    odd_source = series_ratio([Q(-3), Q(1)], [Q(-3), Q(3)], 10)
    odd_critical = atom_moments([(Q(2, 3), Q(1))], 10)
    odd_boundary = [Q(1, 3)] + [Q(0)] * 9

    # Even quartic F=z^4-2z^2+3/4. Critical points 0,+/-1.
    f_even = [Q(3, 4), Q(0), Q(-2), Q(0), Q(1)]
    df_even = derivative(f_even)
    ddf_even = derivative(df_even)
    expected = {Q(0): Q(-3, 16), Q(-1): Q(-1, 32), Q(1): Q(-1, 32)}
    for c, rho in expected.items():
        assert evaluate(df_even, c) == 0
        assert evaluate(f_even, c) / evaluate(ddf_even, c) == rho
        checks += 1
    even_ratio = series_ratio([Q(3, 4), Q(-2), Q(1)], [Q(-4), Q(4)], 11)
    rho0 = Q(-3, 16)
    assert even_ratio[0] == rho0
    even_source = even_ratio[1:11]
    even_critical = atom_moments([(Q(1, 16), Q(1))], 10)
    even_boundary = [Q(1, 4)] + [Q(0)] * 9

    fixtures = [
        (odd_source, odd_critical, odd_boundary),
        (even_source, even_critical, even_boundary),
    ]

    # Twelve exact coefficient splits.
    for source, critical, boundary in fixtures:
        for n in range(6):
            assert source[n] == critical[n] + boundary[n]
            checks += 1

    # Sixteen exact ordinary/shifted matrix splits.
    for source, critical, boundary in fixtures:
        for k in range(1, 5):
            for shift in (0, 1):
                a = moment_matrix(source, k, shift)
                c = moment_matrix(critical, k, shift)
                s = moment_matrix(boundary, k, shift)
                assert a == add(c, s)
                checks += 1

    # Two order-one capacity checks.
    assert odd_critical[0] <= odd_source[0]
    checks += 1
    assert even_critical[0] <= even_source[0]
    checks += 1

    return checks


def check_capacity_normal_form() -> int:
    # Three positive source atoms. The critical measure consumes exactly one
    # quarter of every source weight, so C=(1/4)A and S=(3/4)A.
    source_atoms = [
        (Q(1), Q(1, 4)),
        (Q(2), Q(1)),
        (Q(3), Q(4)),
    ]
    critical_atoms = [(w / 4, s) for w, s in source_atoms]
    boundary_atoms = [(3 * w / 4, s) for w, s in source_atoms]

    source = atom_moments(source_atoms, 8)
    critical = atom_moments(critical_atoms, 8)
    boundary = atom_moments(boundary_atoms, 8)
    checks = 0

    for k in range(1, 4):
        for shift in (0, 1):
            a = moment_matrix(source, k, shift)
            c = moment_matrix(critical, k, shift)
            s = moment_matrix(boundary, k, shift)
            inv_a = inverse(a)

            assert matmul(a, inv_a) == identity(k)
            checks += 1
            assert a == add(c, s)
            checks += 1
            assert determinant(a) > 0
            checks += 1
            assert determinant(s) > 0
            checks += 1

            normalized_trace = trace(matmul(inv_a, c))
            assert normalized_trace == Q(k, 4)
            checks += 1
            assert normalized_trace <= 1
            checks += 1

    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "polynomial_source_split_checks": check_polynomial_source_splits(),
        "capacity_normal_form_checks": check_capacity_normal_form(),
    }
    total = sum(counts.values())
    assert total == 71

    result = {
        "verdict": "PASS_X_105370_SOURCE_CRITICAL_CAPACITY",
        "arithmetic_class": "EXACT_RATIONAL_MOMENT_CAPACITY",
        "checks": total,
        "counts": counts,
        "crvh105330_proved_for_xi": False,
        "oscc105371_proved_for_xi": False,
        "sclc105371_proved_for_xi": False,
        "rh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print("PASS_X_105370_SOURCE_CRITICAL_CAPACITY")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
