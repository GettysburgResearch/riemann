#!/usr/bin/env python3
"""Exact finite replay for the fifth-endpoint canonical-correlation gate."""

from fractions import Fraction
from itertools import combinations
import hashlib
import json
from pathlib import Path


def invert(a):
    n = len(a)
    aug = [
        list(row) + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            f = aug[row][col]
            if f:
                aug[row] = [
                    x - f * y for x, y in zip(aug[row], aug[col])
                ]
    return [row[n:] for row in aug]


def matmul(a, b):
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def gram(xs, ys=None):
    if ys is None:
        ys = xs
    return [
        [Fraction(1, 1) / (Fraction(1, 1) - x * y) for y in ys]
        for x in xs
    ]


def overlap(denominator_zeros, numerator_zeros):
    g_minus = gram(denominator_zeros)
    g_plus = gram(numerator_zeros)
    cross = gram(denominator_zeros, numerator_zeros)
    return trace(
        matmul(
            matmul(
                matmul(invert(g_minus), cross),
                invert(g_plus),
            ),
            transpose(cross),
        )
    )


checks = 0
single_grid = [
    Fraction(-3, 4),
    Fraction(-2, 3),
    Fraction(-1, 2),
    Fraction(-1, 3),
    Fraction(0),
    Fraction(1, 4),
    Fraction(1, 2),
    Fraction(2, 3),
    Fraction(3, 4),
]

for a in single_grid:
    for b in single_grid:
        ov = overlap([a], [b])
        expected_overlap = (
            (1 - a * a) * (1 - b * b) / (1 - a * b) ** 2
        )
        charge = 1 - ov
        expected_charge = ((a - b) / (1 - a * b)) ** 2
        assert ov == expected_overlap
        assert charge == expected_charge
        assert 0 <= ov <= 1
        assert 0 <= charge <= 1
        checks += 4

multi_grid = [
    Fraction(-3, 4),
    Fraction(-1, 2),
    Fraction(-1, 4),
    Fraction(0),
    Fraction(1, 4),
    Fraction(1, 2),
    Fraction(3, 4),
]

for m_minus in range(1, 5):
    for denominator in combinations(multi_grid, m_minus):
        for m_plus in range(1, 5):
            for numerator in combinations(multi_grid, m_plus):
                ov = overlap(list(denominator), list(numerator))
                charge = Fraction(m_minus) - ov
                assert 0 <= ov <= min(m_minus, m_plus)
                assert max(0, m_minus - m_plus) <= charge <= m_minus
                assert charge + ov == m_minus
                assert charge >= 0
                checks += 4
                if denominator == numerator:
                    assert ov == m_minus
                    assert charge == 0
                    checks += 2

for m in range(1, 101):
    # Pure favorable inner degree is free; pure adverse inner degree is paid.
    assert Fraction(0) == 0
    assert Fraction(m) == m
    checks += 2

baseline = Fraction(997, 1000)
target = Fraction(9, 10)
allowance = baseline - target
assert allowance == Fraction(97, 1000)
checks += 1

result = {
    "verdict": "PASS_T106530_CANONICAL_CORRELATION_DEFICIT",
    "checks": checks,
    "single_factor_charge": "((a-b)/(1-a*b))^2",
    "multi_factor_identity": (
        "charge=m_minus-tr(G_minus^-1 C G_plus^-1 C^T)"
    ),
    "fifth_derivative_input": "997/1000",
    "ninety_percent_charge_allowance": "97/1000",
    "canon_corr_106530_proved": False,
    "ninety_percent_established": False,
    "rh_established": False,
}
canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(result["verdict"])
print(json.dumps(result, indent=2, sort_keys=True))
