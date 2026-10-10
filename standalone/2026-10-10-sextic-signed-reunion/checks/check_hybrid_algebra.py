#!/usr/bin/env python3
"""Exact finite diagnostics for smooth cube regrouping and exponent algebra.

Norms 7 and 13 label formal distinct primes. The row phases are quadratic
values -1, 0, 1. Rational piecewise linear cutoff samples check the finite
identity for prescribed weights; they do not certify smoothness or analysis.
Negative controls retain (n,d) overlap and repeated-prime character zeros.
The written proofs supply the continuous analytic and parameter arguments.
"""

from fractions import Fraction as F
from itertools import product
import json

counts = {}

def require(ok, label):
    counts[label] = counts.get(label, 0) + 1
    if not ok:
        raise ValueError(label)

beta = F(11, 12)
raw_terms = [(F(1),F(1),F(0)),
             (beta-F(1,2),F(2),F(5,2)-beta),
             (F(2,3),F(4,3),2*beta),
             (F(0),F(1),F(0)),
             (F(2),F(1,6),F(-3)),
             (F(4,3),F(2,3),F(-2))]
a2_terms = list(raw_terms)
a2_terms[1] = (beta-F(1,2),F(2),F(17,4)-F(5,2)*beta)
regimes = [
    ('literal_first',raw_terms,F(8,29),F(-7,29),F(34,29),F(155,174),F(0),F(111,253),(2,4)),
    ('literal_second',raw_terms,F(19,55),F(-2,5),F(53,55),F(41,30),F(111,253),F(19,22),(1,4)),
    ('a2_first',a2_terms,F(8,29),F(-7,29),F(34,29),F(155,174),F(0),F(150,443),(2,4)),
    ('a2_second',a2_terms,F(38,119),F(-44,119),F(124,119),F(911,714),F(150,443),F(19,22),(1,4)),
]
regime_report=[]
for name,terms,r0,r1,e0,e1,lo,hi,active in regimes:
    affine=[(a+c*r0,b+c*r1) for a,b,c in terms]
    for j in active:
        require(affine[j][0]==e0,'balance_coefficient_equalities')
        require(affine[j][1]==e1,'balance_coefficient_equalities')
    for h in (lo,hi):
        r=r0+r1*h
        require(r>=0,'cutoff_endpoint_inequalities')
        require(r<=F(1,3),'cutoff_endpoint_inequalities')
        for a,b in affine:
            require(a+b*h<=e0+e1*h,'energy_endpoint_inequalities')
    regime_report.append({'name':name,'cutoff_D':str(r0),'cutoff_H':str(r1),
                          'energy_D':str(e0),'energy_H':str(e1),
                          'height_interval':[str(lo),str(hi)],
                          'six_substituted_exponents':[[str(a),str(b)] for a,b in affine]})

require(F(53,55)+F(41,60)==F(1087,660),'displayed_fraction_equalities')
require(F(124,119)+F(911,1428)==F(2399,1428),'displayed_fraction_equalities')
require(F(379,228)-F(1087,660)==F(16,1045),'displayed_fraction_equalities')
require((2-F(53,55))/F(41,30)==F(342,451),'displayed_fraction_equalities')
require((2-F(124,119))/F(911,714)==F(684,911),'displayed_fraction_equalities')

# Exact vertex checks of the auxiliary triangle at thirteen beta values.
# The written proofs establish the full real interval by monotonic polynomial
# inequalities; this finite sample is only a diagnostic.
for b in (F(j,24) for j in range(12,25)):
    for kind in ('literal','a2'):
        p=F(5,2)-b if kind=='literal' else F(17,4)-F(5,2)*b
        hmax=(F(5,2)-b)/(2+p/18)
        qmax=F(5,2)-b
        for h,q in [(F(0),F(0)),(F(0),qmax),(hmax,F(0))]:
            r=h/18
            energies=[1+h,q+2*h+b-F(1,2)+p*r,
                      F(2,3)*q+F(4,3)*h+F(2,3)+2*b*r,
                      h,F(2)+h/6-3*r,F(4,3)+F(2,3)*h-2*r]
            for energy in energies:
                require(energy<=2,'auxiliary_triangle_vertex_inequalities')

# Spectral crossover and threshold arithmetic.
require(F(1,6)+F(11,12)==2-F(11,12),'spectral_equalities')
require(F(1,12)+F(11,12)*(1-F(5,8))==1-F(11,12)*F(5,8),'spectral_equalities')
require(F(6,11)<F(5,8),'spectral_threshold_inequalities')
require(1-F(11,12)*F(5,8)<F(1,2),'spectral_threshold_inequalities')
require(1-F(4,5)*F(5,8)==F(1,2),'spectral_equalities')

primes=(7,13)
def norm(e):
    out=1
    for p,v in zip(primes,e): out*=p**v
    return out
def add(e,f): return tuple(x+y for x,y in zip(e,f))
def sub(e,f): return tuple(x-y for x,y in zip(e,f))
def disjoint(e,f): return all(x==0 or y==0 for x,y in zip(e,f))
def omega_sample(N,R):
    if N<=R: return F(1)
    if N>=2*R: return F(0)
    return F(2)-F(N,R)
def phase(e,row,q,wrong_zero=False):
    ans=1
    for v,t,aux in zip(e,row,q):
        if not v: continue
        t=0 if aux else t
        if wrong_zero and v%2==0:
            z=1
        else:
            z=t**v
        ans*=z
    return ans

regroup_cases=0
wrong_extra_mask=0
wrong_deleted_zero=0
for d in product(range(3),repeat=2):
    hs=[h for h in product(range(2),repeat=2) if all(x<=y for x,y in zip(h,d))]
    for labels in product(range(3),repeat=2):
        a=tuple(int(x==1) for x in labels)
        n=tuple(int(x==2) for x in labels)
        for q in product(range(2),repeat=2):
            for row in product((-1,0,1),repeat=2):
                # Any common physical squarefree coefficient factors out.
                common=int(all(v==0 or (t!=0 and aux==0)
                               for v,t,aux in zip(add(a,n),row,q)))
                for R in (1,8,14,32):
                    lhs=F(0)
                    c=F(0)
                    for h in hs:
                        b=sub(d,h)
                        w=(-1)**sum(h)*(1-omega_sample(norm(h),R))
                        c+=w
                        lhs+=w*phase(h,row,q)*phase(b,row,q)*int(disjoint(a,h))*int(disjoint(a,b))*common
                    rhs=c*phase(d,row,q)*int(disjoint(a,d))*common
                    require(lhs==rhs,'smooth_regrouping_equalities')
                    regroup_cases+=1
                    wrong_extra_mask+=int(rhs*int(disjoint(n,d))!=rhs)
                    wrong_deleted_zero+=int(c*phase(d,row,q,True)*int(disjoint(a,d))*common!=rhs)
require(wrong_extra_mask>0,'negative_control_rejections')
require(wrong_deleted_zero>0,'negative_control_rejections')

report={'status':'pass','arithmetic':'exact Fraction and integer arithmetic',
        'scope':'Finite algebra and affine exponent comparisons, not analytic certification',
        'counts':counts,'regimes':regime_report,
        'regrouping_cases':regroup_cases,
        'wrong_extra_n_d_mask_failures':wrong_extra_mask,
        'wrong_deleted_repeated_prime_zero_failures':wrong_deleted_zero}
print(json.dumps(report,sort_keys=True,indent=2))
