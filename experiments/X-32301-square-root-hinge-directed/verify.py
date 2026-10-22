#!/usr/bin/env python3
"""Directed finite certificates for square-root hinge average-row positivity.

Standard-library only.  Every radical is enclosed by an integer interval with
a common decimal denominator.  The checker proves the nominated finite
endpoints only; it does not prove SHARP cofinally or RH.
"""
from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path

DIGITS = 30
SCALE = 10 ** DIGITS
ENDPOINTS = (100, 1_000, 10_000, 100_000, 1_000_000)


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
    """Return integers lo,hi with lo/S <= 1/sqrt(n) <= hi/S."""
    a = isqrt((SCALE * SCALE) // n)
    while (a + 1) * (a + 1) * n <= SCALE * SCALE:
        a += 1
    while a * a * n > SCALE * SCALE:
        a -= 1
    return a, a + 1


def certify_endpoint(T: int) -> dict[str, object]:
    mu = mobius_sieve(T)

    lo = [0] * (T + 1)
    hi = [0] * (T + 1)
    for n in range(1, T + 1):
        lo[n], hi[n] = invsqrt_interval_scaled(n)

    # h_T(n)=n^-1/2-T^-1/2.
    hlo = [0] * (T + 1)
    hhi = [0] * (T + 1)
    for n in range(1, T + 1):
        hlo[n] = lo[n] - hi[T]
        hhi[n] = hi[n] - lo[T]

    # u_m=sum_{k<=T/m} mu(k) h_T(mk).
    ulo = [0] * (T + 2)
    uhi = [0] * (T + 2)
    for k in range(1, T + 1):
        muk = mu[k]
        if muk == 0:
            continue
        upto = T // k
        if muk > 0:
            for m in range(1, upto + 1):
                n = m * k
                ulo[m] += hlo[n]
                uhi[m] += hhi[n]
        else:
            for m in range(1, upto + 1):
                n = m * k
                ulo[m] -= hhi[n]
                uhi[m] -= hlo[n]

    tail_lo = [0] * (T + 3)
    tail_hi = [0] * (T + 3)
    for m in range(T, 0, -1):
        tail_lo[m] = tail_lo[m + 1] + ulo[m]
        tail_hi[m] = tail_hi[m + 1] + uhi[m]

    positive = 0
    min_num_lo: int | None = None
    min_index: int | None = None
    for j in range(2, T):
        # N_j=(j+1)[j u_j-(j-2)u_(j+1)]+2 sum_(m>=j+2)u_m.
        a_lo = j * ulo[j] - (j - 2) * uhi[j + 1]
        a_hi = j * uhi[j] - (j - 2) * ulo[j + 1]
        num_lo = (j + 1) * a_lo + 2 * tail_lo[j + 2]
        num_hi = (j + 1) * a_hi + 2 * tail_hi[j + 2]
        assert num_hi >= num_lo
        assert num_lo > 0, (T, j, num_lo, num_hi)
        positive += 1
        # Compare lower bounds for c_j by cross multiplication.
        if min_num_lo is None:
            min_num_lo, min_index = num_lo, j
        else:
            assert min_index is not None
            if num_lo * min_index * (min_index - 1) < (
                min_num_lo * j * (j - 1)
            ):
                min_num_lo, min_index = num_lo, j

    assert positive == T - 2
    assert min_num_lo is not None and min_index is not None
    # c_T(T)=0 because h_T(T)=0.  We certify all nontrivial j<T strictly.
    return {
        "endpoint": T,
        "strictly_positive_coefficients": positive,
        "endpoint_zero": True,
        "minimum_lower_bound_index": min_index,
        "minimum_lower_bound_scaled_numerator": str(min_num_lo),
        "minimum_lower_bound_denominator": str(
            SCALE * min_index * (min_index - 1)
        ),
    }


def main() -> None:
    results = {
        "schema": "X-32301-square-root-hinge-directed-v1",
        "classification": "DIRECTED_FINITE_SHARP_NOMINATIONS_VERIFIED",
        "digits": DIGITS,
        "endpoints": [certify_endpoint(T) for T in ENDPOINTS],
        "proof_boundary": (
            "directed finite hinge-inverse signs only; "
            "does not prove SHARP for all endpoints or RH"
        ),
    }
    payload = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
