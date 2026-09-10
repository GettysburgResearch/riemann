"""Finite rational source and outward-dyadic Green energy; no floats or zeta data."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, gcd

BITS=224
DEN=1<<BITS
TERMS=80
CAP=256

def exact(x):
    if type(x) is int: return F(x)
    if type(x) is F: return x
    raise TypeError('exact int or Fraction required')

def nat(x, low=1, high=CAP):
    if type(x) is not int or not low<=x<=high: raise ValueError('integer outside declared cap')
    return x

def ceildiv(a,b):
    if b==0: raise ZeroDivisionError('zero denominator')
    return -((-a)//b)

@dataclass(frozen=True)
class I:
    lo:int
    hi:int
    def __post_init__(self):
        if type(self.lo) is not int or type(self.hi) is not int: raise TypeError('integer endpoints required')
        if self.lo>self.hi: raise ValueError('reversed endpoints')
    @classmethod
    def of(cls,x):
        if type(x) is cls: return x
        q=exact(x);return cls(q.numerator*DEN//q.denominator,ceildiv(q.numerator*DEN,q.denominator))
    @classmethod
    def bounds(cls,a,b):
        a,b=exact(a),exact(b)
        if a>b:raise ValueError('reversed rational bounds')
        return cls(cls.of(a).lo,cls.of(b).hi)
    def __add__(self,b):
        b=I.of(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I.of(b)
    def __rsub__(self,b):return I.of(b)+-self
    def __mul__(self,b):
        b=I.of(b);c=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(c)//DEN,ceildiv(max(c),DEN))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.of(b)
        if b.lo<=0<=b.hi:raise ZeroDivisionError('interval contains zero')
        c=[(x*DEN,y) for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(x//y for x,y in c),max(ceildiv(x,y) for x,y in c))
    def __rtruediv__(self,b):return I.of(b)/self
    def square(self):
        if self.lo<=0<=self.hi:return I(0,ceildiv(max(self.lo**2,self.hi**2),DEN))
        return self*self
    def contains(self,x):
        q=exact(x);return self.lo*q.denominator<=q.numerator*DEN<=self.hi*q.denominator
    def overlaps(self,b):return max(self.lo,b.lo)<=min(self.hi,b.hi)
    def decimal(self,digits=12):
        nat(digits,0,40);scale=10**digits
        out=[]
        for v in (self.lo*scale//DEN,ceildiv(self.hi*scale,DEN)):
            sign='-' if v<0 else '';v=abs(v)
            out.append(sign+str(v//scale)+'.'+str(v%scale).zfill(digits))
        return out
    def record(self):return {'bits':BITS,'lo':str(self.lo),'hi':str(self.hi),'decimal':self.decimal()}

@lru_cache(None)
def pi():
    def atan(q):
        n=96;x=F(1,q)
        s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F())
        r=x**(2*n+1)/F(2*n+1)
        return I.bounds(s-r,s+r)
    return 16*atan(5)-4*atan(239)

def trig(q):
    q=exact(q)%2
    if q>1:q-=2
    return _trig_reduced(q)

@lru_cache(None,typed=True)
def _trig_reduced(q):
    x=pi()*q;y=x*x
    term=x;sn=term
    for j in range(1,TERMS):
        term=-term*y/F((2*j)*(2*j+1));sn+=term
    err=F(4**(2*TERMS+1),factorial(2*TERMS+1))
    sn+=I.bounds(-err,err)
    term=I.of(1);cs=term
    for j in range(1,TERMS):
        term=-term*y/F((2*j-1)*(2*j));cs+=term
    err=F(4**(2*TERMS),factorial(2*TERMS))
    cs+=I.bounds(-err,err)
    return sn,cs

@lru_cache(None,typed=True)
def logq(q):
    q=exact(q)
    if q<=0:raise ValueError('positive log input required')
    y=q;e=0
    while y>=2:y/=2;e+=1
    while y<1:y*=2;e-=1
    def series(z):
        t=I.of(z);power=t;out=I.of(0)
        for j in range(96):
            out+=power/F(2*j+1);power*=t*t
        rem=2*z**193/(193*(1-z*z))
        return 2*out+I.bounds(0,rem)
    return series((y-1)/(y+1))+e*series(F(1,3))

@lru_cache(None,typed=True)
def primes_of(n):
    nat(n);out=[];p=2
    while p*p<=n:
        if n%p==0:
            a=0
            while n%p==0:n//=p;a+=1
            out.append((p,a))
        p+=1
    if n>1:out.append((n,1))
    return tuple(out)

def mu(n):
    fs=primes_of(n)
    return 0 if any(a>1 for p,a in fs) else (-1)**len(fs)

def phi(n):
    nat(n);v=n
    for p,a in primes_of(n):v=v//p*(p-1)
    return v

def j2(n):
    nat(n);v=n*n
    for p,a in primes_of(n):v=v//(p*p)*(p*p-1)
    return v

@lru_cache(None,typed=True)
def balanced(M):
    nat(M,3);ks=range(1,M+1,2)
    S=sum((F(mu(d)**2,j2(d)) for d in ks),F())
    A=sum((F(mu(d)*phi(d),j2(d)) for d in ks),F())
    D=sum((F(phi(d)**2,j2(d)) for d in ks),F())
    K=S*D-A*A
    if K<=0:raise ValueError('nonpositive constrained determinant')
    v={k:k*k*sum((F(mu(d//k)*mu(d),j2(d)) for d in ks if d%k==0),F()) for k in ks}
    w={k:k*k*sum((F(mu(d//k)*phi(d),j2(d)) for d in ks if d%k==0),F()) for k in ks}
    lam={k:(D*v[k]-A*w[k])/K for k in ks}
    return lam,(S,A,D,K),v,w

def source(lam,n):
    if type(n) is not int:raise TypeError('integer cell required')
    return sum((a*(n//k-n//(2*k)) for k,a in lam.items()),F())

def validate_source(lam):
    if type(lam) is not dict or not lam:raise ValueError('nonempty coefficient dictionary required')
    for k,a in lam.items():
        nat(k)
        if k%2!=1:raise ValueError('odd source required')
        exact(a)
    if sum((a/F(k) for k,a in lam.items()),F())!=0:raise ValueError('balance required')

def frequencies(lam):
    validate_source(lam);M=max(lam)
    L={q:sum((a/F(k) for k,a in lam.items() if k%q==0),F()) for q in range(3,M+1,2)}
    rows=[]
    for q,l in L.items():
        for r in range(1,(q+1)//2):
            if gcd(r,q)==1:
                x=F(r,q);sn,cs=trig(x)
                if sn.lo<=0 or cs.lo<=0:raise ValueError('trigonometric positivity not enclosed')
                rows.append({'x':x,'q':q,'r':r,'L':l,'tan':sn/cs,
                             'charge':(-1)**(r+1)*l*cs/sn,'cos':cs})
    rows.sort(key=lambda z:z['x'])
    return rows

def energy(lam):
    rows=frequencies(lam);total=I.of(0);tails=[I.of(0)]*len(rows);tail=I.of(0)
    for i in range(len(rows)-1,-1,-1):
        tail+=rows[i]['charge'];tails[i]=tail
    prev=I.of(0);pieces=[]
    for row,tail in zip(rows,tails):
        width=row['tan']-prev
        if width.lo<=0:raise ValueError('unresolved sorted Green mesh')
        term=pi()/2*width*tail.square();total+=term
        pieces.append(term);prev=row['tan']
    return total,rows,tails,pieces

def partial_energy(rows,tails,tau):
    tau=I.of(tau);out=I.of(0);prev=I.of(0)
    if tau.lo<0:raise ValueError('nonnegative cutoff required')
    for row,tail in zip(rows,tails):
        end=row['tan']
        if tau.hi<=prev.lo:break
        if tau.lo>=end.hi:width=end-prev
        elif tau.hi<=end.lo and tau.lo>=prev.hi:width=tau-prev
        else:raise ValueError('cutoff interval straddles mesh; refine precision')
        out+=pi()/2*width*tail.square()
        if tau.hi<=end.lo:break
        prev=end
    return out

def sine_value(rows,j):
    return -sum((r['charge']/r['cos']*trig(2*j*r['x'])[0] for r in rows),I.of(0))
