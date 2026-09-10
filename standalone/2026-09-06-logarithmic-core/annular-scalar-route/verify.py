#!/usr/bin/env python3
"""Bounded exact controls for the annular scalar route; NOT an RH checker."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path

BITS = 160
Q = 1 << BITS

def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

def ceildiv(a: int, b: int) -> int:
    need(b > 0, 'nonpositive denominator')
    return -((-a) // b)

class I:
    """Closed outward dyadic intervals, with no binary floating-point operations."""
    def __init__(self, lo: int, hi: int):
        need(type(lo) is int and type(hi) is int and lo <= hi, 'invalid interval')
        self.lo, self.hi = lo, hi
    @staticmethod
    def of(x: F | int) -> 'I':
        f = F(x)
        return I(f.numerator*Q // f.denominator, ceildiv(f.numerator*Q, f.denominator))
    def __add__(self, other):
        o = other if isinstance(other, I) else I.of(other)
        return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -I.of(other))
    def __rsub__(self, other):
        return (-self) + other
    def __mul__(self, other):
        o = other if isinstance(other, I) else I.of(other)
        p = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(p)//Q, ceildiv(max(p), Q))
    __rmul__ = __mul__
    def inv(self):
        need(not self.lo <= 0 <= self.hi, 'division by interval containing zero')
        vals = [F(Q*Q, self.lo), F(Q*Q, self.hi)]
        a,b = min(vals),max(vals)
        return I(a.numerator//a.denominator, ceildiv(b.numerator,b.denominator))
    def __truediv__(self, other):
        o = other if isinstance(other, I) else I.of(other)
        return self * o.inv()
    def __pow__(self, n):
        need(type(n) is int and n >= 0, 'invalid exponent')
        out, base = I.of(1), self
        while n:
            if n & 1: out = out * base
            base = base * base
            n //= 2
        return out
    def bounds(self):
        return [str(F(self.lo,Q)), str(F(self.hi,Q))]
    def decimals(self, places=12):
        scale=10**places
        def fmt(n):
            sign='-' if n<0 else ''
            n=abs(n)
            return sign+str(n//scale)+'.'+str(n%scale).zfill(places)
        return [fmt(self.lo*scale//Q),fmt(ceildiv(self.hi*scale,Q))]

@lru_cache(None)
def log_exact(x: F) -> I:
    x=F(x)
    need(x>0, 'log domain')
    k=0
    while x>2: x/=2; k+=1
    while x<1: x*=2; k-=1
    z=I.of((x-1)/(x+1)); z2=z*z
    s=I.of(0); power=z
    for j in range(80):
        s=s+power*F(2,2*j+1)
        power=power*z2
    # z lies in [0,1/3]. The omitted positive tail is bounded analytically.
    rem=F(2,1)*F(1,3)**161/F(161,1)/(1-F(1,9))
    s=I(s.lo,(s+I.of(rem)).hi)
    if k: s=s+k*log_exact(F(2))
    return s

def log_interval(x: I) -> I:
    need(x.lo>0, 'log interval domain')
    return I(log_exact(F(x.lo,Q)).lo, log_exact(F(x.hi,Q)).hi)

def sqrt_interval(x: I) -> I:
    need(x.lo>=0, 'sqrt domain')
    a=isqrt(x.lo*Q); b=isqrt(x.hi*Q)
    if b*b<x.hi*Q: b+=1
    return I(a,b)

def pi_interval() -> I:
    def atan(z):
        s=I.of(0); zz=I.of(z); power=zz; z2=zz*zz
        for j in range(96):
            s=s+power*F((-1)**j,2*j+1)
            power=power*z2
        rem=F(z)**193/F(193)
        # Absolute alternating-series remainder; either sign allowed.
        r=I.of(rem)
        return I(s.lo-r.hi,s.hi+r.hi)
    return 16*atan(F(1,5))-4*atan(F(1,239))

def source_constant() -> I:
    n=1024
    harmonic=sum((F(1,j) for j in range(1,n+1)),F(0))
    l=log_exact(F(n))
    # H_n-log(n)-1/(2n) < gamma < H_n-log(n)-1/(2n+1).
    lower=I.of(harmonic)-l-I.of(F(1,2*n))
    upper=I.of(harmonic)-l-I.of(F(1,2*n+1))
    gamma=I(lower.lo,upper.hi)
    return (I.of(F(47,64))-F(21,64)*(gamma+log_interval(pi_interval()))
            +F(115,96)*log_exact(F(2))-F(641,1728)*log_exact(F(3))
            -F(65,192)*log_exact(F(5)))

def prime_powers(limit):
    need(type(limit) is int and limit>=2,'invalid sieve limit')
    prime=[True]*(limit+1); prime[0]=prime[1]=False
    for p in range(2,isqrt(limit)+1):
        if prime[p]:
            for k in range(p*p,limit+1,p): prime[k]=False
    out={}
    for p in range(2,limit+1):
        if prime[p]:
            n=p
            while n<=limit:
                need(n not in out,'prime power duplicate')
                out[n]=p
                n*=p
    return out

def trial_prime_base(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return p if m==1 else None
    return None

def annular_coeff(m,n):
    # B_m/(192*m^3), with exact quarter endpoint and centre conventions.
    if 4*n<=m*m or n>4*m*m: return F(0)
    if n<=m*m: return (64*F(n)-F(m**6,n*n))/F(192*m**3)
    return (F(64*m**6,n*n)-n)/F(192*m**3)

def reconstruct():
    counts=Counter()
    def check(group,condition):
        need(condition,group+' failed'); counts[group]+=1
    c=F(1,8)
    # Inverse filter and Mellin response: pure rational controls.
    eta=lambda k: c**abs(k)/(1-c*c)
    for k in range(-24,25):
        check('inverse_filter', (1+c*c)*eta(k)-c*eta(k-1)-c*eta(k+1)==(1 if k==0 else 0))
    for k in range(-5,8):
        rho=F(k,2)
        if rho in (F(-1),F(2)): continue
        power=lambda t: F(2)**int(2*t)
        def integ(a,b,p):
            need(p+1!=0,'test primitive pole')
            return (power(b*(p+1))-power(a*(p+1)))/(p+1)
        # a,b are powers of four, hence 4^(a*(p+1))=2^(2a(p+1)).
        direct=(integ(-1,0,rho)/3-integ(-1,0,rho-3)/192
                +integ(0,1,rho-3)/3-integ(0,1,rho)/192)
        z=rho-F(1,2)
        response=(1+c*c-c*(power(z)+power(-z)))/(F(9,4)-z*z)
        check('mellin_response',direct==response)
    check('main_constant', (1+c*c-c*(2+F(1,2)))/2==F(45,128))
    # Positive compact Green bump; square-root ratio is rational.
    g=lambda r:(r**3-r**-3)/2 if r>=1 else F(0)
    for numerator in range(1,33):
        r=F(numerator,8)
        filtered=(1+c*c)*g(r)-c*g(r/2)-c*g(2*r)
        expected=-c*g(2*min(r,1/r)) if F(1,2)<r<2 else F(0)
        check('cusp_filter',filtered==expected)
    # Formal coefficient reconstruction of V(0): order 1,gamma,logpi,log2,log3,log5,P2.
    def vec(*v): return tuple(map(F,v))
    def add(*vs): return tuple(sum(t,F(0)) for t in zip(*vs))
    def mul(a,v): return tuple(a*t for t in v)
    w0=vec(1,F(-1,3),F(-1,3),0,0,0,F(-2,3))
    cb=vec(F(1,3),F(-1,3),F(-1,3),F(-1,3),0,0,0)
    sgd=vec(F(1,12),0,0,F(-16,3),F(21,16),F(65,48),0)
    # S_G(log 4)=1/12+(1/48)log(5/3)+(4/3)log(15/16).
    wd=add(vec(1,0,0,F(7,12),F(37,216),0,F(-65,24)),mul(F(1,8),cb),sgd)
    observed=add(mul(F(65,64),w0),mul(F(-1,4),wd))
    expected=vec(F(47,64),F(-21,64),F(-21,64),F(115,96),F(-641,1728),F(-65,192),0)
    check('constant_cancellation',observed==expected)
    C=source_constant()
    check('source_C_bounds',C.lo>Q//25 and C.hi<Q//20)
    sg0=I.of(F(1,6))+log_exact(F(2))/3
    check('gamma_bound',sg0.hi<(I.of(F(2,5))).lo)
    # Samples for scalar open target only, not arbitrary test-function positivity.
    pp=prime_powers(4*64**2)
    for n in range(2,257):
        check('sieve_independence',pp.get(n)==trial_prime_base(n))
    records=[]
    for m in range(2,65):
        total=I.of(0); used=0
        for n,p in pp.items():
            weight=annular_coeff(m,n)
            need(weight>=0,'negative annular weight')
            if weight:
                total=total+weight*log_exact(F(p)); used+=1
        counts['weight_nonnegative_rows']+=1
        margin=total-F(45*m,128)+F(1,4)
        check('sample_scalar_sign',margin.lo>0)
        records.append({'m':m,'prime_power_terms':used,'margin':margin.bounds()})
    # Continuous-source countercontrol coefficient nonzero at rho=3/4, no oscillation claim inferred.
    for m in range(2,65):
        check('square_sample_normalization',F(45*m,128)*192*m**3==F(135*m**4,2))
        check('rational_slack_normalization',F(1,4)*192*m**3==48*m**3)
    payload={
        'status':'PASS_BOUNDED_ANNULAR_CONTROLS',
        'rh_proved':False,
        'unbounded_arithmetic_inequality_proved':False,
        'new_full_window_positivity_proved':False,
        'arithmetic':'integer/Fraction; outward dyadic logs; no floating point',
        'bits':BITS,
        'groups':dict(sorted(counts.items())),
        'C0_interval':C.bounds(), 'C0_decimal_enclosure':C.decimals(10),
        'sample_scope':'integers m=2,...,64; scalar annular inequality only',
        'sample_count':len(records),
        'sample_minimum_margin':I(min(int(F(r['margin'][0])*Q) for r in records), min(int(F(r['margin'][1])*Q) for r in records)).decimals(10),
        'samples_digest':sha256(json.dumps(records,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        'sample_first_last':[records[0]['m'], records[-1]['m']],
    }
    return payload

def load_json(path):
    def pairs(items):
        d={}
        for k,v in items:
            need(k not in d,'duplicate JSON key'); d[k]=v
        return d
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',type=Path)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    data=reconstruct()
    text=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if args.check:
        # Canonical JSON distinguishes true/1 and integer/float aliases.
        need(json.dumps(load_json(args.check),sort_keys=True,separators=(',',':'))==json.dumps(data,sort_keys=True,separators=(',',':')),'stored result mismatch')
    if args.out: args.out.write_text(text)
    print(text,end='')

if __name__=='__main__': main()
