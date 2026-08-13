#!/usr/bin/env python3
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


def physical_matrix(a, b):
    return [
        [2 * a - b, -2 * (a - b)],
        [a - b, 2 * b - a],
    ]


def positive_dilation(a, b):
    return [
        [a, 0, 0, 0],
        [0, a, 0, 0],
        [0, 0, b, 0],
        [0, 0, 0, b],
    ]


OBSERVATION = [
    [2, -2, -1, 1],
    [1, -1, -1, 1],
]

PAIRS = [
    (Fraction(9, 10), Fraction(4, 5)),
    (Fraction(20, 21), Fraction(6, 7)),
    (Fraction(35, 36), Fraction(11, 12)),
]


def verify():
    checks = 0
    for a, b in PAIRS:
        assert matmul(OBSERVATION, positive_dilation(a, b)) == matmul(
            physical_matrix(a, b), OBSERVATION
        )
        checks += 1

    product_4 = [
        [Fraction(int(i == j)) for j in range(4)]
        for i in range(4)
    ]
    product_2 = [
        [Fraction(int(i == j)) for j in range(2)]
        for i in range(2)
    ]
    product_a = Fraction(1)
    product_b = Fraction(1)

    for a, b in PAIRS:
        product_4 = matmul(positive_dilation(a, b), product_4)
        product_2 = matmul(physical_matrix(a, b), product_2)
        product_a *= a
        product_b *= b

    assert product_4 == positive_dilation(product_a, product_b)
    assert product_2 == physical_matrix(product_a, product_b)
    assert matmul(OBSERVATION, product_4) == matmul(product_2, OBSERVATION)

    state = [Fraction(7), Fraction(3), Fraction(11), Fraction(5)]
    initial_mass = sum(state)
    loss = Fraction(0)
    current = state[:]

    for a, b in PAIRS:
        loss += (1 - a) * (current[0] + current[1])
        loss += (1 - b) * (current[2] + current[3])
        current = [
            a * current[0],
            a * current[1],
            b * current[2],
            b * current[3],
        ]

    assert initial_mass - sum(current) == loss

    sharp = [4, -4, -3, 3]
    score = [5, -5, -3, 3]
    assert sharp == [OBSERVATION[0][i] + 2 * OBSERVATION[1][i] for i in range(4)]
    assert score == [2 * OBSERVATION[0][i] + OBSERVATION[1][i] for i in range(4)]

    result = {
        "classification": "PASS_POSITIVE_FOUR_STATE_ROUGH_DILATION",
        "single_packet_intertwining_checks": checks,
        "three_factor_composition": True,
        "linear_mass_telescope": True,
        "sharp_observation": sharp,
        "score_observation": score,
        "scope": "All identities use exact Fraction arithmetic.",
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    verify()
