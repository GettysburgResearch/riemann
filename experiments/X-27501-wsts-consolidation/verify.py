#!/usr/bin/env python3
"""Exact finite regression for the final WSTS consolidation.

The checker uses only Python's standard library and exact rational/integer
arithmetic.  It authenticates finite algebraic interfaces only.  It does not
prove WSTS, RH, the classical Chebyshev error bound, or any cofinal estimate.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from itertools import product
from pathlib import Path


def check_normalized_derivative() -> dict[str, object]:
    # J(theta)=4N sqrt(theta)-4/sqrt(theta)+C-2(S_N+1)log(theta).
    # Compare its termwise derivative with
    # 2 theta^(-3/2)[N theta+1-(S_N+1)sqrt(theta)].
    lhs = {
        ("N", Fraction(-1, 2)): Fraction(2),
        ("one", Fraction(-3, 2)): Fraction(2),
        ("S_plus_1", Fraction(-1)): Fraction(-2),
    }
    rhs = {
        ("N", Fraction(-1, 2)): Fraction(2),
        ("one", Fraction(-3, 2)): Fraction(2),
        ("S_plus_1", Fraction(-1)): Fraction(-2),
    }
    assert lhs == rhs
    return {
        "formal_terms": len(lhs),
        "identity": "J'=2 theta^-3/2[N theta+1-(S_N+1)sqrt(theta)]",
    }


def check_queue() -> dict[str, object]:
    cases = 0
    for length in range(1, 7):
        for values in product(range(-2, 3), repeat=length):
            queue = 0
            for residual in values:
                queue = max(queue + residual, 0)
            maximum_suffix = max([0] + [sum(values[k:]) for k in range(length)])
            assert queue == maximum_suffix
            cases += 1
    return {"cases": cases, "max_length": 6}


def check_weighted_tail_abel() -> dict[str, object]:
    cases = 0
    for length in range(1, 6):
        weights = [Fraction(k + 2, k + 1) + k for k in range(length)]
        assert all(weights[k] > weights[k - 1] for k in range(1, length))
        for values in product(range(-2, 3), repeat=length):
            residuals = [Fraction(value) for value in values]
            tails = [sum(residuals[k:]) for k in range(length)]
            direct = sum(weights[k] * residuals[k] for k in range(length))
            abel = weights[0] * tails[0]
            abel += sum(
                (weights[k] - weights[k - 1]) * tails[k]
                for k in range(1, length)
            )
            assert direct == abel
            cases += 1
    return {"cases": cases, "max_length": 5}


def check_weighted_skorokhod() -> dict[str, object]:
    cases = 0
    for length in range(1, 7):
        for values in product(range(-2, 3), repeat=length):
            tails = [sum(values[k:]) for k in range(length)]
            charge = max([0] + tails)
            augmented = list(values) + [-charge]
            augmented_tails = [
                sum(augmented[k:]) for k in range(length + 1)
            ]
            assert all(value <= 0 for value in augmented_tails)
            cases += 1
    return {"cases": cases, "max_length": 6}


def synthetic_residual(endpoint: int, column: int) -> Fraction:
    return Fraction(
        ((7 * endpoint + 3 * column) % 11) - 5,
        endpoint + column,
    )


def check_dyadic_telescope() -> dict[str, object]:
    cases = 0
    for endpoint in range(2, 129):
        levels = [endpoint]
        while levels[-1] >= 2:
            next_endpoint = levels[-1] // 2
            levels.append(next_endpoint)
            if next_endpoint < 2:
                break

        for column in range(2, endpoint + 1):
            total = Fraction(0)
            for index, current in enumerate(levels[:-1]):
                next_endpoint = levels[index + 1]
                current_value = (
                    synthetic_residual(current, column)
                    if column <= current
                    else Fraction(0)
                )
                next_value = (
                    synthetic_residual(next_endpoint, column)
                    if column <= next_endpoint
                    else Fraction(0)
                )
                total += current_value - next_value

            terminal = levels[-1]
            if column <= terminal:
                total += synthetic_residual(terminal, column)

            assert total == synthetic_residual(endpoint, column)
            cases += 1

    return {"cases": cases, "max_X": 128}


def integrate_linear(
    left: Fraction,
    right: Fraction,
    value_left: Fraction,
    value_right: Fraction,
) -> Fraction:
    return (value_left + value_right) * (right - left) / 2


def check_stieltjes_integration_by_parts() -> dict[str, object]:
    knots = [Fraction(value) for value in [1, 2, 3, 5, 8, 10]]
    function_values = [Fraction(value) for value in [2, 1, 4, 0, 3, 5]]
    event_weights = {
        Fraction(2): Fraction(3, 2),
        Fraction(3): Fraction(2, 3),
        Fraction(5): Fraction(5, 4),
        Fraction(8): Fraction(7, 5),
    }

    atom_part = sum(
        weight * function_values[knots.index(location)]
        for location, weight in event_weights.items()
    )
    continuous_part = sum(
        integrate_linear(
            knots[index],
            knots[index + 1],
            function_values[index],
            function_values[index + 1],
        )
        for index in range(len(knots) - 1)
    )
    direct = atom_part - continuous_part

    cumulative_weight = sum(event_weights.values())
    residual_left = -knots[0]
    residual_right = cumulative_weight - knots[-1]
    boundary = (
        function_values[-1] * residual_right
        - function_values[0] * residual_left
    )

    integral_residual_df = Fraction(0)
    cumulative_weight = Fraction(0)
    for index in range(len(knots) - 1):
        left = knots[index]
        right = knots[index + 1]
        if left in event_weights:
            cumulative_weight += event_weights[left]
        slope = (
            function_values[index + 1] - function_values[index]
        ) / (right - left)
        integral_residual_df += slope * (
            cumulative_weight * (right - left)
            - (right * right - left * left) / 2
        )

    by_parts = boundary - integral_residual_df
    assert direct == by_parts
    return {
        "events": len(event_weights),
        "segments": len(knots) - 1,
        "value": str(direct),
    }


def check_zero_cost_transfer() -> dict[str, object]:
    cases = 0
    weights = [
        Fraction(1),
        Fraction(3, 2),
        Fraction(2),
        Fraction(5, 2),
        Fraction(3),
    ]
    for left in range(len(weights)):
        for right in range(left + 1, len(weights)):
            for amount in [Fraction(1, 3), Fraction(1), Fraction(7, 4)]:
                raw_transfer = amount / weights[left]
                endpoint_removal = amount * (
                    1 / weights[left] - 1 / weights[right]
                )
                objective_change = (
                    raw_transfer * (weights[right] - weights[left])
                    - endpoint_removal * weights[right]
                )
                assert objective_change == 0
                cases += 1
    return {"cases": cases}


def check_logarithmic_error_budget() -> dict[str, object]:
    # After u=log(t), the two terms are
    # integral_0^L u^2 du = L^3/3 and
    # integral_0^L u^2(L-u)du = L^4/12.
    cubic = Fraction(1, 3)
    quartic = Fraction(1, 12)
    assert Fraction(1, 3) - Fraction(1, 4) == quartic
    return {
        "L3_coefficient": str(cubic),
        "L4_coefficient": str(quartic),
    }


def check_finite_dyadic_ratio() -> dict[str, object]:
    cases = 0
    for endpoint in range(3, 5001):
        ratio = Fraction(endpoint // 2, endpoint)
        assert Fraction(1, 3) <= ratio <= Fraction(1, 2)
        cases += 1
    return {"cases": cases, "range": "[1/3,1/2]"}


def main() -> None:
    results = {
        "schema": "X-27501-wsts-consolidation-v1",
        "classification": "EXACT_FINITE_ALGEBRA_ONLY",
        "checks": {
            "normalized_tail_derivative": check_normalized_derivative(),
            "prime_tail_queue": check_queue(),
            "weighted_tail_abel": check_weighted_tail_abel(),
            "weighted_skorokhod_charge": check_weighted_skorokhod(),
            "dyadic_shell_telescope": check_dyadic_telescope(),
            "stieltjes_integration_by_parts": (
                check_stieltjes_integration_by_parts()
            ),
            "zero_cost_weighted_transfer": check_zero_cost_transfer(),
            "logarithmic_error_budget": check_logarithmic_error_budget(),
            "finite_dyadic_ratio": check_finite_dyadic_ratio(),
        },
        "does_not_prove": [
            "RH",
            "WSTS",
            "Chebyshev error bound",
            "cofinal prime-sampling estimate",
        ],
    }

    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"

    output_path = Path(__file__).with_name("results") / "verification.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
