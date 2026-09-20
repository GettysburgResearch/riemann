#!/usr/bin/env python3
"""DMC31 bounded exact checks. These are not a proof of the infinite theorem."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import factorial, gcd
from pathlib import Path
import sys

# Resolve only the already-published sibling arithmetic, including under -I.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify import Checks, amplitudes, convolution, divisors, factors, mu, phi, ring, u
from verify_continuation import sf_completion, finite_energy


def harmonic(n: int) -> F:
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def cutoff(length: int) -> int:
    """Exactly ceil(L**(164/137)), floored below by 3; no floating powers."""
    if length < 2:
        raise ValueError('length must be >=2')
    target = length**164
    lo, hi = 0, length * length
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**137 >= target:
            hi = mid
        else:
            lo = mid
    return max(3, hi)


def jordan_coefficients(bs: dict[int, F], mutate: bool = False) -> dict[int, F]:
    coeff = {}
    for q, b in bs.items():
        if q == 1:
            continue
        for n in divisors(q):
            sign = 1 if mutate else mu(q // n)
            coeff[n] = coeff.get(n, F(0)) + b * n * sign
    return {n: a for n, a in coeff.items() if a}


def diagonal_polynomial(c: dict[int, F]) -> dict[int, F]:
    """Mellin numerator for D, via product_p(1-p**(1-s))**2."""
    out = {}
    for d in range(2, max(c) + 1):
        if not mu(d):
            continue
        amp = u(c, d)**2
        if not amp:
            continue
        poly = {1: 1}
        for p, _ in factors(d):
            new = {}
            for n, a in poly.items():
                for m, b in ((1, 1), (p, -2 * p), (p*p, p*p)):
                    new[n*m] = new.get(n*m, 0) + a*b
            poly = new
        for n, a in poly.items():
            out[n] = out.get(n, F(0)) + amp*a
    return {n: a for n, a in out.items() if a}


def source_check(c: dict[int, F], t: Checks, mutate: bool = False) -> None:
    length = max(c)
    z = convolution(c)
    bs = amplitudes(z)
    t.equal(u(c, 1), 0, 'source reciprocal balance')
    t.equal(bs.get(1, F(0)), 0, 'B_1 vanishes')
    t.equal(jordan_coefficients(bs, mutate), z, 'complete Jordan numerator')
    # Independently check the prime-by-prime logarithmic moment cancellation.
    primes = {p for n in z for p, _ in factors(n)}
    for p in primes:
        value = sum((a * F(dict(factors(n)).get(p, 0), n)
                     for n, a in z.items()), F(0))
        t.equal(value, 0, 'logarithmic prime moment')
    if length <= 17:
        for k in range(0, 3 * length + 1):
            floors = sum((a * (k // n) for n, a in z.items()), F(0))
            spec = sum((b * ring(q, k) for q, b in bs.items() if q > 1), F(0))
            t.equal(floors, spec, 'floor versus anchored full covariance')
    cap = max(abs(a) for a in c.values())
    m0 = sum((a*a/n for n, a in z.items()), F(0))
    m1 = sum((a*a for a in z.values()), F(0))
    h = harmonic(length)
    t.true(m0 <= cap**4 * h**4, 'weighted collision moment bound')
    t.true(m1 <= 2 * cap**4 * length**2 * h, 'unweighted collision moment bound')
    if all(not a or mu(n) for n, a in c.items()):
        direct = {}
        for d in range(2, length + 1):
            if not mu(d):
                continue
            amp = u(c, d)**2
            for a in divisors(d):
                q = a*d
                direct[q] = direct.get(q, F(0)) + mu(d//a)*amp
        t.equal(jordan_coefficients(direct), diagonal_polynomial(c),
                'square-amplitude Mellin numerator, two constructions')


def collision_checks(t: Checks) -> None:
    for length in range(2, 41):
        z = convolution({n: F(1) for n in range(1, length + 1)})
        actual = sum(a*a for a in z.values())
        formula = length**2 + 2 * sum(phi(m)*(length//m)**2
                                     for m in range(2, length + 1))
        t.equal(actual, formula, 'exact multiplicative collision count')
        weighted = sum((a*a/n for n, a in z.items()), F(0))
        hs = [harmonic(n) for n in range(length + 1)]
        independent = sum((hs[length//max(u0, v)]**2 / (u0*v)
                           for u0 in range(1, length + 1)
                           for v in range(1, length + 1) if gcd(u0, v) == 1), F(0))
        t.equal(weighted, independent, 'weighted coprime collision parametrization')
        t.true(actual <= 2*length**2*hs[-1], 'collision upper envelope')
        t.true(weighted <= hs[-1]**4, 'weighted collision upper envelope')


def schur_and_constants(t: Checks) -> None:
    for nmax in range(2, 65):
        h = harmonic(nmax)
        for n in range(1, nmax + 1):
            row = sum((F(1, m-n) for m in range(n+1, nmax+1)), F(0))
            row += sum((F(1, m)+F(1, n-m) for m in range(1, n)), F(0))
            t.true(row <= 3*h, 'rational Schur row majorant')
    a = F(667, 10)
    t.true(2**137 > 3**82, 'both dyadic geometric constants')
    t.true(2*a*a < 9000, 'first tail constant')
    t.true(6*a*a < 27000, 'second tail constant')
    exp_lower = sum((F(6, 5)**j / factorial(j) for j in range(5)), F(0))
    t.true(exp_lower > F(25, 8), 'elementary exponential constant')
    t.true(F(110,137) > F(4,5), 'harmonic power comparison')
    t.true(126000 < 2**17, 'full covariance constant')
    t.true(2**18 + 1296 < 2**19, 'dense mixed constant')
    for length in list(range(2, 129)) + [255, 1024, 10**6, 10**20]:
        q = cutoff(length)
        t.true(q >= 3 and q**137 >= length**164, 'cutoff exact upper threshold')
        t.true(q == 3 or (q-1)**137 < length**164, 'cutoff exact ceiling')


def hardy_checks(t: Checks) -> None:
    for vals in product((-1, 0, 1), repeat=4):
        p = {k+1: F(a) for k, a in enumerate(vals)}
        mean = sum((a/F(k*(k+1)) for k, a in p.items()), F(0))
        discrete = {k: a/F(k+1) - sum((p[j]/F(j*(j+1))
                                    for j in p if j > k), F(0))
                    for k, a in p.items()}
        for k, a in p.items():
            x = F(k) + F(2, 5)
            tail = a*(1/x-F(1,k+1))
            tail += sum((p[j]/F(j*(j+1)) for j in p if j > k), F(0))
            t.equal(a/x-tail, discrete[k], 'continuous Hardy on every cell')
        physical = sum((a*a/F(k*(k+1)) for k, a in p.items()), F(0))
        transformed = mean*mean + sum(a*a for a in discrete.values())
        t.equal(physical, transformed, 'Hardy isometry includes (0,1) boundary')
        t.equal(-sum((p[j]/F(j*(j+1)) for j in p), F(0)), -mean,
                'below-support value is not silently deleted')


def native_check(y: int, t: Checks) -> dict:
    c = sf_completion(y)
    z = convolution(c)
    b = (y+1)**2
    v = [F(0) for _ in range(b)]
    for n, a in c.items():
        if n < b:
            v[n] += 2*a
    for n, a in z.items():
        for k in range(n, b, n):
            v[k] -= a
    for n in range(1, b):
        t.equal(v[n], mu(n), 'full native square prefix')
    prefix, tail = finite_energy(c, y)
    t.true(tail <= 32*prefix, 'actual squarefree completion budget')
    t.true(max(c) <= 2*y, 'actual squarefree support')
    t.true(max(abs(a) for a in c.values()) <= 16, 'actual squarefree cap')
    z0 = sum((a*a/n for n, a in z.items()), F(0))
    z1 = sum((a*a for a in z.values()), F(0))
    return {'Y': y, 'L': max(c), 'T_L': cutoff(max(c)),
            'native_checked_through': b-1,
            'M_0_exact': str(z0), 'M_1_exact': str(z1)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutate', action='store_true', help='replace divisor signs by +1; must fail')
    args = parser.parse_args()
    t = Checks()
    # This tiny seed already has both a prime and a prime-square term.
    source_check({1: F(1), 2: F(-2)}, t, args.mutate)
    sources = 1
    for vals in product((-1, 0, 1), repeat=4):
        c = {n+1: F(a) for n, a in enumerate(vals)}
        c[5] = -5*u(c, 1)
        source_check(c, t)
        sources += 1
    for y in (3, 7, 15, 31):
        source_check(sf_completion(y), t)
        sources += 1
    collision_checks(t)
    schur_and_constants(t)
    hardy_checks(t)
    panels = [native_check(y, t) for y in (3, 7, 15, 31, 63, 95, 255)]
    report = {
        'packet': 'DMC31', 'status': 'PASS_FINITE_EXACT_CHECKS_ONLY',
        'exact_comparisons': t.count, 'balanced_sources': sources,
        'collision_lengths': [2, 40], 'schur_sizes': [2, 64],
        'hardy_fixtures': 81, 'native_panels': panels,
        'limits': 'No numerical checks of the infinite zeta theorem; no formal verification or independent review.'}
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (AssertionError, ValueError) as exc:
        print('DMC31 REJECTED: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
