#!/usr/bin/env python3
"""Exact finite checks, NOT certification of any analytic theorem.

No floating optimization is used for acceptance. Every epsilon inequality is
checked by rational Bernstein coefficients over the full declared interval.
Phase fixtures are finite residue products, not the CT family or an L-value census.
"""
from __future__ import annotations
import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
MUTATIONS = ('old-mean','squarefree-only','drop-sixth-mask','extra-coprimality',
             'upper-count','old-shift','omit-last','zero-tail-gap')

class P:
    def __init__(self, *cs):
        a = list(map(F, cs or (0,)))
        while len(a)>1 and not a[-1]: a.pop()
        self.a = tuple(a)
    @staticmethod
    def cast(x): return x if isinstance(x,P) else P(x)
    def __add__(self,y):
        y=P.cast(y)
        return P(*(a+b for a,b in itertools.zip_longest(self.a,y.a,fillvalue=F(0))))
    __radd__=__add__
    def __neg__(self): return P(*(-a for a in self.a))
    def __sub__(self,y): return self+-P.cast(y)
    def __rsub__(self,y): return P.cast(y)+-self
    def __mul__(self,y):
        y=P.cast(y); c=[F(0)]*(len(self.a)+len(y.a)-1)
        for i,a in enumerate(self.a):
            for j,b in enumerate(y.a): c[i+j]+=a*b
        return P(*c)
    __rmul__=__mul__
    def __truediv__(self,y): return self*(1/F(y))
    def __call__(self,x): return sum(a*F(x)**i for i,a in enumerate(self.a))
    def bernstein(self,end):
        n=len(self.a)-1
        return [sum(self.a[j]*end**j*F(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
    def strings(self): return list(map(str,self.a))

class Check:
    def __init__(self): self.count=Counter()
    def test(self,group,name,ok):
        if not ok: raise ValueError(f'{group}: {name}')
        self.count[group]+=1
    def eq(self,group,name,x,y): self.test(group,name,P.cast(x).a==P.cast(y).a)
    def pos(self,group,name,p,end,strict=False):
        bs=P.cast(p).bernstein(end)
        # Nonnegative Bernstein coefficients, and not the zero polynomial,
        # imply strict positivity at every 0<epsilon<=end.
        self.test(group,name,all(c>=0 for c in bs) and (not strict or any(c>0 for c in bs)))

# Specialized DF detector parameters. Credited to the exact #965 source.
def density(s):
    q=2*s-1; n=6
    if n*q<=2:
        aa=F(1,2); bb=2/(4-n*q); g=1-q/(4-n*q)
    elif n*q<=n-1:
        den=n*q*(2*(n-1)-n*q)-2*(n-1)
        aa=(n*q*(n-2)-(n-1))/den
        bb=(n*q*(2*n-5)-2*(n-2))/den
        g=((2*n-3)*q*(n+1-n*q)-2*(n-1))/den
    else:
        den=1-n*(1-q)**2
        aa=(n*q-n+2)/den; bb=((n+2)*q-n+1)/den
        g=(1-q)*((n+2)*q-n+1)/den
    return aa,bb,1/(6-4*s),g,(1-s)/(3-2*s)

def sixth_exponent(r):
    return max(F(1),F(r,2),F(5,6)+F(r,6),F(1,3)+F(5*r,12))

# Exact ring Z[omega], omega^2+omega+1=0.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def powr(x,n):
    y=(1,0)
    while n:
        if n&1: y=mul(y,x)
        x=mul(x,x); n//=2
    return y

def root_table(p,g):
    t={0:(0,0)}
    for j in range(p-1): t[pow(g,j,p)]=powr((1,1),j%6)
    if len(t)!=p: raise ValueError('fixture generator is not primitive')
    return t

def convolution(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items(): c[(i+k,j+l)]=c.get((i+k,j+l),0)+x*y
    return {n:v for n,v in c.items() if v}

def phase_checks(c,mutation):
    # Two actual finite-field sextic residue characters; not a complete
    # number-field AFE and not a proof of a large sieve.
    tabs=[root_table(7,3),root_table(13,2)]
    base={(i,j):(-1)**(i+2*j)*(1+(i+3*j)%3) for i in (0,1,2,6,7) for j in (0,1,2)}
    powers=[{(0,0):1}]
    for r in range(1,5): powers.append(convolution(powers[-1],base))
    for u in range(91):
        x,y=tabs[0][u%7],tabs[1][u%13]
        raw=(0,0)
        for (i,j),v in base.items():
            z=mul(powr(x,i),powr(y,j));raw=add(raw,(v*z[0],v*z[1]))
        for r in range(1,5):
            direct=(0,0); grouped=(0,0)
            for (i,j),v in powers[r].items():
                z=mul(powr(x,i),powr(y,j)); direct=add(direct,(v*z[0],v*z[1]))
                ci,di=i%6,i//6; cj,dj=j%6,j//6
                if mutation=='squarefree-only' and (ci>1 or cj>1): continue
                if mutation=='extra-coprimality' and ((ci and di) or (cj and dj)): continue
                mask=not ((di and u%7==0) or (dj and u%13==0))
                if mutation=='drop-sixth-mask': mask=True
                z=mul(powr(x,ci),powr(y,cj)) if mask else (0,0)
                grouped=add(grouped,(v*z[0],v*z[1]))
            c.test('phase-power',f'{u}/{r}',direct==powr(raw,r))
            c.test('sixth-power-mask',f'{u}/{r}',grouped==direct)
    for q in (7,13,19,25):
        for d in range(1,8):
            c.test('critical-sixth-weight',f'{q}/{d}',F(1,q**(6*d))==F(1,q**(3*d))**2)


def run(mutation=None):
    dat=json.loads((HERE/'PARAMETERS.json').read_text())
    a=F(dat['scale']); h=1-a; t=a/2; b=1-(a/2+h/6)
    z=F(dat['z']); small=F(dat['small_cutoff']); end=F(dat['epsilon_max']); e=P(0,1)
    th=list(map(F,dat['thresholds'])); methods=dat['methods']; c=Check()
    c.eq('normalization','support',2*a,F(10,11))
    c.eq('normalization','theta',t,F(5,22))
    b_used=F(17,25) if mutation=='old-shift' else b
    c.eq('normalization','Mellin shift',b_used,F(15,22))
    c.eq('normalization','new boundary',b_used+t,F(10,11))
    c.eq('normalization','gain on 91/100',F(91,100)-b-t,F(1,1100))
    c.test('normalization','subcritical',0<2*a<1)
    for r in range(1,17):
        kap=sixth_exponent(r)
        expected=F(1) if r==1 else F(7,6) if r==2 else F(19,12) if r==3 else F(r,2)
        c.eq('numerator-moments',f'order {2*r}',kap,expected)
    # The fourth moment is for numerator L-values, not inverse-Mobius sums.
    c.eq('numerator-moments','subset fourth slope',F(1)-F(1,4),F(3,4))
    c.eq('numerator-moments','subset fourth constant',sixth_exponent(2)/4,F(7,24))
    c.eq('numerator-moments','gain over second at nu=2/3',(F(2,3)+1)/2-(3*F(2,3)/4+F(7,24)),F(1,24))
    for M in [F(1,4),2*a,F(1),F(3,2)]:
        for p in (F(0),M/3,2*M/3,M):
            d=M-p
            c.test('reflected-cone',f'{M}/{p}',max(p/2+d,3*p/2+2*d-1)<=max(M,2*M-1))
    densities=[]
    for j,s in enumerate(th):
        aa,bb,zz,g,ht=density(s)
        c.test('density-domain',f'{j}',F(2,3)<s<1 and (not j or th[j-1]<s) and 0<=aa<=bb)
        # Complete ten monomials, no omitted supremum endpoint.
        first=[aa,F(1),aa/3+F(5,6),5*aa/6+F(1,3)]
        terms=[(F(1,2)+(F(1,2)-s)*bb+x/2,(F(1,2)-s)*zz+F(1,4)) for x in first]
        terms += [((2-2*s)*bb,(2-2*s)*zz),(1+(1-2*s)*aa,F(0))]
        for base,k in ((F(1,3),F(11,6)-2*s),(F(5,6),F(4,3)-2*s)):
            terms += [(base+k*aa,F(0)),(base+k*bb,k*zz)]
        for i,(norm,height) in enumerate(terms):
            c.test('density-monomials',f'{j}/{i}/norm',norm<=g)
            c.test('density-monomials',f'{j}/{i}/height',height<=ht)
        densities.append({'sigma':str(s),'g':str(g),'A':str(aa),'B':str(bb),'B_height_per_degree':str(zz),'extra_height_per_degree':str(ht)})
        R=2-s-e/4; ro=2-s-e/2; rt=2-s-e; ri=1-e/4
        for nm,p in [('R-ro',R-ro),('ro-rt',ro-rt),('rt-ri',rt-ri),('ri',ri)]: c.pos('reciprocal-disks',f'{j}/{nm}',p,end,True)
    def E(x,y,z1): return a/2+x-1+h*z1+a*(y-1)
    def domain(x,y,z1):
        return [x,y,z1,6*z1+y-1,x+6*z1-1,x+y-1,x+y+6*z1-2,6*x+6*z1-5,x-F(1,2),3*x-2,3*x+y-F(5,2)]
    vertices=[(1+e,1+e,z)]; classes=[]
    def add_class(name,x,y,nu,method,lo=None,hi=None):
        if method=='M2': row=(nu+1)/2-z
        elif method=='M4': row=3*nu/4+F(7,24)-z
        elif method=='CV': row=nu+(1-y)/2-z
        else: raise ValueError('unknown method')
        grow=E(x,y,z)+(h+e)*row
        c.pos('row-powers',name,row,end,True)
        c.pos('class-budgets',name,t+3*e-grow,end,True)
        vertices.extend([(x,1+e,z),(x,y,z)])
        classes.append({'name':name,'lower':None if lo is None else str(lo),'upper':None if hi is None else str(hi),'method':method,'x':P.cast(x).strings(),'y':P.cast(y).strings(),'nu':P.cast(nu).strings(),'row_power':row.strings(),'growth':grow.strings(),'margin_at_zero':str(t-grow(0))})
        return grow
    good=add_class('good',th[0]+e,F(1,2),P(1),'M2',hi=th[0])
    c.eq('exact-exponents','good',good,P(F(5,22),F(8,5)))
    for j,(lo,hi,method) in enumerate(zip(th,th[1:],methods)):
        ct=hi if mutation=='upper-count' else lo
        c.test('class-partition',f'lower-count {j}',ct==lo)
        if mutation=='old-mean' and method=='M4': method='M2'
        y=1-hi+e if method=='CV' else P(F(1,2))
        grow=add_class(f'middle-{j}',hi+e,y,density(ct)[3]+e,method,lo,hi)
        c.test('class-budgets',f'strict constant middle {j}',grow(0)<t)
    if mutation!='omit-last': add_class('last',1+e,e,density(th[-1])[3]+e,'CV',lo=th[-1])
    c.test('class-partition','complete number',len(classes)==len(th)+1)
    for depth in range(-1,len(th)):
        ev=[depth>=j for j in range(len(th))]
        hits=[not ev[0]]+[ev[j] and not ev[j+1] for j in range(len(th)-1)]+[ev[-1]]
        c.test('class-partition',f'nesting depth {depth}',sum(hits)==1)
    wp=E(1+e,F(1,2),F(1,6)+e);zp=E(1+e,1,e)
    sm=E(1+e,F(1,2),z)+small*(1+F(1,4)-z)
    lg=-6+5*a/2-e
    c.eq('exact-exponents','principal w',wp,P(F(1,11),F(17,11)))
    c.eq('exact-exponents','principal z',zp,P(F(5,22),F(17,11)))
    c.eq('exact-exponents','small margin',t-sm,P(F(13,22000),-1))
    c.eq('exact-exponents','large',lg,P(-F(107,22),-1))
    eL=10+2*e
    c.eq('exact-exponents','cleared large contour',e*(a/2+3+3*a)+h*eL+(h+e)*(e-eL),e*lg)
    for nm,grow in [('principal-w',wp),('principal-z',zp),('small',sm),('large',lg)]: c.pos('other-budgets',nm,t+3*e-grow,end,True)
    c.pos('tail-gap','positive gap',0 if mutation=='zero-tail-gap' else e,end,True)
    c.pos('tail-gap','intermediate upper bound',F(55,100)-h-e,end,True)
    vertices += [(1+e,1+e,F(1,6)+e),(1+e,F(1,2),F(1,6)+e),(1+e,1,F(1,6)+e),(1+e,1,e),(1+e,F(1,2),z),(4,4,2)]
    for i,v in enumerate(vertices):
        for j,d in enumerate(domain(*v)): c.pos('contour-domain',f'{i}/{j}',d,end,True)
    phase_checks(c,mutation)
    return {'scope':'Exact finite identities and exponent bookkeeping ONLY; no analytic certification or independent review.',
            'boundary':str(b+t),'epsilon_interval':f'0<e<={end}',
            'number_of_classes':len(classes),'predicates':sum(c.count.values()),'counts':dict(sorted(c.count.items())),
            'smallest_middle_margin':str(min(F(x['margin_at_zero']) for x in classes if x['name'].startswith('middle'))),
            'moment_exponents':{str(2*r):str(sixth_exponent(r)) for r in range(1,9)},
            'classes':classes,'densities':densities}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--mutation',choices=MUTATIONS)
    ap.add_argument('--summary',action='store_true');ap.add_argument('--details',action='store_true');args=ap.parse_args()
    result=run(args.mutation)
    if not args.details: result={k:v for k,v in result.items() if k not in ('classes','densities')}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': main()
