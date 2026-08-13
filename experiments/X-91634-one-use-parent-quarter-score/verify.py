from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from math import isqrt
import json,time
from pathlib import Path

DIG=24
S=10**DIG
NTERMS=24
K=4; BASE=4**K; LEFT=1; RIGHT=67; MAXN=4**K*RIGHT

def ceildiv(a:int,b:int)->int: return -((-a)//b)
@dataclass(frozen=True)
class I:
    lo:int; hi:int
    def __add__(self,o): o=iv(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-iv(o))
    def __rsub__(self,o): return iv(o)-self
    def __mul__(self,o):
        o=iv(o); ps=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(ps)//S,ceildiv(max(ps),S))
    __rmul__=__mul__
    def rat(self,n:int,d:int=1):
        ps=(self.lo*n,self.hi*n)
        return I(min(ps)//d,ceildiv(max(ps),d))
    def recip(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError
        if self.lo>0: return I((S*S)//self.hi,ceildiv(S*S,self.lo))
        raise NotImplementedError
    def __truediv__(self,o): return self*iv(o).recip()

def iv(x):
    if isinstance(x,I): return x
    if isinstance(x,Fraction): return rat_iv(x)
    return I(int(x)*S,int(x)*S)

def rat_iv(x:Fraction)->I:
    x=Fraction(x); a=x.numerator*S; b=x.denominator
    return I(a//b,ceildiv(a,b))

def sqrt_q(x:Fraction)->I:
    x=Fraction(x); v=(x.numerator*S*S)//x.denominator; r=isqrt(v)
    return I(r,r+1)

@lru_cache(None)
def log2()->I: return log_reduced(Fraction(2))

def log_reduced(x:Fraction)->I:
    z=Fraction(x-1,x+1)
    zi=rat_iv(z); z2=zi*zi; p=zi; partial=I(0,0)
    for j in range(NTERMS):
        partial += p.rat(1,2*j+1); p=p*z2
    one_minus=I(S,S)-z2
    tail=p.rat(2,2*NTERMS+1)/one_minus
    return partial.rat(2)+I(0,tail.hi)

@lru_cache(None)
def log_q(x:Fraction)->I:
    x=Fraction(x)
    if x<=0: raise ValueError
    e=0; y=x
    while y>=2: y/=2; e+=1
    while y<1: y*=2; e-=1
    base=I(0,0) if y==1 else log_reduced(y)
    if e==0:return base
    return base+log2().rat(e)

@lru_cache(None)
def invsqrt(n:int)->I: return sqrt_q(Fraction(n)).recip()

def sieves(limit):
    mu=[0]*(limit+1); spf=[0]*(limit+1); ps=[]; mu[1]=1
    for n in range(2,limit+1):
        if spf[n]==0: spf[n]=n; ps.append(n); mu[n]=-1
        for p in ps:
            if p>spf[n] or p*n>limit:break
            spf[p*n]=p
            if n%p==0:mu[p*n]=0;break
            mu[p*n]=-mu[n]
    return mu,spf

def pp(n,spf):
    if n<2:return None
    p=spf[n];m=n;e=0
    while m%p==0:m//=p;e+=1
    return (p,e) if m==1 else None

def prefixes():
    mu,spf=sieves(MAXN)
    A=[Fraction(0)]*(MAXN+1);B=[I(0,0)]*(MAXN+1);C=[I(0,0)]*(MAXN+1);D=[I(0,0)]*(MAXN+1)
    a=Fraction(0);b=I(0,0);c=I(0,0);d=I(0,0)
    for n in range(1,MAXN+1):
        if mu[n]: a+=Fraction(mu[n],n); b += invsqrt(n).rat(mu[n])
        z=pp(n,spf)
        if z:
            p,e=z; lp=log_q(Fraction(p)); ls=lp*invsqrt(n); c+=ls; d+= (lp*lp*invsqrt(n)).rat(e)
        A[n]=a;B[n]=b;C[n]=c;D[n]=d
    return A,B,C,D

t0=time.time();A,B,C,D=prefixes(); LOG4=log2().rat(2); print('prefix seconds',time.time()-t0)
@lru_cache(None)
def coeff(ns):
    # L_one(x) = sum_{j=0}^4 2^{j-4} Sigma(4^j x) - P(4^4 x).
    al=I(0,0); ga=I(0,0)
    for j,n in enumerate(ns):
        if 2*j >= K: al += rat_iv(5*A[n]).rat(2**(2*j-K))
        else: al += rat_iv(5*A[n]).rat(1,2**(K-2*j))
        if j >= K: w_num,w_den=2**(j-K),1
        else: w_num,w_den=1,2**(K-j)
        ga -= B[n].rat(3*w_num,w_den)
    n4=ns[K]
    be=-C[n4]
    ga -= (C[n4]*LOG4).rat(K)
    ga += D[n4]
    return al,be,ga

def ns_open(k): return tuple((4**j*(2*k+1))//(2*BASE) for j in range(K+1))
def ns_point(k): return tuple((4**j*k)//BASE for j in range(K+1))
def value(x,ns):
    al,be,ga=coeff(ns); return al*sqrt_q(x)+be*log_q(x)+ga

maxhi=None;where=None;checks=0;betapos=0
for k in range(BASE*LEFT,BASE*RIGHT):
    ns=ns_open(k); al,be,ga=coeff(ns)
    if be.hi>=0: betapos+=1
    for side in (k,k+1):
        x=Fraction(side,BASE); z=al*sqrt_q(x)+be*log_q(x)+ga
        if z.hi>=0: raise AssertionError(('open',k,side,ns,z.lo/S,z.hi/S))
        if maxhi is None or z.hi>maxhi: maxhi=z.hi;where=('open',k,side,str(x),ns,z.lo/S,z.hi/S)
        checks+=1
for k in range(BASE*LEFT,BASE*RIGHT+1):
    x=Fraction(k,BASE);ns=ns_point(k);z=value(x,ns)
    if z.hi>=0: raise AssertionError(('point',k,ns,z.lo/S,z.hi/S))
    if maxhi is None or z.hi>maxhi: maxhi=z.hi;where=('point',k,str(x),ns,z.lo/S,z.hi/S)
    checks+=1
result={'classification':'PASS_ONE_USE_PARENT_QUARTER_SCORE_K4_ENDPOINT_CERTIFICATE','digits':DIG,'atanh_terms':NTERMS,'checks':checks,'common_cells':BASE*(RIGHT-LEFT),'beta_nonnegative_cells':betapos,'maximum_upper_scaled_integer':str(maxhi),'scale_integer':str(S),'maximum_upper_decimal':f'{maxhi/S:.18f}','maximum_location':where,'scope':'Exact integer/fixed-point interval arithmetic. Square roots use integer isqrt enclosures; logarithms use atanh partial sums with a positive rigorous tail. On each common cell beta=-C(floor(256x))<0, so the only critical point is a minimum and both one-sided endpoints suffice. Activated knot values are checked separately. Certifies the corrected one-use parent score scalar; physical one-use row assembly is supplied separately by L-91621 and the exact parent equality-row score identity.'}
Path(__file__).resolve().parent.joinpath('results','verification.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['classification']); print(json.dumps(result,indent=2,sort_keys=True)); print('runtime_seconds',time.time()-t0)
