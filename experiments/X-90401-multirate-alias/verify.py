#!/usr/bin/env python3
"""Finite diagnostics for L-90401/L-90402/L-90403.

This standard-library script checks numerical instances of:
  * arbitrary no-alias multirate Poisson collapse;
  * the exact alias/polyphase kernel expansion;
  * period-averaged trace and Frobenius identities;
  * prime-power phase locking;
  * the scalar Montgomery--Taylor optimizer.

It is a diagnostic only, not a proof of the analytic theorems.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path
from typing import Callable


def trapz_complex(f: Callable[[float], complex], a: float, b: float, n: int) -> complex:
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def phi(u: float, half_support: float = 1.0) -> float:
    """C^1 compact bump with support [-half_support, half_support]."""
    if abs(u) >= half_support:
        return 0.0
    x = u / half_support
    return (1.0 - x * x) ** 2


def base_hat(z: complex) -> complex:
    """Transform of (1-x^2)^2 1_|x|<1, with a stable Taylor branch."""
    if abs(z) < 0.25:
        total = 0j
        z2 = z * z
        power = 1 + 0j
        fact = 1.0
        sign = 1.0
        for m in range(9):
            if m > 0:
                power *= z2
                fact *= (2 * m - 1) * (2 * m)
                sign *= -1.0
            moment = 2.0 * (
                1.0 / (2 * m + 1)
                - 2.0 / (2 * m + 3)
                + 1.0 / (2 * m + 5)
            )
            total += sign * power * moment / fact
        return total
    return 16.0 * ((3.0 - z * z) * cmath.sin(z) - 3.0 * z * cmath.cos(z)) / (z**5)


def hat_phi(z: complex, half_support: float = 1.0) -> complex:
    return half_support * base_hat(half_support * z)


def hat_abs2(x: float, half_support: float = 1.0, n: int = 5000) -> complex:
    return trapz_complex(
        lambda u: phi(u, half_support) ** 2 * cmath.exp(1j * x * u),
        -half_support,
        half_support,
        n,
    )


def c_hat(r: int, P: float, x: float, half_support: float = 1.0, n: int = 5000) -> complex:
    return trapz_complex(
        lambda u: phi(u, half_support)
        * phi(u - r * P, half_support)
        * cmath.exp(1j * x * u),
        -half_support,
        half_support,
        n,
    )


def lattice_kernel(
    tau: float,
    tau_prime: float,
    offset: float,
    h: float,
    half_support: float,
    kmax: int = 120,
) -> complex:
    total = 0j
    for k in range(-kmax, kmax + 1):
        center = offset + k * h
        total += hat_phi(tau - center, half_support) * hat_phi(
            tau_prime - center, half_support
        ).conjugate()
    return total


def alias_coefficients(P: float, x: float, half_support: float) -> dict[int, complex]:
    rmax = int(math.ceil(2 * half_support / P)) + 1
    return {r: c_hat(r, P, x, half_support) for r in range(-rmax, rmax + 1)}


def alias_formula_from_coeffs(
    tau: float,
    tau_prime: float,
    offset: float,
    P: float,
    coeffs: dict[int, complex],
) -> complex:
    return P * sum(
        cmath.exp(1j * (tau_prime - offset) * r * P) * coeff
        for r, coeff in coeffs.items()
    )


def average_over_period(
    f: Callable[[float], complex], a: float, h: float, n: int = 2000
) -> complex:
    return trapz_complex(f, a, a + h, n) / h


def scalar_functional(v: Callable[[float], float], lam: float, n: int = 500) -> float:
    a, b = -0.5, 0.5
    h = (b - a) / n
    xs = [a + i * h for i in range(n + 1)]
    ws = [0.5 if i in (0, n) else 1.0 for i in range(n + 1)]
    vals = [v(x) for x in xs]
    int_v = h * sum(w * y for w, y in zip(ws, vals))
    int_v2 = h * sum(w * y * y for w, y in zip(ws, vals))
    double = 0.0
    for i, x in enumerate(xs):
        inner = sum(ws[j] * abs(x - y) * vals[j] for j, y in enumerate(xs))
        double += ws[i] * vals[i] * h * inner
    double *= h
    return lam * int_v * int_v / (int_v2 + lam * lam * double)


def main() -> None:
    out: dict[str, object] = {
        "classification": "FINITE_NUMERICAL_DIAGNOSTIC_NOT_ANALYTIC_PROOF",
        "proof_boundary": (
            "The replay samples Poisson/alias identities and constants numerically. "
            "It does not prove the distributional Poisson formula, trace asymptotics, "
            "Montgomery--Vaughan estimates, or any statement about RH."
        ),
    }

    # 1. Two incommensurable no-alias lattices. Support length is L=2.
    half = 1.0
    L = 2.0
    families = [
        {"P": 2.37, "offset": 0.173, "weight": 1.0},
        {"P": math.sqrt(7.0), "offset": -0.291, "weight": 0.71},
    ]
    tau, tau_prime = 0.61, -0.47
    lhs = 0j
    rhs = 0j
    for fam in families:
        P = float(fam["P"])
        h = 2 * math.pi / P
        weight = float(fam["weight"])
        lhs += weight * lattice_kernel(
            tau, tau_prime, float(fam["offset"]), h, half
        )
        rhs += weight * P * hat_abs2(tau - tau_prime, half)
    no_alias_error = abs(lhs - rhs)
    out["no_alias_multirate"] = {
        "support_length": L,
        "dual_periods": [fam["P"] for fam in families],
        "absolute_error": no_alias_error,
        "pass": no_alias_error < 2.0e-9,
    }

    # 2. Aliased lattice: P<L, so r=+-1 overlaps.
    P = 1.25
    h = 2 * math.pi / P
    offset = 0.211
    tau, tau_prime = 0.41, -0.36
    coeffs = alias_coefficients(P, tau - tau_prime, half)
    direct = lattice_kernel(tau, tau_prime, offset, h, half, kmax=140)
    expanded = alias_formula_from_coeffs(tau, tau_prime, offset, P, coeffs)
    alias_error = abs(direct - expanded)

    x = 0.37
    coeffs_x = alias_coefficients(P, x, half)
    coeffs_zero = alias_coefficients(P, 0.0, half)
    mean_diag = average_over_period(
        lambda t: alias_formula_from_coeffs(t, t, offset, P, coeffs_zero),
        offset,
        h,
    )
    predicted_diag = P * coeffs_zero[0]
    mean_square = average_over_period(
        lambda t: abs(
            alias_formula_from_coeffs(t + x, t, offset, P, coeffs_x)
        )
        ** 2,
        offset,
        h,
    ).real
    predicted_square = P * P * sum(abs(value) ** 2 for value in coeffs_x.values())
    scalar_square = P * P * abs(coeffs_x[0]) ** 2
    out["alias_polyphase"] = {
        "dual_period": P,
        "support_length": L,
        "kernel_absolute_error": alias_error,
        "period_mean_diag_error": abs(mean_diag - predicted_diag),
        "period_mean_square_error": abs(mean_square - predicted_square),
        "alias_tax": predicted_square - scalar_square,
        "pass": (
            alias_error < 2.0e-8
            and abs(mean_diag - predicted_diag) < 2.0e-9
            and abs(mean_square - predicted_square) < 3.0e-9
            and predicted_square >= scalar_square - 1.0e-12
        ),
    }

    # 3. Exact phase locking: P=log p, r-th alias mode matches log(p^r).
    prime = 5
    Pp = math.log(prime)
    resonance = []
    for r in range(1, 6):
        n = prime**r
        resonance.append(
            {
                "r": r,
                "n": n,
                "alias_frequency": r * Pp,
                "prime_power_frequency": math.log(n),
                "absolute_error": abs(r * Pp - math.log(n)),
            }
        )
    out["prime_power_resonance"] = {
        "prime": prime,
        "rows": resonance,
        "pass": max(row["absolute_error"] for row in resonance) < 2.0e-15,
    }

    # 4. Scalar optimizer check.
    lam = 1.0
    c_star = math.sqrt(2.0) * math.tan(lam / math.sqrt(2.0)) / (
        1.0 + (lam / math.sqrt(2.0)) * math.tan(lam / math.sqrt(2.0))
    )
    candidates = {
        "optimal_cosine": lambda s: math.cos(math.sqrt(2.0) * lam * s),
        "flat": lambda s: 1.0,
        "quadratic": lambda s: 1.0 - 0.35 * (2.0 * s) ** 2,
        "quartic": lambda s: 1.0
        - 0.15 * (2.0 * s) ** 2
        - 0.08 * (2.0 * s) ** 4,
    }
    vals = {name: scalar_functional(v, lam) for name, v in candidates.items()}
    out["scalar_optimizer"] = {
        "closed_form": c_star,
        "quadrature": vals,
        "optimal_error": abs(vals["optimal_cosine"] - c_star),
        "pass": abs(vals["optimal_cosine"] - c_star) < 3.0e-6
        and all(vals[name] <= c_star + 3.0e-6 for name in vals),
    }

    out["verdict"] = (
        "PASS_X_90401_MULTIRATE_ALIAS"
        if all(
            bool(out[key]["pass"])
            for key in (
                "no_alias_multirate",
                "alias_polyphase",
                "prime_power_resonance",
                "scalar_optimizer",
            )
        )
        else "FAIL_X_90401_MULTIRATE_ALIAS"
    )

    path = Path(__file__).resolve().parent / "results" / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(out["verdict"])
    print(path)


if __name__ == "__main__":
    main()
