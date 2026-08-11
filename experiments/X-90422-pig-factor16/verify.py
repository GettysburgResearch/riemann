#!/usr/bin/env python3
"""Exact finite replay for L-90422.

Uses only integer/Fraction arithmetic. It verifies:
  * M_(Lambda-D4 Lambda+a4)=H-4H(X/4)+M_a4;
  * the five-scale coefficient vector (2,-3,-7,12,-4);
  * exact cancellation of every basis vector at m<=X/16;
  * the four piecewise-linear annular bands;
  * Q(y)=(1-y)(2-y)(1-2y)(1+2y).

It does not prove Mellin continuation, critical growth, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def triangular_mean(a: list[Fraction], X: int) -> Fraction:
    if X < 1:
        return Fraction(0)
    return sum(
        (a[m] * (Fraction(2 * m, X) - 1) for m in range(1, X + 1)),
        Fraction(0),
    )


def d4(a: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * len(a)
    for m in range(4, len(a), 4):
        out[m] = 4 * a[m // 4]
    return out


def atom4(n: int) -> list[Fraction]:
    out = [Fraction(0)] * (n + 1)
    p = 4
    while p <= n:
        out[p] = 3
        p *= 4
    return out


def combine(*vectors: list[Fraction]) -> list[Fraction]:
    n = max(len(v) for v in vectors)
    out = [Fraction(0)] * n
    for v in vectors:
        for i, x in enumerate(v):
            out[i] += x
    return out


def scale(v: list[Fraction], q: int) -> list[Fraction]:
    return [q * x for x in v]


def A4(M, X: int) -> Fraction:
    return 2 * M(X) - 3 * M(X // 2) + M(X // 4)


def B16(lam: list[Fraction], X: int) -> Fraction:
    coeffs = (2, -3, -7, 12, -4)
    return sum(
        (
            q * triangular_mean(lam, X // (2**r))
            for r, q in enumerate(coeffs)
        ),
        Fraction(0),
    )


def kernel16(m: int, X: int) -> Fraction:
    # Canonical exact cutoff convention from the five-scale sum.
    out = Fraction(0)
    coeffs = (2, -3, -7, 12, -4)
    for r, q in enumerate(coeffs):
        Y = X // (2**r)
        if m <= Y:
            out += q * (Fraction(2 * m, Y) - 1)
    return out


def make_lambda(n: int, seed: int) -> list[Fraction]:
    return [Fraction(0)] + [
        Fraction((((seed + 7) * m * m + 5 * m + seed) % 37) - 18, (m + 2 * seed) % 11 + 1)
        for m in range(1, n + 1)
    ]


def run() -> dict[str, object]:
    relation_rows = 0
    support_rows = 0
    kernel_rows = 0

    for X in (16, 32, 64, 128, 256, 512, 1024):
        for seed in range(1, 10):
            lam = make_lambda(X, seed)
            at = atom4(X)
            c = combine(lam, scale(d4(lam), -1), at)

            lhs_M = triangular_mean(c, X)
            rhs_M = (
                triangular_mean(lam, X)
                - 4 * triangular_mean(lam, X // 4)
                + triangular_mean(at, X)
            )
            assert lhs_M == rhs_M

            lhs_A = A4(lambda Y: triangular_mean(c, Y), X)
            rhs_A = B16(lam, X) + A4(lambda Y: triangular_mean(at, Y), X)
            assert lhs_A == rhs_A
            relation_rows += 1

            direct = sum((lam[m] * kernel16(m, X) for m in range(1, X + 1)), Fraction(0))
            assert direct == B16(lam, X)
            kernel_rows += X

        for m in range(1, X // 16 + 1):
            assert kernel16(m, X) == 0
            support_rows += 1

        # Interior controls for the four displayed bands.
        for m in range(X // 16 + 1, X // 8 + 1):
            assert kernel16(m, X) == Fraction(128 * m, X) - 4
        for m in range(X // 8 + 1, X // 4 + 1):
            assert kernel16(m, X) == 8 - Fraction(64 * m, X)
        for m in range(X // 4 + 1, X // 2 + 1):
            assert kernel16(m, X) == 1 - Fraction(8 * m, X)
        for m in range(X // 2 + 1, X + 1):
            assert kernel16(m, X) == Fraction(4 * m, X) - 2

    for y in (
        Fraction(-3, 2),
        Fraction(-1),
        Fraction(-1, 2),
        Fraction(0),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(1),
        Fraction(2),
        Fraction(5, 2),
    ):
        q = 2 - 3 * y - 7 * y * y + 12 * y**3 - 4 * y**4
        assert q == (1 - y) * (2 - y) * (1 - 2 * y) * (1 + 2 * y)

    return {
        "classification": "PASS_X_90422_PIG_FACTOR16_NORMAL_FORM",
        "relation_rows": relation_rows,
        "support_rows": support_rows,
        "kernel_rows": kernel_rows,
        "critical_growth_proved": False,
        "rh_proved": False,
        "scope": "exact five-scale, support, kernel, and polynomial algebra only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
