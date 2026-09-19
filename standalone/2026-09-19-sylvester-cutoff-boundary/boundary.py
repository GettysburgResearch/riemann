#!/usr/bin/env python3
"""Exact native boundary/Gram experiment. Standard library; no asymptotic verdict."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import accumulate
from math import gcd, isqrt
from pathlib import Path

BITS = 80
SCALE = 1 << BITS
LABELS = ['constant', 'p=2', 'p=3', 'p=5', 'p=7', '11<=p<=Y', 'p>Y']


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sieve(n: int) -> tuple[list[int], list[int]]:
    mu = [1] * (n + 1)
    mu[0] = 0
    spf = [0] * (n + 1)
    for p in range(2, n + 1):
        if spf[p] == 0:
            for j in range(p, n + 1, p):
                mu[j] = -mu[j]
                if not spf[j]:
                    spf[j] = p
            for j in range(p * p, n + 1, p * p):
                mu[j] = 0
    return mu, spf


def factor(n: int) -> list[tuple[int, int]]:
    out = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def signed_divisors(primes: list[int]) -> list[tuple[int, int]]:
    out = [(1, 1)]
    for p in primes:
        out += [(d * p, -v) for d, v in out]
    return out


def boundary_atoms(y: int, n: int) -> tuple[int, list[tuple[int, int]]]:
    fac = factor(n)
    require(bool(fac), 'boundary needs n>1')
    p = fac[0][0]
    return p, [(d, v) for d, v in signed_divisors([q for q, _ in fac[1:]])
               if y < p * d and d <= y]


def bucket(p: int, y: int) -> int:
    if p > y:
        return 6
    return {2: 1, 3: 2, 5: 3, 7: 4}.get(p, 5)


def enclose(terms) -> list[int]:
    """Return integer endpoints divided by SCALE; Python // floors signed terms."""
    lo = hi = 0
    for num, den in terms:
        q, r = divmod(num * SCALE, den)
        lo += q
        hi += q + bool(r)
    return [lo, hi]


def plus(*xs: list[int]) -> list[int]:
    return [sum(x[0] for x in xs), sum(x[1] for x in xs)]


def times(k: int, x: list[int]) -> list[int]:
    return [k * x[0], k * x[1]] if k >= 0 else [k * x[1], k * x[0]]


def square(x: list[int]) -> list[int]:
    a, b = x
    low = 0 if a <= 0 <= b else min(a * a, b * b)
    high = max(a * a, b * b)
    return [low // SCALE, (high + SCALE - 1) // SCALE]


def gram(rows: list[list[int]], b: int, full: bool = False) -> dict:
    n = len(rows[0])
    weights = [(k * (k + 1)) for k in range(b, b + n)]
    g = [[None for _ in rows] for _ in rows]
    for i, row in enumerate(rows):
        for j in range(i, len(rows)):
            v = enclose((a * c, w) for a, c, w in zip(row, rows[j], weights))
            g[i][j] = v
            g[j][i] = v
    means = [enclose(zip(row, weights)) for row in rows]
    diag = plus(*(g[i][i] for i in range(len(rows))))
    pos, neg = [0, 0], [0, 0]
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            lo, hi = g[i][j]
            require(lo >= 0 or hi <= 0, 'unresolved covariance sign')
            if lo >= 0:
                pos = plus(pos, times(2, [lo, hi]))
            else:
                neg = plus(neg, times(2, [lo, hi]))
    total = [sum(v) for v in zip(*rows)]
    energy = enclose((v * v, w) for v, w in zip(total, weights))
    bounds = plus(diag, pos, neg)
    require(bounds[0] <= energy[0] <= energy[1] <= bounds[1], 'Gram enclosure')
    ans = dict(diagonal=diag, positive_off_diagonal=pos, negative_off_diagonal=neg,
               annular_energy=energy, signed_means=means)
    if full:
        ans['matrix'] = g
    return ans


def native(y: int, full: bool = False) -> tuple[dict, list[int], list[int]]:
    require(type(y) is int and 2 <= y <= 255, 'bounded exact experiment: 2<=Y<=255')
    b, length = y + 1, (y + 1) ** 2
    mu, spf = sieve(length)
    # Separate trial-factorization Mobius oracle. Not used by the producer.
    for n in range(1, length + 1):
        fac = factor(n)
        trial = 0 if any(e > 1 for _, e in fac) else (-1) ** len(fac)
        require(mu[n] == trial, 'independent Mobius check')
    residual = [0] * (length + 1)
    residual[1] = 1
    for d in range(1, b):
        for n in range(d, length + 1, d):
            residual[n] -= mu[d]
    require(not any(residual[:b]), 'native low-divisor equations')
    derivatives = [[0] * length for _ in LABELS]
    atoms_count = 0
    for n in range(b, length):
        p, atoms = boundary_atoms(y, n)
        require(p == spf[n], 'least prime')
        require(-sum(v for _, v in atoms) == residual[n], 'boundary versus divisor sieve')
        for i, (d, _) in enumerate(atoms):
            for d2, _ in atoms[i + 1:]:
                require(d2 % d != 0 and d % d2 != 0, 'antichain')
        atoms_count += len(atoms)
        c = residual[n]
        if c:
            row = derivatives[bucket(p, y)]
            for r in range(1, min(y, (length - 1) // n) + 1):
                row[r * n] += mu[r] * c
    M = list(accumulate(mu))
    rows = [[M[y]] * (length - b)] + [list(accumulate(v))[b:] for v in derivatives[1:]]
    require([sum(v) for v in zip(*rows)] == M[b:length], 'complete native reconstruction')
    # Independent product-first implementation: N(g)=2g-1*(g*g).
    z = [0] * length
    for r in range(1, b):
        for s in range(1, b):
            z[r * s] += mu[r] * mu[s]
    ng = [2 * mu[n] if n <= y else 0 for n in range(length)]
    for d in range(1, length):
        if z[d]:
            for n in range(d, length, d):
                ng[n] -= z[d]
    require(ng[1:] == mu[1:length], 'product-first Newton')
    report = gram(rows, b, full)
    EY = enclose((M[k] ** 2, k * (k + 1)) for k in range(1, b))
    uy = enclose((M[k], k * (k + 1)) for k in range(1, b))
    ub = enclose((M[k], k * (k + 1)) for k in range(1, length))
    EB = enclose((M[k] ** 2, k * (k + 1)) for k in range(1, length))
    report.update(Y=y, B=length - 1, cells=length - b, boundary_atoms=atoms_count,
                  input_E=EY, input_u=uy, output_u=ub,
                  completed_output=plus(EB, times(2 * length, square(ub))))
    prime_tail = [0] * (length - b)
    primes = [p for p in range(b, length) if spf[p] == p]
    diag_terms = []
    for p in primes:
        for r in range(1, min(y, (length - 1) // p) + 1):
            l, u = p * r, min(p * (r + 1), length)
            diag_terms.append((M[r] ** 2 * (u - l), l * u))
            for k in range(l, u):
                prime_tail[k - b] -= M[r]
    require(prime_tail == rows[6], 'large-prime dilation identity')
    report['individual_prime_diagonal'] = enclose(diag_terms)
    report['prime_reciprocal_sum'] = enclose((1, p) for p in primes)
    report['coalesced_prime_energy'] = enclose((v * v, k * (k + 1))
                                              for k, v in enumerate(prime_tail, b))
    report['prime_shell_energy'] = enclose((prime_tail[k - b] ** 2, k * (k + 1))
                                          for k in range(b, 2 * y))
    count = 0
    for k in range(b, 2 * y):
        count += (spf[k] == k)
        require(prime_tail[k - b] == -count, 'prime shell identity')
    # Rigorous finite check of the proved diagonal inequality, using generous endpoints.
    dp = report['individual_prime_diagonal']
    hp = report['prime_reciprocal_sum']
    require(dp[1] * SCALE <= EY[0] * hp[0], 'certified prime diagonal inequality')
    report['joint_separated_diagonal'] = plus(report['diagonal'], times(2 * length,
        plus(square(uy), *(square(v) for v in report['signed_means']))))
    return report, mu, residual


def causal_rows(y: int, P: int, mu: list[int], residual: list[int]) -> list[list[int]]:
    b, length = y + 1, (y + 1) ** 2
    fac = factor(P)
    require(all(e == 1 for _, e in fac), 'bank must be squarefree')
    divs = signed_divisors([p for p, _ in fac])
    Fcum = list(accumulate(residual))
    H = [sum(v * Fcum[t // d] for d, v in divs) for t in range(length)]
    rows = [[sum(mu[1:b])] * (length - b)] + [[0] * (length - b) for _ in range(y.bit_length())]
    for r in range(1, b):
        if mu[r] and gcd(r, P) == 1:
            row = rows[r.bit_length()]
            for k in range(b * r, length):
                row[k - b] += mu[r] * H[k // r]
    M = list(accumulate(mu))
    require([sum(v) for v in zip(*rows)] == M[b:length], 'causal Euler reconstruction')
    return rows


def kernel(t: int, u: int, b: int) -> F:
    L = b * b
    k = max(t, u, b)
    return F(1, k) - F(1, L) if k < L else F(0)


def small_exact_tests() -> dict:
    # Full uncoalesced step-atom computation; different order from native().
    for y in (2, 3, 7, 15):
        b, L = y + 1, (y + 1) ** 2
        mu, _ = sieve(L)
        M = list(accumulate(mu))
        atoms = [(b, M[y])]
        for n in range(b, L):
            _, ds = boundary_atoms(y, n)
            for r in range(1, min(y, (L - 1) // n) + 1):
                atoms.extend((r * n, -mu[r] * v) for _, v in ds if mu[r])
        eta = lambda t: kernel(t, t, b)
        ann = sum((F(M[k] ** 2, k * (k + 1)) for k in range(b, L)), F(0))
        double = sum((a * c * kernel(t, u, b) for t, a in atoms for u, c in atoms), F(0))
        require(ann == double, 'uncoalesced rational max kernel')
        u0 = sum((F(M[k], k * (k + 1)) for k in range(1, b)), F(0))
        unew = u0 + sum((a * eta(t) for t, a in atoms), F(0))
        direct = sum((F(M[k], k * (k + 1)) for k in range(1, L)), F(0))
        require(unew == direct, 'completion mean, exact rational')
    # Endpoint: Y=2, excluded n=9 has error exactly 1.
    y = 2
    mu, _ = sieve(9)
    ng9 = -sum(mu[r] * mu[s] for r in (1, 2) for s in (1, 2) if 9 % (r * s) == 0)
    require(mu[9] - ng9 == 1, 'excluded Newton endpoint')
    # The claimed e*e driver is identically absent inside the reconstruction annulus.
    for y in (2, 3, 7, 15):
        b, L = y + 1, (y + 1) ** 2
        mu, _ = sieve(L)
        e = [int(n == 1) - sum(mu[d] for d in range(1, y + 1) if n % d == 0)
             for n in range(L + 1)]
        require(all(e[n] == 0 for n in range(1, b)), 'error support')
        require(all(a * c >= L for a in range(b, L) if e[a]
                    for c in range(b, min(L, L // a + 1)) if e[c]), 'squared error support')
    # Structural controls, explicitly not claimed to reproduce NSR's large fake wave.
    mu, _ = sieve(63)
    fake = [0] * 64
    for n, v in {1: 1, 2: -1, 3: -1, 5: -1, 6: -1, 10: 1, 15: 1, 30: 1}.items():
        fake[n] = v
    first = next(n for n in range(1, 64)
                 if sum(fake[d] for d in range(1, n + 1) if n % d == 0) != int(n == 1))
    require(first == 6, 'fake source must fail at 6')
    p, atoms = boundary_atoms(3, 6)
    require(p == 2 and atoms == [(3, -1)], 'one-atom antichain control')
    scrambled = [(d, -v) for d, v in atoms]
    require(-sum(v for _, v in scrambled) != mu[6], 'antichain-only control must fail')
    return dict(rational_kernel_cutoffs=[2, 3, 7, 15], sharp_endpoint_Y=2,
                fake_divisor_failure=6, antichain_sign_scramble_rejected=True)


def calculate() -> dict:
    out = dict(status='finite exact evidence; no all-scale gain or RH verdict',
               denominator=str(SCALE), labels=LABELS, tests=small_exact_tests(), native=[])
    for y in (3, 15, 63, 255):
        row, mu, residual = native(y, full=(y == 255))
        out['native'].append(row)
    banks = []
    for P in (1, 6, 30, 210):
        rows = causal_rows(255, P, mu, residual)
        g = gram(rows, 256, full=(P == 210))
        g.update(P=P, row_count=len(rows), cauchy_upper=times(len(rows), g['diagonal']))
        g['joint_separated_diagonal'] = plus(g['diagonal'], times(2 * 256**2,
            plus(square(out['native'][-1]['input_u']), *(square(v) for v in g['signed_means']))))
        banks.append(g)
    out['inherited_causal_bank_replay'] = banks
    return out


def no_duplicates(items):
    out = {}
    for k, v in items:
        require(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def canonical(data) -> str:
    return json.dumps(data, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n'


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group()
    group.add_argument('--write', type=Path)
    group.add_argument('--check', type=Path)
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    if args.self_test:
        small_exact_tests()
        print('PASS exact kernels, support, endpoints and structural controls')
        return
    text = canonical(calculate())
    if args.write:
        args.write.write_text(text, encoding='utf-8')
    if args.check:
        saved = json.loads(args.check.read_text(encoding='utf-8'), object_pairs_hook=no_duplicates)
        require(canonical(saved) == text, 'report differs from exact reconstruction')
    print('PASS', hashlib.sha256(text.encode()).hexdigest())


if __name__ == '__main__':
    main()
