#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


def matmul(a, b):
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def subtract(a, b):
    return [
        [a[i][j] - b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def add(a, b):
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def determinant_2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def physical_matrix(a, b):
    return [
        [2 * a - b, -2 * (a - b)],
        [a - b, 2 * b - a],
    ]


H = [
    [Fraction(2), Fraction(-3)],
    [Fraction(-3), Fraction(5)],
]
IDENTITY = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
]


def defect(a, b):
    matrix = physical_matrix(a, b)
    return subtract(H, matmul(matmul(transpose(matrix), H), matrix))


def verify():
    pairs = [
        (Fraction(9, 10), Fraction(4, 5)),
        (Fraction(20, 21), Fraction(6, 7)),
        (Fraction(35, 36), Fraction(11, 12)),
        (Fraction(99, 100), Fraction(49, 50)),
    ]

    exact_checks = 0
    for a, b in pairs:
        current = defect(a, b)
        u = 1 - a * a
        v = 1 - b * b
        expected = [
            [u + v, -u - 2 * v],
            [-u - 2 * v, u + 4 * v],
        ]
        assert current == expected
        assert current[0][0] >= 0
        assert current[1][1] >= 0
        assert determinant_2(current) == u * v >= 0
        exact_checks += 1

    product = IDENTITY
    telescoped = [
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    for a, b in pairs[:3]:
        current_defect = defect(a, b)
        telescoped = add(
            telescoped,
            matmul(matmul(transpose(product), current_defect), product),
        )
        product = matmul(physical_matrix(a, b), product)

    assert telescoped == subtract(
        H,
        matmul(matmul(transpose(product), H), product),
    )

    product_a = Fraction(1)
    product_b = Fraction(1)
    for a, b in pairs[:3]:
        product_a *= a
        product_b *= b
    assert product == physical_matrix(product_a, product_b)

    inverse_h = [
        [Fraction(5), Fraction(3)],
        [Fraction(3), Fraction(2)],
    ]
    sharp = [[Fraction(1), Fraction(2)]]
    score = [[Fraction(2), Fraction(1)]]
    assert matmul(matmul(sharp, inverse_h), transpose(sharp))[0][0] == 25
    assert matmul(matmul(score, inverse_h), transpose(score))[0][0] == 34

    result = {
        "classification": "PASS_COMMON_ROUGH_HILBERT_COLLIGATION",
        "single_packet_exact_checks": exact_checks,
        "three_factor_telescope": True,
        "product_diagonalization": True,
        "metric": {"H": [[2, -3], [-3, 5]], "determinant": 1},
        "functional_energy_constants": {"sharp": 25, "endpoint_score": 34},
        "scope": "All identities use exact Fraction arithmetic.",
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    verify()
