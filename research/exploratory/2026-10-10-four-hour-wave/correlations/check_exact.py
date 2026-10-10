#!/usr/bin/env python3
"""Exact finite controls for the correlation identities, with no global extrapolation."""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import hashlib
import json
import math
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def omega_mu(n: int) -> tuple[int, int]:
    total, mu, p = 0, 1, 2
    while p*p <= n:
        power = 0
        while n % p == 0:
            n //= p
            power += 1
        if power:
            total += power
            mu = -mu if power == 1 else 0
        p += 1
    if n > 1:
        total += 1
        mu = -mu
    return total, mu


def real_window_check(a: tuple[int, ...], width: int) -> None:
    n = len(a)
    windows = [sum(a[j-h-1] if 1 <= j-h <= n else 0
                   for h in range(width)) for j in range(1, n+width)]
    corr = [sum(a[k+d]*a[k] for k in range(n-d)) for d in range(1, width)]
    signed = width*sum(x*x for x in a) + 2*sum(
        (width-d)*c for d, c in enumerate(corr, 1))
    require(sum(windows) == width*sum(a), "zero-extended endpoint multiplicity")
    require(sum(x*x for x in windows) == signed, "signed pair-count identity C1")
    require(width**2*sum(a)**2 <= (n+width-1)*signed, "signed Cauchy inequality C2")
    absolute = width*n + 2*sum((width-d)*abs(c) for d, c in enumerate(corr, 1))
    require(width**2*sum(a)**2 <= (n+width-1)*absolute, "absolute inequality C3")


def gaussian_controls() -> int:
    # Gaussian rational pairs avoid machine complex arithmetic entirely.
    def add(z, w):
        return z[0]+w[0], z[1]+w[1]
    def conjugate(z):
        return z[0], -z[1]
    def multiply(z, w):
        return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]
    def norm2(z):
        return z[0]**2+z[1]**2
    def total(values):
        answer = (Q(0), Q(0))
        for value in values:
            answer = add(answer, value)
        return answer
    a = [(Q(1, 2), Q(1, 3)), (Q(-2, 5), Q(3, 7)),
         (Q(0), Q(-1)), (Q(1), Q(0)), (Q(-1, 4), Q(-1, 5))]
    n = len(a)
    for width in range(1, n+1):
        windows = [total(a[j-h-1] if 1 <= j-h <= n else (Q(0), Q(0))
                         for h in range(width)) for j in range(1, n+width)]
        corr = [total(multiply(a[k+d], conjugate(a[k])) for k in range(n-d))
                for d in range(1, width)]
        signed = width*sum(norm2(x) for x in a)+2*sum(
            (width-d)*c[0] for d, c in enumerate(corr, 1))
        require(sum(norm2(x) for x in windows) == signed, "complex C1")
        require(width**2*norm2(total(a)) <= (n+width-1)*signed, "complex C2")
    return n


def certificate() -> dict:
    real_controls = 0
    for n in range(1, 9):
        for a in product((-1, 1), repeat=n):
            for width in range(1, n+1):
                real_window_check(a, width)
                real_controls += 1
    for n in range(1, 1025):
        om, mu = omega_mu(n)
        transformed = sum(omega_mu(d)[1] * (-1)**omega_mu(n//(d*d))[0]
                          for d in range(1, math.isqrt(n)+1) if n % (d*d) == 0)
        require(mu == transformed, f"literal square-divisor identity at {n}")
        require((-1)**om in (-1, 1), "Liouville range")

    # Compare the log-prime coefficients in C8, avoiding numerical logarithms.
    cutoff, r = 128, Q(1, 4)
    g = [Q(0)] + [r**omega_mu(n)[0] for n in range(1, cutoff+1)]
    prime_controls = 0
    for p in range(2, cutoff+1):
        if omega_mu(p)[0] != 1:
            continue
        left = Q(0)
        for n in range(1, cutoff+1):
            m, power = n, 0
            while m % p == 0:
                m //= p
                power += 1
            left += power*g[n]
        right, power, pk = Q(0), 1, p
        while pk <= cutoff:
            right += sum(g[m]*r**power for m in range(1, cutoff//pk+1))
            power += 1
            pk *= p
        require(left == right, f"Chebyshev convolution coefficient at prime {p}")
        prime_controls += 1
    return {"status": "EXACT_FINITE_CONTROLS_PASS", "real_window_controls": real_controls,
            "gaussian_rational_window_controls": gaussian_controls(),
            "square_divisor_controls": 1024, "prime_coefficient_controls": prime_controls,
            "infinite_classical_inputs_reverified": False, "rh_proved": False,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))
