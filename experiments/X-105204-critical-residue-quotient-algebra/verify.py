#!/usr/bin/env python3
"""Exact finite replay for L-105204 critical-residue quotient algebra.

This replay authenticates exact polynomial algebra only. It does not prove
the Xi saddle theorem, the high-derivative asymptotics, CRDB105200, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import List, Tuple

Poly = List[Fraction]
Matrix = List[List[Fraction]]


def trim(a: Poly) -> Poly:
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def sub(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] -= x
    return trim(out)


def scale(a: Poly, c: Fraction) -> Poly:
    return trim([c * x for x in a])


def mul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def derivative(a: Poly) -> Poly:
    if len(a) <= 1:
        return [Fraction(0)]
    return trim([Fraction(i) * a[i] for i in range(1, len(a))])


def divrem(a: Poly, b: Poly) -> Tuple[Poly, Poly]:
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError("zero polynomial")
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while r != [0] and len(r) >= len(b):
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        r = sub(r, [Fraction(0)] * k + scale(b, c))
    return trim(q), trim(r)


def mod_poly(a: Poly, modulus: Poly) -> Poly:
    return divrem(a, modulus)[1]


def egcd(a: Poly, b: Poly) -> Tuple[Poly, Poly, Poly]:
    r0, r1 = trim(a), trim(b)
    s0, s1 = [Fraction(1)], [Fraction(0)]
    t0, t1 = [Fraction(0)], [Fraction(1)]
    while r1 != [0]:
        q, r = divrem(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, sub(s0, mul(q, s1))
        t0, t1 = t1, sub(t0, mul(q, t1))
    lc = r0[-1]
    return scale(r0, 1 / lc), scale(s0, 1 / lc), scale(t0, 1 / lc)


def inverse_mod(a: Poly, modulus: Poly) -> Poly:
    g, s, _ = egcd(a, modulus)
    if g != [Fraction(1)]:
        raise ValueError("not invertible modulo modulus")
    return mod_poly(s, modulus)


def multiplication_matrix(poly: Poly, modulus: Poly) -> Matrix:
    d = len(modulus) - 1
    columns: Matrix = []
    for j in range(d):
        basis = [Fraction(0)] * j + [Fraction(1)]
        r = mod_poly(mul(poly, basis), modulus)
        r += [Fraction(0)] * (d - len(r))
        columns.append(r)
    return [[columns[j][i] for j in range(d)] for i in range(d)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def matpow(a: Matrix, exponent: int) -> Matrix:
    n = len(a)
    result = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    base = [row[:] for row in a]
    e = exponent
    while e:
        if e & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        e >>= 1
    return result


def trace(a: Matrix) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def determinant(a: Matrix) -> Fraction:
    m = [row[:] for row in a]
    n = len(m)
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            out = -out
        value = m[col][col]
        out *= value
        for j in range(col, n):
            m[col][j] /= value
        for r in range(col + 1, n):
            factor = m[r][col]
            if factor:
                for j in range(col, n):
                    m[r][j] -= factor * m[col][j]
    return out


def resultant(f: Poly, g: Poly) -> Fraction:
    f, g = trim(f), trim(g)
    m, n = len(f) - 1, len(g) - 1
    fd, gd = list(reversed(f)), list(reversed(g))
    matrix: Matrix = []
    for i in range(n):
        matrix.append(
            [Fraction(0)] * i + fd + [Fraction(0)] * (n - 1 - i)
        )
    for i in range(m):
        matrix.append(
            [Fraction(0)] * i + gd + [Fraction(0)] * (m - 1 - i)
        )
    return determinant(matrix)


def charpoly(a: Matrix) -> Poly:
    """Monic characteristic polynomial by Newton identities, ascending order."""
    n = len(a)
    power_traces = [Fraction(0)] + [trace(matpow(a, k)) for k in range(1, n + 1)]
    elementary = [Fraction(1)]
    for k in range(1, n + 1):
        value = sum(
            ((-1) ** (i - 1)) * elementary[k - i] * power_traces[i]
            for i in range(1, k + 1)
        ) / k
        elementary.append(value)
    out = [Fraction(0)] * (n + 1)
    for k in range(n + 1):
        out[n - k] = ((-1) ** k) * elementary[k]
    return trim(out)


def evaluate(a: Poly, x: Fraction) -> Fraction:
    out = Fraction(0)
    for c in reversed(a):
        out = out * x + c
    return out


def critical_operator(p: Poly) -> Tuple[Poly, Matrix]:
    p1 = derivative(p)
    p2 = derivative(p1)
    inverse = inverse_mod(p2, p1)
    u = mod_poly(mul(p, inverse), p1)
    return u, multiplication_matrix(u, p1)


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def check_resultant_identity(p: Poly, u_matrix: Matrix) -> int:
    n = len(p) - 1
    p1 = derivative(p)
    p2 = derivative(p1)
    denominator = Fraction(n * n) * resultant(p1, p2)
    cp = charpoly(u_matrix)
    checks = 0
    for lam in map(Fraction, (-5, -2, -1, 0, 1, 2, 5, 11)):
        numerator = resultant(p1, sub(scale(p2, lam), p))
        assert evaluate(cp, lam) == numerator / denominator
        checks += 1
    return checks


def run() -> dict:
    quartic = list(map(Fraction, (2, 0, -2, 0, 1)))
    u4, U4 = critical_operator(quartic)
    expected_traces = {
        1: Fraction(-1, 4),
        2: Fraction(9, 32),
        3: Fraction(-31, 256),
        4: Fraction(129, 2048),
    }
    actual_traces = {r: trace(matpow(U4, r)) for r in expected_traces}
    assert actual_traces == expected_traces
    assert u4 == [Fraction(-1, 2), Fraction(0), Fraction(5, 8)]

    k4 = Fraction(37, 432)
    cross_debt = Fraction(-169, 864)
    assert actual_traces[2] == k4 - cross_debt
    count = check_resultant_identity(quartic, U4)

    cubic = list(map(Fraction, (0, -3, 0, 1)))
    u3, U3 = critical_operator(cubic)
    assert u3 == [Fraction(-1, 3)]
    assert trace(U3) == Fraction(-2, 3)
    assert trace(matpow(U3, 2)) == Fraction(2, 9)
    cubic_coherence = trace(U3) ** 2 / (2 * trace(matpow(U3, 2)))
    assert cubic_coherence == 1
    count += check_resultant_identity(cubic, U3)

    quartic_variance = actual_traces[2] - actual_traces[1] ** 2 / 3
    quartic_coherence = actual_traces[1] ** 2 / (3 * actual_traces[2])
    assert quartic_variance == Fraction(25, 96)
    assert quartic_coherence == Fraction(2, 27)
    assert quartic_coherence == 1 - quartic_variance / actual_traces[2]

    lower, upper = Fraction(1), Fraction(5)
    kant = 4 * lower * upper / (lower + upper) ** 2
    assert kant == Fraction(5, 9) > Fraction(1, 2)

    result = {
        "verdict": "PASS_X_105204_CRITICAL_RESIDUE_QUOTIENT_ALGEBRA",
        "arithmetic_class": "EXACT_RATIONAL",
        "resultant_point_checks": count,
        "quartic_interpolant_u": [fstr(x) for x in u4],
        "quartic_trace_moments": {
            str(r): fstr(value) for r, value in actual_traces.items()
        },
        "quartic_root_ledger_k4": fstr(k4),
        "quartic_cross_residue_debt": fstr(cross_debt),
        "quartic_centered_variance": fstr(quartic_variance),
        "quartic_coherence": fstr(quartic_coherence),
        "cubic_interpolant_u": [fstr(x) for x in u3],
        "cubic_coherence": fstr(cubic_coherence),
        "analytic_xi_saddle_replayed": False,
        "crdb105200_proved": False,
        "rh_established": False,
    }
    result["proof_object"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object"])
    print("RH_UNPROVEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
