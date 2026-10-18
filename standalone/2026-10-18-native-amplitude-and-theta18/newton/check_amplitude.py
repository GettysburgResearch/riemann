#!/usr/bin/env python3
"""Exact finite replay for the native low-product amplitude decomposition.

No floating-point logarithm or Euler-constant oracle is used. Logarithms
of integers are represented by their prime-exponent vectors; gamma is a
separate formal symbol. Infinite inequalities are proved in PROOF.md.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json


COUNTS = Counter()


def require(condition, category, message):
    COUNTS[category] += 1
    if not condition:
        raise ValueError(f"{category}: {message}")


def factor_trial(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mu_trial(n):
    f = factor_trial(n)
    return 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)


def tau(n):
    out = 1
    for e in factor_trial(n).values():
        out *= e + 1
    return out


def mu_sieve(n):
    """Separate Euler sieve, not a call to the prefix factorization."""
    values = [0] * (n + 1)
    values[1] = 1
    primes = []
    composite = [False] * (n + 1)
    for a in range(2, n + 1):
        if not composite[a]:
            primes.append(a)
            values[a] = -1
        for p in primes:
            if a * p > n:
                break
            composite[a * p] = True
            if a % p == 0:
                values[a * p] = 0
                break
            values[a * p] = -values[a]
    return values


class Form:
    """Rational linear form in 1, gamma and log(prime)."""
    def __init__(self, terms=None):
        if isinstance(terms, (int, Q)):
            terms = {"one": Q(terms)}
        self.terms = {k: Q(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def cast(value):
        return value if isinstance(value, Form) else Form(value)

    def __add__(self, other):
        out = self.terms.copy()
        for k, v in self.cast(other).terms.items():
            out[k] = out.get(k, Q(0)) + v
        return Form(out)

    __radd__ = __add__

    def __neg__(self):
        return Form({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, scalar):
        scalar = Q(scalar)
        return Form({k: scalar * v for k, v in self.terms.items()})

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (Q(1) / scalar)

    def __eq__(self, other):
        return self.terms == self.cast(other).terms


GAMMA = Form({"gamma": 1})


def log_integer(n):
    if n < 1:
        raise ValueError("log argument must be a positive integer")
    return Form({f"log_{p}": e for p, e in factor_trial(n).items()})


def harmonic(n):
    return sum((Q(1, j) for j in range(1, n + 1)), Q(0))


def remainder(k, d):
    return Form(harmonic(k // d)) - log_integer(k) + log_integer(d) - GAMMA


def integer_root(n, degree):
    lo, hi = 0, 1
    while hi ** degree <= n:
        hi *= 2
    while lo + 1 < hi:
        middle = (lo + hi) // 2
        if middle ** degree <= n:
            lo = middle
        else:
            hi = middle
    require(lo ** degree <= n < (lo + 1) ** degree,
            "integer-root", "exact rational-power cutoff")
    return lo


def u(d, k):
    return Q(d - 1, 2 * d) - Q(k % d, d)


def primitive_wave(q, k):
    """Möbius inversion of d*u_d, independent of complex Fourier formula."""
    return sum((mu_trial(q // d) * d * u(d, k)
                for d in range(1, q + 1) if q % d == 0), Q(0))


def jordan_two(n):
    out = n * n
    for p in factor_trial(n):
        out = out // (p * p) * (p * p - 1)
    return out


def periodic_checks():
    wave = {q: [primitive_wave(q, k) for k in range(q)]
            for q in range(2, 16)}
    for d in range(1, 16):
        require(sum((u(d, k) for k in range(d)), Q(0)) == 0,
                "period-mean", f"centered period {d}")
        for k in range(d):
            require(Q(1, 2) - Q(k % d, d) == Q(1, 2 * d) + u(d, k),
                    "period-mean", f"literal integer sawtooth {d},{k}")
            assembled = sum((wave[q][k % q]
                             for q in wave if d % q == 0), Q(0))
            require(d * u(d, k) == assembled,
                    "primitive-wave", f"denominator inversion {d},{k}")
    for q in wave:
        require(sum(wave[q], Q(0)) == 0,
                "wave-covariance", f"zero mean of primitive wave {q}")
        for r in wave:
            period = lcm(q, r)
            inner = sum((wave[q][k % q] * wave[r][k % r]
                         for k in range(period)), Q(0)) / period
            expected = Q(jordan_two(q), 12) if q == r else Q(0)
            require(inner == expected,
                    "wave-covariance", f"complete cross period {q},{r}")
            if q == r:
                require(inner <= Q(q * q, 4),
                        "coefficient-mass", f"primitive norm bound {q}")

    stream = sha256()
    fixture_cells = 0
    for D in range(1, 9):
        full_period = 1
        for d in range(1, D + 1):
            full_period = lcm(full_period, d)
        fixtures = {
            "positive_divisor": [0] + [tau(d) for d in range(1, D + 1)],
            "alternating_divisor": [0] + [(-1) ** d * tau(d) for d in range(1, D + 1)],
            "native_product": [0] + [sum(mu_trial(a) * mu_trial(d // a)
                                         for a in range(1, d + 1) if d % a == 0)
                                      for d in range(1, D + 1)],
        }
        fractions = sorted({Q(0)} | {Q(a, q) for q in range(2, D + 1)
                                    for a in range(1, q) if gcd(a, q) == 1})
        require(len(fractions) <= D * D, "farey-spacing", f"complete count D={D}")
        if len(fractions) > 1:
            for left, right in zip(fractions, fractions[1:] + [fractions[0] + 1]):
                require(right - left >= Q(1, D * D),
                        "farey-spacing", f"circular spacing D={D}")
        for label, c in fixtures.items():
            Z = {q: sum((Q(c[d], d) for d in range(q, D + 1, q)), Q(0))
                 for q in range(1, D + 1)}
            squared_mass = Z[1] ** 2 / 4 + sum(
                (Z[q] ** 2 * Q(jordan_two(q), 12) for q in range(2, D + 1)), Q(0))
            require(squared_mass <= Q(D, 2) * harmonic(D) ** 7,
                    "coefficient-mass", f"all grouped coefficients {D},{label}")
            for k in range(full_period):
                direct = sum((c[d] * (Q(1, 2) - Q(k % d, d))
                              for d in range(1, D + 1)), Q(0))
                grouped = Z[1] / 2 + sum(
                    (Z[q] * wave[q][k % q] for q in range(2, D + 1)), Q(0))
                require(direct == grouped,
                        "grouped-source", f"complete period {D},{label},{k}")
                stream.update(f"{D}|{label}|{k}|{direct}\n".encode())
                fixture_cells += 1
            if D >= 2 and label == "positive_divisor":
                k = 0
                direct = sum((Q(c[d], 2) for d in range(1, D + 1)), Q(0))
                no_constant = sum((Z[q] * wave[q][0]
                                   for q in range(2, D + 1)), Q(0))
                require(direct != no_constant,
                        "negative-control", "zero frequency cannot be discarded")
                wrong_Z = {q: sum((Q(c[d], q) for d in range(q, D + 1, q)), Q(0))
                           for q in range(1, D + 1)}
                wrong = wrong_Z[1] / 2 + sum(
                    (wrong_Z[q] * wave[q][0] for q in range(2, D + 1)), Q(0))
                require(wrong != direct,
                        "negative-control", "cofactor weight is 1/d, not 1/q")
    return {"complete_period_cells": fixture_cells,
            "source_stream_sha256": stream.hexdigest(),
            "denominator_range": "1 through 15 for primitive waves; 1 through 8 for complete source periods"}


def native_case(Y):
    b, end = Y + 1, (Y + 1) ** 2
    prefix = [0] + [mu_trial(n) for n in range(1, Y + 1)]
    comparison = mu_sieve(end)
    require(prefix == comparison[:Y + 1],
            "native-prefix", f"independent primitive prefix Y={Y}")
    z = [0] * (Y * Y + 1)
    for a in range(1, Y + 1):
        for c in range(1, Y + 1):
            z[a * c] += prefix[a] * prefix[c]
    v = [0] * (end + 1)
    for n in range(1, Y + 1):
        v[n] += 2 * prefix[n]
    for d in range(1, Y * Y + 1):
        for n in range(d, end + 1, d):
            v[n] -= z[d]
    require(v[1:end] == comparison[1:end],
            "native-coefficient", f"every strict native coefficient Y={Y}")
    require(comparison[end] - v[end] == comparison[b] ** 2,
            "native-coefficient", f"first excluded coefficient Y={Y}")

    m = [Q(0)] * end
    for k in range(1, end):
        m[k] = m[k - 1] + Q(comparison[k], k)
    M = m[Y]
    ell = sum((log_integer(n) * Q(prefix[n], n)
               for n in range(1, Y + 1)), Form(0))
    B = 1 + ell - (log_integer(Y) + GAMMA / 2) * M
    require(sum((Q(z[d], d) for d in range(1, len(z))), Q(0)) == M * M,
            "native-balance", f"constant product moment Y={Y}")
    require(sum((log_integer(d) * Q(z[d], d)
                 for d in range(1, len(z))), Form(0)) == ell * (2 * M),
            "native-balance", f"logarithmic product moment Y={Y}")

    cells = 0
    block_checks = 0
    removed_tuples = 0
    high_above_output_defects = 0
    missed_balance_defects = 0
    X = b
    while X < end:
        stop = min(2 * X, end)
        D = integer_root(X ** 5, 8)
        require(1 <= D <= X, "native-cutoff", f"annular cutoff Y={Y},X={X}")
        for a in range(1, Y + 1):
            for c in range(1, Y + 1):
                if min(a, c) <= D // Y:
                    require(a * c <= D, "pair-sector", f"exact low-high tuple {Y},{X},{a},{c}")
                    removed_tuples += 1
        filtered = {}
        low = {}
        for k in range(X, stop):
            balance = B * (2 * M) + (2 * log_integer(Y) - log_integer(k)) * (M * M)
            full_remainder = sum((remainder(k, d) * Q(z[d], d)
                                  for d in range(1, len(z))), Form(0))
            require(balance - full_remainder == m[k],
                    "native-balanced-reconstruction", f"every cell {Y},{k}")
            low[k] = sum((remainder(k, d) * Q(z[d], d)
                          for d in range(1, min(D, Y * Y) + 1)), Form(0))
            high = sum((remainder(k, d) * Q(z[d], d)
                        for d in range(D + 1, len(z))), Form(0))
            filtered[k] = balance - high
            require(Form(m[k]) - filtered[k] == -low[k],
                    "native-filtered-reconstruction", f"power-sector identity {Y},{k}")
            wrong_high = sum((remainder(k, d) * Q(z[d], d)
                              for d in range(D + 1, min(k, Y * Y) + 1)), Form(0))
            if balance - wrong_high != filtered[k]:
                high_above_output_defects += 1
            if -full_remainder != m[k]:
                missed_balance_defects += 1
            cells += 1

        # Unequal short blocks and their final residual cell are all retained.
        a = X
        while a < stop:
            h = min(1 + ((a - X) % 5), stop - a)
            direct_filtered = sum((filtered[k] for k in range(a, a + h)), Form(0)) / h
            L_I = sum((log_integer(k) for k in range(a, a + h)), Form(0)) / h
            def A(d, t):
                r = (t - 1) // d
                return t * harmonic(r) - d * r
            kernel_mean = sum(((Form(Q(A(d, a + h) - A(d, a), h)) - L_I
                                + log_integer(d) - GAMMA) * Q(z[d], d)
                               for d in range(D + 1, len(z))), Form(0))
            formula_filtered = B * (2 * M) + (2 * log_integer(Y) - L_I) * (M * M) - kernel_mean
            require(direct_filtered == formula_filtered,
                    "coarse-coordinate", f"complete block {Y},{a},{h}")
            native_mean = sum(m[a:a + h], Q(0)) / h
            require(Form(native_mean) - formula_filtered ==
                    -sum((low[k] for k in range(a, a + h)), Form(0)) / h,
                    "coarse-coordinate", f"coarse amplitude difference {Y},{a},{h}")
            block_checks += 1
            a += h
        X *= 2
    require(cells == end - b, "complete-native-cells", f"full square step Y={Y}")
    require(missed_balance_defects > 0,
            "negative-control", f"logarithmic balance is compulsory Y={Y}")
    if Y >= 3:
        require(high_above_output_defects > 0,
                "negative-control", f"above-output products are compulsory Y={Y}")
    return {"Y": Y, "strict_endpoint": end - 1, "cells": cells,
            "complete_blocks": block_checks, "low_high_tuple_checks": removed_tuples,
            "excluded_endpoint_defect": comparison[end] - v[end],
            "detected_above_output_deletions": high_above_output_defects,
            "detected_balance_deletions": missed_balance_defects}


def larger_pair_coverage():
    Y = 512
    b = Y + 1
    X = b
    while 2 * X < b * b:
        X *= 2
    D = integer_root(X ** 5, 8)
    threshold = D // Y
    owned = 0
    for a in range(1, Y + 1):
        for c in range(1, Y + 1):
            if min(a, c) <= threshold:
                require(a * c <= D, "pair-sector", "larger exact top-annulus tuple inclusion")
                owned += 1
    require(owned == Y * Y - (Y - threshold) ** 2,
            "pair-sector", "complete ordered pair count")
    return {"Y": Y, "top_annulus": X, "D": D,
            "removed_small_index_threshold": threshold,
            "complete_included_ordered_pairs": owned,
            "scope": "source tuple inclusion only; no large energy replay"}


def run():
    periodic = periodic_checks()
    cases = [native_case(Y) for Y in (1, 2, 3, 4, 7, 10, 15)]
    require(any(c["excluded_endpoint_defect"] for c in cases),
            "negative-control", "strict square endpoint is tested nontrivially")
    pairs = larger_pair_coverage()
    here = Path(__file__).resolve().parent
    return {
        "status": "PASS",
        "arithmetic": "Exact integers and fractions; formal prime logarithms and gamma",
        "acceptance": "Every explicit predicate must pass; active under Python -O",
        "checks": dict(sorted(COUNTS.items())),
        "total_checks": sum(COUNTS.values()),
        "periodic_replay": periodic,
        "native_cases": cases,
        "larger_pair_coverage": pairs,
        "proof_sha256": sha256((here / "PROOF.md").read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "not_verified": [
            "Infinite harmonic remainder inequality or asymptotic frequency estimate by computation",
            "Any bound on the remaining high-product native amplitude",
            "Any subquadratic coarse-energy recurrence or RH conclusion",
            "An independent mathematical review or transcendental implementation",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")
