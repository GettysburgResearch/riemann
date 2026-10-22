#!/usr/bin/env python3
"""Exact finite regression for the source-flow eta-Pascal repair.

Only Python's standard library is used.  This checker authenticates finite
algebra and finite Hausdorff tests.  It does not prove SFC, the cofinal
capacity estimate, Cycle Debt, or RH.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def add_flow(target: dict[tuple[int, int], Fraction],
             edge: tuple[int, int], amount: Fraction) -> None:
    target[edge] = target.get(edge, Fraction(0)) + amount
    if target[edge] == 0:
        del target[edge]


def central_tree(n: int, memo: dict[int, dict[tuple[int, int], Fraction]]) -> dict[tuple[int, int], Fraction]:
    if n <= 1:
        return {}
    if n in memo:
        return dict(memo[n])
    j = n // 2
    flow: dict[tuple[int, int], Fraction] = {(n, j): Fraction(1)}
    left = central_tree(j, memo)
    right = central_tree(n - j, memo)
    for edge, value in left.items():
        add_flow(flow, edge, value)
    for edge, value in right.items():
        add_flow(flow, edge, value)
    memo[n] = dict(flow)
    return flow


def flow_difference(a: dict[tuple[int, int], Fraction],
                    b: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    result = dict(a)
    for edge, value in b.items():
        add_flow(result, edge, -value)
    return result


def flow_load(flow: dict[tuple[int, int], Fraction], q: int) -> Fraction:
    return sum(value * carry(n, j, q) for (n, j), value in flow.items())


def check_switch_identity(limit: int = 120) -> dict[str, object]:
    cases = 0
    for k in range(1, limit + 1):
        for q in range(2, 4 * k + 2):
            lhs = carry(4 * k, 2 * k - 1, q) - carry(4 * k, 2 * k, q)
            rhs = (1 if 2 * k % q == 0 else 0) - (
                1 if (2 * k + 1) % q == 0 else 0
            )
            assert lhs == rhs, (k, q, lhs, rhs)
            cases += 1
    return {"cases": cases, "limit_k": limit}


def check_standalone_mismatch(limit: int = 120) -> dict[str, object]:
    cases = 0
    for k in range(1, limit + 1):
        A = Fraction(1, 2 * k)
        B = Fraction(1, 2 * k + 1)
        q = 4 * k
        source = A * (1 if 2 * k % q == 0 else 0) - B * (
            1 if (2 * k + 1) % q == 0 else 0
        )
        constructed = (
            (A - B) * carry(4 * k, 2 * k, q)
            + B * carry(4 * k, 2 * k - 1, q)
        )
        assert source == 0
        assert constructed == A
        assert source != constructed
        cases += 1

    A = Fraction(1, 2)
    B = Fraction(1, 3)
    source = []
    constructed = []
    for q in [2, 3, 4]:
        source.append(
            A * (1 if 2 % q == 0 else 0)
            - B * (1 if 3 % q == 0 else 0)
        )
        constructed.append(
            (A - B) * carry(4, 2, q) + B * carry(4, 1, q)
        )
    assert source == [Fraction(1, 2), Fraction(-1, 3), Fraction(0)]
    assert constructed == [Fraction(1, 3), Fraction(1, 6), Fraction(1, 2)]
    return {
        "general_cases": cases,
        "small_source": [str(x) for x in source],
        "small_constructed": [str(x) for x in constructed],
    }


def check_relative_replacement(limit: int = 120) -> dict[str, object]:
    cases = 0
    for k in range(1, limit + 1):
        A = Fraction(3 * k + 2, 5 * k + 7)
        B = A / 3
        for q in range(2, 4 * k + 2):
            new = (
                (A - B) * carry(4 * k, 2 * k, q)
                + B * carry(4 * k, 2 * k - 1, q)
            )
            old = A * carry(4 * k, 2 * k, q)
            expected = B * (
                (1 if 2 * k % q == 0 else 0)
                - (1 if (2 * k + 1) % q == 0 else 0)
            )
            assert new - old == expected, (k, q, new - old, expected)
            cases += 1
    return {"cases": cases, "limit_k": limit}


def check_commutator_source(limit: int = 80) -> dict[str, object]:
    memo: dict[int, dict[tuple[int, int], Fraction]] = {}
    cases = 0
    pair_cases = 0
    for h in range(1, limit + 1):
        Eh = flow_difference(central_tree(h + 1, memo), central_tree(h, memo))
        for q in range(2, h + 3):
            expected = Fraction(1 if (h + 1) % q == 0 else 0)
            assert flow_load(Eh, q) == expected, (h, q, flow_load(Eh, q), expected)
            cases += 1

    for k in range(1, limit // 2 + 1):
        Eeven = flow_difference(central_tree(2 * k, memo), central_tree(2 * k - 1, memo))
        Eodd = flow_difference(central_tree(2 * k + 1, memo), central_tree(2 * k, memo))
        A = Fraction(1, 2 * k)
        B = Fraction(1, 2 * k + 1)
        pair = {}
        for edge, value in Eeven.items():
            add_flow(pair, edge, A * value)
        for edge, value in Eodd.items():
            add_flow(pair, edge, -B * value)
        for q in range(2, 2 * k + 2):
            expected = A * (1 if 2 * k % q == 0 else 0) - B * (
                1 if (2 * k + 1) % q == 0 else 0
            )
            assert flow_load(pair, q) == expected
            pair_cases += 1

        diff = flow_difference(Eeven, Eodd)
        switch = {(4 * k, 2 * k - 1): Fraction(1), (4 * k, 2 * k): Fraction(-1)}
        for q in range(2, 4 * k + 2):
            assert flow_load(diff, q) == flow_load(switch, q)
            pair_cases += 1

    return {
        "divisor_atom_cases": cases,
        "paired_and_cycle_cases": pair_cases,
        "limit_h": limit,
    }


def shifted_residual(q: int, s: int, k: int) -> Fraction:
    A = Fraction(1, 2 * k) * Fraction(1, (2 * k * q - 1) ** s)
    B = Fraction(1, 2 * k + 1) * Fraction(1, ((2 * k + 1) * q) ** s)
    return A - B


def check_hausdorff_residual(
    q_limit: int = 12, s_limit: int = 6, k_limit: int = 36, order_limit: int = 18
) -> dict[str, object]:
    cases = 0
    minimum = None
    argmin = None
    for q in range(1, q_limit + 1):
        for s in range(1, s_limit + 1):
            row = [shifted_residual(q, s, k) for k in range(1, k_limit + 1)]
            for order in range(0, order_limit + 1):
                for index, value in enumerate(row, start=1):
                    assert value >= 0, (q, s, order, index, value)
                    if minimum is None or value < minimum:
                        minimum = value
                        argmin = [q, s, order, index]
                    cases += 1
                if len(row) <= 1:
                    break
                row = [row[i] - row[i + 1] for i in range(len(row) - 1)]
    return {
        "cases": cases,
        "q_limit": q_limit,
        "s_limit": s_limit,
        "k_limit": k_limit,
        "order_limit": order_limit,
        "minimum": str(minimum),
        "argmin": argmin,
    }


def cutoff_starts(N: int, q: int) -> tuple[int, int]:
    even_start = (N + 1) // (2 * q) + 1
    k = 1
    while (2 * k + 1) * q <= N:
        k += 1
    return even_start, k


def check_cutoff_parity(limit_N: int = 300) -> dict[str, object]:
    aligned = 0
    odd_earlier = 0
    cases = 0
    for N in range(2, limit_N + 1):
        for q in range(1, N + 1):
            ke, ko = cutoff_starts(N, q)
            assert ko in {ke, ke - 1}, (N, q, ke, ko)
            if ko == ke:
                aligned += 1
            else:
                odd_earlier += 1
                assert ke == ko + 1
            cases += 1
    assert odd_earlier > 0
    return {
        "cases": cases,
        "aligned": aligned,
        "odd_starts_one_earlier": odd_earlier,
        "limit_N": limit_N,
    }


def main() -> None:
    results = {
        "schema": "X-30201-source-flow-manifest-v1",
        "classification": "EXACT_FINITE_ALGRA_AND_HAUSDORFF_RECONNAISSANCE",
        "checks": {
            "sibling_switch_identity": check_switch_identity(),
            "standalone_source_mismatch": check_standalone_mismatch(),
            "relative_replacement": check_relative_replacement(),
            "adjacent_tree_commutator": check_commutator_source(),
            "shifted_residual_hausdorff": check_hausdorff_residual(),
            "cutoff_start_parity": check_cutoff_parity(),
        },
        "does_not_prove": [
            "SFC",
            "all-generation source-to-flow binding",
            "DCD contraction",
            "Cycle Debt",
            "RH",
        ],
    }
    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
