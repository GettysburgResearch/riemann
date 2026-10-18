#!/usr/bin/env python3
"""Exact finite algebra and coverage checks; no numerical analytic proof."""
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from math import gcd


COUNTS = Counter()
MUTATIONS = (
    "omit_overlap_assignment", "drop_mode_center", "drop_balance_gamma",
    "include_square_endpoint", "drop_q1_mode", "delete_above_output_products",
    "impose_coprime_inputs", "omit_final_cell", "duplicate_core_sector",
)


def need(value, gate):
    COUNTS[gate] += 1
    if not value:
        raise RuntimeError("REJECT:" + gate)


@lru_cache(None)
def factor(n):
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
    fs = factor(n)
    return 0 if any(e > 1 for _, e in fs) else (-1) ** len(fs)


def mu_sieve(n):
    a = [1] * (n + 1)
    a[0] = 0
    prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if prime[p]:
            for k in range(p, n + 1, p):
                a[k] *= -1
                if k > p:
                    prime[k] = False
            for k in range(p * p, n + 1, p * p):
                a[k] = 0
    return a


@lru_cache(None)
def divisors(n):
    out = [1]
    for p, e in factor(n):
        out = [a * p ** j for a in out for j in range(e + 1)]
    return tuple(sorted(out))


def phi(n):
    out = n
    for p, _ in factor(n):
        out = out // p * (p - 1)
    return out


class Form:
    """Q-linear formal constants, prime logarithms and Euler's gamma."""
    def __init__(self, coeff=None):
        if isinstance(coeff, Form):
            coeff = coeff.c
        if coeff is None:
            coeff = {}
        if not isinstance(coeff, dict):
            coeff = {"constant": F(coeff)}
        self.c = {k: F(v) for k, v in coeff.items() if v}

    def __add__(self, other):
        other = Form(other)
        c = self.c.copy()
        for k, v in other.c.items():
            c[k] = c.get(k, F(0)) + v
        return Form(c)

    __radd__ = __add__

    def __neg__(self):
        return Form({k: -v for k, v in self.c.items()})

    def __sub__(self, other):
        return self + -Form(other)

    def __rsub__(self, other):
        return Form(other) + -self

    def __mul__(self, scalar):
        return Form({k: v * scalar for k, v in self.c.items()})

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.c == Form(other).c


GAMMA = Form({"gamma": 1})


@lru_cache(None)
def log_integer(n):
    return Form({"log:" + str(p): e for p, e in factor(n)})


def log_fraction(x):
    x = F(x)
    return log_integer(x.numerator) - log_integer(x.denominator)


def mangoldt(q):
    fs = factor(q)
    return log_integer(fs[0][0]) if len(fs) == 1 else Form()


@lru_cache(None)
def harmonic(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def remainder(x, d=1):
    x = F(x)
    return Form(harmonic(x.numerator // (x.denominator * d))) \
        - log_fraction(x) + log_integer(d) - GAMMA


@lru_cache(None)
def masked(d, x):
    return sum((F(mu_trial(n), n) for n in range(1, x + 1)
                if gcd(n, d) == 1), F(0))


def complete_factorization(q, y, mutation):
    fs = factor(q)
    if any(e >= 3 for _, e in fs):
        return F(0), F(0)
    r = 1
    ps = []
    for p, e in fs:
        if e == 2:
            r *= p
        else:
            ps.append(p)
    s = 1
    for p in ps:
        s *= p
    out = F(0)
    for labels in product(range(3), repeat=len(ps)):
        u = v = w = 1
        for p, label in zip(ps, labels):
            if label == 0:
                u *= p
            elif label == 1:
                v *= p
            else:
                w *= p
        a = masked(r * u * w, y // (r * u * w))
        b = masked(r * v * w, y // (r * v * w))
        need(abs(a) <= 1 and abs(b) <= 1, "masked_reciprocal_cap")
        if mutation == "omit_overlap_assignment" and w != 1:
            continue
        out += a * b / w
    bound = F(1)
    for p in ps:
        bound *= 2 + F(1, p)
    return F(mu_trial(s), q) * out, bound


def ramanujan(q, n):
    return sum(d * mu_trial(q // d) for d in divisors(gcd(q, n)))


def ramanujan_quotient(q, n):
    h = q // gcd(q, n)
    return mu_trial(h) * phi(q) // phi(h)


def centered_mode_checks(mutation):
    for q in range(2, 25):
        acc = F(0)
        for k in range(1, 25):
            need(ramanujan(q, k) == ramanujan_quotient(q, k),
                 "ramanujan_independent_integer_formula")
            acc += F(ramanujan(q, k), k)
            center = Form() if mutation == "drop_mode_center" else mangoldt(q)
            direct = Form(acc) + center
            via_r = sum((mu_trial(q // d) * remainder(k, d)
                         for d in divisors(q)), Form())
            need(direct == via_r, "centered_mode_real_identity")
            fractional = F(3 * k + 1, 3)
            for d in divisors(q):
                need(fractional.numerator // (fractional.denominator * d) == k // d,
                     "whole_integer_cell_floor")
            on_cell = sum((mu_trial(q // d) * remainder(fractional, d)
                           for d in divisors(q)), Form())
            need(on_cell == direct, "whole_integer_cell_mode")


def ceil_root_floor(n, degree):
    lo, hi = 0, n + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


@lru_cache(None)
def squarefree_parts(q):
    r = s = 1
    for p, e in factor(q):
        if e >= 3:
            return None
        if e == 2:
            r *= p
        else:
            s *= p
    return r, s


def weights_for_q_range(C, qlo, qhi, cap, selector=None):
    weights = [F(0)] * (cap + 1)
    const = Form()
    for q in range(qlo, qhi + 1):
        if not C[q] or (selector is not None and not selector(q)):
            continue
        const += C[q] * mangoldt(q)
        for d in divisors(q):
            weights[d] += C[q] * mu_trial(q // d)
    return weights, const


def harmonic_output(weights, last):
    coef = [F(0)] * (last + 1)
    for d, w in enumerate(weights):
        if d and w:
            for n in range(d, last + 1, d):
                coef[n] += d * w
    out = [F(0)] * (last + 1)
    for n in range(1, last + 1):
        out[n] = out[n - 1] + coef[n] / n
    return out


def native_case(y, mutation):
    b, last = y + 1, (y + 1) ** 2 - 1
    cap = y * y
    source = [0] + [mu_trial(n) for n in range(1, y + 1)]
    comparison = mu_sieve(last + 1)
    for n in range(1, y + 1):
        need(source[n] == comparison[n], "independent_native_prefix")
    m = [F(0)] * (last + 2)
    for n in range(1, last + 2):
        m[n] = m[n - 1] + F(comparison[n], n)
    M = m[y]
    z = [0] * (cap + 1)
    for a in range(1, y + 1):
        for c in range(1, y + 1):
            if mutation == "impose_coprime_inputs" and gcd(a, c) != 1:
                continue
            z[a * c] += source[a] * source[c]
    for d in range(1, cap + 1):
        alternate = sum(source[a] * source[d // a]
                        for a in divisors(d) if a <= y and d // a <= y)
        need(z[d] == alternate, "complete_ordered_product_fibers")
    C = [F(0)] * (cap + 1)
    for q in range(1, cap + 1):
        C[q] = sum((F(z[d], d) for d in range(q, cap + 1, q)), F(0))
        fac, bound = complete_factorization(q, y, mutation)
        need(C[q] == fac, "complete_mask_factorization")
        need(abs(q * C[q]) <= bound, "complete_coefficient_cap")
        parts = squarefree_parts(q)
        if parts is None:
            need(C[q] == 0, "prime_cube_coefficient_vanishing")
        else:
            r, core = parts
            need(r * r * core == q and gcd(r, core) == 1
                 and abs(mu_trial(r)) == abs(mu_trial(core)) == 1,
                 "unique_squarefree_core_decomposition")
            if core == 1:
                square = masked(r, y // r) ** 2 / (r * r)
                need(C[q] == square and C[q] >= 0,
                     "exact_positive_square_coefficient")
    need(C[1] == M * M, "zero_denominator_coefficient")
    Cmass = F(0)
    H = F(0)
    for Q in range(1, cap + 1):
        Cmass += Q * Q * C[Q] * C[Q]
        H += F(1, Q)
        need(Cmass <= 32 * Q * H ** 3, "complete_coefficient_mass")
    LY = sum((F(source[n], n) * log_integer(n) for n in range(1, y + 1)), Form())
    B = 1 + LY - M * (log_integer(y) + F(1, 2) * GAMMA)
    rhs = F(1, 2) * M * GAMMA + sum(
        (F(source[n], n) * remainder(y, n) for n in range(1, y + 1)), Form())
    if mutation == "drop_balance_gamma":
        rhs -= F(1, 2) * M * GAMMA
    need(B == rhs, "linear_balance_reconstruction")
    zlog = sum((F(z[d], d) * log_integer(d) for d in range(1, cap + 1)), Form())
    need(zlog == 2 * M * LY, "quadratic_log_balance")
    qlog = sum((C[q] * mangoldt(q) for q in range(2, cap + 1)), Form())
    need(qlog == zlog, "complete_cyclotomic_centering")

    divisor_output = [0] * (last + 2)
    for d in range(1, cap + 1):
        for n in range(d, last + 2, d):
            divisor_output[n] += z[d]
    for n in range(1, last + 1):
        v = 2 * (source[n] if n <= y else 0) - divisor_output[n]
        need(v == comparison[n], "complete_strict_native_coefficients")
    defect = comparison[last + 1] + divisor_output[last + 1]
    need(defect == comparison[b] ** 2, "first_excluded_coefficient_defect")
    if mutation == "include_square_endpoint" and comparison[b]:
        need(defect == 0, "strict_square_endpoint")

    crossing = bool(source[y] and m[y - 1] * m[y] <= 0)
    if crossing:
        need(abs(M) <= F(1, y), "native_crossing_endpoint_cap")

    S = max(1, y.bit_length() - 1)
    X = b
    annuli = 0
    cells = 0
    while X < b * b:
        U = min(2 * X, b * b)
        Q = ceil_root_floor(X ** 5, 8)
        need(Q ** 8 <= X ** 5 < (Q + 1) ** 8, "exact_five_eighth_cutoff")
        low_w, low_const = weights_for_q_range(C, 2, Q, cap)
        high_w, high_const = weights_for_q_range(C, Q + 1, cap, cap)
        def paid_selector(q):
            return squarefree_parts(q)[1] <= S
        def rough_selector(q):
            if mutation == "duplicate_core_sector":
                return True
            return squarefree_parts(q)[1] > S
        paid_w, paid_const = weights_for_q_range(C, Q + 1, cap, cap, paid_selector)
        rough_w, rough_const = weights_for_q_range(C, Q + 1, cap, cap, rough_selector)
        low_values = harmonic_output(low_w, last)
        high_values = harmonic_output(high_w, last)
        paid_values = harmonic_output(paid_w, last)
        rough_values = harmonic_output(rough_w, last)
        need(paid_const + rough_const == high_const,
             "three_sector_complete_centering")
        for d in range(1, cap + 1):
            restored = d * (low_w[d] + high_w[d])
            if d == 1:
                restored += C[1]
            need(restored == z[d], "jordan_polynomial_complete_coefficients")
            need(paid_w[d] + rough_w[d] == high_w[d],
                 "jordan_three_sector_complete_coefficients")
        for d in range(1, min(Q, cap) + 1):
            need(not any(q > Q for q in divisors(d)), "old_low_product_annihilation")
        weighted_mass = sum((q * q * C[q] * C[q] for q in range(2, Q + 1)), F(0))
        absolute_mass = sum((q * q * abs(C[q]) for q in range(2, Q + 1)), F(0))
        need(absolute_mass ** 2 <= weighted_mass * sum(q * q for q in range(2, Q + 1)),
             "complete_error_cauchy_mass")
        cell_end = U - 1 if mutation == "omit_final_cell" else U
        for k in range(X, cell_end):
            A = 2 * M * B + M * M * (2 * log_integer(y) - log_integer(k))
            q1 = M * M * remainder(k)
            if mutation == "drop_q1_mode":
                q1 = Form()
            low = Form(low_values[k]) + low_const
            high = Form(high_values[k]) + high_const
            need(A - q1 - low - high == m[k], "complete_denominator_native_reconstruction")
            paid = Form(paid_values[k]) + paid_const
            rough = Form(rough_values[k]) + rough_const
            need(A - q1 - low - paid - rough == m[k],
                 "complete_rough_core_native_reconstruction")
            if mutation == "delete_above_output_products" and y == 5 and k == b:
                truncated = sum((F(z[d], d) * remainder(k, d)
                                 for d in range(1, min(k, cap) + 1)), Form())
                need(A - truncated == m[k], "above_output_product_retention")
            cells += 1
        annuli += 1
        X = U
    need(cells == b * b - b, "complete_square_step_cell_count")
    return {"Y": y, "crossing": crossing, "cells": cells,
            "annuli": annuli, "products": cap, "denominators": cap,
            "squarefree_core_cutoff": S}


def run(mutation):
    centered_mode_checks(mutation)
    mu = mu_sieve(63)
    m = F(0)
    crossing_list = []
    for y in range(1, 64):
        old = m
        m += F(mu[y], y)
        if y >= 2 and mu[y] and old * m <= 0:
            crossing_list.append(y)
    cases = sorted(set(crossing_list + [2, 3, 4, 8, 16, 32, 63]))
    panels = [native_case(y, mutation) for y in cases]
    return {
        "status": "PASS",
        "arithmetic": "Exact rational and formal prime-log/Euler-gamma coefficients",
        "rho": "5/8",
        "squarefree_core_schedule": "max(1, floor(log_2 Y))",
        "scope": "Finite algebra and complete declared cells; no analytic integral or asymptotic upper-bound certification",
        "crossings_through_63": crossing_list,
        "panels": panels,
        "total_cells": sum(p["cells"] for p in panels),
        "predicates": sum(COUNTS.values()),
        "gates": dict(sorted(COUNTS.items())),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=("none",) + MUTATIONS, default="none")
    args = parser.parse_args()
    print(json.dumps(run(args.mutation), indent=2, sort_keys=True))
