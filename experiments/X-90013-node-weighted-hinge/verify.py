#!/usr/bin/env python3
"""Directed finite witness for R-90005."""
from __future__ import annotations

import json
from pathlib import Path

from mpmath import iv

iv.dps = 70


def lower(x) -> float:
    return float(x.a)


def upper(x) -> float:
    return float(x.b)


def mobius(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    least = [0] * (n + 1)
    for i in range(2, n + 1):
        if least[i] == 0:
            least[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > least[i] or i * p > n:
                break
            least[i * p] = p
            mu[i * p] = 0 if p == least[i] else -mu[i]
    return mu


def coefficient(T: int, j: int):
    mu = mobius(T)
    rootT = iv.sqrt(T)

    def target(q: int):
        return 2 * iv.sqrt(q) - 2 * q / rootT

    u = [iv.mpf(0) for _ in range(T + 3)]
    for m in range(1, T + 1):
        u[m] = iv.fsum(
            mu[k] * target(m * k)
            for k in range(1, T // m + 1)
        )

    tail = [iv.mpf(0) for _ in range(T + 4)]
    for m in range(T, 0, -1):
        tail[m] = tail[m + 1] + u[m]

    return (
        (j + 1) * (j * u[j] - (j - 2) * u[j + 1])
        + 2 * tail[j + 2]
    ) / (j * (j - 1))


def main() -> None:
    first_mutation = None
    finite_minima = []
    for T in range(3, 19):
        values = [(j, coefficient(T, j)) for j in range(2, T)]
        j_min, c_min = min(values, key=lambda item: lower(item[1]))
        finite_minima.append(
            {
                "T": T,
                "row": j_min,
                "lower": lower(c_min),
                "upper": upper(c_min),
            }
        )
        if upper(c_min) < 0 and first_mutation is None:
            first_mutation = (T, j_min, c_min)

    if first_mutation is None or first_mutation[:2] != (18, 3):
        raise AssertionError("first mutation was not T=18,row=3")

    c18 = coefficient(18, 3)
    c24 = coefficient(24, 4)
    if not (-0.016357533249176 < lower(c18) and upper(c18) < -0.016357533249175):
        raise AssertionError("T=18 witness left its retained interval")
    if not (-0.385666938614629 < lower(c24) and upper(c24) < -0.385666938614628):
        raise AssertionError("T=24 witness left its retained interval")

    result = {
        "classification": "PASS_NODE_WEIGHTED_SHARP_AVERAGE_ROW_REFUTATION",
        "first_mutation_scan": finite_minima,
        "load_bearing_witnesses": {
            "T18_row3": [lower(c18), upper(c18)],
            "T24_row4": [lower(c24), upper(c24)],
        },
        "scope": (
            "Finite directed refutation of average-row positivity only; "
            "general balanced-flow and cycle-corrected adapters remain open."
        ),
    }
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
