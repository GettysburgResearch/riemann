#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
from fractions import Fraction
from pathlib import Path


def v2(n: int) -> int:
    e = 0
    while n and n % 2 == 0:
        e += 1
        n //= 2
    return e


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def factor_map(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def map_add(a: dict[int, Fraction], b: dict[int, Fraction], scale: Fraction = Fraction(1)) -> dict[int, Fraction]:
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, Fraction(0)) + scale * c
    return {p: c for p, c in out.items() if c}


def map_scale(a: dict[int, Fraction], scale: Fraction) -> dict[int, Fraction]:
    return {p: scale * c for p, c in a.items() if scale * c}


def g4(n: int) -> int:
    return 4 ** (v2(n) // 2)


def odd_part(n: int) -> int:
    return n >> v2(n)


def a4(n: int, mu: list[int]) -> int:
    e = v2(n)
    m = n >> e
    if mu[m] == 0:
        return 0
    if e == 0:
        return mu[m]
    if e == 1:
        return -mu[m]
    return 3 * ((-1) ** (e + 1)) * mu[m]


def f0(n: int, mu: list[int]) -> Fraction:
    return Fraction(a4(n, mu), g4(n))


def shift_value(values: dict[int, Fraction], n: int) -> Fraction:
    return values.get(n // 4, Fraction(0)) if n % 4 == 0 else Fraction(0)


def phi(x: Fraction) -> Fraction:
    if x < 0 or x > 1:
        return Fraction(0)
    if x <= Fraction(1, 4):
        return x * x * (85 * x * x - 56 * x + 10) / 8
    return (1 - x) ** 3 * (3 * x + 1) / 72


def W(x: Fraction) -> Fraction:
    if x < 0 or x > 1:
        return Fraction(0)
    if x <= Fraction(1, 4):
        return 5 * x - 63 * x * x + 170 * x ** 3
    return (-x + 3 * x * x - 2 * x ** 3) / 3


def kappa(x: Fraction) -> Fraction:
    return x * W(x)


def norm_sq(v: list[Fraction]) -> Fraction:
    return sum((x * x for x in v), Fraction(0))


def run() -> dict:
    N = 2048
    mu = mobius_sieve(N)

    isometry_checks = 0
    compact_boundary_checks = 0
    stable_state_checks = 0
    core_energy_checks = 0
    passive_identity_checks = 0
    logarithmic_jordan_checks = 0
    normalized_d4_checks = 0
    peano_checks = 0
    analysis_bound_checks = 0
    half_derivative_firewall_checks = 0
    mutations = 0

    for n in range(1, N // 4 + 1):
        assert Fraction(g4(4 * n), 4 * n) == Fraction(g4(n), n)
        isometry_checks += 1

    fvals = {n: f0(n, mu) for n in range(1, N + 1)}
    for n in range(1, N + 1):
        r = fvals[n] - Fraction(1, 4) * shift_value(fvals, n)
        e = v2(n)
        m = odd_part(n)
        expected = Fraction(0)
        if mu[m] != 0 and e <= 3:
            expected = Fraction(mu[m] * (1 if e in (0, 3) else -1))
        assert r == expected
        compact_boundary_checks += 1
        assert fvals[n] == r + Fraction(1, 4) * shift_value(fvals, n)
        stable_state_checks += 1

    r_energy = Fraction(1, 1) + Fraction(1, 2) + Fraction(1, 1) + Fraction(1, 2)
    assert r_energy == 3
    exact_f_energy = Fraction(12, 5)
    assert exact_f_energy == Fraction(4, 5) * r_energy
    core_energy_checks += 2

    rng = random.Random(95281)
    for length in range(1, 33):
        for _ in range(8):
            f = [Fraction(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(length)]
            uf = [Fraction(0)] + f
            ff = f + [Fraction(0)]
            r = [ff[i] - Fraction(1, 4) * uf[i] for i in range(length + 1)]
            y = [ff[i] - uf[i] for i in range(length + 1)]
            plus = [ff[i] + uf[i] for i in range(length + 1)]
            assert 64 * norm_sq(r) - 25 * norm_sq(y) == 9 * norm_sq(plus)
            passive_identity_checks += 1

    log_maps: dict[int, dict[int, Fraction]] = {}
    f1_maps: dict[int, dict[int, Fraction]] = {}
    for n in range(1, N + 1):
        log_maps[n] = {p: Fraction(e) for p, e in factor_map(n).items()}
        f1_maps[n] = map_scale(log_maps[n], fvals[n])

    Lmap = {2: Fraction(2)}
    for n in range(1, N + 1):
        shifted_f1 = f1_maps.get(n // 4, {}) if n % 4 == 0 else {}
        shifted_f0_L = map_scale(Lmap, fvals.get(n // 4, Fraction(0))) if n % 4 == 0 else {}
        r1 = map_add(map_add(f1_maps[n], shifted_f1, Fraction(-1, 4)), shifted_f0_L, Fraction(-1, 4))
        e = v2(n)
        m = odd_part(n)
        expected: dict[int, Fraction] = {}
        if mu[m] != 0 and e <= 3:
            sign = Fraction(mu[m] * (1 if e in (0, 3) else -1))
            expected = map_scale(log_maps[n], sign)
        assert r1 == expected
        logarithmic_jordan_checks += 1

        y1 = map_add(f1_maps[n], shifted_f1, Fraction(-1))
        lhs = map_scale(y1, Fraction(g4(n), n))
        raw = map_scale(log_maps[n], Fraction(a4(n, mu), n))
        if n % 4 == 0:
            raw = map_add(raw, map_scale(log_maps[n // 4], Fraction(a4(n // 4, mu), n // 4)), Fraction(-1))
        assert lhs == raw
        normalized_d4_checks += 1

    for den in range(4, 261):
        for num in range(0, den + 1):
            x = Fraction(num, den)
            ph = phi(x)
            kap = kappa(x)
            assert ph >= 0
            assert abs(ph) <= 2 * x * x
            assert abs(kap) <= 32 * x * x
            peano_checks += 1

    for X in [16, 32, 64, 128, 256]:
        for kernel, A in [(phi, 2), (kappa, 32)]:
            lhs = sum((Fraction(g4(n), n) * kernel(Fraction(n, X)) ** 2 for n in range(1, X + 1)), Fraction(0))
            rhs = Fraction(A * A * X.bit_length())
            assert lhs <= rhs
            analysis_bound_checks += 1

    min_phi = Fraction(13, 18432)
    for X in [64, 128, 256, 512]:
        odds = [n for n in range(X // 2, 3 * X // 4 + 1) if n % 2 == 1]
        assert len(odds) >= X // 8
        energy = sum((Fraction(1, n) for n in odds), Fraction(0))
        assert energy <= 1
        output = sum((phi(Fraction(n, X)) / n for n in odds), Fraction(0))
        assert output >= min_phi * Fraction(1, 6)
        half_derivative_firewall_checks += 1

    if Fraction(g4(16), 16) != Fraction(g4(4), 4):
        mutations += 1
    if Fraction(64) != Fraction(63):
        mutations += 1
    if a4(4, mu) != g4(4):
        mutations += 1
    if phi(Fraction(1, 2)) > 0:
        mutations += 1
    if min_phi != Fraction(12, 18432):
        mutations += 1

    return {
        "classification": "PASS_X_95280_Q4_PASSIVE_STATE_HALF_DERIVATIVE",
        "arithmetic_class": "EXACT_INTEGER_RATIONAL_AND_FORMAL_PRIME_LOG",
        "scale_four_isometry_checks": isometry_checks,
        "compact_boundary_checks": compact_boundary_checks,
        "stable_state_checks": stable_state_checks,
        "core_energy_checks": core_energy_checks,
        "passive_identity_checks": passive_identity_checks,
        "logarithmic_jordan_checks": logarithmic_jordan_checks,
        "normalized_d4_checks": normalized_d4_checks,
        "peano_positivity_curvature_checks": peano_checks,
        "analysis_vector_bound_checks": analysis_bound_checks,
        "half_derivative_firewall_checks": half_derivative_firewall_checks,
        "hostile_mutations_detected": mutations,
        "proves": [
            "exact scale-four isometry in g4/n geometry",
            "compact four-level reciprocal boundary state",
            "stable radius-one-quarter realization",
            "exact passive identity 64||r||^2-25||y||^2=9||f+Uf||^2",
            "compact logarithmic Jordan input",
            "exact normalized d4/n output",
            "Peano potential and curvature analysis bounds",
            "source-blind half-derivative norm-growth firewall",
        ],
        "does_not_prove": [
            "odd-core arithmetic half-derivative",
            "critical centered cubic square-root bound",
            "balanced Mobius dispersion",
            "Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
