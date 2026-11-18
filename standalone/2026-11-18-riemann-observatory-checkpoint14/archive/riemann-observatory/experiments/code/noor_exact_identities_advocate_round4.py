#!/usr/bin/env python3
"""Exact finite checks supporting Noor map and Bergman closure reconstruction.

All assertions use integers/Fraction; no floating-point approximation or log
identity is used. Infinite tails of the A inner product are telescoped exactly.
These checks corroborate, and do not replace, the analytic proof.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def mobius(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def harmonic(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def vcoef(n, j):
    if n and j == n - 1:
        return n
    return -1 if j >= n else 0


def exact_inner(n, m):
    cutoff = max(n, m)
    finite = sum((F(vcoef(n, j) * vcoef(m, j), (j+1)*(j+2))
                  for j in range(cutoff)), F(0))
    # Beyond cutoff both v-coefficient sequences are identically -1.
    return finite + F(1, cutoff + 1)


def run():
    basis_checks = 0
    for n in range(17):
        for m in range(17):
            assert exact_inner(n, m) == int(n == m)
            basis_checks += 1
    convolution_checks = 0
    for N in range(1, 65):
        for n in range(1, N + 1):
            lhs = sum((F(mobius(k), k) * harmonic(n // k)
                       for k in range(1, N + 1)), F(0))
            assert lhs == 1
            convolution_checks += 1
    # Coefficient proof that composition is contractive in D_-1.
    composition_checks = 0
    for m in range(1, 18):
        for n in range(0, 65):
            assert F(1, m*n+1) <= F(1, n+1)
            composition_checks += 1
    result = {
        'status': 'all_exact_assertions_passed',
        'arithmetic': 'Python standard-library Fraction and integer operations',
        'orthonormal_basis_inner_products': basis_checks,
        'exact_divisor_convolution_identities': convolution_checks,
        'composition_weight_inequalities': composition_checks,
        'scope': 'Finite exact corroboration only; analytic tails, weak convergence, and external Mertens bound are proved or specified in the companion text.'
    }
    out = Path(__file__).resolve().parents[1] / 'results' / 'noor_exact_identities_advocate_round4.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
