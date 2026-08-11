#!/usr/bin/env python3
from __future__ import annotations

from argparse import ArgumentParser
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
import json
import random


def carry(N: int, d: int, j: int) -> int:
    return N // d - j // d - (N - j) // d


def residue_covariance(d: int, e: int) -> Fraction:
    L = lcm(d, e)
    den = L * L
    sx = sy = sxy = 0
    for u in range(L):
        for v in range(L):
            x = int(v % d > u % d)
            y = int(v % e > u % e)
            sx += x
            sy += y
            sxy += x * y
    return Fraction(sxy, den) - Fraction(sx, den) * Fraction(sy, den)


def jordan_2(n: int) -> int:
    out = n * n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            out = out // (p * p) * (p * p - 1)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out = out // (m * m) * (m * m - 1)
    return out


def covariance_quadratic(coeff: dict[int, int]) -> Fraction:
    return sum(
        (
            Fraction(a * b * (gcd(d, e) ** 2 - 1), 4 * d * e)
            for d, a in coeff.items()
            for e, b in coeff.items()
        ),
        Fraction(0),
    )


def jordan_quadratic(coeff: dict[int, int]) -> Fraction:
    D = max(coeff, default=1)
    out = Fraction(0)
    for q in range(2, D + 1):
        inner = sum(
            (Fraction(a, d) for d, a in coeff.items() if d % q == 0),
            Fraction(0),
        )
        out += Fraction(jordan_2(q), 4) * inner * inner
    return out


def brownian_row(coeff: list[int]) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    N = len(coeff) - 1
    M = N - 1
    prefix = [0]
    for x in coeff[1:]:
        prefix.append(prefix[-1] + x)

    rows = [prefix[N] - prefix[j] - prefix[N - j] for j in range(1, N)]
    mean = Fraction(sum(rows), M)
    lhs = sum(((Fraction(x) - mean) ** 2 for x in rows), Fraction(0)) / M

    rhs = Fraction(0)
    for m in range(1, N // 2 + 1):
        dm = coeff[N + 1 - m] - coeff[m]
        tm = Fraction(N + 1 - 2 * m, M)
        for r in range(1, N // 2 + 1):
            dr = coeff[N + 1 - r] - coeff[r]
            tr = Fraction(N + 1 - 2 * r, M)
            rhs += dm * dr * (min(tm, tr) - tm * tr)

    mean_formula = Fraction(
        sum((2 * m - N - 1) * coeff[m] for m in range(1, N + 1)), M
    )
    return lhs, rhs, mean, mean_formula


def fixed_endpoint_covariance(N: int, d: int, e: int) -> Fraction:
    xs = [carry(N, d, j) for j in range(N)]
    ys = [carry(N, e, j) for j in range(N)]
    mx = Fraction(sum(xs), N)
    my = Fraction(sum(ys), N)
    return sum(
        ((Fraction(x) - mx) * (Fraction(y) - my) for x, y in zip(xs, ys)),
        Fraction(0),
    ) / N


def run() -> dict[str, object]:
    residue_rows = 0
    for d in range(2, 25):
        for e in range(2, 25):
            got = residue_covariance(d, e)
            want = Fraction(gcd(d, e) ** 2 - 1, 4 * d * e)
            assert got == want, (d, e, got, want)
            residue_rows += 1

    rng = random.Random(90417)
    jordan_rows = 0
    for D in range(2, 15):
        for _ in range(20):
            coeff = {d: rng.randint(-4, 4) for d in range(2, D + 1)}
            assert covariance_quadratic(coeff) == jordan_quadratic(coeff)
            jordan_rows += 1

    brownian_rows = 0
    for N in range(3, 41):
        for _ in range(20):
            coeff = [0] + [rng.randint(-5, 5) for _ in range(N)]
            lhs, rhs, mean, mean_formula = brownian_row(coeff)
            assert lhs == rhs, (N, lhs, rhs)
            assert mean == mean_formula, (N, mean, mean_formula)
            brownian_rows += 1

    assert fixed_endpoint_covariance(100, 49, 47) == Fraction(8, 125)
    assert fixed_endpoint_covariance(100, 40, 45) == Fraction(76, 625)

    return {
        "classification": "PASS_X_90416_BROWNIAN_JORDAN_CARRY_DUALITY",
        "residue_covariance_rows": residue_rows,
        "jordan_factorization_rows": jordan_rows,
        "brownian_bridge_rows": brownian_rows,
        "fixed_endpoint_witnesses": 2,
        "pig_proved": False,
        "rh_proved": False,
        "scope": (
            "exact finite carry covariance, Brownian reflection normal form, "
            "Jordan-2 factorization, and fixed-endpoint firewall only"
        ),
    }


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.json is None:
        print(payload, end="")
    else:
        args.json.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
