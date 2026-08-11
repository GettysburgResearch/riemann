#!/usr/bin/env python3
"""Finite algebra regression for L-90603/L-90604/R-90602."""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def harmonic(N: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, N + 1)), Fraction(0))


def log_weights(N: int) -> list[Fraction]:
    h = harmonic(N)
    return [Fraction(1, k) / h for k in range(1, N + 1)]


def green_weights(N: int) -> list[Fraction]:
    raw = [Fraction(math.comb(2 * k, k) ** 2, 16 ** k) for k in range(1, N + 1)]
    total = sum(raw, Fraction(0))
    return [w / total for w in raw]


def C(K: int, n: int) -> Fraction:
    return Fraction(4 * math.factorial(K) ** 4,
                    math.factorial(K - n) ** 2 * math.factorial(K + n) ** 2)


def leading_coefficients(N: int, weights: list[Fraction]) -> list[Fraction]:
    out = []
    for n in range(1, N + 1):
        out.append(Fraction(1, 2) * sum(
            (weights[K - 1] * C(K, n) for K in range(n, N + 1)),
            Fraction(0),
        ))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rows = []
    exact_weight_checks = 0
    coefficient_checks = 0

    for N in [10, 20, 40, 60]:
        for name, maker in [("log", log_weights), ("green", green_weights)]:
            weights = maker(N)
            assert sum(weights, Fraction(0)) == 1
            assert all(w > 0 for w in weights)
            exact_weight_checks += len(weights) + 1

            top_start = (N + 1) // 2
            top_mass = sum(weights[top_start - 1:], Fraction(0))
            scaled_top = float(top_mass) * math.log(N)
            assert scaled_top > 0.55

            beta = leading_coefficients(N, weights)
            assert all(Fraction(0) < b <= 2 for b in beta)
            coefficient_checks += len(beta)

            # Every termwise multiple ratio is controlled by the same exact
            # C_(K,mp)/C_(K,p) ratio used in the analytic theorem.
            for p in range(2, max(3, int(math.sqrt(N))) + 1):
                for m in range(2, N // p + 1):
                    for K in range(m * p, N + 1):
                        lhs = C(K, m * p) / C(K, p)
                        assert lhs > 0
                        assert lhs <= 1
                        coefficient_checks += 1

            rows.append({
                "N": N,
                "mixture": name,
                "top_mass_times_log_N": scaled_top,
                "min_leading_coefficient": float(min(beta)),
                "max_leading_coefficient": float(max(beta)),
            })

    result = {
        "classification": "PASS_X_90602_BROWNIAN_MIXTURE_INSTABILITY",
        "exact_weight_checks": exact_weight_checks,
        "coefficient_checks": coefficient_checks,
        "mixture_rows": rows,
        "scope": (
            "Finite mixture algebra only; the off-line high-frequency theorem "
            "is the written selected-prime/Steinhaus/Kronecker/Rouche proof."
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
