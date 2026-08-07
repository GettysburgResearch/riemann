#!/usr/bin/env python3
"""Exact rational regression for L-26701/L-26702.

This checker validates only finite affine-boundary-lift algebra on a synthetic
rational carry system. It does not prove the cofinal boundary-charge estimate
or RH.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
from typing import Dict, List, Tuple


def primes_upto(limit: int) -> List[int]:
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            for value in range(prime * prime, limit + 1, prime):
                sieve[value] = False
    return [value for value in range(2, limit + 1) if sieve[value]]


def prime_powers(limit: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    for prime in primes_upto(limit):
        value = prime
        while value <= limit:
            result.append((value, prime))
            value *= prime
    result.sort()
    return result


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def carry_response(vector: Dict[int, Fraction], q: int, endpoint: int) -> Fraction:
    total = Fraction(0)
    for multiple in range(q, endpoint + 1, q):
        total += vector.get(multiple, Fraction(0))
        total -= vector.get(multiple + 1, Fraction(0))
    return total


def formal_physical_objective(
    vector: Dict[int, Fraction], endpoint: int
) -> Dict[int, Fraction]:
    coefficients = {prime: Fraction(0) for prime in primes_upto(endpoint)}
    for index in range(2, endpoint + 1):
        coefficient = vector.get(index, Fraction(0))
        for prime in coefficients:
            coefficients[prime] += coefficient * (
                valuation(index, prime) - valuation(index - 1, prime)
            )
    return {prime: value for prime, value in coefficients.items() if value}


def formal_dual_objective(
    vector: Dict[int, Fraction], endpoint: int
) -> Dict[int, Fraction]:
    coefficients = {prime: Fraction(0) for prime in primes_upto(endpoint)}
    for power, prime in prime_powers(endpoint):
        coefficients[prime] += carry_response(vector, power, endpoint)
    return {prime: value for prime, value in coefficients.items() if value}


def solve_fraction_system(
    matrix: List[List[Fraction]], rhs: List[Fraction]
) -> List[Fraction]:
    dimension = len(matrix)
    augmented = [
        [Fraction(entry) for entry in matrix[row]] + [Fraction(rhs[row])]
        for row in range(dimension)
    ]
    for column in range(dimension):
        pivot = next(
            row
            for row in range(column, dimension)
            if augmented[row][column] != 0
        )
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(dimension):
            if row == column:
                continue
            multiplier = augmented[row][column]
            if multiplier == 0:
                continue
            augmented[row] = [
                augmented[row][position]
                - multiplier * augmented[column][position]
                for position in range(dimension + 1)
            ]
    return [augmented[row][-1] for row in range(dimension)]


def endpoint_projected_column(q: int, endpoint: int) -> List[Fraction]:
    values = [Fraction(0)]
    endpoint_indicator = int(endpoint % q == 0)
    for index in range(1, endpoint + 1):
        values.append(
            Fraction(int(index % q == 0))
            - Fraction(index * endpoint_indicator, endpoint)
        )
    return values


def run_control() -> dict:
    endpoint = 12
    oversupport_prime = 13
    powers = [power for power, _ in prime_powers(endpoint)]

    columns = {
        power: endpoint_projected_column(power, endpoint)
        for power in powers
    }
    gradients = {
        power: [
            columns[power][index + 1] - columns[power][index]
            for index in range(endpoint)
        ]
        for power in powers
    }
    gram = [
        [
            sum(
                gradients[left][index] * gradients[right][index]
                for index in range(endpoint)
            )
            for right in powers
        ]
        for left in powers
    ]

    seed = {
        index: Fraction(
            (endpoint - index + 1) * (index + 1), index * endpoint
        )
        for index in range(2, endpoint + 1)
    }

    residual = [
        Fraction(((-1) ** position) * (position + 1), 50 * (len(powers) + 1))
        for position in range(len(powers))
    ]
    coefficients = solve_fraction_system(gram, residual)
    potential = [
        sum(
            coefficients[position] * columns[power][index]
            for position, power in enumerate(powers)
        )
        for index in range(endpoint + 1)
    ]
    green = {
        index: seed[index] + potential[index - 1] - potential[index]
        for index in range(2, endpoint + 1)
    }
    target = {
        power: carry_response(seed, power, endpoint) - residual[position]
        for position, power in enumerate(powers)
    }

    assert all(
        carry_response(green, power, endpoint) == target[power]
        for power in powers
    )

    positive_slopes = [
        potential[index] - potential[index - 1]
        for index in range(2, endpoint + 1)
    ]
    boundary_charge = max([Fraction(0), *positive_slopes])
    lifted = {
        index: green.get(index, Fraction(0)) + boundary_charge
        for index in range(2, oversupport_prime + 1)
    }

    assert all(
        lifted[index] >= seed.get(index, Fraction(0))
        for index in range(2, oversupport_prime + 1)
    )
    assert all(
        carry_response(lifted, power, oversupport_prime) == target[power]
        for power in powers
    )
    assert carry_response(
        lifted, oversupport_prime, oversupport_prime
    ) == boundary_charge
    for power, _ in prime_powers(oversupport_prime):
        if endpoint < power < oversupport_prime:
            assert carry_response(lifted, power, oversupport_prime) == 0

    assert (
        formal_physical_objective(lifted, oversupport_prime)
        == formal_dual_objective(lifted, oversupport_prime)
    )

    green_dual = formal_dual_objective(green, endpoint)
    expected_lifted_dual = dict(green_dual)
    expected_lifted_dual[oversupport_prime] = (
        expected_lifted_dual.get(oversupport_prime, Fraction(0))
        + boundary_charge
    )
    assert formal_dual_objective(
        lifted, oversupport_prime
    ) == expected_lifted_dual

    green_energy = sum(
        (potential[index + 1] - potential[index]) ** 2
        for index in range(endpoint)
    )
    assert boundary_charge**2 <= green_energy

    constant_block_ratio_exponent = sum(
        Fraction(
            valuation(index, oversupport_prime)
            - valuation(index - 1, oversupport_prime)
        )
        for index in range(2, oversupport_prime + 1)
    )
    assert constant_block_ratio_exponent == 1

    mutation_count = 0

    composite_boundary = 14
    composite_lift = {
        index: green.get(index, Fraction(0)) + boundary_charge
        for index in range(2, composite_boundary + 1)
    }
    assert carry_response(composite_lift, 2, composite_boundary) != target[2]
    mutation_count += 1

    too_small = boundary_charge / 2
    bad_lift = {
        index: green.get(index, Fraction(0)) + too_small
        for index in range(2, oversupport_prime + 1)
    }
    assert any(
        bad_lift[index] < seed.get(index, Fraction(0))
        for index in range(2, endpoint + 1)
    )
    mutation_count += 1

    wrong_green = {
        index: seed[index] - potential[index - 1] + potential[index]
        for index in range(2, endpoint + 1)
    }
    assert any(
        carry_response(wrong_green, power, endpoint) != target[power]
        for power in powers
    )
    mutation_count += 1

    assert formal_dual_objective(lifted, oversupport_prime) != green_dual
    mutation_count += 1

    wrong_charge = max(Fraction(0), *[-value for value in positive_slopes])
    assert wrong_charge != boundary_charge
    mutation_count += 1

    classification = "PASS_EXACT_AFFINE_GREEN_BOUNDARY_LIFT_ALGEBRA"
    proof_payload = {
        "schema": "riemann.x26701-affine-green-boundary-lift.v1",
        "classification": classification,
        "endpoint": endpoint,
        "oversupport_prime": oversupport_prime,
        "prime_power_rows": len(powers),
        "boundary_charge": str(boundary_charge),
        "green_energy": str(green_energy),
        "minimum_lifted_coordinate": str(min(lifted.values())),
        "exact_response_checks": len(powers) + 1,
        "formal_objective_prime_coordinates": len(
            formal_physical_objective(lifted, oversupport_prime)
        ),
        "mutations_rejected": mutation_count,
        "proof_boundary": (
            "Finite rational Green/lift algebra only; no cofinal boundary-"
            "charge estimate and no RH claim."
        ),
    }
    digest_material = json.dumps(
        proof_payload, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    proof_payload["proof_object_sha256"] = sha256(digest_material).hexdigest()
    return proof_payload


def main() -> None:
    result = run_control()
    expected_path = Path(__file__).with_name("results") / "verification.json"
    if expected_path.exists():
        retained = json.loads(expected_path.read_text(encoding="utf-8"))
        if retained != result:
            raise AssertionError("retained verification object does not match")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
