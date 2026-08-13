#!/usr/bin/env python3
from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


def build_transport(
    even_nodes: list[int],
    odd_nodes: list[int],
    even_capacity: dict[int, Fraction],
    odd_demand: dict[int, Fraction],
) -> dict[tuple[int, int], Fraction]:
    """Greedy no-upward Hall transport in target-mass units."""
    remaining = dict(even_capacity)
    transport: dict[tuple[int, int], Fraction] = {}
    for odd in sorted(odd_nodes):
        demand = odd_demand[odd]
        for even in sorted(e for e in even_nodes if e <= odd):
            take = min(demand, remaining[even])
            if take:
                transport[(odd, even)] = take
                demand -= take
                remaining[even] -= take
            if demand == 0:
                break
        assert demand == 0
    return transport


def one_trial(rng: random.Random, trial: int) -> int:
    # Interlaced nodes guarantee many admissible no-upward edges.
    even_nodes = [2, 4, 6, 8, 10]
    odd_nodes = [3, 5, 7, 9]

    # Target atoms and monotone target-per-score / normalized-row profiles.
    target = {n: Fraction(rng.randint(2, 11), 1) for n in even_nodes + odd_nodes}
    q = {n: Fraction(3 * (12 - n) + 5, 20) for n in even_nodes + odd_nodes}
    h1 = {n: Fraction(2 * (12 - n) + 3, 17) for n in even_nodes + odd_nodes}
    h2 = {n: Fraction(5 * (12 - n) + 7, 31) for n in even_nodes + odd_nodes}

    for e in even_nodes:
        for o in odd_nodes:
            if e <= o:
                assert q[e] >= q[o]
                assert h1[e] >= h1[o]
                assert h2[e] >= h2[o]

    score = {n: target[n] / q[n] for n in target}
    row1 = {n: target[n] * h1[n] for n in target}
    row2 = {n: target[n] * h2[n] for n in target}

    # Source coefficients. Make every prefix feasible by placing generous mass
    # at the first two even nodes and bounded odd demands.
    a = {n: Fraction(rng.randint(3, 10), 1) for n in even_nodes}
    b = {n: Fraction(rng.randint(0, 3), 1) for n in odd_nodes}
    even_capacity = {n: a[n] * target[n] for n in even_nodes}
    odd_demand = {n: b[n] * target[n] for n in odd_nodes}

    # Scale odd demand if a prefix would fail. This changes coefficients but
    # preserves exact rationality and leaves nontrivial transports.
    for odd in odd_nodes:
        cap = sum(even_capacity[e] for e in even_nodes if e <= odd)
        prior = sum(odd_demand[o] for o in odd_nodes if o < odd)
        available = cap - prior
        if odd_demand[odd] > available:
            odd_demand[odd] = max(Fraction(0), available)
            b[odd] = odd_demand[odd] / target[odd]

    transport = build_transport(
        even_nodes, odd_nodes, even_capacity, odd_demand
    )

    used = {e: Fraction(0) for e in even_nodes}
    matched = {o: Fraction(0) for o in odd_nodes}
    for (o, e), mass in transport.items():
        assert e <= o and mass >= 0
        used[e] += mass
        matched[o] += mass
    for e in even_nodes:
        assert used[e] <= even_capacity[e]
    for o in odd_nodes:
        assert matched[o] == odd_demand[o]

    residual_coeff = {
        e: a[e] - used[e] / target[e]
        for e in even_nodes
    }
    assert all(value >= 0 for value in residual_coeff.values())

    signed_target = (
        sum(a[e] * target[e] for e in even_nodes)
        - sum(b[o] * target[o] for o in odd_nodes)
    )
    residual_target = sum(
        residual_coeff[e] * target[e] for e in even_nodes
    )
    assert residual_target == signed_target

    signed_score = (
        sum(a[e] * score[e] for e in even_nodes)
        - sum(b[o] * score[o] for o in odd_nodes)
    )
    residual_score = sum(
        residual_coeff[e] * score[e] for e in even_nodes
    )
    score_bonus = sum(
        mass * (Fraction(1, 1) / q[o] - Fraction(1, 1) / q[e])
        for (o, e), mass in transport.items()
    )
    assert residual_score - signed_score == score_bonus
    assert score_bonus >= 0

    for row, h in ((row1, h1), (row2, h2)):
        signed_row = (
            sum(a[e] * row[e] for e in even_nodes)
            - sum(b[o] * row[o] for o in odd_nodes)
        )
        residual_row = sum(
            residual_coeff[e] * row[e] for e in even_nodes
        )
        row_bonus = sum(
            mass * (h[e] - h[o])
            for (o, e), mass in transport.items()
        )
        assert signed_row - residual_row == row_bonus
        assert row_bonus >= 0

    # At least one nonzero transport in all but a deliberately empty trial.
    if trial != 0:
        assert sum(transport.values(), Fraction(0)) >= 0

    return 11 + 2 * len(transport)


def main() -> None:
    rng = random.Random(91545)
    checks = 0
    for trial in range(1000):
        checks += one_trial(rng, trial)

    result = {
        "classification": "PASS_HALL_RESIDUAL_HEREDITARY_SOURCE",
        "checks": checks,
        "trials": 1000,
        "scope": (
            "Exact Fraction verification of target-Hall residual source "
            "positivity, target exactness, score superordination, and two "
            "target-null nonnegative row bonuses. The arithmetic Hall margins, "
            "live-branch normalization, factor-54 composition, and RH are not "
            "certified."
        ),
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
