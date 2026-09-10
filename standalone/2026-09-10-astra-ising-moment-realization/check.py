#!/usr/bin/env python3
"""Exact outward dyadic theta moments and a eight-moment ferromagnetic seed.
No floating arithmetic, zeta oracle, zero list, or numerical quadrature library.
This checks the stated finite construction, not the open all-order realization.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import sys

BITS=256
SCALE=1<<BITS
DEGREE=80
ROOT=Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def ceildiv(a,b):
    require(b>0, 'positive divisor required')
    return -((-a)//b)


class I:
    __slots__=('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo=int(lo); self.hi=int(lo if hi is None else hi)
        require(self.lo<=self.hi,'reversed interval')
    @staticmethod
    def rat(p,q=1):
        require(q>0,'positive rational denominator required')
        return I((p*SCALE)//q,ceildiv(p*SCALE,q))
    @staticmethod
    def coerce(x):
        if isinstance(x,I): return x
        if type(x) is int: return I(x*SCALE)
        if isinstance(x,F): return I.rat(x.numerator,x.denominator)
        raise TypeError('only exact numbers accepted')
    def __add__(self,x):
        x=I.coerce(x); return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,x): return self+(-I.coerce(x))
    def __rsub__(self,x): return I.coerce(x)+(-self)
    def __mul__(self,x):
        x=I.coerce(x)
        p=(self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi)
        return I(min(p)//SCALE,ceildiv(max(p),SCALE))
    __rmul__=__mul__
    def __truediv__(self,x):
        if type(x) is int:
            if x<0:return (-self)/(-x)
            require(x>0,'zero divisor');return I(self.lo//x,ceildiv(self.hi,x))
        x=I.coerce(x)
        require(x.lo>0 or x.hi<0,'division through zero')
        if x.hi<0:return (-self)/(-x)
        return self*I((SCALE*SCALE)//x.hi,ceildiv(SCALE*SCALE,x.lo))
    def __rtruediv__(self,x): return I.coerce(x)/self
    def __pow__(self,k):
        require(type(k) is int and k>=0,'nonnegative integer power required')
        out=I.coerce(1); base=self
        while k:
            if k&1: out=out*base
            k//=2
            if k:base=base*base
        return out
    def sqrt(self):
        require(self.lo>=0,'negative square root')
        lo=isqrt(self.lo*SCALE); h=self.hi*SCALE; hi=isqrt(h)
        return I(lo,hi if hi*hi==h else hi+1)
    def record(self): return [self.lo,self.hi]


def exp_endpoint(x):
    """Enclose exp(x/SCALE) for an integer x."""
    if x<0:return 1/exp_endpoint(-x)
    k=0
    while x> (SCALE//8)*(1<<k):k+=1
    y=I.rat(x,SCALE*(1<<k))
    term=I.coerce(1); total=term
    for j in range(1,97):
        term=term*y/j;total=total+term
    nxt=term*y/97
    rem=nxt/(1-y/98)
    total=I(total.lo,total.hi+rem.hi)
    for _ in range(k):total=total*total
    return total


def exp(x):
    x=I.coerce(x)
    return I(exp_endpoint(x.lo).lo,exp_endpoint(x.hi).hi)


def atan_recip(n):
    # Alternating series: 96 terms, first omitted term bounds remainder.
    total=F(0)
    for k in range(96):total+=F((-1)**k,(2*k+1)*n**(2*k+1))
    rem=F(1,193*n**193)
    return I.rat(total.numerator,total.denominator)+I(0,I.rat(rem.numerator,rem.denominator).hi)


def pi_interval():return 16*atan_recip(5)-4*atan_recip(239)


def series_exp_linear(a,center,h):
    out=[exp(a*center)]; v=a*h
    for k in range(1,DEGREE+1):out.append(out[-1]*v/k)
    return out


def mulpoly(a,b,limit=None):
    last=len(a)+len(b)-2
    if limit is not None:last=min(last,limit)
    c=[I.coerce(0) for _ in range(last+1)]
    for i,u in enumerate(a):
        for j in range(min(len(b),last-i+1)):
            c[i+j]=c[i+j]+u*b[j]
    return c


def cell_density(n,center,pi):
    h=I.rat(1,32); c=I.coerce(center);q=pi*n*n
    e2=series_exp_linear(I.coerce(2),c,h)
    g=[-q*v for v in e2]
    hh=[exp(g[0])]
    for j in range(1,DEGREE+1):
        hh.append(sum((k*g[k]*hh[j-k] for k in range(1,j+1)),I.coerce(0))/j)
    e9=series_exp_linear(I.rat(9,2),c,h)
    e5=series_exp_linear(I.rat(5,2),c,h)
    pref=[4*q*q*x-6*q*y for x,y in zip(e9,e5)]
    return mulpoly(pref,hh,DEGREE)


def integrate_moment(poly,center,j):
    h=I.rat(1,32); c=I.coerce(center)
    power=[comb(j,k)*(c**(j-k))*(h**k) for k in range(j+1)]
    out=mulpoly(poly,power)
    # Full-line moment: factor two times half-line cell integral.
    return 4*h*sum((out[k]/(k+1) for k in range(0,len(out),2)),I.coerce(0))


def theta_moments():
    pi=pi_interval(); require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi bounds')
    js=(0,2,4,6,8,10)
    totals={j:I.coerce(0) for j in js}
    counts=(32,24,16,12)
    for n,cnt in enumerate(counts,1):
        for k in range(cnt):
            center=F(2*k+1,32)
            density=cell_density(n,center,pi)
            for j in js:totals[j]=totals[j]+integrate_moment(density,center,j)
    # Complete Taylor and every time/index tail. The paper proves the ceilings.
    cauchy=I.rat(16*10**15,4**81)/I.rat(3,4)
    time_tail=16*factorial(12)*(64*81**2+162+1)*exp(I.coerce(-150))
    omitted=128*625*exp(I.coerce(-75))/I.rat(147,2)
    require(omitted.hi < I.rat(1,10**28).lo,'all omitted theta terms')
    for j in js:
        x=totals[j]
        totals[j]=I(x.lo-cauchy.hi,x.hi+cauchy.hi+time_tail.hi+omitted.hi)
    require(totals[0].lo>0,'positive normalization')
    mu={j:totals[j]/totals[0] for j in js[1:]}
    return pi,totals,mu,{'cells':sum(counts),'degree':DEGREE,
        'cauchy_error':cauchy.record(),'time_tail':time_tail.record(),
        'omitted_index_tail':omitted.record()}


def fit_seed(mu):
    v=mu[2]; r4=mu[4]/v**2; r6=mu[6]/v**3; r8=mu[8]/v**4
    k4=r4-3; k6=r6-15*r4+30
    k8=r8-28*r6-35*r4*r4+420*r4-630
    s2=-k4/2; s3=k6/16; s4=-k8/272
    def data(a):
        r1=1-25*a; r2=s2-25*a*a; r3=s3-25*a**3
        e2=(r1*r1-r2)/2; e3=(r1**3-3*r1*r2+2*r3)/6
        return r1,e2,e3,r2,r3
    def g(a):
        e1,e2,e3,r2,r3=data(a)
        return 25*a**4+e1*r3-e2*r2+e3*e1-s4
    lo=F(220907,10**7); hi=F(220909,10**7)
    require(g(I.coerce(lo)).lo>0 and g(I.coerce(hi)).hi<0,'quartic IVT bracket')
    # Interval brackets for the three roots at EVERY a in this initial interval.
    def root_brackets(a, refine):
        e1,e2,e3,_,_=data(a)
        def f(x):return x**3-e1*x*x+e2*x-e3
        brackets=[(F(404,10000),F(406,10000),1),
                  (F(1415,10000),F(1418,10000),-1),
                  (F(2655,10000),F(2658,10000),1)]
        out=[]
        for l,h,sgn in brackets:
            fl=f(I.coerce(l))*sgn;fh=f(I.coerce(h))*sgn
            require(fl.hi<0 and fh.lo>0,'three positive cubic roots')
            if refine:
                for _ in range(65):
                    mid=(l+h)/2;fm=f(I.coerce(mid))*sgn
                    if fm.hi<0:l=mid
                    elif fm.lo>0:h=mid
                    else:break
            out.append(I(I.coerce(l).lo,I.coerce(h).hi))
        return out
    roots0=root_brackets(I(I.coerce(lo).lo,I.coerce(hi).hi),False)
    require(all(r.lo>I.coerce(hi).hi for r in roots0),'quartic derivative sign')
    for _ in range(65):
        mid=(lo+hi)/2;gm=g(I.coerce(mid))
        if gm.lo>0:lo=mid
        elif gm.hi<0:hi=mid
        else:break
    a=I(I.coerce(lo).lo,I.coerce(hi).hi)
    b,c,d=root_brackets(a,True)
    weights=[(v*x).sqrt() for x in (a,b,c,d)]
    k10=7936*(25*a**5+b**5+c**5+d**5)
    model10=k10+45*k8+210*k6*k4+630*k6+1575*k4*k4+3150*k4+945
    diff=model10-mu[10]/v**5
    require(diff.lo>I.rat(-123,1000).hi and diff.hi<I.rat(-122,1000).lo,
            'unmatched tenth moment')
    return {'s2':s2.record(),'s3':s3.record(),'s4':s4.record(),
        'a':a.record(),'b':b.record(),'c':c.record(),'d':d.record(),
        'weights':[x.record() for x in weights], 'multiplicities':[25,1,1,1],
        'standardized_tenth_difference':diff.record(),
        'left_sign_lower':g(I.coerce(lo)).lo,'right_sign_upper':g(I.coerce(hi)).hi}


def grouped_moments(counts, weights, q, max_order=8):
    """Exact complete-graph Ising moments, Jij=log(q)/2, in grouped states.

    counts are positive integers; weights and q are Fractions, with q>=1.
    Work is product(count+1), not 2**sum(counts). No large-size guarantee.
    """
    from itertools import product
    require(len(counts)==len(weights)>0, 'group dimensions')
    require(all(type(n) is int and n>0 for n in counts), 'positive group sizes')
    require(all(isinstance(a,F) and a>=0 for a in weights), 'exact nonnegative weights')
    require(isinstance(q,F) and q>=1, 'ferromagnetic q required')
    total=sum(counts); norm=F(0); numer=[F(0) for _ in range(max_order+1)]
    for indices in product(*(range(n+1) for n in counts)):
        mag=[2*k-n for k,n in zip(indices,counts)]
        S=sum(mag); power=(S*S-(total%2))//4
        require(4*power==S*S-(total%2), 'integer Gibbs exponent')
        mass=q**power
        for k,n in zip(indices,counts):mass*=comb(n,k)
        x=sum((a*t for a,t in zip(weights,mag)),F(0))
        norm+=mass; xx=F(1)
        for r in range(max_order+1):numer[r]+=mass*xx;xx*=x
    return [u/norm for u in numer]


def determinant(matrix):
    a=[row[:] for row in matrix];d=F(1);n=len(a)
    for k in range(n):
        pivot=next((j for j in range(k,n) if a[j][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];d=-d
        t=a[k][k];d*=t
        for j in range(k+1,n):
            factor=a[j][k]/t
            for l in range(k+1,n):a[j][l]-=factor*a[k][l]
    return d


def rational_controls():
    # Direct enumeration vs the independent-spin moment recursion, no fitted data.
    panels=0
    for weights in ([F(1,3),F(1,5)], [F(1,4),F(1,3),F(1,7)], [F(2,5),F(1,2),F(1,6),F(1,8)]):
        law={F(0):F(1)}
        for a in weights:
            nxt={}
            for x,p in law.items():
                for y in (x-a,x+a):nxt[y]=nxt.get(y,F(0))+p/2
            law=nxt
        m=[sum(p*x**j for x,p in law.items()) for j in range(11)]
        v=sum(a*a for a in weights);k4=-2*sum(a**4 for a in weights)
        k6=16*sum(a**6 for a in weights);k8=-272*sum(a**8 for a in weights)
        expected={2:v,4:k4+3*v*v,6:k6+15*k4*v+15*v**3,
                  8:k8+28*k6*v+35*k4*k4+210*k4*v*v+105*v**4,
                  10:7936*sum(a**10 for a in weights)+45*k8*v+210*k6*k4
                     +630*k6*v*v+1575*k4*k4*v+3150*k4*v**3+945*v**5}
        for j,x in expected.items():require(m[j]==x,'independent moment identity');panels+=1
        for j in (1,3,5,7):require(m[j]==0,'spin reflection');panels+=1
    # Exact rank-one Gibbs subtraction, for every configuration of four spins.
    a=[F(1,2),F(2,3),F(3,5),F(4,7)];tau=F(2,5)
    for mask in range(16):
        spins=[1 if mask>>i&1 else -1 for i in range(4)]
        x=sum(a[i]*spins[i] for i in range(4))
        cross=sum(a[i]*a[j]*spins[i]*spins[j] for i in range(4) for j in range(i+1,4))
        require(tau*x*x/2 == tau*cross+tau*sum(v*v for v in a)/2,'Gibbs subtraction')
        panels+=1
    from itertools import product
    for counts,weights in [([2,1],[F(1,3),F(2,5)]),
                           ([3,1,1],[F(1,7),F(1,3),F(2,5)])]:
        expanded=[a for n,a in zip(counts,weights) for _ in range(n)]
        for q in [F(1),F(5,4),F(2)]:
            norm=F(0);numbers=[F(0) for _ in range(9)]
            for sig in product((-1,1),repeat=len(expanded)):
                aligned=sum(sig[i]==sig[j] for i in range(len(sig)) for j in range(i+1,len(sig)))
                prob=q**aligned;x=sum((a*t for a,t in zip(expanded,sig)),F(0))
                norm+=prob
                for k in range(9):numbers[k]+=prob*x**k
            require(grouped_moments(counts,weights,q)==[x/norm for x in numbers],
                    'grouped vs individual Ising configurations')
            panels+=1
    try:grouped_moments([1,1],[F(1),F(1)],F(1,2))
    except ValueError:panels+=1
    else:raise ValueError('negative coupling accepted')
    for xs in [[F(1,50),F(1,25),F(1,7),F(1,4)],
               [F(1,30),F(1,20),F(1,5),F(1,3)]]:
        mult=[25,1,1,1];cs=[1,-2,16,-272]
        matrix=[[(r+1)*cs[r]*mult[i]*xs[i]**r for i in range(4)] for r in range(4)]
        expected=F(25)
        for r in range(4):expected*=(r+1)*cs[r]
        for i in range(4):
            for j in range(i+1,4):expected*=xs[j]-xs[i]
        require(determinant(matrix)==expected and expected!=0,'moment Jacobian')
        panels+=1
    return panels


def reconstruct():
    pi,moments,mu,coverage=theta_moments()
    return {'schema':'IMR26.1','status':'proposed-components-not-RH-proof',
        'arithmetic':'outward-dyadic-integer','bits':BITS,
        'pi':pi.record(),'raw_moments':{str(j):x.record() for j,x in moments.items()},
        'moments':{str(j):x.record() for j,x in mu.items()},'coverage':coverage,
        'seed':fit_seed(mu),'rational_controls':rational_controls(),
        'all_order_realization_proved':False}


def strict_json(text):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'duplicate key');d[k]=v
        return d
    def bad(x):raise ValueError('floating/special number rejected')
    return json.loads(text,object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)


def same(a,b):
    if type(a) is not type(b):return False
    if type(a) is dict:return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if type(a) is list:return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b


def inventory():
    manifest=ROOT/'SHA256SUMS'
    require(manifest.is_file() and not manifest.is_symlink(),'missing regular manifest')
    wanted={}
    for line in manifest.read_text().splitlines():
        digest,name=line.split('  ')
        require('/' not in name and name not in wanted and len(digest)==64,'manifest format')
        wanted[name]=digest
    require(set(p.name for p in ROOT.iterdir())==set(wanted)|{'SHA256SUMS'},'inventory')
    for name,digest in wanted.items():
        p=ROOT/name
        require(p.is_file() and not p.is_symlink(),'nonregular file')
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'hash mismatch: '+name)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--emit',action='store_true',help='producer-only, no inventory authentication')
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    require(args.emit != (args.check is not None),'choose emit OR check')
    if args.check is not None:
        inventory(); supplied=strict_json(args.check.read_text())
    result=reconstruct()
    if args.check is not None:require(same(result,supplied),'primitive replay mismatch')
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,KeyError,OSError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);sys.exit(2)
