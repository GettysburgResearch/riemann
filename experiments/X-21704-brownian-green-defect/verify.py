#!/usr/bin/env python3
"""Exact replay for L-21707 using only integers and fractions.Fraction."""
from __future__ import annotations

from fractions import Fraction
from math import comb
import hashlib
import json


def H(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def omega(k: int) -> Fraction:
    return Fraction(comb(2 * k, k) ** 2, 16 ** k)


def p_int(k: int, n: int) -> Fraction:
    if n < 0 or n > k:
        return Fraction(0)
    return Fraction(comb(2 * k, k - n), 4 ** k)


def raw_C(k: int, n: int) -> Fraction:
    if n > k:
        return Fraction(0)
    return 4 * Fraction(comb(2 * k, k - n) ** 2, comb(2 * k, k) ** 2)


def delta_H(k: int, n: int) -> Fraction:
    return H(k + n) - H(k - n)


def normalize(ws: list[Fraction]) -> list[Fraction]:
    z = sum(ws, Fraction(0))
    assert z > 0
    return [w / z for w in ws]


def families(N: int) -> dict[str, list[Fraction]]:
    raw = [Fraction(0)] * N
    raw[-1] = Fraction(1)
    harmonic = normalize([Fraction(1, k) for k in range(1, N + 1)])
    cb = normalize([omega(k) for k in range(1, N + 1)])
    return {"raw": raw, "harmonic": harmonic, "central_binomial": cb}


def green_values(N: int, lam: list[Fraction], n: int) -> tuple[Fraction, Fraction]:
    G = Fraction(0)
    Gp = Fraction(0)
    for k in range(max(1, n), N + 1):
        c = lam[k - 1] / omega(k)
        p = p_int(k, n)
        pp = -p * delta_H(k, n)
        G += c * p * p
        Gp += 2 * c * p * pp
    return G, Gp


def direct_linear_coefficient(N: int, lam: list[Fraction], n: int) -> tuple[Fraction, Fraction]:
    # Return intercept + slope*s in the coefficient multiplying n^{-s}.
    intercept = Fraction(0)
    slope = Fraction(0)
    for k in range(max(1, n), N + 1):
        C = raw_C(k, n)
        intercept += lam[k - 1] * C * (n * delta_H(k, n) - Fraction(1, 2))
        slope += lam[k - 1] * C * Fraction(1, 2)
    return intercept, slope


def finite_product(k: int, q: Fraction) -> Fraction:
    out = Fraction(1)
    for j in range(1, k + 1):
        out *= Fraction(j ** 4, 1) / (Fraction(j * j, 1) + q) ** 2
    return out


def run() -> dict:
    coefficient_rows = 0
    normalization_rows = 0
    product_rows = 0
    wallis_rows = 0

    for N in range(1, 17):
        for name, lam in families(N).items():
            assert sum(lam, Fraction(0)) == 1, name
            # G_lambda(0)=sum lambda_k/omega_k*p_k(0)^2=1.
            G0 = sum((lam[k - 1] / omega(k)) * p_int(k, 0) ** 2 for k in range(1, N + 1))
            assert G0 == 1
            normalization_rows += 1
            for n in range(1, N + 1):
                direct_i, direct_s = direct_linear_coefficient(N, lam, n)
                G, Gp = green_values(N, lam, n)
                pred_i = -2 * G - 2 * n * Gp
                pred_s = 2 * G
                assert (direct_i, direct_s) == (pred_i, pred_s)
                coefficient_rows += 1

    # Exact finite-product ordering underlying A_lambda(y)>=0.
    for q in [Fraction(1, 7), Fraction(1, 2), Fraction(3, 2), Fraction(5, 1), Fraction(19, 3)]:
        for M in range(2, 18):
            PM = finite_product(M, q)
            for K in range(1, M):
                assert finite_product(K, q) > PM
                product_rows += 1

    # Elementary Wallis lower bound used for the convergence rate.
    for k in range(1, 513):
        assert omega(k) >= Fraction(1, 4 * k)
        if k < 512:
            assert omega(k + 1) / omega(k) == Fraction((2 * k + 1) ** 2, (2 * k + 2) ** 2)
            assert Fraction((2 * k + 1) ** 2, (2 * k + 2) ** 2) >= Fraction(k, k + 1)
        wallis_rows += 1

    # Mutations: each must be rejected.
    mutations = 0
    N = 8
    lam = families(N)["central_binomial"]
    n = 3
    direct_i, direct_s = direct_linear_coefficient(N, lam, n)
    G, Gp = green_values(N, lam, n)
    assert direct_s != G  # missing factor 2
    mutations += 1
    assert direct_i != -2 * G + 2 * n * Gp  # derivative sign reversed
    mutations += 1
    q = Fraction(3, 2)
    assert finite_product(3, q) != finite_product(9, q)  # false finite/infinite equality
    mutations += 1
    bad = normalize([Fraction(1, k * k) for k in range(1, N + 1)])
    assert bad != lam  # central-binomial producer cannot be silently changed
    mutations += 1

    result = {
        "verdict": "PASS_EXACT_BROWNIAN_GREEN_DEFECT_ALGEBRA",
        "coefficient_rows": coefficient_rows,
        "normalization_rows": normalization_rows,
        "finite_product_order_rows": product_rows,
        "wallis_rows": wallis_rows,
        "mutation_tests": f"{mutations}/{mutations}",
        "scope": "finite rational algebra only; contour identity, zero location, BLNRZ, and RH are not certified",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
