#!/usr/bin/env python3
"""Exact bookkeeping for interpolated numerator means at subcritical scales.

Finite rational checks only. Analytic inputs and the interpolation proof must
be reviewed separately. Polynomial arithmetic is adapted from PR #965 at
d58e3282a9379b6ae165681bc2e21e4f9fd18c26, which credits PR #961.
"""
from __future__ import annotations
import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from math import comb

class Poly:
    def __init__(self,*a):
        self.a=tuple(F(x) for x in a) or (F(0),)
        while len(self.a)>1 and self.a[-1]==0:self.a=self.a[:-1]
    @staticmethod
    def cast(x):return x if isinstance(x,Poly) else Poly(x)
    def __add__(self,other):
        return Poly(*(x+y for x,y in itertools.zip_longest(self.a,self.cast(other).a,fillvalue=F(0))))
    __radd__=__add__
    def __neg__(self):return Poly(*(-x for x in self.a))
    def __sub__(self,other):return self+-self.cast(other)
    def __rsub__(self,other):return self.cast(other)+-self
    def __mul__(self,other):
        b=self.cast(other).a; out=[F(0)]*(len(self.a)+len(b)-1)
        for i,x in enumerate(self.a):
            for j,y in enumerate(b):out[i+j]+=x*y
        return Poly(*out)
    __rmul__=__mul__
    def __truediv__(self,other):return self*(1/F(other))
    def __eq__(self,other):return self.a==self.cast(other).a
    def __call__(self,x):return sum(c*F(x)**i for i,c in enumerate(self.a))
    def bernstein(self,end):
        n=len(self.a)-1
        return [sum(self.a[k]*end**k*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]
    def strings(self):return list(map(str,self.a))

A=F(2243,5000); H=1-A; THETA=A/2; SHIFT=F(5,6)-A/3
Z0=F(2,5); SMALL=F(1,1000); EMAX=F(1,1000000); e=Poly(0,1)
THRESHOLDS=[F(i,10000) for i in range(6728,9401)]
MUTATIONS=['old-numerator','omit-conductor','upper-count','old-small-cutoff','old-shift','zero-tail-gap']

def density(s):
    q=2*s-1; n=6
    if n*q<=2:
        aa=F(1,2);bb=2/(4-n*q);g=1-q/(4-n*q)
    elif n*q<=n-1:
        dd=n*q*(2*(n-1)-n*q)-2*(n-1)
        aa=(n*q*(n-2)-(n-1))/dd
        bb=(n*q*(2*n-5)-2*(n-2))/dd
        g=((2*n-3)*q*(n+1-n*q)-2*(n-1))/dd
    else:
        dd=1-n*(1-q)**2
        aa=(n*q-n+2)/dd;bb=((n+2)*q-n+1)/dd
        g=(1-q)*((n+2)*q-n+1)/dd
    return aa,bb,1/(6-4*s),g,(1-s)/(3-2*s)

def closed_g(s):
    if s<=F(2,3):return 1-(2*s-1)/(4-6*(2*s-1))
    if s<=F(11,12):
        return 1-(2*s-1)*((2*s-1)*36-(6*s-2)*6+3)/((2*s-1)*(3-2*s)*36-24*s+2)
    return 1-(8*s*s-10*s+3)/(1-24*(1-s)**2)

def scale(x,y,z):return A/2+x-1+H*z+A*(y-1)

def domain(x,y,z):
    return [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,
            6*x+6*z-5,x-F(1,2),3*x-2,3*x+y-F(5,2)]

class Checks:
    def __init__(self):self.groups=Counter()
    def check(self,group,name,ok):
        if not ok:raise ValueError(f'{group}: {name}')
        self.groups[group]+=1
    def identity(self,name,x,y):self.check('identities',name,Poly.cast(x)==y)
    def positive(self,group,name,value,strict=False):
        p=Poly.cast(value);bb=p.bernstein(EMAX)
        valid=all(b>=0 for b in bb)
        # With nonnegative Bernstein coefficients, any positive coefficient
        # gives positivity in the open interval; check the included right end.
        if strict:valid=valid and any(b>0 for b in bb) and p(EMAX)>0
        self.check(group,name,valid)

def run(mutation=None,details=False):
    c=Checks();rows=[];vertices=[(1+e,1+e,Z0)]
    c.identity('support',2*A,F(2243,2500))
    c.identity('theta',THETA,F(2243,10000))
    c.identity('shift',F(17,25) if mutation=='old-shift' else SHIFT,F(3419,5000))
    c.identity('boundary',SHIFT+THETA,F(9081,10000))
    c.identity('improvement over #965',F(91,100)-SHIFT-THETA,F(19,10000))
    c.check('scales','positive subcritical',0<2*A<1)
    for sigma in [F(3,5),F(3,4),F(9,10)]:
        for delta in [F(1,100),F(1,1000)]:
            invp=(1+delta-sigma)/(1+2*delta)
            c.check('interpolation','valid norm exponent',0<invp<F(1,2))
            c.check('interpolation','right-line loss',0<=invp-(1-sigma)<=delta)
    for y in [F(1,10),F(1,4),F(2,5)]:
        for nu in [F(1,4),F(3,4),F(1)]:
            conductor=0 if mutation=='omit-conductor' else F(1,2)-y
            c.identity('functional-equation cost',nu*(1-y)+y+conductor,F(1,2)+nu*(1-y))

    for j,s in enumerate(THRESHOLDS):
        aa,bb,z,g,height=density(s)
        c.check('density-domains',str(j),F(2,3)<s<1 and 0<aa<=bb and 0<g<1)
        c.check('density-formula',str(j),g==closed_g(s))
        if j:c.check('partition-grid',str(j),s-THRESHOLDS[j-1]==F(1,10000))
        first=[aa,F(1),aa/3+F(5,6),5*aa/6+F(1,3)]
        terms=[(F(1,2)+(F(1,2)-s)*bb+t/2,(F(1,2)-s)*z+F(1,4)) for t in first]
        terms += [((2-2*s)*bb,(2-2*s)*z),(1+(1-2*s)*aa,F(0))]
        for base,k in [(F(1,3),F(11,6)-2*s),(F(5,6),F(4,3)-2*s)]:
            terms.extend([(base+k*aa,F(0)),(base+k*bb,k*z)])
        for i,(u,v) in enumerate(terms):
            c.check('density-norm-monomials',f'{j}/{i}',u<=g)
            c.check('density-height-monomials',f'{j}/{i}',v<=height)
        R=2-s-e/4;ro=2-s-e/2;rt=2-s-e;ri=1-e/4
        for name,p in [('R-ro',R-ro),('ro-rt',ro-rt),('rt-ri',rt-ri),('ri',ri)]:
            c.positive('reciprocal-disks',f'{j}/{name}',p,True)

    def add(name,x,y,nu,method,lower=None,upper=None):
        if method=='mean':numerator=(nu+1)/2
        elif method=='interpolated':
            numerator=nu+(1-y)/2 if mutation=='old-numerator' else F(1,2)+nu*(1-y)
            c.positive('interpolation-lines',name+' lower',y,True)
            c.positive('interpolation-lines',name+' upper',F(1,2)-y,True)
        else:numerator=nu+(1-y)/2
        row=numerator-Z0
        growth=scale(x,y,Z0)+(H+e)*row
        c.positive('row-exponents',name,row,True)
        c.positive('central-budgets',name,THETA+4*e-growth,True)
        vertices.extend([(x,1+e,Z0),(x,y,Z0)])
        entry={'name':name,'method':method,'lower':None if lower is None else str(lower),
               'upper':None if upper is None else str(upper),'x':Poly.cast(x).strings(),
               'y':Poly.cast(y).strings(),'nu':Poly.cast(nu).strings(),
               'growth':growth.strings(),'constant_margin':str(THETA-growth(0))}
        rows.append(entry)
        return growth

    good=add('good',THRESHOLDS[0]+e,F(1,2),F(1),'mean',upper=THRESHOLDS[0])
    c.identity('good explicit growth',good,Poly(F(1121,5000),F(8,5)))
    for j,(lo,hi) in enumerate(zip(THRESHOLDS,THRESHOLDS[1:])):
        count_at=hi if mutation=='upper-count' else lo
        c.check('partition-count',str(j),count_at==lo)
        if lo<F(69,100):method='mean';y=F(1,2)
        elif lo<F(86,100):method='interpolated';y=max(1-hi,F(5,2)-3*hi)+e
        else:method='convexity';y=1-hi+e
        val=add(f'middle-{j}',hi+e,y,density(count_at)[3]+e,method,lo,hi)
        c.check('middle-strict-margin',str(j),val(0)<THETA)
    add('last',1+e,e,density(THRESHOLDS[-1])[3]+e,'convexity',THRESHOLDS[-1])
    c.check('partition-count','all classes',len(rows)==2674)

    principal_w=scale(1+e,F(1,2),F(1,6)+e)
    principal_z=scale(1+e,1,e)
    small_cutoff=F(1,100) if mutation=='old-small-cutoff' else SMALL
    small=scale(1+e,F(1,2),Z0)+small_cutoff*(F(5,4)-Z0)
    large=A/2+3+3*A+H-10-e
    c.identity('principal w constant',principal_w(0),H/6)
    c.identity('principal z constant',principal_z(0),THETA)
    c.identity('small rows constant',small(0),F(22141,100000))
    c.identity('large rows constant',large(0),-F(9757,2000))
    # z=L=10/e+2 on the original absolutely convergent x=y=4 lines.
    eL=10+2*e
    c.identity('large contour denominator cleared',e*(A/2+3+3*A)+H*eL+(H+e)*(e-eL),e*large)
    for name,value in [('principal-w',principal_w),('principal-z',principal_z),('small',small),('large',large)]:
        c.positive('other-budgets',name,THETA+4*e-value,True)
    c.positive('tail-gap','positive',0 if mutation=='zero-tail-gap' else e,True)
    c.positive('tail-gap','cutoff below .56',F(14,25)-H-e,True)
    vertices += [(1+e,1+e,F(1,6)+e),(1+e,F(1,2),F(1,6)+e),
                 (1+e,1,F(1,6)+e),(1+e,1,e),(1+e,F(1,2),Z0),(4,4,2)]
    for i,v in enumerate(vertices):
        for j,p in enumerate(domain(*v)):c.positive('contour-domain',f'{i}/{j}',p,True)
    c.identity('final Mellin loss',SHIFT+THETA+5*e,Poly(F(9081,10000),5))
    middles=[r for r in rows if r['name'].startswith('middle-')]
    worst=min(middles,key=lambda r:F(r['constant_margin']))
    return {'status':'EXACT_RATIONAL finite bookkeeping; analytic composition proposed',
            'a':str(A),'support':str(2*A),'theta':str(THETA),'Mellin_shift':str(SHIFT),
            'proposed_boundary':str(SHIFT+THETA),'e_interval':'0 < e <= '+str(EMAX),
            'small_norm_cutoff':str(SMALL),'threshold_count':len(THRESHOLDS),
            'class_count':len(rows),'method_counts':dict(sorted(Counter(r['method'] for r in rows).items())),
            'minimum_middle_constant_margin':worst,'checks':dict(sorted(c.groups.items())),
            **({'classes':rows} if details else {})}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mutation',choices=MUTATIONS)
    p.add_argument('--details',action='store_true')
    args=p.parse_args()
    print(json.dumps(run(args.mutation,args.details),sort_keys=True,indent=2))
