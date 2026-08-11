#!/usr/bin/env python3
"""Exact finite regression for L-90416/L-90417.

Uses only integer/Fraction arithmetic. It verifies:
  * bridge cell and reflection identities;
  * first-difference identity;
  * exact discrete Haar Parseval;
  * triangular-window formula for every standard Haar coefficient;
  * the finite fine-scale energy bound;
  * the radix-four triangular/Haar scaling identity;
  * the harmless four-adic atom carry bound.

This is finite algebra only. It does not prove the coarse-Haar gate,
deterministic PIG, the repaired PIG-to-pole adapter, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def prefix(c: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * len(c)
    for i in range(1, len(c)):
        out[i] = out[i - 1] + c[i]
    return out


def bridge(c: list[Fraction]) -> list[Fraction]:
    n = len(c) - 1
    C = prefix(c)
    return [C[n] - C[j] - C[n - j - 1] for j in range(n)]


def haar_intervals(n: int) -> Iterable[tuple[int, int]]:
    ell = 1
    while 2 * ell <= n:
        for u in range(0, n, 2 * ell):
            yield u, ell
        ell *= 2


def haar_numerator(R: list[Fraction], u: int, ell: int) -> Fraction:
    return sum(R[u : u + ell], Fraction(0)) - sum(
        R[u + ell : u + 2 * ell], Fraction(0)
    )


def triangular(c: list[Fraction], u: int, ell: int) -> Fraction:
    return sum(
        (min(t, 2 * ell - t) * c[u + t] for t in range(1, 2 * ell)),
        Fraction(0),
    )


def check_vector(c: list[Fraction], fine_cut: int) -> dict[str, int]:
    n = len(c) - 1
    assert n > 0 and n & (n - 1) == 0
    R = bridge(c)

    for j in range(n):
        assert R[n - 1 - j] == R[j]
    for j in range(1, n):
        assert R[j] - R[j - 1] == c[n - j] - c[j]

    # Exact unnormalised Haar Parseval:
    # sum R_j^2 = (sum R_j)^2/n + sum A_(u,l)^2/(2l).
    lhs = sum((x * x for x in R), Fraction(0))
    rhs = sum(R, Fraction(0)) ** 2 / n

    haar_rows = 0
    fine_energy = Fraction(0)
    for u, ell in haar_intervals(n):
        A = haar_numerator(R, u, ell)
        assert A == triangular(c, u, ell) - triangular(c, n - u - 2 * ell, ell)
        rhs += A * A / (2 * ell)
        haar_rows += 1
        if ell <= fine_cut:
            fine_energy += A * A / (2 * ell)
    assert lhs == rhs

    diff_energy = sum(
        ((c[n - j] - c[j]) ** 2 for j in range(1, n)), Fraction(0)
    )
    coeff_energy = sum((c[j] ** 2 for j in range(1, n)), Fraction(0))
    assert diff_energy <= 4 * coeff_energy
    # Safe theorem constant: sum_(dyadic ell<=L) ell^2/2 < L^2.
    assert fine_energy <= fine_cut * fine_cut * diff_energy
    assert fine_energy <= 4 * fine_cut * fine_cut * coeff_energy

    return {
        "bridge_rows": n,
        "difference_rows": max(0, n - 1),
        "haar_rows": haar_rows,
        "fine_bound_rows": 1,
    }


def q4_scaled(lam: list[Fraction]) -> list[Fraction]:
    m = len(lam) - 1
    out = [Fraction(0)] * (4 * m + 1)
    for r in range(1, m + 1):
        out[4 * r] = 4 * lam[r]
    return out


def check_q4(n: int) -> int:
    assert n % 4 == 0 and n & (n - 1) == 0
    lam = [Fraction(0)] + [
        Fraction(((17 * r + 5) % 19) - 9, (r % 5) + 1)
        for r in range(1, n // 4 + 1)
    ]
    d = q4_scaled(lam)
    rows = 0
    for u, ell in haar_intervals(n):
        if ell < 4:
            continue
        assert u % 4 == 0 and ell % 4 == 0
        assert triangular(d, u, ell) == 16 * triangular(lam, u // 4, ell // 4)
        ref = n - u - 2 * ell
        assert triangular(d, ref, ell) == 16 * triangular(
            lam, ref // 4, ell // 4
        )
        rows += 1
    return rows


def check_atoms(n: int) -> int:
    atom = [Fraction(0)] * (n + 1)
    p = 4
    count = 0
    while p <= n:
        atom[p] = 1
        count += 1
        p *= 4
    R = bridge(atom)
    assert all(abs(x) <= 3 * count for x in R)
    assert sum((x * x for x in R), Fraction(0)) <= n * (3 * count) ** 2
    return n


def make_vector(n: int, seed: int) -> list[Fraction]:
    return [Fraction(0)] + [
        Fraction(
            (((seed + 11) * m * m + 7 * m + 3 * seed) % 29) - 14,
            (m + seed) % 7 + 1,
        )
        for m in range(1, n + 1)
    ]


def run() -> dict[str, object]:
    totals = {
        "bridge_rows": 0,
        "difference_rows": 0,
        "haar_rows": 0,
        "fine_bound_rows": 0,
        "q4_scaling_rows": 0,
        "atom_rows": 0,
    }
    for n in (2, 4, 8, 16, 32, 64, 128, 256):
        cut = 1
        while 2 * cut <= int(n**0.5):
            cut *= 2
        for seed in range(1, 8):
            got = check_vector(make_vector(n, seed), cut)
            for key, value in got.items():
                totals[key] += value
        if n >= 16:
            totals["q4_scaling_rows"] += check_q4(n)
            totals["atom_rows"] += check_atoms(n)

    return {
        "classification": "PASS_X_90416_PIG_HAAR_LOCALIZATION",
        **totals,
        "deterministic_pig_proved": False,
        "repaired_pig_to_pole_adapter_proved": False,
        "rh_proved": False,
        "scope": (
            "exact bridge/Haar algebra, fine-scale energy bound, radix-four "
            "Haar scaling, and finite atom bound only"
        ),
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
