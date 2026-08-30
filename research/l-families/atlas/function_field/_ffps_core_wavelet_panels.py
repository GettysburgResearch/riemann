"""Exact primitive-panel and core-wavelet transforms."""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from _ffps_core_wavelet_arithmetic import (
    EXCEPTIONAL_PRIME,
    Radical,
    ZERO,
    divisors,
    is_squarefree,
    mobius,
    validate_positive_integer,
    validate_squarefree_67_free,
)


def ratio_kernel(physical_left: int, physical_right: int) -> Fraction:
    """A compact, even, exact rational toy for the source autocorrelation."""
    validate_positive_integer(physical_left)
    validate_positive_integer(physical_right)
    if 16 * physical_left < physical_right or 16 * physical_right < physical_left:
        return Fraction()
    return Fraction(
        4 * physical_left * physical_right,
        (physical_left + physical_right) ** 2,
    )


def divisor_wavelet(alpha: int, lower: int, upper: int, product_value: int) -> Fraction:
    """Finite divisor wavelet W_I^alpha(N) for the exact toy kernel."""
    if alpha not in (0, 1, 2):
        raise ValueError("alpha must be 0, 1, or 2")
    if not (0 <= lower < upper):
        raise ValueError("height endpoints must satisfy 0 <= lower < upper")
    validate_squarefree_67_free(product_value)
    physical_scale = EXCEPTIONAL_PRIME**alpha
    total = Fraction()
    for left in divisors(product_value):
        right = product_value // left
        height = max(physical_scale * left, right)
        if lower < height <= upper:
            total += ratio_kernel(physical_scale * left, right)
    return total


def direct_primitive_panel(alpha: int, sieve: int, lower: int, upper: int) -> Radical:
    """Direct ordered primitive-pair definition of P_I^alpha(d)."""
    validate_squarefree_67_free(sieve)
    physical_scale = EXCEPTIONAL_PRIME**alpha
    total = ZERO
    for left in range(1, upper // physical_scale + 1):
        if left % EXCEPTIONAL_PRIME == 0 or not is_squarefree(left):
            continue
        for right in range(1, upper + 1):
            if right % EXCEPTIONAL_PRIME == 0 or not is_squarefree(right):
                continue
            if gcd(left, right) != 1 or gcd(left * right, sieve) != 1:
                continue
            height = max(physical_scale * left, right)
            if not lower < height <= upper:
                continue
            weight = ratio_kernel(physical_scale * left, right)
            if not weight:
                continue
            product_value = left * right
            total += Radical.inv_sqrt(product_value).scale(
                mobius(left) * mobius(right) * weight
            )
    return total


def product_shell_panel(alpha: int, sieve: int, lower: int, upper: int) -> Radical:
    """One-variable product-shell definition of the same full panel."""
    validate_squarefree_67_free(sieve)
    physical_scale = EXCEPTIONAL_PRIME**alpha
    product_cap = upper * upper // physical_scale
    total = ZERO
    for product_value in range(1, product_cap + 1):
        if (
            product_value % EXCEPTIONAL_PRIME == 0
            or not is_squarefree(product_value)
            or gcd(product_value, sieve) != 1
        ):
            continue
        wavelet = divisor_wavelet(alpha, lower, upper, product_value)
        if wavelet:
            total += Radical.inv_sqrt(product_value).scale(
                mobius(product_value) * wavelet
            )
    return total


def core_wavelet(alpha: int, core: int, lower: int, upper: int) -> Radical:
    """Z_I^alpha(core), before the outer 1/sqrt(core) assembly."""
    validate_squarefree_67_free(core)
    physical_scale = EXCEPTIONAL_PRIME**alpha
    product_cap = upper * upper // physical_scale
    total = ZERO
    for cofactor in range(1, product_cap // core + 1):
        if (
            cofactor % EXCEPTIONAL_PRIME == 0
            or not is_squarefree(cofactor)
            or gcd(cofactor, core) != 1
        ):
            continue
        wavelet = divisor_wavelet(alpha, lower, upper, core * cofactor)
        if wavelet:
            total += Radical.inv_sqrt(cofactor).scale(
                mobius(cofactor) * wavelet
            )
    return total


def core_assembled_panel(alpha: int, sieve: int, lower: int, upper: int) -> Radical:
    """Sum_(r|d) Z_I^alpha(r)/sqrt(r)."""
    validate_squarefree_67_free(sieve)
    total = ZERO
    for core in divisors(sieve):
        total += Radical.inv_sqrt(core) * core_wavelet(
            alpha, core, lower, upper
        )
    return total


def recovered_core(alpha: int, core: int, lower: int, upper: int) -> Radical:
    """Boolean divisor inversion: sqrt(r) sum_(s|r) mu(r/s) P(s)."""
    validate_squarefree_67_free(core)
    inverted = ZERO
    for sieve in divisors(core):
        inverted += product_shell_panel(alpha, sieve, lower, upper).scale(
            mobius(core // sieve)
        )
    return Radical.sqrt(core) * inverted
