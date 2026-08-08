#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from typing import Iterable, List, Tuple

N = 160


def mobius_sieve(limit: int) -> List[int]:
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


def prime_list(limit: int) -> List[int]:
    out: List[int] = []
    for n in range(2, limit + 1):
        prime = True
        for p in out:
            if p * p > n:
                break
            if n % p == 0:
                prime = False
                break
        if prime:
            out.append(n)
    return out


PRIMES = prime_list(N)
PRIME_WEIGHT = {p: i + 2 for i, p in enumerate(PRIMES)}
MU = mobius_sieve(N)


def factor(n: int) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    for p in PRIMES:
        if p * p > n:
            break
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
    if n > 1:
        out.append((n, 1))
    return out


def ell(n: int) -> int:
    """A formal completely additive logarithm."""
    return sum(PRIME_WEIGHT[p] * e for p, e in factor(n))


def divisors(n: int) -> Iterable[int]:
    for d in range(1, n + 1):
        if n % d == 0:
            yield d


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


def omega(n: int, middle: Fraction = Fraction(-3, 2),
          last: Fraction = Fraction(1, 2)) -> Fraction:
    ans = Fraction(MU[n])
    if n % 2 == 0:
        ans += middle * MU[n // 2]
    if n % 4 == 0:
        ans += last * MU[n // 4]
    return ans


def aomega(n: int) -> Fraction:
    r = v2(n)
    return Fraction(2 * r) + Fraction(1, 2**r)


AOMEGA = [Fraction(0)] + [aomega(n) for n in range(1, N + 1)]


def generalized_moment(omega_values: List[Fraction], power: int) -> List[Fraction]:
    out = [Fraction(0)] * (N + 1)
    for q in range(1, N + 1):
        out[q] = sum(
            omega_values[d] * AOMEGA[q // d] * ell(q // d) ** power
            for d in divisors(q)
        )
    return out


def carry_average(t: Fraction) -> Fraction:
    k = t.numerator // t.denominator
    integral_floor = (
        Fraction(k * (k - 1), 2) + k * (t - k)
    ) / t
    return k - 2 * integral_floor


def b_kernel(X: int, q: int) -> Fraction:
    k = X // q
    return Fraction(k * (q * (k + 1) - X), X)


def beta_kernel(X: int, q: int) -> Fraction:
    k, r = divmod(X, q)
    return Fraction(k * (q - 1 - r), X + 1)


def top_weight(X: int, q: int) -> Fraction:
    if 2 * q > X:
        return Fraction(2 * q, X) - 1
    if 4 * q > X:
        return Fraction(1, 2) - Fraction(4 * q, X)
    return Fraction(0)


def ordinary_lambda(n: int) -> Fraction:
    fs = factor(n)
    if len(fs) == 1:
        p, _ = fs[0]
        return Fraction(PRIME_WEIGHT[p])
    return Fraction(0)


def source_commutator(X: int, source: List[Fraction]) -> Fraction:
    return sum(
        source[n] * (ell(X) - ell(n)) * b_kernel(X, n)
        for n in range(1, X + 1)
    )


def source_second_commutator(X: int, source: List[Fraction]) -> Fraction:
    return sum(
        source[n] * (ell(X) - ell(n)) ** 2 * b_kernel(X, n)
        for n in range(1, X + 1)
    )


def continuum_discrete_boundary(X: int, source: List[Fraction]) -> Fraction:
    return sum(
        source[q] * (ell(X) - ell(q))
        * (b_kernel(X, q) - beta_kernel(X, q))
        for q in range(1, X + 1)
    )


def boundary_formula(X: int) -> Fraction:
    def B(Y: int) -> Fraction:
        return sum(Fraction(n) * ordinary_lambda(n) for n in range(1, Y + 1))

    return Fraction(2, X * (X + 1)) * (
        B(X) - 3 * B(X // 2) + 2 * B(X // 4) - PRIME_WEIGHT[2]
    )


def filter_coefficients(alpha2: int) -> Tuple[Fraction, Fraction, Fraction]:
    def pow2(k: int) -> Fraction:
        return Fraction(2**k) if k >= 0 else Fraction(1, 2**(-k))

    shift1 = pow2((alpha2 - 1) // 2) + pow2((alpha2 - 3) // 2)
    shift2 = pow2(alpha2 - 2)
    return Fraction(1), 1 - shift1, 1 - shift1 + shift2


def check_core(middle: Fraction = Fraction(-3, 2),
               last: Fraction = Fraction(1, 2)) -> dict[str, int]:
    source = [Fraction(0)] + [
        omega(n, middle=middle, last=last) for n in range(1, N + 1)
    ]
    lam = generalized_moment(source, 1)
    selberg = generalized_moment(source, 2)

    inverse_rows = 0
    for n in range(1, N + 1):
        got = sum(source[d] * AOMEGA[n // d] for d in divisors(n))
        if got != (1 if n == 1 else 0):
            raise AssertionError(("inverse", n, got))
        inverse_rows += 1

    average_rows = 0
    for X in range(2, 65):
        for q in range(1, X + 1):
            if carry_average(Fraction(X, q)) != b_kernel(X, q):
                raise AssertionError(("average", X, q))
            average_rows += 1

    selberg_rows = 0
    for q in range(1, N + 1):
        rhs = lam[q] * ell(q) + sum(lam[d] * lam[q // d] for d in divisors(q))
        if selberg[q] != rhs:
            raise AssertionError(("selberg", q, selberg[q], rhs))
        selberg_rows += 1

    commutator_rows = second_rows = boundary_rows = 0
    for X in range(5, N + 1):
        rhs1 = sum(lam[q] * top_weight(X, q) for q in range(1, X + 1))
        lhs1 = source_commutator(X, source)
        if lhs1 != rhs1:
            raise AssertionError(("commutator", X, lhs1, rhs1))
        commutator_rows += 1

        rhs2 = sum(
            (2 * lam[q] * (ell(X) - ell(q)) + selberg[q]) * top_weight(X, q)
            for q in range(1, X + 1)
        )
        lhs2 = source_second_commutator(X, source)
        if lhs2 != rhs2:
            raise AssertionError(("second", X, lhs2, rhs2))
        second_rows += 1

        lhs_b = continuum_discrete_boundary(X, source)
        rhs_b = boundary_formula(X)
        if lhs_b != rhs_b:
            raise AssertionError(("boundary", X, lhs_b, rhs_b))
        boundary_rows += 1

    intervals = (
        (-filter_coefficients(1)[0], 2 * filter_coefficients(3)[0]),
        (-filter_coefficients(1)[1], 2 * filter_coefficients(3)[1]),
        (-filter_coefficients(1)[2], 2 * filter_coefficients(3)[2]),
    )
    expected = (
        (Fraction(-1), Fraction(2)),
        (Fraction(1, 2), Fraction(-4)),
        (Fraction(0), Fraction(0)),
    )
    if intervals != expected:
        raise AssertionError(("filter", intervals, expected))

    transform_rows = 0
    for sigma in (Fraction(k, 7) for k in range(2, 20) if k != 7):
        lhs = Fraction(sigma - 1, sigma * (sigma + 1))
        rhs = -Fraction(1, sigma) + Fraction(2, sigma + 1)
        if lhs != rhs:
            raise AssertionError(("transform", sigma, lhs, rhs))
        transform_rows += 1

    return {
        "inverse_rows": inverse_rows,
        "average_rows": average_rows,
        "commutator_rows": commutator_rows,
        "second_commutator_rows": second_rows,
        "selberg_rows": selberg_rows,
        "transform_rows": transform_rows,
        "boundary_rows": boundary_rows,
    }


def main() -> None:
    central = check_core()
    mutations = [
        (Fraction(-1), Fraction(1, 2)),
        (Fraction(-3, 2), Fraction(0)),
        (Fraction(-5, 4), Fraction(1, 2)),
    ]
    rejected = 0
    for middle, last in mutations:
        try:
            check_core(middle=middle, last=last)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(("mutations", rejected, len(mutations)))

    result = {
        "schema": "riemann.x27601-averaged-carry-commutator.v2",
        "classification": "PASS_EXACT_AVERAGED_CARRY_COMMUTATOR_ALGEBRA",
        **central,
        "mutations_rejected": rejected,
        "proof_boundary": (
            "Finite formal carry/source/commutator/boundary algebra only; "
            "no subpower top-quarter contrast estimate and no RH claim."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = sha256(canonical).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
