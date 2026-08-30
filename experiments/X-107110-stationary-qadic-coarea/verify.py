#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import floor, gcd
from pathlib import Path


def mobius(n: int) -> int:
    m, parity, p = n, 0, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            parity ^= 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        parity ^= 1
    return -1 if parity else 1


def omega(n: int) -> int:
    m, count, p = n, 0, 2
    while p * p <= m:
        if m % p == 0:
            count += 1
            while m % p == 0:
                m //= p
        p += 1
    return count + (1 if m > 1 else 0)


def shifted_bin_energy(xs: list[F], coeffs: list[F]) -> F:
    breaks = {F(0), F(1)}
    for x in xs:
        breaks.add(x - floor(x))
    points = sorted(breaks)
    total = F(0)
    for left, right in zip(points, points[1:]):
        if left == right:
            continue
        tau = (left + right) / 2
        bins: dict[int, F] = {}
        for x, coeff in zip(xs, coeffs):
            j = floor(x - tau)
            bins[j] = bins.get(j, F(0)) + coeff
        total += (right - left) * sum(value * value for value in bins.values())
    return total


def triangular_pair_energy(xs: list[F], coeffs: list[F]) -> F:
    return sum(
        coeffs[i] * coeffs[j] * max(F(0), F(1) - abs(x - y))
        for i, x in enumerate(xs)
        for j, y in enumerate(xs)
    )


def prefix_max(xs: list[F], coeffs: list[F]) -> F:
    running = out = F(0)
    for index in sorted(range(len(xs)), key=xs.__getitem__):
        running += coeffs[index]
        out = max(out, abs(running))
    return out


def core_identity(y: int, q: int, z: F) -> tuple[F, F]:
    values = [n for n in range(1, y + 1) if n % q and mobius(n)]

    def kernel(a: int, b: int) -> F:
        return F(1) if max(a, b) <= q * min(a, b) else F(0)

    original = sum(
        mobius(m) * mobius(n) * z ** (omega(m) + omega(n)) * kernel(m, n)
        for m in values
        for n in values
    )
    by_core = F(0)
    for d in values:
        core_weight = z ** (2 * omega(d))
        for a in values:
            if d * a > y or gcd(a, d * q) != 1:
                continue
            for b in values:
                if d * b > y or gcd(b, d * q) != 1 or gcd(a, b) != 1:
                    continue
                by_core += (
                    core_weight
                    * mobius(a)
                    * mobius(b)
                    * z ** (omega(a) + omega(b))
                    * kernel(a, b)
                )
    return original, by_core


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = 0

    fixtures = [
        ([F(0), F(1, 3), F(7, 6)], [F(2), F(-1), F(3)]),
        ([F(1, 7), F(4, 7), F(8, 7), F(13, 7)], [F(1), F(2), F(-3), F(4)]),
        ([F(1, 11), F(5, 11), F(9, 11), F(14, 11), F(20, 11)], [F(3), F(-2), F(5), F(-1), F(4)]),
    ]
    for xs, coeffs in fixtures:
        energy = shifted_bin_energy(xs, coeffs)
        assert energy == triangular_pair_energy(xs, coeffs)
        checks += 1
        maximum = prefix_max(xs, coeffs)
        assert maximum * maximum <= len(xs) * energy
        checks += 1

    for y in (10, 20, 30, 50, 70):
        assert core_identity(y, 5, F(1, 2))[0] == core_identity(y, 5, F(1, 2))[1]
        checks += 1

    for y in (50, 100, 250):
        for r in (2, 5, 10):
            for d in range(y // r + 1, y + 1):
                for a in range(1, y // d + 1):
                    for b in range(1, y // d + 1):
                        assert max(a, b) < r
                        checks += 1

    data = {
        "claim": "T-107110",
        "verdict": "PASS_T107110_STATIONARY_QADIC_COAREA",
        "checks": checks,
        "coarea_identity_exact": True,
        "primitive_core_reindexing_exact": True,
        "high_primitive_estimate_proved": False,
        "rh_established": False,
        "scope": "exact finite rational coarea, prefix, and squarefree-core algebra",
    }
    data["proof_object"] = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(data["verdict"])
    print(f"checks={checks}")
    print(data["proof_object"])


if __name__ == "__main__":
    main()
