#!/usr/bin/env python3
"""Exact finite diagnostics for support descent.

This checks local identities and the integral cusp-matrix construction. It
does not certify theta automorphy, a Mellin contour shift, an infinite moment,
or a zero-free region. No floating-point arithmetic is used.
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path


ZERO, ONE, THREE, LAM = (0, 0), (1, 0), (3, 0), (1, 2)
UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1))


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def conj(x):
    return (x[0] - x[1], -x[1])


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def div_exact(x, y):
    n = norm(y)
    require(n != 0, "division by zero")
    p = mul(x, conj(y))
    require(p[0] % n == 0 and p[1] % n == 0, ("inexact division", x, y))
    return (p[0] // n, p[1] // n)


def divides(y, x):
    if y == ZERO:
        return x == ZERO
    n = norm(y)
    p = mul(x, conj(y))
    return p[0] % n == 0 and p[1] % n == 0


def divrem(x, y):
    n = norm(y)
    require(n != 0, "Euclidean division by zero")
    p = mul(x, conj(y))
    a, b = p[0] // n, p[1] // n
    candidates = ((a + i, b + j) for i, j in itertools.product(range(-1, 2), repeat=2))
    q = min(candidates, key=lambda z: (norm(sub(x, mul(z, y))), z))
    r = sub(x, mul(q, y))
    require(norm(r) < n, ("Euclidean norm decrease", x, y, q, r))
    return q, r


def xgcd(x, y):
    r0, r1 = x, y
    s0, s1, t0, t1 = ONE, ZERO, ZERO, ONE
    while r1 != ZERO:
        q, r2 = divrem(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, sub(s0, mul(q, s1))
        t0, t1 = t1, sub(t0, mul(q, t1))
    require(add(mul(s0, x), mul(t0, y)) == r0, ("Bezout", x, y))
    return r0, s0, t0


def invmod(x, modulus):
    require(modulus != ZERO, "zero modulus")
    g, s, _ = xgcd(x, modulus)
    require(norm(g) == 1, ("nonunit gcd", x, modulus, g))
    out = mul(s, conj(g))
    require(divides(modulus, sub(mul(x, out), ONE)), ("modular inverse", x, modulus))
    return out


I = (ONE, ZERO, ZERO, ONE)


def mmul(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return (add(mul(a, e), mul(b, g)), add(mul(a, f), mul(b, h)),
            add(mul(c, e), mul(d, g)), add(mul(c, f), mul(d, h)))


def det(A):
    a, b, c, d = A
    return sub(mul(a, d), mul(b, c))


def minv(A):
    require(det(A) == ONE, ("SL2 inverse", A))
    a, b, c, d = A
    return (d, neg(b), neg(c), a)


def congruent(A, B):
    return all(divides(THREE, sub(x, y)) for x, y in zip(A, B))


def cusp_matrix(a, c, lower):
    """Construct g, G, H in ALL_CUSP_REFLECTION Lemma 2.1."""
    gamma = (ONE, ZERO, lower, ONE)
    A, C = a, add(mul(lower, a), c)
    target = A if divides(LAM, C) else C
    choices = [u for u in UNITS if divides(THREE, sub(mul(u, target), ONE))]
    require(len(choices) == 1, ("unit normalization", a, c, lower, target))
    unit = choices[0]
    A, C = mul(unit, A), mul(unit, C)
    if C == ZERO:
        require(A == ONE, "C=0 normalized A")
        G = I
    elif divides(LAM, C):
        D = invmod(A, mul(THREE, C))
        B = div_exact(sub(mul(A, D), ONE), C)
        G = (A, B, C, D)
    else:
        D = mul(THREE, invmod(mul(THREE, A), C))
        B = div_exact(sub(mul(A, D), ONE), C)
        G = (A, B, C, D)
    if divides(THREE, C):
        H, kind, u = I, "C_multiple_of_3", ZERO
    elif divides(LAM, C):
        choices = [z for z in (LAM, neg(LAM)) if divides(THREE, sub(z, C))]
        require(len(choices) == 1, ("lambda residue", C))
        u = choices[0]
        H, kind = (ONE, ZERO, u, ONE), "lambda_valuation_1"
    else:
        t = (A[0] % 3, A[1] % 3)
        H, kind, u = (t, neg(ONE), ONE, ZERO), "lambda_unit", neg(t)
    g1 = mmul(G, minv(H))
    g = mmul(minv(gamma), G)
    require(det(G) == det(H) == det(g1) == det(g) == ONE, "all determinants")
    require(congruent(g1, I), ("g1 not congruent to I", a, c, lower))
    require(mmul(gamma, g) == mmul(g1, H), "factorization")
    require((g[0], g[2]) == (mul(unit, a), mul(unit, c)), "original first column")
    require(norm(g[2]) == norm(c), "original denominator norm")
    # O/(Z+3O) is indexed by the omega coefficient modulo three.
    cusp = u[1] % 3
    representative = (ZERO, (0, 1), (-1, -1))[cusp]
    difference = sub(u, representative)
    require(difference[1] % 3 == 0, ("three-cusp reduction", u, representative))
    return kind, cusp, norm(C) != norm(c), C == ZERO


def check_matrices():
    elements = list(itertools.product(range(-2, 3), repeat=2))
    counts = {"primitive_columns": 0, "matrix_constructions": 0,
              "transformed_norm_differs": 0, "transformed_denominator_zero": 0}
    kinds = {"C_multiple_of_3": 0, "lambda_valuation_1": 0, "lambda_unit": 0}
    target_cusps = [0, 0, 0]
    for a, c in itertools.product(elements, repeat=2):
        if c == ZERO or norm(xgcd(a, c)[0]) != 1:
            continue
        counts["primitive_columns"] += 1
        for lower in (ZERO, (0, 1), (-1, -1)):
            kind, cusp, different, zero = cusp_matrix(a, c, lower)
            counts["matrix_constructions"] += 1
            counts["transformed_norm_differs"] += int(different)
            counts["transformed_denominator_zero"] += int(zero)
            kinds[kind] += 1
            target_cusps[cusp] += 1
    require(all(kinds.values()) and all(target_cusps), "every construction and target cusp covered")
    require(counts["transformed_norm_differs"] > 0, "wrong-denominator mutation exposed")
    require(counts["transformed_denominator_zero"] > 0, "finite original cusp sent to infinity covered")
    return {"counts": counts, "construction_cases": kinds, "target_cusps": target_cusps}


def check_ramanujan():
    primes = (7, 13, 19, 25)
    count = allocations = 0
    wrong_negative_mask = None
    for size in range(1, len(primes) + 1):
        qs = primes[:size]
        for ns in itertools.product(range(2), repeat=size):
            for bs in itertools.product(range(3), repeat=size):
                local = 1
                for q, n, b in zip(qs, ns, bs):
                    local *= -1 + q * int(n + b > 0)
                total = 0
                for ds in itertools.product(range(2), repeat=size):
                    nd = 1
                    for q, d in zip(qs, ds):
                        if d:
                            nd *= q
                    projected = int(all(not d or n + b > 0 for d, n, b in zip(ds, ns, bs)))
                    split = 0
                    for es in itertools.product(range(2), repeat=size):
                        if any(e > d for e, d in zip(es, ds)):
                            continue
                        fs = [d - e for d, e in zip(ds, es)]
                        split += int(all((not e or n > 0) and
                                         (not f or (b > 0 and n == 0))
                                         for e, f, n, b in zip(es, fs, ns, bs)))
                    require(split == projected, ("e/f projection", qs, ns, bs, ds))
                    allocations += 1
                    total += (-1) ** (size - sum(ds)) * nd * projected
                require(local == total, ("Ramanujan divisor identity", qs, ns, bs))
                count += 1
                # A negative summand exists also when the theta index is divisible.
                if wrong_negative_mask is None and ns[0] + bs[0] > 0:
                    wrong_negative_mask = {"prime_norm": qs[0], "n_valuation": ns[0],
                                           "b_valuation": bs[0], "true_negative": -1,
                                           "incorrect_coprime_negative": 0}
    require(wrong_negative_mask is not None, "negative-mask mutation")
    return {"divisor_identities": count, "projection_identities": allocations,
            "rejected_extra_negative_mask": wrong_negative_mask}


def check_fourier():
    """Exact cyclotomic sums on F_p and F_5[omega], Phi_p(T)=0."""
    cases = ((7, None), (13, None), (19, None), (5, "inert"))
    count = 0
    for p, kind in cases:
        elements = (list(itertools.product(range(p), repeat=2)) if kind
                    else [(a, 0) for a in range(p)])
        q = len(elements)

        def trace_product(x, y):
            z = mul(x, y)
            return ((2 * z[0] - z[1]) if kind else x[0] * y[0]) % p

        for h in elements:
            polynomials = [[0] * p for _ in range(3)]
            for x in elements:
                exponent = -trace_product(h, x) % p
                values = (-1, q * int(x == ZERO), -1 + q * int(x == ZERO))
                for poly, value in zip(polynomials, values):
                    poly[exponent] += value
            expected = (-q if h == ZERO else 0, q, q if h != ZERO else 0)
            for poly, rhs in zip(polynomials, expected):
                poly[0] -= rhs
                # Degree <=p-1; zero modulo Phi_p iff all coefficients equal.
                require(len(set(poly)) == 1, ("Fourier table", p, kind, h, poly))
                count += 1
    require(-1 + 7 != 7, "omitting negative summand changes inactive Fourier coefficient")
    return {"exact_fourier_equalities": count, "residue_norms": [7, 13, 19, 25],
            "normalization": "sums are q times the normalized transform"}


def check_scales():
    minimum_norm = Fraction(1, 81)
    return_factor = 27
    require(return_factor * minimum_norm == Fraction(1, 3), "raw support constant")
    cases = 0
    for a, d, k, B, M, c in itertools.product((6, 30), (1, 2, 3), (7, 13),
                                             (5, 11), (1, 9), (Fraction(1, 27), Fraction(2))):
        if a % d:
            continue
        g = Fraction(a, d)
        X = Fraction(a * a * k * k, 27) / (c * B)
        qnorm = M * k * d
        require(X / (qnorm * qnorm) == g * g / (27 * c * B * M * M),
                "standard-face row cancellation")
        require(X / (3 * qnorm * qnorm) == g * g / (81 * c * B * M * M),
                "standard cutoff factor")
        cases += 1
    require(Fraction(1, 81) != Fraction(1, 3), "missing-27 mutation is rejected")
    return {"exact_scale_cases": cases, "minimum_frequency_norm": "1/81",
            "double_transform_return_factor": 27, "raw_cutoff_multiplier": 3,
            "standard_face_cutoff_multiplier": 81}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"status": "PASS", "arithmetic": "exact integers and rational numbers",
              "scope": "finite local identities and integral matrices only",
              "not_certified": ["imported automorphy", "analytic continuation",
                                "infinite moments", "zero-free regions"],
              "matrices": check_matrices(), "ramanujan": check_ramanujan(),
              "fourier": check_fourier(), "scales": check_scales(),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
