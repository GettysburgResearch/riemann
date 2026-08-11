#!/usr/bin/env python3
"""Finite regression for the terminal Gaussian heat-residue normal form.

This checker verifies only closed algebraic/numerical identities.  It does not
prove a contour shift for zeta, the terminal-pair theorem, the arithmetic
corrected-kernel floor, or RH.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path
from typing import Callable, Dict, List


def simpson(f: Callable[[float], complex], a: float, b: float, n: int) -> complex:
    if n <= 0 or n % 2:
        raise ValueError("Simpson n must be a positive even integer")
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(a + j * h)
    return total * h / 3


def von_mangoldt(limit: int) -> List[float]:
    if limit < 2:
        return [0.0] * (limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    lam = [0.0] * (limit + 1)
    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue
        lp = math.log(p)
        q = p
        while q <= limit:
            lam[q] = lp
            if q > limit // p:
                break
            q *= p
    return lam


def H(sigma: float, y: float, t: float) -> float:
    tau = sigma * sigma
    return (
        math.exp(-(t * t) / (4 * tau))
        - 0.5 * math.exp(-((t - 2 * tau * y) ** 2) / (4 * tau))
        - 0.5 * math.exp(-((t + 2 * tau * y) ** 2) / (4 * tau))
    )


def H_factored(sigma: float, y: float, t: float) -> float:
    tau = sigma * sigma
    return math.exp(-(t * t) / (4 * tau)) * (
        1.0 - math.exp(-tau * y * y) * math.cosh(y * t)
    )


def Acoef(sigma: float, y: float) -> float:
    a = sigma * sigma * y * y
    return math.exp(a) / (
        math.sqrt(math.pi) * sigma * (math.exp(2 * a) - 1.0) ** 2
    )


def parabolic_kernel(sigma: float, y: float, z: complex) -> complex:
    tau = sigma * sigma
    return cmath.exp(tau * z * z) * (
        1.0 - cmath.cosh(2.0 * tau * y * z)
    )


def parabolic_kernel_difference(sigma: float, y: float, z: complex) -> complex:
    tau = sigma * sigma
    a = tau * y * y
    return (
        cmath.exp(tau * z * z)
        - 0.5
        * math.exp(-a)
        * (
            cmath.exp(tau * (z + y) ** 2)
            + cmath.exp(tau * (z - y) ** 2)
        )
    )


def kernel_real_closed(sigma: float, y: float, d: float, r: float) -> float:
    tau = sigma * sigma
    theta = 2.0 * tau * d * r
    alpha = 2.0 * tau * y * d
    beta = 2.0 * tau * y * r
    return math.exp(tau * (d * d - r * r)) * (
        math.cos(theta) * (1.0 - math.cosh(alpha) * math.cos(beta))
        + math.sin(theta) * math.sinh(alpha) * math.sin(beta)
    )


def direct_prime_continuum(
    sigma: float,
    x: float,
    y: float,
    lam: List[float],
    t_max: float,
    integral_steps: int,
) -> float:
    limit = len(lam) - 1
    prime = 0.0
    for n in range(2, limit + 1):
        if lam[n] == 0.0:
            continue
        t = math.log(n)
        prime += lam[n] * math.exp(-0.5 * t) * H(sigma, y, t) * math.cos(x * t)

    def integrand(t: float) -> float:
        return math.exp(0.5 * t) * H(sigma, y, t) * math.cos(x * t)

    continuum = float(simpson(integrand, 0.0, t_max, integral_steps).real)
    return prime - continuum


def D_sigma(
    sigma: float,
    s: complex,
    lam: List[float],
    t_max: float,
    integral_steps: int,
) -> complex:
    tau = sigma * sigma
    limit = len(lam) - 1
    prime = 0.0j
    for n in range(2, limit + 1):
        if lam[n] == 0.0:
            continue
        t = math.log(n)
        prime += lam[n] * cmath.exp(-s * t - t * t / (4 * tau))

    def integrand(t: float) -> complex:
        return cmath.exp((1.0 - s) * t - t * t / (4 * tau))

    continuum = simpson(integrand, 0.0, t_max, integral_steps)
    return prime - continuum


def integer_tail_envelope(sigma: float, y: float, P: int, cap: int) -> Dict[str, float]:
    """Finite control of the all-integer envelope; not an infinite proof."""
    if P < 2 or cap <= P:
        raise ValueError("require 2 <= P < cap")
    actual = 0.0
    envelope = 0.0
    for n in range(P + 1, cap + 1):
        t = math.log(n)
        actual += math.log(n) * n ** (-0.5) * abs(H(sigma, y, t))
        tau = sigma * sigma
        env = (
            math.exp(-t * t / (4 * tau))
            + 0.5 * math.exp(-((t - 2 * tau * y) ** 2) / (4 * tau))
            + 0.5 * math.exp(-((t + 2 * tau * y) ** 2) / (4 * tau))
        )
        envelope += math.log(n) * n ** (-0.5) * env
    return {"actual": actual, "envelope": envelope}


def run() -> Dict[str, object]:
    sigma = 1.25
    x = 3.7
    y = 0.23
    tau = sigma * sigma
    a = tau * y * y

    kernel_errors = []
    samples = [
        complex(0.0, 0.0),
        complex(y, 0.0),
        complex(0.17, -0.31),
        complex(0.41, 0.22),
        complex(-0.2, 0.63),
    ]
    for z in samples:
        kernel_errors.append(
            abs(
                parabolic_kernel(sigma, y, z)
                - parabolic_kernel_difference(sigma, y, z)
            )
        )

    target_K = parabolic_kernel(sigma, y, complex(y, 0.0)).real
    target_contribution = 4.0 * Acoef(sigma, y) * math.sqrt(math.pi) * sigma * target_K

    real_formula_errors = []
    threat_rows = []
    for d, r in [(0.11, 0.07), (0.31, -0.19), (0.44, 0.53), (y, 0.0)]:
        exact = parabolic_kernel(sigma, y, complex(d, r)).real
        closed = kernel_real_closed(sigma, y, d, r)
        real_formula_errors.append(abs(exact - closed))
        phi_a = d * d - r * r + 2 * y * d - 3 * y * y
        phi_b = (d - y) * (d + 3 * y) - r * r
        threat_rows.append(
            {
                "d": d,
                "r": r,
                "expanded": phi_a,
                "factored": phi_b,
                "error": abs(phi_a - phi_b),
            }
        )

    H_errors = [
        abs(H(sigma, y, t) - H_factored(sigma, y, t))
        for t in [0.0, 0.4, 1.7, 3.2, 7.0]
    ]

    t_max = 12.0
    prime_limit = int(math.exp(t_max))
    lam = von_mangoldt(prime_limit)
    steps = 48000
    s0 = complex(0.5, x)
    D0 = D_sigma(sigma, s0, lam, t_max, steps)
    Dm = D_sigma(sigma, s0 - y, lam, t_max, steps)
    Dp = D_sigma(sigma, s0 + y, lam, t_max, steps)
    delta_D = D0 - 0.5 * math.exp(-a) * (Dm + Dp)
    direct = direct_prime_continuum(sigma, x, y, lam, t_max, steps)
    three_point_error = abs(delta_D.real - direct)

    scalar_from_D = -2.0 * Acoef(sigma, y) * delta_D.real
    scalar_direct = -2.0 * Acoef(sigma, y) * direct

    tail = integer_tail_envelope(sigma, y, 5000, 50000)

    gates = {
        "kernel_finite_difference": max(kernel_errors) < 2e-13,
        "target_residue_minus_two": abs(target_contribution + 2.0) < 2e-13,
        "real_part_formula": max(real_formula_errors) < 2e-13,
        "threat_exponent_identity": max(row["error"] for row in threat_rows) < 2e-15,
        "three_gaussian_factorization": max(H_errors) < 2e-13,
        "prime_continuum_three_point": three_point_error < 5e-8,
        "tail_envelope": tail["actual"] <= tail["envelope"] + 1e-12,
    }

    if not all(gates.values()):
        failed = [name for name, ok in gates.items() if not ok]
        raise AssertionError("failed gates: " + ", ".join(failed))

    return {
        "status": "PASS_TERMINAL_GAUSSIAN_HEAT_RESIDUE",
        "parameters": {
            "sigma": sigma,
            "x": x,
            "y": y,
            "a": a,
            "t_max": t_max,
            "prime_limit": prime_limit,
            "integral_steps": steps,
        },
        "gates": gates,
        "kernel_identity": {
            "max_error": max(kernel_errors),
            "sample_errors": kernel_errors,
        },
        "target_residue": {
            "kernel_at_target": target_K,
            "normalized_contribution": target_contribution,
            "error_from_minus_two": abs(target_contribution + 2.0),
        },
        "real_part_formula": {
            "max_error": max(real_formula_errors),
            "sample_errors": real_formula_errors,
        },
        "threat_exponent": threat_rows,
        "three_gaussian_factorization": {
            "max_error": max(H_errors),
            "sample_errors": H_errors,
        },
        "prime_continuum": {
            "delta_D_real": delta_D.real,
            "direct_value": direct,
            "absolute_error": three_point_error,
            "scalar_from_D": scalar_from_D,
            "scalar_direct": scalar_direct,
        },
        "finite_tail_control": tail,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
