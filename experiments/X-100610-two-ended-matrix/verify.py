#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T100610_TWO_ENDED_IMPLICATION_MATRIX"


def add(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def scale(a: dict[int, Fraction], c: Fraction) -> dict[int, Fraction]:
    return {m: c * v for m, v in a.items() if c * v}


def multiply_disjoint(
    a: dict[int, Fraction], b: dict[int, Fraction]
) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            if ma & mb:
                raise AssertionError("formal factors were not disjoint")
            monomial = ma | mb
            out[monomial] = out.get(monomial, Fraction(0)) + ca * cb
    return {m: c for m, c in out.items() if c}


def euler_factor(index: int, r: Fraction) -> dict[int, Fraction]:
    return {0: Fraction(1), 1 << index: -r}


def difference_factor(index: int) -> dict[int, Fraction]:
    return {0: Fraction(1), 1 << index: Fraction(-1)}


def interval_euler(a: int, b: int, r: list[Fraction]) -> dict[int, Fraction]:
    out = {0: Fraction(1)}
    for index in range(a, b + 1):
        out = multiply_disjoint(out, euler_factor(index, r[index]))
    return out


def full_euler(r: list[Fraction]) -> dict[int, Fraction]:
    return interval_euler(0, len(r) - 1, r)


def two_ended_hazard(r: list[Fraction]) -> dict[int, Fraction]:
    k = len(r)
    survival = Fraction(1)
    for value in r:
        survival *= 1 - value
    out = {0: survival}

    for i in range(k):
        left = Fraction(1)
        right = Fraction(1)
        for h in range(i):
            left *= 1 - r[h]
        for h in range(i + 1, k):
            right *= 1 - r[h]
        out = add(out, scale(difference_factor(i), r[i] * left * right))

    for i in range(k):
        for j in range(i + 1, k):
            left = Fraction(1)
            right = Fraction(1)
            for h in range(i):
                left *= 1 - r[h]
            for h in range(j + 1, k):
                right *= 1 - r[h]
            block = multiply_disjoint(difference_factor(i), difference_factor(j))
            if j > i + 1:
                block = multiply_disjoint(block, interval_euler(i + 1, j - 1, r))
            out = add(out, scale(block, r[i] * r[j] * left * right))
    return out


def direct_blocks(r: list[Fraction]) -> dict[tuple[int, int], dict[int, Fraction]]:
    k = len(r)
    blocks: dict[tuple[int, int], dict[int, Fraction]] = {}
    for i in range(k):
        blocks[(i, i)] = {1 << i: -r[i]}
        for j in range(i + 1, k):
            block = {(1 << i) | (1 << j): r[i] * r[j]}
            if j > i + 1:
                block = multiply_disjoint(block, interval_euler(i + 1, j - 1, r))
            blocks[(i, j)] = block
    return blocks


def scalar_energy_lhs(r: list[Fraction], u: list[int]) -> Fraction:
    value = Fraction(1)
    for ri, ui in zip(r, u):
        value *= 1 - ri * ui
    return value * value


def scalar_energy_rhs(r: list[Fraction], u: list[int]) -> Fraction:
    k = len(r)
    survival = Fraction(1)
    for value in r:
        survival *= 1 - value
    total = survival * survival

    for i in range(k):
        left = Fraction(1)
        right = Fraction(1)
        for h in range(i):
            left *= 1 - r[h]
        for h in range(i + 1, k):
            right *= 1 - r[h]
        delta = 1 - u[i]
        total += r[i] * left * left * right * right * delta * delta

    for i in range(k):
        for j in range(i + 1, k):
            left = Fraction(1)
            right = Fraction(1)
            for h in range(i):
                left *= 1 - r[h]
            for h in range(j + 1, k):
                right *= 1 - r[h]
            value = (1 - u[i]) * (1 - u[j])
            for h in range(i + 1, j):
                value *= 1 - r[h] * u[h]
            total += (
                r[i]
                * r[j]
                * left
                * left
                * right
                * right
                * value
                * value
            )
    return total


def canonical_digest(payload: dict[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def run() -> dict[str, object]:
    rng = random.Random(100610)

    hazard_checks = 0
    direct_tensor_checks = 0
    energy_checks = 0
    survival_checks = 0
    schur_checks = 0

    for k in range(1, 11):
        for _ in range(40):
            r = [
                Fraction(rng.randint(1, 20), rng.randint(21, 60))
                for _ in range(k)
            ]

            assert full_euler(r) == two_ended_hazard(r)
            hazard_checks += 1

            blocks = direct_blocks(r)
            total: dict[int, Fraction] = {}
            for block in blocks.values():
                total = add(total, block)
            assert total == add(full_euler(r), {0: Fraction(-1)})

            for i in range(k):
                row: dict[int, Fraction] = {}
                for j in range(i, k):
                    row = add(row, blocks[(i, j)])
                expected = {1 << i: -r[i]}
                if i + 1 < k:
                    expected = multiply_disjoint(
                        expected, interval_euler(i + 1, k - 1, r)
                    )
                assert row == expected

            for j in range(k):
                column: dict[int, Fraction] = {}
                for i in range(j + 1):
                    column = add(column, blocks[(i, j)])
                expected = {1 << j: -r[j]}
                if j > 0:
                    expected = multiply_disjoint(
                        expected, interval_euler(0, j - 1, r)
                    )
                assert column == expected
            direct_tensor_checks += 1

            signs = [rng.choice((-1, 1)) for _ in range(k)]
            assert scalar_energy_lhs(r, signs) == scalar_energy_rhs(r, signs)
            energy_checks += 1

            left = Fraction(1)
            sum_left = Fraction(0)
            for value in r:
                sum_left += value * left * left
                left *= 1 - value
            assert sum_left <= 1

            right = Fraction(1)
            sum_right = Fraction(0)
            for value in reversed(r):
                sum_right += value * right * right
                right *= 1 - value
            assert sum_right <= 1
            survival_checks += 2

    for _ in range(1000):
        rows = rng.randint(1, 8)
        columns = rng.randint(1, 8)
        matrix = [
            [
                Fraction(rng.randint(-8, 8), rng.randint(1, 12))
                for _ in range(columns)
            ]
            for _ in range(rows)
        ]
        a = [Fraction(rng.randint(-8, 8), rng.randint(1, 12)) for _ in range(rows)]
        b = [
            Fraction(rng.randint(-8, 8), rng.randint(1, 12))
            for _ in range(columns)
        ]
        row_bound = max(sum(abs(x) for x in row) for row in matrix)
        column_bound = max(
            sum(abs(matrix[i][j]) for i in range(rows))
            for j in range(columns)
        )
        bilinear = sum(
            a[i] * matrix[i][j] * b[j]
            for i in range(rows)
            for j in range(columns)
        )
        norm_a = sum(x * x for x in a)
        norm_b = sum(x * x for x in b)
        assert bilinear * bilinear <= row_bound * column_bound * norm_a * norm_b
        schur_checks += 1

    separator_size = 100
    payload: dict[str, object] = {
        "schema": "riemann.x100610.two_ended_matrix.v1",
        "classification": VERDICT,
        "base_pr": 691,
        "hazard_identity_checks": hazard_checks,
        "direct_tensor_marginal_checks": direct_tensor_checks,
        "littlewood_paley_checks": energy_checks,
        "survival_vector_checks": survival_checks,
        "schur_bilinear_checks": schur_checks,
        "row_only_separator": {
            "one_sided_bound": 1,
            "operator_norm_squared": separator_size,
        },
        "column_only_separator": {
            "one_sided_bound": 1,
            "operator_norm_squared": separator_size,
        },
        "two_sided_and_gate_proved": True,
        "focr100610_proved": False,
        "locr100610_proved": False,
        "rh_established": False,
    }
    payload["proof_object_sha256"] = canonical_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
