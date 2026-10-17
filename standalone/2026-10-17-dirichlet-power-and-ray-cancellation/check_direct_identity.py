#!/usr/bin/env python3
"""Exact finite regressions for DIRECT_FOURIER.md; not an analytic proof."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import comb, gcd


class CheckFailure(RuntimeError):
    pass


def require(value, message):
    if not value:
        raise CheckFailure(message)


def mobius(limit):
    mu = [1] * (limit + 1)
    mu[0] = 0
    prime = [True] * (limit + 1)
    prime[0:2] = [False, False]
    primes = []
    for p in range(2, limit + 1):
        if prime[p]:
            primes.append(p)
            for n in range(p, limit + 1, p):
                prime[n] = False
                mu[n] *= -1
            for n in range(p * p, limit + 1, p * p):
                mu[n] = 0
    return mu, primes


def convolution(a, b, limit):
    out = [0] * (limit + 1)
    for i in range(1, limit + 1):
        if a[i]:
            for j in range(1, limit // i + 1):
                out[i * j] += a[i] * b[j]
    return out


def char(n, modulus):
    if modulus == 1:
        return 1
    if modulus == 3:
        return (0, 1, -1)[n % 3]
    if modulus == 4:
        return (0, 1, 0, -1)[n % 4]
    if modulus == 5:
        return (0, 1, -1, -1, 1)[n % 5]
    if modulus == 6:
        return int(gcd(n, 6) == 1)
    raise ValueError(modulus)


def product_arrays(arrays, limit):
    unit = [0] * (limit + 1)
    unit[1] = 1
    out = unit
    for a in arrays:
        out = convolution(out, a, limit)
    return out


def ceiling_root(n, j):
    u = 1
    while u ** j < n:
        u += 1
    return u


def finite_inverse(a, b, limit, jmax, omit_last=False):
    u = ceiling_root(limit, jmax)
    au = a[:u + 1] + [0] * (limit - u)
    ab = convolution(au, b, limit)
    term = au
    out = [0] * (limit + 1)
    for j in range(1, jmax + 1):
        if not (omit_last and j == jmax):
            coefficient = (-1) ** (j - 1) * comb(jmax, j)
            out = [x + coefficient * y for x, y in zip(out, term)]
        if j < jmax:
            term = convolution(term, ab, limit)
    return out, u


def q_part(n, q):
    d = 1
    m = n
    while (g := gcd(m, q)) > 1:
        d *= g
        m //= g
    return d, m


def run():
    limit = 2048
    mu, primes = mobius(limit)
    cases = [(1,), (1, 3), (3, 4, 6), (1, 3, 4, 5)]
    records = []
    identity_values = 0
    cofactor_values = 0
    phase_values = 0
    coefficients = {}
    for moduli in cases:
        xis = [[0] + [char(n, q) for n in range(1, limit + 1)] for q in moduli]
        a = product_arrays([[mu[n] * xi[n] for n in range(limit + 1)] for xi in xis], limit)
        b = product_arrays(xis, limit)
        ab = convolution(a, b, limit)
        require(ab[1] == 1 and all(v == 0 for v in ab[2:]), "Dirichlet inverse")
        coefficients[moduli] = a
        for jmax in (2, 3, 5, 8):
            actual, u = finite_inverse(a, b, limit, jmax)
            require(actual == a, f"finite identity {moduli}, J={jmax}")
            identity_values += limit
            records.append({"moduli": moduli, "J": jmax, "U": u, "through": limit})
        for q in range(1, 49):
            for n in range(1, 257):
                if not a[n]:
                    continue
                d, m = q_part(n, q)
                require(d * m == n and gcd(m, q) == 1 and gcd(d, m) == 1,
                        "full q-supported cofactor")
                require(a[n] == a[d] * a[m], "cofactor coefficient")
                cofactor_values += 1
                g = gcd(d, q)
                reduced_q = q // g
                for numerator in (1, q - 1):
                    if gcd(numerator, q) != 1:
                        continue
                    left = Fraction(numerator * n, q) % 1
                    right = Fraction((numerator * d // g) * m, reduced_q) % 1
                    require(left == right, "reduced additive phase")
                    require(gcd(numerator * d // g, reduced_q) == 1,
                            "reduced numerator")
                    phase_values += 1

    # A separate Euler recurrence, with literal split/inert/ramified factors.
    euler = [0] * (limit + 1)
    euler[1] = 1
    for p in primes:
        if p == 3:
            local = [(p, -1)]
        elif p % 3 == 1:
            local = [(p, -2), (p * p, 1)]
        else:
            local = [(p * p, -1)]
        before = euler[:]
        for power, value in local:
            for n in range(1, limit // power + 1):
                euler[n * power] += value * before[n]
    native = coefficients[(1, 3)]
    require(euler == native, "complete Eisenstein rational norm source")
    require(native[7] == -2 and native[49] == 1 and native[4] == -1,
            "split conjugates and inert square")
    require(native[3] == -1 and native[9] == 0, "ramified local factor")

    # Exact exponent budgets for the stated domain, not numerical L-values.
    exponent_cases = []
    for denominator in range(3, 65):
        kappa = Fraction(1, denominator)
        theta = 1 - kappa
        target = (1 + theta) / 2
        require(theta + kappa / 2 == target, "major-arc exponent")
        require(1 - kappa / 2 == target, "Type II exponent")
        require(1 - 2 * kappa >= kappa, "greedy grouping domain")
        require(1 - kappa <= target, "Type I exponent")
        exponent_cases.append(str(kappa))

    # Real corrupted constructions are evaluated and must disagree.
    negatives = {}
    xis = [[0] + [char(n, q) for n in range(1, limit + 1)] for q in (1, 3)]
    b = product_arrays(xis, limit)
    wrong, _ = finite_inverse(native, b, limit, 8, omit_last=True)
    negatives["dropped_final_inverse_term"] = wrong != native
    bad_d = gcd(49, 7)
    negatives["gcd_instead_of_q_infinity"] = gcd(49 // bad_d, 7) != 1
    negatives["one_bounded_native_prime"] = native[7] != -1
    negatives["erased_ramified_character_zero"] = native[9] != 1
    unit = [0] * (limit + 1)
    unit[1] = 1
    # E=1-B A_U may first be nonzero at U+1: the support inequality is strict.
    special = [0] * (limit + 1)
    special[1] = 1
    special[2] = 1
    special_inv = [0] * (limit + 1)
    special_inv[1] = 1
    for n in range(2, limit + 1):
        special_inv[n] = -sum(special[d] * special_inv[n // d]
                              for d in range(2, n + 1) if n % d == 0)
    truncated = special_inv[:2] + [0] * (limit - 1)
    e = [x-y for x, y in zip(unit, convolution(special, truncated, limit))]
    e2 = convolution(e, e, limit)
    negatives["incorrect_closed_support_endpoint"] = e2[4] != 0
    require(all(negatives.values()), "negative control was not rejected")

    digest = hashlib.sha256(json.dumps(native, separators=(",", ":")).encode()).hexdigest()
    return {
        "status": "PASS",
        "scope": "Exact finite coefficient, source, cofactor and exponent regressions only; no analytic theorem certification",
        "inverse_identity_cases": records,
        "inverse_coefficient_comparisons": identity_values,
        "full_cofactor_cases": cofactor_values,
        "reduced_phase_cases": phase_values,
        "complete_norm_coefficients_through": limit,
        "norm_coefficients_sha256": digest,
        "exact_exponent_cases": exponent_cases,
        "negative_controls": negatives,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    output = json.dumps(run(), sort_keys=True, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output, end="")
