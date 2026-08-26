#!/usr/bin/env python3
"""Tiny exact replay for the Sym12 S5 Eisenstein-defect audit.

This verifies only finite algebra transcribed in the companion note.  It does
not prove the cited cohomology theorems, query a modular-form database, or
enumerate a finite-field family.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from collections.abc import Iterable

Partition = tuple[int, ...]


def partitions(total: int, ceiling: int | None = None) -> Iterable[Partition]:
    if total == 0:
        yield ()
        return
    top = total if ceiling is None else min(total, ceiling)
    for first in range(top, 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def remove_corners(partition: Partition) -> set[Partition]:
    out: set[Partition] = set()
    for index, row in enumerate(partition):
        next_row = partition[index + 1] if index + 1 < len(partition) else 0
        if row <= next_row:
            continue
        reduced = list(partition)
        reduced[index] -= 1
        out.add(tuple(value for value in reduced if value))
    return out


def s5_fixed_dimension(partition: Partition) -> int:
    return int((5,) in remove_corners(partition))


def specht_dimension(partition: Partition) -> int:
    hooks = 1
    for row, length in enumerate(partition):
        for column in range(length):
            below = sum(other > column for other in partition[row + 1 :])
            hooks *= length - column + below
    return math.factorial(sum(partition)) // hooks


def euler_polynomial(terms: Iterable[tuple[int, int, int]]) -> dict[int, int]:
    """Return Tate-exponent coefficients from (degree, exponent, multiplicity)."""
    result: defaultdict[int, int] = defaultdict(int)
    for degree, exponent, multiplicity in terms:
        result[exponent] += (-1) ** degree * multiplicity
    return {
        exponent: coefficient for exponent, coefficient in result.items() if coefficient
    }


def symmetric_fifth_of_sym9_weights() -> dict[int, int]:
    weights = tuple(range(-9, 10, 2))
    states: dict[tuple[int, int], int] = {(0, 0): 1}
    for weight in weights:
        updated: defaultdict[tuple[int, int], int] = defaultdict(int)
        for (used, total_weight), multiplicity in states.items():
            for copies in range(6 - used):
                updated[(used + copies, total_weight + copies * weight)] += multiplicity
        states = dict(updated)
    return {
        total_weight: multiplicity
        for (used, total_weight), multiplicity in states.items()
        if used == 5
    }


def main() -> int:
    invariant_carriers = {
        partition: s5_fixed_dimension(partition) for partition in partitions(6)
    }
    invariant_carriers = {
        partition: value for partition, value in invariant_carriers.items() if value
    }
    assert invariant_carriers == {(6,): 1, (5, 1): 1}

    # Shmakov 4.6.6--4.6.8 after the exact invariant projection.
    siegel = euler_polynomial(((2, 0, 2), (3, 1, 2)))
    klingen = euler_polynomial(())
    borel = euler_polynomial(((3, 1, 2),))
    total_eisenstein = {
        exponent: siegel.get(exponent, 0) + borel.get(exponent, 0)
        for exponent in (0, 1)
    }
    assert siegel == {0: 2, 1: -2}
    assert klingen == {}
    assert borel == {1: -2}
    assert total_eisenstein == {0: 2, 1: -4}
    bfg_formal = {0: 2, 1: -5}
    epsilon_eis = {
        exponent: total_eisenstein.get(exponent, 0) - bfg_formal.get(exponent, 0)
        for exponent in (0, 1)
    }
    epsilon_eis = {key: value for key, value in epsilon_eis.items() if value}
    assert epsilon_eis == {1: 1}

    # The official rows are frozen only to audit lift/nonlift classification.
    rows = (
        ((3, 1, 1, 1), 0, 1),
        ((2, 2, 2), 1, 0),
        ((2, 2, 1, 1), 0, 1),
        ((2, 1, 1, 1, 1), 1, 0),
        ((1, 1, 1, 1, 1, 1), 1, 0),
    )
    lift_dimension = sum(
        specht_dimension(partition) * lift for partition, lift, _ in rows
    )
    nonlift_dimension = sum(
        specht_dimension(partition) * nonlift for partition, _, nonlift in rows
    )
    assert (lift_dimension, nonlift_dimension) == (11, 19)
    assert all(s5_fixed_dimension(partition) == 0 for partition, _, _ in rows)

    sym5_sym9 = symmetric_fifth_of_sym9_weights()
    sym9_weights = tuple(range(-9, 10, 2))

    def tensor_weight(weight: int) -> int:
        return sum(sym5_sym9.get(weight - other, 0) for other in sym9_weights)

    weight_12 = tensor_weight(12)
    weight_14 = tensor_weight(14)
    covariant_multiplicity = weight_12 - weight_14
    assert (weight_12, weight_14, covariant_multiplicity) == (752, 686, 66)

    payload = {
        "schema": "riemann.genus2.sym12.s5_eisenstein_defect_audit.v1",
        "scope": "finite exact character and weight algebra only",
        "s6_to_s5_invariant_carriers": ["[6]", "[5,1]"],
        "formal_eisenstein_projection": {
            "siegel": "2-2*L",
            "klingen": "0",
            "borel": "-2*L",
            "total": "2-4*L",
            "epsilon_against_BFG_formal_2_minus_5L": "L",
        },
        "conditional_master_defect": "Hhat_12=L-L*f_minus-G",
        "official_row_audit": {
            "lift_dimension": lift_dimension,
            "nonlift_dimension": nonlift_dimension,
            "all_returned_rows_have_zero_S5_invariants": True,
        },
        "marked_covariant_source": {
            "weight_12_multiplicity": weight_12,
            "weight_14_multiplicity": weight_14,
            "Sym12_highest_weight_multiplicity": covariant_multiplicity,
        },
        "firewall": (
            "The 66-dimensional source precedes holomorphy valuations, and the "
            "formal 2-4*L projection does not establish its Galois realization; "
            "this replay proves neither the modular-form-space nor stable-channel "
            "vanishing."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
