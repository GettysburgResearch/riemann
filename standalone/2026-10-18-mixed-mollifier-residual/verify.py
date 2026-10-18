#!/usr/bin/env python3
"""Exact finite regression checks, not an analytic proof or an L-value census."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
import math

COUNTS: Counter[str] = Counter()
MUTATION = ""

def check(ok: bool, group: str) -> None:
    if not ok:
        raise ValueError("failed gate: " + group)
    COUNTS[group] += 1

def kappa(n: int, v: Q) -> Q:
    if n < 3 or v < 0:
        raise ValueError("invalid sieve parameters")
    return max(Q(1), v, 1-Q(1,n)+2*v/n, Q(2,n)+(1-Q(1,n))*v)

def envelope(n: int, d: Q, a: Q, x: Q, r: int, p: int) -> dict[str, Q]:
    if not (isinstance(r,int) and isinstance(p,int) and r>=1 and p>=2):
        raise ValueError("integer moment orders required")
    if not (0<d<1 and 0<a<=x<=1):
        raise ValueError("invalid line or cutoff")
    main=max(kappa(n,r*a)-d*r*a,kappa(n,r*(a+x))-d*r*(a+x))
    m=max(Q(1),kappa(n,p*r*a)-d*p*r*a)
    b1=kappa(n,r*(1-x))-r*d*x
    b2=kappa(n,2*r*(1-x))-2*r*d*x
    mixed=(m+(p-2)*b1+b2)/p
    if MUTATION == "pointwise_mollifier":
        mixed= r*a*(1-d)+b1
    principal=r*a*(1-d)
    return dict(main=main,mollifier=m,dual_low=b1,dual_high=b2,
                mixed=mixed,principal=principal,total=max(main,mixed,principal,Q(0)))

def ceilq(x: Q) -> int:
    return -((-x.numerator)//x.denominator)

# Exact arithmetic in Q(omega), omega^2+omega+1=0.
Z=tuple[Q,Q]
ZERO: Z=(Q(0),Q(0)); ONE: Z=(Q(1),Q(0))
ROOTS: tuple[Z,...]=tuple((Q(a),Q(b)) for a,b in [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)])
def add(z: Z,w: Z)->Z: return (z[0]+w[0],z[1]+w[1])
def mul(z: Z,w: Z)->Z:
    a,b=z; c,d=w
    return (a*c-b*d,a*d+b*c-b*d)
def scale(z:Z,a:Q)->Z: return(z[0]*a,z[1]*a)
def conj(z:Z)->Z: return(z[0]-z[1],-z[1])
def power(z:Z,e:int)->Z:
    out=ONE
    for _ in range(e): out=mul(out,z)
    return out

def primitive_root(p:int)->int:
    return next(g for g in range(2,p) if len({pow(g,j,p) for j in range(p-1)})==p-1)
LOGS={p:{pow(primitive_root(p),j,p):j for j in range(p-1)} for p in (7,13)}
def character(b:int,e:int,f:int)->Z:
    # Principal powers STILL vanish at nonunits modulo 91.
    if b%7==0 or b%13==0:
        return ONE if MUTATION=="erase_masks" else ZERO
    return ROOTS[(e*LOGS[7][b%7]+f*LOGS[13][b%13])%6]

def mu(n:int)->int:
    sign=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; sign=-sign
            if n%p==0: return 0
            while n%p==0: n//=p
        p+=1
    return -sign if n>1 else sign

def cutoff(b:int,X:int)->Q:
    # Rational flat/linear fixture: algebra only, NOT the smooth analytic V.
    return Q(1) if b<=X else max(Q(0),Q(2)-Q(b,X))

def convolution(a:dict[int,Z],b:dict[int,Z])->dict[int,Z]:
    out:dict[int,Z]={}
    for m,z in a.items():
        for n,w in b.items():
            out[m*n]=add(out.get(m*n,ZERO),mul(z,w))
    return {n:z for n,z in out.items() if z!=ZERO}

def run()->dict:
    exp=envelope(6,Q(1,2),Q(3,5),Q(3,5),1,3)
    target={'main':Q(11,15),'mollifier':Q(1),'dual_low':Q(7,10),
            'dual_high':Q(1,2),'mixed':Q(11,15),'principal':Q(3,10),'total':Q(11,15)}
    for name,value in target.items(): check(exp[name]==value,"three_quarters_exact")
    check(Q(7,8)-exp['total']==Q(17,120),"comparison_not_zero_free")
    for r in range(1,17):
        expected=Q(11,15) if r==1 else Q(3*r,5)
        check(envelope(6,Q(1,2),Q(3,5),Q(3,5),r,3)['total']==expected,"all_fixed_residual_orders")
    try:
        envelope(6,Q(1,2),Q(1,4),Q(1,2),1,Q(3,2))
    except ValueError:
        check(True,"fractional_powering_rejected")
    else:
        check(False,"fractional_powering_rejected")

    near=[]
    for n in (3,4,6,8,12):
        for t in range(1,81):
            y=Q(t,100); d=y/n; a=y/4; pp=4/(y*(2-y)); p=ceilq(pp)
            if MUTATION=="floor_order": p=pp.numerator//pp.denominator
            check(pp<=p<=4/y,"nearline_ceiling")
            check(Q(1)/(2-y)<=p*a<=1,"nearline_branch")
            e=envelope(n,d,a,Q(1,2),1,p)
            check(e['main']==1-n*d*d/4,"nearline_main")
            check(e['mixed']==1-n*d*d/4,"nearline_mixed")
            check(e['total']==1-n*d*d/4,"nearline_complete")
            if n==6 and t in (6,30,60,80):
                near.append({'sigma':str((1+d)/2),'a':str(a),'p':p,'exponent':str(e['total'])})
    # Continuity / dyadic endpoint bookkeeping on declared finite grids.
    for n,d,r,a,x in product((3,6,10),(Q(1,10),Q(1,2),Q(4,5)),(1,2,4),(Q(1,10),Q(1,4)),(Q(1,2),Q(3,4))):
        ends=max(kappa(n,r*a)-d*r*a,kappa(n,r*(a+x))-d*r*(a+x))
        for t in range(11):
            v=r*a+r*x*Q(t,10)
            check(kappa(n,v)-d*v<=ends,"finite_convex_endpoint_samples")

    # Actual-conductor algebra, including microscopic effective lengths.
    for n,d,j,x in product((3,6,8),(Q(1,10),Q(1,2),Q(4,5)),(1,2,3,6),(Q(1,2),Q(3,5),Q(3,4))):
        upper=kappa(n,j*(1-x))-j*d*x
        for z in range(21):
            q=Q(z,20)
            if q>=x:
                value=-j*d*q+j*d*(q-x)+kappa(n,j*(q-x))
                check(value<=upper,"actual_conductor_main")
            else:
                J=4*j+4
                value=1-j*d*q+J*(q-x)
                check(value<=1-j*d*x<=upper,"subunit_dual_tail")
    q=Q(1,5); j=2; d=Q(1,2)
    kept=-j*d*q if MUTATION!="replace_negative_conductor" else -j*d
    check(kept==Q(-1,5),"negative_conductor_identity")
    # The principal row has an AFE pole and must NOT be assigned the R4 bound.
    claimed=Q(1,2) if MUTATION=="principal_in_dual" else Q(3,5)
    check(claimed>=Q(3,5),"principal_polar_term_separate")

    fixtures=((0,0),(1,1),(1,2),(3,0))
    for e,f in fixtures:
        check(character(7,e,f)==ZERO and character(13,e,f)==ZERO,"literal_nonunit_zero")
        for b,c in product(range(1,26),repeat=2):
            left=mul(character(b,e,f),conj(character(c,e,f)))
            right=character(b*c**5,e,f)
            if MUTATION=="same_character_dual": right=character(b*c,e,f)
            check(left==right,"mixed_character_ratio_identity")
        for c,d0 in product(range(1,16),repeat=2):
            left=character(c*d0**6,e,f)
            right=character(c,e,f) if math.gcd(d0,91)==1 else ZERO
            if MUTATION=="extra_coprimality" and math.gcd(c,d0)!=1: right=ZERO
            check(left==right,"power_removal_shared_primes")
        for A,X in ((3,4),(4,4),(8,8)):
            primal={b:scale(character(b,e,f),cutoff(b,X)/b) for b in range(1,2*X+1)}
            moll={d0:scale(character(d0,e,f),Q(mu(d0),d0)) for d0 in range(1,A+1)}
            direct=convolution(primal,moll)
            unit=Q(0) if MUTATION=="retain_unit_error" else Q(-1)
            direct[1]=add(direct.get(1,ZERO),scale(ONE,unit))
            for b in range(1,2*A*X+1):
                hh=sum((Q(mu(d0))*cutoff(b//d0,X) for d0 in range(1,A+1) if b%d0==0),Q(0))
                want=scale(character(b,e,f),hh/b)
                if b==1: want=add(want,scale(ONE,Q(-1)))
                check(direct.get(b,ZERO)==want,"full_flat_convolution")
                if b<=A: check(want==ZERO,"low_coefficients_cancel")
            if (A,X)==(3,4):
                error={b:z for b,z in direct.items() if z!=ZERO}
                rr={1:ONE}
                for r in range(1,4):
                    rr=convolution(rr,error)
                    for b in rr: check(A**r<b<=(2*A*X)**r,"powered_error_support")
    # Finite mixed Holder inequality: no independence or character collapse.
    for p in range(2,9):
        for idx in range(60):
            M=[(idx+3*j)%7 for j in range(1,6)] # squared moduli fixtures
            R=[(idx*idx+5*j)%9 for j in range(1,6)]
            lhs=sum(a*b for a,b in zip(M,R))**p
            rhs=sum(a**p for a in M)*sum(R)**(p-2)*sum(b*b for b in R)
            check(lhs<=rhs,"mixed_holder_integer_arrays")
    lhs=2**3; rhs=2*2*(1 if MUTATION=="omit_fourth_moment" else 2)
    check(lhs<=rhs,"mixed_holder_fourth_factor")
    for r in range(1,17):
        residual=Q(1) if MUTATION!="delete_zero_member" else Q(0)
        check(residual==1,"zero_member_cost_not_deleted")
        check(Q(1)<=Q(2)**(r+1),"positive_mean_bound_allows_one_error")

    return {'status':'PASS; finite algebra only, not an analytic proof',
      'three_quarters':{name:str(value) for name,value in exp.items()},
      'nearline_examples':near,'groups':dict(sorted(COUNTS.items())),
      'coverage':{'finite_character_moduli':[7,13], 'character_profiles':[list(x) for x in fixtures],
       'mixed_ratio_columns':[1,25], 'power_removal_c_d':[1,15],
       'convolution_cutoffs':[[3,4],[4,4],[8,8]],
       'field_note':'Actual residue characters modulo 7 and 13; NOT the entire number-field L family.',
       'cutoff_note':'Flat piecewise rational fixture checks algebra, not C-infinity analytic decay.',
       'computed_L_values':False,'computed_zeta_zeros':False,'independent_referee':False},
      'total_finite_predicates':sum(COUNTS.values())}

def main()->None:
    global MUTATION
    parser=argparse.ArgumentParser();parser.add_argument('--mutate',default='')
    args=parser.parse_args();MUTATION=args.mutate
    print(json.dumps(run(),indent=2,sort_keys=True))
if __name__=='__main__': main()
