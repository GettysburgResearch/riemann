#!/usr/bin/env python3
"""Bounded algebra and one directed finite-source check; NOT an RH verifier."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import sys
import sympy as sp

BITS = 128
SCALE = 1 << BITS

class CheckError(ValueError):
    pass

def require(test: bool, label: str) -> None:
    if not test:
        raise CheckError(label)

def ceildiv(a: int, b: int) -> int:
    return -((-a)//b)

@dataclass(frozen=True)
class IV:
    lo: int
    hi: int
    def __post_init__(self) -> None:
        require(self.lo <= self.hi, 'reversed interval')
    @staticmethod
    def rational(q: Q | int) -> 'IV':
        q = Q(q)
        return IV(q.numerator*SCALE//q.denominator,
                  ceildiv(q.numerator*SCALE, q.denominator))
    def __add__(self, other: 'IV | Q | int') -> 'IV':
        o = other if isinstance(other, IV) else IV.rational(other)
        return IV(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __neg__(self) -> 'IV':
        return IV(-self.hi, -self.lo)
    def __sub__(self, other: 'IV | Q | int') -> 'IV':
        return self + -(other if isinstance(other,IV) else IV.rational(other))
    def __mul__(self, other: 'IV | Q | int') -> 'IV':
        o = other if isinstance(other, IV) else IV.rational(other)
        v = [self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return IV(min(v)//SCALE,ceildiv(max(v),SCALE))
    __rmul__ = __mul__
    def divint(self, n: int) -> 'IV':
        require(n > 0, 'nonpositive interval divisor')
        return IV(self.lo//n,ceildiv(self.hi,n))
    def power(self, n: int) -> 'IV':
        require(n >= 0, 'negative exponent')
        v=IV.rational(1)
        for _ in range(n):v=v*self
        return v
    def obj(self) -> dict[str,str|int]:
        return {'lower_numerator':str(self.lo),'upper_numerator':str(self.hi),
                'denominator':str(SCALE),'precision_bits':BITS}


def log_unit(x: Q) -> IV:
    require(Q(1)<=x<=Q(2),'log input out of range')
    z=(x-1)/(x+1)
    total=Q(0)
    for j in range(80):total += 2*z**(2*j+1)/Q(2*j+1)
    rem=2*z**161/(161*(1-z*z))
    return IV(total.numerator*SCALE//total.denominator,
              ceildiv((total+rem).numerator*SCALE,(total+rem).denominator))

def log_int(n: int) -> IV:
    require(n>=1,'nonpositive log input')
    k=n.bit_length()-1
    return k*log_unit(Q(2)) + log_unit(Q(n,1<<k))

def sqrt_int(n: int) -> IV:
    k=math.isqrt(n*SCALE*SCALE)
    return IV(k,k if k*k==n*SCALE*SCALE else k+1)

def mu_sieve(n: int) -> list[int]:
    mu=[1]*(n+1); mu[0]=0
    prime=[True]*(n+1)
    for p in range(2,n+1):
        if prime[p]:
            for m in range(p,n+1,p):
                prime[m]=False;mu[m]*=-1
            for m in range(p*p,n+1,p*p):mu[m]=0
    return mu

def polyval(p: list[IV], x: IV) -> IV:
    v=IV.rational(0)
    for c in reversed(p):v=v*x+c
    return v

def polysquare(p: list[IV]) -> list[IV]:
    r=[IV.rational(0) for _ in range(2*len(p)-1)]
    for j,a in enumerate(p):
        for k,b in enumerate(p):r[j+k]=r[j+k]+a*b
    return r

def primitive_poly(p: list[IV]) -> list[IV]:
    # integral_a^b e^(-2t) p(t) dt = e^(-2a) A(a)-e^(-2b) A(b)
    r=[]
    for j in range(len(p)):
        r.append(sum((p[k]*Q(math.factorial(k),math.factorial(j)*2**(k-j+1))
                      for k in range(j,len(p))),IV.rational(0)))
    return r

def directed_head() -> dict[str,object]:
    endpoint=64  # Fixed complete experiment, not a caller-selected coverage claim.
    mu=mu_sieve(endpoint)
    lp=[log_int(n) for n in range(1,endpoint+1)]
    raw=[Q(1),Q(-5,2),Q(7,8),Q(-1,16)]
    coeff=[IV.rational(0) for _ in raw]
    total=IV.rational(0)
    for n in range(1,endpoint):
        sn=mu[n]*sqrt_int(n)
        ln=lp[n-1]
        for j in range(4):
            shifted=sum((raw[k]*math.comb(k,j)*(-ln).power(k-j)
                         for k in range(j,4)),IV.rational(0))
            coeff[j]=coeff[j]+sn*shifted
        prim=primitive_poly(polysquare(coeff))
        cell=polyval(prim,lp[n-1]).divint(n*n)-polyval(prim,lp[n]).divint((n+1)**2)
        require(cell.lo>0,f'cell {n} failed strict positivity')
        total=total+cell
    # h(log 2) = P(log2)/2 - 1/sqrt2; sqrt2/2 is exact reciprocal.
    l2=log_int(2)
    p2=sum((raw[k]*l2.power(k) for k in range(4)),IV.rational(0))
    h2=p2.divint(2)-sqrt_int(2).divint(2)
    require(h2.hi < IV.rational(Q(-4,5)).lo,'actual inverse sign')
    require(total.lo > SCALE//2,'head norm below half')
    require(total.hi < IV.rational(Q(13,25)).lo,'head norm exceeds 13/25')
    require(total.hi-total.lo < (1<<40),'head enclosure too wide')
    return {'arithmetic':'DIRECTED_INTEGER_INTERVAL',
            'endpoint_integer':endpoint,'time_endpoint':'log(64)',
            'complete_cells':endpoint-1,'H_log64':total.obj(),
            'h_log2':h2.obj(),'source_sign_certificate':'h(log 2)<-4/5',
            'interpretation':'H is the complete truncated inverse norm, not the full y norm; no growth extrapolation'}


def run() -> dict[str,object]:
    z,t,v,L=sp.symbols('z t v L',real=True)
    P=1-sp.Rational(5,2)*t+sp.Rational(7,8)*t**2-t**3/16
    Qp=t-sp.Rational(3,2)*t**2+sp.Rational(3,8)*t**3
    def lap(poly:sp.Expr)->sp.Expr:
        po=sp.Poly(poly,t)
        return sum(c*sp.factorial(k[0])/(z+1)**(k[0]+1) for k,c in po.terms())
    Phi=(z-sp.Rational(1,2))*(z+sp.Rational(1,2))**2/(z+1)**4
    F=(z-sp.Rational(1,2))**2/(z+1)**4
    require(sp.cancel(lap(P)-Phi)==0,'phi transform')
    require(sp.cancel(lap(Qp)-F)==0,'target transform')
    require(sp.cancel((z-sp.Rational(1,2))/(z+sp.Rational(1,2))**2*Phi-F)==0,
            'local base convolution')
    def moment(poly:sp.Expr,k:int=0,rate:sp.Rational=sp.Rational(2))->sp.Expr:
        po=sp.Poly(sp.expand(poly*t**k),t)
        return sp.factor(sum(c*sp.factorial(j[0])/rate**(j[0]+1) for j,c in po.terms()))
    require(moment(P**2)==sp.Rational(385,2048),'phi norm')
    require(moment(Qp**2)==sp.Rational(29,512),'f norm')
    require(Phi.subs(z,sp.Rational(1,2))==0,'positive half moment')
    require(Phi.subs(z,sp.Rational(-1,2))==0,'negative half moment')
    require(sp.diff(Phi,z).subs(z,sp.Rational(-1,2))==0,'first negative half moment')
    corr=moment(P*P.subs(t,t+v))
    require(sp.expand(corr-(385-639*v+162*v*v-9*v**3)/2048)==0,'whole correlation')
    for k in range(10):
        tail=sp.exp(-2*L)*sum(sp.factorial(k)*L**j/(sp.factorial(j)*2**(k-j+1)) for j in range(k+1))
        require(sp.simplify(sp.diff(tail,L)+L**k*sp.exp(-2*L))==0,'tail derivative')
    mu=mu_sieve(512)
    for n in range(1,513):
        require(sum(mu[d] for d in range(1,n+1) if n%d==0)==int(n==1),'complete Mobius row')
    jet_cases=0
    for d in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1),sp.Rational(3,2)]:
        for m in range(1,7):
            C=sp.Matrix(m,m,lambda i,j:sp.factorial(i+j)/(2*d)**(i+j+1))
            det=sp.prod(sp.factorial(j)**2 for j in range(m))/(2*d)**(m*m)
            require(C.det()==det,'jet determinant')
            require(C.inv()[m-1,m-1]==(2*d)**(2*m-1)/sp.factorial(m-1)**2,'jet leading cost')
            jet_cases+=1
    for N in range(101):
        ell=Q(1,640*(N+1))
        exact=ell**(2*N+1)*math.factorial(N)**2/(2048*16**N)
        floor=Q(1,2**(28*N+21)*(N+1))
        require(exact>floor,'finite Gram floor calibration')
    for n in range(1,101):
        require(Q(786*n**3,2**(36*n+6))<1,'cutoff inverse threshold')
    head=directed_head()
    return {'schema':'riemann.DCP26.bounded-checks.v1','status':'PASS_BOUNDED_CHECKS_NOT_RH',
            'named_checks':10,
            'details':{
                'rational_transform_identities':3,'norms_and_null_moments':5,
                'complete_correlation_identity':1,'tail_antiderivative_identities':10,
                'Mobius_coefficient_rows':512,'Cauchy_jet_cases':jet_cases,
                'exact_Gram_floor_calibrations':101,'cutoff_threshold_calibrations':100,
                'directed_source':head,
                'proof_boundary':'No all-rank domain limit, infinite signed correlation bound, critical source-map contraction, or RH is certified.'}}


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--check',type=Path)
    args=ap.parse_args()
    try:
        data=run()
        if args.check:
            require(json.loads(args.check.read_text())==data,'retained record mismatch')
        text=json.dumps(data,sort_keys=True,indent=2)+'\n'
        if args.output:args.output.write_text(text)
        else:print(text,end='')
        return 0
    except (ValueError,OSError,TypeError,json.JSONDecodeError) as exc:
        print(json.dumps({'status':'REJECTED','reason':str(exc)}),file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(main())
