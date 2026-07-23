#!/usr/bin/env python3
"""Exact rational geometry for the L-4204 first-cell prime-entry event.

All transcendental scale factors are stripped.  The module checks the hat value,
unit-phase corner matrix, fixed-vector quadratic form, derivative limit, and
first-cell norm.  It is a regression kernel, not a prime or zeta computation.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Sequence

Gaussian = tuple[Fraction, Fraction]


class EventError(ValueError):
    """Raised for invalid first-cell event parameters."""


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def gconj(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def gscale(value: Gaussian, scalar: Fraction | int) -> Gaussian:
    scale = Fraction(scalar)
    return value[0] * scale, value[1] * scale


def gabs2(value: Gaussian) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def first_cell_hat(k_cells: int, eta: Fraction) -> Fraction:
    """Return tau_{K-1} for eta=epsilon/L0.

    The first-cell condition is 0 < eta < 1/(K-1).
    """
    if k_cells < 2:
        raise EventError("K must be at least two")
    if eta <= 0 or eta >= Fraction(1, k_cells - 1):
        raise EventError("eta must lie strictly inside the first deposition cell")
    return k_cells * eta / (1 + eta)


def stripped_corner_coefficient(
    k_cells: int,
    eta: Fraction,
    phase: Gaussian,
) -> Gaussian:
    """Upper-corner coefficient after stripping log(p)/(pi*sqrt(q))."""
    if gabs2(phase) != 1:
        raise EventError("phase must have exact unit modulus")
    return gscale(phase, first_cell_hat(k_cells, eta) / 2)


def stripped_rayleigh(
    k_cells: int,
    eta: Fraction,
    phase: Gaussian,
    vector: Sequence[Gaussian],
) -> Fraction:
    """Return the stripped S_q quadratic form.

    The full value is log(p)/(pi*sqrt(q)) times this exact rational.
    """
    if len(vector) != k_cells:
        raise EventError("vector length must equal K")
    if gabs2(phase) != 1:
        raise EventError("phase must have exact unit modulus")
    product = gmul(phase, gmul(gconj(vector[0]), vector[-1]))
    return first_cell_hat(k_cells, eta) * product[0]


def stripped_matrix_quadratic(
    k_cells: int,
    eta: Fraction,
    phase: Gaussian,
    vector: Sequence[Gaussian],
) -> Fraction:
    """Evaluate the two explicit corner terms independently."""
    coefficient = stripped_corner_coefficient(k_cells, eta, phase)
    upper = gmul(gconj(vector[0]), gmul(coefficient, vector[-1]))
    lower = gmul(gconj(vector[-1]), gmul(gconj(coefficient), vector[0]))
    total = gadd(upper, lower)
    if total[1] != 0:
        raise AssertionError("Hermitian corner quadratic acquired an imaginary part")
    return total[0]


def stripped_operator_norm(k_cells: int, eta: Fraction, phase: Gaussian) -> Fraction:
    """Exact norm after stripping log(p)/(pi*sqrt(q))."""
    coefficient = stripped_corner_coefficient(k_cells, eta, phase)
    # The phase is unit modulus, so the 2x2 Hermitian corner eigenvalues are
    # +-hat/2.  Return the positive magnitude without a square root.
    if gabs2(phase) != 1:
        raise EventError("phase must have exact unit modulus")
    return first_cell_hat(k_cells, eta) / 2
