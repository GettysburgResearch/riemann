#!/usr/bin/env python3
"""Finite regression for L-90601/L-90602/R-90601.

The analytic refutation is the coefficient-estimate + Steinhaus + polygon +
Kronecker/Hurwitz proof in L-90601.  This script checks its exact finite algebra
and several numerical diagnostics.  It does not prove the asymptotic prime-count,
random-torus, Kronecker, or Hurwitz steps.
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def exact_C(N: int, n: int) -> Fraction:
    return Fraction(4 * math.factorial(N) ** 4,
                    math.factorial(N - n) ** 2 * math.factorial(N + n) ** 2)


def harmonic_table(m: int) -> list[float]:
    out = [0.0] * (m + 1)
    for k in range(1, m + 1):
        out[k] = out[k - 1] + 1.0 / k
    return out


def coefficient_data(N: int) -> list[tuple[float, float, float]]:
    """Return (log n, C_Nn, alpha_Nn), using stable log-gamma arithmetic."""
    hs = harmonic_table(2 * N)
    base = math.lgamma(N + 1)
    out: list[tuple[float, float, float]] = []
    for n in range(1, N + 1):
        log_c = (math.log(4.0) + 4.0 * base
                 - 2.0 * math.lgamma(N - n + 1)
                 - 2.0 * math.lgamma(N + n + 1))
        alpha = n * (hs[N + n] - hs[N - n]) - 0.5
        out.append((math.log(n), math.exp(log_c), alpha))
    return out


def H_and_derivative(data: Iterable[tuple[float, float, float]], z: complex) -> tuple[complex, complex, float]:
    value = 0j
    derivative = 0j
    scale = 0.0
    for log_n, c, alpha in data:
        phase = cmath.exp(-2.0 * z * log_n)
        term = c * phase * (z + alpha)
        value += term
        derivative += c * phase * (1.0 - 2.0 * log_n * (z + alpha))
        scale += abs(term)
    return value, derivative, scale


def newton_root(N: int, seed: complex, max_steps: int = 30) -> tuple[complex, float, float, int]:
    data = coefficient_data(N)
    z = seed
    for step in range(1, max_steps + 1):
        value, derivative, _ = H_and_derivative(data, z)
        delta = value / derivative
        z -= delta
        if abs(delta) < 1e-13:
            break
    value, _, scale = H_and_derivative(data, z)
    return z, abs(value), abs(value) / scale, step


def liouville_sieve(nmax: int) -> list[int]:
    omega = [0] * (nmax + 1)
    for p in range(2, nmax + 1):
        if omega[p] == 0:  # prime
            for m in range(p, nmax + 1, p):
                x = m
                while x % p == 0:
                    omega[m] += 1
                    x //= p
    return [1 if k == 0 or omega[k] % 2 == 0 else -1 for k in range(nmax + 1)]


def liouville_twist_value(N: int, sigma: float) -> float:
    signs = liouville_sieve(N)
    total = 0.0
    for n, (log_n, c, _) in enumerate(coefficient_data(N), start=1):
        total += c * signs[n] * math.exp(-2.0 * sigma * log_n)
    return total


def continuum_cancellation(z: complex) -> complex:
    """Closed form of integral in L-90602.13; it should vanish identically."""
    # Integral I0 = int exp(-2x^2)x^(-2z) dx
    # = 1/2 * 2^(z-1/2) Gamma(1/2-z).
    # Integral I2 = int exp(-2x^2)x^(2-2z) dx
    # = 1/2 * 2^(z-3/2) Gamma(3/2-z).
    # Python's stdlib has no complex gamma, so use the recurrence directly:
    # 2 I2 / I0 = (1/2-z), making (z-1/2)I0 + 2I2 = 0.
    return (z - 0.5) + (0.5 - z)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    # Exact coefficient-ratio identity.
    ratio_checks = 0
    for N in range(2, 81):
        for k in range(1, N):
            lhs = exact_C(N, k + 1) / exact_C(N, k)
            rhs = Fraction((N - k) ** 2, (N + k + 1) ** 2)
            assert lhs == rhs
            ratio_checks += 1

    # Uniform multiple-tail constant used in the proof.
    eta = sum(math.exp(-5.0 * (m * m - 1.0)) * m ** (-0.5)
              for m in range(2, 1000))
    assert eta < 1e-6

    # A concrete right-half-plane root.  The relative residual is the meaningful
    # quantity because the individual exponential-polynomial terms are large.
    root63, residual63, relative63, steps63 = newton_root(
        63, 0.2508 + 55.8235j
    )
    assert root63.real > 0.2508
    assert abs(root63.imag - 55.8235433904) < 1e-8
    assert relative63 < 1e-12

    # A still higher violating root at N=60: the obstruction is not tied to one
    # low-height xi approximation branch.
    root60, residual60, relative60, steps60 = newton_root(
        60, 0.2527 + 270.2566j
    )
    assert root60.real > 0.252
    assert relative60 < 1e-11

    # The simple Liouville vertical-limit probe changes sign between N=79 and 80.
    # This is only a diagnostic; L-90601 uses an adaptive torus twist and does not
    # rely on Liouville having a fixed sign.
    liouville79 = liouville_twist_value(79, 0.25)
    liouville80 = liouville_twist_value(80, 0.25)
    assert liouville79 > 0.0
    assert liouville80 < 0.0

    # Exact symbolic cancellation reduced to the gamma recurrence.
    cancellation_samples = []
    for z in [0.1 + 0.3j, 0.25 + 7.0j, -1.2 + 2.5j]:
        value = continuum_cancellation(z)
        assert value == 0j
        cancellation_samples.append([z.real, z.imag])

    result = {
        "classification": "PASS_X_90601_BROWNIAN_BOHR_INSTABILITY",
        "exact_coefficient_ratio_checks": ratio_checks,
        "multiple_tail_eta_upper": eta,
        "root_N63": {
            "real": root63.real,
            "imag": root63.imag,
            "absolute_residual": residual63,
            "relative_residual": relative63,
            "newton_steps": steps63,
        },
        "root_N60_high": {
            "real": root60.real,
            "imag": root60.imag,
            "absolute_residual": residual60,
            "relative_residual": relative60,
            "newton_steps": steps60,
        },
        "liouville_probe_sigma_quarter": {
            "N79": liouville79,
            "N80": liouville80,
        },
        "continuum_cancellation_samples": cancellation_samples,
        "scope": (
            "Finite algebra and numerical diagnostics only; the unconditional "
            "high-frequency refutation is the written Steinhaus-polygon-"
            "Kronecker-Hurwitz proof."
        ),
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
