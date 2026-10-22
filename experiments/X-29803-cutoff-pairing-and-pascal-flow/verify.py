#!/usr/bin/env python3
"""Exact finite manifest for cutoff pairing and Pascal source flow.

Verifies with integer/Fraction arithmetic:
- first omitted odd index is equal to or one before the shifted-even index;
- the unmatched collar has at most one odd term per (N,q);
- every common pure-power finite-difference tail has even value >= odd value;
- the central/sibling carry image is exact;
- paired edge coefficients are nonnegative and have zero negative debt.

This is a finite regression, not the all-endpoint theorem or RH.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def first_even(N: int, q: int) -> int:
    k = 1
    while 2 * k * q - 1 <= N:
        k += 1
    return k


def first_odd(N: int, q: int) -> int:
    k = 1
    while (2 * k + 1) * q <= N:
        k += 1
    return k


def diff_at(start: int, step: int, exponent: int, order: int) -> Fraction:
    vals = [Fraction(1, (start + r * step) ** exponent) for r in range(order + 1)]
    for _ in range(order):
        vals = [vals[r] - vals[r + 1] for r in range(len(vals) - 1)]
    return vals[0]


def run() -> dict:
    index_rows = 0
    unmatched_odd_rows = 0
    paired_jet_rows = 0

    for N in range(2, 257):
        for q in range(1, (N + 1) // 2 + 1):
            ke = first_even(N, q)
            ko = first_odd(N, q)
            assert ke - ko in (0, 1)
            if ke == ko + 1:
                unmatched_odd_rows += 1
                assert (2 * ko + 1) * q > N
                assert 2 * ko * q - 1 <= N
            index_rows += 1

            step = 2 * q
            for k in range(ke, ke + 4):
                even_arg = 2 * k * q - 1
                odd_arg = (2 * k + 1) * q
                assert even_arg < odd_arg
                for exponent in range(1, 4):
                    for order in range(0, 4):
                        ve = diff_at(even_arg, step, exponent, order)
                        vo = diff_at(odd_arg, step, exponent, order)
                        assert ve >= vo > 0
                        M = Fraction(1, 2 * k) * ve
                        T = Fraction(1, 2 * k + 1) * vo
                        assert 0 <= T <= M
                        assert M - T >= 0
                        paired_jet_rows += 1

    carry_rows = 0
    for k in range(1, 129):
        parent = 4 * k
        central = 2 * k
        sibling = 2 * k - 1
        for q in range(1, parent + 1):
            lhs = carry(parent, sibling, q) - carry(parent, central, q)
            rhs = int((2 * k) % q == 0) - int((2 * k + 1) % q == 0)
            assert lhs == rhs
            carry_rows += 1

    # Mutation: pairing the unmatched odd term with the previous even index is illegal.
    mutation_rejected = False
    N, q = 4, 2
    ke, ko = first_even(N, q), first_odd(N, q)
    assert ke == ko + 1
    illegal_even_arg = 2 * ko * q - 1
    unmatched_odd_arg = (2 * ko + 1) * q
    if illegal_even_arg <= N < unmatched_odd_arg:
        mutation_rejected = True
    assert mutation_rejected

    result = {
        "schema": "X-29803-cutoff-pairing-pascal-flow-v1",
        "classification": "EXACT_CUTOFF_PAIRING_AND_NONNEGATIVE_PASCAL_FLOW_VERIFIED",
        "first_omitted_index_rows": index_rows,
        "unmatched_single_odd_rows": unmatched_odd_rows,
        "paired_pure_power_jet_rows": paired_jet_rows,
        "central_sibling_carry_rows": carry_rows,
        "mutations_rejected": 1,
        "proof_boundary": (
            "finite integer/rational source manifest only; shifted Taylor superposition, "
            "all common destinations, collar capacity, DCD, and RH are not certified"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["result_sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
