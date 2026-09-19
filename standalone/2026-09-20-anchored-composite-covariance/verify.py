#!/usr/bin/env python3
"""Exact, bounded checks for ACC29. Standard library only; no proof by testing."""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, isqrt
import json

@lru_cache(None)
def factors(n):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            h=0
            while n%p==0: n//=p; h+=1
            out.append((p,h))
        p+=1
    if n>1: out.append((n,1))
    return tuple(out)

@lru_cache(None)
def divisors(n):
    out=[1]
    for p,h in factors(n): out=[a*p**j for a in out for j in range(h+1)]
    return tuple(sorted(out))

def mu(n):
    fs=factors(n)
    return 0 if any(h>1 for _,h in fs) else (-1)**len(fs)

def radical(n): return prod(p for p,_ in factors(n))
def prod(xs):
    ans=1
    for x in xs: ans*=x
    return ans

def phi(n): return prod((p-1)*p**(h-1) for p,h in factors(n))
def powerful(n): return all(h>=2 for _,h in factors(n))

def ring(q,k):
    if q<2 or k<0: raise ValueError('q>=2, k>=0 required')
    return -sum(mu(q//d)*(k%d) for d in divisors(q))

def convolution(c):
    z={}
    for r,a in c.items():
        for s,b in c.items(): z[r*s]=z.get(r*s,F(0))+a*b
    return {d:v for d,v in z.items() if v}

def amplitudes(z):
    bs={}
    for n,a in z.items():
        for q in divisors(n): bs[q]=bs.get(q,F(0))+a/n
    return bs

def u(c,d): return sum((a/n for n,a in c.items() if n%d==0),F(0))
def cumulative(c,k): return sum((a for n,a in c.items() if n<=k),F(0))

def completed_native(y):
    c={n:F(mu(n)) for n in range(1,y+1) if mu(n)}
    residual=u(c,1); n=y
    while residual:
        n+=1
        a=-min(F(3),abs(n*residual))*(1 if residual>0 else -1)
        c[n]=a; residual+=a/n
    return c

class Checks:
    def __init__(self): self.count=0
    def equal(self,a,b,label):
        self.count+=1
        if a!=b: raise AssertionError((label,a,b))
    def true(self,a,label):
        self.count+=1
        if not a: raise AssertionError(label)

def check_source(c,t):
    z=convolution(c); bs=amplitudes(z); L=max(c)
    t.equal(u(c,1),0,'balanced')
    t.equal(sum((bs.get(q,0)*phi(q) for q in bs if q>1),F(0)),sum(c.values())**2,'constant')
    for k in range(0,2*L+3):
        physical=2*cumulative(c,k)-sum((a*(k//d) for d,a in z.items()),F(0))
        anchored=2*cumulative(c,k)-sum((b*ring(q,k) for q,b in bs.items() if q>1),F(0))
        t.equal(physical,anchored,'anchored Newton')
    for p in (2,3,5,7):
        for h in range(1,6):
            b=sum((u(c,p**j)*u(c,p**(h-j)) for j in range(1,h)),F(0))
            b-=sum((u(c,p**j)*u(c,p**(h+1-j)) for j in range(1,h+1)),F(0))
            t.equal(bs.get(p**h,F(0)),b,'prime power coefficient')
    for q in (2,3,6,10,15,30):
        coprime=lambda d:sum((a/n for n,a in c.items() if gcd(n,d)==1),F(0))
        t.equal(bs.get(q,F(0)),sum((mu(d)*coprime(d)**2 for d in divisors(q)),F(0)),'squarefree coefficient')
        for p in (2,3,5):
            if gcd(p,q)>1: continue
            hmax=0
            while q*p**hmax<=L*L: hmax+=1
            for k in range(0,L+2):
                left=sum((bs.get(q*p**j,0)*ring(q*p**j,k) for j in range(hmax)),F(0))
                right=sum((p**j*(bs.get(q*p**j,0)-bs.get(q*p**(j+1),0))*ring(q,k//p**j) for j in range(hmax)),F(0))
                t.equal(left,right,'tower telescoping')

def main():
    t=Checks(); sources=0
    # Balance at one added support point. No native hypotheses used here.
    for a in (-1,0,1):
        for b in (-1,0,1):
            for c0 in (-1,0,1):
                for d in (-1,0,1):
                    c={1:F(a),2:F(b),3:F(c0),4:F(d)}
                    c[5]=-5*u(c,1)
                    check_source(c,t); sources+=1
    for q in range(2,181):
        r=radical(q); m=q//r
        for k in range(0,2*q+1):
            t.equal(ring(q,k),m*ring(r,k//m),'radical dilation')
            t.true(abs(ring(q,k))<=2**len(factors(q))*min(k,q),'kernel majorant')
            if len(factors(q))==1:
                p,h=factors(q)[0]
                t.equal(ring(q,k),-p**(h-1)*((k//p**(h-1))%p),'digit')
    native=[]
    for y in (3,7,15,31,63,95):
        c=completed_native(y); z=convolution(c); L=max(c)
        t.true(L<=2*y,'completion support')
        t.true(max(map(abs,c.values()))<=3,'completion cap')
        t.equal(u(c,1),0,'native balance')
        for n in range(1,(y+1)**2):
            v=2*c.get(n,0)-sum((z.get(d,0) for d in divisors(n)),F(0))
            t.equal(v,mu(n),'native Newton coefficient')
        if y<=15: check_source(c,t)
        native.append({'Y':y,'L':L,'completion_coefficients':sum(n>y for n in c)})
    # Exact cell grouping for the dilation norm, on finite source f.
    f=[F(0),F(2),F(-3),F(1,2),F(4)]
    for m in range(1,13):
        left=sum((f[k//m]**2/F(k*(k+1)) for k in range(1,m*len(f))),F(0))
        right=sum((f[k]**2/F(k*(k+1)*m) for k in range(1,len(f))),F(0))
        t.equal(left,right,'dilation isometry')
    print(json.dumps({'status':'PASS','exact_comparisons':t.count,'balanced_sources':sources,'native':native,'scope':'finite exact regression; no analytic theorem or full-repository validation'},indent=2))

if __name__=='__main__': main()
