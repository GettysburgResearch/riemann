#!/usr/bin/env python3
"""Exact bounded checks for the whole-xi gamma attempt, not an RH verifier.

No gamma/zeta evaluation, floating arithmetic, phase search, or zero oracle.
The unbounded zero theorem is a paper argument, not certified by these checks.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from math import comb, factorial, isqrt
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

def harmonic(k: int) -> F:
    return sum((F(1, j) for j in range(1, k + 1)), F(0))

def data(N: int) -> list[tuple[F, F]]:
    require(type(N) is int and N >= 1, 'invalid N')
    r = F(1)
    result = []
    hs = [F(0)]
    for j in range(1, 2 * N + 1):
        hs.append(hs[-1] + F(1, j))
    for n in range(1, N + 1):
        r *= F(N-n+1, N+n)
        result.append((r*r, n*(hs[N+n]-hs[N-n])))
    return result

def liouville_sieve(N: int) -> list[int]:
    spf = list(range(N + 1))
    for p in range(2, isqrt(N) + 1):
        if spf[p] == p:
            for n in range(p*p, N+1, p):
                if spf[n] == n:
                    spf[n] = p
    out = [0] * (N+1)
    out[1] = 1
    for n in range(2, N+1):
        out[n] = -out[n // spf[n]]
    return out

def liouville_trial(n: int) -> int:
    s, d = 1, 2
    while d*d <= n:
        while n % d == 0:
            n //= d
            s = -s
        d += 1
    return -s if n > 1 else s

def cbrt_floor(n: int) -> int:
    require(type(n) is int and n >= 0, 'invalid cube input')
    lo, hi = 0, 1 << ((n.bit_length()+2)//3 + 1)
    while hi-lo > 1:
        m = (hi+lo)//2
        if m*m*m <= n:
            lo = m
        else:
            hi = m
    require(lo**3 <= n < (lo+1)**3, 'cube-root bracket failed')
    return lo

def negative_twist(N: int = 256, bits: int = 96) -> tuple[F,F,F]:
    ls = liouville_sieve(N)
    low, high, half = F(0), F(0), F(0)
    scale = 1 << bits
    for n, (w, _) in enumerate(data(N), 1):
        k = cbrt_floor((scale**3)//(n*n))
        a, b = F(k, scale), F(k+1, scale)
        require(a**3 * n*n <= 1 <= b**3*n*n, 'power enclosure')
        if ls[n] == 1:
            low += w*a
            high += w*b
        else:
            low -= w*b
            high -= w*a
        half += ls[n]*w/n
    require(F(-23,1000) < low <= high < F(-22,1000), 'one-third sign')
    require(F(249,1000) < half < F(250,1000), 'one-half sign')
    return low, high, half

def floor_fraction(x: F) -> int:
    return x.numerator // x.denominator

def ceiling_fraction(x: F) -> int:
    return -((-x.numerator)//x.denominator)

def decimal_bracket(a: F, b: F, digits: int = 15) -> list[str]:
    scale = 10**digits
    low, high = floor_fraction(a*scale), ceiling_fraction(b*scale)
    def render(n: int) -> str:
        sign = '-' if n < 0 else ''
        v = abs(n)
        return sign + str(v//scale) + '.' + str(v%scale).zfill(digits)
    return [render(low), render(high)]

def canonical(obj: object) -> str:
    return json.dumps(obj, sort_keys=True, indent=2) + '\n'

def run() -> dict:
    counts = {}
    ls = liouville_sieve(512)
    for n in range(1,513):
        require(ls[n] == liouville_trial(n), 'Liouville source mismatch')
    counts['liouville_independent_integer_checks'] = 512
    laplace, moments, removables, product_checks = 0,0,0,0
    for N in range(1,13):
        co = data(N)
        for n,(w,u) in enumerate(co,1):
            require(w == F(factorial(N)**2, factorial(N-n)*factorial(N+n))**2, 'weight factorial')
            inv = sum((F(1,j*j-n*n) for j in range(1,N+1) if j != n), F(0))
            require(inv == F(3,4*n*n)-u/(2*n*n), 'partial fraction slope')
            product_checks += 1
        for t in [F(0),F(1,2),F(1),F(2),F(7),F(19,3)]:
            prod = F(1)
            for n in range(1,N+1):
                prod *= (F(n*n)/(n*n+t))**2
            pf = sum((4*n*n*w*(u-F(3,2))/(t+n*n)
                      +4*n**4*w/(t+n*n)**2
                      for n,(w,u) in enumerate(co,1)), F(0))
            require(prod == pf, 'Laplace partial fractions')
            laplace += 1
        # Independent moment reconstruction by adding Gamma(2)/n^2 variables.
        raw = [F(1)] + [F(0)]*5
        for n in range(1,N+1):
            raw = [sum((comb(k,j)*raw[k-j]*F(factorial(j+1),n**(2*j))
                        for j in range(k+1)),F(0)) for k in range(6)]
        for k in range(6):
            formula = 4*factorial(k)*sum((w*(F(k)-F(1,2)+u)/n**(2*k)
                                           for n,(w,u) in enumerate(co,1)),F(0))
            require(formula == raw[k], 'positive moments')
            moments += 1
        for j in range(1,2*N):
            value = sum((w*(-F(j)-F(1,2)+u)*n**(2*j)
                         for n,(w,u) in enumerate(co,1)),F(0))
            require(value == 0, 'removable Gamma pole')
            removables += 1
    counts.update(partial_fraction_source_identities=product_checks,
                  laplace_rational_values=laplace, positive_integer_moments=moments,
                  exact_negative_integer_cancellations=removables)
    # All-prime phase construction's numerical constants, not PNT itself.
    lower_e = sum((F(1,factorial(k)) for k in range(5)),F(0))
    upper_e = sum((F(1,factorial(k)) for k in range(9)),F(0)) + F(10,9*factorial(9))
    require(F(8,3) < lower_e < upper_e < F(11,4), 'e bounds')
    require(F(1,21)-F(2,99) > F(1,40), 'prime coefficient lower')
    require(2*F(11,10)**2+4*F(11,10)**3/1000 < 3, 'Gaussian coefficient exponent')
    counts['large_N_constant_budgets'] = 3
    lo,hi,half = negative_twist()
    counts['cube_root_enclosures'] = 256
    # Finite selected-prime monomial property (not the all-large-N count).
    no_cross=0
    for N in [100,256,1000,4096]:
        ps=[p for p in range(isqrt(N)+1, isqrt(121*N)//10+1)
            if p > 1 and all(p%d for d in range(2,isqrt(p)+1))]
        for p in ps:
            for q in ps:
                require(p*q > N,'two selected prime factors')
                no_cross += 1
    counts['finite_selected_prime_product_pairs'] = no_cross
    return {
        'status':'FAILED_FULL_RH_ATTEMPT_WITH_PROPOSED_COMPONENT_PROOFS',
        'rh_proved':False,
        'zeros_belong_to':'explicit finite approximants, not xi or zeta',
        'bounded_checks':counts,
        'twist_certificate':{
            'N':256, 'power_interval_bits':96,
            'A_liouville_at_one_third':decimal_bracket(lo,hi),
            'A_liouville_at_one_half':decimal_bracket(half,half),
            'strict_signs':'negative at 1/3; positive at 1/2',
            'implied_real_zero_interval':['1/3','1/2'],
            'off_axis_approximant_zero_existence':'paper proof via finite prime phases and Rouche; no ordinate computed'
        },
        'unexecuted':['global analytic arguments','PNT proof','actual xi zero computation',
                      'gamma or zeta oracle','finite phase approximation heights','formal proof build']
    }

def strict_json(path: Path) -> object:
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:
                raise ValueError('duplicate JSON key')
            out[k]=v
        return out
    def no_number(x):
        raise ValueError('noninteger JSON number')
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_float=no_number, parse_constant=no_number)

def authenticate() -> None:
    manifest=ROOT/'SHA256SUMS'
    entries={}
    for line in manifest.read_text().splitlines():
        digest,name=line.split('  ',1)
        require(name not in entries and '/' not in name and name != 'SHA256SUMS','bad manifest')
        require(len(digest)==64,'bad digest')
        entries[name]=digest
    present={p.name for p in ROOT.iterdir()}
    require(present==set(entries)|{'SHA256SUMS'},'file inventory differs')
    for name,digest in entries.items():
        p=ROOT/name
        require(p.is_file() and not p.is_symlink(),'not an ordinary file')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'changed bytes: '+name)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true',help='unauthenticated production only')
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    if args.write:
        require(args.check is None, 'select one mode')
        (ROOT/'result.json').write_text(canonical(run()))
    else:
        require(args.check is not None,'use --check result.json or --write')
        authenticate()
        expected=run()
        actual=strict_json(args.check)
        require(canonical(actual)==canonical(expected),'mathematical reconstruction differs')
        print(canonical(expected),end='')
