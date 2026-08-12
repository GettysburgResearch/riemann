#!/usr/bin/env python3
from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


def one_trial(rng: random.Random) -> int:
    branch_count = rng.randint(1, 6)

    # Exact subprobability target masses.
    remaining = Fraction(1)
    weights: list[Fraction] = []
    for _ in range(branch_count):
        weight = remaining * Fraction(rng.randint(0, 10), 10)
        weights.append(weight)
        remaining -= weight
    assert sum(weights, Fraction(0)) <= 1

    # Normalized packet ledgers. Packing score may exceed declared score, so
    # child loss may be negative exactly as in the native signed score loss.
    declared_normalized = [
        Fraction(rng.randint(0, 30), 5) for _ in range(branch_count)
    ]
    packing_normalized = [
        Fraction(rng.randint(0, 40), 5) for _ in range(branch_count)
    ]

    declared = [
        weight * score
        for weight, score in zip(weights, declared_normalized)
    ]
    packing = [
        weight * score
        for weight, score in zip(weights, packing_normalized)
    ]

    current_score = Fraction(rng.randint(0, 30), 5)
    debt = Fraction(rng.randint(0, 10), 5)
    ledger_surplus = Fraction(rng.randint(0, 10), 5)
    lift_bonus = Fraction(rng.randint(0, 20), 5)

    # Score-superordinate source ledger and score-noncontracting parent lift.
    parent_declared = (
        current_score
        + sum(declared, Fraction(0))
        + debt
        - ledger_surplus
    )
    parent_packing = (
        current_score
        + sum(packing, Fraction(0))
        + lift_bonus
    )

    parent_loss = parent_declared - parent_packing
    weighted_child_bound = debt + sum(
        declared_score - packing_score
        for declared_score, packing_score in zip(declared, packing)
    )
    assert parent_loss <= weighted_child_bound

    normalized_bound = debt + sum(
        weight * (declared_score - packing_score)
        for weight, declared_score, packing_score in zip(
            weights, declared_normalized, packing_normalized
        )
    )
    assert weighted_child_bound == normalized_bound

    return 2 + branch_count


def main() -> None:
    rng = random.Random(91551)
    checks = 0
    for _ in range(5000):
        checks += one_trial(rng)

    result = {
        "classification": "PASS_NATIVE_PACKET_LOSS_GLUING",
        "checks": checks,
        "trials": 5000,
        "scope": (
            "Exact Fraction stress tests of subprobability target weights, "
            "actual-packet homogeneity, favorable negative child losses, and "
            "the score-superordinate native-loss gluing inequality. Arithmetic "
            "Hall production, physical capacity feasibility, the outer/collar "
            "machinery, and RH are not certified."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
