#!/usr/bin/env python3
"""Exact rational replay for L-105320.

Checks finite root-compression and Schur identities only. It does not replay
the spectral angle perturbation theorem, the Xi saddle analysis, CRDB, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pder(a):
    return trim([Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)])


def peval(a, x):
    out = Fraction(0)
    for c in reversed(a):
        out = out * x + c
    return out


def pscale(a, c):
    return trim([c * x for x in a])


def pfromroots(roots):
    out = [Fraction(1)]
    for root in roots:
        out = pmul(out, [Fraction(-root), Fraction(1)])
    return out


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def charpoly(a):
    """Monic characteristic polynomial, ascending coefficient order."""
    n = len(a)
    powers = []
    power = eye(n)
    for _ in range(1, n + 1):
        power = matmul(power, a)
        powers.append(trace(power))
    elementary = [Fraction(1)]
    for k in range(1, n + 1):
        value = sum(
            ((-1) ** (i - 1)) * elementary[k - i] * powers[i - 1]
            for i in range(1, k + 1)
        ) / k
        elementary.append(value)
    out = [Fraction(0)] * (n + 1)
    for k in range(n + 1):
        out[n - k] = ((-1) ** k) * elementary[k]
    return trim(out)


def solve(a, b):
    n = len(a)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if m[i][col] != 0)
        m[col], m[pivot] = m[pivot], m[col]
        value = m[col][col]
        m[col] = [x / value for x in m[col]]
        for i in range(n):
            if i != col and m[i][col] != 0:
                factor = m[i][col]
                m[i] = [m[i][j] - factor * m[col][j] for j in range(n + 1)]
    return [m[i][-1] for i in range(n)]


def build_compression(roots):
    roots = list(map(Fraction, roots))
    n = len(roots)
    r = n - 1
    # Basis f_j=e_j-e_n of the zero-sum space. Gram matrix is I+J.
    gram = [[Fraction(int(i == j)) + 1 for j in range(r)] for i in range(r)]
    gram_inv = [
        [Fraction(int(i == j)) - Fraction(1, n) for j in range(r)]
        for i in range(r)
    ]
    form = [
        [Fraction(int(i == j)) * roots[i] + roots[-1] for j in range(r)]
        for i in range(r)
    ]
    compression = matmul(gram_inv, form)
    mean = sum(roots) / n
    # Coordinates of sqrt(n)b=P D (1,...,1)^T.
    coupling = [roots[i] - mean for i in range(r)]
    return gram, compression, coupling, mean


def schur_scalar(gram, compression, coupling, z, n):
    r = len(compression)
    matrix = [
        [Fraction(int(i == j)) * z - compression[i][j] for j in range(r)]
        for i in range(r)
    ]
    vector = solve(matrix, coupling)
    gram_vector = [
        sum(gram[i][j] * vector[j] for j in range(r)) for i in range(r)
    ]
    return sum(coupling[i] * gram_vector[i] for i in range(r)) / n


def run():
    fixtures = [
        (-4, -1, 2),
        (-5, -2, 1, 4),
        (-7, -3, 0, 2, 8),
        (-9, -4, -1, 3, 6, 11),
    ]
    checks = 0
    records = []
    for roots in fixtures:
        p = pfromroots(roots)
        dp = pder(p)
        gram, compression, coupling, mean = build_compression(roots)
        cp = charpoly(compression)
        assert cp == pscale(dp, Fraction(1, len(roots)))
        checks += 1

        for z0 in range(-12, 15):
            z = Fraction(z0)
            if peval(p, z) == 0 or peval(dp, z) == 0:
                continue
            scalar = schur_scalar(gram, compression, coupling, z, len(roots))
            rhs = Fraction(1, len(roots)) * (z - mean - scalar)
            assert rhs == peval(p, z) / peval(dp, z)
            checks += 1

        gram_coupling = [
            sum(gram[i][j] * coupling[j] for j in range(len(coupling)))
            for i in range(len(coupling))
        ]
        bnorm2 = sum(
            coupling[i] * gram_coupling[i] for i in range(len(coupling))
        ) / len(roots)
        variance = sum((Fraction(x) - mean) ** 2 for x in roots)
        assert bnorm2 == variance / len(roots)
        checks += 1

        records.append(
            {
                "roots": list(roots),
                "compression_charpoly": [str(x) for x in cp],
                "coupling_norm_squared": str(bnorm2),
            }
        )

    result = {
        "verdict": "PASS_X_105320_ROOT_COMPRESSION_SCHUR",
        "arithmetic_class": "EXACT_RATIONAL",
        "checks": checks,
        "fixtures": records,
        "spectral_angle_bound_replayed": False,
        "analytic_xi_saddle_replayed": False,
        "crdb_proved": False,
        "rh_established": False,
    }
    result["proof_object"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def main():
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
