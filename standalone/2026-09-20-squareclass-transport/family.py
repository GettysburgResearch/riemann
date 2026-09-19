"""Exact arithmetic-normalized CM inert-square deletion/sign fixtures.
This is a finite good-prime Euler model, not a global elliptic L computation.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def point_count(m, p):
    require(prime(p) and p > 3 and (3*m) % p != 0, 'good odd prime required')
    c = (m*m*pow(4, -1, p)) % p
    return 1 + sum(sum((y*y-x*x*x-c) % p == 0 for y in range(p)) for x in range(p))


def source(N, factors):
    a = [0]*(N+1)
    a[1] = 1
    for p, cs in factors:
        nxt = [0]*(N+1)
        for n, v in enumerate(a):
            if not v:
                continue
            power = 1
            for c in cs:
                if n*power > N:
                    break
                nxt[n*power] += v*c
                power *= p
        a = nxt
    return a


def energy(a, endpoint):
    """Integral |sum_{n<=x} a(n)|^2 dx/x^3, with exact rational endpoint."""
    X = F(endpoint)
    if X <= 1:
        return F(0)
    total, val, last = F(0), 0, F(1)
    for n in range(1, min(len(a), (X.numerator+X.denominator-1)//X.denominator)):
        if a[n]:
            total += val*val*(1/last**2-F(1,n*n))/2
            val += a[n]
            last = F(n)
    total += val*val*(1/last**2-1/X**2)/2
    return total


def delete_inert(a, p):
    b = list(a)
    for n in range(p*p, len(a), p*p):
        b[n] = a[n]-p*b[n//(p*p)]
    return b


def rational(x):
    return [x.numerator, x.denominator]


def build():
    m, X = 17, 4096
    N = X-1
    inert = [p for p in range(5, 64) if prime(p) and p % 3 == 2 and m % p]
    split = [7, 13, 19]
    counts = {str(p): point_count(m, p) for p in inert+split}
    ap = {p: p+1-counts[str(p)] for p in inert+split}
    require(all(ap[p] == 0 for p in inert), 'CM inert trace zero')
    factors = [(p, (1, -ap[p], p)) for p in split]
    base = source(N, factors)
    E0 = energy(base, X)
    Bplus = Bminus = D = F(1)
    for p in inert:
        Bplus *= F(p+1, p)
        Bminus *= F(p, p-1)
        D *= F(p*p+1, p*p)
    ds = [1]
    for p in inert:
        ds += [p*d for d in ds if (p*d)**2 < X]
    ds.sort()
    parseval = sum((energy(base, F(X, d*d))/ (d*d) for d in ds), F(0))
    energies = []
    native = None
    checked = 0
    for sig in itertools.product((-1, 1), repeat=len(inert)):
        a = source(N, factors+[(p, (1, 0, s*p)) for p, s in zip(inert, sig)])
        # Independent coefficient assembly through square-divisor fibres.
        dsig = [(1, 1)]
        for p, s in zip(inert, sig):
            dsig += [(p*d, s*e) for d, e in dsig if (p*d)**2 < X]
        for n in range(1, N+1):
            v = sum(e*d*base[n//(d*d)] for d, e in dsig if n % (d*d) == 0)
            require(a[n] == v, 'square-divisor source reconstruction')
            checked += 1
        E = energy(a, X)
        require(E <= Bplus**2*E0 and E0 <= Bminus**2*E, 'two-way energy bound')
        energies.append((E, sig))
        if all(s == 1 for s in sig):
            native = a
            native_energy = E
    avg = sum((E for E, _ in energies), F(0))/len(energies)
    require(avg == parseval, 'character Parseval including rational endpoints')
    require(E0 <= avg <= D*E0, 'uniform average envelope')
    require(native_energy <= Bplus**2*avg and avg <= D*Bminus**2*native_energy,
            'average-to-native individualization')
    restored = native
    for p in inert:
        restored = delete_inert(restored, p)
    require(restored == base, 'causal inert deletion')
    lo, hi = min(energies), max(energies)
    require(native_energy <= (Bplus*Bminus)**2*lo[0], 'best signature restoration')
    # Omitting the mixed 5^2*11^2 term or confusing unitary/arithmetic normalization fails.
    mixed = 55**2
    require(mixed < X and native[mixed] == 55 and base[mixed] == 0, 'mixed-square control')
    wrong = source(N, factors+[(p, (1, 0, 1)) for p in inert])
    require(wrong[25] != native[25], 'normalization control')
    return dict(schema='STC26-CM-1', m=m, X=X, energy_measure='dx/x^3; arithmetic coefficients',
                model='finite good-prime Euler model; not complete E_17',
                inert=inert, split=split, counts=counts,
                signatures=len(energies), coefficient_comparisons=checked,
                base=rational(E0), native=rational(native_energy), average=rational(avg),
                parseval=rational(parseval), minimum=rational(lo[0]), maximum=rational(hi[0]),
                minimum_signature=list(lo[1]), maximum_signature=list(hi[1]),
                B_plus=rational(Bplus), B_minus=rational(Bminus), D=rational(D),
                active_square_divisors=ds, mixed_square_index=mixed,
                controls=['mixed square term retained', 'wrong normalization rejected',
                          'causal inverse signs checked'],
                status='exact finite algebra; global ranks and zeros not computed')


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', type=Path)
    ap.add_argument('--check', type=Path)
    args = ap.parse_args()
    text = canonical(build())
    if args.write:
        args.write.write_text(text+'\n')
    if args.check:
        require(args.check.read_text().strip() == text, 'family report mismatch')
    print('STC26 family OK', hashlib.sha256(text.encode()).hexdigest())


if __name__ == '__main__':
    main()
