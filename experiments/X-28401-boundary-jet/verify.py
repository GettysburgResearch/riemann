from __future__ import annotations

from fractions import Fraction
from math import comb


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


def third_abel_producer(endpoint: int) -> list[Fraction]:
    mu = mobius_sieve(endpoint)
    target = [Fraction(0) for _ in range(endpoint + 1)]
    for q in range(2, endpoint + 1):
        target[q] = Fraction(comb(endpoint - q + 2, 2))

    mobius_state = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(1, endpoint + 1):
        for k in range(1, endpoint // m + 1):
            if mu[k]:
                mobius_state[m] += mu[k] * target[m * k]

    divergence = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(1, endpoint + 1):
        divergence[m] = mobius_state[m] - mobius_state[m + 1]

    producer = [Fraction(0) for _ in range(endpoint + 2)]
    incoming = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(endpoint, 1, -1):
        producer[m] = divergence[m] + incoming[m]
        a3 = (m + 2) // 3
        b3 = m - a3
        a2 = m // 2
        b2 = m - a2
        for child in (a3, b3, a2, b2):
            if child >= 2:
                incoming[child] += producer[m] / 2
    return producer


def main() -> None:
    endpoint = 520
    producer = third_abel_producer(endpoint)
    minimum, argmin = min(
        (producer[n], n) for n in range(2, endpoint + 1)
    )

    assert producer[15] == Fraction(-91, 256)
    assert minimum == Fraction(-91, 256)
    assert argmin == 15

    # Positive finite scans are not cofinal theorems.
    for control_endpoint in (40, 80):
        control = third_abel_producer(control_endpoint)
        assert min(control[2 : control_endpoint + 1]) >= 0

    print("PASS_EXACT_FIXED_THIRD_ABEL_REFUTATION")
    print("endpoint", endpoint)
    print("argmin", argmin)
    print("minimum", minimum)
    print("controls", "40,80 nonnegative")
    print(
        "proof_boundary",
        "exact finite producer mutation only; no RBJC, DCCS, or RH claim",
    )


if __name__ == "__main__":
    main()
