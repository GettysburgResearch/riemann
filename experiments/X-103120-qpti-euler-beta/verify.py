#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb
import hashlib
import json

PRIMES = (2, 3, 5, 7, 11, 13)


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def integrate_one_minus_theta(poly: list[Fraction]) -> Fraction:
    return sum(
        value * Fraction(1, (degree + 1) * (degree + 2))
        for degree, value in enumerate(poly)
    )


def beta_identity() -> tuple[int, Fraction]:
    z = {p: Fraction(1, p + 1) for p in PRIMES}
    direct = Fraction(0)
    term_count = 0
    for depth in range(len(PRIMES) + 1):
        for c_tuple in combinations(PRIMES, depth):
            core_set = set(c_tuple)
            core = Fraction(1)
            for prime in core_set:
                core *= z[prime] ** 2
            remaining = [p for p in PRIMES if p not in core_set]
            for p, q in combinations(remaining, 2):
                direct_coeff = Fraction((-1) ** depth, comb(depth + 2, 2))
                beta_coeff = 2 * Fraction(1, (depth + 1) * (depth + 2))
                assert direct_coeff == ((-1) ** depth) * beta_coeff
                direct += direct_coeff * z[p] * z[q] * core
                term_count += 1

    polynomial = [Fraction(0)]
    for p, q in combinations(PRIMES, 2):
        factor = [Fraction(1)]
        for prime in PRIMES:
            if prime in (p, q):
                continue
            factor = poly_mul(factor, [Fraction(1), -(z[prime] ** 2)])
        if len(polynomial) < len(factor):
            polynomial.extend([Fraction(0)] * (len(factor) - len(polynomial)))
        scale = 2 * z[p] * z[q]
        for degree, value in enumerate(factor):
            polynomial[degree] += scale * value

    beta = integrate_one_minus_theta(polynomial)
    assert direct == beta
    return term_count, direct


def coefficientwise_count() -> int:
    checks = 0
    prime_count = len(PRIMES)
    for mask in range(1 << prime_count):
        support = {PRIMES[i] for i in range(prime_count) if mask & (1 << i)}
        if len(support) < 2:
            continue
        depth = len(support)
        native = Fraction((-1) ** depth)
        shares = Fraction(0)
        for _ in combinations(sorted(support), 2):
            shares += Fraction((-1) ** depth, comb(depth, 2))
            checks += 1
        assert shares == native
    return checks


def live_owner_mode_check() -> tuple[int, Fraction]:
    core = {2, 3}
    z = {p: Fraction(1, p + 1) for p in PRIMES}
    owner = Fraction(0)
    for p, q in combinations([r for r in PRIMES if r not in core], 2):
        owner += z[p] * z[q]
    mode = Fraction(1, comb(len(core) + 2, 2))
    for prime in core:
        mode *= z[prime] ** 2
    mode *= owner
    assert owner > 0 and mode > 0
    return comb(len(PRIMES) - len(core), 2), mode


def vaughan_boolean_checks() -> int:
    checks = 0
    products: dict[int, tuple[int, int]] = {}
    for mask in range(1 << len(PRIMES)):
        product = 1
        depth = 0
        for i, prime in enumerate(PRIMES):
            if mask & (1 << i):
                product *= prime
                depth += 1
        products[mask] = (product, depth)

    def star(f: dict[int, int], g: dict[int, int]) -> dict[int, int]:
        out: dict[int, int] = {}
        for mask in products:
            total = 0
            sub = mask
            while True:
                other = mask ^ sub
                total += f.get(sub, 0) * g.get(other, 0)
                if sub == 0:
                    break
                sub = (sub - 1) & mask
            out[mask] = total
        return out

    one = {mask: 1 for mask in products}
    epsilon = {mask: int(mask == 0) for mask in products}
    mu = {mask: (-1) ** products[mask][1] for mask in products}

    for cutoff in (1, 2, 5, 11, 30, 100, 1000):
        mu_u = {
            mask: mu[mask] * int(products[mask][0] <= cutoff)
            for mask in products
        }
        mu_u_star_one = star(mu_u, one)
        a_u = {mask: epsilon[mask] - mu_u_star_one[mask] for mask in products}
        type_i_first = {mask: 2 * mu_u[mask] for mask in products}
        type_i_second = star(star(mu_u, mu_u), one)
        balanced = star(star(a_u, a_u), mu)
        for mask in products:
            rhs = type_i_first[mask] - type_i_second[mask] + balanced[mask]
            assert rhs == mu[mask]
            checks += 1
    return checks


def main() -> None:
    beta_terms, beta_value = beta_identity()
    owner_share_checks = coefficientwise_count()
    live_pairs, live_value = live_owner_mode_check()
    vaughan_checks = vaughan_boolean_checks()

    proof = {
        "schema": "riemann.t103120.qpti.euler_beta.v1",
        "beta_terms": beta_terms,
        "beta_value": [beta_value.numerator, beta_value.denominator],
        "owner_share_checks": owner_share_checks,
        "live_core_owner_pairs": live_pairs,
        "live_core_mode": [live_value.numerator, live_value.denominator],
        "vaughan_boolean_checks": vaughan_checks,
        "euler_beta_identity": True,
        "live_owner_mode_nonzero": True,
        "quarter_power_cancels_owner_mode_combinatorially": False,
        "qpti_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
    proof["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    proof["verdict"] = "PASS_T103120_QPTI_EULER_BETA_REDUCTION"
    print(json.dumps(proof, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
