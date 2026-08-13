#!/usr/bin/env python3
from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt, prod
import json
from pathlib import Path

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
P61 = prod(PRIMES)
SCALE = 10**55
SHIFT = 8
CHILD_MAX = 67
SWITCH = 67*67

@dataclass(frozen=True)
class I:
    lo: int
    hi: int
    def __add__(self,o):
        o=as_i(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-as_i(o))
    def __rsub__(self,o): return as_i(o)-self
    def __mul__(self,o):
        o=as_i(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(vals)//SCALE,-((-max(vals))//SCALE))
    __rmul__=__mul__
    def lower(self): return self.lo/SCALE
    def upper(self): return self.hi/SCALE

def floor_scaled(x:Fraction)->int: return (x.numerator*SCALE)//x.denominator
def ceil_scaled(x:Fraction)->int: return -((-x.numerator*SCALE)//x.denominator)
def as_i(x):
    if isinstance(x,I): return x
    if isinstance(x,int): return I(x*SCALE,x*SCALE)
    if isinstance(x,Fraction): return I(floor_scaled(x),ceil_scaled(x))
    raise TypeError(type(x))

def sqrt_i(n:int)->I:
    q=n*SCALE*SCALE; m=isqrt(q)
    return I(m,m if m*m==q else m+1)

def invsqrt_i(n:int)->I:
    q=(SCALE*SCALE)//n; m=isqrt(q)
    return I(m,m if m*m*n==SCALE*SCALE else m+1)

def generate_divisors():
    vals=[(1,1)]
    for p in PRIMES:
        vals += [(d*p,-mu) for d,mu in list(vals)]
    return sorted(vals)

def prefix_interval(values,index):
    if index<0:return I(0,0)
    return values[index]

def certify():
    divs=generate_divisors()
    assert len(divs)==2**18
    evens=[d for d,mu in divs if mu==1]
    odds=[d for d,mu in divs if mu==-1]

    even_rec=[]; n=0
    even_sqrt=[]; s=I(0,0)
    for d in evens:
        n += P61//d; even_rec.append(n)
        s += invsqrt_i(d); even_sqrt.append(s)
    odd_rec=[]; n=0
    odd_sqrt=[]; s=I(0,0)
    for d in odds:
        n += P61//d; odd_rec.append(n)
        s += invsqrt_i(d); odd_sqrt.append(s)

    minimum=None; min_A=None; prefix_checks=0
    for t in odds:
        ie=bisect_right(evens,t+SHIFT)-1
        io=bisect_right(odds,t)-1
        anum=(even_rec[ie] if ie>=0 else 0)-(odd_rec[io] if io>=0 else 0)
        A=Fraction(anum,P61)
        B=prefix_interval(even_sqrt,ie)-prefix_interval(odd_sqrt,io)
        assert A>Fraction(1,67)
        z=t+SHIFT; root=sqrt_i(z)
        if z<=SWITCH:
            lower = root*as_i(5*A-Fraction(4,67))-3*B
        else:
            lower = 5*as_i(A)*root-3*B-268*invsqrt_i(z)
        assert lower.lo>as_i(Fraction(9,5)).hi,(t,A,B,lower.lower())
        rec=(lower.lo,t,A,B)
        if minimum is None or rec[0]<minimum[0]:minimum=rec
        if min_A is None or A<min_A[0]:min_A=(A,t)
        prefix_checks+=1

    small=[(d,mu) for d,mu in divs if d<=CHILD_MAX]
    thresholds=sorted({d for d,mu in small if mu==-1 and d>=2} | {CHILD_MAX})
    child_max=None; child_checks=0
    for t in thresholds:
        for N in range(1,CHILD_MAX+1):
            active=[(d,mu) for d,mu in small if d<=N]
            A=Fraction(0); B=I(0,0)
            for d,mu in active:
                coeff=0
                if mu==1 and d<=t+SHIFT: coeff=1
                elif mu==-1 and d<=t: coeff=-1
                if coeff:
                    A += Fraction(coeff,d); B += coeff*invsqrt_i(d)
            endpoints=(N,N+1) if N<CHILD_MAX else (CHILD_MAX,)
            for endpoint in endpoints:
                value=as_i(5*A-4)-3*B*invsqrt_i(endpoint)
                assert value.hi<0,(t,N,endpoint,A,B,value.upper())
                hnorm=value+4
                rec=(hnorm.hi,t,N,endpoint)
                if child_max is None or rec[0]>child_max[0]:child_max=rec
                child_checks+=1

    A_num=0; M=I(0,0)
    min_D=None; min_derivative=None; min_A_prefix=None; max_A_prefix=None
    prefix_normal_checks=0; derivative_checks=0
    for index,(d,mu) in enumerate(divs):
        if d>=2:
            A_left=Fraction(A_num,P61)
            D_left=as_i(A_left)-M*invsqrt_i(d)
            assert D_left.lo>as_i(Fraction(3,40)).hi,(d,A_left,M,D_left.lower())
            rec=(D_left.lo,d)
            if min_D is None or rec[0]<min_D[0]:min_D=rec
            prefix_normal_checks+=1

        A_num += mu*(P61//d)
        M += mu*invsqrt_i(d)
        A=Fraction(A_num,P61)
        assert A>=-1 and A<=1
        if min_A_prefix is None or A<min_A_prefix[0]:min_A_prefix=(A,d)
        if max_A_prefix is None or A>max_A_prefix[0]:max_A_prefix=(A,d)

        endpoints=[d]
        if index+1<len(divs): endpoints.append(divs[index+1][0])
        for endpoint in endpoints:
            derivative=as_i(A)-Fraction(1,2)*M*invsqrt_i(endpoint)
            assert derivative.lo>as_i(Fraction(1,40)).hi,(d,endpoint,A,M,derivative.lower())
            rec=(derivative.lo,d,endpoint)
            if min_derivative is None or rec[0]<min_derivative[0]:min_derivative=rec
            derivative_checks+=1

    t=47
    ie=bisect_right(evens,t+7)-1; io=bisect_right(odds,t)-1
    A7=Fraction((even_rec[ie] if ie>=0 else 0)-(odd_rec[io] if io>=0 else 0),P61)
    assert A7<0

    result={
      'classification':'PASS_P61_SCORE_HALL_AND_LORENZ_PREFIX',
      'small_prime_block':PRIMES,
      'divisor_states':len(divs),
      'score_hall_prefix_checks':prefix_checks,
      'minimum_shifted_reciprocal_prefix':{
        'lower_decimal':float(min_A[0]),'threshold':min_A[1],
        'certified_above':'1/67'},
      'minimum_nonterminal_score_hall_bound':{
        'lower_decimal':minimum[0]/SCALE,'threshold':minimum[1],
        'certified_above':'9/5'},
      'child_score_envelope_checks':child_checks,
      'maximum_child_score_hall_over_sqrt_y':{
        'upper_decimal':child_max[0]/SCALE,'threshold':child_max[1],
        'cell':child_max[2],'endpoint':child_max[3],
        'certified_below':'4'},
      'left_prefix_D_checks':prefix_normal_checks,
      'minimum_left_prefix_D':{
        'lower_decimal':min_D[0]/SCALE,'cutoff':min_D[1],
        'certified_above':'3/40'},
      'F_derivative_checks':derivative_checks,
      'minimum_F_derivative':{
        'lower_decimal':min_derivative[0]/SCALE,
        'cell_start':min_derivative[1],'endpoint':min_derivative[2],
        'certified_above':'1/40'},
      'A_prefix_range':{
        'minimum':str(min_A_prefix[0]),'minimum_at':min_A_prefix[1],
        'maximum':str(max_A_prefix[0]),'maximum_at':max_A_prefix[1],
        'certified_inside':'[-1,1]'},
      'radius_seven_witness':{'threshold':47,'value':str(A7),'negative':True},
      'scope':(
        'Exact reciprocal arithmetic and directed square-root enclosures certify '
        'the score-currency displacement-eight Hall gates and the three finite '
        'prefix inequalities used by the symbolic Lorenz/likelihood-ratio theorem. '
        'The checker does not certify the remaining row subordination or RH.'),
    }
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification'])
    print(json.dumps(result['minimum_left_prefix_D'],sort_keys=True))
    print(json.dumps(result['minimum_F_derivative'],sort_keys=True))
    print(out)

if __name__=='__main__':certify()
