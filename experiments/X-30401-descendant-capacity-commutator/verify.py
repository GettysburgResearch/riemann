#!/usr/bin/env python3
"""Exact regression for descendant capacity and terminal commutator lifting.

Standard-library only.  The checker authenticates finite combinatorial and
rational identities.  It does not verify the all-generation source manifest,
Cycle Debt, or RH.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def add_flow(
    target: dict[tuple[int, int], Fraction],
    edge: tuple[int, int],
    value: Fraction,
) -> None:
    target[edge] = target.get(edge, Fraction(0)) + value
    if target[edge] == 0:
        del target[edge]


def add_scaled(
    target: dict[tuple[int, int], Fraction],
    source: dict[tuple[int, int], Fraction],
    scale: Fraction,
) -> None:
    for edge, value in source.items():
        add_flow(target, edge, scale * value)


@lru_cache(maxsize=None)
def central_tree_items(n: int) -> tuple[tuple[tuple[int, int], Fraction], ...]:
    if n <= 1:
        return tuple()
    j = n // 2
    flow: dict[tuple[int, int], Fraction] = {(n, j): Fraction(1)}
    for edge, value in central_tree_items(j):
        add_flow(flow, edge, value)
    for edge, value in central_tree_items(n - j):
        add_flow(flow, edge, value)
    return tuple(sorted(flow.items()))


def central_tree(n: int) -> dict[tuple[int, int], Fraction]:
    return dict(central_tree_items(n))


def flow_difference(
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    result = dict(left)
    add_scaled(result, right, Fraction(-1))
    return result


def flow_load(flow: dict[tuple[int, int], Fraction], q: int) -> Fraction:
    return sum(value * carry(n, j, q) for (n, j), value in flow.items())


def actual_layer_flow(c: list[Fraction], endpoint: int) -> dict[tuple[int, int], Fraction]:
    flow: dict[tuple[int, int], Fraction] = {}
    for m in range(2, endpoint + 1):
        add_scaled(flow, central_tree(m), c[m] - c[m + 1])
    return flow


def haar_capacity(c: list[Fraction], endpoint: int, n: int) -> Fraction:
    total = Fraction(0)
    scale = 1
    while scale * (n - 1) <= endpoint:
        total += sum(
            c[m] if m <= endpoint else Fraction(0)
            for m in range(scale * (n - 1) + 1, scale * n + 1)
        )
        total -= sum(
            c[m] if m <= endpoint else Fraction(0)
            for m in range(scale * n + 1, scale * (n + 1) + 1)
        )
        scale *= 2
    return total


def check_descendant_capacity(limit: int = 80) -> dict[str, object]:
    cases = 0
    recurrence_cases = 0
    for endpoint in range(3, limit + 1):
        families: list[list[Fraction]] = []
        for power in (1, 2, 3):
            c = [Fraction(0)] * (endpoint + 2)
            for m in range(2, endpoint + 1):
                c[m] = Fraction(1, m**power)
            families.append(c)

        affine = [Fraction(0)] * (endpoint + 2)
        for m in range(2, endpoint + 1):
            affine[m] = Fraction(endpoint - m + 1, endpoint * m)
        families.append(affine)

        for c in families:
            flow = actual_layer_flow(c, endpoint)
            capacities: dict[int, Fraction] = {}
            for n in range(2, endpoint + 1):
                actual = flow.get((n, n // 2), Fraction(0))
                formula = haar_capacity(c, endpoint, n)
                assert actual == formula, (endpoint, n, actual, formula)
                assert actual >= 0
                capacities[n] = actual
                cases += 1

            for n in range(2, endpoint + 1):
                root = c[n] - c[n + 1]
                expected = (
                    root
                    + 2 * capacities.get(2 * n, Fraction(0))
                    + capacities.get(2 * n - 1, Fraction(0))
                    + capacities.get(2 * n + 1, Fraction(0))
                )
                assert capacities[n] == expected
                recurrence_cases += 1

    return {
        "expanded_capacity_cases": cases,
        "factor_two_recurrence_cases": recurrence_cases,
        "limit_endpoint": limit,
    }


def check_scope_witnesses() -> dict[str, object]:
    endpoint = 4
    c = [Fraction(0)] * (endpoint + 2)
    for m in range(2, endpoint + 1):
        c[m] = Fraction(1, m)
    expanded = actual_layer_flow(c, endpoint)
    assert c[2] - c[3] == Fraction(1, 6)
    assert expanded[(2, 1)] == Fraction(3, 4)

    endpoint = 6
    c = [Fraction(0)] * (endpoint + 2)
    for m in range(2, endpoint + 1):
        c[m] = Fraction(1, m)
    expanded = actual_layer_flow(c, endpoint)
    assert expanded[(4, 2)] == Fraction(1, 20)
    assert Fraction(1, 2 * 2 + 1) == Fraction(1, 5)
    assert expanded[(4, 2)] < Fraction(1, 5)

    return {
        "root_only_value_N4_n2": "1/6",
        "expanded_value_N4_n2": "3/4",
        "insufficient_expanded_value_N6_n4": "1/20",
        "model_required_value_N6_n4": "1/5",
    }


def check_commutator_source(limit: int = 160) -> dict[str, object]:
    cases = 0
    for h in range(1, limit + 1):
        commutator = flow_difference(central_tree(h + 1), central_tree(h))
        for q in range(2, h + 3):
            expected = Fraction(1 if (h + 1) % q == 0 else 0)
            assert flow_load(commutator, q) == expected
            cases += 1
    return {"divisor_source_cases": cases, "limit_h": limit}


def ceil_sqrt(n: int) -> int:
    root = isqrt(n)
    return root if root * root == n else root + 1


def integer_capacity_majorant(flow: dict[tuple[int, int], Fraction]) -> Fraction:
    # omega_(n,j) <= 2 sqrt(n) <= 2 ceil_sqrt(n).
    return sum(
        abs(value) * 2 * ceil_sqrt(n)
        for (n, _j), value in flow.items()
    )


def check_commutator_capacity(limit: int = 1024) -> dict[str, object]:
    cases = 0
    maximum_ratio = Fraction(0)
    argmax = 0
    for h in range(1, limit + 1):
        commutator = flow_difference(central_tree(h + 1), central_tree(h))
        majorant = integer_capacity_majorant(commutator)
        bound = 24 * ceil_sqrt(h + 1)
        assert majorant <= bound, (h, majorant, bound)
        ratio = majorant / ceil_sqrt(h + 1)
        if ratio > maximum_ratio:
            maximum_ratio = ratio
            argmax = h
        cases += 1
    return {
        "cases": cases,
        "limit_h": limit,
        "largest_integer_majorant_ratio": str(maximum_ratio),
        "argmax": argmax,
        "proved_bound": "majorant <= 24 ceil_sqrt(h+1)",
    }


def check_paired_source(limit_k: int = 80) -> dict[str, object]:
    cases = 0
    order_cases = 0
    for k in range(1, limit_k + 1):
        for q0 in range(1, 13):
            for exponent in range(1, 5):
                A = Fraction(1, 2 * k) * Fraction(1, (2 * k * q0 - 1) ** exponent)
                B = Fraction(1, 2 * k + 1) * Fraction(
                    1, ((2 * k + 1) * q0) ** exponent
                )
                assert A >= B >= 0
                order_cases += 1

                commutator = flow_difference(
                    central_tree(2 * k), central_tree(2 * k - 1)
                )
                flow: dict[tuple[int, int], Fraction] = {}
                add_scaled(flow, commutator, A - B)
                add_flow(flow, (4 * k, 2 * k - 1), B)
                add_flow(flow, (4 * k, 2 * k), -B)

                for q in range(2, 4 * k + 2):
                    expected = A * (1 if (2 * k) % q == 0 else 0)
                    expected -= B * (1 if (2 * k + 1) % q == 0 else 0)
                    assert flow_load(flow, q) == expected
                    cases += 1

    return {
        "source_order_cases": order_cases,
        "paired_carry_replay_cases": cases,
        "limit_k": limit_k,
    }


def main() -> None:
    results = {
        "schema": "X-30401-descendant-capacity-commutator-v1",
        "classification": "EXACT_DESCENDANT_CAPACITY_AND_COMMUTATOR_ALGEBRA",
        "checks": {
            "descendant_capacity": check_descendant_capacity(),
            "scope_witnesses": check_scope_witnesses(),
            "commutator_source": check_commutator_source(),
            "commutator_capacity_majorant": check_commutator_capacity(),
            "paired_shifted_source": check_paired_source(),
        },
        "does_not_prove": [
            "the complete PR #286 source manifest",
            "the all-generation atomic-norm bound",
            "Cycle Debt",
            "RH",
        ],
    }
    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"
    result_path = Path(__file__).with_name("results") / "verification.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
