#!/usr/bin/env python3
"""Outward integer theta integrals and a nonperturbative interacting-spin root.
Interval primitives/Taylor recursion adapted from IMR26 (#847), not an independent backend.
No floating arithmetic, zeta oracle, input moment receipt, or extrapolation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import sys

BITS=320
SCALE=1<<BITS
DEGREE=120
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
    pi=pi_interval()
    require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi')
    js=tuple(range(0,17,2));counts=(32,24,16,12)
    totals={j:I.coerce(0) for j in js}
    for n,cnt in enumerate(counts,1):
        for k in range(cnt):
            center=F(2*k+1,32)
            d=cell_density(n,center,pi)
            for j in js:totals[j]+=integrate_moment(d,center,j)
    errs={}
    for j in js:
        # Cauchy circle radius1/8, half-cell1/32. Full source, not just a truncation.
        e=I.rat(16*10**11*2**j,4**(DEGREE+1))/F(3,4)
        tails=I.coerce(0)
        for n,cnt in enumerate(counts,1):
            U=F(cnt,16);q=pi*n*n;E=exp(2*I.coerce(U));lam=2*q*E-F(9,2)
            tails+=8*q*q*exp(F(9,2)*I.coerce(U)-q*E)*sum(
                (comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
        omitted=16*pi*pi*625*exp(-25*pi)*factorial(j)/(50*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-e.hi, totals[j].hi+e.hi+tails.hi+omitted.hi)
        errs[str(j)]={'taylor':e.record(),'time':tails.record(),'index':omitted.record()}
    require(totals[0].lo>0,'normalization')
    mu={j:totals[j]/totals[0] for j in js[1:]}
    return totals,mu,errs


def cumulants(mom):
    k=[mom[0]*0 for _ in mom]
    for n in range(1,len(mom)):
        k[n]=mom[n]-sum((comb(n-1,j-1)*k[j]*mom[n-j] for j in range(1,n)),mom[0]*0)
    return k


def inverse(a):
    n=len(a);b=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for col in range(n):
        k=next(i for i in range(col,n) if b[i][col])
        b[k],b[col]=b[col],b[k];v=b[col][col];b[col]=[x/v for x in b[col]]
        for i in range(n):
            if i==col:continue
            v=b[i][col];b[i]=[x-v*y for x,y in zip(b[i],b[col])]
    return [row[n:] for row in b]


def absup(x):return max(abs(x.lo),abs(x.hi))


def strict_json(p):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'duplicate JSON key');d[k]=v
        return d
    def nofloat(s):raise ValueError('float tokens forbidden')
    return json.loads(Path(p).read_text(),object_pairs_hook=pairs,parse_float=nofloat,parse_constant=nofloat)


def algebra_controls():
    from itertools import product
    controls=0
    # Three-state dimer formula, independently enumerate its four spin states.
    for q in (F(1),F(2,3),F(1,2),F(1,4)):
        p=[F(1) if x==y else q for x,y in product((-1,1),repeat=2)]
        Z=sum(p)
        for k in range(1,9):
            direct=sum(v*F(x+y,2)**(2*k) for v,(x,y) in zip(p,product((-1,1),repeat=2)))/Z
            require(direct==1/(1+q),'dimer probability/moment');controls+=1
    # Matched dimer at cos(theta)=-2/3 escapes zero tripling.
    c=F(-2,3);require((F(2,3)+(4*c**3-3*c))/(1+F(2,3))==F(8,9),'triple-angle')
    controls+=1
    # Exact convolution moments vs full independent block enumeration.
    for counts in ((2,1),(3,2),(1,1,1)):
        weights=[F(i+1,7) for i in range(len(counts))]
        expanded=[w for n,w in zip(counts,weights) for _ in range(n)]
        direct=[]
        for k in range(9):
            direct.append(sum(sum((a*s for a,s in zip(expanded,bits)),F(0))**k
                for bits in product((-1,1),repeat=len(expanded)))/2**len(expanded))
        kc=cumulants(direct)
        unit=cumulants([F(0) if k%2 else F(1) for k in range(9)])
        for k in range(1,9):
            require(kc[k]==unit[k]*sum(a**k for a in expanded),'block cumulants');controls+=1
    return controls


def reconstruct():
    pars=strict_json(ROOT/'parameters.json')
    require(pars['schema']=='ICR26.parameters.v1' and pars['q']==[2,3],'parameter convention')
    require(all(type(x) is int and x>0 for x in pars['multiplicities']),'multiplicities')
    nu=pars['multiplicities'];require(nu==[256,10,1,1,1,1],'complete spin inventory')
    require(all(type(x) is str for x in pars['centers']),'rational center strings')
    c=[F(x) for x in pars['centers']];require(len(c)==7,'seven centers')
    rad=F(pars['radius']);require(rad==F(1,10**14),'fixed box')
    box=[I(I.coerce(x-rad).lo,I.coerce(x+rad).hi) for x in c]
    require(all(x.lo>0 for x in box),'positive weights')
    raw,mu,errs=theta_moments();v=mu[2]
    mom=[I.coerce(0) for _ in range(17)];mom[0]=I.coerce(1)
    for j in range(1,9):mom[2*j]=mu[2*j]/v**j
    kap=cumulants(mom)
    cs=cumulants([F(0) if j%2 else F(1) for j in range(17)])
    dm=[F(0) if j%2 else F(3,5) for j in range(17)];dm[0]=F(1)
    dc=cumulants(dm);ratios=[dc[2*j]/cs[2*j] for j in range(1,9)]
    s=[kap[2*j]/cs[2*j] for j in range(1,9)]
    A=[[j*nu[i]*c[i]**(j-1) for i in range(6)]+[j*ratios[j-1]*c[6]**(j-1)] for j in range(1,8)]
    R=inverse(A)
    for i in range(7):
        for j in range(7):require(sum(R[i][k]*A[k][j] for k in range(7))==F(i==j),'rational inverse')
    resid=[sum(nu[i]*c[i]**j for i in range(6))+ratios[j-1]*c[6]**j-s[j-1] for j in range(1,8)]
    beta=max(absup(sum((R[i][j]*resid[j] for j in range(7)),I.coerce(0))) for i in range(7))
    J=[[j*nu[i]*box[i]**(j-1) for i in range(6)]+[j*ratios[j-1]*box[6]**(j-1)] for j in range(1,8)]
    L=max(sum(absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j] for k in range(7)),I.coerce(0)))
        for j in range(7)) for i in range(7))
    require(L<SCALE//100,'whole-box contraction')
    require(F(beta,SCALE)+F(L,SCALE)*rad<rad,'whole-box invariance')
    require(beta<I.rat(6,10**22).lo,'small residual')
    require(L<I.rat(101,10**9).lo,'stated row-sum bound')
    require(max(sum(abs(x) for x in row) for row in R)<75000000,'stated inverse norm')
    share=F(3,5)*box[6]
    require(share.lo>I.rat(9268,100000).hi and share.hi<I.rat(9269,100000).lo,'dimer variance share')
    err16=cs[16]*(sum((nu[i]*box[i]**8 for i in range(6)),I.coerce(0))+ratios[7]*box[6]**8-s[7])
    require(err16.lo>I.rat(20,100).hi and err16.hi<I.rat(21,100).lo,'unmatched16 remains')
    require(s[1].lo>0 and kap[4].hi<I.rat(-20,100).lo,'actual non-Gaussian theta')
    weights=[(v*x).sqrt() for x in box[:6]]+[(v*box[6]).sqrt()/2]
    return {'schema':'ICR26.result.v1','status':'proposed-component-not-RH','rh_proved':False,
       'matched_even_orders':[2,4,6,8,10,12,14],'spins':272,'positive_edges':1,
       'exp_minus_2J':[2,3], 'normalization':raw[0].record(),'variance':v.record(),
       'theta_raw_integrals':{str(j):raw[j].record() for j in raw},
       'standardized_cumulant_ratios':[x.record() for x in s],
       'beta_dyadic_upper':beta,'jacobian_row_sum_dyadic_upper':L,
       'preconditioner_row_norm':[max(sum(abs(x) for x in row) for row in R).numerator,
                                  max(sum(abs(x) for x in row) for row in R).denominator],
       'root_box':[[str(x-rad),str(x+rad)] for x in c],
       'physical_weight_intervals':[x.record() for x in weights],
       'standardized_unmatched16':err16.record(),'bits':BITS,'cells':84,'degree':DEGREE,
       'tail_errors':errs,'finite_algebra_controls':algebra_controls(),'inverse_identities':49}


def authenticate():
    lines=(ROOT/'SHA256SUMS').read_text().splitlines()
    listed={}
    for line in lines:
        h,p=line.split('  ',1);require('/' not in p and p not in listed,'manifest path')
        f=ROOT/p;require(f.is_file() and not f.is_symlink(),'regular file')
        require(hashlib.sha256(f.read_bytes()).hexdigest()==h,'file hash '+p);listed[p]=h
    actual={p.name for p in ROOT.iterdir()}
    require(actual==set(listed)|{'SHA256SUMS'},'exact inventory')
    require('check.py' in listed and 'PROOF.md' in listed,'required proof/code')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--check')
    a=ap.parse_args()
    require(a.emit != bool(a.check),'choose producer or accepting mode')
    if not a.emit:authenticate()
    old=strict_json(a.check) if a.check else None
    result=reconstruct()
    if a.check:
        # Canonical JSON comparison distinguishes bool and integer aliases.
        require(json.dumps(old,sort_keys=True,separators=(',',':'))==json.dumps(result,sort_keys=True,separators=(',',':')),'primitive result mismatch')
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
