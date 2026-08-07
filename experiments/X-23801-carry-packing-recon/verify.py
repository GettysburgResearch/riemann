#!/usr/bin/env python3
"""Discovery-only regression for the carry-packing proposal.

Exact checks use fractions.Fraction. Large-X rows use binary64 and are
explicitly labelled reconnaissance, not proof certificates.
"""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction

SCHEMA = "riemann.x23801-carry-packing-recon.v1"


def beta_fraction(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def beta_floor_fraction(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    return Fraction(n // q) - Fraction(
        2 * sum(j // q for j in range(n + 1)), n + 1
    )


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def exact_regression(limit: int = 50) -> dict[str, object]:
    mu = mobius_sieve(limit)
    floor_checks = 0
    mobius_checks = 0
    row_lower_min: Fraction | None = None
    for n in range(2, limit + 1):
        s = Fraction(0)
        for q in range(2, n + 1):
            b = beta_fraction(n, q)
            if b != beta_floor_fraction(n, q):
                raise AssertionError(("beta-floor", n, q))
            floor_checks += 1
            s += b / q
        row_lower_min = s if row_lower_min is None else min(row_lower_min, s)
        for m in range(2, n + 1):
            got = sum(
                mu[k] * beta_fraction(n, m * k)
                for k in range(1, n // m + 1)
            )
            want = Fraction(2 * m - n - 1, n + 1)
            if got != want:
                raise AssertionError(("mobius-affine", n, m, got, want))
            mobius_checks += 1
    if row_lower_min is None or row_lower_min < Fraction(1, 16):
        raise AssertionError(("row-lower", row_lower_min))
    return {
        "limit": limit,
        "beta_floor_checks": floor_checks,
        "mobius_affine_checks": mobius_checks,
        "min_sum_beta_over_q": [row_lower_min.numerator, row_lower_min.denominator],
    }


def inverse_recon(xmax: int) -> dict[str, object]:
    mu = mobius_sieve(xmax)
    w = [0.0] * (xmax + 1)
    for q in range(1, xmax + 1):
        w[q] = math.log(xmax / q) / math.sqrt(q)
    u = [0.0] * (xmax + 3)
    for k in range(1, xmax + 1):
        if mu[k] == 0:
            continue
        for m in range(2, xmax // k + 1):
            u[m] += mu[k] * w[m * k]
    suffix = [0.0] * (xmax + 4)
    for m in range(xmax, 1, -1):
        suffix[m] = suffix[m + 1] + u[m]
    c = [0.0] * (xmax + 1)
    for j in range(2, xmax + 1):
        c[j] = (
            (j + 1) * (j * u[j] - (j - 2) * u[j + 1])
            + 2 * suffix[j + 2]
        ) / (j * (j - 1))
    negative = [j for j in range(2, xmax + 1) if c[j] < -1e-12]
    weighted_mass = sum(j * c[j] for j in range(2, xmax + 1))
    coeff_mass = sum(c[2:])
    return {
        "xmax": xmax,
        "classification": "BINARY64_RECONNAISSANCE_ONLY",
        "negative_count_below_minus_1e_12": len(negative),
        "first_negative_indices": negative[:10],
        "weighted_mass": weighted_mass,
        "mass_ratio_to_8_sqrt_x": weighted_mass / (8 * math.sqrt(xmax)),
        "coefficient_mass": coeff_mass,
    }


def row_potential_recon(limit: int = 5000, constant: float = 1.0) -> dict[str, object]:
    worst_value = -math.inf
    worst_n = 0
    for n in range(2, limit + 1):
        row = 0.0
        for q in range(2, n + 1):
            row += (2.0 - constant / math.sqrt(q)) * float(beta_fraction(n, q))
        violation = row - n
        if violation > worst_value:
            worst_value = violation
            worst_n = n
    return {
        "limit": limit,
        "constant": constant,
        "classification": "BINARY64_RECONNAISSANCE_ONLY",
        "max_row_minus_n": worst_value,
        "argmax_n": worst_n,
    }


def payload() -> dict[str, object]:
    data: dict[str, object] = {
        "schema": SCHEMA,
        "exact": exact_regression(),
        "inverse_recon": [inverse_recon(x) for x in (1000, 10000, 100000)],
        "row_potential_recon": row_potential_recon(),
        "proof_boundary": (
            "Exact finite algebra is checked only in the exact section. "
            "The inverse and row-potential scans are binary64 reconnaissance "
            "and do not prove GCM, Carry Saturation, or RH."
        ),
    }
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    data["sha256"] = hashlib.sha256(encoded).hexdigest()
    return data


if __name__ == "__main__":
    print(json.dumps(payload(), indent=2, sort_keys=True))
