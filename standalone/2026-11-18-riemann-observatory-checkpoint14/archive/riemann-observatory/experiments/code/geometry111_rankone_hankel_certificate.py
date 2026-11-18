#!/usr/bin/env python3
"""Reproduce exact small Hankel witnesses for the rank-one formal series."""

import hashlib
import json
from fractions import Fraction
from itertools import combinations
from math import prod
from pathlib import Path


def moments(variance, tilt):
    """Moments through degree six for exp(variance*z*z/2)*(1-tilt*z)."""
    return [
        Fraction(prod(range(1, degree, 2))) * variance ** (degree // 2)
        if degree % 2 == 0 else
        -tilt * prod(range(1, degree + 1, 2)) * variance ** (degree // 2)
        for degree in range(7)
    ]


def determinant(matrix):
    """Gaussian elimination with exact pivoting."""
    work = [row.copy() for row in matrix]
    value = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value *= pivot_value
        for row in range(column + 1, len(work)):
            ratio = work[row][column] / pivot_value
            for j in range(column + 1, len(work)):
                work[row][j] -= ratio * work[column][j]
    return value


def order_certificate(sequence, order):
    hankel = [[sequence[i + j] for j in range(order + 1)] for i in range(order + 1)]
    principal_minors = []
    for size in range(1, order + 2):
        for subset in combinations(range(order + 1), size):
            minor = [[hankel[i][j] for j in subset] for i in subset]
            principal_minors.append(determinant(minor))
    return {
        "order": order,
        "hankel_determinant": str(principal_minors[-1]),
        "principal_minors_by_size_then_lexicographic_indices": list(map(str, principal_minors)),
        "positive_semidefinite": all(value >= 0 for value in principal_minors),
    }


def quadratic_value(sequence, coefficients):
    return sum(
        left * right * sequence[i + j]
        for i, left in enumerate(coefficients)
        for j, right in enumerate(coefficients)
    )


def certificate(variance, tilt, coordinate, witness, expected, equality=False):
    sequence = moments(variance, tilt)
    orders = [order_certificate(sequence, order) for order in range(4)]
    assert [order["positive_semidefinite"] for order in orders] == [True, True, True, False]
    value = quadratic_value(sequence, witness)
    assert value == expected < 0
    result = {
        "coordinate": coordinate,
        "exact_variance": str(variance),
        "exact_tilt": str(tilt),
        "moments_degree_zero_through_six": list(map(str, sequence)),
        "order_certificates": orders,
        "least_negative_witness_degree": 3,
        "witness_coefficients_ascending": witness,
        "functional_of_witness_square": str(value),
    }
    if equality:
        null_polynomial = [0, 3, 1]
        assert quadratic_value(sequence, null_polynomial) == 0
        assert orders[2]["hankel_determinant"] == "0"
        result["order_two_null_coefficients_ascending"] = null_polynomial
    return result


def main():
    output = {
        "code": "experiments/code/geometry111_rankone_hankel_certificate.py",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "Python standard library fractions.Fraction",
        "standardized_t_one_half": certificate(
            Fraction(1), Fraction(1, 2), "x", [-3, 6, 9, 2], -30,
        ),
        "standardized_t_one_over_sqrt_three": certificate(
            Fraction(3), Fraction(1), "y = sqrt(3) * x", [0, 12, 4, 1], -27, equality=True,
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
