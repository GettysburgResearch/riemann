#!/usr/bin/env python3
"""Exact rational kernels for the matched-pole Pick annihilator L-3904."""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from typing import Iterable, Sequence


def require_nodes(nodes: Sequence[Fraction]) -> tuple[Fraction, ...]:
    values = tuple(Fraction(x) for x in nodes)
    if len(values) < 2:
        raise ValueError("at least two nodes are required")
    if any(x <= 0 for x in values):
        raise ValueError("all nodes must be positive")
    if len(set(values)) != len(values):
        raise ValueError("nodes must be pairwise distinct")
    return values


def barycentric_weights(nodes: Sequence[Fraction]) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    return tuple(
        1 / _product(xs[i] - xs[j] for j in range(len(xs)) if i != j)
        for i in range(len(xs))
    )


def matched_pole_vector(
    nodes: Sequence[Fraction], squared_displacement: Fraction
) -> tuple[Fraction, ...]:
    """Return the exact L-3904 vector for the model value d=delta^2."""
    xs = require_nodes(nodes)
    d = Fraction(squared_displacement)
    if d <= 0:
        raise ValueError("squared_displacement must be positive")
    if any(x * x == d for x in xs):
        raise ZeroDivisionError("a node lies on the model pole")
    weights = barycentric_weights(xs)
    a = tuple(x / (x * x - d) for x in xs)
    s0 = sum(w * value for w, value in zip(weights, a))
    s1 = sum(w * x * value for w, x, value in zip(weights, xs, a))
    vector = tuple(w * (s1 - s0 * x) for w, x in zip(weights, xs))
    if not any(vector):
        raise ArithmeticError("matched vector unexpectedly vanished")
    return vector


def primitive_integer_scale(values: Sequence[Fraction]) -> tuple[int, ...]:
    fractions = tuple(Fraction(value) for value in values)
    if not fractions or not any(fractions):
        raise ValueError("a nonzero vector is required")
    denominator = 1
    for value in fractions:
        denominator = lcm(denominator, value.denominator)
    integers = [
        value.numerator * (denominator // value.denominator) for value in fractions
    ]
    common = reduce(gcd, (abs(value) for value in integers if value), 0)
    integers = [value // common for value in integers]
    if next(value for value in integers if value) > 0:
        integers = [-value for value in integers]
    return tuple(integers)


def matched_identities(
    nodes: Sequence[Fraction], squared_displacement: Fraction
) -> dict[str, object]:
    """Reconstruct the exact annihilation, overlap, and moment identities."""
    xs = require_nodes(nodes)
    d = Fraction(squared_displacement)
    vector = matched_pole_vector(xs, d)
    a = tuple(x / (x * x - d) for x in xs)
    b = tuple(1 / (x * x - d) for x in xs)
    product = _product(x * x - d for x in xs)
    return {
        "vector": vector,
        "a_overlap": sum(c * value for c, value in zip(vector, a)),
        "b_overlap": sum(c * value for c, value in zip(vector, b)),
        "expected_b_overlap": -1 / product,
        "moments": tuple(
            sum(c * x**k for c, x in zip(vector, xs))
            for k in range(max(0, len(xs) - 2))
        ),
    }


def same_ordinate_pair_quadratic(
    nodes: Sequence[Fraction],
    vector: Sequence[Fraction],
    squared_displacement: Fraction,
    multiplicity: int = 1,
) -> Fraction:
    """Exact Pick quadratic of the same-ordinate off-line symmetric pair."""
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs) or not any(c):
        raise ValueError("vector length mismatch or zero vector")
    d = Fraction(squared_displacement)
    if d <= 0 or multiplicity < 1:
        raise ValueError("positive d and multiplicity are required")
    if any(x * x == d for x in xs):
        raise ZeroDivisionError("a node lies on the model pole")
    a_overlap = sum(ci * x / (x * x - d) for ci, x in zip(c, xs))
    b_overlap = sum(ci / (x * x - d) for ci, x in zip(c, xs))
    return 2 * multiplicity * (a_overlap * a_overlap - d * b_overlap * b_overlap)


def critical_line_pick_quadratic(
    nodes: Sequence[Fraction],
    vector: Sequence[Fraction],
    ordinate_offsets: Iterable[Fraction],
) -> Fraction:
    """Exact contribution of critical-line zeros at the supplied T-gamma offsets."""
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs) or not any(c):
        raise ValueError("vector length mismatch or zero vector")
    total = Fraction(0)
    for raw_y in ordinate_offsets:
        y = Fraction(raw_y)
        real = sum(ci * x / (x * x + y * y) for ci, x in zip(c, xs))
        imag = -sum(ci * y / (x * x + y * y) for ci, x in zip(c, xs))
        total += real * real + imag * imag
    return total


def pick_linear_coefficients(
    nodes: Sequence[Fraction], vector: Sequence[Fraction]
) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs) or not any(c):
        raise ValueError("vector length mismatch or zero vector")
    return tuple(
        2 * c[i] * sum(c[j] / (xs[i] + xs[j]) for j in range(len(xs)))
        for i in range(len(xs))
    )


def pick_quadratic_from_real_values(
    nodes: Sequence[Fraction],
    vector: Sequence[Fraction],
    real_f: Sequence[Fraction],
) -> Fraction:
    coefficients = pick_linear_coefficients(nodes, vector)
    values = tuple(Fraction(value) for value in real_f)
    if len(values) != len(coefficients):
        raise ValueError("F-value length mismatch")
    return sum(coefficient * value for coefficient, value in zip(coefficients, values))


def _product(values: Iterable[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result
