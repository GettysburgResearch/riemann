"""Exact native norm arithmetic; all primes above 2 and 3 are excluded."""
from fractions import Fraction
from math import isqrt


def sieve(cap: int) -> list[int]:
    if cap < 1:
        raise ValueError('cap must be positive')
    spf = list(range(cap + 1))
    for p in range(2, isqrt(cap) + 1):
        if spf[p] == p:
            for n in range(p*p, cap + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor(n: int, spf: list[int]) -> list[tuple[int, int]]:
    if not 1 <= n < len(spf):
        raise ValueError('factor input outside sieve')
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def local_a(p: int, e: int) -> int:
    if e == 0:
        return 1
    if p in (2, 3):
        return 0
    if p % 3 == 1:
        return -2 if e == 1 else (1 if e == 2 else 0)
    return -1 if e == 2 else 0


def local_b(p: int, e: int) -> Fraction:
    if e == 0:
        return Fraction(1)
    if p in (2, 3):
        return Fraction(0)
    if p % 3 == 1:
        den = p*p + 4*p + 1
        if e == 1:
            return Fraction(-2*p*(p+1), den)
        if e == 2:
            return Fraction(p*p, den)
        return Fraction(0)
    return Fraction(-p*p, p*p + 1) if e == 2 else Fraction(0)


def q_at_one(p: int) -> Fraction:
    if p in (2,3):
        return Fraction(1)
    return (1 + Fraction(4,p) + Fraction(1,p*p)) if p%3 == 1 else (1 + Fraction(1,p*p))


def coefficient_arrays(cap: int):
    spf = sieve(cap)
    a = [0] * (cap + 1)
    b = [Fraction(0) for _ in range(cap + 1)]
    a[1], b[1] = 1, Fraction(1)
    for n in range(2, cap + 1):
        p, r, e = spf[n], n, 0
        while r % p == 0:
            r //= p
            e += 1
        a[n] = a[r] * local_a(p, e)
        b[n] = b[r] * local_b(p, e)
    return spf, a, b


def shared_divisors(r: int, spf: list[int]) -> list[int]:
    """All possible shared p factors for a split-prime ratio of exponent one."""
    ds = [1]
    for p,e in factor(r, spf):
        if p%3 == 1 and e == 1:
            ds += [d*p for d in list(ds)]
    return sorted(ds)


def enumerate_squarefree_ideals(cap: int) -> list[tuple[int, int, tuple]]:
    """All good squarefree ideals under cap. Split conjugates are separate."""
    spf = sieve(cap)
    primes = []
    for p in range(5, cap + 1):
        if spf[p] != p:
            continue
        if p % 3 == 1:
            primes.extend([(p, (p,0)), (p, (p,1))])
        elif p*p <= cap:
            primes.append((p*p, (p,0)))
    ideals = [(1,1,())]
    for norm,label in primes:
        additions = [(n*norm, -sign, labs+(label,))
                     for n,sign,labs in ideals if n*norm <= cap]
        ideals.extend(additions)
    return sorted(ideals)
