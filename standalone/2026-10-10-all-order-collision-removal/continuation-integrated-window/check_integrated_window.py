#!/usr/bin/env python3
"""Exact finite algebra checks, NOT an infinite arithmetic moment verifier.

The cyclotomic fixtures use a free monoid with generator norms 8,16,32.
They are not Eisenstein ideal samples. No float arithmetic or bare assert
is used. Both --write and --check reconstruct every declared fixture.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from math import comb, factorial
from pathlib import Path
import sys

Pair = tuple[int, int]  # a+b*zeta_6, zeta_6^2=zeta_6-1
ZERO: Pair = (0, 0)
ONE: Pair = (1, 0)
ROOTS: tuple[Pair, ...] = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
COUNTS: Counter[str] = Counter()


def require(ok: bool, label: str) -> None:
    if not ok:
        raise ValueError(f"verification failed: {label}")
    COUNTS[label.split(':')[0]] += 1


def add(z: Pair, w: Pair) -> Pair:
    return z[0]+w[0], z[1]+w[1]


def mul(z: Pair, w: Pair) -> Pair:
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c+b*d


def scale(z: Pair, n: int) -> Pair:
    return z[0]*n, z[1]*n


def norm(z: Pair) -> int:
    a, b = z
    return a*a+a*b+b*b


def wp(j: int) -> int:
    return (1, 2, 1)[j] if 0 <= j <= 2 else 0


def compositions(total: int, k: int):
    if k == 1:
        yield (total,)
    else:
        for e in range(total+1):
            for rest in compositions(total-e, k-1):
                yield (e,)+rest


def inverse_local(e: tuple[int, ...]) -> int:
    support = sum(t != 0 for t in e)
    return 1 if support == 0 else 1-support


def local_checks() -> None:
    for k in range(2, 7):
        for total in range(8):
            for e in compositions(total, k):
                convolution = 0
                for mask in product((0, 1), repeat=k):
                    if all(mask[i] <= e[i] for i in range(k)):
                        rem = tuple(e[i]-mask[i] for i in range(k))
                        convolution += (-1)**sum(mask) * inverse_local(rem)
                target = 1 if total == 0 else (-1 if total == 1 else 0)
                require(convolution == target, 'local_inverse: coefficient')
    for z in ROOTS+(ZERO,):
        z6 = ONE
        for _ in range(6):
            z6 = mul(z6, z)
        require(z6 == (ZERO if z == ZERO else ONE), 'cyclotomic: sixth powers and zeros')
        for w in ROOTS+(ZERO,):
            require(norm(mul(z, w)) == norm(z)*norm(w), 'cyclotomic: norm multiplicative')


def convolution(a: list[F], b: list[F], N: int) -> list[F]:
    return [sum((a[j]*b[n-j] for j in range(n+1)), F(0)) for n in range(N+1)]


def window_checks() -> list[str]:
    N = 30
    moments = [F(1)]
    for n in range(1, N+1):
        rhs = sum((F(comb(n, j))*moments[j]*F(1, n-j+1)
                   for j in range(n) if (n-j) % 2 == 0), F(0))
        moments.append(rhs/(2**n-1))
        require(moments[n] >= 0, 'window: positive even moments')
        if n % 2:
            require(moments[n] == 0, 'window: odd moments vanish')
    require(moments[2] == F(1, 9), 'window: variance')
    require(moments[4] == F(19, 675), 'window: fourth moment')
    expected = [moments[n]/factorial(n) for n in range(N+1)]
    for J in range(1, 9):
        finite = [F(1)]+[F(0)]*N
        for j in range(1, J+1):
            factor = [F(1, 2**(j*n)*factorial(n+1)) if n % 2 == 0 else F(0)
                      for n in range(N+1)]
            finite = convolution(finite, factor, N)
        tail = [expected[n]/2**(J*n) for n in range(N+1)]
        rebuilt = convolution(finite, tail, N)
        for n in range(N+1):
            require(rebuilt[n] == expected[n], 'window: finite product plus exact tail')
    for m in range(1, 257):
        factor_count = sum((2*m) % 2**j == 0 for j in range(1, 12))
        v, q = 0, m
        while q % 2 == 0:
            v += 1
            q //= 2
        require(factor_count == 1+v, 'window: zero multiplicity lattice')
    return [str(moments[2*j]) for j in range(7)]


def inverse_mass(k: int, log_norms: tuple[int, ...]) -> F:
    prod_mass = F(1)
    for a in log_norms:
        t = F(1, 2**a)
        prod_mass *= 2-(1-k*t)/(1-t)**k
    return prod_mass-1


def series_A(phases: tuple[Pair, ...], logs: tuple[int, ...], T: int) -> list[Pair]:
    out = [ZERO]*(T+1)
    for mask in product((0, 1), repeat=len(logs)):
        log_n, coeff = 0, ONE
        for i, present in enumerate(mask):
            if present:
                log_n += logs[i]
                coeff = mul(coeff, scale(phases[i], -1))
        for j in range(T+1):
            out[j] = add(out[j], scale(coeff, wp(j-log_n)))
    return out


def series_B(phases: tuple[Pair, ...], logs: tuple[int, ...], k: int, T: int) -> list[Pair]:
    out = [ZERO]*(T+1)
    for allocation in product(range(k+1), repeat=len(logs)):
        lengths, coeff = [0]*k, ONE
        for i, colour in enumerate(allocation):
            if colour:
                lengths[colour-1] += logs[i]
                coeff = mul(coeff, scale(phases[i], -1))
        for j in range(T+1):
            weight = 1
            for a in lengths:
                weight *= wp(j-a)
            out[j] = add(out[j], scale(coeff, weight))
    return out


def integral_checks() -> dict[str, str | int]:
    logs, T = (3, 4, 5), 16
    rows = list(product(ROOTS+(ZERO,), repeat=3))
    q_values = {k: inverse_mass(k, logs) for k in (2, 3, 4)}
    for q in q_values.values():
        require(0 <= q < F(1, 3), 'finite_norm: small inverse mass')
    for phases in rows:
        A = series_A(phases, logs, T)
        removed = []
        for i, log_p in enumerate(logs):
            p_phases = list(phases)
            p_phases[i] = ZERO
            C = series_A(tuple(p_phases), logs, T)
            removed.append(C)
            for j in range(T+1):
                lower = C[j-log_p] if j >= log_p else ZERO
                require(A[j] == add(C[j], scale(mul(phases[i], lower), -1)),
                        'prime_removal: exact shifted sequence')
        for k in (2, 3, 4):
            p0 = 2*k
            M = sum((F(norm(z)**k, 2**(p0*j)) for j, z in enumerate(A)), F(0))
            B = series_B(phases, logs, k, T)
            IB = sum((F(norm(z), 2**(p0*j)) for j, z in enumerate(B)), F(0))
            q = q_values[k]
            require((1-q)**2*M <= IB <= (1+q)**2*M,
                    'finite_norm: integrated balanced comparison')
            for shifts in ((0,)*k, (3,)+(0,)*(k-1), tuple(range(k)), (3,)*k):
                mixed = F(0)
                for j in range(T+1):
                    z = ONE
                    for d in shifts:
                        z = mul(z, A[j-d] if j >= d else ZERO)
                    mixed += F(norm(z), 2**(p0*j))
                require(mixed <= F(1, 2**(2*sum(shifts)))*M,
                        'finite_norm: joint scale Holder bound')
            for i, C in enumerate(removed):
                IC = sum((F(norm(z)**k, 2**(p0*j)) for j, z in enumerate(C)), F(0))
                require(M <= (1+F(1, 2**logs[i]))**p0*IC,
                        'prime_removal: weighted norm inequality')
    return {'rows': len(rows), 'horizon': T, **{f'q_{k}': str(q) for k, q in q_values.items()}}


def exponent_checks() -> None:
    for k in range(2, 13):
        delta = F(1, 120*k)
        for j in range(1, 12*k+1):
            h = F(j, 12)
            terms = [F(0), k-F(5, 6)*h-2*k*delta,
                     F(k, 3)-h/6-2*k*delta,
                     F(5*k, 6)-F(2, 3)*h-2*k*delta]
            lam = max(terms)
            require(lam == terms[1], 'sieve: dominant sixth-power term')
            alpha = F(1, 2)+delta+(lam+F(5, 6)*h)/(2*k)
            require(alpha == 1, 'sieve: generic boundary remains one')
    for a in range(1, 31):
        h = F(a, 12)
        for b in range(1, 31):
            n = F(b, 12)
            old = max(h, h/6+n, F(2, 3)*(h+n))
            new = max(h, h/6+n, F(5, 6)*h+n/3, h/3+F(5, 6)*n)
            require(new <= old, 'sieve: improved envelope comparison')
    require(F(4, 3)-F(7, 6) == F(1, 6), 'sieve: balanced saving')
    for k, expected in ((2, F(17, 24)), (3, F(23, 36)), (4, F(29, 48))):
        require(F(1, 2)+F(5, 12*k) == expected, 'extraction: hierarchy')
    require(F(1, 2)+(F(1, 2)+F(5, 6))/4 == F(5, 6), 'extraction: defective fourth moment')


def mutation_checks() -> int:
    wrong = [
        (inverse_local((1, 1)) == 0, 'dropping shared-prime inverse coefficient'),
        (F(1, 9) == F(1, 3), 'wrong window variance'),
        (F(1, 2)+F(5, 24) == F(3, 4), 'wrong replica fraction'),
    ]
    rejected = 0
    for claim, name in wrong:
        try:
            require(claim, 'mutation:'+name)
        except ValueError:
            rejected += 1
        else:
            raise ValueError('a deliberately false identity was accepted: '+name)
    return rejected


def reconstruct() -> dict:
    COUNTS.clear()
    local_checks()
    moments = window_checks()
    finite = integral_checks()
    exponent_checks()
    rejected = mutation_checks()
    return {
        'status': 'PASS_FINITE_IDENTITIES_ONLY',
        'scope': 'Exact rational and Q(zeta_6) algebra; finite free-monoid fixtures, not Hecke moment data.',
        'counts': dict(sorted(COUNTS.items())),
        'total_successful_predicates': sum(COUNTS.values()),
        'deliberately_false_identities_rejected': rejected,
        'window_even_moments_0_through_12': moments,
        'finite_norm_fixture': finite,
        'claims_not_verified': ['infinite signed covariance bound', 'external large-sieve proof',
                                'fourth/sixth arithmetic moment', 'new zero-free half-plane', 'RH'],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--write', type=Path)
    group.add_argument('--check', type=Path)
    args = parser.parse_args()
    result = reconstruct()
    encoded = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.check:
        if json.loads(args.check.read_text(encoding='utf-8')) != result:
            raise ValueError('stored result differs from full reconstruction')
    if args.write:
        args.write.write_text(encoded, encoding='utf-8')
    sys.stdout.write(encoded)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
