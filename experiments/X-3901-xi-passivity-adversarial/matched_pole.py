#!/usr/bin/env python3
"""Exact rational kernels for L-3904 matched-pole Pick annihilators.

This module contains finite algebra only. It does not evaluate zeta or xi and
never treats a modeled zero pair as a Riemann-xi candidate.
"""
from __future__ import annotations

from fractions import Fraction
from math import prod
from typing import Iterable, Sequence

from barycentric import barycentric_weights, linear_coefficients, require_nodes


def matched_pole_vector(
    nodes: Sequence[Fraction], model_d: Fraction
) -> tuple[Fraction, ...]:
    """Return the canonically scaled L-3904 rational vector.

    The scaling is chosen so that, at the modeled pair, the alpha overlap is
    zero and the beta overlap is exactly -1.
    """
    xs = require_nodes(nodes)
    if len(xs) < 2:
        raise ValueError("at least two nodes are required")
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
    """Return sum_i c_i x_i**power exactly."""
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
    """Return the alpha and beta overlaps for a squared displacement."""
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


def symmetric_pair_quadratic(
    nodes: Sequence[Fraction],
    vector: Sequence[Fraction],
    actual_d: Fraction,
    *,
    multiplicity: int = 1,
) -> Fraction:
    """Return one same-ordinate reflected-pair Pick contribution exactly."""
    if (
        isinstance(multiplicity, bool)
        or not isinstance(multiplicity, int)
        or multiplicity < 1
    ):
        raise ValueError("multiplicity must be a positive integer")
    d = Fraction(actual_d)
    alpha, beta = model_overlaps(nodes, vector, d)
    return 2 * multiplicity * (alpha * alpha - d * beta * beta)


def pair_polynomial_data(
    nodes: Sequence[Fraction], vector: Sequence[Fraction], actual_d: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    """Return U(d), V(d), D(d) from L-3904 equation (9)."""
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


def pair_quadratic_from_polynomials(
    nodes: Sequence[Fraction],
    vector: Sequence[Fraction],
    actual_d: Fraction,
    *,
    multiplicity: int = 1,
) -> Fraction:
    """Reconstruct equation (10) without rational-function summation."""
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


def contracted_real_f_coefficients(
    nodes: Sequence[Fraction], vector: Sequence[Fraction]
) -> tuple[Fraction, ...]:
    """Return exact coefficients q_i in sum q_i Re F(s_i)."""
    return linear_coefficients(nodes, vector)


def online_zero_quadratic(
    nodes: Sequence[Fraction], vector: Sequence[Fraction], ordinate_offset: Fraction
) -> Fraction:
    """Return |sum_i c_i/(x_i+i*y)|^2 for one critical-line zero."""
    xs = require_nodes(nodes)
    c = tuple(Fraction(value) for value in vector)
    if len(c) != len(xs):
        raise ValueError("vector length mismatch")
    y = Fraction(ordinate_offset)
    real = sum(c_i * x / (x * x + y * y) for c_i, x in zip(c, xs))
    imag = -y * sum(c_i / (x * x + y * y) for c_i, x in zip(c, xs))
    return real * real + imag * imag


def finite_online_model_quadratic(
    nodes: Sequence[Fraction],
    vector: Sequence[Fraction],
    ordinate_offsets: Iterable[Fraction],
) -> Fraction:
    """Return a finite critical-line Gram control exactly."""
    return sum(online_zero_quadratic(nodes, vector, y) for y in ordinate_offsets)
