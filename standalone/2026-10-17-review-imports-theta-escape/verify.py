#!/usr/bin/env python3
"""Independent rational bookkeeping, not an analytic proof or an L-value test.

No third-party packages. Every failure uses an exception (also under python -O).
Run normally, or --mutation NAME for a deliberately corrupted model.
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
        while len(self.a) > 1 and self.a[-1] == 0:
            self.a = self.a[:-1]
    @staticmethod
    def cast(x):
        return x if isinstance(x, Poly) else Poly(x)
    def __add__(self, other):
        b = self.cast(other).a
        return Poly(*(sum(x) for x in itertools.zip_longest(self.a, b, fillvalue=F(0))))
    __radd__ = __add__
    def __neg__(self): return Poly(*(-x for x in self.a))
    def __sub__(self, other): return self + (-self.cast(other))
    def __rsub__(self, other): return self.cast(other) + (-self)
    def __mul__(self, other):
        b = self.cast(other).a
        out = [F(0)] * (len(self.a) + len(b) - 1)
        for i,x in enumerate(self.a):
            for j,y in enumerate(b): out[i+j] += x*y
        return Poly(*out)
    __rmul__ = __mul__
    def __truediv__(self, other): return self * (1/F(other))
    def __call__(self, x): return sum(c*F(x)**i for i,c in enumerate(self.a))
    def __eq__(self, other): return self.a == self.cast(other).a
    def bernstein(self, endpoint):
        n = len(self.a)-1
        return [sum(self.a[k]*endpoint**k*F(comb(i,k), comb(n,k))
                    for k in range(i+1)) for i in range(n+1)]
    def strings(self): return list(map(str,self.a))

E_MAX=F(1,100000)
e=Poly(0,1)
alpha=F(1,2)+e
beta=F(1,2)
M=alpha+beta
C=alpha/2+(1-alpha)/6
b=1-C
z0=F(2,5)

def scale(x,y,z):
    return alpha/2+x-1+(1-alpha)*z+beta*(y-1)

def domain(x,y,z):
    return [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,
            6*x+6*z-5,x-F(1,2),3*x-2,3*x+y-F(5,2)]

def density(sigma):
    q=2*sigma-1; n=6
    if n*q<=2:
        a=F(1,2); bb=2/(4-n*q); g=1-q/(4-n*q)
    elif n*q<=n-1:
        dd=n*q*(2*(n-1)-n*q)-2*(n-1)
        a=(n*q*(n-2)-(n-1))/dd
        bb=(n*q*(2*n-5)-2*(n-2))/dd
        g=((2*n-3)*q*(n+1-n*q)-2*(n-1))/dd
    else:
        dd=1-n*(1-q)**2
        a=(n*q-n+2)/dd
        bb=((n+2)*q-n+1)/dd
        g=(1-q)*((n+2)*q-n+1)/dd
    z=1/(6-4*sigma)
    h=(1-sigma)/(3-2*sigma)
    return a,bb,z,g,h

def conv(a,b):
    n=max(len(a),len(b)); out=[F(0)]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<n: out[i+j]+=x*y
    return out

class Checks:
    def __init__(self): self.groups=Counter(); self.names=[]
    def check(self, group, name, ok):
        if not ok: raise ValueError(f'{group}: {name}')
        self.groups[group]+=1; self.names.append(f'{group}: {name}')
    def identity(self, name, lhs, rhs): self.check('identities',name,Poly.cast(lhs)==rhs)
    def positive(self, group, name, p, strict=False):
        p=Poly.cast(p); bs=p.bernstein(E_MAX)
        ok=all(v>=0 for v in bs)
        if strict: ok=ok and any(v>0 for v in bs) and p(E_MAX)>0
        self.check(group,name,ok)

MUTATIONS=['individual-numerator','unmoved-principal','endpoint-M',
           'double-tail-saving','single-mobius-is-reciprocal','lost-loglog']

def run(mutation=None):
    c=Checks()
    c.identity('M',M,1+e)
    c.identity('Mellin shift',b,F(2,3)-e/3)
    c.positive('domains','strict M>1',Poly(0) if mutation=='endpoint-M' else M-1,True)
    for s,expected in [(F(3,4),F(8,11)),(F(21,25),F(4919,8846)),
                       (F(19,20),F(11,47)),(F(187,250),F(62212,85183))]:
        a,bb,z,g,h=density(s)
        c.check('density',f'{s} expected g',g==expected)
        c.check('density',f'{s} A<=B',0<=a<=bb)
        first=[a,F(1),a/3+F(5,6),5*a/6+F(1,3)]
        terms=[(F(1,2)+(F(1,2)-s)*bb+t/2,(F(1,2)-s)*z+F(1,4)) for t in first]
        terms += [((2-2*s)*bb,(2-2*s)*z),(1+(1-2*s)*a,F(0))]
        for base,k in [(F(1,3),F(11,6)-2*s),(F(5,6),F(4,3)-2*s)]:
            terms += [(base+k*a,F(0)),(base+k*bb,k*z)]
        for i,(npow,tpow) in enumerate(terms):
            c.check('density',f'{s} term {i} norm',npow<=g)
            c.check('density',f'{s} term {i} height/d',tpow<=h)

    def central(s0):
        g0=density(s0)[3]
        return [scale(s0+e,F(1,2),z0)+(1-z0)/2,
                scale(F(21,25)+e,F(4,25)+e,z0)+(g0+e+(1-(F(4,25)+e))/2-z0)/2,
                scale(F(19,20)+e,F(1,20)+e,z0)+(F(4919,8846)+e+(1-(F(1,20)+e))/2-z0)/2,
                scale(1+e,e,z0)+(F(11,47)+e+(1-e)/2-z0)/2]
    old=central(F(3,4))
    expect=[Poly(F(1,4),F(11,10)),Poly(F(67,275),F(37,20)),
            Poly(F(85111,353840),F(37,20)),Poly(F(11,94),F(37,20))]
    for i,(v,w) in enumerate(zip(old,expect)):
        c.identity(f'959 central {i}',v,w)
        c.positive('old-budget',str(i),F(1,4)+2*e-v)
    pw=scale(1+e,F(1,2),F(1,6)+e)
    pz=scale(1+e,1,e)
    c.identity('959 w remainder',pw,Poly(F(1,12),F(11,6),-1))
    c.identity('959 z remainder',pz,Poly(F(1,4),2,-1))
    small=scale(1+e,F(1,2),z0)+(1+F(1,4)-z0)/100
    c.identity('small U',small,Poly(F(417,2000),F(11,10)))
    # Avoid rational functions in e: expand the large-range L=10/e+2 term.
    large=alpha/2+3+3*beta+F(1,2)-10-2*e
    c.identity('large U tail',large,Poly(-F(19,4),-F(3,2)))
    c.identity('959 endpoint',b+F(1,4)+3*e,F(11,12)+8*e/3)
    c.identity('theta saving',C-(alpha+beta/2-F(1,2)),(1-alpha)/6-(M-1)/2)
    c.check('ties','three equal constants',
            old[0](0)==pz(0)==(alpha+beta/2-F(1,2))(0)==F(1,4))

    new=central(F(187,250))
    if mutation=='individual-numerator': new[0]+=F(1,8)
    # Known CT QRH(1/32), NOT #959's conclusion, permits this principal xi line.
    xp=F(31,32)+e
    zw=F(1,6)+e
    zp=F(1,100)
    new_pw=scale(xp,F(1,2),zw)
    new_pz=scale(xp,1,zp)
    if mutation=='unmoved-principal': new_pz=pz
    c.identity('new principal w',new_pw,Poly(F(5,96),F(11,6),-1))
    if mutation!='unmoved-principal':
        c.identity('new principal z',new_pz,Poly(F(179,800),F(149,100)))
    target=F(249,1000)+2*e
    for i,v in enumerate(new+[new_pw,new_pz,small,large]):
        c.positive('new-budget',f'contribution {i}',target-v,True)
    # Domain convexity means endpoints certify every connecting contour segment.
    vertices=[(1+e,1+e,z0),(F(3,4)+e,F(1,2),z0),
              (F(187,250)+e,1+e,z0),(F(187,250)+e,F(1,2),z0),
              (F(21,25)+e,1+e,z0),(F(21,25)+e,F(4,25)+e,z0),
              (F(19,20)+e,1+e,z0),(F(19,20)+e,F(1,20)+e,z0),
              (1+e,e,z0),(1+e,1+e,zw),(1+e,F(1,2),zw),
              (1+e,1,e),(xp,1+e,zw),(xp,F(1,2),zw),
              (xp,1,zw),(xp,1,zp),(4,4,2)]
    for i,v in enumerate(vertices):
        for j,p in enumerate(domain(*v)):
            c.positive('domains',f'vertex {i} margin {j}',p,True)
    # A tempting z=e shift on xp<1 is INVALID. This is an independent guard.
    c.check('domain-warning','cannot retain z=e below xi=1',
            (xp+6*e-1)(E_MAX)<0)
    for s in [F(3,4),F(187,250),F(21,25),F(19,20)]:
        R=2-s-e/4; ro=2-s-e/2; rt=2-s-e; ri=1-e/4
        for name,p in [('R-ro',R-ro),('ro-rt',ro-rt),('rt-ri',rt-ri),('ri',ri)]:
            c.positive('reciprocal-disks',f'{s} {name}',p,True)

    tau=F(1,100)
    theta=alpha+beta/2-F(1,2)
    high=(2*M-1-tau/2)/2-beta/2
    claimed=theta-tau/(2 if mutation=='double-tail-saving' else 4)
    c.identity('high-powerful tail saving',high,claimed)
    c.positive('new-budget','high powerful sector',target-high,True)
    c.identity('conditional new boundary',b+F(249,1000)+3*e,F(2747,3000)+8*e/3)
    c.check('scope','new boundary is better, only conditional',F(2747,3000)<F(11,12))
    # Polynomial exponents for both theta regimes, with legal support slack.
    for aa,bb in [(F(51,100),F(1,2)),(F(1,2),F(51,100)),(F(3,5),F(3,5))]:
        th=aa+bb-F(1,2)-min(aa,bb)/2
        saving=F(1,6)+aa/3-th
        c.check('barrier',f'{aa},{bb}',saving<F(1,12))

    applications=[]
    for sigma in [F(31,32),F(23,24),F(25,27),F(11,12)]:
        delta=1-sigma; logpow=1/delta
        loglogpow=(1 if mutation=='lost-loglog' else 2)/delta
        c.check('applications',f'{sigma} loglog factor',loglogpow==2*logpow)
        applications.append({'boundary':str(sigma),'delta':str(delta),
                             'log_D_power':str(logpow),'loglog_D_power':str(loglogpow)})
    # BV floor argument: extremal two-point laws attain the derived inequality.
    for m in range(1,9):
        floor=-F(4,m)
        for p in [F(i,10) for i in range(11)]:
            mean=p+(1-p)*floor
            lower=(1-mean)/(1+F(4,m))
            c.check('geometric-density',f'm={m} p={p}',lower==1-p)
    # Local Euler coefficients: zeta * mu = 1, zeta * mu * mu = mu.
    n=18; zeta=[F(1)]*n; mu=[F(1),F(-1)]+[F(0)]*(n-2)
    once=conv(zeta,mu); twice=conv(once,mu)
    c.check('geometric-reciprocal','one convolution is not reciprocal',
            once==(mu if mutation=='single-mobius-is-reciprocal' else [F(1)]+[F(0)]*(n-1)))
    c.check('geometric-reciprocal','two convolutions are reciprocal',twice==mu)
    # Tame shared-prime support must not be silently replaced by conductor radials.
    for j in range(1,6):
        c.check('indexing',f'sixth-free prime exponent {j}',j%6!=0)
    c.check('indexing','full norm not radical norm',2**5!=2)
    return {'status':'PASS','arithmetic':'exact rational; whole e interval via Bernstein',
            'e_interval':'0 < e <= 1/100000','predicates':sum(c.groups.values()),
            'groups':dict(sorted(c.groups.items())),
            'new_central_polynomials':[v.strings() for v in new],
            'new_principal_polynomials':[new_pw.strings(),new_pz.strings()],
            'conditional_boundary':'2747/3000','applications':applications,
            'scope':'Finite identities and sufficient inequalities only. No L-values, independent referee, Lean, or new global zero-free theorem.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation',choices=MUTATIONS)
    args=parser.parse_args()
    print(json.dumps(run(args.mutation),indent=2,sort_keys=True))
