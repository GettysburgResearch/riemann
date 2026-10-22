"""Continuation helpers for the Hardy-flower / real-phase transducer packet.

The module contains two independent pieces of finite, auditable mathematics:

* angular-petal turning and curvature-defect bookkeeping;
* gamma-resolvent smoothing of exponential zero responses.

The actual-Xi theorem proved in the accompanying manuscript is analytic.  The
functions below replay its finite algebra and a non-directed numerical
regression of the prime/zero source formula.  They do not prove RH.
"""

from __future__ import annotations

import cmath
import math
from typing import Iterable, Sequence


TAU = 2.0 * math.pi


# ---------------------------------------------------------------------------
# Flower turning / curvature ledger
# ---------------------------------------------------------------------------


def open_petal_signed_turn(angular_span: float) -> float:
    """Signed tangent turn of r(phi) exp(-i phi) on one nodal interval.

    Hypotheses for the theorem: r is C^2 in the open interval, has fixed
    nonzero sign there, and has simple zeros at the two endpoints.  The result
    is independent of the radial profile.
    """

    if angular_span <= 0:
        raise ValueError("angular_span must be positive")
    return -angular_span - math.pi


def simple_petal_corner_turn(angular_span: float) -> float:
    """Closing turn at the origin for a simple petal.

    A simple petal necessarily has angular_span <= 2*pi.  The oriented corner
    turn is in (-pi, pi] and equals angular_span-pi.
    """

    if not 0 < angular_span <= TAU:
        raise ValueError("simple-petal corner requires 0<span<=2*pi")
    return angular_span - math.pi


def simple_petal_total_turn(angular_span: float) -> float:
    """Total signed turn, including the origin corner, for a simple petal."""

    return open_petal_signed_turn(angular_span) + simple_petal_corner_turn(
        angular_span
    )


def forced_lag_classes(angular_span: float) -> int:
    """Number of integer full-turn lags forced by the IVT.

    For every integer k with 2*pi*k < angular_span, a fixed-sign radius r with
    endpoint zeros has some phi satisfying r(phi)=r(phi+2*pi*k).  The two
    parameters map to the same nonzero point of the flower.
    """

    if angular_span <= 0:
        raise ValueError("angular_span must be positive")
    return max(0, math.ceil(angular_span / TAU) - 1)


def petal_is_forced_simple_from_span(angular_span: float) -> bool:
    """Whether angular span alone rules out a nonzero self-intersection."""

    if angular_span <= 0:
        raise ValueError("angular_span must be positive")
    return angular_span <= TAU


def minimum_absolute_curvature_for_span(angular_span: float) -> float:
    """Lower bound for total absolute curvature of a simple closed petal.

    The total absolute curvature includes the closing corner at the origin.
    It is at least 2*pi + 2*max(span-pi, 0).
    """

    if not 0 < angular_span <= TAU:
        raise ValueError("bound is stated for a simple petal, 0<span<=2*pi")
    return TAU + 2.0 * max(angular_span - math.pi, 0.0)


def curvature_defect_zero_count_bound(
    total_angular_span: float,
    petal_absolute_curvatures: Sequence[float],
) -> float:
    """Lower bound on petal count from total absolute-curvature excess.

    For M simple petals with absolute curvatures K_j,

        M >= total_span/pi - sum(K_j-2*pi)/(2*pi).

    The caller is responsible for supplying true total absolute curvatures.
    """

    if total_angular_span < 0:
        raise ValueError("total_angular_span must be nonnegative")
    if any(value < TAU for value in petal_absolute_curvatures):
        raise ValueError("each simple closed petal has absolute curvature >=2*pi")
    excess = sum(value - TAU for value in petal_absolute_curvatures)
    return total_angular_span / math.pi - excess / (2.0 * math.pi)


def radial_curve(phi: float, radius: float) -> complex:
    return radius * cmath.exp(-1j * phi)


def radial_curve_derivative(phi: float, radius: float, radius_prime: float) -> complex:
    return cmath.exp(-1j * phi) * (radius_prime - 1j * radius)


def hardy_clockwise_convexity_numerator(
    theta_prime: float,
    theta_second: float,
    z_value: float,
    z_prime: float,
    z_second: float,
) -> float:
    """Real numerator controlling local clockwise curvature of the flower.

    In the angular variable phi=theta(t), the signed-curvature numerator is
    ``-C/theta_prime**2`` where C is the returned quantity.  Thus C>=0
    means nonpositive (clockwise) signed curvature.
    """

    if theta_prime == 0:
        raise ZeroDivisionError("theta_prime must be nonzero")
    return (
        theta_prime * theta_prime * z_value * z_value
        + 2.0 * z_prime * z_prime
        - z_value * z_second
        + (theta_second / theta_prime) * z_value * z_prime
    )


def signed_turn_density(
    radius: float,
    radius_prime: float,
    radius_second: float,
) -> float:
    """d(arg Gamma')/dphi for Gamma=r exp(-i phi)."""

    denominator = radius * radius + radius_prime * radius_prime
    if denominator == 0:
        raise ZeroDivisionError("curve is not regular")
    numerator = radius * radius_second - radius * radius - 2.0 * radius_prime**2
    return numerator / denominator


# ---------------------------------------------------------------------------
# Gamma-resolvent response
# ---------------------------------------------------------------------------


def gamma_resolvent_multiplier(lam: complex, rate: float, order: int) -> complex:
    """Multiplier of the future Gamma resolvent on exp(lam*t)."""

    if rate <= 0:
        raise ValueError("rate must be positive")
    if order < 1:
        raise ValueError("order must be a positive integer")
    return (rate - lam) ** (-order)


def gamma_resolvent_zero_sum(
    t: float,
    centered_zeros: Iterable[complex],
    *,
    rate: float,
    order: int,
) -> complex:
    """Finite zero response sum exp(lambda*t)/(rate-lambda)^order."""

    return sum(
        cmath.exp(lam * t) * gamma_resolvent_multiplier(lam, rate, order)
        for lam in centered_zeros
    )


def finite_log_derivative(z: complex, centered_zeros: Sequence[complex]) -> complex:
    """Finite logarithmic derivative sum ``sum 1/(z-lambda)``."""

    return sum(1.0 / (z - lam) for lam in centered_zeros)


def finite_log_derivative_derivative(
    a: complex,
    derivative_order: int,
    centered_zeros: Sequence[complex],
) -> complex:
    """Derivative of the finite logarithmic derivative at ``a``."""

    if derivative_order < 0:
        raise ValueError("derivative_order must be nonnegative")
    return (
        (-1) ** derivative_order
        * math.factorial(derivative_order)
        * sum(
            (a - lam) ** (-(derivative_order + 1))
            for lam in centered_zeros
        )
    )


def finite_taylor_remainder_resolvent(
    z: complex,
    centered_zeros: Sequence[complex],
    *,
    rate: float,
    order: int,
) -> complex:
    """Taylor-remainder form of the finite meromorphic resolvent."""

    if order < 1:
        raise ValueError("order must be positive")
    delta = z - rate
    if delta == 0:
        derivative = finite_log_derivative_derivative(
            complex(rate), order, centered_zeros
        )
        return ((-1) ** order) * derivative / math.factorial(order)
    polynomial = 0j
    for k in range(order):
        derivative = finite_log_derivative_derivative(
            complex(rate), k, centered_zeros
        )
        polynomial += derivative * delta**k / math.factorial(k)
    return ((-1) ** order) * (
        finite_log_derivative(z, centered_zeros) - polynomial
    ) / delta**order


def finite_laplace_resolvent(
    z: complex,
    centered_zeros: Sequence[complex],
    *,
    rate: float,
    order: int,
) -> complex:
    """Zero-sum form ``sum 1/((rate-lambda)^order(z-lambda))``."""

    return sum(
        1.0 / ((rate - lam) ** order * (z - lam))
        for lam in centered_zeros
    )


def finite_resolvent_energy(
    sigma: float,
    centered_zeros: Sequence[complex],
    *,
    rate: float,
    order: int,
) -> float:
    """Closed weighted L2 energy for a finite resolvent response.

    E(sigma)=integral_0^infinity exp(-2*sigma*t)|R(t)|^2 dt.
    Valid when sigma exceeds every real part in ``centered_zeros``.
    """

    if not centered_zeros:
        return 0.0
    top = max(value.real for value in centered_zeros)
    if not sigma > top:
        raise ValueError(f"need sigma>{top}")
    coefficients = [
        gamma_resolvent_multiplier(value, rate, order)
        for value in centered_zeros
    ]
    total = 0j
    for j, lam_j in enumerate(centered_zeros):
        for k, lam_k in enumerate(centered_zeros):
            denominator = 2.0 * sigma - lam_j - lam_k.conjugate()
            total += coefficients[j] * coefficients[k].conjugate() / denominator
    if abs(total.imag) > 1e-9 * max(1.0, abs(total.real)):
        raise ArithmeticError(f"expected a real energy, got {total}")
    return float(total.real)


def archimedean_resolvent(
    t: float,
    *,
    rate: float,
    order: int,
    tolerance: float = 1e-16,
    max_terms: int = 1_000_000,
) -> float:
    """Gamma-resolvent of the positive-frequency archimedean source.

    A(t)=exp(t/2)+exp(-t/2)-sum_{k>=0}exp(-(2k+1/2)t).
    The displayed series is valid for t>0.  At t=0 the resolved series still
    converges for order>=2, but this routine keeps the original positive-
    frequency boundary explicit and requires t>0.
    """

    if t <= 0:
        raise ValueError("t must be positive")
    if rate <= 0.5:
        raise ValueError("rate must exceed 1/2")
    if order < 2:
        raise ValueError("order>=2 is required for the zero/source theorem")
    total = (
        math.exp(t / 2.0) / (rate - 0.5) ** order
        + math.exp(-t / 2.0) / (rate + 0.5) ** order
    )
    series = 0.0
    for k in range(max_terms):
        exponent = 2.0 * k + 0.5
        term = math.exp(-exponent * t) / (rate + exponent) ** order
        series += term
        if term < tolerance:
            break
    else:  # pragma: no cover - defensive
        raise RuntimeError("archimedean series did not converge")
    return total - series


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            count = ((limit - start) // prime) + 1
            sieve[start : limit + 1 : prime] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def prime_resolvent_tail_truncation(
    t: float,
    *,
    rate: float,
    order: int,
    limit: int,
) -> float:
    """Prime-power part of the source formula, truncated at n<=limit.

    Returns the positive quantity which is subtracted from the archimedean
    term.  Arithmetic is ordinary double precision and is reconnaissance only.
    """

    if t < 0:
        raise ValueError("t must be nonnegative")
    if rate <= 0.5:
        raise ValueError("rate must exceed 1/2")
    if order < 2:
        raise ValueError("order>=2 is required")
    if limit < 2:
        return 0.0

    total = 0.0
    exponent = rate + 0.5
    for prime in primes_up_to(limit):
        log_prime = math.log(prime)
        power = prime
        while power <= limit:
            log_power = math.log(power)
            if log_power > t:
                total += (
                    log_prime
                    * power ** (-exponent)
                    * (log_power - t) ** (order - 1)
                )
            if power > limit // prime:
                break
            power *= prime
    return math.exp(rate * t) * total / math.factorial(order - 1)


def source_resolvent_truncation(
    t: float,
    *,
    rate: float,
    order: int,
    prime_limit: int,
) -> float:
    """Truncated all-real prime-side formula for the Xi resolvent response."""

    return archimedean_resolvent(t, rate=rate, order=order) - (
        prime_resolvent_tail_truncation(
            t,
            rate=rate,
            order=order,
            limit=prime_limit,
        )
    )


def logarithmic_power_integral_tail(limit: int, exponent: float, power: int) -> float:
    """Integral_N^infinity (log x)^power x^-exponent dx.

    The closed formula is used as an elementary upper-bound component for the
    omitted prime source.  It is not directed interval arithmetic.
    """

    if limit < 2:
        raise ValueError("limit must be at least 2")
    if exponent <= 1:
        raise ValueError("exponent must exceed 1")
    if power < 0:
        raise ValueError("power must be nonnegative")
    q = exponent - 1.0
    log_limit = math.log(limit)
    factorial = math.factorial(power)
    polynomial = 0.0
    for j in range(power + 1):
        polynomial += (
            factorial
            / math.factorial(power - j)
            * log_limit ** (power - j)
            / q ** (j + 1)
        )
    return limit ** (1.0 - exponent) * polynomial


FIRST_TWENTY_GAMMAS = (
    14.134725141734695,
    21.022039638771556,
    25.01085758014569,
    30.424876125859512,
    32.93506158773919,
    37.586178158825675,
    40.9187190121475,
    43.327073280915,
    48.00515088116716,
    49.7738324776723,
    52.970321477714464,
    56.44624769706339,
    59.34704400260235,
    60.83177852460981,
    65.1125440480816,
    67.07981052949417,
    69.54640171117398,
    72.0671576744819,
    75.70469069908393,
    77.1448400688748,
)


def first_twenty_centered_zero_model() -> tuple[complex, ...]:
    """The first twenty verified critical-line pairs, as a regression fixture."""

    values: list[complex] = []
    for gamma in FIRST_TWENTY_GAMMAS:
        values.append(1j * gamma)
        values.append(-1j * gamma)
    return tuple(values)
