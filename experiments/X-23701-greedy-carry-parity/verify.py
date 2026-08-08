#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from typing import Dict, List, Tuple


def beta(n: int, q: int) -> Fraction:
    if not (2 <= q <= n):
        return Fraction(0)
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def carry_count(n: int, q: int) -> int:
    return sum(1 for j in range(n + 1) if (j % q) > (n % q))


def vp_factorial(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def digit_sum(n: int, base: int = 2) -> int:
    if n < 0 or base < 2:
        raise ValueError("invalid digit-sum input")
    total = 0
    while n:
        total += n % base
        n //= base
    return total


def mobius_values(limit: int) -> List[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: List[int] = []
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


def b2_values(limit: int) -> List[int]:
    mu = mobius_values(limit)
    b2 = [0] * (limit + 1)
    for n in range(1, limit + 1):
        b2[n] = mu[n] - (mu[n // 2] if n % 2 == 0 else 0)
    return b2


def parity_convolution(N: int, b2: List[int]) -> int:
    return sum(b2[m] for m in range(1, N + 1) if (N // m) % 2 == 1)


def digit_convolution(N: int, b2: List[int]) -> int:
    return sum(b2[m] * digit_sum(N // m, 2) for m in range(1, N + 1))


def mobius_collapsed_entry(n: int, m: int, mu: List[int]) -> Fraction:
    return sum(
        (Fraction(mu[k]) * beta(n, m * k) for k in range(1, n // m + 1)),
        Fraction(0),
    )


def adjoint_inverse(
    X: int,
    target: Dict[int, Fraction],
) -> Dict[int, Fraction]:
    mu = mobius_values(X)
    u = [Fraction(0) for _ in range(X + 3)]
    for m in range(2, X + 1):
        u[m] = sum(
            (Fraction(mu[k]) * target[m * k] for k in range(1, X // m + 1)),
            Fraction(0),
        )
    tail = [Fraction(0) for _ in range(X + 4)]
    for m in range(X, 1, -1):
        tail[m] = tail[m + 1] + u[m]
    coefficients: Dict[int, Fraction] = {}
    for j in range(2, X + 1):
        numerator = (
            (j + 1) * (j * u[j] - (j - 2) * u[j + 1])
            + 2 * tail[j + 2]
        )
        coefficients[j] = numerator / (j * (j - 1))
    return coefficients


def greedy_minorant(
    X: int,
    target: Dict[int, Fraction],
) -> Tuple[Dict[int, Fraction], Dict[int, Fraction], Dict[int, int]]:
    residual = {q: target[q] for q in range(2, X + 1)}
    coefficients: Dict[int, Fraction] = {}
    blockers: Dict[int, int] = {}

    for n in range(X, 1, -1):
        candidates: List[Tuple[Fraction, int]] = []
        for q in range(2, n + 1):
            entry = beta(n, q)
            if entry > 0:
                candidates.append((residual[q] / entry, q))
        if not candidates:
            raise AssertionError(f"no positive carry entry in row {n}")
        value, blocker = min(candidates, key=lambda item: (item[0], item[1]))
        if value < 0:
            raise AssertionError(f"negative greedy coefficient at row {n}")
        coefficients[n] = value
        blockers[n] = blocker
        for q in range(2, n + 1):
            residual[q] -= value * beta(n, q)
            if residual[q] < 0:
                raise AssertionError(f"negative residual at stage {n}, q={q}")

    return coefficients, residual, blockers


def synthetic_greedy_result(X: int = 24) -> Dict[str, object]:
    # A rational decreasing target with the same triangular endpoint geometry as
    # q^(-1/2) log(X/q), used only to replay the finite greedy algebra exactly.
    target = {q: Fraction(X - q, q * X) for q in range(2, X + 1)}
    coefficients, residual, blockers = greedy_minorant(X, target)
    adjoint = adjoint_inverse(X, target)
    adjoint_mismatches = sum(
        1 for n in range(2, X + 1) if adjoint[n] != coefficients[n]
    )

    reconstructed = {
        q: sum(coefficients[n] * beta(n, q) for n in range(q, X + 1))
        for q in range(2, X + 1)
    }
    slacks = {q: target[q] - reconstructed[q] for q in range(2, X + 1)}
    if any(value < 0 for value in slacks.values()):
        raise AssertionError("synthetic greedy vector is infeasible")
    if any(value < 0 for value in coefficients.values()):
        raise AssertionError("synthetic greedy coefficient is negative")

    mass = sum(Fraction(n) * coefficients[n] for n in coefficients)
    coefficient_mass = sum(coefficients.values(), Fraction(0))
    return {
        "synthetic_endpoint": X,
        "synthetic_min_coefficient": str(min(coefficients.values())),
        "synthetic_min_slack": str(min(slacks.values())),
        "synthetic_mass": str(mass),
        "synthetic_coefficient_mass": str(coefficient_mass),
        "synthetic_non_diagonal_blockers": sum(
            1 for n, q in blockers.items() if n != q
        ),
        "synthetic_adjoint_inverse_mismatches": adjoint_mismatches,
        "synthetic_discrete_convexity_failures": sum(
            1 for value in adjoint.values() if value < 0
        ),
    }


def build_result() -> Dict[str, object]:
    carry_checks = 0
    binary_kummer_checks = 0
    for n in range(2, 25):
        for q in range(2, n + 1):
            expected = Fraction(carry_count(n, q), n + 1)
            if beta(n, q) != expected:
                raise AssertionError(f"carry count mismatch n={n}, q={q}")
            carry_checks += 1
        for j in range(n + 1):
            lhs = (
                vp_factorial(n, 2)
                - vp_factorial(j, 2)
                - vp_factorial(n - j, 2)
            )
            rhs = digit_sum(j, 2) + digit_sum(n - j, 2) - digit_sum(n, 2)
            if lhs != rhs:
                raise AssertionError(f"binary Kummer mismatch n={n}, j={j}")
            binary_kummer_checks += 1

    mu = mobius_values(24)
    mobius_collapse_checks = 0
    for n in range(2, 25):
        for m in range(2, n + 1):
            expected = Fraction(2 * m - n - 1, n + 1)
            if mobius_collapsed_entry(n, m, mu) != expected:
                raise AssertionError(f"Mobius row collapse mismatch n={n}, m={m}")
            mobius_collapse_checks += 1

    digital_limit = 512
    b2 = b2_values(digital_limit)
    parity_rows: Dict[str, int] = {}
    digit_rows: Dict[str, int] = {}
    sample_points = {1, 2, 3, 4, 16, 64, 256, 512}
    for N in range(1, digital_limit + 1):
        parity = parity_convolution(N, b2)
        digit = digit_convolution(N, b2)
        parity_expected = 1 if N == 1 else (-2 if N <= 3 else 0)
        digit_expected = 1 if N == 1 else -1
        if parity != parity_expected:
            raise AssertionError(f"parity identity mismatch N={N}: {parity}")
        if digit != digit_expected:
            raise AssertionError(f"digit identity mismatch N={N}: {digit}")
        if N in sample_points:
            parity_rows[str(N)] = parity
            digit_rows[str(N)] = digit

    result: Dict[str, object] = {
        "schema": "X-23701-v1",
        "carry_count_checks": carry_checks,
        "binary_kummer_checks": binary_kummer_checks,
        "mobius_row_collapse_checks": mobius_collapse_checks,
        "digital_identity_limit": digital_limit,
        "parity_rows": parity_rows,
        "digit_rows": digit_rows,
    }
    result.update(synthetic_greedy_result())
    result["verdict"] = "SYNTHETIC_GREEDY_CARRY_PARITY_ALGEBRA_VERIFIED"
    result["scope"] = (
        "exact finite algebra and rational synthetic greedy feasibility only; "
        "does not verify logarithmic target asymptotics, DBT, or RH"
    )
    return result


def main() -> None:
    print(json.dumps(build_result(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
