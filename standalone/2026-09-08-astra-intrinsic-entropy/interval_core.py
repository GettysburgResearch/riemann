"""Exact Gaussian-rational kernel algebra and outward integer interval arithmetic.
No numerical zeros, floating point, numpy, sympy, or external source code is used.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt


def rat(x):
    if type(x) is int:
        return F(x)
    if type(x) is F:
        return x
    raise TypeError('exact int/Fraction required')


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 're', rat(self.re))
        object.__setattr__(self, 'im', rat(self.im))

    @staticmethod
    def of(x):
        return x if type(x) is C else C(rat(x))

    def __add__(self, b):
        b = C.of(b)
        return C(self.re+b.re, self.im+b.im)
    __radd__ = __add__

    def __neg__(self): return C(-self.re, -self.im)
    def __sub__(self,b): return self+-C.of(b)
    def __rsub__(self,b): return C.of(b)+-self

    def __mul__(self,b):
        b=C.of(b)
        return C(self.re*b.re-self.im*b.im, self.re*b.im+self.im*b.re)
    __rmul__=__mul__

    def conj(self): return C(self.re, -self.im)
    def abs2(self): return self.re*self.re+self.im*self.im

    def __truediv__(self,b):
        b=C.of(b)
        d=b.abs2()
        if not d: raise ZeroDivisionError('zero Gaussian rational')
        z=self*b.conj()
        return C(z.re/d,z.im/d)
    def __rtruediv__(self,b): return C.of(b)/self

    def __pow__(self,n):
        if type(n) is not int: raise TypeError('integer power required')
        if n<0: return (1/self)**(-n)
        out=C(1);x=self
        while n:
            if n&1: out=out*x
            n//=2;x=x*x
        return out

    def record(self): return [str(self.re),str(self.im)]


Z=C(0); ONE=C(1)

def matrix(r,c): return [[Z for _ in range(c)] for _ in range(r)]
def eye(n): return [[ONE if i==j else Z for j in range(n)] for i in range(n)]
def star(M): return [[M[i][j].conj() for i in range(len(M))] for j in range(len(M[0]))]
def mm(A,B):
    if not A or not B or len(A[0])!=len(B): raise ValueError('matrix dimensions')
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z)
             for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x): return [sum((a*b for a,b in zip(row,x)),Z) for row in A]
def madd(A,B): return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def msub(A,B): return [[a-b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def dot(x,y): return sum((a.conj()*b for a,b in zip(x,y)),Z)
def quad(x,A): return dot(x,mv(A,x))

def inverse(M):
    n=len(M)
    if not n or any(len(r)!=n for r in M): raise ValueError('nonempty square matrix required')
    A=[list(row)+eye(n)[i] for i,row in enumerate(M)]
    for k in range(n):
        p=next((i for i in range(k,n) if A[i][k]!=Z),None)
        if p is None: raise ValueError('singular matrix')
        A[k],A[p]=A[p],A[k]
        q=A[k][k];A[k]=[v/q for v in A[k]]
        for i in range(n):
            if i!=k:
                v=A[i][k]
                A[i]=[a-v*b for a,b in zip(A[i],A[k])]
    return [row[n:] for row in A]


def ldl_pivots(G):
    if G!=star(G): raise ValueError('not Hermitian')
    n=len(G);L=eye(n);p=[]
    for j in range(n):
        q=G[j][j]-sum((L[j][k]*p[k]*L[j][k].conj() for k in range(j)),Z)
        if q.im or q.re<=0: raise ValueError('not positive definite')
        p.append(q)
        for i in range(j+1,n):
            L[i][j]=(G[i][j]-sum((L[i][k]*p[k]*L[j][k].conj() for k in range(j)),Z))/q
    return [v.re for v in p]


def kernels(nodes):
    """nodes is a list of DISTINCT (C(lambda), multiplicity) pairs, Re lambda>0."""
    if type(nodes) is not list or not nodes: raise ValueError('nonempty nodes')
    seen=set();ix=[]
    for z,m in nodes:
        if type(z) is not C or z.re<=0: raise ValueError('strict right-half-plane node required')
        if type(m) is not int or not 1<=m<=4: raise ValueError('multiplicity 1..4 required')
        if z in seen: raise ValueError('combine equal nodes using multiplicity')
        seen.add(z)
        ix.extend((z,r) for r in range(m))
    if len(ix)>8: raise ValueError('bounded fixture dimension')
    G=[[C(comb(r+s,r))/(z+w.conj())**(r+s+1) for w,s in ix] for z,r in ix]
    A=matrix(len(ix),len(ix));b=[]
    for i,(z,r) in enumerate(ix):
        A[i][i]=z
        if r: A[i][i-1]=C(-1)
        b.append(ONE if r==0 else Z)
    return ix,G,A,b


def target_data(ix,a,p):
    a=rat(a)
    if a<=0 or type(p) is not int or not 0<=p<=3: raise ValueError('target parameters')
    return [-C(comb(p+r,r))/(z+a)**(p+r+1) for z,r in ix]


def energy_series(A,Ginv,d0,degree):
    ds=[d0]
    for n in range(1,degree+1): ds.append([x/n for x in mv(A,ds[-1])])
    es=[sum((dot(ds[j],mv(Ginv,ds[n-j])) for j in range(n+1)),Z)
        for n in range(degree+1)]
    return ds,es

# Outward dyadic intervals. All endpoints are integers divided by SCALE.
BITS=160
SCALE=1<<BITS
LOG_TERMS=64

def ceildiv(a,b):
    if b==0: raise ZeroDivisionError('zero denominator')
    return -((-a)//b)

@dataclass(frozen=True)
class I:
    lo:int
    hi:int
    def __post_init__(self):
        if type(self.lo) is not int or type(self.hi) is not int: raise TypeError('integer endpoints')
        if self.lo>self.hi: raise ValueError('reversed interval')
    @classmethod
    def of(cls,x):
        if type(x) is cls: return x
        q=rat(x)
        return cls(q.numerator*SCALE//q.denominator,ceildiv(q.numerator*SCALE,q.denominator))
    @classmethod
    def bounds(cls,a,b):
        a,b=rat(a),rat(b)
        if a>b: raise ValueError('reversed bounds')
        return cls(cls.of(a).lo,cls.of(b).hi)
    def __add__(self,b):
        b=I.of(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I.of(b)
    def __rsub__(self,b):return I.of(b)+-self
    def __mul__(self,b):
        b=I.of(b);v=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(v)//SCALE,ceildiv(max(v),SCALE))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.of(b)
        if b.lo<=0<=b.hi: raise ZeroDivisionError('interval includes zero')
        v=[(x*SCALE,y) for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(x//y for x,y in v),max(ceildiv(x,y) for x,y in v))
    def __rtruediv__(self,b):return I.of(b)/self
    def square(self):
        if self.lo<=0<=self.hi: return I(0,ceildiv(max(self.lo**2,self.hi**2),SCALE))
        return self*self
    def contains(self,x):
        q=rat(x);return self.lo*q.denominator<=q.numerator*SCALE<=self.hi*q.denominator
    def overlaps(self,b):return max(self.lo,b.lo)<=min(self.hi,b.hi)
    def decimal(self,d=12):
        if type(d) is not int or not 0<=d<=30:raise ValueError('decimal digits')
        q=10**d
        def render(n):
            s='-' if n<0 else '';n=abs(n)
            return s+str(n//q)+'.'+str(n%q).zfill(d)
        return [render(self.lo*q//SCALE),render(ceildiv(self.hi*q,SCALE))]
    def record(self):return {'bits':BITS,'lo':str(self.lo),'hi':str(self.hi),'decimal':self.decimal()}

@lru_cache(None)
def _log_series(z):
    z=rat(z)
    if not 0<=z<=F(1,3):raise ValueError('range reduction required')
    t=I.of(z);power=t;s=I.of(0);t2=t*t
    for j in range(LOG_TERMS):
        s+=power/F(2*j+1);power*=t2
    rem=2*z**(2*LOG_TERMS+1)/((2*LOG_TERMS+1)*(1-z*z))
    return 2*s+I.bounds(0,rem)

@lru_cache(None,typed=True)
def logq(x):
    x=rat(x)
    if x<=0:raise ValueError('positive logarithm input')
    k=0;y=x
    while y>=2:y/=2;k+=1
    while y<1:y*=2;k-=1
    return _log_series((y-1)/(y+1))+k*_log_series(F(1,3))


def sqrt2():
    n=isqrt(2*SCALE*SCALE)
    return I(n,n+1)


def log_square_integral(a,b,x,y):
    """Integral_x^y (a log u+b)^2 du/u^2, outward even when a,b are intervals."""
    if not 0<x<y:raise ValueError('positive ordered endpoints')
    a,b=I.of(a),I.of(b)
    def primitive(u):
        z=a*logq(u)+b
        return -(z.square()+2*a*z+2*a.square())/u
    return primitive(y)-primitive(x)


def arithmetic_tail_certificate(X=512):
    if type(X) is not int or X!=512:raise ValueError('the certified fixture is X=512')
    logs=[I.of(0)]+[logq(F(j)) for j in range(1,2*X+1)]
    lf=[I.of(0)]
    for j in range(1,len(logs)):lf.append(lf[-1]+logs[j])
    old=new=I.of(0);cells=0;root2=sqrt2();l2=logq(F(2))
    # u>=0; x=e^u. q0(u)=2^-1/2 e^-u/2 [S(2x)-2S(x)-log(2x)].
    for n in range(1,X):
        ga=I.of(-n);gb=n+lf[n]
        for m,x,y in ((2*n,F(n),F(2*n+1,2)),(2*n+1,F(2*n+1,2),F(n+1))):
            ea=I.of(m-2*n-1);eb=(m-1)*l2-lf[m]+2*lf[n]
            old+=log_square_integral(ea,eb,x,y)/2
            na=ea/root2+ga/2;nb=eb/root2+gb/2
            new+=log_square_integral(na,nb,x,y)
            cells+=1
    lx=logq(F(X));u=lx+6
    tail=(u.square()+2*u+2)/(64*X)
    upper=I(new.lo,new.hi+tail.hi)
    if old.lo<=I.of(F(3,10)).hi: raise ValueError('seed lower certificate failed')
    if upper.hi>=I.of(F(7,125)).lo: raise ValueError('corrected upper certificate failed')
    if old.lo<=5*upper.hi: raise ValueError('fivefold improvement not certified')
    return {'cutoff_x':X,'integrated_half_cells':cells,
            'seed_error_partial':old.record(),'corrected_error_partial':new.record(),
            'corrected_infinite_tail_upper':tail.record(),
            'corrected_full_error_enclosure':upper.record(),
            'seed_error_lower_claim':'3/10','corrected_error_upper_claim':'7/125',
            'squared_error_improvement_factor_greater_than':5,
            'correction_coefficient':'1/2','horizon':'log(2)',
            'target':'t exp(-t/2)','arithmetic':'outward-dyadic-160-bit; exact cell integrals; analytic infinite tail'}
