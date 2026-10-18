#!/usr/bin/env python3
"""Exact finite native-source replay. No finite experiment proves an asymptotic.

The checker constructs the source from old ordered input pairs, independently
constructs its prime-incidence formula, and compares formal Q-linear logarithms
and Euler's constant. Python's standard library only; assertions are not used.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, isqrt
import json
from pathlib import Path
import subprocess
import sys


COUNTS = Counter()
MUTATION = "none"
MUTATIONS = (
    "drop_shared_prime_correction", "drop_above_output_products",
    "squarefree_products_only", "drop_H2_balance", "admit_inactive_primes",
    "replace_incidence_by_owner", "erase_mode_center",
    "wrong_short_Newton_sign",
)


def need(value, gate):
    COUNTS[gate] += 1
    if not value:
        raise RuntimeError("REJECT:" + gate)


@lru_cache(None)
def factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def mu_trial(n):
    a = factors(n)
    return 0 if any(e > 1 for _, e in a) else (-1) ** len(a)


def mu_sieve(n):
    a = [1] * (n + 1)
    a[0] = 0
    prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if prime[p]:
            for j in range(p, n + 1, p):
                a[j] *= -1
                if j > p:
                    prime[j] = False
            for j in range(p * p, n + 1, p * p):
                a[j] = 0
    return a


@lru_cache(None)
def divisors(n):
    a = [1]
    for p, e in factors(n):
        a = [d * p ** j for d in a for j in range(e + 1)]
    return tuple(sorted(a))


class Linear:
    """Formal rational constant + rational prime logs + rational gamma."""
    def __init__(self, value=0):
        if isinstance(value, Linear):
            self.c = value.c.copy()
        elif isinstance(value, dict):
            self.c = {k: F(v) for k, v in value.items() if v}
        else:
            self.c = {"1": F(value)} if value else {}

    def __add__(self, other):
        other = Linear(other)
        c = self.c.copy()
        for k, v in other.c.items():
            c[k] = c.get(k, F(0)) + v
        return Linear(c)

    __radd__ = __add__

    def __neg__(self):
        return Linear({k: -v for k, v in self.c.items()})

    def __sub__(self, other):
        return self + -Linear(other)

    def __rsub__(self, other):
        return Linear(other) - self

    def __mul__(self, scalar):
        return Linear({k: v * scalar for k, v in self.c.items()})

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.c == Linear(other).c


GAMMA = Linear({"gamma": 1})


@lru_cache(None)
def log_int(n):
    return Linear({"log:" + str(p): e for p, e in factors(n)})


@lru_cache(None)
def harmonic(n):
    # Cached recurrence gives a different construction from divisor inversion.
    if n == 0:
        return F(0)
    return HARMONICS[n]


HARMONICS = [F(0)]


def prepare_harmonics(n):
    for j in range(len(HARMONICS), n + 1):
        HARMONICS.append(HARMONICS[-1] + F(1, j))


@lru_cache(None)
def remainder(k, d=1):
    return Linear(harmonic(k // d)) - log_int(k) + log_int(d) - GAMMA


@lru_cache(None)
def mode(q, k):
    fs = factors(q)
    center = log_int(fs[0][0]) if len(fs) == 1 else Linear()
    if MUTATION == "erase_mode_center":
        center = Linear()
    # This formula uses finite Ramanujan sums, not the R-dilation formula.
    h = sum((F(mu_trial(q // d)) * harmonic(k // d)
             for d in divisors(q)), F(0))
    return Linear(h) + center


@lru_cache(None)
def mobius_prefix(j):
    return sum((F(mu_trial(n), n) for n in range(1, j + 1)), F(0))


@lru_cache(None)
def log_prefix(j):
    return sum((log_int(n) * F(mu_trial(n), n)
                for n in range(1, j + 1)), Linear())


@lru_cache(None)
def T(y, k, d=1):
    return sum((remainder(k, d * n) * F(mu_trial(n), n)
                for n in range(1, y + 1)), Linear())


@lru_cache(None)
def Z(j, k, d=1):
    return sum((remainder(k, d * n * m) * F(mu_trial(n) * mu_trial(m), n * m)
                for n in range(1, j + 1) for m in range(1, j + 1)), Linear())


def source(y):
    mu = mu_sieve(y)
    need(all(mu[n] == mu_trial(n) for n in range(1, y + 1)), "independent_mu")
    z = Counter()
    for a in range(1, y + 1):
        for b in range(1, y + 1):
            if MUTATION == "squarefree_products_only" and mu_trial(a * b) == 0:
                continue
            z[a * b] += mu[a] * mu[b]
    z = {d: v for d, v in z.items() if v}
    c = {}
    for q in range(1, y * y + 1):
        v = sum((F(z.get(d, 0), d) for d in range(q, y * y + 1, q)), F(0))
        if v:
            c[q] = v
    need(c.get(1, 0) == mobius_prefix(y) ** 2, "complete_q1")
    return z, c


def incidence_direct(y, p, k, z, c):
    if MUTATION == "drop_above_output_products":
        c = {q: sum((F(z.get(d, 0), d)
                     for d in range(q, min(k, y * y) + 1, q)), F(0))
             for q in c}
    return sum((mode(q, k) * v for q, v in c.items() if q >= 2 and q % p == 0), Linear())


def incidence_formula(y, p, k):
    j = y // p
    first = sum(((T(y, k, p * n) - T(y, k, n)) * F(mu_trial(n), n)
                 for n in range(1, j + 1)), Linear()) * F(-2, p)
    middle = 1 if MUTATION == "drop_shared_prime_correction" else 2
    error = (-Z(j, k, p * p) + middle * Z(j, k, p) - Z(j, k)) * F(1, p * p)
    return first + error


def threshold(y):
    p = 1
    while p ** 3 < y * y:
        p += 1
    return p


def block_kernel(blocks, power2=True):
    h1 = [sum((F(1, p) for p in a), F(0)) for a in blocks]
    h2 = [sum((F(1, p * p) for p in a), F(0)) for a in blocks]
    if not power2:
        a = min(F(1), h1[1] / h1[0])
        b = -a * h1[0] / h1[1]
        return [a, b]
    v = [h1[1] * h2[2] - h1[2] * h2[1],
         h1[2] * h2[0] - h1[0] * h2[2],
         h1[0] * h2[1] - h1[1] * h2[0]]
    scale = max(abs(a) for a in v)
    need(scale > 0, "kernel_rank_two")
    return [a / scale for a in v]


def weights(y, k, primes):
    groups = defaultdict(list)
    p0 = threshold(y)
    for p in primes:
        if p > p0 and (p * y > k or MUTATION == "admit_inactive_primes"):
            groups[y // p].append(p)
    w = {}
    for j, ps in groups.items():
        if MUTATION == "drop_H2_balance":
            if len(ps) < 2:
                continue
            blocks = [ps[:len(ps) // 2], ps[len(ps) // 2:]]
            values = block_kernel(blocks, False)
        else:
            if len(ps) < 3:
                continue
            a = len(ps) // 3
            b = 2 * len(ps) // 3
            blocks = [ps[:a], ps[a:b], ps[b:]]
            values = block_kernel(blocks)
        for block, value in zip(blocks, values):
            for p in block:
                w[p] = value
        need(sum((w[p] / p for p in ps), F(0)) == 0, "first_balance")
        need(sum((w[p] / (p * p) for p in ps), F(0)) == 0, "second_balance")
        need(all(abs(w.get(p, 0)) <= 1 for p in ps), "bounded_weights")
        need(all(p * y > k for p in ps if w.get(p, 0)), "active_prefix_support")
    return w


def weighted_direct(y, k, c, w):
    out = Linear()
    for q, value in c.items():
        if q == 1:
            continue
        ps = [p for p in w if q % p == 0]
        if MUTATION == "replace_incidence_by_owner":
            ps = ps[:1]
        coefficient = sum((w[p] for p in ps), F(0))
        if coefficient:
            out += mode(q, k) * (coefficient * value)
    return out


def weighted_reduced(y, k, w):
    out = Linear()
    my = mobius_prefix(y)
    for p, wp in w.items():
        j = y // p
        mj = mobius_prefix(j)
        out -= log_int(p) * (2 * my * mj * wp / p)
        out -= Linear(mobius_prefix(k // (p * p))) * (wp / (p * p))
        out -= log_int(p) * (2 * mj * mj * wp / (p * p))
        out += (2 * Z(j, k, p) - Z(j, k)) * (wp / (p * p))
    return out


def native_identities(y, p, k):
    j = y // p
    if k < p * y:
        for n in range(1, j + 1):
            d = p * n
            rhs = Linear(1) + log_prefix(y) \
                - (log_int(k) - log_int(d) + GAMMA) * mobius_prefix(y)
            need(T(y, k, d) == rhs, "short_single_inverse")
        d = p * p
        sign = -1 if MUTATION == "wrong_short_Newton_sign" else 1
        rhs = Linear(sign * mobius_prefix(k // d)) \
            - (log_int(k) - log_int(d) + GAMMA) * mobius_prefix(j) ** 2 \
            + log_prefix(j) * (2 * mobius_prefix(j))
        need(Z(j, k, d) == rhs, "short_double_inverse")


def sample_cells(y, full):
    b = y + 1
    n = b * b - 1
    if full:
        return list(range(b, n + 1))
    a = {b, b + 1, 2 * b - 1, y * y // 32, y * y // 16,
         y * y // 4, y * y // 2, y * y - 1, y * y, n - 1, n}
    for p in range(2, y + 1):
        if len(factors(p)) == 1 and factors(p)[0] == (p, 1):
            a.update((p * y - 1, p * y, p * y + 1))
    return sorted(k for k in a if b <= k <= n)


def core(q):
    return 0 if any(e > 2 for _, e in factors(q)) else \
        __import__("functools").reduce(lambda a, b: a * b,
                                      (p for p, e in factors(q) if e == 1), 1)


def exact_checks():
    ys = list(range(2, 17)) + [20, 24, 32, 48, 64, 80, 96]
    prepare_harmonics((max(ys) + 1) ** 2)
    coverage = []
    nonzero_weight_cases = 0
    for y in ys:
        z, c = source(y)
        primes = [p for p in range(2, y + 1) if factors(p) == ((p, 1),)]
        large = [p for p in primes if p * p > y]
        cells = sample_cells(y, y <= 9)
        need(cells[0] == y + 1 and cells[-1] == (y + 1) ** 2 - 1, "strict_output_endpoints")
        for q, cq in c.items():
            fs = factors(q)
            need(all(e <= 2 for _, e in fs), "cube_free_support")
            need(sum(p in large for p, _ in fs) <= 2, "prime_incidence_resource")
            if q > 1:
                av = F(1)
                d7 = 1
                for p, e in fs:
                    if e == 1:
                        av *= 2 + F(1, p)
                    d7 *= __import__("math").comb(e + 6, 6)
                need(abs(q * cq) <= av, "complete_coefficient_cap")
                need(av * av <= d7, "seventh_divisor_resource")
        for p in primes:
            if p > y / 2:
                need(c.get(p * p) == F(1, p * p), "exact_prime_square")
        top = [p for p in primes if 2 * p > y]
        for i, p in enumerate(top):
            for ell in top[i + 1:]:
                need(c.get(p * ell) == F(2, p * ell), "exact_prime_pair")
        for k in cells:
            for p in large:
                direct = incidence_direct(y, p, k, z, c)
                predicted = incidence_formula(y, p, k)
                need(direct == predicted, "complete_incidence_identity")
                native_identities(y, p, k)
            w = weights(y, k, primes)
            if w:
                nonzero_weight_cases += 1
                need(weighted_direct(y, k, c, w) == weighted_reduced(y, k, w),
                     "weighted_native_reduction")
                need(max(abs(a) for a in w.values()) == 1, "nontrivial_normalization")
        # A pair of independent coefficient constructions at prime incidence.
        for p in large:
            for q, cq in c.items():
                if q % p == 0:
                    native_pairs = sum((F(mu_trial(a) * mu_trial(b), a * b)
                                        for a in range(1, y + 1)
                                        for b in range(1, y + 1) if a * b % q == 0), F(0))
                    need(cq == native_pairs, "ordered_pair_coefficient_replay")
        coverage.append({"Y": y, "cells": len(cells), "large_primes": len(large),
                         "nonzero_denominators": len(c)})
    need(nonzero_weight_cases > 0, "nonvacuous_probe_cases")
    # The pair target forces three weights to 1/2 and violates the first balance.
    for ps in ([5, 7, 11], [37, 41, 43], [101, 103, 107]):
        v = [F(1, 2)] * 3
        need(all(v[i] + v[j] == 1 for i in range(3) for j in range(i)), "pair_target")
        need(sum(v[i] / ps[i] for i in range(3)) > 0, "capture_obstruction")
    # The explicit prime-pair mode lower bound reduces to a rational inequality.
    for y in (512, 513, 1024, 4096, 1000000):
        need(F(1, 3) - F(64, y) - F(32, y * y) >= F(1, 5), "mode_lower_constant")
        cells = y * y // 16 - (y * y + 31) // 32 + 1
        need(cells >= F(y * y, 64), "lower_sector_cell_count")
    # Exact dyadic decomposition coverage, separately from native formulas.
    for n in range(1, 65):
        for r in range(n + 1):
            blocks = []
            at = 0
            for power in reversed(range(n.bit_length())):
                size = 1 << power
                if at + size <= r:
                    blocks.append((at, at + size))
                    at += size
            covered = [j for a, b in blocks for j in range(a, b)]
            need(covered == list(range(r)), "dyadic_prefix_coverage")
            need(len(blocks) <= n.bit_length(), "dyadic_prefix_count")
    # Rational exponent budget for the concrete rho=13/24.
    rho = F(13, 24)
    alpha = 2 - 3 * rho
    need(F(1, 2) < rho < F(5, 9), "rho_domain")
    need(alpha > F(1, 3), "moving_strata_budget")
    need(F(1, 3) - alpha == F(-1, 24), "vanishing_low_denominator_power")
    return {"status": "PASS", "arithmetic": "EXACT_RATIONAL_AND_FORMAL_LOGARITHMS",
            "cases": coverage, "nonzero_weight_cases": nonzero_weight_cases,
            "checks_by_gate": dict(sorted(COUNTS.items())),
            "total_checks_including_guards": sum(COUNTS.values()),
            "not_checked": ["infinite large-sieve and maximal proofs", "PNT",
                            "global zero-free estimates", "RH", "complete target capture"]}


def run_mutations():
    rows = []
    for mutation in MUTATIONS:
        r = subprocess.run([sys.executable, "-B", "-O", str(Path(__file__).resolve()),
                            "--mutate", mutation], capture_output=True, text=True)
        need(r.returncode != 0 and "REJECT:" in r.stderr, "mutation_rejected")
        gate = r.stderr.rsplit("REJECT:", 1)[-1].splitlines()[0]
        rows.append({"mutation": mutation, "status": "REJECTED", "gate": gate})
    return rows


def main():
    global MUTATION
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutate", choices=("none",) + MUTATIONS, default="none")
    ap.add_argument("--mutations", action="store_true")
    ap.add_argument("--report", type=Path)
    args = ap.parse_args()
    MUTATION = args.mutate
    report = exact_checks()
    if args.mutations:
        report["mutations"] = run_mutations()
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(encoded, encoding="utf-8", newline="\n")
    sys.stdout.write(encoded)


if __name__ == "__main__":
    main()
