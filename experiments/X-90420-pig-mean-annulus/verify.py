#!/usr/bin/env python3
"""Exact finite replay for L-90418, R-90411, T-90420, and L-90421.

The checker uses only integer/Fraction arithmetic. It verifies:
  * prefix and source forms of the carry mean;
  * the exact inclusive average-carry kernel;
  * divisor and top-annulus kernel formulas;
  * the corrected PIG/Haar normalization;
  * exact factor-four cancellation below X/4;
  * the explicit two-band annular kernel;
  * the dilation polynomial factorization.

It does not prove the analytic Mellin continuation, the critical mean bound,
deterministic PIG, the repaired global adapter, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def convolve_one(f: list[Fraction]) -> list[Fraction]:
    n = len(f) - 1
    c = [Fraction(0)] * (n + 1)
    for m in range(1, n + 1):
        c[m] = sum((f[d] for d in divisors(m)), Fraction(0))
    return c


def prefix(c: list[Fraction]) -> list[Fraction]:
    C = [Fraction(0)] * len(c)
    for m in range(1, len(c)):
        C[m] = C[m - 1] + c[m]
    return C


def beta(N: int, d: int) -> Fraction:
    q, r = divmod(N, d)
    return Fraction(q * (d - 1 - r), N + 1)


def omega(N: int, d: int) -> Fraction:
    q, r = divmod(N, d)
    return Fraction(q * (d - r), N)


def mean_prefix(c: list[Fraction], N: int) -> Fraction:
    return sum(
        (c[m] * (Fraction(2 * m, N) - 1) for m in range(1, N + 1)),
        Fraction(0),
    )


def mean_source(f: list[Fraction], N: int) -> Fraction:
    return sum((f[d] * omega(N, d) for d in range(1, N + 1)), Fraction(0))


def bridge(c: list[Fraction], N: int) -> list[Fraction]:
    C = prefix(c)
    return [C[N] - C[j] - C[N - j - 1] for j in range(N)]


def haar_numerators(R: list[Fraction]):
    N = len(R)
    ell = 1
    while 2 * ell <= N:
        for u in range(0, N, 2 * ell):
            A = sum(R[u : u + ell], Fraction(0)) - sum(
                R[u + ell : u + 2 * ell], Fraction(0)
            )
            yield ell, A
        ell *= 2


def M(c: list[Fraction], X: int) -> Fraction:
    if X < 1:
        return Fraction(0)
    return sum(
        (c[m] * (Fraction(2 * m, X) - 1) for m in range(1, X + 1)),
        Fraction(0),
    )


def annular(c: list[Fraction], X: int) -> Fraction:
    return 2 * M(c, X) - 3 * M(c, X // 2) + M(c, X // 4)


def annular_explicit(c: list[Fraction], X: int) -> Fraction:
    out = Fraction(0)
    for m in range(X // 4 + 1, X // 2 + 1):
        out += c[m] * (1 - Fraction(8 * m, X))
    for m in range(X // 2 + 1, X + 1):
        out += c[m] * (Fraction(4 * m, X) - 2)
    return out


def make_source(N: int, seed: int) -> list[Fraction]:
    return [Fraction(0)] + [
        Fraction((((seed + 5) * d * d + 3 * d + seed) % 31) - 15, (d + seed) % 9 + 1)
        for d in range(1, N + 1)
    ]


def run() -> dict[str, object]:
    mean_rows = 0
    kernel_rows = 0
    normalization_rows = 0
    annular_rows = 0

    for N in (4, 8, 16, 32, 64, 128, 256, 512):
        for seed in range(1, 10):
            f = make_source(N, seed)
            c = convolve_one(f)
            C = prefix(c)

            mp = mean_prefix(c, N)
            ms = mean_source(f, N)
            assert mp == ms
            assert mp == Fraction(N + 1, N) * sum(
                (f[d] * beta(N, d) for d in range(1, N + 1)), Fraction(0)
            ) + Fraction(C[N], N)
            mean_rows += 1

            for d in range(1, N + 1):
                assert omega(N, d) == Fraction(N + 1, N) * beta(N, d) + Fraction(N // d, N)
                assert omega(N, d) > 0
                assert omega(N, d) <= 1
                if N % d == 0:
                    assert omega(N, d) == 1
                if 2 * d > N:
                    assert omega(N, d) == Fraction(2 * d - N, N)
                kernel_rows += 1

            R = bridge(c, N)
            continuous = sum((x * x for x in R), Fraction(0)) / N
            mean = sum(R, Fraction(0)) / N
            haar = sum((A * A / (2 * ell) for ell, A in haar_numerators(R)), Fraction(0))
            assert continuous == mean * mean + haar / N
            pig = continuous / N
            assert pig == mean * mean / N + haar / (N * N)
            normalization_rows += 1

            if N % 4 == 0:
                assert annular(c, N) == annular_explicit(c, N)
                # Basis-vector firewall: every coefficient at m<=N/4 cancels exactly.
                for m in range(1, N // 4 + 1):
                    e = [Fraction(0)] * (N + 1)
                    e[m] = 1
                    assert annular(e, N) == 0
                annular_rows += 1

    # Polynomial identity 2-3y+y^2=(1-y)(2-y).
    for y in (Fraction(-3, 2), Fraction(-1), Fraction(0), Fraction(1, 3), Fraction(1), Fraction(2), Fraction(5, 2)):
        assert 2 - 3 * y + y * y == (1 - y) * (2 - y)

    return {
        "classification": "PASS_X_90420_PIG_MEAN_ANNULUS",
        "mean_identity_rows": mean_rows,
        "kernel_rows": kernel_rows,
        "normalization_rows": normalization_rows,
        "annular_rows": annular_rows,
        "critical_mean_bound_proved": False,
        "deterministic_pig_proved": False,
        "repaired_pig_to_pole_adapter_proved": False,
        "rh_proved": False,
        "scope": "exact mean/Pascal, normalization, and factor-four annular algebra only",
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
