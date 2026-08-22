#!/usr/bin/env python3
"""Exact standard-library replay for L-90203 / T-90203 arithmetic cone."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"

def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]

def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    if n >= 1:
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

def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def primes_upto(n: int) -> list[int]:
    return [m for m in range(2, n + 1) if factor(m) == {m: 1}]

def conv(a: list[Fraction], b: list[Fraction], nmax: int) -> list[Fraction]:
    out = [Fraction(0)] * (nmax + 1)
    for n in range(1, nmax + 1):
        out[n] = sum((a[d] * b[n // d] for d in divisors(n)), Fraction(0))
    return out

def valuation_data(nmax: int) -> tuple[list[Fraction], list[Fraction]]:
    ell = [Fraction(0)] * (nmax + 1)
    for n in range(2, nmax + 1):
        fac = factor(n)
        if len(fac) == 1:
            p, a = next(iter(fac.items()))
            ell[n] = Fraction((3 * p + 5 * a) % 13 + 1, 17)
    g = [Fraction(0)] * (nmax + 1)
    for n in range(2, nmax + 1):
        value = Fraction(0)
        for p, a in factor(n).items():
            value += sum((ell[p**j] for j in range(1, a + 1)), Fraction(0))
        g[n] = value
    return ell, g

def vp(n: int, p: int) -> int:
    a = 0
    while n % p == 0:
        a += 1
        n //= p
    return a

def main() -> None:
    nmax = 180
    mui = mobius_sieve(nmax)
    mu = [Fraction(x) for x in mui]
    one = [Fraction(0)] + [Fraction(1)] * nmax

    # Deliberately nonmultiplicative positive h: this tests the enlarged cone.
    h = [Fraction(0)] * (nmax + 1)
    h[1] = Fraction(1)
    for n in range(2, nmax + 1):
        h[n] = Fraction((7 * n + 5) % 19, 23)

    b = conv(mu, h, nmax)
    assert conv(one, b, nmax) == h

    ell, g = valuation_data(nmax)
    mug = conv(mu, g, nmax)
    assert mug == ell
    bg = conv(b, g, nmax)
    hell = conv(h, ell, nmax)
    assert bg == hell
    domination_checks = 0
    for n in range(1, nmax + 1):
        assert bg[n] >= ell[n]
        domination_checks += 1

    # Embed a nontrivial rational point of the full real prime cube.
    primes = primes_upto(nmax)
    choices = [Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(1)]
    x = {p: choices[i % len(choices)] for i, p in enumerate(primes)}
    hx = [Fraction(0)] * (nmax + 1)
    bx_expected = [Fraction(0)] * (nmax + 1)
    hx[1] = bx_expected[1] = Fraction(1)
    cube_checks = 0
    for n in range(2, nmax + 1):
        fac = factor(n)
        hv = Fraction(1)
        for p in fac:
            hv *= 1 + x[p]
        hx[n] = hv
        if mui[n] != 0:
            bv = Fraction(1)
            for p in fac:
                bv *= x[p]
            bx_expected[n] = bv
        cube_checks += 1
    assert conv(mu, hx, nmax) == bx_expected

    # Maximality: localized v_p probes recover h(m) exactly at mp, p∤m.
    maximality_checks = 0
    for m in range(2, 80):
        for p in primes:
            if m % p != 0 and m * p <= nmax:
                gp = [Fraction(0)] * (nmax + 1)
                for n in range(1, nmax + 1):
                    gp[n] = Fraction(vp(n, p))
                bgp = conv(b, gp, nmax)
                assert bgp[m * p] == h[m]
                maximality_checks += 1
                break

    # Prime-power extraction sanity checks: complete additive and strong additive.
    loglike = [Fraction(0)] * (nmax + 1)
    strong = [Fraction(0)] * (nmax + 1)
    for n in range(2, nmax + 1):
        for p, a in factor(n).items():
            cost = Fraction((p % 11) + 1, 13)
            loglike[n] += a * cost
            strong[n] += cost
    mu_loglike = conv(mu, loglike, nmax)
    mu_strong = conv(mu, strong, nmax)
    extraction_checks = 0
    for n in range(2, nmax + 1):
        fac = factor(n)
        if len(fac) == 1:
            p, a = next(iter(fac.items()))
            cost = Fraction((p % 11) + 1, 13)
            assert mu_loglike[n] == cost
            assert mu_strong[n] == (cost if a == 1 else 0)
        else:
            assert mu_loglike[n] == 0
            assert mu_strong[n] == 0
        extraction_checks += 1

    result = {
        "verdict": "PASS_X_90203_POSITIVE_CONVOLUTION_CONE",
        "nmax": nmax,
        "convolution_inverse_checks": nmax,
        "valuation_domination_checks": domination_checks,
        "real_cube_embedding_checks": cube_checks,
        "maximality_probe_checks": maximality_checks,
        "prime_power_extraction_checks": extraction_checks,
        "nonmultiplicative_h": True,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
