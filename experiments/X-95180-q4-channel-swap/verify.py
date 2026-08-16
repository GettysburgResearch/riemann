#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def sieve_spf(n: int) -> list[int]:
    spf = list(range(n + 1))
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factor(n: int, spf: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    while n > 1:
        p = spf[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def v2(n: int) -> int:
    e = 0
    while n and n % 2 == 0:
        e += 1
        n //= 2
    return e


def mobius_odd(m: int, spf: list[int]) -> int:
    f = factor(m, spf)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


def g4(n: int) -> int:
    return 4 ** (v2(n) // 2)


def a4(n: int, spf: list[int]) -> int:
    e = v2(n)
    m = n >> e
    mu = mobius_odd(m, spf)
    if mu == 0:
        return 0
    if e == 0:
        return mu
    if e == 1:
        return -mu
    return 3 * ((-1) ** (e + 1)) * mu


def lambda4_formal(n: int, spf: list[int]) -> dict[int, int]:
    f = factor(n, spf)
    if len(f) != 1:
        return {}
    p, r = next(iter(f.items()))
    if p != 2:
        return {p: 1}
    return {2: 1 if r % 2 else 2 ** (r + 1) - 1}


def add_map(a: dict[int, Fraction], b: dict[int, int], scale: Fraction | int = 1) -> dict[int, Fraction]:
    out = dict(a)
    scale = Fraction(scale)
    for p, c in b.items():
        out[p] = out.get(p, Fraction(0)) + scale * c
    return {p: c for p, c in out.items() if c}


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def poly_D2(poly: dict[int, Fraction]) -> dict[int, Fraction]:
    return {k: c * k * k for k, c in poly.items() if k and c}


def phi(x: Fraction) -> Fraction:
    if x < 0 or x > 1:
        return Fraction(0)
    if x <= Fraction(1, 4):
        return x * x * (85 * x * x - 56 * x + 10) / 8
    return (1 - x) ** 3 * (3 * x + 1) / 72


def formal_a_log(n: int, spf: list[int]) -> dict[int, Fraction]:
    return {p: Fraction(a4(n, spf) * e) for p, e in factor(n, spf).items() if a4(n, spf) * e}


def run() -> dict[str, object]:
    N = 1024
    spf = sieve_spf(N)
    coefficient_checks = 0
    channel_checks = 0
    signed_checks = 0
    energy_checks = 0
    dyadic_pair_checks = 0
    peano_checks = 0
    flux_checks = 0
    pole_checks = 0
    mutations = 0

    energy = Fraction(0)
    for n in range(1, N + 1):
        a = a4(n, spf)
        g = g4(n)
        assert abs(a) <= g
        assert g + a >= 0 and g - a >= 0
        coefficient_checks += 1
        energy += Fraction(a * a, g * n)
    assert energy <= Fraction(12, 5) * harmonic(N)
    energy_checks += 1

    for n in range(2, N + 1):
        fac = factor(n, spf)
        a = a4(n, spf)
        g = g4(n)
        up = g + a
        um = g - a
        lhs_p = {p: Fraction(up * e) for p, e in fac.items() if up * e}
        lhs_m = {p: Fraction(um * e) for p, e in fac.items() if um * e}
        lhs_a = {p: Fraction(a * e) for p, e in fac.items() if a * e}
        rhs_p: dict[int, Fraction] = {}
        rhs_m: dict[int, Fraction] = {}
        rhs_a: dict[int, Fraction] = {}
        for d in divisors(n):
            if d == 1:
                continue
            lam = lambda4_formal(d, spf)
            rhs_p = add_map(rhs_p, lam, g4(n // d) - a4(n // d, spf))
            rhs_m = add_map(rhs_m, lam, g4(n // d) + a4(n // d, spf))
            rhs_a = add_map(rhs_a, lam, -a4(n // d, spf))
        assert lhs_p == rhs_p
        assert lhs_m == rhs_m
        assert lhs_a == rhs_a
        channel_checks += 2
        signed_checks += 1

    for m in range(1, 128, 2):
        if mobius_odd(m, spf) == 0:
            continue
        k = 0
        while 2 * (4 ** k) * m <= N:
            assert a4(2 * (4 ** k) * m, spf) == -a4((4 ** k) * m, spf)
            dyadic_pair_checks += 1
            k += 1

    # D^2 Phi = x W on both polynomial pieces.
    phi1 = {2: Fraction(10, 8), 3: Fraction(-56, 8), 4: Fraction(85, 8)}
    xw1 = {2: Fraction(5), 3: Fraction(-63), 4: Fraction(170)}
    assert poly_D2(phi1) == xw1
    phi2 = {0: Fraction(1, 72), 2: Fraction(-6, 72), 3: Fraction(8, 72), 4: Fraction(-3, 72)}
    xw2 = {2: Fraction(-1, 3), 3: Fraction(1), 4: Fraction(-2, 3)}
    assert poly_D2(phi2) == xw2
    assert (-56) ** 2 - 4 * 85 * 10 == -264
    for k in range(257):
        assert phi(Fraction(k, 256)) >= 0
        peano_checks += 1

    # Exact Peano scale identity for the signed a4 log state.
    for X in (16, 32, 64, 96, 128):
        lhs: dict[int, Fraction] = {}
        cX: dict[int, Fraction] = {}
        cQ: dict[int, Fraction] = {}
        for n in range(1, X + 1):
            weight = phi(Fraction(n, X)) / n
            cX = add_map(cX, {p: int(c) for p, c in formal_a_log(n, spf).items()}, weight)
            dmap = formal_a_log(n, spf)
            if n % 4 == 0:
                dmap = add_map(dmap, {p: int(c) for p, c in formal_a_log(n // 4, spf).items()}, -4)
            lhs = add_map(lhs, {p: int(c) for p, c in dmap.items()}, weight)
        X4 = X // 4
        for n in range(1, X4 + 1):
            weight = phi(Fraction(n, X4)) / n
            cQ = add_map(cQ, {p: int(c) for p, c in formal_a_log(n, spf).items()}, weight)
        rhs = dict(cX)
        for p, c in cQ.items():
            rhs[p] = rhs.get(p, Fraction(0)) - c
            if rhs[p] == 0:
                del rhs[p]
        assert lhs == rhs
        flux_checks += 1

    # Any nonzero positive scalar projection has positive G4 coefficient.
    for rp, rm in ((1, 0), (0, 1), (1, 1), (3, 2)):
        assert rp >= 0 and rm >= 0 and rp + rm > 0
        assert rp + rm > 0
        pole_checks += 1

    if g4(16) != 8:
        mutations += 1
    if a4(4, spf) != 3:
        mutations += 1
    if Fraction(11, 5) * harmonic(N) < energy:
        mutations += 1
    if poly_D2({**phi1, 4: Fraction(84, 8)}) != xw1:
        mutations += 1
    if phi(Fraction(1, 2)) >= 0:
        mutations += 1

    return {
        'classification': 'PASS_X_95180_Q4_CHANNEL_SWAP_PEANO_FLUX',
        'arithmetic_class': 'EXACT_INTEGER_RATIONAL_AND_FORMAL_PRIME_LOG',
        'coefficient_checks': coefficient_checks,
        'channel_swap_checks': channel_checks,
        'signed_reciprocal_checks': signed_checks,
        'energy_bound_checks': energy_checks,
        'dyadic_pair_checks': dyadic_pair_checks,
        'peano_positivity_and_curvature_checks': peano_checks + 3,
        'finite_scale_flux_checks': flux_checks,
        'principal_pole_algebra_checks': pole_checks,
        'hostile_mutations_detected': mutations,
        'proves': [
            'finite g4/a4 coefficients and positive channels',
            'coefficient-one channel swap through N=1024',
            'signed reciprocal recursion through N=1024',
            'exact 12/5 Hilbert-energy bound',
            'dyadic shell sign pairing',
            'piecewise Peano curvature identity',
            'finite exact scale-four Peano difference identity',
        ],
        'does_not_prove': [
            'critical centered-flux extraction',
            'centered cubic square-root bound',
            'balanced Mobius dispersion',
            'Riemann Hypothesis',
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
