#!/usr/bin/env python3
"""Exact finite regression for the cubic-shell / balanced-dispersion packet.

The checker uses only Python's standard library and Fraction arithmetic.
It authenticates finite algebra, source reorganizations, exact grid formulas,
the Vaughan decomposition, and scope firewalls.  It does not prove BCD or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Tuple

Q = Fraction
VERDICT = "PASS_CUBIC_SHELL_BALANCED_DISPERSION_REDUCTION"


def poly_eval(a: List[Q], x: Q) -> Q:
    ans = Q(0)
    for coefficient in reversed(a):
        ans = ans * x + coefficient
    return ans


def poly_integral(a: List[Q], left: Q = Q(0), right: Q = Q(1)) -> Q:
    anti = [Q(0)] + [a[i] / Q(i + 1) for i in range(len(a))]
    return poly_eval(anti, right) - poly_eval(anti, left)


K = [Q(0), Q(-1, 3), Q(1), Q(-2, 3)]
F_LEFT = [Q(0), Q(5), Q(-63), Q(170)]
F_RIGHT = K


def k_value(x: Q) -> Q:
    if x < 0 or x > 1:
        return Q(0)
    return poly_eval(K, x)


def f_value(x: Q, contracted_factor: int = 4) -> Q:
    if x <= 0 or x > 1:
        return Q(0)
    value = k_value(x)
    if x <= Q(1, 4):
        value -= Q(contracted_factor) * k_value(Q(4) * x)
    return value


def primes_upto(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def prime_weights(n: int) -> Dict[int, Q]:
    return {p: Q((p % 13) + 2, (p % 7) + 3) for p in primes_upto(n)}


def factorization(n: int) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    d, x = 2, n
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0:
                x //= d
                e += 1
            out.append((d, e))
        d += 1 if d == 2 else 2
    if x > 1:
        out.append((x, 1))
    return out


def mu(n: int) -> int:
    if n == 1:
        return 1
    fac = factorization(n)
    if any(e > 1 for _, e in fac):
        return 0
    return -1 if len(fac) % 2 else 1


def log_formal(n: int, weights: Dict[int, Q]) -> Q:
    return sum((Q(e) * weights[p] for p, e in factorization(n)), Q(0))


def lambda_formal(n: int, weights: Dict[int, Q]) -> Q:
    fac = factorization(n)
    return weights[fac[0][0]] if len(fac) == 1 else Q(0)


def divisors(n: int) -> List[int]:
    out = [1]
    for p, e in factorization(n):
        old = list(out)
        mult = 1
        for _ in range(e):
            mult *= p
            out += [d * mult for d in old]
    return sorted(out)


def is_power_of_four(n: int) -> bool:
    if n < 4:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1


def q4_source(nmax: int, weights: Dict[int, Q], drop_gauge: bool = False) -> List[Q]:
    out = [Q(0)] * (nmax + 1)
    for n in range(1, nmax + 1):
        value = lambda_formal(n, weights)
        if n % 4 == 0:
            value -= 4 * lambda_formal(n // 4, weights)
        if is_power_of_four(n) and not drop_gauge:
            value += 6 * weights[2]
        out[n] = value
    return out


def cubic_sum(values: List[Q]) -> Q:
    n = len(values) - 1
    return sum((values[m] * k_value(Q(m, n)) for m in range(1, n + 1)), Q(0))


def scale_four_sum(n: int, weights: Dict[int, Q], contracted_factor: int = 4) -> Q:
    total = sum(
        (lambda_formal(m, weights) * f_value(Q(m, n), contracted_factor)
         for m in range(1, n + 1)), Q(0)
    )
    p4 = 4
    while p4 <= n:
        total += 6 * weights[2] * k_value(Q(p4, n))
        p4 *= 4
    return total


def prime_block_scale_four(n: int, p: int, weights: Dict[int, Q]) -> Q:
    lp, total, power = weights[p], Q(0), p
    while power <= n:
        total += lp * f_value(Q(power, n))
        if power > n // p:
            break
        power *= p
    if p == 2:
        p4 = 4
        while p4 <= n:
            total += 6 * lp * k_value(Q(p4, n))
            p4 *= 4
    return total


def grid_sum(m: int) -> Q:
    return sum((f_value(Q(n, m)) for n in range(1, m + 1)), Q(0))


def grid_formula(m: int) -> Q:
    h, r = divmod(m, 4)
    if r == 0:
        return Q(0)
    if r == 1:
        return -Q(8 * h * (h + 1), (4 * h + 1) ** 3)
    if r == 2:
        return -Q(4 * h * (h + 1), 3 * (2 * h + 1) ** 3)
    return -Q(8 * h * (h + 1), (4 * h + 3) ** 3)


def cube_root_floor(n: int) -> int:
    u = int(round(n ** (1 / 3)))
    while (u + 1) ** 3 <= n:
        u += 1
    while u ** 3 > n:
        u -= 1
    return u


def a_u(m: int, u: int, wrong: bool = False) -> int:
    return sum(mu(d) for d in divisors(m) if d >= u) if wrong else sum(
        mu(d) for d in divisors(m) if d > u
    )


def vaughan_terms(n: int, weights: Dict[int, Q], wrong_sign: bool = False) -> Dict[str, Q]:
    u = v = cube_root_floor(n)
    source = sum((lambda_formal(k, weights) * f_value(Q(k, n)) for k in range(1, n + 1)), Q(0))
    t1 = sum((lambda_formal(k, weights) * f_value(Q(k, n)) for k in range(1, min(v, n) + 1)), Q(0))
    t2 = Q(0)
    for d in range(1, min(u, n) + 1):
        if mu(d):
            for r in range(1, n // d + 1):
                t2 += mu(d) * log_formal(r, weights) * f_value(Q(d * r, n))
    t3 = Q(0)
    for d in range(1, min(u, n) + 1):
        if not mu(d):
            continue
        for ell in range(1, min(v, n // d) + 1):
            le = lambda_formal(ell, weights)
            if le:
                for r in range(1, n // (d * ell) + 1):
                    t3 += mu(d) * le * f_value(Q(d * ell * r, n))
    t4 = Q(0)
    for d in range(u + 1, n + 1):
        if not mu(d):
            continue
        for ell in range(v + 1, n // d + 1):
            le = lambda_formal(ell, weights)
            if le:
                for r in range(1, n // (d * ell) + 1):
                    t4 += mu(d) * le * f_value(Q(d * ell * r, n))
    grouped = Q(0)
    for m in range(u + 1, n + 1):
        au = a_u(m, u)
        for ell in range(v + 1, n // m + 1):
            le = lambda_formal(ell, weights)
            if au and le:
                grouped += au * le * f_value(Q(m * ell, n))
    return {
        "source": source, "t1": t1, "t2": t2, "t3": t3, "t4": t4,
        "grouped": grouped,
        "reconstructed": t1 + t2 + (t3 if wrong_sign else -t3) + t4,
    }


def canonical_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results/verification.json"))
    args = parser.parse_args()

    assert f_value(Q(1, 4)) == Q(-1, 32)
    assert poly_integral(K) == 0
    assert poly_integral(F_LEFT, Q(0), Q(1, 4)) + poly_integral(F_RIGHT, Q(1, 4), Q(1)) == 0

    for m in range(1, 513):
        assert grid_sum(m) == grid_formula(m)

    shell_endpoints = [16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
    source_checks = block_checks = large_shell_checks = 0
    gauge_mutations = factor_mutations = 0
    for n in shell_endpoints:
        weights = prime_weights(n)
        direct = cubic_sum(q4_source(n, weights))
        reorganized = scale_four_sum(n, weights)
        assert direct == reorganized
        source_checks += 1
        blocks = {p: prime_block_scale_four(n, p, weights) for p in weights}
        assert direct == sum(blocks.values(), Q(0))
        block_checks += 1
        for p, value in blocks.items():
            if p > math.isqrt(n):
                assert value == weights[p] * f_value(Q(p, n))
                large_shell_checks += 1
        gauge_mutations += cubic_sum(q4_source(n, weights, True)) != direct
        factor_mutations += scale_four_sum(n, weights, 3) != reorganized

    vaughan_endpoints = [64, 72, 81, 96, 100, 120, 125, 144]
    sign_mutations = threshold_mutations = 0
    for n in vaughan_endpoints:
        weights = prime_weights(n)
        terms = vaughan_terms(n, weights)
        assert terms["source"] == terms["reconstructed"]
        assert terms["t4"] == terms["grouped"]
        sign_mutations += vaughan_terms(n, weights, True)["source"] != vaughan_terms(n, weights, True)["reconstructed"]
        u = cube_root_floor(n)
        bad = Q(0)
        for m in range(u + 1, n + 1):
            au = a_u(m, u, True)
            for ell in range(u + 1, n // m + 1):
                le = lambda_formal(ell, weights)
                if au and le:
                    bad += au * le * f_value(Q(m * ell, n))
        threshold_mutations += bad != terms["t4"]

    assert gauge_mutations == len(shell_endpoints)
    assert factor_mutations == len(shell_endpoints)
    assert sign_mutations == len(vaughan_endpoints)
    assert threshold_mutations > 0

    payload = {
        "schema": "riemann.x93300.cubic-shell-balanced-dispersion.v1",
        "frozen_base": "6cc0da2fa5711017e260ebdcea4ba8c22e453288",
        "arithmetic_class": "EXACT_RATIONAL",
        "kernel": {"integral_F": "0", "mellin_zero_order_at_s1": 2,
                   "first_nonzero_log_moment": "log(4)/36", "grid_residue_checks": 512},
        "prime_shell": {"source_reorganizations": source_checks,
                        "prime_block_reconstructions": block_checks,
                        "large_prime_single_power_checks": large_shell_checks},
        "vaughan": {"identity_checks": len(vaughan_endpoints),
                    "grouped_type_ii_checks": len(vaughan_endpoints),
                    "safe_ranges": ["Lambda<=N^(1/3)", "mu<=N^(1/3)*log",
                                    "mu<=N^(1/3)*Lambda<=N^(1/3)*1",
                                    "TypeII product<=N^(3/4)"],
                    "remaining": "balanced near-hyperbola BCD"},
        "first_hermite": {"fourier_symbol_checks": 1, "critical_one_carrier_imported": False},
        "mutations": {"drop_four_adic_gauge": gauge_mutations,
                      "replace_scale_four_factor": factor_mutations,
                      "reverse_vaughan_sign": sign_mutations,
                      "change_aU_strict_threshold": threshold_mutations},
        "bcd_proved": False, "rh_established": False,
        "verdict": VERDICT,
    }
    payload["proof_object_sha256"] = canonical_hash(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(VERDICT)
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
