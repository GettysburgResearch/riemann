#!/usr/bin/env python3
"""Exact rational kernels for L-3901/L-3902 xi-passivity localizers."""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from typing import Iterable, Sequence


def require_nodes(nodes: Sequence[Fraction]) -> tuple[Fraction, ...]:
    values = tuple(Fraction(x) for x in nodes)
    if not values:
        raise ValueError("at least one node is required")
    if any(x <= 0 for x in values):
        raise ValueError("all nodes must be positive")
    if len(set(values)) != len(values):
        raise ValueError("nodes must be pairwise distinct")
    return values


def barycentric_weights(nodes: Sequence[Fraction]) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    out: list[Fraction] = []
    for i, x in enumerate(xs):
        denominator = Fraction(1)
        for j, y in enumerate(xs):
            if i != j:
                denominator *= x - y
        out.append(1 / denominator)
    return tuple(out)


def primitive_integer_scale(values: Sequence[Fraction]) -> tuple[int, ...]:
    if not values:
        raise ValueError("at least one value is required")
    denominator = 1
    for value in values:
        denominator = lcm(denominator, Fraction(value).denominator)
    integers = [
        Fraction(value).numerator * (denominator // Fraction(value).denominator)
        for value in values
    ]
    common = reduce(gcd, (abs(value) for value in integers if value), 0)
    if common == 0:
        raise ValueError("zero vector")
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    if first > 0:
        integers = [-value for value in integers]
    return tuple(integers)


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


def quadratic_from_real_f(
    nodes: Sequence[Fraction], vector: Sequence[Fraction], real_f: Sequence[Fraction]
) -> Fraction:
    coefficients = linear_coefficients(nodes, vector)
    values = tuple(Fraction(value) for value in real_f)
    if len(values) != len(coefficients):
        raise ValueError("F-value length mismatch")
    return sum(coefficients[i] * values[i] for i in range(len(values)))


def two_channel_values(
    x1: Fraction, x2: Fraction, r1: Fraction, r2: Fraction
) -> tuple[Fraction, Fraction]:
    """Return the L-3902 channels A and B from two real F values.

    A = (R(x1)/x1 - R(x2)/x2)/(x2^2-x1^2)
    B = (x2*R(x2) - x1*R(x1))/(x2^2-x1^2)
    """
    x1 = Fraction(x1)
    x2 = Fraction(x2)
    r1 = Fraction(r1)
    r2 = Fraction(r2)
    if not (0 < x1 < x2):
        raise ValueError("require 0 < x1 < x2")
    denominator = x2 * x2 - x1 * x1
    a_value = (r1 / x1 - r2 / x2) / denominator
    b_value = (x2 * r2 - x1 * r1) / denominator
    return a_value, b_value


def online_two_channel_values(
    x1: Fraction, x2: Fraction, offsets: Iterable[Fraction]
) -> tuple[Fraction, Fraction]:
    xs = (Fraction(x1), Fraction(x2))
    real_f = online_real_f(xs, offsets)
    return two_channel_values(xs[0], xs[1], real_f[0], real_f[1])


def symmetric_offline_pair_two_channels(
    x1: Fraction, x2: Fraction, delta: Fraction
) -> tuple[Fraction, Fraction]:
    x1 = Fraction(x1)
    x2 = Fraction(x2)
    delta = Fraction(delta)
    real_f = symmetric_offline_pair_real_f((x1, x2), delta)
    return two_channel_values(x1, x2, real_f[0], real_f[1])


def online_real_f(
    nodes: Sequence[Fraction], offsets: Iterable[Fraction]
) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    ds = tuple(Fraction(value) for value in offsets)
    return tuple(sum(x / (x * x + d * d) for d in ds) for x in xs)


def online_product_value(
    nodes: Sequence[Fraction], offsets: Iterable[Fraction]
) -> Fraction:
    xs = require_nodes(nodes)
    ds = tuple(Fraction(value) for value in offsets)
    return sum(1 / _product(x * x + d * d for x in xs) for d in ds)


def symmetric_offline_pair_real_f(
    nodes: Sequence[Fraction], delta: Fraction
) -> tuple[Fraction, ...]:
    xs = require_nodes(nodes)
    delta = Fraction(delta)
    if delta <= 0:
        raise ValueError("delta must be positive")
    if any(x == delta for x in xs):
        raise ZeroDivisionError("node lies on the synthetic pole")
    return tuple(2 * x / (x * x - delta * delta) for x in xs)


def symmetric_offline_pair_product_value(
    nodes: Sequence[Fraction], delta: Fraction
) -> Fraction:
    xs = require_nodes(nodes)
    delta = Fraction(delta)
    if delta <= 0:
        raise ValueError("delta must be positive")
    return 2 / _product(x * x - delta * delta for x in xs)


def amplification_l1(
    nodes: Sequence[Fraction], vector: Sequence[Fraction]
) -> Fraction:
    return sum(abs(value) for value in linear_coefficients(nodes, vector))


def _product(values: Iterable[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result
