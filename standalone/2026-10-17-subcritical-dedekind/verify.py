#!/usr/bin/env python3
"""Exact finite bookkeeping for the proposed subcritical-scale composition.

This does NOT certify the analytic inputs, character adapter, infinite sums,
contour shifts, or theorem. Polynomial utility adapted from PR #961; new data,
budgets and controls. Standard library only; explicit errors work under -O.
"""
from __future__ import annotations
import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from math import comb

class Poly:
    def __init__(self, *a):
        self.a = tuple(F(x) for x in a) or (F(0),)
        while len(self.a)>1 and self.a[-1]==0: self.a=self.a[:-1]
    @staticmethod
    def cast(x): return x if isinstance(x,Poly) else Poly(x)
    def __add__(self, other):
        b=self.cast(other).a
        return Poly(*(x+y for x,y in itertools.zip_longest(self.a,b,fillvalue=F(0))))
    __radd__=__add__
    def __neg__(self): return Poly(*(-x for x in self.a))
    def __sub__(self, other): return self+-self.cast(other)
    def __rsub__(self, other): return self.cast(other)+-self
    def __mul__(self,other):
        b=self.cast(other).a; out=[F(0)]*(len(self.a)+len(b)-1)
        for i,x in enumerate(self.a):
            for j,y in enumerate(b): out[i+j]+=x*y
        return Poly(*out)
    __rmul__=__mul__
    def __truediv__(self,other): return self*(1/F(other))
    def __eq__(self,other): return self.a==self.cast(other).a
    def __call__(self,x): return sum(c*F(x)**i for i,c in enumerate(self.a))
    def bernstein(self,end):
        n=len(self.a)-1
        return [sum(self.a[k]*end**k*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]
    def strings(self): return list(map(str,self.a))

A=F(23,50); H=1-A; THETA=A/2; B=1-(A/2+(1-A)/6)
E_MAX=F(1,1000000); e=Poly(0,1); Z0=F(2,5)
THRESHOLDS=list(map(F,['69/100','3709/5000','3801/5000','7679/10000',
'7713/10000','7729/10000','484/625','7761/10000','389/500','3901/5000',
'1957/2500','7859/10000','987/1250','7941/10000','1999/2500','4033/5000',
'8157/10000','8281/10000','4229/5000','873/1000','23/25']))
MUTATIONS=['drop-diagonal','individual-numerator','upper-count',
           'old-shift','zero-tail-gap','delete-subunit-profile','wrong-beta']

def density(s):
    q=2*s-1; n=6
    if n*q<=2:
        aa=F(1,2); bb=2/(4-n*q); g=1-q/(4-n*q)
    elif n*q<=n-1:
        dd=n*q*(2*(n-1)-n*q)-2*(n-1)
        aa=(n*q*(n-2)-(n-1))/dd
        bb=(n*q*(2*n-5)-2*(n-2))/dd
        g=((2*n-3)*q*(n+1-n*q)-2*(n-1))/dd
    else:
        dd=1-n*(1-q)**2
        aa=(n*q-n+2)/dd; bb=((n+2)*q-n+1)/dd
        g=(1-q)*((n+2)*q-n+1)/dd
    return aa,bb,1/(6-4*s),g,(1-s)/(3-2*s)

def closed_g(s):
    if s<=F(2,3): return 1-(2*s-1)/(4-6*(2*s-1))
    if s<=F(11,12):
        return 1-(2*s-1)*((2*s-1)*36-(6*s-2)*6+3)/((2*s-1)*(3-2*s)*36-24*s+2)
    return 1-(8*s*s-10*s+3)/(1-24*(1-s)**2)

def scale(x,y,z): return A/2+x-1+H*z+A*(y-1)

def domain(x,y,z):
    return [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,
            6*x+6*z-5,x-F(1,2),3*x-2,3*x+y-F(5,2)]

class Checks:
    def __init__(self): self.groups=Counter()
    def check(self,g,n,ok):
        if not ok: raise ValueError(f'{g}: {n}')
        self.groups[g]+=1
    def identity(self,n,x,y): self.check('identities',n,Poly.cast(x)==y)
    def positive(self,g,n,p,strict=False):
        p=Poly.cast(p); bs=p.bernstein(E_MAX)
        ok=all(x>=0 for x in bs)
        if strict: ok=ok and any(x>0 for x in bs) and p(E_MAX)>0
        self.check(g,n,ok)

def run(mutation=None):
    c=Checks(); classes=[]; densities=[]
    c.identity('support exponent',2*A,F(23,25))
    c.identity('theta exponent',THETA,F(23,100))
    c.identity('principal shift',F(2,3) if mutation=='old-shift' else B,F(17,25))
    c.identity('boundary',B+THETA,F(91,100))
    c.identity('improvement',F(11,12)-(B+THETA),F(1,150))
    c.identity('excluded width ratio',(1-B-THETA)/F(1,12),F(27,25))
    c.check('domains','subcritical positive support',0<2*A<1)
    # Entire dyadic cone: compare exponents at p=log_Z P,d=log_Z D.
    for M in [F(1,4),F(23,25),F(1),F(3,2)]:
        for j in range(5):
            p=M*j/4; d=M-p
            exponents=[p/2+d,3*p/2+2*d-1]
            bound=max(M,2*M-1)
            if mutation=='drop-diagonal': bound=2*M-1
            c.check('dyadic-envelope',f'{M},{j}',max(exponents)<=bound)
    # Full local beta sums, using Q=r^2 so every certificate is rational.
    for r in [5,7,13,17]:
        Q=F(r*r); K=5
        s0=1+(1+1/F(r))/(1-1/Q)
        # Q^(-5/2)=r^(-5). Avoid floating exponents entirely.
        s1=1+(F(1,r)+Q**-2)/(1-F(1,r**5))
        truncated0=F(1); truncated1=F(1)
        for k in range(K+1):
            beta=Q**(-k)
            if mutation=='wrong-beta' and k==0: beta=Q**-1
            truncated0+=beta; truncated1+=beta*F(1,r**(1+3*k))
        for k in range(1,K+1):
            beta=F(r)*Q**(-k)
            truncated0+=beta; truncated1+=beta*F(1,r**(3*k))
        tail0=(Q**(-(K+1))+F(r)*Q**(-(K+1)))/(1-Q**-1)
        tail1=(F(1,r)*F(1,r**5)**(K+1)+F(r)*F(1,r**5)**(K+1))/(1-F(1,r**5))
        c.identity(f'local S0 {r}',truncated0+tail0,s0)
        c.identity(f'local S1 {r}',truncated1+tail1,s1)
        c.identity(f'f-weight {r}',1+Q*s1,Q*(1/Q+s1))
    for exps in itertools.product([0,2,3,4],repeat=3):
        qh=1; rad=1
        for p,k in zip([13,37,61],exps):
            qh*=p**k
            if k: rad*=p
        c.check('powerful-radical',str(exps),rad*rad<=qh)
    # T<1: at C=1 the envelope is T^Adecay, not zero.
    # Choose T=(1/2)^8 so T^(1/8) is rational as well.
    T=F(1,256); decay=3; value=T**decay
    model=0 if mutation=='delete-subunit-profile' else value
    c.check('profile-tail','retain C=1 when T<1',model==value and value>0)
    for rpow in [F(1,8),F(5,8)]:
        c.check('profile-tail',f'convergent dyadic powers {rpow}',0<rpow<decay)
    # All 10 monomials in DF's detector for every threshold.
    for j,s in enumerate(THRESHOLDS):
        aa,bb,z,g,height=density(s)
        c.check('density',f'{j} ordering',F(2,3)<s<1 and (j==0 or THRESHOLDS[j-1]<s))
        c.check('density',f'{j} parameters',0<=aa<=bb)
        c.check('density',f'{j} closed formula',g==closed_g(s))
        first=[aa,F(1),aa/3+F(5,6),5*aa/6+F(1,3)]
        terms=[(F(1,2)+(F(1,2)-s)*bb+t/2,(F(1,2)-s)*z+F(1,4)) for t in first]
        terms += [((2-2*s)*bb,(2-2*s)*z),(1+(1-2*s)*aa,F(0))]
        for base,k in [(F(1,3),F(11,6)-2*s),(F(5,6),F(4,3)-2*s)]:
            terms.extend([(base+k*aa,F(0)),(base+k*bb,k*z)])
        for i,(u,v) in enumerate(terms):
            c.check('density',f'{j} norm {i}',u<=g)
            c.check('density',f'{j} height {i}',v<=height)
        densities.append({'sigma':str(s),'A_power':str(aa),'B_power':str(bb),
                          'B_height_over_degree':str(z),'g':str(g),'extra_height_over_degree':str(height)})
        R=2-s-e/4; ro=2-s-e/2; rt=2-s-e; ri=1-e/4
        for name,p in [('R-ro',R-ro),('ro-rt',ro-rt),('rt-ri',rt-ri),('ri',ri)]:
            c.positive('reciprocal-disks',f'{j} {name}',p,True)
    vertices=[(1+e,1+e,Z0)]
    def add_class(name,x,y,nu,method,lower=None,upper=None):
        if method=='mean':
            row=(nu+1)/2-Z0
            if mutation=='individual-numerator' and name=='good': row=nu+(1-y)/2-Z0
        else: row=nu+(1-y)/2-Z0
        growth=scale(x,y,Z0)+(H+e)*row
        c.positive('row-powers',name,row,True)
        c.positive('central-budgets',name,THETA+3*e-growth,True)
        vertices.extend([(x,1+e,Z0),(x,y,Z0)])
        classes.append({'class':name,'lower_count_threshold':None if lower is None else str(lower),
                        'upper_shift_threshold':None if upper is None else str(upper),
                        'method':method,'x':Poly.cast(x).strings(),'y':Poly.cast(y).strings(),
                        'nu':Poly.cast(nu).strings(),'row_power':Poly.cast(row).strings(),
                        'growth':growth.strings(),'constant_margin':str(THETA-growth(0))})
        return growth
    good=add_class('good',THRESHOLDS[0]+e,F(1,2),F(1),'mean',upper=THRESHOLDS[0])
    c.identity('good growth',good,Poly(F(23,100),F(8,5)))
    for j,(lo,hi) in enumerate(zip(THRESHOLDS,THRESHOLDS[1:])):
        count_at=hi if mutation=='upper-count' else lo
        # The gate verifies the actual lower-count/upper-shift construction.
        c.check('partition',f'count of middle {j}',count_at==lo)
        method='mean' if j<5 else 'convexity'
        y=F(1,2) if method=='mean' else 1-hi+e
        middle=add_class(f'middle-{j}',hi+e,y,density(count_at)[3]+e,method,lo,hi)
        c.check('middle-coefficients',f'{j} constant',middle.a[0]<THETA)
        c.check('middle-coefficients',f'{j} linear',middle.a[1]<F(5,2))
        c.check('middle-coefficients',f'{j} quadratic',middle.a[2]==F(1,2))
    add_class('last',1+e,e,density(THRESHOLDS[-1])[3]+e,'convexity',THRESHOLDS[-1])
    c.check('partition','complete class count',len(classes)==22)
    # Every possible largest-threshold class has exactly one destination.
    for depth in range(-1,len(THRESHOLDS)):
        Esets=[depth>=j for j in range(len(THRESHOLDS))]
        membership=[not Esets[0]]+[Esets[j] and not Esets[j+1] for j in range(len(Esets)-1)]+[Esets[-1]]
        c.check('partition',f'nested pattern {depth}',sum(membership)==1)
    # Principal contours stay to the RIGHT of 1 in xi: no input QRH is needed.
    principal_w=scale(1+e,F(1,2),F(1,6)+e)
    principal_z=scale(1+e,1,e)
    small=scale(1+e,F(1,2),Z0)+F(1,100)*(1+F(1,4)-Z0)
    large=A/2+3+3*A+H-10-e
    c.identity('principal w',principal_w,Poly(F(9,100),F(77,50)))
    c.identity('principal z',principal_z,Poly(F(23,100),F(77,50)))
    c.identity('small rows',small,Poly(F(449,2000),1))
    c.identity('large rows',large,Poly(-F(97,20),-1))
    eL=10+2*e
    cleared=e*(A/2+3+3*A)+H*eL+(H+e)*(e-eL)
    c.identity('large-line denominator cleared',cleared,e*large)
    for name,v in [('principal-w',principal_w),('principal-z',principal_z),('small',small),('large',large)]:
        c.positive('other-budgets',name,THETA+3*e-v,True)
    gap=0 if mutation=='zero-tail-gap' else e
    c.positive('large-tail','strict cutoff gap',gap,True)
    c.positive('large-tail','cutoff < .55',F(55,100)-(H+e),True)
    vertices += [(1+e,1+e,F(1,6)+e),(1+e,F(1,2),F(1,6)+e),
                 (1+e,1,F(1,6)+e),(1+e,1,e),(1+e,F(1,2),Z0),(4,4,2)]
    for i,v in enumerate(vertices):
        for j,p in enumerate(domain(*v)): c.positive('contour-domains',f'{i}/{j}',p,True)
    c.identity('Mellin loss',B+THETA+4*e,Poly(F(91,100),4))
    return {'status':'FINITE BOOKKEEPING ONLY; analytic proof requires independent review',
            'parameter_interval':{'e_min':'0 (excluded)','e_max':str(E_MAX)},
            'exact_predicates':sum(c.groups.values()),'groups':dict(sorted(c.groups.items())),
            'a':str(A),'support':str(2*A),'b':str(B),'theta':str(THETA),
            'proposed_boundary':str(B+THETA),'thresholds':densities,'classes':classes}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation',choices=MUTATIONS)
    parser.add_argument('--details',action='store_true',help='Print all exact density and class coefficients')
    args=parser.parse_args()
    report=run(args.mutation)
    if not args.details:
        report['threshold_count']=len(report.pop('thresholds'))
        rows=report.pop('classes')
        report['class_count']=len(rows)
        report['smallest_middle_constant_margin']=str(min(F(r['constant_margin']) for r in rows if r['class'].startswith('middle')))
    print(json.dumps(report,indent=2,sort_keys=True))
