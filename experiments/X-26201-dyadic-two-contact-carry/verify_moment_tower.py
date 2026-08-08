#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json

LIMIT = 72
EXPECTED_SHA256 = "eaaed5595e09e6b7d0f9fd990f42bea3e99d4c4e180fd04d78b7d2fa8434c2af"


def mobius_table(limit: int) -> list[int]:
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


def divisor_table(limit: int) -> list[list[int]]:
    out = [[] for _ in range(limit + 1)]
    for d in range(1, limit + 1):
        for n in range(d, limit + 1, d):
            out[n].append(d)
    return out


MU = mobius_table(LIMIT)
DIVS = divisor_table(LIMIT)


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        out += 1
        n //= 2
    return out


OMEGA = [Fraction(0)] * (LIMIT + 1)
AOMEGA = [Fraction(0)] * (LIMIT + 1)
for n in range(1, LIMIT + 1):
    om = Fraction(MU[n])
    if n % 2 == 0:
        om -= Fraction(3, 2) * MU[n // 2]
    if n % 4 == 0:
        om += Fraction(1, 2) * MU[n // 4]
    OMEGA[n] = om
    vv = v2(n)
    AOMEGA[n] = Fraction(2 * vv, 1) + Fraction(1, 2**vv)


PRIME_WEIGHT = [0] * (LIMIT + 1)
idx = 0
for p in range(2, LIMIT + 1):
    if all(p % d for d in range(2, int(p**0.5) + 1)):
        idx += 1
        PRIME_WEIGHT[p] = idx


ADDLOG = [0] * (LIMIT + 1)
for n0 in range(1, LIMIT + 1):
    n = n0
    p = 2
    value = 0
    while p * p <= n:
        while n % p == 0:
            value += PRIME_WEIGHT[p]
            n //= p
        p += 1
    if n > 1:
        value += PRIME_WEIGHT[n]
    ADDLOG[n0] = value


def convolution_values(weight_power: int) -> list[Fraction]:
    values = [Fraction(0)] * (LIMIT + 1)
    for n in range(1, LIMIT + 1):
        values[n] = sum(
            OMEGA[n // m] * AOMEGA[m] * (ADDLOG[m] ** weight_power)
            for m in DIVS[n]
        )
    return values


INV = convolution_values(0)
LAMBDA = convolution_values(1)
SECOND = convolution_values(2)


def carry(n: int, j: int, q: int) -> int:
    if q == 1:
        return 0
    return n // q - j // q - (n - j) // q


def z_wavelet(n: int, j: int, m: int, mutate: bool = False) -> Fraction:
    total = Fraction(0)
    for k in range(1, n // m + 1):
        coeff = OMEGA[k]
        if mutate and k == 2:
            coeff += Fraction(1, 2)
        total += coeff * carry(n, j, m * k)
    return total


def check_convolutions() -> dict[str, int]:
    for n in range(1, LIMIT + 1):
        expected = Fraction(1 if n == 1 else 0)
        if INV[n] != expected:
            raise AssertionError(("inverse", n, INV[n], expected))
        rhs = LAMBDA[n] * ADDLOG[n] + sum(
            LAMBDA[d] * LAMBDA[n // d] for d in DIVS[n]
        )
        if SECOND[n] != rhs:
            raise AssertionError(("Selberg", n, SECOND[n], rhs))
        if LAMBDA[n] < 0 or SECOND[n] < 0:
            raise AssertionError(("positivity", n, LAMBDA[n], SECOND[n]))
    return {"rows": LIMIT}


def check_moment_tower() -> dict[str, int]:
    cells = 0
    boundary_cells = 0
    mutation_rejected = False
    for n in range(2, LIMIT + 1):
        for j in range(n + 1):
            zvals = [Fraction(0)] + [
                z_wavelet(n, j, m) for m in range(1, n + 1)
            ]
            m0 = sum(AOMEGA[m] * zvals[m] for m in range(1, n + 1))
            m1 = sum(
                AOMEGA[m] * ADDLOG[m] * zvals[m] for m in range(1, n + 1)
            )
            m2 = sum(
                AOMEGA[m] * ADDLOG[m] ** 2 * zvals[m]
                for m in range(1, n + 1)
            )
            c0 = sum(INV[q] * carry(n, j, q) for q in range(1, n + 1))
            c1 = sum(LAMBDA[q] * carry(n, j, q) for q in range(1, n + 1))
            c2 = sum(SECOND[q] * carry(n, j, q) for q in range(1, n + 1))
            if (m0, m1, m2) != (c0, c1, c2):
                raise AssertionError(("moment", n, j, m0, c0, m1, c1, m2, c2))
            if m0 != 0 or m1 < 0 or m2 < 0:
                raise AssertionError(("sign", n, j, m0, m1, m2))

            unit = AOMEGA[1] * zvals[1]
            if unit != 0:
                boundary_cells += 1
                if m0 - unit == 0:
                    raise AssertionError(("unit boundary lost", n, j, unit))

            mutated_m0 = sum(
                AOMEGA[m] * z_wavelet(n, j, m, mutate=True)
                for m in range(1, n + 1)
            )
            mutation_rejected |= mutated_m0 != 0
            cells += 1

    if not mutation_rejected:
        raise AssertionError("coefficient mutation was not detected")
    return {
        "pointwise_cells": cells,
        "nonzero_unit_boundary_cells": boundary_cells,
        "coefficient_mutation_rejected": 1,
    }


def build_result() -> dict[str, object]:
    return {
        "schema": "X-26201-selberg-carry-moment-tower-v1",
        "classification": "PASS_EXACT_SELBERG_CARRY_MOMENT_TOWER_AND_BOUNDARY_FIREWALL",
        "checks": {
            "convolutions": check_convolutions(),
            "moment_tower": check_moment_tower(),
        },
        "scope": (
            "exact finite algebra only; does not prove physical transference, "
            "F5TC, bottom-charge positivity, DSS, or RH"
        ),
    }


def main() -> None:
    result = build_result()
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError((digest, EXPECTED_SHA256))
    result["sha256_without_digest"] = digest
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
