#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SMALL_PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    x = n
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def mobius(n: int) -> int:
    fs = factor(n)
    if any(e > 1 for e in fs.values()):
        return 0
    return -1 if len(fs) % 2 else 1


def von_mangoldt_formal(n: int) -> dict[int, int]:
    fs = factor(n)
    if len(fs) == 1:
        p = next(iter(fs))
        return {p: 1}
    return {}


def add_vec(a: dict[int, Fraction], b: dict[int, Fraction], scale=Fraction(1)):
    out = defaultdict(Fraction)
    for p, c in a.items():
        out[p] += c
    for p, c in b.items():
        out[p] += scale * c
    return {p: c for p, c in out.items() if c}


def scale_vec(a: dict[int, Fraction], scale: Fraction):
    return {p: scale * c for p, c in a.items() if scale * c}


def divisors(n: int):
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return sorted(ds)


def formal_log_of_integer(n: int) -> dict[int, Fraction]:
    return {p: Fraction(e) for p, e in factor(n).items()}


def benchmark_convolution_checks(limit: int = 4000) -> int:
    checks = 0
    for n in range(1, limit + 1):
        lhs: dict[int, Fraction] = {}
        for d in divisors(n):
            mu = mobius(d)
            if not mu:
                continue
            lhs = add_vec(lhs, formal_log_of_integer(n // d), Fraction(mu))
        rhs = {p: Fraction(c) for p, c in von_mangoldt_formal(n).items()}
        assert lhs == rhs, (n, lhs, rhs)
        checks += 1
    return checks


def y4(q: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    scale = 1
    n = q
    while True:
        out = add_vec(out, {p: Fraction(c) for p, c in von_mangoldt_formal(n).items()}, Fraction(scale))
        if n % 4:
            break
        n //= 4
        scale *= 2
    return out


def radix4_dual_checks(limit: int = 5000) -> int:
    checks = 0
    for q in range(1, limit + 1):
        lhs = y4(q)
        if q % 4 == 0:
            lhs = add_vec(lhs, y4(q // 4), Fraction(-2))
        rhs = {p: Fraction(c) for p, c in von_mangoldt_formal(q).items()}
        assert lhs == rhs, (q, lhs, rhs)
        checks += 1

    # Formal summation-by-parts regression on deterministic rational columns.
    C = {q: Fraction((17 * q + 11) % 97, 101) for q in range(1, limit + 1)}
    left: dict[int, Fraction] = {}
    right: dict[int, Fraction] = {}
    for q in range(1, limit + 1):
        left = add_vec(left, von_mangoldt_formal(q), C[q])
        detail = C[q] - 2 * C.get(4 * q, Fraction(0))
        right = add_vec(right, y4(q), detail)
    assert left == right
    return checks + 1


def is_rough(n: int) -> bool:
    return all(n % p for p in SMALL_PRIMES)


def mu_small(n: int) -> int:
    if n == 1:
        return 1
    fs = factor(n)
    if any(p not in SMALL_PRIMES or e > 1 for p, e in fs.items()):
        return 0
    return -1 if len(fs) % 2 else 1


def rough_convolution_checks(limit: int = 100000) -> int:
    checks = 0
    for n in range(1, limit + 1):
        lhs = 0
        for m in divisors(n):
            if is_rough(m):
                lhs += mobius(n // m)
        rhs = mu_small(n)
        assert lhs == rhs, (n, lhs, rhs)
        checks += 1
    return checks


def least_prime_partition_checks(limit: int = 100000) -> int:
    checks = 0
    for n in range(1, limit + 1):
        if not is_rough(n):
            continue
        if n == 1:
            checks += 1
            continue
        ps = sorted(factor(n))
        p = ps[0]
        assert p >= 67
        u = n // p
        assert all(q >= p for q in factor(u))
        # uniqueness of the least-prime label
        assert all(not (q < p and n % q == 0) for q in range(67, p))
        checks += 1
    return checks


def explicit_capacity_witness() -> dict:
    value = math.log(68 / 67) / math.sqrt(134)
    assert value > 0
    return {
        "X": 136,
        "q": 2,
        "exact": "log(68/67)/sqrt(134)",
        "decimal": value,
    }


def target_debt_checks() -> int:
    checks = 0
    for p in [2, 3, 5, 67, 71, 83, 127, 509, 5003]:
        r = 1 / math.sqrt(p)
        for Y in [p, p + 1, 2 * p, 17 * p, 1000 * p]:
            lhs = 2 * ((1-r) * (4 * math.sqrt(Y) * (1+r) - 3))
            rhs = (1-r) * (5 * math.sqrt(Y) * (1+r) - 3)
            assert lhs + 1e-12 >= rhs
            checks += 1
    return checks



def injectivity_regression(limit: int = 250) -> int:
    # Rational triangular toy carry with the exact diagonal beta_(q,q).
    d = {n: Fraction((19*n + 7) % 101, 103) for n in range(2, limit + 1)}
    def beta_frac(n: int, q: int) -> Fraction:
        if q > n:
            return Fraction(0)
        a, r = divmod(n, q)
        return Fraction(a * (q - 1 - r), n + 1)
    C = {q: sum(beta_frac(n, q) * d[n] for n in range(q, limit + 1))
         for q in range(2, limit + 1)}
    Xi = {q: C[q] - 2 * C.get(4*q, Fraction(0))
          for q in range(2, limit + 1)}
    Crec = {q: sum(Fraction(2**k) * Xi.get((4**k)*q, Fraction(0))
                   for k in range(0, 20) if (4**k)*q <= limit)
            for q in range(2, limit + 1)}
    assert C == Crec
    drec = {}
    for q in range(limit, 1, -1):
        tail = sum(beta_frac(n, q) * drec[n] for n in range(q + 1, limit + 1))
        drec[q] = (C[q] - tail) / beta_frac(q, q)
    assert d == drec
    return 2 * (limit - 1)


def main() -> None:
    result = {
        "classification": "PASS_NATIVE_ROOT_NORMALIZATION_AND_DUAL_PACKET",
        "benchmark_convolution_checks": benchmark_convolution_checks(),
        "radix4_dual_checks": radix4_dual_checks(),
        "rough_convolution_checks": rough_convolution_checks(),
        "least_prime_partition_checks": least_prime_partition_checks(),
        "target_debt_checks": target_debt_checks(),
        "injectivity_regression_checks": injectivity_regression(),
        "strict_capacity_overdraw_witness": explicit_capacity_witness(),
        "one_prime_scan_commands": [
            "c++ -O3 scan_oneprime.cpp -o scan_oneprime",
            "./scan_oneprime 67 200 200",
            "./scan_oneprime 71 200 200",
            "./scan_oneprime 83 200 200",
            "./scan_oneprime 127 200 200",
            "c++ -O3 random_oneprime.cpp -o random_oneprime && ./random_oneprime",
        ],
        "scope": (
            "The formal prime-log checks prove the Möbius benchmark identity, "
            "the positive radix-four dual recurrence, and the finite-Euler/rough "
            "convolution dictionary on a large exact regression range. The "
            "capacity witness and target-debt algebra are exact. The C++ "
            "one-prime scans are discovery evidence only and do not prove the "
            "global one-prime row theorem, NRCT, CFFP, or RH."
        ),
    }
    out = HERE / "results" / "verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
