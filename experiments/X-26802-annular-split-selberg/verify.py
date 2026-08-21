#!/usr/bin/env python3
"""Exact regression for the annular split-frame and generalized Selberg defect.

Standard-library only.  The checker verifies finite rational/formal algebra.
It does not prove the annular Selberg recurrence, Bottom-Charge Positivity, or RH.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path


MAX_N = 64
MAX_M = 10


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


def omega2(n: int, mu: list[int]) -> Fraction:
    value = Fraction(mu[n])
    if n % 2 == 0:
        value -= Fraction(3, 2) * mu[n // 2]
    if n % 4 == 0:
        value += Fraction(1, 2) * mu[n // 4]
    return value


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        out += 1
        n //= 2
    return out


def aomega(n: int) -> Fraction:
    v = v2(n)
    return Fraction(2 * v) + Fraction(1, 2**v)


def g(m: int, r: int) -> Fraction:
    if m <= r < 2 * m:
        return Fraction(1)
    if 2 * m <= r < 4 * m:
        return Fraction(-1, 2)
    return Fraction(0)


@lru_cache(maxsize=None)
def factorization(n: int) -> dict[int, int]:
    answer: dict[int, int] = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                exponent += 1
                n //= p
            answer[p] = exponent
        p = 3 if p == 2 else p + 2
    if n > 1:
        answer[n] = 1
    return answer


Linear = dict[int, Fraction]
Quadratic = dict[tuple[int, int], Fraction]


def clean(values: dict) -> dict:
    return {key: value for key, value in values.items() if value}


def lin_add(left: Linear, right: Linear, scale: Fraction = Fraction(1)) -> Linear:
    out = defaultdict(Fraction)
    out.update(left)
    for key, value in right.items():
        out[key] += scale * value
    return clean(dict(out))


def lin_scale(value: Linear, scale: Fraction) -> Linear:
    return clean({key: scale * coefficient for key, coefficient in value.items()})


def lin_mul(left: Linear, right: Linear) -> Quadratic:
    out = defaultdict(Fraction)
    for p, a in left.items():
        for q, b in right.items():
            key = (p, q) if p <= q else (q, p)
            out[key] += a * b
    return clean(dict(out))


def quad_add(
    left: Quadratic, right: Quadratic, scale: Fraction = Fraction(1)
) -> Quadratic:
    out = defaultdict(Fraction)
    out.update(left)
    for key, value in right.items():
        out[key] += scale * value
    return clean(dict(out))


def quad_scale(value: Quadratic, scale: Fraction) -> Quadratic:
    return clean({key: scale * coefficient for key, coefficient in value.items()})


@lru_cache(maxsize=None)
def formal_log(n: int) -> Linear:
    return {prime: Fraction(exponent) for prime, exponent in factorization(n).items()}


def convolution_linear(
    scalar: list[Fraction], linear: list[Linear], n: int
) -> Linear:
    out: Linear = {}
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            out = lin_add(out, linear[divisor], scalar[n // divisor])
    return out


def convolution_quadratic(
    scalar: list[Fraction], quadratic: list[Quadratic], n: int
) -> Quadratic:
    out: Quadratic = {}
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            out = quad_add(out, quadratic[divisor], scalar[n // divisor])
    return out


def convolution_linear_linear(
    left: list[Linear], right: list[Linear], n: int
) -> Quadratic:
    out: Quadratic = {}
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            out = quad_add(out, lin_mul(left[divisor], right[n // divisor]))
    return out


def deterministic_coefficients(m: int) -> dict[int, Fraction]:
    return {
        index: Fraction(((index * index + 3 * index + 1) % 11) - 5, index + 2)
        for index in range(m, 2 * m)
    }


def main() -> None:
    mu = mobius_sieve(MAX_N * 4)
    omega = [Fraction(0)] + [omega2(n, mu) for n in range(1, MAX_N * 4 + 1)]

    floor_rows = 0
    for m in range(1, MAX_M + 1):
        for r in range(0, MAX_N + 1):
            actual = sum(
                omega[k] * (r // (m * k)) for k in range(1, r // m + 1)
            )
            assert actual == g(m, r)
            floor_rows += 1

    split_rows = 0
    weighted_isometries = 0
    for m in range(1, MAX_M + 1):
        coefficients = deterministic_coefficients(m)

        def potential(r: int) -> Fraction:
            return sum(
                coefficient * g(scale, r)
                for scale, coefficient in coefficients.items()
            )

        for n in range(1, 16 * m):
            for j in range(n + 1):
                left = sum(
                    coefficient
                    * (g(scale, n) - g(scale, j) - g(scale, n - j))
                    for scale, coefficient in coefficients.items()
                )
                right = potential(n) - potential(j) - potential(n - j)
                assert left == right
                split_rows += 1

        endpoint = 16 * m - 1
        assert all(potential(r) == 0 for r in range(0, m))
        assert all(potential(r) == 0 for r in range(8 * m, endpoint + 1))

        physical = sum(
            potential(r) ** 2 * Fraction(1, r * (r + 1))
            for r in range(m, 8 * m)
        )
        split = sum(
            (
                potential(endpoint)
                - potential(j)
                - potential(endpoint - j)
            )
            ** 2
            * Fraction(1, j * (j + 1))
            for j in range(1, 8 * m)
        )
        assert physical == split
        weighted_isometries += 1

    a = [Fraction(0)] + [aomega(n) for n in range(1, MAX_N + 1)]
    omega_short = omega[: MAX_N + 1]
    a_log: list[Linear] = [{} for _ in range(MAX_N + 1)]
    a_log2: list[Quadratic] = [{} for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        log_n = formal_log(n)
        a_log[n] = lin_scale(log_n, a[n])
        a_log2[n] = quad_scale(lin_mul(log_n, log_n), a[n])

    generalized_lambda: list[Linear] = [{} for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        generalized_lambda[n] = convolution_linear(omega_short, a_log, n)

    lambda_rows = 0
    selberg_rows = 0
    defect_rows = 0
    for n in range(1, MAX_N + 1):
        expected: Linear = {}
        factors = factorization(n)
        if len(factors) == 1:
            prime, exponent = next(iter(factors.items()))
            expected[prime] = Fraction(1)
            if prime == 2:
                expected[2] += Fraction(1) + Fraction(1, 2**exponent)
        assert generalized_lambda[n] == expected
        lambda_rows += 1

        left = convolution_quadratic(omega_short, a_log2, n)
        lambda_log = lin_mul(generalized_lambda[n], formal_log(n))
        lambda_square = convolution_linear_linear(
            generalized_lambda, generalized_lambda, n
        )
        forcing = quad_add(lambda_log, lambda_square)
        assert left == forcing
        selberg_rows += 1

        defect = quad_add(a_log2[n], forcing, Fraction(-1))
        proper_divisor_sum: Quadratic = {}
        for divisor in range(1, n):
            if n % divisor == 0:
                term = quad_add(
                    lin_mul(generalized_lambda[divisor], formal_log(divisor)),
                    convolution_linear_linear(
                        generalized_lambda, generalized_lambda, divisor
                    ),
                )
                proper_divisor_sum = quad_add(
                    proper_divisor_sum, term, a[n // divisor]
                )
        assert defect == proper_divisor_sum
        assert all(coefficient >= 0 for coefficient in defect.values())
        defect_rows += 1

    mutation_rejections = 0
    bad_outer = Fraction(-2, 3)
    failed = False
    for r in range(0, 10):
        bad_g = (
            Fraction(1)
            if 1 <= r < 2
            else bad_outer
            if 2 <= r < 4
            else Fraction(0)
        )
        actual = sum(omega[k] * (r // k) for k in range(1, r + 1))
        if actual != bad_g:
            failed = True
            break
    assert failed
    mutation_rejections += 1

    m = 5
    coefficients = deterministic_coefficients(m)

    def potential(r: int) -> Fraction:
        return sum(
            coefficient * g(scale, r)
            for scale, coefficient in coefficients.items()
        )

    bad_endpoint = 8 * m - 1
    bad_physical = sum(
        potential(r) ** 2 * Fraction(1, r * (r + 1))
        for r in range(m, 8 * m)
    )
    bad_split = sum(
        (
            potential(bad_endpoint)
            - potential(j)
            - potential(bad_endpoint - j)
        )
        ** 2
        * Fraction(1, j * (j + 1))
        for j in range(1, 8 * m)
    )
    assert bad_split != bad_physical
    mutation_rejections += 1

    result = {
        "schema": "X-26802-annular-split-selberg-v1",
        "classification": "EXACT_ANNULAR_SPLIT_AND_SELBERG_DEFECT_VERIFIED",
        "max_n": MAX_N,
        "max_annulus": MAX_M,
        "checks": {
            "compact_floor_source_rows": floor_rows,
            "split_intertwiner_rows": split_rows,
            "weighted_annular_isometries": weighted_isometries,
            "generalized_lambda_rows": lambda_rows,
            "formal_selberg_rows": selberg_rows,
            "positive_defect_rows": defect_rows,
            "mutations_rejected": mutation_rejections,
        },
        "proof_boundary": (
            "finite rational/formal algebra only; the annular reflected "
            "recurrence, bottom-charge sign, and RH are not proved"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
