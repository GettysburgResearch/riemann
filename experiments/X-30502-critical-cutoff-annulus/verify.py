#!/usr/bin/env python3
"""Directed rational verifier for L-30503.

The checker proves a rational enclosure for

    H(5/2)=P(1/2) log(5/2)+P'(1/2),
    P(s)=1-eta(s)-2^(-s),

using the globally convergent Hasse series for eta. It also checks the exact
first-omitted-index geometry. The uniform-limit and atomic-norm arguments are
proved analytically in L-30503.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path

Interval = tuple[Fraction, Fraction]


def iadd(a: Interval, b: Interval) -> Interval:
    return a[0] + b[0], a[1] + b[1]


def ineg(a: Interval) -> Interval:
    return -a[1], -a[0]


def iscale(c: Fraction, a: Interval) -> Interval:
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def imul(a: Interval, b: Interval) -> Interval:
    values = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(values), max(values)


def invsqrt_interval(n: int, digits: int = 40) -> Interval:
    scale = 10**digits
    lower_root_numerator = isqrt(n * scale * scale)
    return (
        Fraction(scale, lower_root_numerator + 1),
        Fraction(scale, lower_root_numerator),
    )


def log_interval(x: Fraction, terms: int = 700) -> Interval:
    assert x >= 1
    if x == 1:
        return Fraction(0), Fraction(0)
    y = (x - 1) / (x + 1)
    y2 = y * y
    power = y
    partial = Fraction(0)
    for j in range(terms):
        partial += power / Fraction(2 * j + 1)
        power *= y2
    lower = 2 * partial
    remainder = 2 * power / Fraction(2 * terms + 1) / (1 - y2)
    return lower, lower + remainder


def eta_hasse(order: int = 30) -> tuple[Interval, Interval]:
    eta: Interval = (Fraction(0), Fraction(0))
    eta_prime: Interval = (Fraction(0), Fraction(0))
    for n in range(order + 1):
        difference: Interval = (Fraction(0), Fraction(0))
        derivative: Interval = (Fraction(0), Fraction(0))
        for k in range(n + 1):
            inverse_root = invsqrt_interval(k + 1)
            sign = Fraction(comb(n, k) * (1 if k % 2 == 0 else -1))
            difference = iadd(difference, iscale(sign, inverse_root))

            if k == 0:
                log_term = (Fraction(0), Fraction(0))
            else:
                log_term = imul(inverse_root, log_interval(Fraction(k + 1)))
            derivative_sign = Fraction(
                comb(n, k) * (-1 if k % 2 == 0 else 1)
            )
            derivative = iadd(
                derivative, iscale(derivative_sign, log_term)
            )

        weight = Fraction(1, 2 ** (n + 1))
        eta = iadd(eta, iscale(weight, difference))
        eta_prime = iadd(eta_prime, iscale(weight, derivative))

    # Hasse tail: 0 <= Delta^n[(k+1)^(-1/2)]_(k=0) <= 1.
    eta = (eta[0], eta[1] + Fraction(1, 2 ** (order + 1)))

    # At s=1/2 the derivative of each finite difference has magnitude <8:
    # |psi(1/2)|<3 and int t^(-1/2)e^(-t)|log t|dt<5.
    derivative_tail = Fraction(8, 2 ** (order + 1))
    eta_prime = (
        eta_prime[0] - derivative_tail,
        eta_prime[1] + derivative_tail,
    )
    return eta, eta_prime


def decimal_bounds(interval: Interval, digits: int = 18) -> list[str]:
    scale = 10**digits
    lower_numerator = interval[0].numerator * scale // interval[0].denominator
    upper_numerator = -(
        (-interval[1].numerator * scale) // interval[1].denominator
    )

    def format_integer(value: int) -> str:
        sign = "-" if value < 0 else ""
        value = abs(value)
        whole, fractional = divmod(value, scale)
        return f"{sign}{whole}.{fractional:0{digits}d}"

    return [format_integer(lower_numerator), format_integer(upper_numerator)]


def first_even_omitted(endpoint: int, q: int) -> int:
    k = 1
    while 2 * k * q - 1 <= endpoint:
        k += 1
    return k


def first_odd_omitted(endpoint: int, q: int) -> int:
    k = 1
    while (2 * k + 1) * q <= endpoint:
        k += 1
    return k


def main() -> None:
    eta, eta_prime = eta_hasse()
    inverse_root_two = invsqrt_interval(2)
    log_two = log_interval(Fraction(2))
    log_five_halves = log_interval(Fraction(5, 2))

    p_value = iadd(
        iadd((Fraction(1), Fraction(1)), ineg(eta)),
        ineg(inverse_root_two),
    )
    p_derivative = iadd(
        ineg(eta_prime), imul(log_two, inverse_root_two)
    )
    h_value = iadd(imul(p_value, log_five_halves), p_derivative)

    assert p_value[1] < 0
    assert h_value[0] > Fraction(1, 1000)

    index_cases = 0
    for endpoint in range(100, 5001):
        lower = (2 * endpoint + 4) // 5
        upper = 4 * endpoint // 9
        for q in (lower, (lower + upper) // 2, upper):
            if q <= upper:
                assert first_odd_omitted(endpoint, q) == 1
                assert first_even_omitted(endpoint, q) == 2
                next_endpoint = (endpoint + 1) // 2
                assert q <= next_endpoint
                assert 2 * q > next_endpoint
                index_cases += 1

    result = {
        "schema": "X-30502-critical-cutoff-annulus-v1",
        "classification": "DIRECTED_CRITICAL_CUTOFF_ANNULUS_MARGIN_VERIFIED",
        "hasse_order": 30,
        "eta_interval_decimal": decimal_bounds(eta),
        "eta_prime_interval_decimal": decimal_bounds(eta_prime),
        "P_interval_decimal": decimal_bounds(p_value),
        "P_prime_interval_decimal": decimal_bounds(p_derivative),
        "H_5_over_2_interval_decimal": decimal_bounds(h_value),
        "proved_margin": "H(5/2)>1/1000",
        "first_index_geometry_cases": index_cases,
        "analytic_completion": [
            "uniform shifted-tail error <= 6/q",
            "unique divisor source has sigma(q)=Q_N(q) when 2q>M",
            "atomic norm is Omega(N) on q in [2N/5,4N/9]",
        ],
        "proof_boundary": (
            "directed constant and integer geometry only; the uniform-limit "
            "argument is in L-30503; cycle-optimized debt and RH are not proved"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, indent=2) + "\n"
    result["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(result, sort_keys=True, indent=2) + "\n"

    destination = Path(__file__).resolve().parent / "results" / "verification.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
