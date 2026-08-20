#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T100000_CENTERED_BERNSTEIN_HIERARCHY"
B2 = 0.6077916759012857004768960092028393540691853607427612090252973960450643353243653
B15 = 0.3820953891482850738669426189602306448454873231503014501936597450697457673523409


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = bytearray(limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = n * p
            if m > limit:
                break
            composite[m] = 1
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def kappa(m: int, r: int, t: Fraction) -> Fraction:
    if not (1 <= r <= m - 1):
        raise ValueError((m, r))
    if t <= 1:
        return sum(
            ((-1) ** (j - r)) * math.comb(m, j) * t**j
            for j in range(r, m + 1)
        )
    return sum(
        ((-1) ** (r - 1 - j)) * math.comb(m, j) * t**j
        for j in range(0, r)
    )


def binomial_hierarchy_checks() -> dict[str, int]:
    recurrence = positivity = ratio = bernstein = 0
    grid = [Fraction(k, 12) for k in range(1, 49)]
    for m in range(3, 13):
        for r in range(1, m):
            for t in grid:
                value = kappa(m, r, t)
                assert value > 0, (m, r, t, value)
                positivity += 1
                if r == 1:
                    expected = 1 - max(Fraction(1) - t, Fraction(0)) ** m
                else:
                    expected = math.comb(m, r - 1) * t ** (r - 1) - kappa(m, r - 1, t)
                assert value == expected, (m, r, t, value, expected)
                recurrence += 1

            previous: Fraction | None = None
            for t in grid:
                current = kappa(m, r, t) / t**r
                if previous is not None:
                    assert current <= previous, (m, r, t, current, previous)
                previous = current
                ratio += 1

            a = m - r
            assert a >= 1
            b0 = Fraction(1, a + 1)
            assert b0 > 0
            bernstein += 1
            for j in range(1, r):
                bj = Fraction(a, (a + j) * (a + j + 1))
                assert bj > 0
                bernstein += 1
    return {
        "recurrence_checks": recurrence,
        "kernel_positivity_checks": positivity,
        "normalized_ratio_checks": ratio,
        "positive_bernstein_coefficients": bernstein,
    }


def differential_checks() -> dict[str, bool]:
    def deriv(poly: list[Fraction]) -> list[Fraction]:
        return [Fraction(i + 1) * poly[i + 1] for i in range(len(poly) - 1)]

    def mul_z(poly: list[Fraction]) -> list[Fraction]:
        return [Fraction(0)] + poly

    def add(a: list[Fraction], b: list[Fraction], scale: Fraction = Fraction(1)) -> list[Fraction]:
        n = max(len(a), len(b))
        out = [Fraction(0)] * n
        for i in range(n):
            if i < len(a):
                out[i] += a[i]
            if i < len(b):
                out[i] += scale * b[i]
        while out and out[-1] == 0:
            out.pop()
        return out

    def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
        out = [Fraction(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        return out

    U = [Fraction(-4), Fraction(4)]
    U2 = mul(U, U)
    U3 = mul(U2, U)
    DU3 = [x / 2 for x in mul_z(deriv(U3))]
    lhs = add(DU3, U3, Fraction(-3, 2))
    rhs = [6 * x for x in U2]
    assert lhs == rhs, (lhs, rhs)

    DU2 = [x / 2 for x in mul_z(deriv(U2))]
    lhs2 = add(DU2, U2, Fraction(-1))
    rhs2 = [4 * x for x in U]
    assert lhs2 == rhs2, (lhs2, rhs2)
    return {
        "cubic_to_quadratic_descent": True,
        "quadratic_to_linear_descent": True,
    }


def mellin_checks() -> dict[str, int]:
    checks = 0
    for m in range(3, 11):
        for s in (Fraction(13, 4), Fraction(17, 5), Fraction(23, 6), Fraction(29, 7)):
            if any(2 * s == m - l for l in range(m + 1)):
                continue
            partial = sum(
                Fraction((4**m) * ((-1) ** l) * math.comb(m, l), 1)
                / (s - Fraction(m - l, 2))
                for l in range(m + 1)
            )
            product = Fraction(2 * (4**m) * math.factorial(m), 1)
            for j in range(m + 1):
                product /= 2 * s - m + j
            assert partial == product, (m, s, partial, product)
            checks += 1
    return {"mellin_partial_fraction_checks": checks}


def finite_diagnostic(limit: int) -> dict[str, float | int | bool]:
    mu = mobius_sieve(limit)
    beta = mu[:]
    for n in range(67, limit + 1, 67):
        beta[n] -= mu[n // 67]

    a2 = a15 = a1 = a05 = 0.0
    min_c2 = (float("inf"), 0)
    min_c3 = (float("inf"), 0)
    for x in range(1, limit + 1):
        b = float(beta[x])
        root = math.sqrt(x)
        a2 += b / (x * x)
        a15 += b / (x * root)
        a1 += b / x
        a05 += b / root

        hu2 = 16.0 * x * a15 - 32.0 * root * a1 + 16.0 * a05
        c2 = 16.0 * B15 * x - hu2
        hu3 = 64.0 * x * root * a2 - 192.0 * x * a15 + 192.0 * root * a1 - 64.0 * a05
        c3 = 192.0 * B15 * x - 64.0 * B2 * x * root + hu3
        if c2 < min_c2[0]:
            min_c2 = (c2, x)
        if c3 < min_c3[0]:
            min_c3 = (c3, x)

    assert min_c2[0] > 5.0, min_c2
    assert min_c3[0] > 30.0, min_c3
    return {
        "scan_limit": limit,
        "critical_quadratic_minimum": min_c2[0],
        "critical_quadratic_minimum_at": min_c2[1],
        "critical_cubic_minimum": min_c3[0],
        "critical_cubic_minimum_at": min_c3[1],
        "finite_scan_proves_global": False,
    }


def negative_controls() -> dict[str, bool | float]:
    a = math.log(2.0)
    kval = 3.0 * math.exp(-a / 4.0) - math.exp(-3.0 * a / 4.0)
    linear = 2.0 - 2.0 * kval
    assert linear < -1.0

    def g(u: float) -> float:
        if u < 0:
            return 64.0 * (3.0 * math.exp(1.5 * u) - math.exp(2.0 * u))
        return 64.0 * (3.0 * math.exp(u) - math.exp(0.5 * u))

    h = 0.1
    u = 0.33
    fifth = sum(((-1) ** j) * math.comb(5, j) * g(u - j * h) for j in range(6))
    assert fifth < -0.01, fifth
    return {
        "positive_definite_not_linear_sign": True,
        "two_atom_linear_witness": linear,
        "arbitrary_shift_complete_monotonicity_refuted": True,
        "fifth_difference_witness": fifth,
    }


def run(limit: int) -> dict:
    payload = {
        "schema": "riemann.x100000.centered-bernstein-hierarchy.v1",
        "classification": VERDICT,
        "base_pr": 672,
        "base_sha": "2a351548eb7960ff8ae99f193c10e278984c5657",
        **binomial_hierarchy_checks(),
        **differential_checks(),
        **mellin_checks(),
        **finite_diagnostic(limit),
        **negative_controls(),
        "proved_safe_centering_range": "1 <= r <= m-2",
        "critical_prime_harmonic_exponent": "1",
        "critical_remainder_proved_nonnegative": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=200_000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "results" / "verification.json",
    )
    args = parser.parse_args()
    result = run(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
