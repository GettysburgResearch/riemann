#!/usr/bin/env python3
"""Independent calibration of Issue #26's scalar formula against D-0001.

The script evaluates Q_nn/(2*pi) and the translated Fejer scalar functional at
lattice carrier T=2*pi*n/log(c). Agreement is a normalization regression, not a
proof of the Guinand--Weil theorem.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_powers(c: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for p in primes_up_to(c):
        q = p
        while q <= c:
            out.append((q, p))
            if q > c // p:
                break
            q *= p
    return sorted(out)


def sinc(z: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return mp.sin(z) / z if z else mp.mpf(1)


def b_limit(L: mp.mpf) -> mp.mpf:
    return mp.mpf("0.25") - 1 / (2 * L)


def scalar_functional(c: int, n: int) -> mp.mpf:
    L = mp.log(c)
    Delta = L / (2 * mp.pi)
    T = 2 * mp.pi * n / L

    def h(z: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
        return Delta * sinc(mp.pi * Delta * z) ** 2

    def g(z: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
        return (h(z - T) + h(z + T)) / 2

    pole = 2 * g(mp.j / 2)
    prime = mp.mpf("0")
    for q, p in prime_powers(c):
        y = mp.log(q)
        prime += mp.log(p) / mp.sqrt(q) * (1 - y / L) * mp.cos(T * y)
    prime *= -1 / mp.pi

    def b_kernel(t: mp.mpf) -> mp.mpf:
        if abs(t) < mp.mpf("1e-25"):
            return b_limit(L)
        return mp.exp(-t / 4) / (1 - mp.exp(-t)) * (1 - t / (2 * L)) - 1 / t

    integral = mp.quad(lambda t: b_kernel(t) * mp.cos(T * t / 2), [0, 2 * L])
    arch = (mp.log(T / (2 * mp.pi)) - mp.ci(L * T) - integral) / (2 * mp.pi)
    return mp.re(pole + arch + prime)


def geometric(n: int, L: mp.mpf) -> tuple[mp.mpf, ...]:
    w = 2 * mp.pi * n / L
    w2 = w * w
    g_s = g_cc = g_x1 = g_x2 = mp.mpf("0")
    for k in range(10000):
        c_k = mp.mpf(2 * k) + mp.mpf("0.5")
        e_k = mp.exp(-c_k * L)
        den = c_k * c_k + w2
        g_s += e_k / den
        g_cc += e_k * w2 / (c_k * den)
        g_x1 += e_k * c_k / den
        g_x2 += e_k * (c_k * c_k - w2) / (den * den)
        if e_k < mp.mpf("1e-90"):
            break
    return g_s, g_cc, g_x1, g_x2


def matrix_diagonal(c: int, n: int) -> mp.mpf:
    L = mp.log(c)
    pi = mp.pi
    z = mp.mpc(mp.mpf("0.25"), pi * n / L)
    psi = mp.digamma(z)
    psi1 = mp.polygamma(1, z)
    _, g_cc, g_x1, g_x2 = geometric(n, L)
    CC = -(mp.re(psi) - mp.digamma(mp.mpf("0.25"))) / 2 + g_cc
    XC = mp.re(psi1) / 4 - L * g_x1 - g_x2
    eL = mp.exp(L)
    kappa = mp.log(4 * pi * (eL - 1) / (eL + 1)) + mp.euler
    U = mp.exp(L / 2)
    J = -2 * mp.log(U + 1) + mp.log(U * U + 1) + 2 * mp.atan(U) + mp.log(2) - pi / 2
    prefactor = 32 * L * mp.sinh(L / 4) ** 2
    w02 = prefactor * (L * L - 16 * pi * pi * n * n) / (L * L + 16 * pi * pi * n * n) ** 2
    wp = mp.mpf("0")
    for q, p in prime_powers(c):
        y = mp.log(q)
        wp += mp.log(p) / mp.sqrt(q) * 2 * (1 - y / L) * mp.cos(2 * pi * n * y / L)
    return (w02 - (kappa + 2 * CC + J - (2 / L) * XC) - wp) / (2 * pi)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    mp.mp.dps = args.dps
    rows = []
    for c in (13, 100):
        for n in (1, 2, 3, 8, 50):
            scalar = scalar_functional(c, n)
            diagonal = matrix_diagonal(c, n)
            error = abs(scalar - diagonal)
            rows.append(
                {
                    "c": c,
                    "n": n,
                    "scalar": mp.nstr(scalar, 45),
                    "matrix_diagonal_over_2pi": mp.nstr(diagonal, 45),
                    "absolute_error": mp.nstr(error, 20),
                }
            )
            if error > mp.mpf("1e-35"):
                raise AssertionError((c, n, error))
    result = {"status": "PASS", "rows": rows}
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
