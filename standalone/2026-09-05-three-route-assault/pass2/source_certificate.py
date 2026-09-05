"""Exact rational interval certificate for the actual invariant-xi first three moments.
No zero data, floating point, special-function library, or assert acceptance gates.
Euler--Maclaurin remainder bounds are proved in R1_XI_MINIMAL_RANK.md.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial, isqrt
from functools import lru_cache
import json
from pathlib import Path

DEN = 10**40

def down(x):
    x=F(x); return F((x.numerator*DEN)//x.denominator,DEN)

def up(x):
    x=F(x); return -down(-x)

@dataclass(frozen=True)
class Ball:
    lo: F
    hi: F
    def __init__(self, lo, hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        if lo>hi: raise ValueError('reversed interval')
        object.__setattr__(self,'lo',down(lo))
        object.__setattr__(self,'hi',up(hi))
    @staticmethod
    def of(x): return x if isinstance(x,Ball) else Ball(x)
    def __add__(self,x):
        x=self.of(x); return Ball(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return Ball(-self.hi,-self.lo)
    def __sub__(self,x): return self+-self.of(x)
    def __rsub__(self,x): return self.of(x)+-self
    def __mul__(self,x):
        x=self.of(x); v=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return Ball(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.of(x)
        if x.lo<=0<=x.hi: raise ValueError('division by zero interval')
        return self*Ball(1/x.hi,1/x.lo)
    def __rtruediv__(self,x): return self.of(x)/self
    def __pow__(self,n):
        if type(n) is not int or n<0: raise ValueError('nonnegative integer power required')
        out=Ball(1)
        for _ in range(n): out=out*self
        return out
    def sqrt(self):
        if self.lo<0: raise ValueError('negative square root interval')
        a=isqrt((self.lo.numerator*DEN*DEN)//self.lo.denominator)
        b=isqrt((self.hi.numerator*DEN*DEN)//self.hi.denominator)+1
        return Ball(F(a,DEN),F(b,DEN))
    def widen(self,e):
        e=F(e)
        if e<0: raise ValueError('negative radius')
        return Ball(self.lo-e,self.hi+e)
    def decimal(self):
        def fmt(x):
            q=x*DEN
            if q.denominator!=1: raise ArithmeticError('unquantized endpoint')
            n=q.numerator; sign='-' if n<0 else ''; n=abs(n)
            return f'{sign}{n//DEN}.{n%DEN:040d}'
        return [fmt(self.lo),fmt(self.hi)]

@lru_cache(None)
def log_rational(x):
    x=F(x)
    if x<=0: raise ValueError('log domain')
    k=0
    while x<1: x*=2; k-=1
    while x>2: x/=2; k+=1
    def series(t):
        y=(t-1)/(t+1); M=40
        z=2*sum((y**(2*j+1)/F(2*j+1) for j in range(M)),F(0))
        e=2*y**(2*M+1)/(F(2*M+1)*(1-y*y))
        return Ball(z,z+e)
    return series(x)+k*series(F(2))

def log_ball(x):
    x=Ball.of(x)
    return Ball(log_rational(x.lo).lo,log_rational(x.hi).hi)

def atan_small(x):
    x=F(x)
    if not 0<x<1: raise ValueError('atan domain')
    M=40
    v=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(M)),F(0))
    nxt=(-1)**M*x**(2*M+1)/F(2*M+1)
    return Ball(min(v,v+nxt),max(v,v+nxt))

def harmonic(n,p=1): return sum((F(1,k**p) for k in range(1,n+1)),F(0))

def rising(s,n):
    v=1
    for j in range(n): v*=s+j
    return v

def constants():
    N=64; m=4; L=log_rational(F(N))
    bern=[F(1,6),F(-1,30),F(1,42),F(-1,30)]
    cs=[bern[k-1]/(2*k*N**(2*k)) for k in range(1,m+1)]
    gamma=Ball(harmonic(N-1))-L+F(1,2*N)+sum(cs,F(0))
    g1=sum((log_rational(F(n))/n for n in range(1,N)),Ball(0))-L**2/2+L/(2*N)
    g2=sum((log_rational(F(n))**2/n for n in range(1,N)),Ball(0))-L**3/3+L**2/(2*N)
    for k,ck in enumerate(cs,1):
        H=harmonic(2*k-1); H2=harmonic(2*k-1,2)
        g1=g1-ck*(H-L)
        g2=g2+ck*((H-L)**2-H2)
    r0=abs(bern[-1])/F(2*m*N**(2*m))
    A=harmonic(2*m)+L.hi
    r1=r0*(A+F(1,2*m))
    r2=r0*(A*A+harmonic(2*m,2)+A/m+F(1,2*m*m))
    gamma=gamma.widen(r0); g1=g1.widen(r1); g2=g2.widen(r2)
    pi=16*atan_small(F(1,5))-4*atan_small(F(1,239))
    z3=F(0)
    for n in range(1,N): z3+=F(1,n**3)
    z3+=F(1,2*N*N)+F(1,2*N**3)
    for k in range(1,m+1):
        z3+=bern[k-1]*rising(3,2*k-1)/F(factorial(2*k)*N**(2*k+2))
    rz3=abs(bern[-1])*rising(3,2*m)/F(factorial(2*m)*(2*m+2)*N**(2*m+2))
    return gamma,g1,g2,pi,Ball(z3).widen(rz3)

def certify():
    g,g1,g2,pi,z3=constants()
    C=1+g/2-log_ball(4*pi)/2
    L1=-1+pi**2/8-2*g1-g**2
    L2=2-F(7,4)*z3+3*g2+6*g*g1+2*g**3
    p=2*C-L1; t=6*C-3*L1+L2/2
    D=((31*p-C**2)/30).sqrt(); x31=(C-D)/31; y31=(C+30*D)/31
    gap31=t-(30*x31**3+y31**3)
    def vals(x):
        x=Ball(x); S=C-30*x; disc=2*(p-30*x*x)-S*S
        cubic=30*x**3-S**3/2+F(3,2)*S*(p-30*x*x)-t
        deriv=45*(31*32*x*x-62*C*x+C*C-p)
        return S,disc,S*S-disc,cubic,deriv
    va=vals(F(56,100000)); vb=vals(F(57,100000))
    checks={
      'positive_trace':C.lo>0,
      'positive_square_trace':p.lo>0,
      'rank_two_coefficients_at_least_15':(C*C-14*p).lo>0,
      'rank_two_coefficients_15_suffices':(15*p-C*C).lo>0,
      'positive_cubic_trace':t.lo>0,
      'no_rank_31_three_coefficient_completion':gap31.lo>0,
      'cubic_lower_endpoint_negative':va[3].hi<0,
      'cubic_upper_endpoint_positive':vb[3].lo>0,
      'positive_sum_on_interval':vb[0].lo>0,
      'discriminant_at_lower_positive':va[1].lo>0,
      'discriminant_at_upper_positive':vb[1].lo>0,
      'both_last_eigenvalues_positive':vb[2].lo>0,
      'cubic_strictly_increasing':vb[4].lo>0,
      'derivative_decreases_until_upper':(C/32-F(57,100000)).lo>0,
      'product_decreases_until_upper':(C/31-F(57,100000)).lo>0,
    }
    if not all(checks.values()): raise ArithmeticError(f'certificate failure: {checks}')
    return {
      'status':'PASS_ACTUAL_XI_MINIMAL_RANK_15_AND_32',
      'arithmetic':'RATIONAL_INTERVAL_WITH_ANALYTIC_REMAINDERS',
      'Euler_Maclaurin_N':64,'Euler_Maclaurin_m':4,'decimal_outward_places':40,
      'checks':checks,
      'intervals':{'C':C.decimal(),'p2':p.decimal(),'p3':t.decimal(),
        'rank31_gap':gap31.decimal(),'cubic_at_0.00056':va[3].decimal(),
        'cubic_at_0.00057':vb[3].decimal(),'gamma0':g.decimal(),
        'gamma1':g1.decimal(),'gamma2':g2.decimal(),'pi':pi.decimal(),'zeta3':z3.decimal()},
      'RH_proved':False,'higher_coefficient_completion_proved':False
    }

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args()
    out=certify();text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    path=Path(__file__).with_name('XI_SOURCE_CERTIFICATE.json')
    if args.write: path.write_text(text)
    elif path.read_text()!=text: raise SystemExit('stored source certificate mismatch')
    print(out['status']); print('checked',len(out['checks']),'strict inequalities')
