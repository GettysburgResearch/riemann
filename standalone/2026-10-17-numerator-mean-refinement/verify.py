#!/usr/bin/env python3
"""Exact finite bookkeeping only; not a verification of analytic imports.

Run: python verify.py --output CHECKS.json
     python -O verify.py
All arithmetic is Fraction/integer; checks survive python -O.
"""
from __future__ import annotations
import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction as Q
from math import comb
from pathlib import Path

COUNTS: Counter[str] = Counter()
MUTATION = "none"
EMAX = Q(1, 100000)

def need(ok: bool, kind: str, message: str) -> None:
    COUNTS[kind] += 1
    if not ok:
        raise ArithmeticError(f"{kind}: {message}")

class P:
    """Ascending coefficients of an exact rational polynomial in e."""
    def __init__(self, value=0):
        if isinstance(value, P):
            a = value.a
        elif isinstance(value, (tuple, list)):
            a = tuple(Q(x) for x in value)
        else:
            if isinstance(value, float):
                raise TypeError("floating coefficients are prohibited")
            a = (Q(value),)
        while len(a) > 1 and not a[-1]:
            a = a[:-1]
        self.a = a
    def __add__(self, other):
        b = P(other).a
        return P(tuple((self.a[i] if i<len(self.a) else 0) +
                       (b[i] if i<len(b) else 0)
                       for i in range(max(len(self.a),len(b)))))
    __radd__ = __add__
    def __neg__(self):
        return P(tuple(-x for x in self.a))
    def __sub__(self, other):
        return self + -P(other)
    def __rsub__(self, other):
        return P(other) + -self
    def __mul__(self, other):
        b = P(other).a
        a = [Q(0)]*(len(self.a)+len(b)-1)
        for i,x in enumerate(self.a):
            for j,y in enumerate(b):
                a[i+j] += x*y
        return P(a)
    __rmul__ = __mul__
    def __truediv__(self, other):
        if isinstance(other, float):
            raise TypeError("floating divisors are prohibited")
        return P(tuple(x/Q(other) for x in self.a))
    def __eq__(self, other):
        return self.a == P(other).a
    def at(self, x: Q) -> Q:
        if not isinstance(x,Q):
            raise TypeError("use Fraction parameter")
        ans=Q(0)
        for c in reversed(self.a):
            ans=ans*x+c
        return ans
    def strings(self):
        return [str(c) for c in self.a]
    def bernstein(self):
        n=len(self.a)-1
        power=[c*EMAX**i for i,c in enumerate(self.a)]
        return [sum((power[j]*Q(comb(i,j),comb(n,j))
                     for j in range(i+1)),Q(0)) for i in range(n+1)]

e=P((0,1)); alpha=Q(1,2)+e; beta=P(Q(1,2)); h=1-alpha
C=alpha/2+h/6; b=1-C; z0=Q(2,5)

def positive(poly: P, kind: str, name: str, strict: bool=False):
    bs=poly.bernstein()
    need(all(x>=0 for x in bs),kind,name+" has a negative Bernstein coefficient")
    if strict:
        # On (0,EMAX], nonnegative Bernstein coefficients and positive last
        # coefficient imply positivity, even if the value at zero is zero.
        need(bs[-1]>0,kind,name+" is not strictly positive on (0,EMAX]")
    return [str(x) for x in bs]

def exponent(x,y,z):
    return alpha/2+x-1+h*z+beta*(y-1)

def domain(x,y,z):
    return [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,
            6*x+6*z-5,x-Q(1,2),3*x-2,3*x+y-Q(5,2)]

def density(s:Q):
    q=2*s-1; n=6
    if q<=Q(2,n):
        a=Q(1,2); bb=2/(4-n*q)
    elif q<=Q(n-1,n):
        D=n*q*(2*(n-1)-n*q)-2*(n-1)
        a=(n*q*(n-2)-(n-1))/D
        bb=(n*q*(2*n-5)-2*(n-2))/D
    else:
        D=1-n*(1-q)**2
        a=(n*q-n+2)/D
        bb=((n+2)*q-n+1)/D
    zz=1/(6-4*s)
    powers=[(Q(1,2)-s)*bb+Q(1,2)+v/2
            for v in [a,Q(1),a/3+Q(5,6),5*a/6+Q(1,3)]]
    heights=[(Q(1,2)-s)*zz+Q(1,4)]*4
    powers += [(2-2*s)*bb,1+a*(1-2*s)]
    heights += [(2-2*s)*zz,Q(0)]
    for A,B in [(Q(1,3),Q(11,6)-2*s),(Q(5,6),Q(4,3)-2*s)]:
        powers += [A+B*a,A+B*bb]
        heights += [Q(0),B*zz]
    return a,bb,zz,powers,heights

def qjson(q): return str(q)

def classify_checks():
    # Synthetic nested zero-set memberships, not a real zero census.
    for labels in itertools.product(range(4),repeat=4):
        U=set(range(4))
        sets=[{i for i,l in enumerate(labels) if l>=j+1} for j in range(3)]
        classes=[U-sets[0],sets[0]-sets[1],sets[1]-sets[2],sets[2]]
        if MUTATION=="omit-good": classes[0]=set()
        need(set.union(*classes)==U and sum(map(len,classes))==len(U),
             "synthetic_partition",str(labels))
        for j in [1,2]:
            # Middle class j belongs to E_(j-1) and avoids E_j.
            idx=j if MUTATION=="wrong-bin" else j-1
            need(classes[j]<=sets[idx] and not classes[j]&sets[j],
                 "lower_count_upper_contour",str((labels,j)))

def gaussian_mul(z,w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def norm(z): return z[0]*z[0]+z[1]*z[1]
def cauchy_checks():
    atoms=[(0,0),(1,0),(-1,0),(0,1),(1,1)]
    for i,vals in enumerate(itertools.product(atoms,repeat=3)):
        coeffs=[atoms[(i+2*j+1)%len(atoms)] for j in range(3)]
        S={j for j in range(3) if (i+j)%3!=0}
        terms=[gaussian_mul(coeffs[j],vals[j]) for j in S]
        total=(sum(x[0] for x in terms),sum(x[1] for x in terms))
        rhs=sum(norm(coeffs[j]) for j in S)*sum(norm(v) for v in vals)
        uniform=len(S)*max([norm(coeffs[j]) for j in S]+[0])*sum(norm(v) for v in vals)
        need(norm(total)<=rhs<=uniform,"weighted_cauchy",str(i))

def main():
    legal_e=Q(0) if MUTATION=="endpoint-M" else EMAX
    need(legal_e>0 and (alpha+beta).at(legal_e)>1,"legal_M","M=1 is inadmissible")
    need(C==P((Q(1,3),Q(1,3))),"normalization","wrong C")
    used_b=P(Q(35,54)) if MUTATION=="old-shift" else b
    need(used_b+P((Q(1,4),3))==P((Q(11,12),Q(8,3))),
         "normalization","wrong detector/Mellin shift")
    positive(alpha-beta,"scale_domain","beta<=alpha")
    for name,p in [("alpha",alpha),("beta",beta),("h",h),("M-1",alpha+beta-1)]:
        positive(p,"scale_domain",name,True)
    expected=[(Q(3,4),Q(7,11),Q(13,11),Q(1,3),Q(8,11),Q(1,6)),
              (Q(21,25),Q(7075,8846),Q(6425,4423),Q(25,66),Q(4919,8846),Q(4,33)),
              (Q(19,20),Q(70,47),Q(110,47),Q(5,11),Q(11,47),Q(1,22))]
    densities=[]
    for s,a0,b0,z00,g,H in expected:
        a1,b1,z1,powers,heights=density(s)
        need((a1,b1,z1)==(a0,b0,z00),"density_parameters",str(s))
        need(0<=a1<=b1 and z1>=0,"density_parameters","invalid A,B")
        for i,(p,t) in enumerate(zip(powers,heights)):
            need(p<=g,"density_norm",str((s,i,p,g)))
            need(t<=H,"density_height",str((s,i,t,H)))
        need(max(powers)==g and max(heights)==H,"density_sharp_bookkeeping",str(s))
        densities.append({'sigma':str(s),'a':str(a1),'b':str(b1),'z':str(z1),
                          'g':str(g),'height_d_coefficient':str(H),
                          'norm_powers':list(map(str,powers)), 'height_powers':list(map(str,heights))})
    classes=[('good',Q(3,4)+e,P(Q(1,2)),P(1)),
             ('middle_0',Q(21,25)+e,Q(4,25)+e,Q(8,11)+e),
             ('middle_1',Q(19,20)+e,Q(1,20)+e,Q(4919,8846)+e),
             ('last',1+e,e,Q(11,47)+e)]
    start=(1+e,1+e,P(z0))
    vertices=[start,(1+e,P(Q(1,2)),P(z0)),
              (1+e,1+e,Q(1,6)+e),(1+e,P(Q(1,2)),Q(1,6)+e),
              (1+e,P(1),e)]
    for _,x,y,_ in classes:
        vertices += [(x,1+e,P(z0)),(x,y,P(z0))]
    for i,(x,y,z) in enumerate(vertices):
        for j,p in enumerate(domain(x,y,z)):
            positive(P(p),'contour_domain',str((i,j)),True)
    for s,*_ in expected:
        radii=[2-s-e/4,2-s-e/2,2-s-e,1-e/4]
        for i in range(3): positive(radii[i]-radii[i+1],'reciprocal_disks',str((s,i)),True)
        positive(radii[-1],'reciprocal_disks',str(s),True)
    rows={
        'theta':alpha+beta/2-Q(1,2),
        'principal_w':exponent(1+e,P(Q(1,2)),Q(1,6)+e),
        'principal_z':exponent(1+e,P(1),e),
        'small':exponent(1+e,P(Q(1,2)),P(z0))+Q(17,2000),
    }
    u_exponents={}
    for name,x,y,nu in classes:
        mean=(name=='good' and MUTATION!='convexity-instead')
        u=(nu+1)/2-z0 if mean else nu+(1-y)/2-z0
        positive(u,'increasing_dyad',name,True)
        rows[name]=exponent(x,y,P(z0))+u/2
        u_exponents[name]=u.strings()
    # Evaluate e*L=10+2e before any division: no rational-function approximation.
    rows['large']=alpha/2+3+3*beta+Q(1,2)-(10+2*e)
    expected_rows={
        'theta':P((Q(1,4),1)), 'principal_w':P((Q(1,12),Q(11,6),-1)),
        'principal_z':P((Q(1,4),2,-1)), 'small':P((Q(417,2000),Q(11,10))),
        'good':P((Q(1,4),Q(11,10))), 'middle_0':P((Q(67,275),Q(37,20))),
        'middle_1':P((Q(85111,353840),Q(37,20))),
        'last':P((Q(11,94),Q(37,20))), 'large':P((Q(-19,4),Q(-3,2)))}
    output_rows={}
    for name,p in rows.items():
        need(p==expected_rows[name],"exact_exponent",name)
        budget=P((Q(1,4),2))-p
        bs=positive(budget,'whole_interval_budget',name)
        output_rows[name]={'exponent':p.strings(),'margin':budget.strings(),'bernstein_margin':bs}
    # Independent direct scalar substitution into the raw scale monomial.
    for ee in [Q(1,10**j) for j in range(5,11)]:
        aa=Q(1,2)+ee; bb=Q(1,2); hh=1-aa
        for name,x,y,nu in classes:
            xx=x.at(ee); yy=y.at(ee); nn=nu.at(ee)
            uu=(nn+1)/2-z0 if name=='good' else nn+(1-yy)/2-z0
            direct=aa/2+xx-1+hh*z0+bb*(yy-1)+uu/2
            need(direct==rows[name].at(ee),'scalar_reconstruction',str((ee,name)))
        LL=10/ee+2
        direct=aa/2+3+hh*LL+3*bb+(1-LL)/2
        need(direct==rows['large'].at(ee),'scalar_reconstruction','large')
    # Two additive regimes: check exact dual identities, not an arithmetic no-go.
    for aa,bb in [(Q(3,5),Q(1,2)),(Q(7,10),Q(4,5)),(Q(1,2),Q(3,5)),(Q(3,5),Q(3,5))]:
        cc=aa/2+(1-aa)/6; mm=aa+bb
        theta=aa+bb-Q(1,2)-min(aa,bb)/2
        dual=(1-aa)/6-(mm-1)/2 if bb<=aa else Q(1,2)-5*bb/6-(mm-1)/6
        need(cc-theta==dual<Q(1,12),'theta_model_identity',str((aa,bb)))
    classify_checks(); cauchy_checks()
    return {'status':'PASS: exact finite bookkeeping, not analytic certification',
            'parameter_domain':'0 < e <= 1/100000', 'density':densities,
            'dyad_u_powers':u_exponents,'contributions':output_rows,
            'growth':'1/4 + 3e','mellin_boundary':'11/12 + 8e/3',
            'counts':dict(sorted(COUNTS.items())),'total_predicates':sum(COUNTS.values()),
            'limitations':['No actual Hecke values, zero counts or number fields were computed.',
                           'CT/BGL/DF analytic inputs and the family adapter are NOT verified by these checks.',
                           'Whole-interval claims use exact Bernstein coefficients; scalar samples only cross-check algebra.',
                           'Cauchy vectors and zero memberships are synthetic finite algebra fixtures.',
                           'Same-author proof/checker; no independent referee or Lean build.']}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--mutation',choices=['none','convexity-instead','wrong-bin','omit-good','endpoint-M','old-shift'],default='none')
    args=ap.parse_args(); MUTATION=args.mutation
    text=json.dumps(main(),indent=2,sort_keys=True)+'\n'
    if args.output: args.output.write_text(text,encoding='utf-8')
    else: print(text,end='')
