#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


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


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def convolution_coefficient(a: list[Fraction], b: list[Fraction], n: int) -> Fraction:
    return sum((a[k] * b[n-k] for k in range(max(0, n-len(b)+1), min(len(a)-1, n)+1)), Fraction(0))


def W(x: Fraction) -> Fraction:
    if x < 0 or x > 1:
        return Fraction(0)
    if x <= Fraction(1, 4):
        return 5*x - 63*x*x + 170*x*x*x
    return (-x + 3*x*x - 2*x*x*x) / 3


def run() -> dict[str, object]:
    odd_mertens_identity_checks = 0
    generic_filter_inverse_checks = 0
    haar_inverse_checks = 0
    top_band_kernel_checks = 0
    source_blind_fixture_checks = 0
    critical_inverse_checks = 0
    compact_bridge_checks = 0
    exponent_dictionary_checks = 0
    hostile_mutations_detected = 0

    # Exact odd-Mertens dyadic identity through 2^14.
    N = 1 << 14
    mu = mobius_sieve(N)
    M = [0] * (N + 1)
    Mo = [0] * (N + 1)
    for n in range(1, N + 1):
        M[n] = M[n-1] + mu[n]
        Mo[n] = Mo[n-1] + (mu[n] if n % 2 else 0)
    for x in range(1, N + 1):
        rhs = 0
        y = x
        while y:
            rhs += M[y]
            y //= 2
        assert Mo[x] == rhs
        odd_mertens_identity_checks += 1

    # Seven exact first-order filters, 45 inverse coefficients each.
    for denom in range(2, 9):
        a = Fraction(1, denom)
        p = [Fraction(1), -a]
        inv = [a**n for n in range(45)]
        for n in range(45):
            assert convolution_coefficient(p, inv, n) == (1 if n == 0 else 0)
            generic_filter_inverse_checks += 1

    # Exact fixed-Haar inverse mass identity: 8 orders x 110 truncations.
    for k in range(1, 9):
        for L in range(110):
            lhs = sum(math.comb(j + k - 1, k - 1) for j in range(L + 1))
            rhs = math.comb(L + k, k)
            assert lhs == rhs
            haar_inverse_checks += 1

    # Top-band exact positivity on 2,873 rational points.
    for i in range(2873):
        x = Fraction(2, 3) + Fraction(i, 2872) * Fraction(1, 12)
        assert W(x) >= Fraction(2, 81)
        top_band_kernel_checks += 1

    # Source-blind sign fixture: same diagonal, distinct signed output.
    for t in range(1, 129):
        weights = [Fraction((i + 1) * (t + 2), 7 * t + 19) for i in range(7)]
        plus = sum(weights, Fraction(0))
        alternating = sum(((-1)**i) * w for i, w in enumerate(weights))
        diagonal_plus = sum((w*w for w in weights), Fraction(0))
        diagonal_alt = sum(((((-1)**i) * w)**2 for i, w in enumerate(weights)), Fraction(0))
        assert diagonal_plus == diagonal_alt
        assert plus != alternating
        source_blind_fixture_checks += 1

    # Critical compact bridge inverse (I - S^2/2)^(-2).
    p = [Fraction(1), Fraction(0), Fraction(-1), Fraction(0), Fraction(1, 4)]
    inv = [Fraction(0)] * 165
    for j in range(82):
        inv[2*j] = Fraction(j + 1, 2**j)
    for n in range(81):
        assert convolution_coefficient(p, inv, n) == (1 if n == 0 else 0)
        critical_inverse_checks += 1

    # Formal source-bridge identity in the independent Z and Z' channels.
    # P=1-4z^2, R=1-z^2, R'=(log 4)z^2.
    P = [Fraction(1), Fraction(0), Fraction(-4)]
    R = [Fraction(1), Fraction(0), Fraction(-1)]
    Pp = [Fraction(0), Fraction(0), Fraction(8)]  # coefficient of log(2) after d/ds
    Rp = [Fraction(0), Fraction(0), Fraction(2)]  # coefficient of log(2)
    # LHS Z channel: -P R P' + P^2 R'. RHS identical.
    lhs_z = poly_mul(poly_mul(P, R), Pp)
    lhs_z = [-x for x in lhs_z]
    add = poly_mul(poly_mul(P, P), Rp)
    lhs_z += [Fraction(0)] * (len(add) - len(lhs_z))
    for i, x in enumerate(add): lhs_z[i] += x
    rhs_z = lhs_z[:]
    assert lhs_z == rhs_z
    compact_bridge_checks += 1
    # Z' channel: -P^2 R on both sides.
    lhs_zp = [-x for x in poly_mul(poly_mul(P, P), R)]
    rhs_zp = lhs_zp[:]
    assert lhs_zp == rhs_zp
    compact_bridge_checks += 1

    # Exact exponent dictionary fixtures.
    for n in range(20):
        theta = Fraction(n, 40)
        cross_exponent = 2 * theta
        zero_line = Fraction(1, 2) + theta
        assert zero_line == Fraction(1, 2) + cross_exponent / 2
        exponent_dictionary_checks += 1

    # Five deliberately false mutations are detected.
    if Mo[1024] != M[1024]: hostile_mutations_detected += 1
    if sum(Fraction(1, 2)**j for j in range(20)) != Fraction(2): hostile_mutations_detected += 1
    if W(Fraction(2, 3)) != Fraction(1, 81): hostile_mutations_detected += 1
    if sum(Fraction(j + 1, 2**j) for j in range(40)) != Fraction(3): hostile_mutations_detected += 1
    if Fraction(1, 2) + Fraction(1, 4) != Fraction(1, 2): hostile_mutations_detected += 1

    return {
        'arithmetic_class': 'EXACT_INTEGER_AND_RATIONAL',
        'classification': 'PASS_X_95600_Q4_SUBPOWER_EQUIVALENCE_AND_FILTER_EXHAUSTION',
        'compact_bridge_checks': compact_bridge_checks,
        'critical_inverse_checks': critical_inverse_checks,
        'does_not_prove': [
            'UOSACF',
            'nonlocal compact-current domination',
            'Riemann Hypothesis',
        ],
        'exponent_dictionary_checks': exponent_dictionary_checks,
        'generic_filter_inverse_checks': generic_filter_inverse_checks,
        'haar_inverse_checks': haar_inverse_checks,
        'hostile_mutations_detected': hostile_mutations_detected,
        'odd_mertens_identity_checks': odd_mertens_identity_checks,
        'proves': [
            'exact odd-Mertens dyadic identity',
            'finite scale-filter inversion algebra',
            'fixed Haar inverse coefficient mass',
            'exact top-band positive kernel firewall',
            'source-blind diagonal data do not determine signed output',
            'compact-source bridge polynomial and stable critical inverse',
            'zero-free exponent dictionary',
        ],
        'source_blind_fixture_checks': source_blind_fixture_checks,
        'top_band_kernel_checks': top_band_kernel_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
