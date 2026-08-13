#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path


def matvec(K, mu):
    return [
        sum((mu[i] * K[i][j] for i in range(len(mu))), Fraction(0))
        for j in range(len(K[0]))
    ]


def add(*vectors):
    return [sum(xs, Fraction(0)) for xs in zip(*vectors)]


def main():
    K = [
        [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6), Fraction(0)],
        [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)],
        [Fraction(0), Fraction(0), Fraction(2, 5), Fraction(3, 5)],
    ]
    assert all(sum(row, Fraction(0)) == 1 for row in K)

    mu1 = [Fraction(2, 7), Fraction(1, 8), Fraction(0)]
    mu2 = [Fraction(1, 7), Fraction(0), Fraction(3, 10)]
    slack = [Fraction(1, 14), Fraction(1, 4), Fraction(1, 5)]
    mu = add(mu1, mu2, slack)

    nu1 = matvec(K, mu1)
    nu2 = matvec(K, mu2)
    nu0 = matvec(K, slack)
    nu = matvec(K, mu)
    assert add(nu1, nu2, nu0) == nu

    resp1 = [x * Fraction(4, 5) for x in nu1]
    resp2 = [x * Fraction(7, 8) for x in nu2]
    assert all(x <= y for x, y in zip(add(resp1, resp2), nu))

    sigma = Fraction(1000, 1003)
    assert add([sigma*x for x in nu1], [sigma*x for x in nu2],
               [sigma*x for x in nu0]) == [sigma*x for x in nu]

    out = {
        "classification": "PASS_TRANSPORT_DISINTEGRATION_AND_SINGLE_TARGET_LEDGER",
        "source_states": len(mu),
        "target_states": len(nu),
        "colored_branches": 2,
        "markov_rows_exact": True,
        "target_partition_exact": True,
        "single_global_safety_scaling_exact": True,
        "scope": "Exact Fraction replay of the measure-disintegration algebra. The Riemann application depends on the positive source partition and continuous-column theorems cited by L-91325."
    }
    path = Path(__file__).resolve().parent / "results" / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(out["classification"])


if __name__ == "__main__":
    main()
