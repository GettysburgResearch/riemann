"""Helpers for PFR-T7--T9.

This module supplies finite algebra and non-directed numerical regressions for:

* the prime-knot jump law of the actual-Xi Gamma resolvent;
* the curvature / derivative-critical-point Poisson transducer;
* complex Gamma soft ordinate filters and finite-horizon leakage.

It does not prove RH, locate an off-line zero, or certify analytic continuation.
"""

from __future__ import annotations

import cmath
import math
from typing import Iterable, Sequence


# First twenty positive ordinates, used only for a bounded numerical regression.
FIRST_ZETA_ZERO_ORDINATES: tuple[float, ...] = (
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


# ---------------------------------------------------------------------------
# PFR-T7: prime knots and resolvent ladder
# ---------------------------------------------------------------------------


def prime_knot_jump(m: int, mangoldt: float, n: int) -> float:
    """Jump [right-left] of derivative order m-1 at t=log(n).

    Formula: (-1)^(m+1) Lambda(n)/sqrt(n).
    """

    if m < 2:
        raise ValueError("m must be at least 2")
    if n < 2 or mangoldt < 0:
        raise ValueError("invalid prime-power data")
    return ((-1.0) ** (m + 1)) * mangoldt / math.sqrt(n)


def prime_tail_knot_term(
    t: float,
    *,
    tau: float,
    mangoldt: float,
    n: int,
    a: float,
    m: int,
) -> float:
    """One prime-power term in the source formula for R_(a,m)."""

    if a <= 0.5 or m < 2:
        raise ValueError("need a>1/2 and m>=2")
    if t >= tau:
        return 0.0
    return (
        -mangoldt
        * (n ** (-a - 0.5))
        * math.exp(a * t)
        * ((tau - t) ** (m - 1))
        / math.factorial(m - 1)
    )


def finite_resolvent_response(
    t: float,
    lambdas: Sequence[complex],
    *,
    q: complex,
    m: int,
) -> complex:
    """Finite response sum exp(lambda*t)/(q-lambda)^m."""

    if q.real <= 0.5 or m < 2:
        raise ValueError("need Re(q)>1/2 and m>=2")
    return sum(cmath.exp(lam * t) / ((q - lam) ** m) for lam in lambdas)


def finite_resolvent_energy(
    sigma: float,
    lambdas: Sequence[complex],
    *,
    q: complex,
    m: int,
) -> float:
    """Exact Cauchy-Gram energy for a finite filtered response."""

    if not lambdas:
        return 0.0
    boundary = max(lam.real for lam in lambdas)
    if sigma <= boundary:
        raise ValueError("energy is divergent or boundary-singular")
    coeffs = [1.0 / ((q - lam) ** m) for lam in lambdas]
    total = 0j
    for j, lam_j in enumerate(lambdas):
        for k, lam_k in enumerate(lambdas):
            total += coeffs[j] * coeffs[k].conjugate() / (
                2.0 * sigma - lam_j - lam_k.conjugate()
            )
    if abs(total.imag) > 1e-8 * max(1.0, abs(total.real)):
        raise ArithmeticError(f"expected a real energy, got {total}")
    return float(total.real)


# ---------------------------------------------------------------------------
# PFR-T8: curvature and critical-point phase flow
# ---------------------------------------------------------------------------


def tangent_phase_acceleration(zeta_prime: complex, zeta_second: complex) -> float:
    """Re(zeta''/zeta'), equal to d_t arg zeta'(1/2+it)."""

    if zeta_prime == 0:
        raise ZeroDivisionError("zeta_prime must be nonzero")
    return float((zeta_second / zeta_prime).real)


def hardy_curvature_from_complex_derivatives(
    theta_prime: float,
    zeta_prime: complex,
    zeta_second: complex,
) -> tuple[float, float]:
    """Return (D_H, C_H) from complex zeta derivatives.

    D_H=|zeta'|^2 and -theta' C_H=Re(conj(zeta') zeta'').
    """

    if theta_prime <= 0:
        raise ValueError("theta_prime must be positive")
    d_h = abs(zeta_prime) ** 2
    c_h = -((zeta_prime.conjugate() * zeta_second).real) / theta_prime
    return float(d_h), float(c_h)


def critical_point_poisson_field(
    t: float,
    sigma0: float,
    critical_points: Sequence[complex],
) -> float:
    """Re(P''/P') on a line from the critical points of a polynomial."""

    total = 0.0
    for point in critical_points:
        horizontal = sigma0 - point.real
        if horizontal == 0.0:
            raise ValueError("critical point lies on the observation line")
        vertical = t - point.imag
        total += horizontal / (horizontal * horizontal + vertical * vertical)
    return total


def critical_point_signed_index(
    sigma0: float,
    critical_points: Sequence[complex],
) -> int:
    """N_left-N_right, equal to (1/pi) integral of the Poisson field."""

    left = 0
    right = 0
    for point in critical_points:
        if point.real < sigma0:
            left += 1
        elif point.real > sigma0:
            right += 1
        else:
            raise ValueError("critical point lies on the observation line")
    return left - right


def critical_point_field_integral(
    sigma0: float,
    critical_points: Sequence[complex],
) -> float:
    """Analytic whole-line integral of the finite Poisson field."""

    return math.pi * critical_point_signed_index(sigma0, critical_points)


# ---------------------------------------------------------------------------
# PFR-T9: soft complex-Gamma localization
# ---------------------------------------------------------------------------


def soft_band_scales(a: float, w: float, W: float) -> tuple[float, float, float]:
    """Return D_in, D_out, eta for the guarded soft band."""

    if a <= 0.5 or w < 0 or W <= w:
        raise ValueError("need a>1/2 and 0<=w<W")
    d_in = math.hypot(a + 0.5, w)
    d_out = math.hypot(a - 0.5, W)
    if d_out <= d_in:
        raise ValueError("guard band is too narrow: D_out must exceed D_in")
    return d_in, d_out, d_in / d_out


def normalized_gamma_weight(
    lam: complex,
    *,
    a: float,
    center: float,
    m: int,
    d_in: float,
) -> complex:
    """(D_in/(a+i*center-lambda))^m."""

    if a <= 0.5 or m < 2 or d_in <= 0:
        raise ValueError("invalid Gamma-filter parameters")
    return (d_in / (complex(a, center) - lam)) ** m


def finite_horizon_factor(exponent: float, horizon: float) -> float:
    """sqrt(int_0^L exp(2*exponent*t) dt)."""

    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    if horizon == 0:
        return 0.0
    if abs(exponent) < 1e-14:
        return math.sqrt(horizon)
    value = math.expm1(2.0 * exponent * horizon) / (2.0 * exponent)
    return math.sqrt(value)


def finite_horizon_leakage_bound(
    coefficient_mass: float,
    *,
    sigma: float,
    horizon: float,
    unconditional_growth: float = 0.5,
) -> float:
    """C_out * Phi(B-sigma,L), with B<=1/2 by the critical strip."""

    if coefficient_mass < 0:
        raise ValueError("coefficient mass must be nonnegative")
    return coefficient_mass * finite_horizon_factor(
        unconditional_growth - sigma,
        horizon,
    )


# ---------------------------------------------------------------------------
# Bounded actual-Xi source/zero-prefix regression for complex q
# ---------------------------------------------------------------------------


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


def von_mangoldt_prime_powers(limit: int) -> Iterable[tuple[int, float]]:
    for prime in primes_up_to(limit):
        logp = math.log(prime)
        power = prime
        while power <= limit:
            yield power, logp
            if power > limit // prime:
                break
            power *= prime


def complex_archimedean_resolvent(
    t: float,
    *,
    q: complex,
    m: int,
    tolerance: float = 1e-17,
) -> complex:
    if t <= 0 or q.real <= 0.5 or m < 2:
        raise ValueError("need t>0, Re(q)>1/2, m>=2")
    total = cmath.exp(t / 2.0) / ((q - 0.5) ** m)
    total += cmath.exp(-t / 2.0) / ((q + 0.5) ** m)
    for k in range(1_000_000):
        exponent = 2.0 * k + 0.5
        term = math.exp(-exponent * t) / ((q + exponent) ** m)
        total -= term
        if abs(term) < tolerance:
            break
    else:  # pragma: no cover
        raise RuntimeError("archimedean series did not converge")
    return total


def complex_prime_tail_resolvent(
    t: float,
    *,
    q: complex,
    m: int,
    limit: int,
) -> complex:
    if t < 0 or q.real <= 0.5 or m < 2 or limit < 2:
        raise ValueError("invalid source truncation parameters")
    total = 0j
    for n, logp in von_mangoldt_prime_powers(limit):
        logn = math.log(n)
        if logn <= t:
            continue
        total += (
            logp
            * cmath.exp(-(q + 0.5) * logn)
            * ((logn - t) ** (m - 1))
        )
    return cmath.exp(q * t) * total / math.factorial(m - 1)


def complex_source_resolvent_truncation(
    t: float,
    *,
    q: complex,
    m: int,
    prime_limit: int,
) -> complex:
    return complex_archimedean_resolvent(t, q=q, m=m) - complex_prime_tail_resolvent(
        t,
        q=q,
        m=m,
        limit=prime_limit,
    )


def complex_zero_prefix_resolvent(
    t: float,
    *,
    q: complex,
    m: int,
    ordinates: Sequence[float] = FIRST_ZETA_ZERO_ORDINATES,
) -> complex:
    total = 0j
    for gamma in ordinates:
        total += cmath.exp(1j * gamma * t) / ((q - 1j * gamma) ** m)
        total += cmath.exp(-1j * gamma * t) / ((q + 1j * gamma) ** m)
    return total
