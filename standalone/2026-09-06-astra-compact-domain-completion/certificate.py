#!/usr/bin/env python3
"""CD26 actual critical-source tail certificate: integer intervals only.

Eight prescribed Mobius truncations, every cell through Y=32768, and a
proved complete infinite tail. No floating-point or special-function oracle.
The finite certificates do not prove domain completion or an asymptotic.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

BITS=192
Q=1<<BITS
TERMS=72
Y=32768
ORDERS=(1,2,4,8,16,32,64,128)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo:int,hi:int):
        if type(lo) is not int or type(hi) is not int or lo>hi:
            raise ValueError('invalid dyadic endpoints')
        self.lo,self.hi=lo,hi
    @classmethod
    def rat(cls,p,q=1):
        if isinstance(p,F): p,q=p.numerator,p.denominator
        if type(p) is not int or type(q) is not int or q<=0:
            raise ValueError('invalid rational')
        return cls(p*Q//q,-((-p*Q)//q))
    @staticmethod
    def cv(o): return o if isinstance(o,I) else I.rat(o)
    def __add__(self,o):
        o=self.cv(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-self.cv(o)
    def __rsub__(self,o):return self.cv(o)+-self
    def __mul__(self,o):
        o=self.cv(o);vs=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return I(min(vs)//Q,-((-max(vs))//Q))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.cv(o)
        if o.lo<=0<=o.hi:raise ValueError('division by zero interval')
        lower=[];upper=[]
        for a in (self.lo,self.hi):
            for b in (o.lo,o.hi):
                p=a*Q
                if b<0:p,b=-p,-b
                lower.append(p//b);upper.append(-((-p)//b))
        return I(min(lower),max(upper))
    def square(self):
        v=[self.lo*self.lo,self.hi*self.hi]
        return I(0 if self.lo<=0<=self.hi else min(v)//Q,-((-max(v))//Q))
    def sqrt(self):
        if self.lo<0:raise ValueError('negative square-root interval')
        a=math.isqrt(self.lo*Q);v=self.hi*Q;b=math.isqrt(v)
        if b*b<v:b+=1
        return I(a,b)
    def record(self):return {'lo':str(self.lo),'hi':str(self.hi),'bits':BITS}

def log_ratio(p:int,q:int):
    if not 0<q<=p<=2*q:raise ValueError('log ratio outside [1,2]')
    if p==q:return I.rat(0)
    z=I.rat(p-q,p+q);z2=z*z;power=z;out=I.rat(0)
    for j in range(TERMS):
        out+=power*F(2,2*j+1);power=power*z2
    tail=I.rat(9,4*(2*TERMS+1)*3**(2*TERMS+1))
    return I(out.lo,out.hi+tail.hi)

LOG2=log_ratio(2,1)
def log_fraction(p:int,q:int=1):
    if p<=0 or q<=0:raise ValueError('log domain')
    k=p.bit_length()-q.bit_length()
    def scaled(k):return (p,q<<k) if k>=0 else (p<<(-k),q)
    a,b=scaled(k)
    if a<b:k-=1;a,b=scaled(k)
    if a>2*b:k+=1;a,b=scaled(k)
    return k*LOG2+log_ratio(a,b)

def atan_inverse(q:int):
    if q<2:raise ValueError('arctangent domain')
    out=I.rat(0)
    for j in range(TERMS):out+=F((-1)**j,(2*j+1)*q**(2*j+1))
    # TERMS even, so the next alternating term is positive.
    tail=I.rat(1,(2*TERMS+1)*q**(2*TERMS+1))
    return I(out.lo,out.hi+tail.hi)

PI=16*atan_inverse(5)-4*atan_inverse(239)
LOG2PI=I(log_fraction(2*PI.lo,Q).lo,log_fraction(2*PI.hi,Q).hi)

def mobius(nmax):
    if type(nmax) is not int or not 1<=nmax<=128:raise ValueError('Mobius resource contract')
    mu=[1]*(nmax+1);mu[0]=0;prime=[True]*(nmax+1)
    for p in range(2,nmax+1):
        if prime[p]:
            for j in range(p,nmax+1,p):prime[j]=False;mu[j]*=-1
            for j in range(p*p,nmax+1,p*p):mu[j]=0
    return mu

def coefficients(N):
    mu=mobius(N);s=sum((F(mu[n],n) for n in range(1,N+1)),F(0))
    c=[F(0)]+[F(mu[n]) for n in range(1,N+1)]+[-(N+1)*s]
    if sum((c[n]/n for n in range(1,N+2)),F(0))!=0:
        raise RuntimeError('pole balancing failure')
    return mu,c

def one(N,logs):
    mu,c=coefficients(N)
    aa=[F(0) for _ in range(Y+1)]
    for n in range(1,N+2):
        if c[n]:
            for k in range(n,Y+1,n):aa[k]+=c[n]
    if aa[1]!=1 or any(aa[k] for k in range(2,N+1)):
        raise RuntimeError('local divisor cancellation')
    A=F(-1);B=I.rat(0);core=I.rat(0);h_cross=I.rat(0);count=0
    # Error e(t)=exp(-t/2)[A log x+B] on x in [k,k+1].
    for k in range(1,Y):
        A+=aa[k];B-=aa[k]*logs[k]
        if k<=N:
            if A!=0 or not B.lo<=0<=B.hi:raise RuntimeError('local reproduction')
            continue
        def end(idx):
            w=A*logs[idx]+B
            return (w.square()+2*A*w+2*A*A)/idx
        v=end(k)-end(k+1)
        # Integral is nonnegative; intersect with this independent fact.
        if v.hi<0:raise RuntimeError('negative norm-cell upper bound')
        core+=I(max(0,v.lo),v.hi);count+=1
    if count!=Y-N-1:raise RuntimeError('cell coverage')
    C=sum(c,F(0));L=sum((c[n]*logs[n] for n in range(1,N+2)),I.rat(0))
    W=sum((abs(c[n])*n for n in range(1,N+2)),F(0))
    alpha=-1-C/2;beta=(L-C*LOG2PI)/2
    Z=alpha*logs[Y]+beta
    main=(Z.square()+2*alpha*Z+2*alpha*alpha)/Y
    if main.hi<0:raise RuntimeError('negative main norm')
    main=I(max(0,main.lo),main.hi)
    remainder=I.rat(W*W/F(108*Y**3))
    sm=main.sqrt();se=remainder.sqrt()
    low=max(0,sm.lo-se.hi)
    tail=I((low*low)//Q,(sm+se).square().hi)
    error=core+tail
    rel=error/2  # ||t exp(-t/2)||^2=2 exactly.
    invnorm=sum((sum((F(mu[j],j) for j in range(1,k+1)),F(0))**2
                 for k in range(1,N+1)),F(0))
    bound={1:F(1,6),2:F(1,35),4:F(1,500),8:F(1,2500),
           16:F(1,11000),32:F(1,8000),64:F(1,19000),128:F(1,14000)}[N]
    if not rel.hi<I.rat(bound).lo:raise RuntimeError(f'coarse bound failed N={N}')
    return {'N':N,'cutoff_X':N+1,'b':'1/2','target':'t*exp(-t/2)',
            'complete_integrated_cells':count,'exact_zero_cells':N,
            'complete_infinite_tail':True,'error_squared':error.record(),
            'normalized_error_squared':rel.record(),
            'core_error_squared':core.record(),'tail_error_squared':tail.record(),
            'main_tail_squared':main.record(),'tail_remainder_squared_upper':str(remainder.hi),
            'source_input_norm_squared':str(invnorm),'balanced_coefficient':str(c[-1]),
            'C':str(C),'W':str(W),'normalized_coarse_bound':str(bound)}

def run():
    logs=[None]+[log_fraction(n) for n in range(1,Y+1)]
    rows=[one(N,logs) for N in ORDERS]
    by={r['N']:r for r in rows}
    # These are strict certified nonmonotonicities of THIS candidate sequence.
    for n,m in [(16,32),(64,128)]:
        if int(by[n]['normalized_error_squared']['hi'])>=int(by[m]['normalized_error_squared']['lo']):
            raise RuntimeError('nonmonotonicity check')
    return {'schema':'CD26.compact-inverse-eight-cutoffs.v1','arithmetic':'DIRECTED_INTERVAL',
            'precision_bits':BITS,'atanh_terms':TERMS,'tail_start_Y':Y,
            'pi':PI.record(),'log_2pi':LOG2PI.record(),'orders':list(ORDERS),'rows':rows,
            'strict_error_increases':[[16,32],[64,128]],
            'RH_proved':False,'domain_completed':False,'finite_to_infinite_extrapolation':False,
            'special_function_oracle_used':False,
            'scope':'Actual finite candidates; every real cell and infinite tail. No all-N norm bound.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path)
    p.add_argument('--compare',type=Path);a=p.parse_args()
    r=run();text=json.dumps(r,sort_keys=True,indent=2)+'\n'
    if a.compare and a.compare.read_text()!=text:raise ValueError('retained certificate mismatch')
    if a.output:a.output.write_text(text)
    else:print(text,end='')
if __name__=='__main__':main()
