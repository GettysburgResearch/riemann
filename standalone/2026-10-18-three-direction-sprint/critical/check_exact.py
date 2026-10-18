"""Exact arithmetic checks for the critical-ray Euler identities.

These finite checks authenticate coefficient identities on the displayed
domain. The infinite analytic estimates are proved in PROOF.md.
"""
from fractions import Fraction
from functools import lru_cache
import json
import math
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


@lru_cache(None)
def factor(n):
    require(isinstance(n, int) and n >= 1, 'Positive integer required.')
    out = []
    p = 2
    while p*p <= n:
        j = 0
        while n % p == 0:
            n //= p
            j += 1
        if j:
            out.append((p, j))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


@lru_cache(None)
def a(n):
    z = 1
    for p, _ in factor(n):
        z *= 1-p
    return Fraction(z, n)


@lru_cache(None)
def beta(n):
    z = Fraction(1)
    for p, j in factor(n):
        z *= Fraction(-(p*p-1), p**j*(p+2))
    return z


def divisors(n):
    out = [1]
    for p, j in factor(n):
        out = [d*p**k for d in out for k in range(j+1)]
    return out


def correction(e, support):
    z = Fraction(1)
    for p, j in factor(e):
        if p not in support:
            return Fraction(0)
        z *= -Fraction(p-1, p)*(-Fraction(p-2, p))**(j-1)
    return z


def main():
    checks = 0
    for n in range(1, 1001):
        expected = a(n)
        for p, _ in factor(n):
            expected *= Fraction(p+1, p+2)
        require(beta(n) == expected, 'Beta/source coefficient mismatch.')
        checks += 1

    shared_cases = 0
    for r in range(1, 17):
        for s in range(1, 17):
            if math.gcd(r, s) != 1:
                continue
            support = frozenset(p for p, _ in factor(r*s))
            for d in range(1, 65):
                conv = sum((a(d//e)**2*correction(e, support)
                            for e in divisors(d)), Fraction(0))
                require(a(r*d)*a(s*d) == a(r)*a(s)*conv,
                        'Complete shared-prime convolution failed.')
                shared_cases += int(math.gcd(d, r*s) > 1)
                checks += 1

    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        b = Fraction(p-2, p)
        for j in range(1, 9):
            q = Fraction((p-1)**2, p**(2*j))
            corrected = q + sum(
                (Fraction((p-1)**2, p**(2*(j-k))) if k < j else Fraction(1))
                *(-Fraction(p-1, p)*(-b)**(k-1))
                for k in range(1, j+1)
            )
            require(corrected == -Fraction(p-1, p**(2*j)),
                    'Local Euler correction at a shared prime failed.')
            checks += 1

    # Ordered versus disjoint-row partition of the complete finite ratio sector.
    for cap in (8, 16, 32, 64):
        for small in (1, 2, 3, 4, 7):
            if small > cap:
                continue
            direct = {(r, s) for r in range(1, cap+1)
                      for s in range(1, cap+1)
                      if math.gcd(r, s) == 1 and min(r, s) <= small}
            disjoint = {(1, 1)}
            for s in range(1, small+1):
                for r in range(s+1, cap+1):
                    if math.gcd(r, s) == 1:
                        disjoint.update(((r, s), (s, r)))
            require(direct == disjoint, 'Primitive-sector partition mismatch.')
            checks += 1

    # A lost shared-prime correction must visibly change the coefficient.
    require(a(2*2)*a(3*2) != a(2)*a(3)*a(2)**2,
            'Negative control did not expose a removed shared prime.')
    checks += 1
    result = {'arithmetic': 'EXACT_RATIONAL', 'status': 'PASS',
              'checks': checks, 'shared_prime_cases': shared_cases,
              'source_range': [1, 1000], 'ray_caps': [16, 16, 64],
              'infinite_analytic_estimate_certified_by_this_script': False}
    out = Path(__file__).with_name('EXACT_CHECKS.json')
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
