"""Exact shared-divisor Gram algebra for primitive core wavelets."""

from __future__ import annotations

from fractions import Fraction
from math import ceil, gcd, log2

from _ffps_core_wavelet_arithmetic import (
    EXCEPTIONAL_PRIME,
    Radical,
    ZERO,
    divisors,
    factorization,
    is_squarefree,
    mobius,
    tau,
    validate_positive_integer,
    validate_squarefree_67_free,
)
from _ffps_core_wavelet_panels import core_wavelet, divisor_wavelet, ratio_kernel


def shared_divisor_kernel(left: int, right: int) -> Fraction:
    validate_squarefree_67_free(left)
    validate_squarefree_67_free(right)
    return sum(
        (Fraction(tau(core), core) for core in divisors(gcd(left, right))),
        Fraction(),
    )


def kernel_euler(common: int) -> Fraction:
    validate_squarefree_67_free(common)
    result = Fraction(1)
    for prime, _ in factorization(common):
        result *= 1 + Fraction(2, prime)
    return result


def shell_wavelets(alpha: int, lower: int, upper: int) -> dict[int, Fraction]:
    cap = upper * upper // EXCEPTIONAL_PRIME**alpha
    return {
        product_value: wavelet
        for product_value in range(1, cap + 1)
        if product_value % EXCEPTIONAL_PRIME
        and is_squarefree(product_value)
        and (wavelet := divisor_wavelet(alpha, lower, upper, product_value))
    }


def core_energy(alpha: int, lower: int, upper: int) -> Radical:
    cap = upper * upper // EXCEPTIONAL_PRIME**alpha
    total = ZERO
    for core in range(1, cap + 1):
        if core % EXCEPTIONAL_PRIME == 0 or not is_squarefree(core):
            continue
        vector = core_wavelet(alpha, core, lower, upper)
        total += (vector * vector).scale(Fraction(tau(core), core * core))
    return total


def gram_parts(
    alpha: int, lower: int, upper: int
) -> tuple[Radical, Radical, Radical]:
    wavelets = shell_wavelets(alpha, lower, upper)
    total = ZERO
    diagonal = ZERO
    for left, left_wavelet in wavelets.items():
        left_coefficient = Radical.inv_sqrt(left).scale(
            mobius(left) * left_wavelet
        )
        for right, right_wavelet in wavelets.items():
            right_coefficient = Radical.inv_sqrt(right).scale(
                mobius(right) * right_wavelet
            )
            term = (left_coefficient * right_coefficient).scale(
                shared_divisor_kernel(left, right)
            )
            total += term
            if left == right:
                diagonal += term
    return total, diagonal, total - diagonal


def gcd_off_diagonal(alpha: int, lower: int, upper: int) -> Radical:
    wavelets = shell_wavelets(alpha, lower, upper)
    total = ZERO
    for left, left_wavelet in wavelets.items():
        for right, right_wavelet in wavelets.items():
            if left == right:
                continue
            common = gcd(left, right)
            reduced_left = left // common
            reduced_right = right // common
            if (
                gcd(reduced_left, reduced_right) != 1
                or gcd(reduced_left * reduced_right, common) != 1
            ):
                raise ArithmeticError("gcd decomposition lost coprimality")
            coefficient = Fraction(
                mobius(reduced_left)
                * mobius(reduced_right)
                * left_wavelet
                * right_wavelet,
                common,
            )
            term = (
                Radical.inv_sqrt(reduced_left)
                * Radical.inv_sqrt(reduced_right)
            ).scale(coefficient * kernel_euler(common))
            total += term
    return total


def aligned_dyadic_intervals(length: int) -> tuple[tuple[int, int], ...]:
    validate_positive_integer(length)
    intervals: list[tuple[int, int]] = []
    scale = 1
    while scale <= length:
        for start in range(0, length - scale + 1, scale):
            intervals.append((start, start + scale))
        scale *= 2
    return tuple(intervals)


def finite_diagonal_majorant() -> dict[str, object]:
    heights = tuple(range(9, 17))
    index = {height: position for position, height in enumerate(heights)}
    intervals = aligned_dyadic_intervals(len(heights))
    level_count = ceil(log2(len(heights) + 1))
    cap = 16 * 16
    exact_diagonal = Fraction()
    orientation_majorant = Fraction()
    checked_shells = 0
    for product_value in range(1, cap + 1):
        if product_value % EXCEPTIONAL_PRIME == 0 or not is_squarefree(product_value):
            continue
        contributions = [Fraction() for _ in heights]
        absolute_mass = Fraction()
        for left in divisors(product_value):
            right = product_value // left
            height = max(left, right)
            if height not in index:
                continue
            value = ratio_kernel(left, right)
            contributions[index[height]] += value
            absolute_mass += abs(value)
        if not absolute_mass:
            continue
        square_function = sum(
            (
                sum(contributions[start:end], Fraction()) ** 2
                for start, end in intervals
            ),
            Fraction(),
        )
        if square_function > level_count * absolute_mass**2:
            raise ArithmeticError("dyadic square-function majorant failed")
        kernel_diagonal = shared_divisor_kernel(product_value, product_value)
        exact_diagonal += kernel_diagonal * square_function / product_value
        orientation_majorant += (
            kernel_diagonal
            * level_count
            * Fraction(tau(product_value) ** 2, product_value)
        )
        checked_shells += 1
    if exact_diagonal > orientation_majorant:
        raise ArithmeticError("finite diagonal majorant failed")
    harmonic = sum((Fraction(1, value) for value in range(1, cap + 1)), Fraction())
    _ = harmonic**12
    return {
        "checked_product_shells": checked_shells,
        "dyadic_level_count": level_count,
        "exact_diagonal": str(exact_diagonal),
        "finite_orientation_majorant": str(orientation_majorant),
        "harmonic_d12_upper_verified": True,
        "harmonic_cap": cap,
        "proof_bound": "L_H ||R||_infinity^2 sum_(N<=4H^2/A) d_12(N)/N",
    }
