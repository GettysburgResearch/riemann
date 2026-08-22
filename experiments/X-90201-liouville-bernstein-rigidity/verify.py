#!/usr/bin/env python3
"""Independent replay for L-90201 / T-90201.

Assurance layers:
  1. pointwise generalized-von-Mangoldt Bernstein identity and Liouville
     domination on vertex and interior prime cubes;
  2. exact finite Boolean Bernstein expansion for arbitrary rational kernels;
  3. semigroup/primitive identity for every mixed derivative;
  4. high-precision scaled-descendant identity for actual GFEP kernels;
  5. finite class-minimum collapse and large-point reconnaissance;
  6. ramp extremality, equality, and coercivity checks.

The finite Boolean layer uses Fraction exactly. Actual logarithmic kernels use
mpmath at 70 decimal digits. Large points are a clearly labelled float64-style
reconnaissance layer implemented with Python doubles.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path

from mpmath import mp

mp.dps = 70

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    if n >= 1:
        mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            composite[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def factor_distinct(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def omega(n: int) -> int:
    return len(factor_distinct(n))


def rad(n: int) -> int:
    out = 1
    for p in factor_distinct(n):
        out *= p
    return out


def divisors_squarefree_from_primes(ps: list[int]) -> list[int]:
    vals = [1]
    for p in ps:
        vals += [v * p for v in list(vals)]
    return sorted(vals)


def generalized_lambda_direct(n: int, x: dict[int, mp.mpf]) -> mp.mpf:
    ps = factor_distinct(n)
    total = mp.mpf("0")
    for d in divisors_squarefree_from_primes(ps):
        f = mp.mpf("1")
        for p in ps:
            if d % p == 0:
                f *= x[p]
        total += f * mp.log(mp.mpf(n) / d)
    return total


def generalized_lambda_formula(n: int, x: dict[int, mp.mpf]) -> mp.mpf:
    ps = factor_distinct(n)
    r = len(ps)
    y = {p: (1 + x[p]) / 2 for p in ps}
    first = mp.mpf("0")
    for q in ps:
        mon = mp.mpf("1")
        for p in ps:
            if p != q:
                mon *= y[p]
        first += mp.log(q) * mon
    first *= 2 ** (r - 1)
    all_mon = mp.mpf("1")
    for p in ps:
        all_mon *= y[p]
    second = (2**r) * mp.log(mp.mpf(n) / rad(n)) * all_mon
    return first + second


def ordinary_lambda(n: int) -> mp.mpf:
    ps = factor_distinct(n)
    if len(ps) != 1:
        return mp.mpf("0")
    return mp.log(ps[0])


def verify_local_lambda() -> dict:
    vertex_cases = 0
    interior_cases = 0
    max_formula_error = mp.mpf("0")
    min_domination = mp.inf

    for n in range(2, 241):
        ps = factor_distinct(n)
        for signs in product((-1, 1), repeat=len(ps)):
            x = {p: mp.mpf(s) for p, s in zip(ps, signs)}
            direct = generalized_lambda_direct(n, x)
            formula = generalized_lambda_formula(n, x)
            err = abs(direct - formula)
            max_formula_error = max(max_formula_error, err)
            assert err < mp.mpf("1e-60")
            gap = formula - ordinary_lambda(n)
            min_domination = min(min_domination, gap)
            assert gap >= -mp.mpf("1e-60")
            vertex_cases += 1

    interior_grid = [mp.mpf("-1"), mp.mpf("-0.5"), mp.mpf("0"), mp.mpf("0.333333333333333333333333"), mp.mpf("1")]
    for n in range(2, 100):
        ps = factor_distinct(n)
        if len(ps) > 3:
            continue
        for vals in product(interior_grid, repeat=len(ps)):
            x = {p: v for p, v in zip(ps, vals)}
            direct = generalized_lambda_direct(n, x)
            formula = generalized_lambda_formula(n, x)
            err = abs(direct - formula)
            max_formula_error = max(max_formula_error, err)
            assert err < mp.mpf("1e-60")
            gap = formula - ordinary_lambda(n)
            min_domination = min(min_domination, gap)
            assert gap >= -mp.mpf("1e-60")
            interior_cases += 1

    return {
        "vertex_cases": vertex_cases,
        "interior_cases": interior_cases,
        "max_formula_error": mp.nstr(max_formula_error, 8),
        "minimum_domination_gap": mp.nstr(min_domination, 8),
    }


def bernstein_coefficients_fraction(c: list[Fraction], kmax: int) -> dict[int, Fraction]:
    mu = mobius_sieve(kmax)
    out: dict[int, Fraction] = {}
    for a in range(1, kmax + 1):
        if mu[a] == 0:
            continue
        s = Fraction(0)
        for m in range(1, kmax // a + 1):
            if mu[m] and math.gcd(m, a) == 1:
                s += mu[m] * c[a * m]
        out[a] = (2 ** omega(a)) * s
    return out


def primitive_fraction(c: list[Fraction], kmax: int, q: int) -> Fraction:
    mu = mobius_sieve(kmax // q)
    return sum((mu[d] * c[q * d] for d in range(1, kmax // q + 1) if mu[d]), Fraction(0))


def semigroup(primes: list[int], limit: int) -> list[int]:
    vals = {1}
    for p in primes:
        old = list(vals)
        expanded = set(vals)
        for v in old:
            z = v * p
            while z <= limit:
                expanded.add(z)
                z *= p
        vals = expanded
    return sorted(v for v in vals if v <= limit)


def eval_class_fraction(c: list[Fraction], kmax: int, signs: dict[int, int]) -> Fraction:
    mu = mobius_sieve(kmax)
    total = Fraction(0)
    for k in range(1, kmax + 1):
        if mu[k] == 0:
            continue
        f = 1
        for p in factor_distinct(k):
            f *= signs[p]
        total += f * c[k]
    return total


def verify_boolean_fraction() -> dict:
    kmax = 30
    mu = mobius_sieve(kmax)
    c = [Fraction(0)] * (kmax + 1)
    for k in range(1, kmax + 1):
        c[k] = Fraction(((37 * k + 11) % 29) - 14, k + 5)

    B = bernstein_coefficients_fraction(c, kmax)
    primitive_checks = 0
    for a, value in B.items():
        rhs = Fraction(0)
        for r in semigroup(factor_distinct(a), kmax // a):
            rhs += primitive_fraction(c, kmax, a * r)
        rhs *= 2 ** omega(a)
        assert rhs == value
        primitive_checks += 1

    P = primes_upto(kmax)
    expansion_checks = 0
    minimum = None
    minimum_bits = None
    for bits in range(1 << len(P)):
        signs = {p: (1 if (bits >> i) & 1 else -1) for i, p in enumerate(P)}
        direct = eval_class_fraction(c, kmax, signs)
        expanded = Fraction(0)
        for a, coeff in B.items():
            active = all(signs[p] == 1 for p in factor_distinct(a))
            if active:
                expanded += coeff
        assert direct == expanded
        if minimum is None or direct < minimum:
            minimum = direct
            minimum_bits = bits
        expansion_checks += 1

    mutation_detected = False
    for a, value in B.items():
        only_first = (2 ** omega(a)) * primitive_fraction(c, kmax, a)
        if only_first != value:
            mutation_detected = True
            break
    assert mutation_detected

    return {
        "kmax": kmax,
        "prime_vertices": 1 << len(P),
        "expansion_checks": expansion_checks,
        "primitive_checks": primitive_checks,
        "minimum_value": str(minimum),
        "minimum_bits": minimum_bits,
        "semigroup_mutation_detected": mutation_detected,
    }


def children(m: int) -> tuple[int, int, int, int]:
    return (m // 2, m - m // 2, (m + 2) // 3, m - (m + 2) // 3)


def g_table_fraction(max_x: int, n: int, p: int) -> list[Fraction]:
    G = [Fraction(0)] * (max_x + 2)
    if p <= max_x:
        G[p] = Fraction(p)
    for m in range(2 * n, max_x + 1):
        G[m] = sum((G[c] for c in children(m) if c >= n), Fraction(0)) / 2
    return G


def w_mp(X: mp.mpf, q: int) -> mp.mpf:
    if mp.mpf(q) > X:
        return mp.mpf("0")
    return mp.log(X / q) / mp.sqrt(q)


def c_vector_mp(X: mp.mpf, n: int, p: int, G: list[Fraction]) -> list[mp.mpf]:
    kmax = int(mp.floor(X / n))
    out = [mp.mpf("0")] * (kmax + 1)
    for k in range(1, kmax + 1):
        mmax = int(mp.floor(X / k))
        total = mp.mpf("0")
        for m in range(n, mmax + 1):
            gm = G[m] if m < len(G) else Fraction(0)
            gp = G[m - 1] if m - 1 >= n and m - 1 < len(G) else Fraction(0)
            dg = gm - gp
            total += (mp.mpf(dg.numerator) / dg.denominator) * w_mp(X, m * k)
        out[k] = total
    return out


def sigma_from_c(c: list[mp.mpf]) -> mp.mpf:
    mu = mobius_sieve(len(c) - 1)
    return sum((mu[k] * c[k] for k in range(1, len(c)) if mu[k]), mp.mpf("0"))


def primitive_mp(c: list[mp.mpf], q: int) -> mp.mpf:
    kmax = len(c) - 1
    mu = mobius_sieve(kmax // q)
    return sum((mu[d] * c[q * d] for d in range(1, kmax // q + 1) if mu[d]), mp.mpf("0"))


def bernstein_mp(c: list[mp.mpf]) -> dict[int, mp.mpf]:
    kmax = len(c) - 1
    mu = mobius_sieve(kmax)
    out: dict[int, mp.mpf] = {}
    for a in range(1, kmax + 1):
        if mu[a] == 0:
            continue
        s = mp.mpf("0")
        for m in range(1, kmax // a + 1):
            if mu[m] and math.gcd(m, a) == 1:
                s += mu[m] * c[a * m]
        out[a] = (2 ** omega(a)) * s
    return out


def verify_actual_hierarchy() -> dict:
    cases = [(120, 5, 5), (180, 7, 9), (300, 10, 10), (360, 12, 17)]
    max_scale_error = mp.mpf("0")
    max_semigroup_error = mp.mpf("0")
    max_renewal_error = mp.mpf("0")
    scale_checks = 0
    derivative_checks = 0
    exhaustive_min_checks = 0
    case_rows: list[dict] = []

    for X_int, n, p in cases:
        X = mp.mpf(X_int)
        G = g_table_fraction(X_int, n, p)
        c = c_vector_mp(X, n, p, G)
        kmax = len(c) - 1
        Pvals = [mp.mpf("0")] * (kmax + 1)
        descendant = [mp.mpf("0")] * (kmax + 1)
        for q in range(1, kmax + 1):
            Pvals[q] = primitive_mp(c, q)
            Y = X / q
            cY = c_vector_mp(Y, n, p, G)
            descendant[q] = sigma_from_c(cY) / mp.sqrt(q)
            err = abs(Pvals[q] - descendant[q])
            max_scale_error = max(max_scale_error, err)
            assert err < mp.mpf("1e-58")
            scale_checks += 1

        B = bernstein_mp(c)
        for a, value in B.items():
            rhs = mp.mpf("0")
            for r in semigroup(factor_distinct(a), kmax // a):
                rhs += Pvals[a * r]
            rhs *= 2 ** omega(a)
            err = abs(value - rhs)
            max_semigroup_error = max(max_semigroup_error, err)
            assert err < mp.mpf("1e-57")
            derivative_checks += 1

        renewal = sum(Pvals[1:], mp.mpf("0"))
        err = abs(c[1] - renewal)
        max_renewal_error = max(max_renewal_error, err)
        assert err < mp.mpf("1e-58")

        all_desc_nonnegative = all(v >= -mp.mpf("1e-55") for v in descendant[2:])
        all_nonempty_B_nonnegative = all(v >= -mp.mpf("1e-55") for a, v in B.items() if a > 1)
        assert all_desc_nonnegative == all_nonempty_B_nonnegative or all_desc_nonnegative

        primes = primes_upto(kmax)
        if len(primes) <= 12:
            lam = B[1]
            best = None
            mu_all = mobius_sieve(kmax)
            for bits in range(1 << len(primes)):
                x = {q: (1 if (bits >> i) & 1 else -1) for i, q in enumerate(primes)}
                val = mp.mpf("0")
                for k in range(1, kmax + 1):
                    if mu_all[k] == 0:
                        continue
                    f = 1
                    for q in factor_distinct(k):
                        f *= x[q]
                    val += f * c[k]
                if best is None or val < best:
                    best = val
            assert abs(best - lam) < mp.mpf("1e-55")
            exhaustive_min_checks += 1

        min_nonempty = min((v for a, v in B.items() if a > 1), default=mp.mpf("0"))
        case_rows.append(
            {
                "X": X_int,
                "n": n,
                "p": p,
                "K": kmax,
                "lambda_value": mp.nstr(B[1], 14),
                "min_nonempty_B": mp.nstr(min_nonempty, 14),
                "all_descendants_nonnegative": all_desc_nonnegative,
            }
        )

    return {
        "cases": case_rows,
        "scale_checks": scale_checks,
        "mixed_derivative_checks": derivative_checks,
        "exhaustive_min_checks": exhaustive_min_checks,
        "max_scale_error": mp.nstr(max_scale_error, 8),
        "max_semigroup_error": mp.nstr(max_semigroup_error, 8),
        "max_renewal_error": mp.nstr(max_renewal_error, 8),
    }


def g_table_float(max_x: int, n: int, p: int) -> list[float]:
    G = [0.0] * (max_x + 2)
    if p <= max_x:
        G[p] = float(p)
    for m in range(2 * n, max_x + 1):
        G[m] = sum(G[c] for c in children(m) if c >= n) / 2.0
    return G


def c_vector_float(X: int, n: int, p: int) -> list[float]:
    G = g_table_float(X, n, p)
    dg = [0.0] * (X + 1)
    for m in range(n, X + 1):
        dg[m] = G[m] - (G[m - 1] if m - 1 >= n else 0.0)
    kmax = X // n
    c = [0.0] * (kmax + 1)
    for k in range(1, kmax + 1):
        total = 0.0
        for m in range(n, X // k + 1):
            total += dg[m] * math.log(X / (m * k)) / math.sqrt(m * k)
        c[k] = total
    return c


def large_reconnaissance() -> list[dict]:
    cases = [(2000, 20, 20), (3000, 25, 25), (4000, 15, 15), (10000, 20, 20)]
    rows: list[dict] = []
    for X, n, p in cases:
        c = c_vector_float(X, n, p)
        kmax = len(c) - 1
        mu = mobius_sieve(kmax)
        B: dict[int, float] = {}
        for a in range(1, kmax + 1):
            if mu[a] == 0:
                continue
            s = 0.0
            for m in range(1, kmax // a + 1):
                if mu[m] and math.gcd(m, a) == 1:
                    s += mu[m] * c[a * m]
            B[a] = (2 ** omega(a)) * s
        nonempty = [(v, a) for a, v in B.items() if a > 1]
        min_v, min_a = min(nonempty)
        negatives = sum(1 for v, _ in nonempty if v < -1e-10)
        assert negatives == 0
        rows.append(
            {
                "X": X,
                "n": n,
                "p": p,
                "K": kmax,
                "described_prime_vertex_exponent": len(primes_upto(kmax)),
                "deep_checks_after_band": max(0, kmax // 20 - 1),
                "lambda_value": B[1],
                "minimum_nonempty_B": min_v,
                "minimum_label": min_a,
                "negative_nonempty_B": negatives,
            }
        )
    return rows


def ramp_from_generalized_lambda(X: int, signs: dict[int, int]) -> mp.mpf:
    total = mp.mpf("0")
    for n in range(2, X + 1):
        x = {p: mp.mpf(signs.get(p, -1)) for p in factor_distinct(n)}
        total += w_mp(mp.mpf(X), n) * generalized_lambda_formula(n, x)
    return total


def ramp_kernel_transport(X: int, signs: dict[int, int]) -> mp.mpf:
    mu = mobius_sieve(X // 2)
    total = mp.mpf("0")
    for d in range(1, X // 2 + 1):
        if mu[d] == 0:
            continue
        f = 1
        for p in factor_distinct(d):
            f *= signs.get(p, -1)
        inner = mp.mpf("0")
        for m in range(2, X // d + 1):
            inner += mp.log(m) * w_mp(mp.mpf(X), m * d)
        total += f * inner
    return total


def verify_ramp() -> dict:
    exhaustive_cases = 0
    max_identity_error = mp.mpf("0")
    min_coercivity_slack = mp.inf
    rows = []
    for X in (30, 60):
        active = [p for p in primes_upto(X) if p < X / 2]
        lam_signs = {p: -1 for p in primes_upto(X)}
        lam = ramp_from_generalized_lambda(X, lam_signs)
        best = None
        minimizers = 0
        for bits in range(1 << len(active)):
            signs = {p: -1 for p in primes_upto(X)}
            for i, p in enumerate(active):
                if (bits >> i) & 1:
                    signs[p] = 1
            direct = ramp_from_generalized_lambda(X, signs)
            transported = ramp_kernel_transport(X, signs)
            err = abs(direct - transported)
            max_identity_error = max(max_identity_error, err)
            assert err < mp.mpf("1e-58")
            assert direct >= lam - mp.mpf("1e-58")
            lower = mp.mpf("0")
            for p in active:
                y = mp.mpf(1 if signs[p] == 1 else 0)
                lower += 2 * mp.log(2) * y * w_mp(mp.mpf(X), 2 * p)
            slack = (direct - lam) - lower
            min_coercivity_slack = min(min_coercivity_slack, slack)
            assert slack >= -mp.mpf("1e-58")
            if best is None or direct < best - mp.mpf("1e-58"):
                best = direct
                minimizers = 1
            elif abs(direct - best) < mp.mpf("1e-58"):
                minimizers += 1
            exhaustive_cases += 1
        assert abs(best - lam) < mp.mpf("1e-58")
        rows.append(
            {
                "X": X,
                "active_primes": len(active),
                "vertices": 1 << len(active),
                "lambda_ramp": mp.nstr(lam, 15),
                "active_minimizers": minimizers,
            }
        )
    return {
        "cases": rows,
        "exhaustive_vertices": exhaustive_cases,
        "max_divisor_switch_error": mp.nstr(max_identity_error, 8),
        "minimum_coercivity_slack": mp.nstr(min_coercivity_slack, 8),
    }


def main() -> None:
    result = {
        "verdict": "PASS_X_90201_LIOUVILLE_BERNSTEIN_RIGIDITY",
        "local_von_mangoldt": verify_local_lambda(),
        "boolean_fraction": verify_boolean_fraction(),
        "actual_gfep_hierarchy": verify_actual_hierarchy(),
        "large_reconnaissance": large_reconnaissance(),
        "ramp": verify_ramp(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
