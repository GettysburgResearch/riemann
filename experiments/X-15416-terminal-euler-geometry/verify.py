#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import comb, gcd
import json
from typing import Dict, List, Tuple


def reduced(a: int, q: int) -> bool:
    return a != 0 and gcd(abs(a), q) == 1


def reduced_solutions(q: int, v: int, r: int, bound: int) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    for a in range(-bound, bound + 1):
        if not reduced(a, q):
            continue
        for b in range(-bound, bound + 1):
            if reduced(b, v) and a * v - b * q == r:
                out.append((a, b))
    return out


def solution_geometry_row(q: int, v: int, r: int, bound: int) -> Dict[str, object]:
    g = gcd(q, v)
    if r % g:
        raise ValueError("row has no integer solution")
    true_step = (q // g, v // g)
    sols = reduced_solutions(q, v, r, bound)
    if not sols:
        raise ValueError("no reduced solution in test box")

    invariant = {a * true_step[1] - b * true_step[0] for a, b in sols}
    false_classes = {(a % q, b % v) for a, b in sols}

    true_step_consistent = True
    a0, b0 = sols[0]
    for a, b in sols:
        da, db = a - a0, b - b0
        if true_step[0] == 0 or da % true_step[0] != 0:
            true_step_consistent = False
            break
        k = da // true_step[0]
        if db != k * true_step[1]:
            true_step_consistent = False
            break

    return {
        "q": q,
        "v": v,
        "r": r,
        "gcd": g,
        "true_step": list(true_step),
        "reduced_solution_count_in_box": len(sols),
        "false_shift_residue_class_count": len(false_classes),
        "false_shift_residue_classes": [list(x) for x in sorted(false_classes)],
        "equation_invariant_count": len(invariant),
        "true_step_consistent": true_step_consistent,
    }


def moment_row(order: int) -> Dict[str, object]:
    values = []
    for degree in range(order):
        value = sum(
            (-1) ** j * comb(order, j) * (j ** degree)
            for j in range(order + 1)
        )
        values.append(value)
    return {
        "difference_order": order,
        "formal_half_pole_moments": values,
        "all_zero": all(value == 0 for value in values),
    }


def exponent_row(delta: Fraction) -> Dict[str, object]:
    amplitude = delta - Fraction(1, 2)
    energy = 2 * delta - 1
    return {
        "delta": str(delta),
        "amplitude_exponent": str(amplitude),
        "energy_exponent": str(energy),
        "contracting": amplitude < 0 and energy < 0,
    }


def build_result() -> Dict[str, object]:
    geometry = [
        solution_geometry_row(5, 5, 5, 50),
        solution_geometry_row(5, 6, 1, 80),
        solution_geometry_row(8, 12, 4, 80),
    ]
    moments = [moment_row(order) for order in range(1, 9)]
    exponents = [
        exponent_row(delta)
        for delta in (
            Fraction(1, 5),
            Fraction(1, 4),
            Fraction(1, 3),
            Fraction(2, 5),
            Fraction(49, 100),
        )
    ]

    fixed_delta = Fraction(1, 5)
    fixed_K = 6
    truncated_variable_excluded = Fraction(1, fixed_K) < fixed_delta

    noncoprime = geometry[0]
    false_step_mutation_rejected = (
        noncoprime["true_step"] != [5, 5]
        and noncoprime["false_shift_residue_class_count"] == 3
    )

    verdict = (
        all(row["true_step_consistent"] for row in geometry)
        and all(row["equation_invariant_count"] == 1 for row in geometry)
        and all(row["all_zero"] for row in moments)
        and all(row["contracting"] for row in exponents)
        and truncated_variable_excluded
        and false_step_mutation_rejected
    )

    return {
        "schema": "X-15416-v1",
        "solution_geometry": geometry,
        "formal_moment_rows": moments,
        "terminal_exponent_rows": exponents,
        "fixed_reserve_control": {
            "delta": str(fixed_delta),
            "K": fixed_K,
            "one_over_K_below_delta": truncated_variable_excluded,
        },
        "false_step_mutation_rejected": false_step_mutation_rejected,
        "verdict": (
            "SYNTHETIC_TERMINAL_EULER_GEOMETRY_VERIFIED"
            if verdict
            else "FAIL"
        ),
        "scope": (
            "exact finite combinatorial algebra only; does not independently "
            "verify the bounded-variation Euler estimate or BTP(K)"
        ),
    }


def main() -> None:
    result = build_result()
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["verdict"] == "FAIL":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
