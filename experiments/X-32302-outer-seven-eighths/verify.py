#!/usr/bin/env python3
"""Directed finite base for the outer-seven-eighths SHARP theorem.

Standard-library only. It certifies all endpoints 3<=T<40 and every
coefficient index j>T/8 using integer enclosures for inverse square roots.
The cofinal T>=40 argument is analytic and lives in L-32304.
"""
from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path

DIGITS = 36
SCALE = 10 ** DIGITS
T_MAX = 39


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def invsqrt_interval_scaled(n: int) -> tuple[int, int]:
    a = isqrt((SCALE * SCALE) // n)
    while (a + 1) * (a + 1) * n <= SCALE * SCALE:
        a += 1
    while a * a * n > SCALE * SCALE:
        a -= 1
    return a, a + 1


def certify(T: int) -> tuple[int, int]:
    mu = mobius_sieve(T)
    lo = [0] * (T + 1)
    hi = [0] * (T + 1)
    for n in range(1, T + 1):
        lo[n], hi[n] = invsqrt_interval_scaled(n)

    hlo = [0] * (T + 1)
    hhi = [0] * (T + 1)
    for n in range(1, T + 1):
        hlo[n] = lo[n] - hi[T]
        hhi[n] = hi[n] - lo[T]

    ulo = [0] * (T + 2)
    uhi = [0] * (T + 2)
    for k in range(1, T + 1):
        muk = mu[k]
        if muk == 0:
            continue
        for m in range(1, T // k + 1):
            n = m * k
            if muk > 0:
                ulo[m] += hlo[n]
                uhi[m] += hhi[n]
            else:
                ulo[m] -= hhi[n]
                uhi[m] -= hlo[n]

    tail = [0] * (T + 3)
    for m in range(T, 0, -1):
        tail[m] = tail[m + 1] + ulo[m]

    checked = 0
    minimum: tuple[int, int] | None = None
    for j in range(2, T):
        if 8 * j <= T:
            continue
        a_lo = j * ulo[j] - (j - 2) * uhi[j + 1]
        num_lo = (j + 1) * a_lo + 2 * tail[j + 2]
        assert num_lo > 0, (T, j, num_lo)
        checked += 1
        if minimum is None or (
            num_lo * minimum[0] * (minimum[0] - 1)
            < minimum[1] * j * (j - 1)
        ):
            minimum = (j, num_lo)
    return checked, minimum[0] if minimum else 0


def rational_gates() -> dict[str, bool]:
    gates = {
        "inv2_lt_177_over_250": 177 * 177 * 2 > 250 * 250,
        "inv3_lt_289_over_500": 289 * 289 * 3 > 500 * 500,
        "sqrt5_lt_9_over_4": 5 * 16 < 81,
        "inv5_lt_9_over_20": 9 * 9 * 5 > 20 * 20,
        "inv6_gt_20_over_49": 20 * 20 * 6 < 49 * 49,
        "sqrt7_lt_8_over_3": 7 * 9 < 64,
        "inv2_lt_7072_over_10000": 7072 * 7072 * 2 > 10000 * 10000,
        "inv3_lt_5774_over_10000": 5774 * 5774 * 3 > 10000 * 10000,
        "inv5_lt_4473_over_10000": 4473 * 4473 * 5 > 10000 * 10000,
        "inv7_lt_3780_over_10000": 3780 * 3780 * 7 > 10000 * 10000,
        "inv6_gt_4082_over_10000": 4082 * 4082 * 6 < 10000 * 10000,
        "sqrt8_lt_2829_over_1000": 8 * 1000 * 1000 < 2829 * 2829,
    }
    assert all(gates.values())
    return gates


def main() -> None:
    total = 0
    endpoints = []
    for T in range(3, T_MAX + 1):
        checked, minimum_index = certify(T)
        total += checked
        endpoints.append(
            {"T": T, "checked": checked, "minimum_index": minimum_index}
        )
    data = {
        "schema": "X-32302-outer-seven-eighths-v1",
        "classification": "DIRECTED_FINITE_OUTER_SEVEN_EIGHTHS_SHARP_VERIFIED",
        "finite_endpoint_max": T_MAX,
        "coefficient_rows_checked": total,
        "rational_gates": rational_gates(),
        "endpoints": endpoints,
        "proof_boundary": (
            "finite base only; T>=40 is proved analytically in L-32304; "
            "neither this file alone nor finite checks prove RH"
        ),
    }
    raw = json.dumps(data, indent=2, sort_keys=True) + "\n"
    data["sha256_without_digest"] = hashlib.sha256(raw.encode()).hexdigest()
    output = json.dumps(data, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
