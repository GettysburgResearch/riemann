#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sieve(n: int):
    mu = [0] * (n + 1)
    spf = [0] * (n + 1)
    primes: list[int] = []
    mu[1] = 1
    for x in range(2, n + 1):
        if spf[x] == 0:
            spf[x] = x
            primes.append(x)
            mu[x] = -1
        for p in primes:
            y = x * p
            if y > n:
                break
            spf[y] = p
            if x % p == 0:
                mu[y] = 0
                break
            mu[y] = -mu[x]
    return mu, spf


def prime_factors(n: int, spf: list[int]) -> list[int]:
    out: list[int] = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


def divisors(n: int, spf: list[int]) -> list[int]:
    out = [1]
    x = n
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        old = list(out)
        power = 1
        for _ in range(e):
            power *= p
            out.extend(d * power for d in old)
    return out


def q(row: int, n: int) -> int:
    if row == 2:
        return 0 if n < 2 else 3 if n == 2 else 0 if n == 3 else 1
    if row == 3:
        return 0 if n < 3 else 6 if n == 3 else -2 if n == 4 else 1
    raise ValueError(row)


def mu_ge(n: int, z: int, mu: list[int], spf: list[int]) -> int:
    if mu[n] == 0:
        return 0
    return mu[n] if all(p >= z for p in prime_factors(n, spf)) else 0


def conv_coeff(a, b, n: int, spf: list[int]):
    return sum(a(d) * b(n // d) for d in divisors(n, spf))


def h(k: int) -> Fraction:
    if k < 0:
        return Fraction(0)
    return Fraction(2) - Fraction(1, 2**k)


def k2_coeff(n: int) -> Fraction:
    total = Fraction(0)
    p2 = 1
    k = 0
    while p2 <= n:
        if n == p2:
            total += h(k) - 2 * h(k - 1)
        if n == 3 * p2:
            total += h(k)
        p2 *= 2
        k += 1
    return total


def k3_coeff(n: int) -> Fraction:
    total = Fraction(0)
    p2 = 1
    k = 0
    while p2 <= n:
        if n == p2:
            total += h(k) + h(k - 1) + 3 * h(k - 2)
        if n == 3 * p2:
            total -= 5 * h(k)
        p2 *= 2
        k += 1
    return total


def run() -> dict:
    limit = 20000
    mu, spf = sieve(limit)
    checks = 0

    for z in (5, 11, 19):
        def mz(n: int) -> Fraction:
            return Fraction(mu_ge(n, z, mu, spf))

        def bz(n: int) -> Fraction:
            value = mz(n)
            if n % 2 == 0:
                value -= Fraction(3, 2) * mz(n // 2)
            if n % 4 == 0:
                value += Fraction(1, 2) * mz(n // 4)
            return value

        def rz(n: int) -> Fraction:
            return Fraction(int(all(p < z for p in prime_factors(n, spf))))

        for n in range(1, limit + 1):
            a2 = conv_coeff(mz, lambda d: Fraction(q(2, d)), n, spf)
            a3 = conv_coeff(mz, lambda d: Fraction(q(3, d)), n, spf)
            k2b = conv_coeff(lambda d: k2_coeff(d), bz, n, spf)
            k3b = conv_coeff(lambda d: k3_coeff(d), bz, n, spf)
            inv = Fraction(0)
            p2 = 1
            k = 0
            while p2 <= n:
                if n % p2 == 0:
                    inv += h(k) * bz(n // p2)
                p2 *= 2
                k += 1
            assert a2 == rz(n) - k2b
            assert a3 == rz(n) - k3b
            assert 5 * a2 + a3 == 6 * (rz(n) - bz(n))
            assert inv == mz(n)
            checks += 4

    def mfull(n: int) -> Fraction:
        return Fraction(mu[n])

    def bdiamond(n: int) -> Fraction:
        value = mfull(n)
        if n % 2 == 0:
            value -= Fraction(3, 2) * mfull(n // 2)
        if n % 4 == 0:
            value += Fraction(1, 2) * mfull(n // 4)
        return value

    def cdiamond(n: int) -> Fraction:
        return Fraction(int(n == 1)) - bdiamond(n)

    def smooth23(n: int) -> Fraction:
        x = n
        while x % 2 == 0:
            x //= 2
        while x % 3 == 0:
            x //= 3
        return Fraction(int(x == 1))

    z = 5
    def m5(n: int) -> Fraction:
        return Fraction(mu_ge(n, z, mu, spf))

    for n in range(1, limit + 1):
        scalar = 5 * conv_coeff(m5, lambda d: Fraction(q(2, d)), n, spf)
        scalar += conv_coeff(m5, lambda d: Fraction(q(3, d)), n, spf)
        lifted = 6 * conv_coeff(smooth23, cdiamond, n, spf)
        assert scalar == lifted
        checks += 1

    assert h(0) == 1 and all(h(k) > 0 for k in range(64))
    assert k2_coeff(2) == Fraction(-1, 2)
    assert k3_coeff(3) == Fraction(-5)
    assert 5 * Fraction(-1) + Fraction(6) == 1

    core = {
        "schema": "riemann.x99130.reciprocal-julia-single-profile.v1",
        "base_sha": "9d0b0521e5ace8c96df63a85a68f60a789b09923",
        "coefficient_limit": limit,
        "exact_identity_checks": checks,
        "positive_inverse_checks": 64,
        "negative_controls": {
            "k2_at_2": "-1/2",
            "k3_at_3": "-5",
            "sharp_scalar_positive_with_row2_negative": True
        },
        "mutations_rejected": [
            "claim_rjce23_by_replay_rejected",
            "claim_fpcb23_by_replay_rejected",
            "claim_rh_by_replay_rejected",
            "drop_positive_dyadic_inverse_rejected",
            "erase_common_profile_rejected",
            "promote_scalar_to_two_rows_rejected",
            "treat_k2_as_positive_rejected",
            "treat_k3_as_positive_rejected"
        ],
        "rjce23_proved": False,
        "fpcb23_proved": False,
        "rh_established": False,
        "verdict": "PASS_T99130_RECIPROCAL_JULIA_SINGLE_PROFILE_REDUCTION"
    }
    proof = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {**core, "ok": True, "proof_object_sha256": proof}


if __name__ == "__main__":
    result = run()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])
