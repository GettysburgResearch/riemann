#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from typing import Dict, Tuple


def beta(n: int, q: int) -> Fraction:
    if not 2 <= q <= n:
        return Fraction(0)
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def greedy(
    X: int, target: Dict[int, Fraction]
) -> Tuple[Dict[int, Fraction], Dict[int, Fraction], Dict[int, int], Dict[int, Fraction]]:
    residual = dict(target)
    coefficients: Dict[int, Fraction] = {}
    blockers: Dict[int, int] = {}
    diagonal_losses: Dict[int, Fraction] = {}

    for n in range(X, 1, -1):
        candidates = []
        for q in range(2, n + 1):
            entry = beta(n, q)
            if entry:
                candidates.append((residual[q] / entry, q))
        value, blocker = min(candidates, key=lambda item: (item[0], item[1]))
        diagonal = residual[n] / beta(n, n)
        coefficients[n] = value
        blockers[n] = blocker
        diagonal_losses[n] = diagonal - value
        if value < 0 or diagonal_losses[n] < 0:
            raise AssertionError("invalid greedy ratio")
        for q in range(2, n + 1):
            residual[q] -= value * beta(n, q)
            if residual[q] < 0:
                raise AssertionError("negative residual")

    return coefficients, residual, blockers, diagonal_losses


def divisor_summatory(n: int) -> int:
    return sum(n // q for q in range(1, n + 1))


def carry_row_sum(n: int) -> Fraction:
    return sum((beta(n, q) for q in range(2, n + 1)), Fraction(0))


def carry_row_sum_via_divisors(n: int) -> Fraction:
    return Fraction(
        (n + 1) * divisor_summatory(n)
        - 2 * sum(divisor_summatory(j) for j in range(1, n + 1)),
        n + 1,
    )


def build_result() -> Dict[str, object]:
    X = 9
    target = {
        2: Fraction(91, 100),
        3: Fraction(41, 50),
        4: Fraction(33, 50),
        5: Fraction(33, 50),
        6: Fraction(63, 100),
        7: Fraction(11, 20),
        8: Fraction(53, 100),
        9: Fraction(0),
    }
    d, residual, blockers, losses = greedy(X, target)

    expected_d = {
        2: Fraction(651, 500),
        3: Fraction(133, 125),
        4: Fraction(0),
        5: Fraction(111, 250),
        6: Fraction(101, 250),
        7: Fraction(8, 35),
        8: Fraction(477, 700),
        9: Fraction(0),
    }
    if d != expected_d:
        raise AssertionError("coefficient mutation")
    if blockers[5] != 4:
        raise AssertionError("off-diagonal blocker missing")
    if residual[5] != Fraction(29, 500):
        raise AssertionError("slack mutation")
    if any(residual[q] for q in residual if q != 5):
        raise AssertionError("unexpected residual")
    if losses[5] != Fraction(87, 1000):
        raise AssertionError("diagonal-loss mutation")
    if beta(5, 5) * losses[5] != residual[5]:
        raise AssertionError("slack/loss identity failure")

    row_checks = 0
    for n in range(2, 65):
        if carry_row_sum(n) != carry_row_sum_via_divisors(n):
            raise AssertionError(f"row-sum mismatch at n={n}")
        row_checks += 1

    total_slack = sum(residual.values(), Fraction(0))
    mass = sum(Fraction(n) * d[n] for n in d)
    target_sum = sum(target.values(), Fraction(0))
    row_error = sum(
        d[n] * (Fraction(n) - 2 * carry_row_sum(n)) for n in d
    )
    if mass != 2 * target_sum - 2 * total_slack + row_error:
        raise AssertionError("exact mass/slack identity failure")

    return {
        "schema": "X-23702-v1",
        "endpoint": X,
        "off_diagonal_blocker": {"row": 5, "column": 4},
        "positive_final_slack": str(total_slack),
        "diagonal_loss_row_5": str(losses[5]),
        "row_sum_checks": row_checks,
        "exact_mass": str(mass),
        "exact_row_error": str(row_error),
        "verdict": "EXACT_GREEDY_SLACK_SCOPE_CONTROL_VERIFIED",
        "scope": (
            "finite rational carry/slack algebra only; demonstrates that generic "
            "digit identities do not force saturation and does not refute DBT "
            "for the logarithmic target"
        ),
    }


def main() -> None:
    print(json.dumps(build_result(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
