#!/usr/bin/env python3
"""Credited NCL29 arithmetic excerpt, retained at 144 bits.

Interval operations, elementary functions and arithmetic helpers are copied
from NCL29 check.py through mu_sieve. This is NOT an independent backend.
See SOURCES.md for exact source identity. No predecessor campaign is run here.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
from math import factorial, gcd, isqrt, lcm
from pathlib import Path
from typing import Iterable

BITS = 144
SCALE = 1 << BITS
IV = tuple[int, int]
ZERO: IV = (0, 0)
ONE: IV = (SCALE, SCALE)
ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def ceildiv(a: int, b: int) -> int:
    require(b > 0, 'nonpositive integer denominator')
    return -((-a) // b)


def rat(x: int | F) -> IV:
    v = F(x)
    return v.numerator * SCALE // v.denominator, ceildiv(v.numerator * SCALE, v.denominator)


def add(a: IV, b: IV) -> IV:
    return a[0] + b[0], a[1] + b[1]


def neg(a: IV) -> IV:
    return -a[1], -a[0]


def sub(a: IV, b: IV) -> IV:
    return add(a, neg(b))


def mul(a: IV, b: IV) -> IV:
    v = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(v)//SCALE, ceildiv(max(v), SCALE)


def scale(a: IV, r: int | F) -> IV:
    x = F(r)
    if x < 0:
        return scale(neg(a), -x)
    return a[0]*x.numerator//x.denominator, ceildiv(a[1]*x.numerator, x.denominator)


def divint(a: IV, n: int) -> IV:
    require(n > 0, 'nonpositive divisor')
    return a[0]//n, ceildiv(a[1], n)


def square(a: IV) -> IV:
    v = min(a[0]*a[0], a[1]*a[1]) if a[0]*a[1] > 0 else 0
    return v//SCALE, ceildiv(max(a[0]*a[0], a[1]*a[1]), SCALE)


def reciprocal(a: IV) -> IV:
    require(a[0] > 0, 'reciprocal interval touches zero')
    return SCALE*SCALE//a[1], ceildiv(SCALE*SCALE, a[0])


def sumiv(values: Iterable[IV]) -> IV:
    lo = hi = 0
    for a,b in values:
        lo += a
        hi += b
    return lo, hi


def contains(a: IV, r: int | F) -> bool:
    x = F(r)*SCALE
    return a[0] <= x <= a[1]


def overlaps(a: IV, b: IV) -> bool:
    return max(a[0],b[0]) <= min(a[1],b[1])


def decimal_endpoint(n: int, places: int, upper: bool) -> str:
    v = ceildiv(n*10**places, SCALE) if upper else n*10**places//SCALE
    sign = '-' if v < 0 else ''
    v = abs(v)
    return f'{sign}{v//10**places}.{v%10**places:0{places}d}'


def enc(a: IV) -> dict:
    require(a[0] <= a[1], 'reversed interval')
    return {'lo': str(a[0]), 'hi': str(a[1]), 'bits': BITS,
            'decimal_outward': [decimal_endpoint(a[0],16,False),decimal_endpoint(a[1],16,True)]}


def frac(r: F) -> list[str]:
    return [str(r.numerator), str(r.denominator)]


@lru_cache(None)
def ataninverse(d: int) -> IV:
    require(d >= 2, 'arctangent parameter')
    n = 128
    acc = ZERO
    for j in range(n):
        acc = add(acc, rat(F((-1)**j, (2*j+1)*d**(2*j+1))))
    # Alternating series: n even, next term positive.
    tail = rat(F(1,(2*n+1)*d**(2*n+1)))
    return acc[0], acc[1]+tail[1]


@lru_cache(None)
def pi_iv() -> IV:
    # Machin identity. A distinct arctan(1/2)+arctan(1/3) reference is tested.
    return sub(scale(ataninverse(5),16),scale(ataninverse(239),4))


@lru_cache(None)
def cos_fraction(a: int, q: int) -> IV:
    require(q > 0, 'cos denominator')
    a %= q
    a = min(a, q-a)
    if a == 0:
        return ONE
    g = gcd(a,q)
    if g > 1:
        return cos_fraction(a//g,q//g)
    x = scale(pi_iv(),F(2*a,q))
    xx = square(x)
    term, out = ONE, ONE
    for j in range(1,49):
        term = divint(mul(term,xx),(2*j-1)*(2*j))
        out = add(out,term) if j%2 == 0 else sub(out,term)
    err = ceildiv(SCALE*4**98,factorial(98))
    # Taylor degree 97 (zero odd coefficient), real argument in [0,pi]<4.
    return max(-SCALE,out[0]-err), min(SCALE,out[1]+err)


def atanhpositive(z: IV) -> IV:
    require(0 <= z[0] <= z[1] <= ceildiv(SCALE,3), 'atanh domain')
    z2 = mul(z,z)
    term, out = z, ZERO
    for j in range(96):
        out = add(out,divint(term,2*j+1))
        term = mul(term,z2)
    out = scale(out,2)
    # Exact argument <=1/3. Full positive Taylor tail beyond exponent 191.
    tail = rat(F(9,4*193*3**193))
    return out[0], out[1]+tail[1]


@lru_cache(None)
def log2_iv() -> IV:
    return atanhpositive(rat(F(1,3)))


def log_dyadic(t: int) -> IV:
    require(t > 0, 'log requires positive input')
    k = t.bit_length()-1-BITS
    if k >= 0:
        num, den = t, SCALE << k
    else:
        num, den = t << (-k), SCALE
    require(den <= num < 2*den, 'log range reduction')
    z = rat(F(num-den,num+den))
    return add(scale(log2_iv(),k),atanhpositive(z))


def log_iv(x: IV) -> IV:
    require(x[0] > 0, 'log interval touches zero')
    return log_dyadic(x[0])[0], log_dyadic(x[1])[1]


@lru_cache(None)
def log_sine(a: int,q: int) -> IV:
    require(0 < a < q, 'log-sine root')
    # log(2sin(pi*a/q)) = (1/2)log(2-2cos(2pi*a/q)).
    return divint(log_iv(sub(rat(2),scale(cos_fraction(a,q),2))),2)


@lru_cache(None)
def factors(n: int) -> tuple[tuple[int,int], ...]:
    require(n >= 1, 'factor domain')
    out=[]
    p=2
    while p*p<=n:
        if n%p == 0:
            k=0
            while n%p == 0:
                n//=p; k+=1
            out.append((p,k))
        p+=1
    if n>1: out.append((n,1))
    return tuple(out)


@lru_cache(None)
def divisors(n: int) -> tuple[int, ...]:
    ds=[1]
    for p,a in factors(n):
        ds=[d*p**j for d in ds for j in range(a+1)]
    return tuple(sorted(ds))


def mu_trial(n: int) -> int:
    fs=factors(n)
    return 0 if any(a>1 for _,a in fs) else (-1)**len(fs)


def mu_sieve(N: int) -> list[int]:
    mu=[1]*(N+1); mu[0]=0
    mark=bytearray(N+1)
    for p in range(2,N+1):
        if not mark[p]:
            for k in range(p,N+1,p):
                mu[k]=-mu[k]
                if k>p: mark[k]=1
            for k in range(p*p,N+1,p*p): mu[k]=0
    return mu
