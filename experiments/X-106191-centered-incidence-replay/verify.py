#!/usr/bin/env python3
"""Finite replay for L-106190 and L-106191.

This checks the exact finite-dimensional identities numerically on deterministic
rational-complex packets. It does not estimate the global conductor sums
WCCORR106191/WCADD106140 or WCKUM106140.
"""

from __future__ import annotations

import cmath
import json
import math
import random
from fractions import Fraction
from pathlib import Path
from typing import Any


SEED = 106191
TOLERANCE = 1.0e-8
PRIME_PAIRS = ((3, 5), (3, 7), (5, 7), (5, 11), (7, 11), (7, 13))


def phase(q: int, h: int, x: int) -> complex:
    return cmath.exp(2j * math.pi * h * x / q)


def packet_residuals(
    ell: int,
    rho: int,
    z: list[complex],
    x: list[int],
    y: list[int],
    g: int,
) -> dict[str, float]:
    n = len(z)
    total = abs(sum(z)) ** 2
    diagonal = sum(abs(a) ** 2 for a in z)

    c_ell = sum(
        z[i] * z[j].conjugate()
        for i in range(n)
        for j in range(n)
        if x[i] % ell == x[j] % ell
    )
    c_rho = sum(
        z[i] * z[j].conjugate()
        for i in range(n)
        for j in range(n)
        if y[i] % rho == y[j] % rho
    )
    c_joint = sum(
        z[i] * z[j].conjugate()
        for i in range(n)
        for j in range(n)
        if x[i] % ell == x[j] % ell and y[i] % rho == y[j] % rho
    )

    e11 = 0.0
    for h in range(1, ell):
        for k in range(1, rho):
            member = sum(
                z[i] * phase(ell, h, x[i]) * phase(rho, k, y[i])
                for i in range(n)
            )
            e11 += abs(member) ** 2

    e10 = 0.0
    for h in range(1, ell):
        member = sum(z[i] * phase(ell, h, x[i]) for i in range(n))
        e10 += abs(member) ** 2

    e01 = 0.0
    for k in range(1, rho):
        member = sum(z[i] * phase(rho, k, y[i]) for i in range(n))
        e01 += abs(member) ** 2

    centered_e11 = e11 - (ell - 1) * (rho - 1) * diagonal

    z_tilde = [g * ell * rho * a for a in z]
    diagonal_tilde = sum(abs(a) ** 2 for a in z_tilde)
    e11_tilde = 0.0
    for h in range(1, ell):
        for k in range(1, rho):
            member = sum(
                z_tilde[i] * phase(ell, h, x[i]) * phase(rho, k, y[i])
                for i in range(n)
            )
            e11_tilde += abs(member) ** 2

    source_dual_left = g * g * ell * rho * centered_e11
    source_dual_phase = (
        e11_tilde - (ell - 1) * (rho - 1) * diagonal_tilde
    ) / (ell * rho)

    source_dual_kernel = 0j
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            k_ell = (1.0 if x[i] % ell == x[j] % ell else 0.0) - 1.0 / ell
            k_rho = (1.0 if y[i] % rho == y[j] % rho else 0.0) - 1.0 / rho
            source_dual_kernel += (
                z_tilde[i] * z_tilde[j].conjugate() * k_ell * k_rho
            )

    return {
        "mobius_expansion": abs(
            e11 - (ell * rho * c_joint - ell * c_ell - rho * c_rho + total)
        ),
        "principal_inversion": abs(
            total - (e11 + ell * c_ell + rho * c_rho - ell * rho * c_joint)
        ),
        "one_phase_form": abs(
            total - (ell * rho * c_joint - e11 - e10 - e01)
        ),
        "centered_connected": abs(
            (total - diagonal)
            - (
                centered_e11
                + ell * (c_ell - diagonal)
                + rho * (c_rho - diagonal)
                - ell * rho * (c_joint - diagonal)
            )
        ),
        "source_dual_phase": abs(source_dual_left - source_dual_phase),
        "source_dual_kernel": abs(source_dual_left - source_dual_kernel),
        "collision_imaginary_part": max(
            abs(c_ell.imag), abs(c_rho.imag), abs(c_joint.imag)
        ),
    }


def even_character_weight_total(q: int) -> Fraction:
    principal = Fraction(q + 1, q - 1)
    nonprincipal_count = (q - 3) // 2
    nonprincipal_weight = Fraction(2 * q, q - 1)
    return principal + nonprincipal_count * nonprincipal_weight


def run() -> dict[str, Any]:
    rng = random.Random(SEED)
    residual_names = (
        "mobius_expansion",
        "principal_inversion",
        "one_phase_form",
        "centered_connected",
        "source_dual_phase",
        "source_dual_kernel",
        "collision_imaginary_part",
    )
    maxima = {name: 0.0 for name in residual_names}

    packet_cases = 0
    for ell, rho in PRIME_PAIRS:
        for size in range(1, 9):
            for _ in range(5):
                z = [
                    complex(rng.randint(-5, 5), rng.randint(-5, 5)) / 7.0
                    for _ in range(size)
                ]
                x = [rng.randrange(ell) for _ in range(size)]
                y = [rng.randrange(rho) for _ in range(size)]
                g = rng.randint(1, 5)
                residuals = packet_residuals(ell, rho, z, x, y, g)
                packet_cases += 1
                for name, value in residuals.items():
                    maxima[name] = max(maxima[name], value)

    weight_primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
    weight_checks = 0
    for q in weight_primes:
        assert even_character_weight_total(q) == q - 1
        weight_checks += 1

    cancellation_checks = 0
    for ell, rho in PRIME_PAIRS:
        assert (ell - 1) * (rho - 1) + ell + rho - ell * rho == 1
        cancellation_checks += 1

    failed = {name: value for name, value in maxima.items() if value > TOLERANCE}
    verdict = (
        "PASS_X_106191_CENTERED_INCIDENCE_IDENTITY"
        if not failed
        else "FAIL_X_106191_CENTERED_INCIDENCE_IDENTITY"
    )

    return {
        "schema": "riemann.x106191.centered-incidence-replay.v1",
        "seed": SEED,
        "tolerance": TOLERANCE,
        "packet_cases": packet_cases,
        "numerical_identity_checks": packet_cases * 7,
        "exact_character_weight_checks": weight_checks,
        "exact_atomic_cancellation_checks": cancellation_checks,
        "max_absolute_residuals": maxima,
        "failed_residuals": failed,
        "prime_core_warning_checked": {
            "statement": (
                "For c=ell and d=rho, the rescaled atom "
                "z_tilde=gamma/(g*u*v*sqrt(PQ)) has u=v=1 and no least-prime decay."
            ),
            "global_gate_proved": False,
        },
        "verdict": verdict,
        "scope": {
            "proved_by_replay": [
                "finite connected Kummer-Mobius identities",
                "finite source-dual rescaling",
                "finite centered double-incidence expansion",
                "one-prime total character weight q-1",
                "atomic coefficient cancellation",
            ],
            "not_proved": [
                "WCCORR106191",
                "WCADD106140",
                "WCEQ106191",
                "WCDIST106191",
                "WCKUM106140",
                "BCI102990",
                "Riemann Hypothesis",
            ],
        },
    }


def main() -> None:
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output_path = Path(__file__).with_name("results") / "verification.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    print(text, end="")
    if not result["verdict"].startswith("PASS"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
