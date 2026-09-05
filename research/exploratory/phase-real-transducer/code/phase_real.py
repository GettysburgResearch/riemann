"""Finite and safe-line helpers for the phase-flow / real-only packet.

The module deliberately separates:

* exact finite-zero algebra;
* numerical regressions of analytic identities;
* actual-Xi formulas requiring mpmath.

It does not prove RH and does not locate any new zeta zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import cmath
import math
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Zero:
    """A zero a + i b in centered coordinates."""

    a: float
    b: float

    @classmethod
    def from_complex(cls, value: complex) -> "Zero":
        return cls(float(value.real), float(value.imag))


# ---------------------------------------------------------------------------
# Hardy-flower kinematics
# ---------------------------------------------------------------------------


def flower_curve(theta: float, z_value: float) -> complex:
    """Gamma = exp(-i theta) Z."""

    return cmath.exp(-1j * theta) * z_value


def flower_velocity(
    theta: float,
    theta_prime: float,
    z_value: float,
    z_prime: float,
) -> complex:
    """d/dt [exp(-i theta) Z]."""

    return cmath.exp(-1j * theta) * (z_prime - 1j * theta_prime * z_value)


def flower_speed(theta_prime: float, z_value: float, z_prime: float) -> float:
    """|Gamma'| = sqrt(Z'^2 + theta'^2 Z^2)."""

    return math.hypot(z_prime, theta_prime * z_value)


def flower_signed_area_density(theta_prime: float, z_value: float) -> float:
    """(1/2) Im(conj(Gamma) Gamma') = -(1/2) theta' Z^2."""

    return -0.5 * theta_prime * z_value * z_value


def petal_participation_lower_bound(areas: Sequence[float]) -> float:
    """Cauchy participation ratio (sum A)^2/sum A^2 for nonnegative areas."""

    if not areas:
        return 0.0
    if any(area < 0 for area in areas):
        raise ValueError("areas must be nonnegative")
    denominator = sum(area * area for area in areas)
    if denominator == 0:
        return 0.0
    return sum(areas) ** 2 / denominator


def angular_moment_participation_bound(
    weighted_second: float,
    weighted_fourth: float,
    max_angular_gap: float,
) -> float:
    """Lower bound I2^2/(Lmax I4) from the flower participation theorem."""

    if weighted_second < 0 or weighted_fourth <= 0 or max_angular_gap <= 0:
        raise ValueError("invalid moment or angular-gap data")
    return weighted_second * weighted_second / (max_angular_gap * weighted_fourth)


def angular_curvature_numerator(
    r: float,
    r_phi: float,
    r_phi_phi: float,
) -> float:
    """Numerator of signed curvature for w(phi)=r(phi) exp(-i phi).

    The signed curvature is this number divided by
    ``(r*r + r_phi*r_phi)**1.5`` wherever the curve is regular.
    """

    return r * r_phi_phi - r * r - 2.0 * r_phi * r_phi


# ---------------------------------------------------------------------------
# Finite-zero phase field and inverse Poisson response
# ---------------------------------------------------------------------------


def max_upper_height(zeros: Sequence[Zero]) -> float:
    if not zeros:
        return float("-inf")
    return max(z.b for z in zeros)


def max_absolute_height(zeros: Sequence[Zero]) -> float:
    if not zeros:
        return 0.0
    return max(abs(z.b) for z in zeros)


def phase_velocity(x: float, y: float, zeros: Sequence[Zero]) -> float:
    """-Im P'/P(x+i y) for a polynomial with the supplied zeros.

    Requires ``y > max(Im zero)`` for the displayed positive-Poisson form.
    """

    top = max_upper_height(zeros)
    if not y > top:
        raise ValueError(f"need y>{top}, got {y}")
    total = 0.0
    for zero in zeros:
        c = y - zero.b
        total += c / ((x - zero.a) ** 2 + c * c)
    return total


def depoissonized_response(t: float, zeros: Sequence[Zero]) -> complex:
    """R(t)=sum exp(Im(lambda)|t|) exp(-i Re(lambda)t)."""

    u = abs(t)
    return sum(
        cmath.exp(zero.b * u - 1j * zero.a * t)
        for zero in zeros
    )


def phase_fourier_transform(t: float, y: float, zeros: Sequence[Zero]) -> complex:
    """Analytic Fourier transform of ``phase_velocity``.

    Convention: hat(f)(t) = integral f(x) exp(-i t x) dx.
    """

    return math.pi * math.exp(-y * abs(t)) * depoissonized_response(t, zeros)


def response_energy_cauchy(sigma: float, zeros: Sequence[Zero]) -> float:
    """Closed Cauchy-Gram formula for the weighted response energy.

    E(sigma)=integral_0^infinity exp(-2 sigma t)|R(t)|^2 dt.
    The formula is valid for sigma > max Im(lambda).
    """

    top = max_upper_height(zeros)
    if not sigma > top:
        raise ValueError(f"energy diverges or is boundary-singular for sigma<={top}")
    total = 0j
    for zj in zeros:
        for zk in zeros:
            denominator = complex(
                2.0 * sigma - zj.b - zk.b,
                zj.a - zk.a,
            )
            total += 1.0 / denominator
    if abs(total.imag) > 1e-8 * max(1.0, abs(total.real)):
        raise ArithmeticError(f"expected real energy, got {total}")
    return float(total.real)


def quartet_zeros(a: float, b: float) -> tuple[Zero, ...]:
    if a <= 0 or b < 0:
        raise ValueError("require a>0 and b>=0")
    return (
        Zero(a, b),
        Zero(a, -b),
        Zero(-a, b),
        Zero(-a, -b),
    )


def quartet_response(t: float, a: float, b: float) -> float:
    """R(t)=4 cos(a t) cosh(b |t|) for the symmetric quartet."""

    return 4.0 * math.cos(a * t) * math.cosh(b * abs(t))


def quartet_energy_closed(sigma: float, a: float, b: float) -> float:
    """Closed weighted energy for one symmetric off-axis quartet."""

    if not sigma > b:
        raise ValueError("quartet energy converges exactly for sigma>b")
    p = 2.0 * sigma
    i0 = 1.0 / p
    icos = p / (p * p + 4.0 * a * a)
    icosh = p / (p * p - 4.0 * b * b)
    icross = 0.5 * (
        (p - 2.0 * b) / ((p - 2.0 * b) ** 2 + 4.0 * a * a)
        + (p + 2.0 * b) / ((p + 2.0 * b) ** 2 + 4.0 * a * a)
    )
    return 4.0 * (i0 + icos + icosh + icross)


def quartet_polynomial_coefficients(
    a: Fraction,
    b: Fraction,
) -> tuple[Fraction, ...]:
    """Ascending coefficients of ((z-a)^2+b^2)((z+a)^2+b^2)."""

    # z^4 + 2(b^2-a^2)z^2 + (a^2+b^2)^2
    return (
        (a * a + b * b) ** 2,
        Fraction(0),
        2 * (b * b - a * a),
        Fraction(0),
        Fraction(1),
    )


def derivative_coefficients(
    coefficients: Sequence[Fraction],
) -> tuple[Fraction, ...]:
    return tuple(Fraction(i) * coefficients[i] for i in range(1, len(coefficients)))


def quartet_derivative_coefficients(
    a: Fraction,
    b: Fraction,
) -> tuple[Fraction, ...]:
    """Ascending coefficients of 4 z (z^2-a^2+b^2)."""

    return (
        Fraction(0),
        4 * (b * b - a * a),
        Fraction(0),
        Fraction(4),
    )


def quartet_pick_two_point_eigenvalues(a: float, b: float) -> tuple[float, float]:
    """Eigenvalues of the 2x2 response kernel at 0 and tau=2pi/a."""

    tau = 2.0 * math.pi / a
    off = quartet_response(tau, a, b)
    diagonal = quartet_response(0.0, a, b)
    return diagonal - abs(off), diagonal + abs(off)


# ---------------------------------------------------------------------------
# Safe-line completed-zeta phase identity
# ---------------------------------------------------------------------------


def _require_mpmath():
    try:
        import mpmath as mp  # type: ignore
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError("mpmath is required for actual-Xi numerical checks") from exc
    return mp


def xi_log_derivative(s):
    """xi'/xi in the standard completed-zeta normalization."""

    mp = _require_mpmath()
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(lambda z: mp.zeta(z), s) / mp.zeta(s)
    )


def centered_xi_phase_velocity(x, y):
    """Safe-line identity for -d_x arg X(x+i y), X(z)=xi(1/2+i z).

    For y>1/2, functional equation and conjugation give
    V_y(x)=Re xi'/xi(1/2+y+i x).
    """

    mp = _require_mpmath()
    if not y > mp.mpf("0.5"):
        raise ValueError("the direct prime-series lane requires y>1/2")
    s = mp.mpf("0.5") + y + 1j * x
    return mp.re(xi_log_derivative(s))


def completion_phase_term(s):
    """Real completion contribution in xi'/xi."""

    mp = _require_mpmath()
    return mp.re(
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
    )


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    stop = int(math.isqrt(limit))
    for prime in range(2, stop + 1):
        if sieve[prime]:
            start = prime * prime
            count = ((limit - start) // prime) + 1
            sieve[start : limit + 1 : prime] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def prime_cosine_sum(sigma, x, limit: int):
    """Sum Lambda(n)n^-sigma cos(x log n) over prime powers n<=limit."""

    mp = _require_mpmath()
    total = mp.mpf("0")
    for prime in primes_up_to(limit):
        logp = mp.log(prime)
        power = prime
        while power <= limit:
            total += logp * mp.power(power, -sigma) * mp.cos(x * mp.log(power))
            if power > limit // prime:
                break
            power *= prime
    return total


def prime_tail_absolute_bound(sigma: float, limit: int) -> float:
    """Elementary bound for sum_{n>limit} Lambda(n)n^-sigma.

    Uses Lambda(n)<=log n and the decreasing integral bound.  The precondition
    is intentionally stronger than necessary and keeps the checker simple.
    """

    if not sigma > 1.0:
        raise ValueError("need sigma>1")
    if limit < max(3, math.ceil(math.exp(1.0 / sigma))):
        raise ValueError("limit is too small for the monotone integral bound")
    l = math.log(limit)
    return (limit ** (1.0 - sigma)) * (
        l / (sigma - 1.0) + 1.0 / (sigma - 1.0) ** 2
    )


def archimedean_depoisson_kernel(t):
    """Positive-frequency archimedean term in the critical explicit formula.

    A(t)=e^(t/2)+e^(-t/2)-e^(-t/2)/(1-e^(-2t)), t>0.
    """

    mp = _require_mpmath()
    if not t > 0:
        raise ValueError("kernel is represented on t>0")
    return (
        mp.exp(t / 2)
        + mp.exp(-t / 2)
        - mp.exp(-t / 2) / (1 - mp.exp(-2 * t))
    )
