#!/usr/bin/env python3
"""Numerical regression for L-91404."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70


def prime_powers(limit: int) -> list[tuple[int, int, int]]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = ((limit - p * p) // p) + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    out: list[tuple[int, int, int]] = []
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        n, k = p, 1
        while n <= limit:
            out.append((n, k, p))
            n *= p
            k += 1
    return sorted(out)


def xi(s: mp.mpc | mp.mpf) -> mp.mpc:
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_log_derivative(s: mp.mpc | mp.mpf) -> mp.mpc:
    return mp.diff(lambda z: mp.log(xi(z)), s)


def nakamura_lambda(sigma: mp.mpf) -> mp.mpf:
    first = (mp.e ** (-sigma / 2) - 1) / sigma
    second = (mp.e ** ((1 - sigma) / 2) - 1) / (sigma - 1)

    def stable_integrand(x: mp.mpf) -> mp.mpf:
        if x == 0:
            return (3 - sigma) / 2
        denominator = -mp.expm1(-x)
        numerator = x * mp.e ** (-sigma * x / 2) - mp.e ** (-x) * denominator
        return numerator / (x * denominator)

    integral = mp.quad(stable_integrand, [0, 1])
    return (
        first
        + second
        + mp.log(mp.pi) / 2
        + integral / 2
        - mp.e1(1) / 2
    )


def quasi_density(sigma: mp.mpf, u: mp.mpf) -> mp.mpf:
    y = mp.e**u
    return mp.e ** (-sigma * u) / u * (1 + y - y**3) / (y**2 - 1)


def carrier_compensation(x: mp.mpf, u: mp.mpf) -> mp.mpf:
    return mp.cos(x * u) - (1 if u <= mp.mpf("0.5") else 0)


def continuous_moment(
    sigma: mp.mpf,
    x: mp.mpf,
    power: int,
    plastic_log: mp.mpf,
) -> mp.mpf:
    return mp.quad(
        lambda u: u**power * carrier_compensation(x, u) * quasi_density(sigma, u),
        [0, plastic_log, mp.mpf("0.5"), 1, mp.inf],
    )


def atomic_moment(
    sigma: mp.mpf,
    x: mp.mpf,
    power: int,
    rows: list[tuple[int, int, int]],
) -> mp.mpf:
    return mp.fsum(
        mp.log(n) ** power
        * carrier_compensation(x, mp.log(n))
        * mp.power(n, -sigma)
        / k
        for n, k, _p in rows
    )


def cauchy_n_direct(c: mp.mpf, x: mp.mpf) -> mp.mpf:
    def p(scale: mp.mpf) -> mp.mpf:
        return mp.re(xi_log_derivative(mp.mpf("0.5") + scale + 1j * x))

    return (c * p(c) - c * c * mp.diff(p, c)) / 2


def cauchy_n_source(
    c: mp.mpf,
    x: mp.mpf,
    plastic_log: mp.mpf,
    rows: list[tuple[int, int, int]],
) -> mp.mpf:
    sigma = mp.mpf("0.5") + c
    lambda_value = nakamura_lambda(sigma)
    lambda_prime = mp.diff(nakamura_lambda, sigma)
    source_integral = (
        continuous_moment(sigma, x, 1, plastic_log)
        + c * continuous_moment(sigma, x, 2, plastic_log)
        + atomic_moment(sigma, x, 1, rows)
        + c * atomic_moment(sigma, x, 2, rows)
    )
    return -c * (lambda_value - c * lambda_prime) / 2 - c * source_integral / 2


def normalized_gate(c: mp.mpf, x: mp.mpf) -> mp.mpf:
    return c ** (-4) * (cauchy_n_direct(2 * c, x) - cauchy_n_direct(c, x))


def recurrence_direct(a: mp.mpf, x: mp.mpf) -> mp.mpf:
    return normalized_gate(a, x) - normalized_gate(2 * a, x)


def recurrence_source(
    a: mp.mpf,
    x: mp.mpf,
    plastic_log: mp.mpf,
    rows: list[tuple[int, int, int]],
) -> mp.mpf:
    alpha = {1: mp.mpf(-1), 2: mp.mpf(17) / 16, 4: -mp.mpf(1) / 16}
    return a ** (-4) * mp.fsum(
        alpha[r] * cauchy_n_source(r * a, x, plastic_log, rows)
        for r in (1, 2, 4)
    )


def physical_residual(a: mp.mpf, t: mp.mpf) -> mp.mpf:
    return a * (
        -mp.mpf(1) / 4 * (1 + a * t) * mp.e ** (-a * t)
        + mp.mpf(17) / 32 * (1 + 2 * a * t) * mp.e ** (-2 * a * t)
        - mp.mpf(1) / 16 * (1 + 4 * a * t) * mp.e ** (-4 * a * t)
    )


def prime_source_recurrence(
    a: mp.mpf,
    x: mp.mpf,
    rows: list[tuple[int, int, int]],
) -> mp.mpf:
    kappa = {
        1: mp.mpf(1) / (2 * a**3),
        2: -mp.mpf(17) / (16 * a**3),
        4: mp.mpf(1) / (8 * a**3),
    }
    total = mp.mpf("0")
    for r in (1, 2, 4):
        sigma = mp.mpf("0.5") + r * a
        total += kappa[r] * (
            atomic_moment(sigma, x, 1, rows)
            + r * a * atomic_moment(sigma, x, 2, rows)
        )
    return total


def prime_physical_recurrence(
    a: mp.mpf,
    x: mp.mpf,
    rows: list[tuple[int, int, int]],
) -> mp.mpf:
    return -2 * a ** (-4) * mp.fsum(
        mp.log(p)
        * mp.power(n, -mp.mpf("0.5"))
        * physical_residual(a, mp.log(n))
        * mp.cos(x * mp.log(n))
        for n, _k, p in rows
    )


def build() -> dict[str, object]:
    a = mp.mpf("4")
    x = mp.mpf("0.83")
    cutoff = 50_000
    rows = prime_powers(cutoff)
    plastic = mp.findroot(lambda y: y**3 - y - 1, mp.mpf("1.3"))
    plastic_log = mp.log(plastic)

    direct = recurrence_direct(a, x)
    source = recurrence_source(a, x, plastic_log, rows)
    recurrence_error = abs(source - direct)

    scale_errors = {
        str(r): float(
            abs(
                cauchy_n_source(r * a, x, plastic_log, rows)
                - cauchy_n_direct(r * a, x)
            )
        )
        for r in (1, 2, 4)
    }

    prime_source = prime_source_recurrence(a, x, rows)
    prime_physical = prime_physical_recurrence(a, x, rows)
    prime_error = abs(prime_source - prime_physical)

    theta_derivative_error = abs(
        mp.diff(
            lambda carrier: mp.log(
                xi(mp.mpf("0.5") + a + 1j * carrier)
                / xi(mp.mpf("0.5") + a - 1j * carrier)
            ),
            x,
        )
        - 2j * mp.re(xi_log_derivative(mp.mpf("0.5") + a + 1j * x))
    )

    gates = {
        "phase_differential": theta_derivative_error < mp.mpf("1e-55"),
        "three_scale_source": recurrence_error < mp.mpf("1e-15"),
        "prime_residual": prime_error < mp.mpf("1e-60"),
    }
    assert all(gates.values())

    return {
        "status": "PASS_THREE_SCALE_CAUCHY_QUASI_LEVY_SOURCE",
        "gates": gates,
        "a": float(a),
        "carrier": float(x),
        "prime_power_cutoff": cutoff,
        "plastic_log_boundary": float(plastic_log),
        "direct_recurrence": float(direct),
        "source_recurrence": float(source),
        "three_scale_source_error": float(recurrence_error),
        "scale_N_errors": scale_errors,
        "prime_source_recurrence": float(prime_source),
        "prime_physical_recurrence": float(prime_physical),
        "prime_residual_error": float(prime_error),
        "phase_differential_error": float(theta_derivative_error),
        "alpha": {"1": -1.0, "2": 17.0 / 16.0, "4": -1.0 / 16.0},
        "kappa": {
            "1": float(mp.mpf(1) / (2 * a**3)),
            "2": float(-mp.mpf(17) / (16 * a**3)),
            "4": float(mp.mpf(1) / (8 * a**3)),
        },
        "positive_sectors": ["r1:nu+", "r2:nu-", "r4:nu+"],
        "negative_sectors": ["r1:nu-", "r2:nu+", "r4:nu-"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.json:
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
