"""Symmetric real-response and flower/Speiser screening helpers.

This module accompanies PFR-T10--T11 and PFR-R4.  It separates exact finite
algebra from non-directed actual-zeta regressions.  Nothing here proves RH.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence


@dataclass(frozen=True)
class CriticalPoint:
    """A critical point alpha + i beta relative to a vertical observation line."""

    alpha: float
    beta: float


# ---------------------------------------------------------------------------
# PFR-T10: symmetric resolvent / positive-definite normal form
# ---------------------------------------------------------------------------


def symmetric_resolvent_weight(lam: complex, rate: float, order: int) -> complex:
    """Return (rate^2-lam^2)^(-order)."""

    if rate <= 0.5:
        raise ValueError("rate must exceed 1/2 for the actual-Xi application")
    if order < 1:
        raise ValueError("order must be a positive integer")
    return (rate * rate - lam * lam) ** (-order)


def symmetric_resolvent_response(
    t: float,
    centered_zeros: Iterable[complex],
    *,
    rate: float,
    order: int,
) -> complex:
    """Finite version of S_(a,m)(t)=sum exp(lam*t)/(a^2-lam^2)^m."""

    return sum(
        cmath.exp(lam * t) * symmetric_resolvent_weight(lam, rate, order)
        for lam in centered_zeros
    )


def symmetric_resolvent_energy(
    sigma: float,
    centered_zeros: Sequence[complex],
    *,
    rate: float,
    order: int,
) -> float:
    """Closed finite Cauchy--Gram formula for the damped L2 energy.

    This equals integral_0^infinity exp(-2*sigma*t)|S(t)|^2 dt whenever
    sigma exceeds every real part of the finite exponent set.
    """

    if not centered_zeros:
        return 0.0
    top = max(lam.real for lam in centered_zeros)
    if not sigma > top:
        raise ValueError(f"need sigma>{top}")
    coeffs = [symmetric_resolvent_weight(lam, rate, order) for lam in centered_zeros]
    total = 0j
    for j, lam_j in enumerate(centered_zeros):
        for k, lam_k in enumerate(centered_zeros):
            total += (
                coeffs[j]
                * coeffs[k].conjugate()
                / (2.0 * sigma - lam_j - lam_k.conjugate())
            )
    if abs(total.imag) > 1e-9 * max(1.0, abs(total.real)):
        raise ArithmeticError(f"expected real energy, got {total}")
    return float(total.real)


def symmetric_toeplitz_gram(
    times: Sequence[float],
    centered_zeros: Sequence[complex],
    *,
    rate: float,
    order: int,
) -> list[list[complex]]:
    """Return [S(t_j-t_k)] for a finite zero model."""

    return [
        [
            symmetric_resolvent_response(
                t_j - t_k,
                centered_zeros,
                rate=rate,
                order=order,
            )
            for t_k in times
        ]
        for t_j in times
    ]


def two_point_toeplitz_eigenvalues(s0: float, st: float) -> tuple[float, float]:
    """Eigenvalues of [[S(0),S(t)],[S(t),S(0)]] for real even S."""

    return s0 - abs(st), s0 + abs(st)


def partial_fraction_coefficients(rate: float, order: int) -> list[float]:
    r"""Coefficients c_(m,k) in

        (a^2-z^2)^(-m)
          = sum_(k=1)^m c_(m,k)[(a-z)^(-k)+(a+z)^(-k)].
    """

    if rate <= 0:
        raise ValueError("rate must be positive")
    if order < 1:
        raise ValueError("order must be positive")
    result: list[float] = []
    for k in range(1, order + 1):
        coefficient = (
            2.0 ** (k - 2 * order)
            * math.comb(2 * order - k - 1, order - k)
            * rate ** (k - 2 * order)
        )
        result.append(coefficient)
    return result


def finite_log_derivative_derivative(
    z: complex,
    derivative_order: int,
    centered_zeros: Sequence[complex],
) -> complex:
    """Derivative of sum_lambda 1/(z-lambda)."""

    if derivative_order < 0:
        raise ValueError("derivative_order must be nonnegative")
    return (
        (-1) ** derivative_order
        * math.factorial(derivative_order)
        * sum((z - lam) ** (-(derivative_order + 1)) for lam in centered_zeros)
    )


def _solve_linear_system(matrix: list[list[complex]], rhs: list[complex]) -> list[complex]:
    """Small dense Gaussian elimination with partial pivoting."""

    n = len(rhs)
    a = [row[:] + [rhs_value] for row, rhs_value in zip(matrix, rhs)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) == 0:
            raise ArithmeticError("singular interpolation system")
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [value / scale for value in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            if factor == 0:
                continue
            a[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(a[row], a[col])
            ]
    return [a[row][-1] for row in range(n)]


def two_point_hermite_coefficients(
    rate: float,
    order: int,
    derivative: Callable[[complex, int], complex],
) -> list[complex]:
    """Polynomial coefficients for Hermite interpolation at +/-rate.

    The returned polynomial has degree at most 2*order-1 and matches the first
    ``order`` jets of the supplied function at both nodes.
    """

    if rate <= 0:
        raise ValueError("rate must be positive")
    if order < 1:
        raise ValueError("order must be positive")
    degree_count = 2 * order
    matrix: list[list[complex]] = []
    rhs: list[complex] = []
    for node in (-rate, rate):
        for derivative_order in range(order):
            row: list[complex] = []
            for power in range(degree_count):
                if power < derivative_order:
                    row.append(0j)
                else:
                    row.append(
                        math.factorial(power)
                        / math.factorial(power - derivative_order)
                        * node ** (power - derivative_order)
                    )
            matrix.append(row)
            rhs.append(derivative(complex(node), derivative_order))
    return _solve_linear_system(matrix, rhs)


def evaluate_polynomial(coefficients: Sequence[complex], z: complex) -> complex:
    """Evaluate ascending polynomial coefficients by Horner's rule."""

    value = 0j
    for coefficient in reversed(coefficients):
        value = value * z + coefficient
    return value


def finite_hermite_source_resolvent(
    z: complex,
    centered_zeros: Sequence[complex],
    *,
    rate: float,
    order: int,
) -> complex:
    """Hermite-remainder source form of the symmetric finite resolvent."""

    derivative = lambda point, degree: finite_log_derivative_derivative(
        point,
        degree,
        centered_zeros,
    )
    interpolation = two_point_hermite_coefficients(rate, order, derivative)
    f_value = finite_log_derivative_derivative(z, 0, centered_zeros)
    numerator = f_value - evaluate_polynomial(interpolation, z)
    return numerator / (rate * rate - z * z) ** order


def finite_partial_fraction_resolvent(
    z: complex,
    centered_zeros: Sequence[complex],
    *,
    rate: float,
    order: int,
) -> complex:
    """Direct zero partial fraction for comparison with the source form."""

    return sum(
        symmetric_resolvent_weight(lam, rate, order) / (z - lam)
        for lam in centered_zeros
    )


def green_kernel_order_two(t: float, rate: float) -> float:
    """Green kernel of (a^2-D^2)^2 on the full real line."""

    if rate <= 0:
        raise ValueError("rate must be positive")
    u = abs(t)
    return math.exp(-rate * u) * (1.0 + rate * u) / (4.0 * rate**3)


# ---------------------------------------------------------------------------
# PFR-T11 / PFR-R4: flower--Speiser Poisson screening and Gauss ledger
# ---------------------------------------------------------------------------


def poisson_kernel(distance: float, offset: float) -> float:
    """Cauchy/Poisson kernel d/(d^2+offset^2), d>0."""

    if distance <= 0:
        raise ValueError("distance must be positive")
    return distance / (distance * distance + offset * offset)


def split_critical_point_field(
    t: float,
    observation_sigma: float,
    critical_points: Sequence[CriticalPoint],
) -> tuple[float, float, float]:
    """Return left field, right field, and signed phase acceleration."""

    left = 0.0
    right = 0.0
    for point in critical_points:
        displacement = observation_sigma - point.alpha
        if displacement == 0:
            raise ValueError("a critical point lies on the observation line")
        value = poisson_kernel(abs(displacement), t - point.beta)
        if displacement > 0:
            left += value
        else:
            right += value
    return left, right, left - right


def screening_overlap_numeric(
    observation_sigma: float,
    critical_points: Sequence[CriticalPoint],
    *,
    cutoff: float = 200.0,
    panels: int = 200_000,
) -> tuple[float, float, float, int, int]:
    """Trapezoidal reconnaissance for the whole-line screening identity.

    Returns positive mass, overlap, negative mass, N_left, N_right.  The finite
    cutoff makes this a numerical regression, not a directed certificate.
    """

    if cutoff <= 0 or panels < 100:
        raise ValueError("invalid quadrature parameters")
    step = 2.0 * cutoff / panels
    positive = 0.0
    negative = 0.0
    overlap = 0.0
    for index in range(panels + 1):
        t = -cutoff + index * step
        left, right, signed = split_critical_point_field(
            t,
            observation_sigma,
            critical_points,
        )
        weight = 0.5 if index in (0, panels) else 1.0
        positive += weight * max(signed, 0.0)
        negative += weight * max(-signed, 0.0)
        overlap += weight * min(left, right)
    positive *= step
    negative *= step
    overlap *= step
    n_left = sum(point.alpha < observation_sigma for point in critical_points)
    n_right = sum(point.alpha > observation_sigma for point in critical_points)
    return positive, overlap, negative, n_left, n_right


def mirrored_screening_field(
    t: float,
    *,
    observation_sigma: float,
    distance: float,
    ordinate: float,
) -> float:
    """Exact left/right mirror pair; the signed field should vanish."""

    points = (
        CriticalPoint(observation_sigma - distance, ordinate),
        CriticalPoint(observation_sigma + distance, ordinate),
    )
    return split_critical_point_field(t, observation_sigma, points)[2]


def polynomial_log_derivative(z: complex, zeros: Sequence[complex]) -> complex:
    return sum(1.0 / (z - zero) for zero in zeros)


def rectangle_argument_ledger(
    zeros: Sequence[complex],
    *,
    sigma_left: float,
    sigma_right: float,
    t_bottom: float,
    t_top: float,
    quadrature_steps: int = 200_000,
) -> tuple[float, int]:
    """Numerical argument-principle ledger for an entire finite product.

    Returns the oriented boundary argument change and the exact count of the
    supplied zeros in the open rectangle.  The quadrature is a regression.
    """

    if not sigma_left < sigma_right or not t_bottom < t_top:
        raise ValueError("invalid rectangle")
    if quadrature_steps < 100:
        raise ValueError("quadrature_steps too small")

    def trap_integral(func: Callable[[float], float], start: float, stop: float) -> float:
        step = (stop - start) / quadrature_steps
        total = 0.0
        for index in range(quadrature_steps + 1):
            x = start + index * step
            weight = 0.5 if index in (0, quadrature_steps) else 1.0
            total += weight * func(x)
        return total * step

    bottom = trap_integral(
        lambda sigma: polynomial_log_derivative(
            complex(sigma, t_bottom),
            zeros,
        ).imag,
        sigma_left,
        sigma_right,
    )
    right = trap_integral(
        lambda t: polynomial_log_derivative(
            complex(sigma_right, t),
            zeros,
        ).real,
        t_bottom,
        t_top,
    )
    top = trap_integral(
        lambda sigma: polynomial_log_derivative(
            complex(sigma, t_top),
            zeros,
        ).imag,
        sigma_left,
        sigma_right,
    )
    left = trap_integral(
        lambda t: polynomial_log_derivative(
            complex(sigma_left, t),
            zeros,
        ).real,
        t_bottom,
        t_top,
    )
    oriented_change = bottom + right - top - left
    count = sum(
        sigma_left < zero.real < sigma_right
        and t_bottom < zero.imag < t_top
        for zero in zeros
    )
    return oriented_change, count
