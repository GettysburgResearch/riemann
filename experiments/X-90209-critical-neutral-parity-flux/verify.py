#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import mpmath as mp

mp.mp.dps = 90
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"
SQ2 = mp.sqrt(2)
Y0 = mp.mpf(3) / 2 + SQ2
ENDPOINTS = (8, 9, 16, 31, 64, 127, 256, 1000, 4096)


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
            ip = i * p
            if ip > n:
                break
            composite[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def kappa(y: mp.mpf) -> mp.mpf:
    if y < 1 or y >= 8:
        return mp.mpf("0")
    if y < 2:
        return y ** (-mp.mpf(1) / 2) - 1
    if y < 4:
        return SQ2 - (1 + SQ2) * y ** (-mp.mpf(1) / 2)
    return SQ2 * y ** (-mp.mpf(1) / 2) - mp.mpf(1) / 2


def source_b(mu: list[int], n: int) -> mp.mpf:
    v = mp.mpf(mu[n])
    if n % 2 == 0:
        v -= (1 + SQ2) * mu[n // 2]
    if n % 4 == 0:
        v += SQ2 * mu[n // 4]
    return v


def hinge(X: int, q: int) -> mp.mpf:
    if q < 2 or q > X:
        return mp.mpf("0")
    return mp.mpf(q) ** (-mp.mpf(1) / 2) - mp.mpf(X) ** (-mp.mpf(1) / 2)


def direct_k(X: int, mu: list[int]) -> mp.mpf:
    return -mp.fsum(source_b(mu, q) * hinge(X, q) for q in range(2, X + 1))


def multiples_u(X: int, m: int, mu: list[int]) -> mp.mpf:
    return mp.fsum(mu[k] * hinge(X, m * k) for k in range(1, X // m + 1))


def three_source_k(X: int, mu: list[int]) -> mp.mpf:
    return (1 + SQ2) * multiples_u(X, 2, mu) - multiples_u(X, 1, mu) - SQ2 * multiples_u(X, 4, mu)


def odd_annulus_k(X: int, mu: list[int]) -> mp.mpf:
    total = 1 - mp.mpf(X) ** (-mp.mpf(1) / 2)
    lo = X / 8
    for m in range(1, X + 1, 2):
        if m <= lo or mu[m] == 0:
            continue
        total += mu[m] * mp.mpf(m) ** (-mp.mpf(1) / 2) * kappa(mp.mpf(X) / m)
    return total


def mertens_prefix(mu: list[int]) -> list[int]:
    out = [0] * len(mu)
    s = 0
    for i in range(1, len(mu)):
        s += mu[i]
        out[i] = s
    return out


def flux_integral(X: int, M: list[int]) -> mp.mpf:
    a = mp.mpf(X) / 4
    b = mp.mpf(X) / 2
    points = {a, b}
    for n in range(math.floor(a) + 1, math.ceil(b)):
        if a < n < b:
            points.add(mp.mpf(n))
    for n in range(math.floor(2 * a) + 1, math.ceil(2 * b)):
        p = mp.mpf(n) / 2
        if a < p < b:
            points.add(p)
    pts = sorted(points)
    total = mp.mpf("0")
    for left, right in zip(pts, pts[1:]):
        mid = (left + right) / 2
        m1 = M[int(mp.floor(mid))]
        m2 = M[int(mp.floor(2 * mid))]
        total += (m1 - m2) * 2 * (left ** (-mp.mpf(1) / 2) - right ** (-mp.mpf(1) / 2))
    return total


def flux_k(X: int, M: list[int]) -> mp.mpf:
    return 1 - mp.mpf(X) ** (-mp.mpf(1) / 2) + flux_integral(X, M) / (2 * SQ2)


def graph_checks(X: int, mu: list[int]) -> tuple[int, int]:
    active = [m for m in range(1, X + 1, 2) if 8 * m > X and mu[m] != 0 and kappa(mp.mpf(X) / m) != 0]
    active_set = set(active)
    edges = 0
    colors = 0
    for m in active:
        for p in (3, 5, 7):
            n = p * m
            if n not in active_set:
                continue
            edges += 1
            y = mp.mpf(X) / n
            assert 1 <= y < mp.mpf(8) / p <= mp.mpf(8) / 3 < Y0
            assert p * y >= p > Y0 and p * y < 8
            c_m = mp.sign(mu[m] * kappa(mp.mpf(X) / m))
            c_n = mp.sign(mu[n] * kappa(mp.mpf(X) / n))
            assert c_m == c_n
            colors += 1
    return edges, colors


def corrected_forcing(x: mp.mpf) -> mp.mpf:
    N = int(mp.floor(x))
    J = mp.fsum(mp.mpf(d) ** (-mp.mpf(1) / 2) for d in range(1, N + 1)) - N / mp.sqrt(x)
    if x < 2:
        return mp.mpf("0")
    if x < 4:
        return 6 * J - 6 + 9 / SQ2 - 3 / mp.sqrt(x)
    return 6 * J - mp.mpf(15) / 2 + 9 / SQ2


def old_large_forcing(x: mp.mpf) -> mp.mpf:
    N = int(mp.floor(x))
    J = mp.fsum(mp.mpf(d) ** (-mp.mpf(1) / 2) for d in range(1, N + 1)) - N / mp.sqrt(x)
    return 6 * J - mp.mpf(15) / 2 + 9 / SQ2


def canonical_omega(mu: list[int], n: int) -> int:
    value = 2 * mu[n]
    if n % 2 == 0:
        value -= 3 * mu[n // 2]
    if n % 4 == 0:
        value += mu[n // 4]
    return value


def canonical_h(X: int, mu: list[int]) -> mp.mpf:
    return -3 * mp.fsum(canonical_omega(mu, q) * hinge(X, q) for q in range(2, X + 1))


def forcing_inversion(X: int, mu: list[int], forcing) -> mp.mpf:
    return mp.fsum(mu[d] / mp.sqrt(d) * forcing(mp.mpf(X) / d) for d in range(1, X + 1))


def main() -> None:
    mu = mobius_sieve(2 * max(ENDPOINTS) + 10)
    M = mertens_prefix(mu)
    max_direct_three = mp.mpf("0")
    max_direct_annulus = mp.mpf("0")
    max_direct_flux = mp.mpf("0")
    total_edges = 0
    total_color_checks = 0
    rows = []

    for X in ENDPOINTS:
        d = direct_k(X, mu)
        t = three_source_k(X, mu)
        a = odd_annulus_k(X, mu)
        f = flux_k(X, M)
        e1 = abs(d - t)
        e2 = abs(d - a)
        e3 = abs(d - f)
        max_direct_three = max(max_direct_three, e1)
        max_direct_annulus = max(max_direct_annulus, e2)
        max_direct_flux = max(max_direct_flux, e3)
        edges, colors = graph_checks(X, mu)
        total_edges += edges
        total_color_checks += colors
        rows.append({
            "X": X,
            "K": mp.nstr(d, 35),
            "direct_vs_three": mp.nstr(e1, 8),
            "direct_vs_annulus": mp.nstr(e2, 8),
            "direct_vs_flux": mp.nstr(e3, 8),
            "divisor_edges": edges,
        })

    assert max_direct_three < mp.mpf("1e-75")
    assert max_direct_annulus < mp.mpf("1e-75")
    assert max_direct_flux < mp.mpf("1e-75")
    assert total_edges == total_color_checks

    # Boundary-repair mutation and corrected inversion.
    old_at_two = forcing_inversion(2, mu, old_large_forcing)
    true_at_two = canonical_h(2, mu)
    assert abs(true_at_two) < mp.mpf("1e-80")
    assert old_at_two > mp.mpf("1")
    max_corrected_error = mp.mpf("0")
    for X in range(2, 257):
        err = abs(canonical_h(X, mu) - forcing_inversion(X, mu, corrected_forcing))
        max_corrected_error = max(max_corrected_error, err)
    assert max_corrected_error < mp.mpf("1e-75")

    result = {
        "verdict": "PASS_X_90209_CRITICAL_NEUTRAL_PARITY_FLUX",
        "endpoints": rows,
        "max_errors": {
            "direct_vs_three": mp.nstr(max_direct_three, 12),
            "direct_vs_annulus": mp.nstr(max_direct_annulus, 12),
            "direct_vs_flux": mp.nstr(max_direct_flux, 12),
            "corrected_forcing_inversion": mp.nstr(max_corrected_error, 12),
        },
        "graph": {
            "edges_checked": total_edges,
            "color_equalities": total_color_checks,
            "allowed_primes": [3, 5, 7],
            "zero": mp.nstr(Y0, 40),
        },
        "boundary_repair": {
            "true_H_2": mp.nstr(true_at_two, 20),
            "old_unqualified_inversion_at_2": mp.nstr(old_at_two, 30),
        },
        "scope": "exact identities and parity firewall only; no Mertens-flux bound and no RH proof",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])


if __name__ == "__main__":
    main()
