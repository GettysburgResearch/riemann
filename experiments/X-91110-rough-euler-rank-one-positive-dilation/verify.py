#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def lift(a, b):
    d = a - b
    return [
        [2 * a - b, F(0), F(0)],
        [d, b, F(0)],
        [F(0), d, a],
    ]


def physical(a, b):
    d = a - b
    return [[2 * a - b, -2 * d], [d, 2 * b - a]]


J = [[F(1), F(0), F(-2)], [F(0), F(1), F(-1)]]
PAIRS = [
    (F(9, 10), F(4, 5)),
    (F(7, 8), F(2, 3)),
    (F(3, 4), F(1, 4)),
    (F(1), F(1)),
]


def main():
    checks = 0
    for a, b in PAIRS:
        assert 0 <= b <= a
        lifted = lift(a, b)
        phys = physical(a, b)
        assert matmul(J, lifted) == matmul(phys, J)
        checks += 1

        for l, r, z in [
            (F(0), F(0), F(0)),
            (F(1), F(2), F(0)),
            (F(3, 2), F(5, 3), F(7, 5)),
        ]:
            source = [[l], [r], [z]]
            out = matmul(lifted, source)
            assert all(value[0] >= 0 for value in out)
            assert matmul(J, out) == matmul(phys, matmul(J, source))
            checks += 1

    for a1, b1 in PAIRS:
        for a2, b2 in PAIRS:
            lifted_product = matmul(lift(a1, b1), lift(a2, b2))
            physical_product = matmul(physical(a1, b1), physical(a2, b2))
            assert matmul(J, lifted_product) == matmul(physical_product, J)
            assert all(value >= 0 for row in lifted_product for value in row)
            checks += 1

    for a, b in PAIRS:
        d = a - b
        for l, r in [(F(0), F(1)), (F(2), F(3))]:
            out = matmul(physical(a, b), [[l], [r]])
            corrected = [[out[0][0] + 2 * d * r], [out[1][0] + d * r]]
            assert corrected == [[(2 * a - b) * l], [d * l + b * r]]
            assert all(value[0] >= 0 for value in corrected)
            checks += 1

        if d > 0:
            tau = F(999, 1000) * d
            assert -2 * d + 2 * tau < 0
            checks += 1

    result = {
        "classification": "PASS_ROUGH_EULER_RANK_ONE_POSITIVE_DILATION",
        "checks": checks,
        "generic_pairs": [[str(a), str(b)] for a, b in PAIRS],
        "scope": (
            "Exact Fraction algebra checks the fixed positive three-state "
            "dilation, arbitrary two-factor composition, rank-one port "
            "correction and its minimality along the square-root ray."
        ),
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
