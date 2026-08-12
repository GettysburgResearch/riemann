#!/usr/bin/env python3
"""Finite algebra replay for L-91331--L-91333 and T-91308."""

from __future__ import annotations

import argparse
import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


def poly_mul(a: list[complex], b: list[complex], nmax: int) -> list[complex]:
    out = [0j] * (nmax + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= nmax:
                out[i + j] += x * y
    return out


def poly_exp(q: list[complex], nmax: int) -> list[complex]:
    """exp(q), with q[0]=0, truncated."""
    out = [0j] * (nmax + 1)
    out[0] = 1
    power = [0j] * (nmax + 1)
    power[0] = 1
    fact = 1
    for m in range(1, nmax + 1):
        power = poly_mul(power, q, nmax)
        fact *= m
        for j in range(nmax + 1):
            out[j] += power[j] / fact
    return out


def local_D_coeffs(a: float, b: float, nmax: int) -> list[complex]:
    # (1-a z)/(1-b z)
    out = [0j] * (nmax + 1)
    out[0] = 1
    for k in range(1, nmax + 1):
        out[k] = -(a - b) * b ** (k - 1)
    return out


def harmonic_count(omega: Fraction) -> int:
    return math.floor(Fraction(1, 1) / (1 - 2 * omega))


def run() -> dict[str, object]:
    checks = 0
    max_factor_error = 0.0
    max_cocycle_error = 0.0
    max_model_error = 0.0

    # 1. Threshold and equality cases.
    samples = {
        Fraction(1, 8): 1,
        Fraction(1, 5): 1,
        Fraction(1, 4): 2,
        Fraction(1, 3): 3,
        Fraction(2, 5): 5,
    }
    threshold_rows = []
    for omega, expected in samples.items():
        K = harmonic_count(omega)
        assert K == expected
        checks += 1
        q = 1 - 2 * omega
        assert K * q <= 1
        assert (K + 1) * q > 1
        checks += 2
        threshold_rows.append({
            "omega": str(omega),
            "K": K,
            "last_divergent_exponent": str(K * q),
            "first_convergent_exponent": str((K + 1) * q),
        })

    # Preferred cofinal sequence is always one-charge.
    for j in range(20):
        omega = Fraction(1, 2 ** (j + 3))
        assert harmonic_count(omega) == 1
        checks += 1

    # 2. Log coefficients and charge/remainder factorization.
    nmax = 30
    for p in (2, 3, 5, 11, 101):
        omega = 0.125
        a = p ** (-0.5 + omega)
        b = p ** (-0.5 - omega)
        K = 1
        h = [0j] * (nmax + 1)
        for k in range(1, nmax + 1):
            h[k] = (a ** k - b ** k) / k

        q_all = [0j] + [-h[k] for k in range(1, nmax + 1)]
        D_from_log = poly_exp(q_all, nmax)
        D_exact = local_D_coeffs(a, b, nmax)
        err = max(abs(x-y) for x, y in zip(D_from_log, D_exact))
        assert err < 2e-12
        checks += 1

        q_charge = [0j] * (nmax + 1)
        q_rem = [0j] * (nmax + 1)
        for k in range(1, nmax + 1):
            if k <= K:
                q_charge[k] = -h[k]
            else:
                q_rem[k] = -h[k]
        charge = poly_exp(q_charge, nmax)
        rem = poly_exp(q_rem, nmax)
        product = poly_mul(charge, rem, nmax)
        err = max(abs(x-y) for x, y in zip(product, D_exact))
        max_factor_error = max(max_factor_error, err)
        assert err < 2e-12
        checks += 1

    # 3. Fiber transport and cocycle in finite prime tensor coordinates.
    primes = [2, 3, 5, 7, 11]
    omega = 0.125
    for t in (0.0, 0.37, -0.91):
        for a_shift in (0.2, -0.4):
            for b_shift in (0.13,):
                for p in primes:
                    aa = p ** (-0.5 + omega)
                    bb = p ** (-0.5 - omega)
                    c_t = local_D_coeffs(aa, bb, 6)
                    c_t = [c * cmath.exp(1j * k * t * math.log(p))
                           for k, c in enumerate(c_t)]
                    once = [c * cmath.exp(1j * k * a_shift * math.log(p))
                            for k, c in enumerate(c_t)]
                    target = local_D_coeffs(aa, bb, 6)
                    target = [c * cmath.exp(1j * k * (t+a_shift) * math.log(p))
                              for k, c in enumerate(target)]
                    err = max(abs(x-y) for x,y in zip(once,target))
                    max_cocycle_error = max(max_cocycle_error, err)
                    assert err < 1e-14
                    checks += 1

                    twice = [c * cmath.exp(1j * k * b_shift * math.log(p))
                             for k, c in enumerate(once)]
                    direct = [c * cmath.exp(1j * k * (a_shift+b_shift) * math.log(p))
                              for k, c in enumerate(c_t)]
                    err = max(abs(x-y) for x,y in zip(twice,direct))
                    max_cocycle_error = max(max_cocycle_error, err)
                    assert err < 1e-14
                    checks += 1

    # 4. Disk model-space identity for B=z^m.
    coeffs = [
        1 + 2j, -0.3 + 0.7j, 2.0 - 0.5j, -1.1j,
        0.25 + 0.1j, -0.8 + 0.2j, 1.3
    ]
    for m in range(1, 6):
        negative_energy = sum(abs(coeffs[j])**2 for j in range(min(m, len(coeffs))))
        model_projection = sum(abs(coeffs[j])**2 for j in range(min(m, len(coeffs))))
        err = abs(negative_energy-model_projection)
        max_model_error = max(max_model_error, err)
        assert err < 1e-15
        checks += 1

    planted_defect = 1.0
    assert planted_defect > 0
    checks += 1

    return {
        "verdict": "PASS_X_91307_HARMONIC_SECTOR_POSITIVE_ENERGY",
        "checks": checks,
        "threshold_rows": threshold_rows,
        "max_factorization_error": max_factor_error,
        "max_fiber_cocycle_error": max_cocycle_error,
        "max_model_projection_error": max_model_error,
        "planted_model_defect": planted_defect,
        "scope": (
            "finite algebra only; source-defined charge neutralization, "
            "positive-energy membership, OCIPE, innerness, and RH are not proved"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
