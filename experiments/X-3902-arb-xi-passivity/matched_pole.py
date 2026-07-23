#!/usr/bin/env python3
"""Exact rational kernels for L-3904 matched-pole Pick annihilators."""
from __future__ import annotations

from fractions import Fraction
from math import prod
from typing import Sequence


def require_nodes(nodes: Sequence[Fraction]) -> tuple[Fraction, ...]:
    values = tuple(Fraction(value) for value in nodes)
    if len(values) < 2:
        raise ValueError("at least two nodes are required")
    if any(value <= 0 for value in values):
        raise ValueError("nodes must be positive")
    if len(set(values)) != len(values):
        raise ValueError("nodes must be pairwise distinct")
    return values


def barycentric_weights(nodes: Sequence[Fraction]) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    return tuple(
        1 / prod(xs[i] - xs[j] for j in range(len(xs)) if j != i)
        for i in range(len(xs))
    )


def matched_pole_vector(
    nodes: Sequence[Fraction], model_d: Fraction
) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    d = Fraction(model_d)
    if d <= 0:
        raise ValueError("model_d must be positive")
    if any(x * x == d for x in xs):
        raise ZeroDivisionError("a node lies on the modeled pole")
    weights = barycentric_weights(xs)
    alpha = tuple(x / (x * x - d) for x in xs)
    s0 = sum(w * a for w, a in zip(weights, alpha))
    s1 = sum(w * x * a for w, x, a in zip(weights, xs, alpha))
    scale = prod(x * x - d for x in xs)
    vector = tuple(scale * w * (s1 - s0 * x) for w, x in zip(weights, xs))
    if not any(vector):
        raise ArithmeticError("matched vector unexpectedly vanished")
    return vector


def moment(
    nodes: Sequence[Fraction], vector: Sequence[Fraction], power: int
) -> Fraction:
    if power < 0:
        raise ValueError("power must be nonnegative")
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs):
        raise ValueError("vector length mismatch")
    return sum(c_i * x**power for c_i, x in zip(c, xs))


def model_overlaps(
    nodes: Sequence[Fraction], vector: Sequence[Fraction], model_d: Fraction
) -> tuple[Fraction, Fraction]:
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs):
        raise ValueError("vector length mismatch")
    d = Fraction(model_d)
    if d <= 0:
        raise ValueError("model_d must be positive")
    if any(x * x == d for x in xs):
        raise ZeroDivisionError("a node lies on the modeled pole")
    alpha = sum(c_i * x / (x * x - d) for c_i, x in zip(c, xs))
    beta = sum(c_i / (x * x - d) for c_i, x in zip(c, xs))
    return alpha, beta


def linear_coefficients(
    nodes: Sequence[Fraction], vector: Sequence[Fraction]
) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs):
        raise ValueError("vector length mismatch")
    if not any(c):
        raise ValueError("zero vector")
    return tuple(
        2 * c[i] * sum(c[j] / (xs[i] + xs[j]) for j in range(len(xs)))
        for i in range(len(xs))
    )


def pair_polynomial_data(
    nodes: Sequence[Fraction], vector: Sequence[Fraction], actual_d: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs):
        raise ValueError("vector length mismatch")
    d = Fraction(actual_d)
    if d <= 0:
        raise ValueError("actual_d must be positive")
    factors = tuple(x * x - d for x in xs)
    denominator = prod(factors)
    if denominator == 0:
        raise ZeroDivisionError("a node lies on the actual pole")
    u_value = sum(
        c[i]
        * xs[i]
        * prod(factors[j] for j in range(len(xs)) if j != i)
        for i in range(len(xs))
    )
    v_value = sum(
        c[i] * prod(factors[j] for j in range(len(xs)) if j != i)
        for i in range(len(xs))
    )
    return u_value, v_value, denominator


def isolated_pair_quadratic(
    nodes: Sequence[Fraction],
    vector: Sequence[Fraction],
    actual_d: Fraction,
    *,
    multiplicity: int = 1,
) -> Fraction:
    if (
        isinstance(multiplicity, bool)
        or not isinstance(multiplicity, int)
        or multiplicity < 1
    ):
        raise ValueError("multiplicity must be a positive integer")
    d = Fraction(actual_d)
    u_value, v_value, denominator = pair_polynomial_data(nodes, vector, d)
    return (
        2
        * multiplicity
        * (u_value * u_value - d * v_value * v_value)
        / (denominator * denominator)
    )


def vector_norm_squared(vector: Sequence[Fraction]) -> Fraction:
    values = tuple(Fraction(value) for value in vector)
    if not any(values):
        raise ValueError("zero vector")
    return sum(value * value for value in values)


def amplification_l1(
    nodes: Sequence[Fraction], vector: Sequence[Fraction]
) -> Fraction:
    return sum(abs(value) for value in linear_coefficients(nodes, vector))
