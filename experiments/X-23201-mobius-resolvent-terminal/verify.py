#!/usr/bin/env python3
"""Exact finite regressions for the Möbius-resolvent terminal-contraction proposal."""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction

SCHEMA = "riemann.x23201-mobius-resolvent-terminal.v1"


class VerificationError(ValueError):
    pass


def mobius_table(limit: int) -> list[int]:
    if limit < 1:
        raise VerificationError("limit must be positive")
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


def dirichlet_convolution(a: list[int], b: list[int], limit: int) -> list[int]:
    out = [0] * (limit + 1)
    for d in range(1, limit + 1):
        if a[d] == 0:
            continue
        for m in range(1, limit // d + 1):
            if b[m]:
                out[d * m] += a[d] * b[m]
    return out


def add_vectors(a: list[int], b: list[int]) -> list[int]:
    if len(a) != len(b):
        raise VerificationError("vector length mismatch")
    return [x + y for x, y in zip(a, b)]


def ceil_kth_root(x: int, k: int) -> int:
    if x < 1 or k < 1:
        raise VerificationError("invalid root arguments")
    lo, hi = 1, max(2, x)
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**k >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def verify_resolvent(xmax: int = 60, order: int = 4) -> dict[str, object]:
    mu = mobius_table(xmax)
    v = ceil_kth_root(xmax, order)
    eps = [0] * (xmax + 1)
    eps[1] = 1
    one = [0] + [1] * xmax
    mu_v = [0] * (xmax + 1)
    for n in range(1, min(v, xmax) + 1):
        mu_v[n] = mu[n]
    one_mu_v = dirichlet_convolution(one, mu_v, xmax)
    r = [eps[n] - one_mu_v[n] for n in range(xmax + 1)]
    if any(r[n] != 0 for n in range(1, min(v, xmax) + 1)):
        raise VerificationError("resolvent support gate failed")

    total = [0] * (xmax + 1)
    power = eps
    for _ in range(order):
        total = add_vectors(total, dirichlet_convolution(mu_v, power, xmax))
        power = dirichlet_convolution(power, r, xmax)

    mismatches = [n for n in range(1, xmax + 1) if total[n] != mu[n]]
    if mismatches:
        raise VerificationError(f"resolvent mismatch at {mismatches[:5]}")

    nonzero_r = [n for n in range(1, xmax + 1) if r[n]]
    return {
        "xmax": xmax,
        "order": order,
        "cutoff_v": v,
        "first_residual_support": min(nonzero_r) if nonzero_r else None,
        "mismatch_count": 0,
    }


def mertens(mu: list[int], x: Fraction) -> int:
    if x < 1:
        return 0
    n = min(len(mu) - 1, x.numerator // x.denominator)
    return sum(mu[1 : n + 1])


def geometric_difference(
    mu: list[int], x: Fraction, order: int, ratio: Fraction
) -> int:
    return sum(
        (-1) ** j
        * math.comb(order, j)
        * mertens(mu, x * ratio**j)
        for j in range(order + 1)
    )


def reconstruct_mertens(
    mu: list[int], x: Fraction, order: int, ratio: Fraction
) -> int:
    total = 0
    j = 0
    y = x
    while y >= 1:
        total += math.comb(order + j - 1, j) * geometric_difference(
            mu, y, order, ratio
        )
        j += 1
        y *= ratio
        if j > 10000:
            raise VerificationError("geometric inversion did not terminate")
    return total


def verify_geometric_inversion(limit: int = 200) -> dict[str, object]:
    mu = mobius_table(limit)
    ratio = Fraction(2, 3)
    checks = 0
    for order in range(1, 6):
        for n in range(1, limit + 1):
            got = reconstruct_mertens(mu, Fraction(n), order, ratio)
            want = mertens(mu, Fraction(n))
            if got != want:
                raise VerificationError(
                    f"difference inversion mismatch order={order}, n={n}"
                )
            checks += 1
    return {
        "ratio": [ratio.numerator, ratio.denominator],
        "orders": 5,
        "integer_points": limit,
        "checks": checks,
    }


def ldl_positive_semidefinite(matrix: list[list[Fraction]]) -> bool:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise VerificationError("matrix is not square")
    a = [row[:] for row in matrix]
    for k in range(n):
        if a[k][k] < 0:
            return False
        if a[k][k] == 0:
            if any(a[k][j] != 0 for j in range(k + 1, n)):
                return False
            continue
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(i, n):
                a[j][i] = a[i][j] = a[i][j] - a[i][k] * a[j][k] / pivot
        for i in range(k + 1, n):
            a[i][k] = a[k][i] = Fraction(0)
    return True


def quadratic(matrix: list[list[Fraction]], vector: list[Fraction]) -> Fraction:
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def verify_terminal_adapter() -> dict[str, object]:
    k = [
        [Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(2)],
    ]
    f = [
        [Fraction(3), Fraction(1)],
        [Fraction(1), Fraction(3)],
    ]
    lower = [
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    domination = [
        [f[i][j] + lower[i][j] - k[i][j] for j in range(2)]
        for i in range(2)
    ]
    if not ldl_positive_semidefinite(k):
        raise VerificationError("terminal kernel is not PSD")
    if not ldl_positive_semidefinite(f):
        raise VerificationError("Hankel majorant is not PSD")
    if not ldl_positive_semidefinite(domination):
        raise VerificationError("terminal kernel domination failed")

    v = [Fraction(1), Fraction(-1)]
    terminal_energy = quadratic(k, v)
    hankel_energy = quadratic(f, v)
    forcing = Fraction(5)
    linear_reserve = Fraction(1)
    if forcing - linear_reserve != hankel_energy:
        raise VerificationError("Selberg forcing ledger mismatch")
    if terminal_energy > forcing - linear_reserve:
        raise VerificationError("terminal energy is not paid")

    terminal = Fraction(7)
    lower_scale = Fraction(5)
    e0 = terminal + lower_scale
    e1 = 2 * e0 + lower_scale
    e2 = 3 * e1 + lower_scale
    closed = 6 * terminal + 10 * lower_scale
    if e2 != closed:
        raise VerificationError("complexity elimination mismatch")

    return {
        "terminal_energy": [terminal_energy.numerator, terminal_energy.denominator],
        "hankel_energy": [hankel_energy.numerator, hankel_energy.denominator],
        "forcing": [forcing.numerator, forcing.denominator],
        "linear_reserve": [linear_reserve.numerator, linear_reserve.denominator],
        "complexity_closed_value": [closed.numerator, closed.denominator],
    }


def proof_digest(payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def verify() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_PROPOSAL_REGRESSION",
        "mobius_resolvent": verify_resolvent(),
        "geometric_difference": verify_geometric_inversion(),
        "terminal_adapter": verify_terminal_adapter(),
        "proof_boundary": (
            "Exact finite algebra only. This does not prove the source-specific "
            "terminal Selberg-Hankel contraction STC(K), its vanishing rate, or RH."
        ),
    }
    payload["proof_object_sha256"] = proof_digest(payload)
    return payload


def main() -> int:
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
