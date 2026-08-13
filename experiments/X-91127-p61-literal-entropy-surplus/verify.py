#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from functools import lru_cache
from math import isqrt, prod
import bisect, json, time
from pathlib import Path

PRIMES=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)
P=prod(PRIMES)
D=10**45

@dataclass(frozen=True)
class FI:
    lo:int
    hi:int
    def __add__(self,o):
        o=asfi(o); return FI(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return FI(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asfi(o))
    def __rsub__(self,o): return asfi(o)-self
    def __mul__(self,o):
        o=asfi(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return FI(min(vals)//D, -((-max(vals))//D))
    __rmul__=__mul__
    def scale(self,q):
        q=Fraction(q)
        vals=(self.lo*q.numerator,self.hi*q.numerator)
        if q.numerator>=0:
            return FI(vals[0]//q.denominator,-((-vals[1])//q.denominator))
        return FI(vals[1]//q.denominator,-((-vals[0])//q.denominator))

def asfi(x):
    if isinstance(x,FI): return x
    q=Fraction(x); return FI((q.numerator*D)//q.denominator,-((-q.numerator*D)//q.denominator))

def rec_pos(x):
    assert x.lo>0
    return FI((D*D)//x.hi,-((-(D*D))//x.lo))

def invsqrt_int(n):
    z=n*D*D; r=isqrt(z); hi=r if r*r==z else r+1
    return rec_pos(FI(r,hi))

def sqrt_int(n):
    z=n*D*D; r=isqrt(z); hi=r if r*r==z else r+1
    return FI(r,hi)

@lru_cache(None)
def log_int(n):
    if n==1:return FI(0,0)
    with localcontext() as ctx:
        ctx.prec=75
        z=Decimal(n).ln()*Decimal(D)
        lo=int(z.to_integral_value(rounding=ROUND_FLOOR))-2
        hi=int(z.to_integral_value(rounding=ROUND_CEILING))+2
    return FI(lo,hi)

def log_ratio(a,b): return log_int(a)-log_int(b)

# Generate all squarefree divisors, signs, and log intervals from prime logs.
divs=[(1,1,FI(0,0))]
for q in PRIMES:
    lq=log_int(q)
    old=list(divs)
    divs += [(d*q,-mu,ld+lq) for d,mu,ld in old]
divs.sort(key=lambda z:z[0])
assert len(divs)==2**18

# Global prefix corridors.
a_num=0
A1=FI(0,0); B0=FI(0,0)
min_a_num=None; max_a1=None; min_b0=None; max_b0=None
b067=None
small_by_n={}
for d,mu,ld in divs:
    a_num += mu*(P//d)
    inv=invsqrt_int(d)
    A1 += (ld.scale(Fraction(mu,d)))
    B0 += inv.scale(mu)
    if d<=15000: small_by_n[d]=(mu,ld,inv)
    if d<=67: b067=B0
    if d>=67:
        if min_a_num is None or a_num<min_a_num:min_a_num=a_num
        if max_a1 is None or A1.hi>max_a1:max_a1=A1.hi
        if min_b0 is None or B0.lo<min_b0:min_b0=B0.lo
        if max_b0 is None or B0.hi>max_b0:max_b0=B0.hi
assert min_a_num*61>P
assert max_a1 < -Fraction(9,100)*D
assert min_b0 > -D
assert max_b0 < Fraction(27,20)*D
assert b067 is not None and b067.lo > -Fraction(14,25)*D

C=FI(D,D)
for q in PRIMES:C=C*(FI(D,D)+invsqrt_int(q))
assert C.hi<60*D

# Lambda_P(n): log n if no P-prime divides n; log q if exactly one; else zero.
L=FI(0,0)
M=FI(0,0)
a_num=0; b=FI(0,0)
min_B=None
# terminal score minimum and finite data through 67
min_terminal_score=None
# store prefixes for D67
L67=M67=None; a67=None; b67=None
for n in range(1,15000):
    if n>=2:
        ds=[q for q in PRIMES if n%q==0]
        lam=log_int(n) if len(ds)==0 else log_int(ds[0]) if len(ds)==1 else FI(0,0)
        term=lam*invsqrt_int(n)
        L += term
        M += term*log_int(n)
    if n in small_by_n:
        mu,ld,inv=small_by_n[n]
        a_num += mu*(P//n)
        b += inv.scale(mu)
    a=FI((a_num*D)//P,-((-a_num*D)//P))
    if n>=67:
        assert a.lo>0
        B=L-(sqrt_int(n+1)*a).scale(Fraction(5,2))
        assert B.lo>13*D,(n,B.lo/D)
        if min_B is None or B.lo<min_B[0]:min_B=(B.lo,n)
    if n<=66:
        t=n if a.lo>=0 else n+1
        score=5*(sqrt_int(t)*a)-3*b
        assert score.lo>D,(n,score.lo/D)
        if min_terminal_score is None or score.lo<min_terminal_score[0]:min_terminal_score=(score.lo,n,t)
    if n==67:
        L67,M67,a67,b67=L,M,a,b

# Uniform A approximation finite base N<=8.
A=FI(0,0)
for n in range(1,9):
    if n>=2:A += log_int(n)*invsqrt_int(n)
    for t in (n,n+1):
        F0=2*sqrt_int(t)*(log_int(t)-2)+4
        err=A-F0
        assert err.lo>-Fraction(1,2)*D and err.hi<Fraction(1,2)*D

# D_P(67)=E_P(67)-S_P(67).
E67=log_int(67)*L67-M67
S67=5*(sqrt_int(67)*a67)-3*b67
D67=E67-S67
assert D67.lo>15*D
assert E67.hi<18*D

# Analytic tail constants.
assert log_int(15000).lo>Fraction(48,5)*D
assert 122*122<15000
analytic=2*122*((Fraction(48,5)-Fraction(13,4))/61+Fraction(9,100))-34
assert analytic==Fraction(334,25)>13
final=Fraction(559,50)-Fraction(18,8)
assert final==Fraction(893,100)>0

res={
 'classification':'PASS_P61_LITERAL_ENTROPY_SURPLUS',
 'checks':{
   'divisor_states':len(divs),
   'B_cells':15000-67,
   'terminal_score_cells':66,
 },
 'prefix_corridors':{
   'min_A0_lower':str(Fraction(min_a_num,P)),
   'max_A1_upper_decimal':max_a1/D,
   'min_B0_lower_decimal':min_b0/D,
   'max_B0_upper_decimal':max_b0/D,
   'B0_at_67_lower_decimal':b067.lo/D,
   'sum_abs_inv_sqrt_upper_decimal':C.hi/D,
 },
 'B_min_cell':{'left':min_B[1],'lower_decimal':min_B[0]/D,'certified_above':13},
 'terminal_score_min':{'cell':min_terminal_score[1],'endpoint':min_terminal_score[2],'lower_decimal':min_terminal_score[0]/D,'certified_above':1},
 'E67':{'lower_decimal':E67.lo/D,'upper_decimal':E67.hi/D,'certified_below':18},
 'D67':{'lower_decimal':D67.lo/D,'certified_above':15},
 'analytic_B_tail_margin':str(analytic),
 'one_prime_entropy_surplus':{'certified_above':str(final)},
}
text=json.dumps(res,indent=2,sort_keys=True)
out=Path(__file__).resolve().parent/'results'/'verification.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(text+'\n')
print(res['classification'])
print(out)
