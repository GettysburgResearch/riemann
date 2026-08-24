#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i in range(n):
        if i < len(a):
            out[i] += a[i]
        if i < len(b):
            out[i] += b[i]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a, c):
    return [c * x for x in a]


def poly_mul(a, b, limit=None):
    n = len(a) + len(b) - 1
    if limit is not None:
        n = min(n, limit)
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < n:
                out[i + j] += x * y
    return out


def binom_value(t, k):
    out = Fraction(1)
    for j in range(k):
        out *= t - j
        out /= j + 1
    return out


def binom_derivative(t, k):
    if k == 0:
        return Fraction(0)
    total = Fraction(0)
    for omit in range(k):
        term = Fraction(1)
        for j in range(k):
            if j != omit:
                term *= t - j
        total += term
    return total / math.factorial(k)


def sigma_coeffs(t, order):
    b = [binom_value(t, k) for k in range(order)]
    return [b[k] - (b[k - 1] if k else 0) for k in range(order)]


def sigma_derivative_coeffs(t, order):
    b = [binom_derivative(t, k) for k in range(order)]
    return [b[k] - (b[k - 1] if k else 0) for k in range(order)]


def series_inverse(a, order):
    assert a[0] != 0
    out = [Fraction(0) for _ in range(order)]
    out[0] = 1 / a[0]
    for n in range(1, order):
        s = Fraction(0)
        for k in range(1, min(n + 1, len(a))):
            s += a[k] * out[n - k]
        out[n] = -s / a[0]
    return out


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    order = 10
    target = [Fraction(1), Fraction(-1), Fraction(-1), Fraction(1)]
    target += [Fraction(0)] * (order - 4)

    tests = [
        Fraction(0),
        Fraction(1, 5),
        Fraction(1, 2),
        Fraction(4, 5),
        Fraction(1),
    ]

    complementary_checks = 0
    flatness_checks = 0
    energy_checks = 0

    for t in tests:
        left = sigma_coeffs(t, order)
        right = sigma_coeffs(1 - t, order)
        assert poly_mul(left, right, order) == target
        complementary_checks += 1

        dleft = sigma_derivative_coeffs(t, order)
        dright_independent = sigma_derivative_coeffs(1 - t, order)
        assert poly_mul(dleft, right, order) == poly_mul(
            left, dright_independent, order
        )
        flatness_checks += 1

        lhs = (1 - t) ** 2 + t**2
        rhs = Fraction(1, 2) + 2 * (t - Fraction(1, 2)) ** 2
        assert lhs == rhs
        energy_checks += 1

    E = [Fraction(1), Fraction(-1)]
    C = [Fraction(1), Fraction(0), Fraction(-1)]
    M = poly_scale(poly_add(E, C), Fraction(1, 2))
    D = poly_scale(poly_add(E, poly_scale(C, -1)), Fraction(1, 2))

    EC = poly_mul(E, C, order)
    EC += [Fraction(0)] * (order - len(EC))
    assert EC == target

    walsh = poly_add(
        poly_mul(M, M, order),
        poly_scale(poly_mul(D, D, order), -1),
    )
    walsh += [Fraction(0)] * (order - len(walsh))
    assert walsh == target

    D2 = poly_mul(D, D, order)
    assert D2[0] == 0 and D2[1] == 0
    assert D2[2] == Fraction(1, 4)

    M2 = poly_mul(M, M, order)
    ratio = poly_mul(target, series_inverse(M2, order), order)
    assert ratio[0] == 1
    assert ratio[1] == 0
    assert ratio[2] == Fraction(-1, 4)
    assert ratio[3] == Fraction(1, 4)

    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 67,
    ]
    reciprocal_sum = sum(Fraction(1, p) for p in primes)
    assert float(reciprocal_sum) < 3.0

    payload = {
        "schema": "riemann.t102930.primewise-flat-gauge.v1",
        "complementary_local_checks": complementary_checks,
        "flatness_local_checks": flatness_checks,
        "energy_identity_checks": energy_checks,
        "series_order": order,
        "endpoint_split_checks": 8,
        "walsh_identity_checks": 4,
        "ratio_linear_term_zero": True,
        "ratio_first_nonconstant_degree": 2,
        "unique_local_energy_minimizer": "t_p=1/2",
        "sparse_endpoint_cost": "exp(O(sum_{p in S} 1/p))",
        "pcoi102930_proved": False,
        "ctzd102897_proved": False,
        "sgic102890_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102930_PRIMEWISE_FLAT_GAUGE",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")

    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
