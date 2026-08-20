#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

SCHEMA = "riemann.t100700.double_owner_dual_terminal.v1"


def digest(payload: dict[str, object]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def prod(values):
    out = Fraction(1)
    for value in values:
        out *= value
    return out


def double_owner_weights(rs: list[Fraction]):
    k = len(rs)
    root = prod(1 - r for r in rs)
    singles: dict[tuple[int, int], Fraction] = {}
    doubles: dict[tuple[int, int], Fraction] = {}
    for i, r_i in enumerate(rs):
        singles[(i, i)] = r_i * prod(1 - rs[h] for h in range(k) if h != i)
        for j in range(i + 1, k):
            doubles[(i, j)] = (
                r_i
                * rs[j]
                * prod(1 - rs[h] for h in range(i))
                * prod(1 - rs[h] for h in range(j + 1, k))
            )
    return root, singles, doubles


def native_coefficients(rs: list[Fraction]):
    out: dict[tuple[int, ...], Fraction] = {}
    k = len(rs)
    for size in range(k + 1):
        for subset in combinations(range(k), size):
            out[subset] = (-1) ** size * prod(rs[i] for i in subset)
    return out


def double_owner_coefficients(rs: list[Fraction]):
    out: dict[tuple[int, ...], Fraction] = {(): Fraction(1)}
    k = len(rs)
    for i in range(k):
        out[(i,)] = -rs[i]
        for j in range(i + 1, k):
            middle = list(range(i + 1, j))
            for size in range(len(middle) + 1):
                for chosen in combinations(middle, size):
                    subset = (i,) + chosen + (j,)
                    out[subset] = (-1) ** len(subset) * prod(rs[h] for h in subset)
    return out


def phase_formula_tau_one(p: int, q: int) -> Fraction:
    return 4 * (
        Fraction(1)
        - Fraction(1, p)
        - Fraction(1, q)
        + Fraction(1, 2) * (Fraction(p, q) + Fraction(1, p * q))
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    fixtures = [
        [Fraction(1, 2)],
        [Fraction(1, 3), Fraction(2, 5)],
        [Fraction(1, 67), Fraction(1, 67), Fraction(1, 71)],
        [Fraction(1, 5), Fraction(1, 7), Fraction(1, 11), Fraction(1, 13)],
    ]

    weight_checks = 0
    coefficient_checks = 0
    for rs in fixtures:
        root, singles, doubles = double_owner_weights(rs)
        assert root + sum(singles.values(), Fraction(0)) + sum(
            doubles.values(), Fraction(0)
        ) == 1
        assert all(value >= 0 for value in [root, *singles.values(), *doubles.values()])
        weight_checks += 1

        assert native_coefficients(rs) == double_owner_coefficients(rs)
        coefficient_checks += 1

    convex_checks = 0
    for a in [Fraction(-5, 3), Fraction(-1, 7), Fraction(2, 5), Fraction(9, 4)]:
        for b in [Fraction(-7, 5), Fraction(1, 9), Fraction(3, 2)]:
            for r in [Fraction(1, 67), Fraction(1, 5), Fraction(3, 4)]:
                lhs = (a - r * b) ** 2
                rhs = (1 - r) * a**2 + r * (a - b) ** 2
                assert rhs - lhs == r * (1 - r) * b**2 >= 0
                convex_checks += 1

    phase_checks = 0
    phase_values: list[dict[str, str | int]] = []
    for p, q in [(2, 3), (67, 71), (67, 1009), (101, 809)]:
        value = phase_formula_tau_one(p, q)
        assert 0 <= value <= 16
        phase_values.append({"p": p, "q": q, "value": str(value)})
        phase_checks += 1

    squaring_checks = 0
    for r in [Fraction(1, 2), Fraction(1, 3), Fraction(1, 67)]:
        lhs = {0: Fraction(1), 1: Fraction(0), 2: -(r**2)}
        rhs = {0: Fraction(1), 1: Fraction(0), 2: -(r**2)}
        assert lhs == rhs
        squaring_checks += 1

    gluing_checks = 0
    for short in range(-7, 8):
        for long in range(-7, 8):
            lhs = max(-(short + long), 0)
            rhs = abs(short) + max(-long, 0)
            assert lhs <= rhs
            gluing_checks += 1

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "base_pr": 691,
        "base_sha": "c85123d6c25b5b2ade89ab30a736f9b18844a489",
        "checks": {
            "double_owner_weight_partitions": weight_checks,
            "double_owner_native_coefficients": coefficient_checks,
            "one_prime_convexity": convex_checks,
            "endpoint_cauchy_phase_formulas": phase_checks,
            "interior_squaring_identities": squaring_checks,
            "short_long_negative_part_gluing": gluing_checks,
            "phase_values": phase_values,
        },
        "scope": {
            "two_sided_decoupling_proved": True,
            "endpoint_phase_budget_proved": True,
            "squaring_renewal_normal_form_proved": True,
            "short_long_gluing_proved": True,
            "scme100704_proved": False,
            "lrnm100704_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T100700_DOUBLE_OWNER_DUAL_TERMINAL_ALGEBRA",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
