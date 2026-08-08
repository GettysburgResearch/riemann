#!/usr/bin/env python3
"""Exact gates and declared Decimal reconnaissance for L-30503--L-30506.

The exact layer checks rational inequalities and finite carry/tree algebra.
The Decimal layer samples the analytic coefficient formula; it is not used as
proof of any all-scale statement.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

getcontext().prec = 80


def central_edge(n: int) -> tuple[int, int]:
    return (n, n // 2)


def add_counter(target: Counter, source: Counter, scale: int = 1) -> None:
    for key, value in source.items():
        target[key] += scale * value
        if target[key] == 0:
            del target[key]


def central_tree(n: int, memo: dict[int, Counter]) -> Counter:
    if n <= 1:
        return Counter()
    if n in memo:
        return memo[n].copy()
    j = n // 2
    result = Counter({(n, j): 1})
    add_counter(result, central_tree(j, memo))
    add_counter(result, central_tree(n - j, memo))
    memo[n] = result.copy()
    return result


def adjacent_tree(r: int, memo: dict[int, Counter]) -> Counter:
    result = central_tree(r + 1, memo)
    add_counter(result, central_tree(r, memo), -1)
    return result


def carry(edge: tuple[int, int], q: int) -> int:
    n, j = edge
    return n // q - j // q - (n - j) // q


def flow_load(flow: Counter, q: int) -> int:
    return sum(value * carry(edge, q) for edge, value in flow.items())


def exact_gates() -> dict[str, object]:
    assert Fraction(9, 8) < Fraction(17, 16) ** 2
    log2_lower = 2 * (Fraction(1, 3) + Fraction(1, 81))
    assert log2_lower == Fraction(56, 81)
    assert log2_lower > Fraction(11, 16)
    assert 3 * Fraction(11, 16) == Fraction(33, 16)
    assert Fraction(1, 6) / Fraction(3, 2) == Fraction(1, 9)
    return {
        "sqrt_9_over_8_upper": "17/16",
        "log2_lower": str(log2_lower),
        "row_sign_threshold": 8,
        "large_row_threshold": 64,
    }


def tree_and_commutator_checks(limit: int = 96) -> dict[str, int]:
    memo: dict[int, Counter] = {}
    adjacent_rows = 0
    dyadic_rows = 0
    carry_rows = 0
    for r in range(1, limit + 1):
        e = adjacent_tree(r, memo)
        for q in range(2, r + 2):
            expected = int((r + 1) % q == 0)
            assert flow_load(e, q) == expected
            carry_rows += 1
        adjacent_rows += 1

    for m in range(1, limit // 2 + 1):
        lhs = Counter({central_edge(2 * m + 1): 1, central_edge(2 * m): -1})
        rhs = adjacent_tree(2 * m, memo)
        add_counter(rhs, adjacent_tree(m, memo), -1)
        assert lhs == rhs
        dyadic_rows += 1

    return {
        "adjacent_tree_rows": adjacent_rows,
        "dyadic_commutator_rows": dyadic_rows,
        "carry_load_rows": carry_rows,
    }


def decimal_recon(limit: int = 10000) -> dict[str, object]:
    negative_from_eight = True
    first_negative = None
    weighted_debt = Decimal(0)
    for n in range(2, limit + 1):
        nd = Decimal(n)
        beta = (
            (Decimal(1) + Decimal(1) / nd).ln()
            / Decimal(n + 1).sqrt()
            - nd.ln()
            * (Decimal(1) / nd.sqrt() - Decimal(1) / Decimal(n + 1).sqrt())
        )
        if beta < 0 and first_negative is None:
            first_negative = n
        if n >= 8 and not beta < 0:
            negative_from_eight = False
        if beta < 0:
            # Discovery-only upper surrogate 2 sqrt(n) for omega_n.
            weighted_debt += 2 * nd.sqrt() * (-beta)
    return {
        "limit": limit,
        "first_negative": first_negative,
        "negative_from_eight": negative_from_eight,
        "upper_surrogate_debt": str(weighted_debt),
        "debt_over_log_squared": str(weighted_debt / (Decimal(limit).ln() ** 2)),
    }


def main() -> None:
    result = {
        "schema": "X-30502-coupled-boundary-flow-v1",
        "classification": "EXACT_RATIONAL_AND_INTEGER_PLUS_DECIMAL_RECONNAISSANCE",
        "exact_gates": exact_gates(),
        "tree_algebra": tree_and_commutator_checks(),
        "decimal_reconnaissance": decimal_recon(),
        "does_not_prove": [
            "all-scale paired-tail debt bound",
            "Cycle Debt",
            "Riemann Hypothesis",
        ],
    }
    canonical = json.dumps(result, indent=2, sort_keys=True) + "\n"
    result["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
