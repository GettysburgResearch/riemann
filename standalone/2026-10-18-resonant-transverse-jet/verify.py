#!/usr/bin/env python3
"""Exact rational and Gaussian-rational regression checks, not an analytic proof."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import json
import math

@dataclass(frozen=True)
class QI:
    re: F = F(0)
    im: F = F(0)
    @staticmethod
    def of(x):
        return x if isinstance(x, QI) else QI(F(x))
    def __add__(self, other):
        b=self.of(other); return QI(self.re+b.re,self.im+b.im)
    __radd__=__add__
    def __neg__(self): return QI(-self.re,-self.im)
    def __sub__(self, other): return self+-self.of(other)
    def __rsub__(self, other): return self.of(other)+-self
    def __mul__(self, other):
        b=self.of(other); return QI(self.re*b.re-self.im*b.im,self.re*b.im+self.im*b.re)
    __rmul__=__mul__
    def __truediv__(self, other):
        b=self.of(other); n=b.re*b.re+b.im*b.im
        if not n: raise ZeroDivisionError('QI division by zero')
        return self*QI(b.re/n,-b.im/n)
    def __rtruediv__(self, other): return self.of(other)/self
    def __pow__(self, n: int):
        if n<0: return (QI.of(1)/self)**(-n)
        out=QI.of(1); base=self
        while n:
            if n&1: out=out*base
            base=base*base; n//=2
        return out
    def norm2(self): return self.re*self.re+self.im*self.im

ONE=QI.of(1)
PHASES=(ONE,-ONE,QI(F(0),F(1)),QI(F(0),F(-1)))

def raw_h(q,d,W,v,E):
    r=F(1,q)
    f=1/(1-v)+W/(1-W)+E/(1-E)*((1-r)/(1-v)+W)-d/(1-E)*(1+(q-1)*W*v/(1-v))
    return (1-v)*(1-W)*f/(1-d)

def numerator(q,d,W,v,E):
    return 1-d+d*W+v*(d*W**2*(q-1)-d*W*q+d-W)+E*(W**2*v-W**2+W/q-F(1,q))

def poly_mul(a,b,cap=3):
    out=[F(0)]*(cap+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=cap: out[i+j]+=x*y
    return out

class Checks:
    def __init__(self): self.counts={}
    def eq(self, name, a,b):
        self.counts[name]=self.counts.get(name,0)+1
        if a!=b: raise RuntimeError(f'{name}: exact equality failed')
    def yes(self,name, p): self.eq(name,bool(p),True)

def run(mutation=None):
    c=Checks()
    for q in (7,13,25,49):
        for rad in (F(1,3),F(1,2),F(2,3)):
            for phase in PHASES:
                d=rad*phase
                for W in (F(1,4)*ONE,F(1,3)*PHASES[2]):
                    for v,E in ((F(1,101)*ONE,F(1,127)*PHASES[2]),(QI(),QI())):
                        h=raw_h(q,d,W,v,E)
                        n=numerator(q,d,W,v,E)
                        c.eq('raw_to_polynomial',h,n/((1-E)*(1-d)))
                        hb=raw_h(q,d,W,QI(),QI())
                        k=(1-d*W)*hb if mutation!='wrong_zeta_direction' else (1+d*W)*hb
                        c.eq('mixed_cancellation',k-1,d**2*W*(1-W)/(1-d))
    for q in (7,13,25,49):
        for rad in (F(1,3),F(1,2),F(2,3)):
            for phase in PHASES:
                d=rad*phase; W=1/(q*d); v=F(1,q**12)*ONE
                for b in PHASES+(QI(),):
                    E=q**4*d**6*v*b
                    n=numerator(q,d,W,v,E)
                    n0=1-d+F(1,q)
                    R=v*(d-1-W/q)+E*(-W**2+W/q-F(1,q)+W**2*v)
                    if mutation=='lost_phase_relation': W=F(1,q)*ONE
                    c.eq('resonant_unit_relation',d*W,QI.of(F(1,q)))
                    c.eq('resonant_numerator',n,n0+R)
                    # A transverse derivative holds d fixed; a total derivative does not.
                    partial= -d**2*W*(1-2*W)/(1-d)
                    product_rule=d*W*(1+d*W/(1-d))-(1-d*W)*d*W/(1-d)
                    if mutation=='wrong_derivative_direction':
                        product_rule=-(1-F(1,q))*F(1,q)*d/(1-d)**2
                    c.eq('transverse_not_tangent',partial,product_rule)
                    rho=2*F(1,q**5)+F(1,q**6)+2*F(1,q**3)+F(1,q**2)+F(1,q**9)
                    c.yes('nonvanishing_fixture',R.norm2()<rho*rho*n0.norm2())
                    kp=(1-F(1,q))*n/((1-E)*(1-d))
                    c.yes('local_lower_fixture',kp.norm2()>F(9,16))
    rho7=2*F(1,7**5)+F(1,7**6)+2*F(1,7**3)+F(1,7**2)+F(1,7**9)
    c.eq('exact_margin',rho7,F(1063987,40353607))
    c.yes('exact_margin',rho7<F(1,32))
    c.yes('exact_margin',F(6,7)*F(31,32)/F(50,49)>F(3,4))
    # Taylor ratio of Q(x) = x^m (1+a*x). Roots are synthetic, not zeta data.
    for m in range(1,13):
        for x in (F(1,5),F(-1,3),F(2,7)):
            for a in (F(0),F(1,4),F(-1,5)):
                ratio=[F(math.comb(m,j))*(-1/x)**j if j<=m else F(0) for j in range(4)]
                ratio=poly_mul(ratio,[F(1),-a/(1+a*x)])
                qp=F(m)/x+a/(1+a*x)
                c.eq('ratio_derivative',ratio[1],-qp)
                k0,k1,delta0,delta1,kappa,gamma=map(F,(2,3,5,7,11,13))
                # Delta(s-t), K(s,1-s+t), and Q(s-t)/Q(s) are assembled separately.
                delta=[delta0,-delta1 if mutation!='wrong_fe_sign' else delta1]
                plain=poly_mul(poly_mul([k0,k1],delta),ratio)
                residue=kappa*plain[0]
                finite=gamma*plain[0]+kappa*plain[1]
                expected=delta0*(gamma*k0+kappa*k1)-kappa*delta1*k0-kappa*delta0*k0*qp
                c.eq('finite_part_formula',finite,expected)
                jet=finite/residue-gamma/kappa-k1/k0+delta1/delta0
                if mutation=='delete_normal_derivative': jet=F(0)
                c.eq('compensated_jet',jet,-qp)
                residue_weight=-(F(1) if mutation=='lose_multiplicity' else F(m))
                c.eq('multiplicity_weight',residue_weight,-F(m))
    # Restriction to t=0 is identical with or without a synthetic zero.
    for m in range(1,9):
        ratio=[F(math.comb(m,j))*(-F(5))**j if j<=m else F(0) for j in range(2)]
        c.eq('residue_blindness',ratio[0],F(1))
        c.yes('transverse_visibility',ratio[1]!=0)
    return {
        'status':'PASS',
        'scope':'exact finite algebra; no analytic, theta-source, or RH certification',
        'counts':c.counts,
        'total_predicates':sum(c.counts.values()),
        'exact_uniform_local_margin':str(rho7),
        'roots_are_synthetic':True,
        'new_zero_free_bound_proved':False,
        'independent_mathematical_review':False,
    }

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--mutation',choices=('wrong_zeta_direction','lost_phase_relation','wrong_fe_sign','delete_normal_derivative','lose_multiplicity','wrong_derivative_direction'))
    args=ap.parse_args()
    print(json.dumps(run(args.mutation),indent=2,sort_keys=True))
