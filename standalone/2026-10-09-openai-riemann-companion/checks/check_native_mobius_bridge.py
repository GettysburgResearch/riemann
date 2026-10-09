#!/usr/bin/env python3
"""Exact finite regression checks for OAI-NB26's arithmetic interfaces.

This authenticates finite identities in the stated ranges. It does not
authenticate an upstream analytic theorem, an all-scale estimate, or RH.
Uses only Python's standard library and exact integers/Fraction arithmetic.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q
from math import isqrt


def primes_through(limit: int) -> list[int]:
    flags = [True] * (limit + 1)
    flags[:2] = [False, False]
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            for k in range(p * p, limit + 1, p):
                flags[k] = False
    return [p for p in range(2, limit + 1) if flags[p]]


def mobius_sieve(limit: int, primes: list[int]) -> list[int]:
    """Ordinary integer Mobius values, independent of norm coefficients."""
    mu = [1] * (limit + 1)
    mu[0] = 0
    for p in primes:
        for n in range(p, limit + 1, p):
            mu[n] = -mu[n]
        for n in range(p * p, limit + 1, p * p):
            mu[n] = 0
    return mu


def norm_mobius(limit: int, primes: list[int], excluded: frozenset[int] = frozenset()) -> list[int]:
    """Multiply local Euler polynomials for Q(sqrt(-3)), truncated by norm.

    A split prime contributes (1-T)^2, an inert prime 1-T^2, and the
    ramified prime 3 contributes 1-T, where T denotes p^{-s}.
    `excluded` refers to rational primes, sufficient for the tests here.
    """
    beta = [0] * (limit + 1)
    beta[1] = 1
    for p in primes:
        if p in excluded:
            continue
        local = [(p, -1)] if p == 3 else ([(p, -2), (p * p, 1)] if p % 3 == 1 else [(p * p, -1)])
        old = beta[:]
        for power, coefficient in local:
            if power <= limit:
                for n in range(1, limit // power + 1):
                    beta[n * power] += coefficient * old[n]
    return beta


def chi(n: int) -> int:
    return (0, 1, -1)[n % 3]


def convolution(left: list[int], right: list[int], limit: int) -> list[int]:
    result = [0] * (limit + 1)
    for a in range(1, limit + 1):
        if left[a]:
            for b in range(1, limit // a + 1):
                result[a * b] += left[a] * right[b]
    return result


def prefix(values: list[int]) -> list[int]:
    result = [0] * len(values)
    for n in range(1, len(values)):
        result[n] = result[n - 1] + values[n]
    return result


def floor_kernel(x: Q, n: int) -> int:
    return int((x.numerator // (x.denominator * n)) % 3 == 1)


def interval_sum(x: Q, beta_prefix: list[int]) -> int:
    """Sum disjoint strict-left/closed-right intervals, using beta prefixes."""
    whole = x.numerator // x.denominator
    answer = 0
    for j in range((whole + 2) // 3):
        lower = x.numerator // (x.denominator * (3 * j + 2))
        upper = x.numerator // (x.denominator * (3 * j + 1))
        answer += beta_prefix[upper] - beta_prefix[lower]
    return answer


def gram_from_intervals(x: int, m: int, n: int) -> Q:
    answer = Q(0)
    for j in range((x // m + 2) // 3):
        for ell in range((x // n + 2) // 3):
            lower = max(m * (3 * j + 1), n * (3 * ell + 1))
            upper = min(x, m * (3 * j + 2) - 1, n * (3 * ell + 2) - 1)
            if lower <= upper:
                answer += Q(1, lower) - Q(1, upper + 1)
    return answer


def cube_floor(n: int) -> int:
    low, high = 0, n + 1
    while low + 1 < high:
        mid = (low + high) // 2
        if mid * mid * mid <= n:
            low = mid
        else:
            high = mid
    return low


def cubic_mesh(y: int) -> list[tuple[int, int]]:
    b, a, end = y + 1, y + 1, (y + 1) ** 2
    blocks = []
    while a < end:
        h = min(end - a, cube_floor(a * a // b))
        if h < 1:
            raise AssertionError("Cubic mesh failed to advance")
        blocks.append((a, h))
        a += h
    return blocks


def require_equal(left: object, right: object, context: str) -> None:
    if left != right:
        raise AssertionError(f"{context}: {left!r} != {right!r}")


def run(limit: int, gram_limit: int, square_step_limit: int) -> dict[str, object]:
    if limit < 7 or not 1 <= gram_limit <= limit or not 1 <= square_step_limit or (square_step_limit + 1) ** 2 - 1 > limit:
        raise ValueError("Require limit>=7, 1<=gram-limit<=limit, and (square-step-limit+1)^2-1<=limit")
    primes = primes_through(limit)
    mu = mobius_sieve(limit, primes)
    beta = norm_mobius(limit, primes)
    beta_away_6 = norm_mobius(limit, primes, frozenset({2, 3}))
    char = [0] + [chi(n) for n in range(1, limit + 1)]
    mu_char = [mu[n] * char[n] for n in range(limit + 1)]
    require_equal(convolution(mu, mu_char, limit), beta, "beta = mu * (mu chi)")
    require_equal(convolution(beta, char, limit), mu, "mu = beta * chi")

    restore = [0] * (limit + 1)
    for n, coefficient in ((1, 1), (3, -1), (4, -1), (12, 1)):
        if n <= limit:
            restore[n] = coefficient
    require_equal(convolution(restore, beta_away_6, limit), beta, "Euler restoration at norm 3 and norm 4")
    require_equal(beta[3], -1, "ramified coefficient")
    require_equal(beta[7], -2, "split-prime coefficient is not one-bounded")

    big_m = prefix(mu)
    beta_prefix = prefix(beta)
    char_prefix = prefix(char)
    for n in range(limit + 1):
        require_equal(char_prefix[n], int(n % 3 == 1), f"character partial sum at {n}")

    rational_cases = 0
    for k in range(limit + 1):
        for offset in (Q(0), Q(1, 2), Q(2, 3)):
            x = Q(k) + offset
            floor_value = sum(beta[n] * floor_kernel(x, n) for n in range(1, k + 1))
            require_equal(floor_value, big_m[k], f"floor identity at {x}")
            require_equal(interval_sum(x, beta_prefix), big_m[k], f"strict/closed interval identity at {x}")
            rational_cases += 1

    # Two explicit rejected shortcuts, tested rather than silently assumed.
    uncorrected_at_3 = sum(beta_away_6[n] * floor_kernel(Q(3), n) for n in range(1, 4))
    if uncorrected_at_3 == big_m[3]:
        raise AssertionError("Missing ramified-factor counterexample disappeared")
    absolute_at_4 = sum(abs(beta[n]) * floor_kernel(Q(4), n) for n in range(1, 5))
    if absolute_at_4 == big_m[4]:
        raise AssertionError("Absolute coefficient replacement counterexample disappeared")

    small_m = [Q(0)] * (limit + 1)
    harmonic = [Q(0)] * (limit + 1)
    char_harmonic = [Q(0)] * (limit + 1)
    energies_f = [Q(0)] * (limit + 1)
    energy_e = Q(0)
    completed_mean = Q(0)
    for x in range(1, limit + 1):
        harmonic[x] = harmonic[x - 1] + Q(1, x)
        char_harmonic[x] = char_harmonic[x - 1] + Q(char[x], x)
        small_m[x] = small_m[x - 1] + Q(mu[x], x)
        energies_f[x] = energies_f[x - 1] + small_m[x] ** 2
        energy_e += Q(big_m[x] ** 2, x * (x + 1))
        completed_mean += Q(big_m[x], x * (x + 1))
        energy_a = energy_e + 2 * (x + 1) * completed_mean ** 2
        require_equal(energies_f[x], energy_e + (x + 1) * completed_mean ** 2, f"F/E completion at {x}")
        require_equal(energy_a, 2 * energies_f[x] - energy_e, f"A completion at {x}")
        if not energies_f[x] <= energy_a <= 2 * energies_f[x] or energies_f[x] < energies_f[x - 1]:
            raise AssertionError(f"Completion comparison/monotonicity at {x}")
        reciprocal_adapter = sum(Q(beta[n], n) * char_harmonic[x // n] for n in range(1, x + 1))
        require_equal(reciprocal_adapter, small_m[x], f"reciprocal coefficient adapter at {x}")

    gram_entries = 0
    for x in range(1, gram_limit + 1):
        weights = [Q(0)] + [Q(1, k * (k + 1)) for k in range(1, x + 1)]
        cells = [[0] * (x + 1)] + [[0] + [floor_kernel(Q(k), n) for n in range(1, x + 1)] for k in range(1, x + 1)]
        gram_energy = Q(0)
        gram_mean = Q(0)
        for m in range(1, x + 1):
            v_m = sum(weights[k] * cells[k][m] for k in range(1, x + 1))
            v_signed = sum(char[r] * (Q(1, m * r) - Q(1, x + 1)) for r in range(1, x // m + 1))
            require_equal(v_m, v_signed, f"signed completion vector {x},{m}")
            gram_mean += beta[m] * v_m
            for n in range(1, x + 1):
                direct = sum(weights[k] * cells[k][m] * cells[k][n] for k in range(1, x + 1))
                signed_max = sum(char[r] * char[s] * (Q(1, max(m * r, n * s)) - Q(1, x + 1)) for r in range(1, x // m + 1) for s in range(1, x // n + 1))
                require_equal(direct, signed_max, f"signed max Gram {x},{m},{n}")
                require_equal(direct, gram_from_intervals(x, m, n), f"intersection Gram {x},{m},{n}")
                gram_energy += beta[m] * beta[n] * direct
                gram_entries += 1
        direct_e = sum(Q(big_m[k] ** 2, k * (k + 1)) for k in range(1, x + 1))
        direct_u = sum(Q(big_m[k], k * (k + 1)) for k in range(1, x + 1))
        require_equal(gram_energy, direct_e, f"quadratic-form energy {x}")
        require_equal(gram_mean, direct_u, f"quadratic-form completion mean {x}")
        require_equal(gram_energy + 2 * (x + 1) * gram_mean ** 2, 2 * energies_f[x] - direct_e, f"completed Gram energy {x}")

    block_count = 0
    for y in range(1, square_step_limit + 1):
        end = (y + 1) ** 2 - 1
        blocks = cubic_mesh(y)
        coarse, defect, mesh_budget = Q(0), Q(0), Q(0)
        for a, h in blocks:
            native_mean = sum(small_m[k] for k in range(a, a + h)) / h
            adapter_mean = Q(0)
            for n in range(1, end + 1):
                count_weight = sum(Q(char[r], r) * max(0, a + h - max(a, n * r)) for r in range(1, (a + h - 1) // n + 1))
                adapter_mean += Q(beta[n], h * n) * count_weight

            def harmonic_antiderivative(d: int, t: int) -> Q:
                quotient = (t - 1) // d
                return t * harmonic[quotient] - d * quotient

            newton_mean = 2 * small_m[y]
            for r in range(1, y + 1):
                for s in range(1, y + 1):
                    d = r * s
                    newton_mean -= Q(mu[r] * mu[s], h * d) * (harmonic_antiderivative(d, a + h) - harmonic_antiderivative(d, a))
            require_equal(native_mean, adapter_mean, f"norm-coefficient block mean {y},{a},{h}")
            require_equal(native_mean, newton_mean, f"old-prefix Newton block mean {y},{a},{h}")
            coarse += h * native_mean ** 2
            defect += sum((small_m[k] - native_mean) ** 2 for k in range(a, a + h))
            mesh_budget += Q(h * (h * h - 1), 12 * a * a)
            block_count += 1
        require_equal(coarse + defect, energies_f[end] - energies_f[y], f"complete square-step energy {y}")
        if not 0 <= defect <= mesh_budget < Q(5, 6) or not len(blocks) < 10 * (y + 1):
            raise AssertionError(f"NRC32 exact cubic-mesh budget at {y}")

    return {
        "status": "PASS",
        "arithmetic": "exact integers and fractions; no floating-point tolerances",
        "coefficient_and_completion_prefixes": limit,
        "rational_endpoint_cases": rational_cases,
        "rational_endpoint_grid": "x=k, k+1/2, k+2/3 for every integer 0<=k<=limit",
        "all_gram_cutoffs": [1, gram_limit],
        "gram_entries_compared_in_three_forms": gram_entries,
        "all_square_step_inputs": [1, square_step_limit],
        "square_step_blocks_compared_in_three_forms": block_count,
        "counterexamples": {
            "beta_3": beta[3],
            "beta_7_not_one_bounded": beta[7],
            "missing_local_factors_at_x_3": {"uncorrected": uncorrected_at_3, "M_3": big_m[3]},
            "absolute_coefficients_at_x_4": {"absolute_sum": absolute_at_4, "M_4": big_m[4]},
        },
        "scope": "finite algebra regression only; no upstream theorem, all-scale inequality, or RH validation",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=512)
    parser.add_argument("--gram-limit", type=int, default=24)
    parser.add_argument("--square-step-limit", type=int, default=12)
    args = parser.parse_args()
    print(json.dumps(run(args.limit, args.gram_limit, args.square_step_limit), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
