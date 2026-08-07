#!/usr/bin/env python3
"""Exact finite algebra and discovery-only carry reconnaissance."""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction

SCHEMA = "riemann.x23801-greedy-carry-residual.v1"


def beta_fraction(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)


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
    row_min: Fraction | None = None
    for n in range(2, limit + 1):
        row = Fraction(0)
        for q in range(2, n + 1):
            beta = beta_fraction(n, q)
            if beta != beta_floor_fraction(n, q):
                raise ValueError(f"carry/floor mismatch n={n}, q={q}")
            floor_checks += 1
            row += beta / q
        row_min = row if row_min is None else min(row_min, row)
        for m in range(2, n + 1):
            got = sum(
                mu[k] * beta_fraction(n, m * k)
                for k in range(1, n // m + 1)
            )
            want = Fraction(2 * m - n - 1, n + 1)
            if got != want:
                raise ValueError(
                    f"Mobius affine mismatch n={n}, m={m}: {got} != {want}"
                )
            mobius_checks += 1
    if row_min is None or row_min < Fraction(1, 16):
        raise ValueError(f"row lower bound failed: {row_min}")
    return {
        "limit": limit,
        "beta_floor_checks": floor_checks,
        "mobius_affine_checks": mobius_checks,
        "min_sum_beta_over_q": [row_min.numerator, row_min.denominator],
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
    coefficients = [0.0] * (xmax + 1)
    for j in range(2, xmax + 1):
        coefficients[j] = (
            (j + 1) * (j * u[j] - (j - 2) * u[j + 1])
            + 2 * suffix[j + 2]
        ) / (j * (j - 1))
    negative = [
        j for j in range(2, xmax + 1)
        if coefficients[j] < -1e-12
    ]
    weighted_mass = sum(
        j * coefficients[j] for j in range(2, xmax + 1)
    )
    return {
        "xmax": xmax,
        "classification": "BINARY64_RECONNAISSANCE_ONLY",
        "negative_count_below_minus_1e_12": len(negative),
        "first_negative_indices": negative[:10],
        "weighted_mass": weighted_mass,
        "mass_ratio_to_8_sqrt_x": weighted_mass / (8 * math.sqrt(xmax)),
        "coefficient_mass": sum(coefficients[2:]),
    }


def greedy_recon(xmax: int) -> dict[str, object]:
    residual = [0.0] * (xmax + 1)
    for q in range(2, xmax + 1):
        residual[q] = math.log(xmax / q) / math.sqrt(q)
    coefficients = [0.0] * (xmax + 1)
    nonzero_steps = 0
    off_diagonal = 0
    for n in range(xmax, 1, -1):
        best = math.inf
        pivot = n
        for q in range(2, n + 1):
            beta = float(beta_fraction(n, q))
            if beta <= 0:
                continue
            ratio = residual[q] / beta
            if ratio < best:
                best = ratio
                pivot = q
        if best < 0 and best > -1e-12:
            best = 0.0
        if best < 0:
            raise ValueError(f"negative greedy ratio n={n}: {best}")
        coefficients[n] = best
        if best > 1e-15:
            nonzero_steps += 1
            if pivot != n:
                off_diagonal += 1
            for q in range(2, n + 1):
                beta = float(beta_fraction(n, q))
                if beta > 0:
                    residual[q] -= best * beta
                    if -1e-12 < residual[q] < 0:
                        residual[q] = 0.0
    weighted_mass = sum(
        n * coefficients[n] for n in range(2, xmax + 1)
    )
    positive_potential = sum(
        max(2 - 64 / math.sqrt(q), 0.0) * max(residual[q], 0.0)
        for q in range(2, xmax + 1)
    )
    return {
        "xmax": xmax,
        "classification": "BINARY64_RECONNAISSANCE_ONLY",
        "weighted_mass": weighted_mass,
        "mass_ratio_to_8_sqrt_x": weighted_mass / (8 * math.sqrt(xmax)),
        "nonzero_steps": nonzero_steps,
        "off_diagonal_pivots": off_diagonal,
        "positive_final_residual_count": sum(
            value > 1e-12 for value in residual[2:]
        ),
        "positive_final_residual_potential": positive_potential,
    }


def row_potential_recon(
    limit: int = 5000,
    constant: float = 1.0,
) -> dict[str, object]:
    worst = -math.inf
    argmax = 0
    for n in range(2, limit + 1):
        value = sum(
            (2 - constant / math.sqrt(q)) * float(beta_fraction(n, q))
            for q in range(2, n + 1)
        ) - n
        if value > worst:
            worst = value
            argmax = n
    return {
        "limit": limit,
        "constant": constant,
        "classification": "BINARY64_RECONNAISSANCE_ONLY",
        "max_row_minus_n": worst,
        "argmax_n": argmax,
    }


def verify() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "classification": "EXACT_ALGEBRA_PLUS_BINARY64_RECONNAISSANCE",
        "exact": exact_regression(),
        "inverse_recon": [
            inverse_recon(x) for x in (1000, 10000, 100000)
        ],
        "greedy_recon": [greedy_recon(x) for x in (1000, 2000)],
        "row_potential_recon": row_potential_recon(),
        "proof_boundary": (
            "Only the exact section is proof-grade finite algebra. All inverse, "
            "greedy, and potential scans are binary64 reconnaissance and do not "
            "prove GR, Carry Saturation, or RH."
        ),
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["sha256"] = hashlib.sha256(encoded).hexdigest()
    return payload


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
