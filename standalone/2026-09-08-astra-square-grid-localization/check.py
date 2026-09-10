#!/usr/bin/env python3
"""Exact finite controls and a directed prime-count sample-energy certificate.

All numeric primitives are Python integers/Fractions. Infinite theorems and
Brun--Titchmarsh are not proved by this code. Run --check result.json to compare
with a fresh reconstruction; assertions are not used for acceptance.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import json
from math import factorial, isqrt
from pathlib import Path
import sys

BITS = 160
SCALE = 1 << BITS
LOG_TERMS = 72
EI_TERMS = 128
MAX_N = 128

def need(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)

def ceildiv(a: int, b: int) -> int:
    need(b > 0, 'nonpositive denominator')
    return -((-a) // b)

@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        need(type(self.lo) is int and type(self.hi) is int, 'noninteger endpoint')
        need(self.lo <= self.hi, 'reversed interval')

    @staticmethod
    def rat(n: int, d: int = 1) -> 'I':
        need(d > 0, 'nonpositive rational denominator')
        return I(n * SCALE // d, ceildiv(n * SCALE, d))

    def __add__(self, other: 'I') -> 'I':
        return I(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> 'I':
        return I(-self.hi, -self.lo)

    def __sub__(self, other: 'I') -> 'I':
        return self + (-other)

    def __mul__(self, other: 'I') -> 'I':
        p = [self.lo*other.lo, self.lo*other.hi,
             self.hi*other.lo, self.hi*other.hi]
        return I(min(p)//SCALE, ceildiv(max(p), SCALE))

    def __truediv__(self, other: 'I') -> 'I':
        need(other.lo > 0, 'interval division crosses zero')
        return self * I(SCALE*SCALE//other.hi,
                        ceildiv(SCALE*SCALE, other.lo))

    def sq(self) -> 'I':
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo*self.lo, self.hi*self.hi)
        high = max(self.lo*self.lo, self.hi*self.hi)
        return I(low//SCALE, ceildiv(high, SCALE))

    def record(self) -> dict[str, str]:
        return {'lo': str(self.lo), 'hi': str(self.hi), 'denominator': str(SCALE)}

ZERO, ONE = I.rat(0), I.rat(1)

def unit_log(n: int, d: int) -> I:
    """Log(n/d) for 1<=n/d<=2, with the complete atanh tail."""
    need(d <= n <= 2*d, 'log range reduction failed')
    q = I.rat(n-d, n+d)
    q2 = q*q
    power, total = q, ZERO
    for j in range(LOG_TERMS):
        total = total + power / I.rat(2*j+1)
        power = power*q2
    # 2 sum_(j>=K) q^(2j+1)/(2j+1) <= 9/[4(2K+1)3^(2K+1)].
    rem = I.rat(9, 4*(2*LOG_TERMS+1)*3**(2*LOG_TERMS+1)).hi
    twice = I.rat(2)*total
    return I(twice.lo, twice.hi+rem)

LN2 = unit_log(2, 1)
need(LN2.lo*3 > 2*SCALE, 'log2 lower bound')

@lru_cache(maxsize=None)
def log_ratio(n: int, d: int = 1) -> I:
    need(n > 0 and d > 0, 'log nonpositive argument')
    k = 0
    while n >= 2*d:
        d *= 2
        k += 1
    while n < d:
        n *= 2
        k -= 1
    return unit_log(n, d) + I.rat(k)*LN2

def log_interval(a: I) -> I:
    need(a.lo > 0, 'log interval crosses zero')
    return I(log_ratio(a.lo, SCALE).lo, log_ratio(a.hi, SCALE).hi)

def li_square(n: int) -> I:
    """Integral_2^(n^2) 1/log(x) dx; no special-function oracle."""
    L = I.rat(2)*log_ratio(n)
    a = LN2
    need(L.hi < 10*SCALE and L.lo >= a.hi, 'Ei range contract')
    total = log_interval(L/a)
    pL, pa = ONE, ONE
    for j in range(1, EI_TERMS+1):
        pL = pL*L/I.rat(j)
        pa = pa*a/I.rat(j)
        total = total + (pL-pa)/I.rat(j)
    # Tail difference is nonnegative since L>=a. Bound it by the L tail,
    # with L<10: next term times geometric ratio <=10/(K+2).
    K = EI_TERMS
    tail = F(10**(K+1), (K+1)*factorial(K+1)) / (1-F(10, K+2))
    rem = ceildiv(tail.numerator*SCALE, tail.denominator)
    return I(total.lo, total.hi+rem)

def sieve(limit: int) -> list[int]:
    flags = bytearray(b'\x01')*(limit+1)
    flags[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if flags[p]:
            for k in range(p*p, limit+1, p):
                flags[k] = 0
    return [i for i in range(2, limit+1) if flags[i]]

def trial_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n)+1):
        if n % d == 0:
            return False
    return True

def run() -> dict:
    groups: list[dict] = []
    # Bounded controls for the precise stable norm adapter.
    for y in [F(0), F(1,4), F(1,2), F(1), F(2), F(3), F(7)]:
        ratio = (y*y+F(1,4))/(y*y+1)
        need(F(1,4) <= ratio <= 1, 'adapter norm')
        # Squared moduli of forward/inverse transfers multiply to one.
        need(ratio*((y*y+1)/(y*y+F(1,4))) == 1, 'adapter inverse')
    groups.append({'name':'stable_metric_adapter', 'cases':7})

    variance_cases = 0
    for values, weights in [([F(-2),F(1),F(4)],[F(1),F(2),F(3)]),
                             ([F(3),F(3)],[F(1,3),F(7)]),
                             ([F(-5),F(2)],[F(1),F(1)]),
                             ([F(0),F(1),F(-1),F(3)],[F(2),F(1),F(4),F(3)]),
                             ([F(1,7),F(-2,5),F(4,3)],[F(1,2),F(1,3),F(1,5)])]:
        w=sum(weights); mean=sum(a*b for a,b in zip(values,weights))/w
        energy=sum(b*a*a for a,b in zip(values,weights))
        detail=sum(b*(a-mean)**2 for a,b in zip(values,weights))
        need(energy == w*mean*mean+detail, 'Pythagorean identity')
        need(detail <= w*(max(values)-min(values))**2/4, 'variance range')
        variance_cases += 1
    groups.append({'name':'weighted_projection_identities','cases':variance_cases})

    for n in range(2, MAX_N+1):
        h=2*n+1; w=F(1,n*n)-F(1,(n+1)**2)
        need(w == F(h,n*n*(n+1)**2), 'cell weight')
        need(F(1,n**3) < w < F(2,n**3), 'sample comparability')
        need(h <= F(5,2)*n and h <= n**4, 'cell range')
        need(F(h**3, n*n*(n+1)**2) <= F(125,8*n), 'detail constant')
    need(F(125,8)*F(7,4) == F(875,32) < 28, 'infinite-tail constant')
    groups.append({'name':'square_geometry','cases':MAX_N-1})

    primes=sieve(MAX_N*MAX_N)
    independent=[n for n in range(2, MAX_N*MAX_N+1) if trial_prime(n)]
    need(primes == independent, 'primitive prime replay')
    counts=[0]*(MAX_N*MAX_N+1); pset=set(primes)
    for x in range(1,len(counts)):
        counts[x]=counts[x-1]+int(x in pset)
    groups.append({'name':'integer_prime_sieve_vs_trial',
                   'integers_through':MAX_N*MAX_N,'prime_count':len(primes)})

    for n in range(2, MAX_N):
        h=2*n+1; pc=counts[(n+1)**2]-counts[n*n]
        need(pc*log_ratio(h).hi < 2*h*SCALE, 'bounded BT fixture')
    groups.append({'name':'finite_square_cell_count_controls','cases':MAX_N-2})

    prefixes=[]; value=ZERO
    target={4:(23054869191,23054869193),8:(174282049867,174282049870),
            16:(330234902225,330234902228),32:(441341708779,441341708783),
            64:(515356116352,515356116356),128:(565641628407,565641628409)}
    for n in range(2, MAX_N):
        discrepancy=I.rat(counts[n*n])-li_square(n)
        w=F(1,n*n)-F(1,(n+1)**2)
        value=value+discrepancy.sq()*I.rat(w.numerator,w.denominator)
        M=n+1
        if M in target:
            lo,hi=target[M]
            need(value.lo*10**12 > lo*SCALE, 'prefix lower bound')
            need(value.hi*10**12 < hi*SCALE, 'prefix upper bound')
            prefixes.append({'M':M,'sample_energy':value.record(),
                             'decimal_bracket_numerators':[str(lo),str(hi)],
                             'decimal_bracket_denominator':'1000000000000'})
    groups.append({'name':'actual_sample_energy_certificates','cases':len(prefixes),
                   'sample_terms':MAX_N-2})

    # Stopped discrete energy with signed artificial innovations; no claim
    # these innovations are actual prime counts.
    for M in range(3,11):
        b=F(3,7); initial=b; square_energy=F(0); work=F(0)
        for n in range(2,M):
            u=F((-1)**n*(n+2),n+1)
            square_energy+=(F(1,n*n)-F(1,(n+1)**2))*b*b
            work+=(2*b*u+u*u)/((n+1)**2)
            b+=u
        need(square_energy+b*b/(M*M) == initial*initial/4+work,
             'complete stopped discrete work identity')
    groups.append({'name':'signed_discrete_endpoint_identity','cases':8})

    return {'schema':'SSQ26-finite-controls-v1','rh_proved':False,
            'global_coarse_tail_certified':False,
            'arithmetic':'160-bit outward dyadic intervals; Python integers and Fraction',
            'log_series_terms':LOG_TERMS,'li_series_terms':EI_TERMS,
            'external_BT_reproved':False,'groups':groups,'prefixes':prefixes}

def no_duplicates(pairs):
    d={}
    for k,v in pairs:
        if k in d:
            raise ValueError('duplicate JSON key: '+k)
        d[k]=v
    return d

def canonical(d: dict) -> str:
    return json.dumps(d,sort_keys=True,separators=(',',':'),allow_nan=False)

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',type=Path)
    args=p.parse_args()
    actual=run()
    if args.check:
        retained=json.loads(args.check.read_text(),object_pairs_hook=no_duplicates,
                            parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
        # Comparing canonical JSON distinguishes true from 1 and floats from ints.
        need(canonical(retained) == canonical(actual), 'retained result mismatch')
    print(json.dumps(actual,sort_keys=True,indent=2,allow_nan=False))
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ArithmeticError,ValueError,OSError,KeyError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
