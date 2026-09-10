#!/usr/bin/env python3
"""Complete defining-theta-integral moment enclosure; standard library only.

This computes a fixed finite certificate. It is not an RH proof. All numerical
intervals use integer endpoints in units 2**-512. No zeta/zero oracle is used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import sys

BITS = 512
S = 1 << BITS
DEGREE = 96
CELLS = 96
THETA_TERMS = 8
MAX_MOMENT = 14


def require(test, why):
    if not test:
        raise ValueError(why)


def floor_div(a, b):
    return a // b


def ceil_div(a, b):
    return -((-a) // b)


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo = lo
        self.hi = lo if hi is None else hi
        require(type(self.lo) is int and type(self.hi) is int and lo <= self.hi,
                'invalid dyadic interval')

    @classmethod
    def q(cls, x):
        x = Q(x)
        return cls((x.numerator*S)//x.denominator,
                   ceil_div(x.numerator*S, x.denominator))

    def __add__(self, y):
        if not isinstance(y, I): y = I.q(y)
        return I(self.lo+y.lo, self.hi+y.hi)
    __radd__ = __add__

    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, y): return self + (-y if isinstance(y,I) else -Q(y))
    def __rsub__(self, y): return -self + y

    def __mul__(self, y):
        if type(y) is int:
            return I(self.lo*y,self.hi*y) if y>=0 else I(self.hi*y,self.lo*y)
        if not isinstance(y,I): y = I.q(y)
        a,b,c,d=self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi
        return I(min(a,b,c,d)//S,ceil_div(max(a,b,c,d),S))
    __rmul__ = __mul__

    def scale(self, q):
        q=Q(q)
        if q.numerator < 0: return -self.scale(-q)
        return I((self.lo*q.numerator)//q.denominator,
                 ceil_div(self.hi*q.numerator,q.denominator))

    def __truediv__(self,y):
        if not isinstance(y,I): return self.scale(1/Q(y))
        require(y.lo>0 or y.hi<0,'division interval contains zero')
        if y.hi<0: return (-self)/(-y)
        inv=I((S*S)//y.hi,ceil_div(S*S,y.lo))
        return self*inv

    def __pow__(self,n):
        require(type(n) is int and n>=0,'bad power')
        if n==0: return I(S)
        if n%2==0:
            if self.lo>=0: return I((self.lo**n)//(S**(n-1)),ceil_div(self.hi**n,S**(n-1)))
            if self.hi<=0: return (-self)**n
            return I(0,ceil_div(max(-self.lo,self.hi)**n,S**(n-1)))
        return I((self.lo**n)//(S**(n-1)),ceil_div(self.hi**n,S**(n-1)))

    def pair(self): return [str(self.lo),str(self.hi)]

    def decimals(self,digits=48):
        ten=10**digits
        def fmt(n):
            sign='-' if n<0 else ''
            n=abs(n)
            return sign+str(n//ten)+'.'+str(n%ten).zfill(digits)
        return [fmt((self.lo*ten)//S),fmt(ceil_div(self.hi*ten,S))]


def exp_point(q):
    """Enclose exp(q) for an exact rational q, by reduction and positive series."""
    q=Q(q)
    if q<0:
        r=exp_point(-q)
        return I((S*S)//r.hi,ceil_div(S*S,r.lo))
    k=0
    while q>Q(1,16): q/=2; k+=1
    term=I(S); value=I(S)
    for j in range(1,129):
        term=term.scale(q/j)
        value=value+term
    # For 0 <= q <= 1/16, omitted positive series <= 2 q^129/129!.
    rem=2*q**129/factorial(129)
    value=I(value.lo,value.hi+ceil_div(rem.numerator*S,rem.denominator))
    for _ in range(k): value=value*value
    return value


def exp_iv(x):
    a=exp_point(Q(x.lo,S)); b=exp_point(Q(x.hi,S))
    return I(a.lo,b.hi)


def pi_interval():
    def atan_inv(n):
        r=Q(0)
        for j in range(192): r+=Q((-1)**j,(2*j+1)*n**(2*j+1))
        # 192 terms, ending in a negative term: remainder is positive.
        err=Q(1,385*n**385)
        return I.q(r)+I(0,I.q(err).hi)
    return 16*atan_inv(5)-4*atan_inv(239)


def theta_moments():
    pi=pi_interval()
    require(3*S < pi.lo < pi.hi < 4*S,'pi bound failed')
    h=Q(1,64)
    e2=[I.q(Q(2**j,factorial(j))) for j in range(DEGREE+1)]
    weights={j:Q(2)*h**(j+1)/(j+1) for j in range(0,DEGREE+1,2)}
    total={k:I(0) for k in range(0,MAX_MOMENT+1,2)}
    active=skipped=0
    for cell in range(CELLS):
        center=Q(2*cell+1,64)
        e2c=exp_point(2*center)
        e25c=exp_point(Q(5,2)*center)
        left_e2=exp_point(2*(center-h))
        phi=[I(0) for _ in range(DEGREE+1)]
        for n in range(1,THETA_TERMS+1):
            a=pi*n*n*e2c
            left_a=pi*n*n*left_e2
            if left_a.lo >= 300*S:
                skipped+=1
                continue
            active+=1
            # f(v)=exp((5/2)v-a exp(2v)); k f_k=(5/2)f_{k-1}-2a(e^{2v}f)_{k-1}.
            f=[exp_iv(-a)]
            for k in range(1,DEGREE+2):
                conv=I(0)
                for j in range(k): conv=conv+e2[j]*f[k-1-j]
                f.append((f[k-1].scale(Q(5,2))-2*a*conv)/k)
            lead=pi*n*n*e25c
            for j in range(DEGREE+1):
                phi[j]=phi[j]+lead*(-f[j]-2*(j+1)*f[j+1])
        for power in total:
            poly=[Q(comb(power,l))*center**(power-l) for l in range(power+1)]
            ans=I(0)
            for j in range(DEGREE+1):
                weight=sum((poly[l]*weights[j+l] for l in range(power+1)
                            if j+l<=DEGREE and (j+l)%2==0),Q(0))
                if weight: ans=ans+phi[j].scale(weight)
            total[power]=total[power]+2*ans
    # NUMERICS.md proves that all omitted theta terms, t>3, skipped terms,
    # and ALL complex-Taylor remainders together have absolute error < 2^-190.
    error=1 << (BITS-190)
    for k in total:
        total[k]=I(total[k].lo-error,total[k].hi+error)
        require(total[k].lo>0,'raw moment positivity failed')
    normal={k:total[k]/total[0] for k in total}
    normal[0]=I(S)  # exact normalized zeroth moment
    cumulants={}
    for n in range(1,MAX_MOMENT+1):
        v=normal.get(n,I(0))
        for j in range(1,n):
            v=v-comb(n-1,j-1)*cumulants[j]*normal.get(n-j,I(0))
        cumulants[n]=v
    traces={m:((-1)**(m+1))*cumulants[2*m]/(2*factorial(2*m-1))
            for m in range(1,MAX_MOMENT//2+1)}
    # Full interval LDL, proving positive definiteness of the entire 4x4
    # matrix; this is NOT just checking its entries or unqualified minors.
    n=4
    H=[[traces[i+j+1] for j in range(n)] for i in range(n)]
    L=[[I(S if i==j else 0) for j in range(n)] for i in range(n)]
    piv=[]
    for j in range(n):
        p=H[j][j]-sum((L[j][k]**2*piv[k] for k in range(j)),I(0))
        require(p.lo>0,'Hankel pivot not strictly positive at '+str(j))
        piv.append(p)
        for i in range(j+1,n):
            L[i][j]=(H[i][j]-sum((L[i][k]*L[j][k]*piv[k] for k in range(j)),I(0)))/p
    det=[]; v=I(S)
    for p in piv: v=v*p; det.append(v)
    return {
      'schema':'THETA_TRACE_HANKEL_V1','status':'FINITE_SOURCE_CERTIFICATE_NOT_RH',
      'rh_proved':False,'zero_ordinates_used':False,'zeta_oracle_used':False,
      'arithmetic':{'unit':'2^-512','pi':'Machin; 192 alternating terms per atan',
         'exp':'positive Taylor through degree128 after reduction to [0,1/16]'},
      'coverage':{'theta_indices':THETA_TERMS,'time_cells':CELLS,'cell_width':'1/32',
         'time_interval':['0','3'],'taylor_degree':DEGREE,
         'maximum_moment':MAX_MOMENT,'computed_cell_summands':active,
         'analytically_enclosed_cell_summands':skipped,
         'complete_theta_and_time_tails':True,'absolute_analytic_error':'2^-190',
         'hankel_order':n},
      'raw_even_moments':{str(k):total[k].pair() for k in total},
      'moments':{str(k):normal[k].pair() for k in normal},
      'traces':{str(k):traces[k].pair() for k in traces},
      'ldl_pivots':[p.pair() for p in piv],
      'leading_determinants':[d.pair() for d in det],
      'display':{'normalization':total[0].decimals(),
         'traces':{str(k):traces[k].decimals(65) for k in traces},
         'ldl_pivots':[p.decimals(65) for p in piv],
         'leading_determinants':[d.decimals(80) for d in det]},
    }


def strict_json(data):
    def pairs(kv):
        d={}
        for k,v in kv:
            require(k not in d,'duplicate JSON key');d[k]=v
        return d
    def bad(x): raise ValueError('floating or nonfinite JSON numeric value')
    return json.loads(data,object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)


def typed_equal(a,b):
    if type(a) is not type(b):return False
    if type(a) is dict:return a.keys()==b.keys() and all(typed_equal(a[k],b[k]) for k in a)
    if type(a) is list:return len(a)==len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
    return a==b


def main():
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',type=Path);g.add_argument('--check',type=Path)
    args=p.parse_args()
    expected=None
    if args.check:
        expected=strict_json(args.check.read_text(encoding='utf-8'))
        required={'schema','status','rh_proved','zero_ordinates_used','zeta_oracle_used',
                  'arithmetic','coverage','raw_even_moments','moments','traces',
                  'ldl_pivots','leading_determinants','display'}
        require(type(expected) is dict and set(expected)==required,'receipt field set')
        require(expected['schema']=='THETA_TRACE_HANKEL_V1' and
                expected['status']=='FINITE_SOURCE_CERTIFICATE_NOT_RH','wrong schema/status')
        for key in ('rh_proved','zero_ordinates_used','zeta_oracle_used'):
            require(expected[key] is False,'false proof/input claim: '+key)
        cov=expected['coverage']
        require(type(cov) is dict,'bad coverage')
        fixed={'theta_indices':THETA_TERMS,'time_cells':CELLS,'taylor_degree':DEGREE,
               'maximum_moment':MAX_MOMENT,'hankel_order':4,
               'complete_theta_and_time_tails':True}
        for key,value in fixed.items():
            require(key in cov and typed_equal(cov[key],value),'wrong coverage: '+key)
    out=theta_moments()
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.emit:
        args.emit.write_text(text,encoding='utf-8')
        print('PRODUCED '+hashlib.sha256(text.encode()).hexdigest())
    else:
        require(typed_equal(expected,out),'receipt differs from full fresh reconstruction')
        print('PASS_FINITE_THETA_TRACE_HANKEL '+hashlib.sha256(text.encode()).hexdigest())

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,ArithmeticError) as e:
        print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
