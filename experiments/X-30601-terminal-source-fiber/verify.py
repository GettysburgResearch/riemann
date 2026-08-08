#!/usr/bin/env python3
"""Exact regression for the terminal-source fiber audit.

Standard-library only.  The checker proves finite carry algebra:

- the PR #304 quotient-only lift loses the arithmetic fiber;
- the correctly dilated adjacent-tree flow realizes the complete divisor source;
- central rows form an exact step basis on every dyadic top half.

It does not prove the all-generation band recurrence, Cycle Debt, or RH.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import hashlib
import json
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
def central_tree_items(
    n: int,
) -> tuple[tuple[tuple[int, int], Fraction], ...]:
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


def commutator(h: int) -> dict[tuple[int, int], Fraction]:
    flow = central_tree(h + 1)
    add_scaled(flow, central_tree(h), Fraction(-1))
    return flow


def flow_load(flow: dict[tuple[int, int], Fraction], q: int) -> Fraction:
    return sum(
        value * carry(n, j, q)
        for (n, j), value in flow.items()
    )


def check_minimal_fiber_witness() -> dict[str, str]:
    q0 = 5
    k = 1
    exponent = 1
    A = Fraction(1, 2 * k * (2 * k * q0 - 1) ** exponent)
    B = Fraction(
        1,
        (2 * k + 1) * ((2 * k + 1) * q0) ** exponent,
    )
    assert A == Fraction(1, 18)
    assert B == Fraction(1, 45)

    quotient_flow: dict[tuple[int, int], Fraction] = {}
    add_scaled(quotient_flow, commutator(2 * k - 1), A)
    add_scaled(quotient_flow, commutator(2 * k), -B)

    dilated_flow: dict[tuple[int, int], Fraction] = {}
    add_scaled(dilated_flow, commutator(2 * k * q0 - 1), A)
    add_scaled(
        dilated_flow,
        commutator((2 * k + 1) * q0 - 1),
        -B,
    )

    assert flow_load(quotient_flow, q0) == 0
    assert flow_load(dilated_flow, q0) == Fraction(1, 30)

    return {
        "A": "1/18",
        "B": "1/45",
        "quotient_load_q5": "0",
        "dilated_load_q5": "1/30",
    }


def check_dilated_sources() -> tuple[int, int]:
    carry_rows = 0
    mismatching_families = 0

    for q0 in range(2, 13):
        for k in range(1, 13):
            for exponent in range(1, 4):
                A = Fraction(
                    1,
                    2 * k * (2 * k * q0 - 1) ** exponent,
                )
                B = Fraction(
                    1,
                    (2 * k + 1)
                    * ((2 * k + 1) * q0) ** exponent,
                )

                dilated: dict[tuple[int, int], Fraction] = {}
                add_scaled(
                    dilated,
                    commutator(2 * k * q0 - 1),
                    A,
                )
                add_scaled(
                    dilated,
                    commutator((2 * k + 1) * q0 - 1),
                    -B,
                )

                quotient: dict[tuple[int, int], Fraction] = {}
                add_scaled(quotient, commutator(2 * k - 1), A)
                add_scaled(quotient, commutator(2 * k), -B)

                family_mismatch = False
                for q in range(2, (2 * k + 1) * q0 + 1):
                    expected = A * int((2 * k * q0) % q == 0)
                    expected -= B * int(((2 * k + 1) * q0) % q == 0)
                    assert flow_load(dilated, q) == expected
                    if flow_load(quotient, q) != expected:
                        family_mismatch = True
                    carry_rows += 1

                if family_mismatch:
                    mismatching_families += 1

    return carry_rows, mismatching_families


def check_top_half_steps() -> tuple[int, int]:
    rows = 0
    profiles = 0

    for H in range(2, 81):
        profile_list: list[dict[int, Fraction]] = []
        profile_list.append(
            {
                n: Fraction(((7 * n + 3 * H) % 17) - 8, 19)
                for n in range(H + 1, 2 * H + 1)
            }
        )
        profile_list.append(
            {
                n: -Fraction(1, n)
                for n in range(H + 1, 2 * H + 1)
            }
        )
        profile_list.append(
            {
                n: Fraction((-1) ** n * (n - H), 11 * (H + 1))
                for n in range(H + 1, 2 * H + 1)
            }
        )

        for profile in profile_list:
            flow: dict[tuple[int, int], Fraction] = {}
            for n in range(H + 1, 2 * H + 1):
                coefficient = profile[n] - profile.get(n + 1, Fraction(0))
                add_flow(flow, (n, n // 2), coefficient)

            for q in range(H + 1, 2 * H + 1):
                assert flow_load(flow, q) == profile[q]
                rows += 1
            profiles += 1

    return rows, profiles


def main() -> None:
    witness = check_minimal_fiber_witness()
    dilated_rows, mismatching_families = check_dilated_sources()
    top_rows, top_profiles = check_top_half_steps()

    result = {
        "schema": "X-30601-terminal-source-fiber-audit-v1",
        "classification": (
            "EXACT_SOURCE_FIBER_REFUTATION_AND_TOP_BAND_STEP_FLOW"
        ),
        "witness": witness,
        "dilated_source_carry_rows": dilated_rows,
        "fiber_families_with_quotient_mismatch": mismatching_families,
        "top_half_profiles": top_profiles,
        "top_half_carry_rows": top_rows,
        "does_not_prove": [
            "the all-generation band-variation recurrence",
            "Cycle Debt",
            "RH",
        ],
    }

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()

    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    result_path = Path(__file__).with_name("results") / "verification.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
