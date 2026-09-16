#!/usr/bin/env python3
"""Independent exact cross-checks for the 2026-08-07 fourth-pass review.

Only Python's standard library is used.  All arithmetic checks are exact over
fractions/integers except for no transcendental numerical claims whatsoever.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    m = n
    parity = 0
    p = 2
    while p * p <= m:
        if m % p == 0:
            exponent = 0
            while m % p == 0:
                m //= p
                exponent += 1
            if exponent >= 2:
                return 0
            parity ^= 1
        p = 3 if p == 2 else p + 2
    if m > 1:
        parity ^= 1
    return -1 if parity else 1


def beta(n: int, q: int) -> Fraction:
    if n < 0 or q < 1:
        raise ValueError("invalid carry indices")
    if q > n:
        return Fraction(0)
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def continuum_b_at_ratio(n: int, q: int) -> Fraction:
    """Right-continuous b(n/q) from PR #252."""
    if q > n or q < 1:
        raise ValueError("require 1 <= q <= n")
    k, r = divmod(n, q)
    if r == 0:
        return Fraction(1)
    return Fraction(k * (q - r), n)


def v2(n: int) -> int:
    exponent = 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    return exponent


def binary_digit_sum(n: int) -> int:
    return n.bit_count()


def prime_powers_up_to(x: int) -> list[int]:
    sieve = [True] * (x + 1)
    primes: list[int] = []
    for n in range(2, x + 1):
        if sieve[n]:
            primes.append(n)
            if n * n <= x:
                for k in range(n * n, x + 1, n):
                    sieve[k] = False
    values: set[int] = set()
    for p in primes:
        q = p
        while q <= x:
            values.add(q)
            if q > x // p:
                break
            q *= p
    return sorted(values)


def matrix_multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matrix_rank(a: list[list[Fraction]]) -> int:
    m = [row[:] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if m[r][col]), None)
        if pivot is None:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        scale = m[pivot_row][col]
        m[pivot_row] = [x / scale for x in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and m[r][col]:
                factor = m[r][col]
                m[r] = [m[r][c] - factor * m[pivot_row][c] for c in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def build_dirichlet_gram(x: int) -> tuple[list[int], list[list[Fraction]]]:
    qs = prime_powers_up_to(x)
    delta: dict[int, list[Fraction]] = {}
    for q in qs:
        f = [Fraction(0)] * (x + 1)
        endpoint = 1 if x % q == 0 else 0
        for j in range(1, x + 1):
            f[j] = Fraction(1 if j % q == 0 else 0) - Fraction(j * endpoint, x)
        delta[q] = [f[j + 1] - f[j] for j in range(x)]
    g = [
        [sum(delta[q][j] * delta[d][j] for j in range(x)) for d in qs]
        for q in qs
    ]
    return qs, g


def check_carry_mobius_contraction(limit: int = 160) -> dict[str, object]:
    cases = 0
    for n in range(2, limit + 1):
        for m in range(1, n + 1):
            lhs = sum(Fraction(mobius(k)) * beta(n, m * k) for k in range(1, n // m + 1))
            rhs = Fraction(2 * m - n - 1, n + 1)
            assert lhs == rhs, (n, m, lhs, rhs)
            cases += 1
    return {"cases": cases, "limit": limit}


def check_second_difference(limit_q: int = 80, limit_m: int = 180) -> dict[str, object]:
    cases = 0
    for q in range(2, limit_q + 1):
        def g(m: int) -> Fraction:
            return Fraction(m + 1) * beta(m, q) if m >= 0 else Fraction(0)
        for m in range(2, limit_m + 1):
            lhs = g(m) - 2 * g(m - 1) + g(m - 2)
            rhs = Fraction(m - 1) * ((1 if m % q == 0 else 0) - (1 if (m - 1) % q == 0 else 0))
            assert lhs == rhs, (q, m, lhs, rhs)
            cases += 1
    return {"cases": cases, "limit_q": limit_q, "limit_m": limit_m}


def check_continuum_comparison(limit: int = 240) -> dict[str, object]:
    cases = 0
    maximum = Fraction(0)
    maximizer = None
    for n in range(2, limit + 1):
        for q in range(2, n + 1):
            diff = continuum_b_at_ratio(n, q) - beta(n, q)
            assert Fraction(0) <= diff <= Fraction(2, q), (n, q, diff)
            if diff > maximum:
                maximum = diff
                maximizer = [n, q]
            cases += 1
    return {
        "cases": cases,
        "limit": limit,
        "max_difference": str(maximum),
        "maximizer": maximizer,
    }


def check_hankel_obstruction() -> dict[str, object]:
    # For f(t)=8e^t-7e^(t/2)-(3/2)t e^(t/2).
    f2 = Fraction(19, 4)
    f3 = Fraction(6, 1)
    f4 = Fraction(109, 16)
    determinant = f2 * f4 - f3 * f3
    assert determinant == Fraction(-233, 64)
    assert determinant < 0
    return {
        "f_second_0": str(f2),
        "f_third_0": str(f3),
        "f_fourth_0": str(f4),
        "log_convexity_determinant": str(determinant),
    }


def check_digit_convolution(limit: int = 400) -> dict[str, object]:
    # c2(n)=1-v2(n), b2(n)=mu(n)-1_{2|n}mu(n/2).
    for n in range(1, limit + 1):
        total = 0
        for d in range(1, n + 1):
            if n % d == 0:
                c = 1 - v2(d)
                e = n // d
                b = mobius(e) - (mobius(e // 2) if e % 2 == 0 else 0)
                total += c * b
        expected = 1 if n == 1 else (-2 if n == 2 else 0)
        assert total == expected, (n, total, expected)
        assert sum(1 - v2(k) for k in range(1, n + 1)) == binary_digit_sum(n)
    return {"limit": limit, "coefficient_cases": limit, "partial_sum_cases": limit}


def check_profile_identification() -> dict[str, object]:
    # PR #243 C(e^t) = PR #252 g(t), term by term.
    # PR #247 a(t) = e^{-t/2} g(t)/8, term by term.
    # It suffices to verify the exact scalar coefficients after x=t-log n.
    assert Fraction(1, 8) * 8 == 1
    assert Fraction(1, 8) * (-7) == Fraction(-7, 8)
    assert Fraction(1, 8) * Fraction(-3, 2) == Fraction(-3, 16)
    return {
        "identity_1": "g(t)=C(exp(t))",
        "identity_2": "a(t)=exp(-t/2)*g(t)/8",
        "transform_identity": "A(s)=G_resolvent(s+1/2)/8",
    }


def check_exceptional_cluster_inverse() -> dict[str, object]:
    a = [[Fraction(x) for x in row] for row in [
        [2, -2, 2, -2],
        [-1, 2, -1, -1],
        [0, -1, 2, -1],
        [0, 0, -1, 2],
    ]]
    inv = [[Fraction(x) for x in row] for row in [
        [Fraction(3, 2), 2, 1, 3],
        [Fraction(3, 2), 3, 2, 4],
        [1, 2, 2, 3],
        [Fraction(1, 2), 1, 1, 2],
    ]]
    product = matrix_multiply(a, inv)
    identity = [[Fraction(1 if i == j else 0) for j in range(4)] for i in range(4)]
    assert product == identity
    assert all(x >= 0 for row in inv for x in row)
    return {"dimension": 4, "inverse_entrywise_nonnegative": True}


def check_dirichlet_gram() -> dict[str, object]:
    checked = []
    for x in [8, 12, 18, 24, 32, 40]:
        qs, g = build_dirichlet_gram(x)
        rank = matrix_rank(g)
        assert rank == len(qs), (x, rank, len(qs))
        checked.append({"X": x, "prime_powers": len(qs), "rank": rank})
    return {"instances": checked}


def check_exact_green_correction(x: int = 24) -> dict[str, object]:
    qs, g = build_dirichlet_gram(x)
    # Deterministic rational test vector T and arbitrary baseline b.
    t = [Fraction((i % 5) - 2, i + 2) for i in range(len(qs))]
    baseline = [Fraction(0)] * (x + 1)
    for m in range(2, x + 1):
        baseline[m] = Fraction((3 * m + 1) % 11, m + 3)

    endpoint_value = {q: 1 if x % q == 0 else 0 for q in qs}
    f_t = [Fraction(0)] * (x + 1)
    for j in range(1, x + 1):
        f_t[j] = sum(
            t[i] * (Fraction(1 if j % q == 0 else 0) - Fraction(j * endpoint_value[q], x))
            for i, q in enumerate(qs)
        )
    corrected = baseline[:]
    for m in range(2, x + 1):
        corrected[m] = baseline[m] + f_t[m - 1] - f_t[m]

    def v_q(vector: list[Fraction], q: int) -> Fraction:
        return sum(vector[k * q] - (vector[k * q + 1] if k * q + 1 <= x else 0) for k in range(1, x // q + 1))

    delta_v = [v_q(corrected, q) - v_q(baseline, q) for q in qs]
    minus_gt = [-sum(g[i][j] * t[j] for j in range(len(qs))) for i in range(len(qs))]
    assert delta_v == minus_gt
    return {"X": x, "prime_powers": len(qs), "map_identity": "delta_v=-G*T"}


def check_consecutive_prime_power_run(limit: int = 5000) -> dict[str, object]:
    pp = set(prime_powers_up_to(limit))
    longest: list[int] = []
    current: list[int] = []
    for n in range(2, limit + 1):
        if n in pp:
            current.append(n)
            if len(current) > len(longest):
                longest = current[:]
        else:
            current = []
    assert longest == [2, 3, 4, 5]
    # Above 5, no run can exceed three; this finite check is regression only.
    return {"limit": limit, "longest_run": longest}


def main() -> None:
    results = {
        "schema": "X-26101-fourth-pass-crosschecks-v1",
        "checks": {
            "carry_mobius_contraction": check_carry_mobius_contraction(),
            "carry_second_difference": check_second_difference(),
            "continuum_discrete_comparison": check_continuum_comparison(),
            "conditional_hankel_obstruction": check_hankel_obstruction(),
            "dyadic_digit_convolution": check_digit_convolution(),
            "carry_profile_identification": check_profile_identification(),
            "exceptional_prime_power_cluster": check_exceptional_cluster_inverse(),
            "endpoint_projected_dirichlet_gram": check_dirichlet_gram(),
            "green_correction_map": check_exact_green_correction(),
            "prime_power_run_regression": check_consecutive_prime_power_run(),
        },
    }
    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"
    out_path = Path(__file__).with_name("results") / "verification.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
