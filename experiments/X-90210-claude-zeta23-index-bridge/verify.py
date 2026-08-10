#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import random
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"


def dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def wedge_square(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum(
        (a[i] * b[j] - a[j] * b[i]) ** 2
        for i in range(len(a))
        for j in range(i + 1, len(a))
    )


def pair_matrix(a: list[Fraction], b: list[Fraction]) -> list[list[Fraction]]:
    n = len(a)
    return [
        [a[i] * b[j] + b[i] * a[j] for j in range(n)]
        for i in range(n)
    ]


def det3(M: list[list[Fraction]], ids: tuple[int, int, int]) -> Fraction:
    i, j, k = ids
    return (
        M[i][i] * (M[j][j] * M[k][k] - M[j][k] * M[k][j])
        - M[i][j] * (M[j][i] * M[k][k] - M[j][k] * M[k][i])
        + M[i][k] * (M[j][i] * M[k][j] - M[j][j] * M[k][i])
    )


def exact_random_checks(cases: int = 500) -> dict:
    rng = random.Random(90228)
    rank_minor_checks = 0
    sign_product_checks = 0
    wedge_checks = 0

    for _ in range(cases):
        n = rng.randint(2, 8)
        a = [Fraction(rng.randint(-9, 9), rng.randint(1, 7)) for _ in range(n)]
        b = [Fraction(rng.randint(-9, 9), rng.randint(1, 7)) for _ in range(n)]
        A = dot(a, a)
        B = dot(b, b)
        s = dot(a, b)
        wedge = wedge_square(a, b)

        # Lagrange's exact identity: ||a||^2||b||^2-(a.b)^2 is a sum of squares.
        if A * B - s * s != wedge or wedge < 0:
            raise AssertionError((a, b, A * B - s * s, wedge))
        wedge_checks += 1

        # The two possible nonzero eigenvalues are s +/- sqrt(A B), so their
        # product is s^2-A B <= 0: at most one positive and at most one negative.
        if s * s - A * B > 0:
            raise AssertionError((a, b, s * s - A * B))
        sign_product_checks += 1

        # Q=a b^T+b a^T has rank at most two. Every 3x3 minor vanishes exactly.
        Q = pair_matrix(a, b)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if det3(Q, (i, j, k)) != 0:
                        raise AssertionError((a, b, (i, j, k), det3(Q, (i, j, k))))
                    rank_minor_checks += 1

    return {
        "random_cases": cases,
        "lagrange_wedge_identities": wedge_checks,
        "opposite_weak_sign_products": sign_product_checks,
        "vanishing_3x3_minors": rank_minor_checks,
    }


def canonical_near_line_checks() -> dict:
    epsilons = [Fraction(1, 2), Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)]
    rows = []
    for e in epsilons:
        a = [Fraction(1), e]
        b = [Fraction(1), -e]
        Q = pair_matrix(a, b)
        expected = [[Fraction(2), Fraction(0)], [Fraction(0), -2 * e * e]]
        if Q != expected:
            raise AssertionError((e, Q, expected))
        rows.append({
            "epsilon": str(e),
            "positive_eigenvalue": "2",
            "negative_eigenvalue": str(-2 * e * e),
        })
    return {"exact_models": rows}


def constants() -> dict:
    c1 = math.sqrt(2.0) * math.tan(1.0 / math.sqrt(2.0)) / (
        1.0 + (1.0 / math.sqrt(2.0)) * math.tan(1.0 / math.sqrt(2.0))
    )
    line = 2.0 - 1.0 / c1
    pair = (1.0 - line) / 2.0
    distinct = (1.0 + line) / 2.0
    return {
        "c1_star_display": c1,
        "simple_line_fraction_display": line,
        "off_line_pair_budget_display": pair,
        "not_below_tail_fraction_display": distinct,
    }


def main() -> None:
    result = {
        "verdict": "PASS_X_90210_CLAUDE_ZETA23_INDEX_BRIDGE",
        "exact_pullback_checks": exact_random_checks(),
        "near_line_mutation": canonical_near_line_checks(),
        "constants": constants(),
        "scope": (
            "Exact finite-channel rank/inertia algebra and near-line mutation only. "
            "The Claude Zeta23 proportion theorem is imported, not reproved here. "
            "No RH conclusion."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])


if __name__ == "__main__":
    main()
