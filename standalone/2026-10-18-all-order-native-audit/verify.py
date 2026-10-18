#!/usr/bin/env python3
"""Exact finite diagnostics. This does not prove the imported analytic estimates."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import factorial, gcd, isqrt
from typing import Iterable

class CheckFailure(RuntimeError):
    pass

COUNTS: Counter[str] = Counter()

def check(category: str, condition: bool, detail: object = '') -> None:
    if not condition:
        raise CheckFailure(f'{category}: {detail}')
    COUNTS[category] += 1

# Q(omega), omega^2+omega+1=0: pairs of exact integers.
Z = tuple[int, int]
ZERO: Z = (0, 0)
ONE: Z = (1, 0)

def add(x: Z, y: Z) -> Z:
    return x[0] + y[0], x[1] + y[1]

def mul(x: Z, y: Z) -> Z:
    a,b=x; c,d=y
    return a*c-b*d, a*d+b*c-b*d

def scale(x: Z, c: int) -> Z:
    return c*x[0], c*x[1]

def power(x: Z, e: int) -> Z:
    if e < 0:
        raise ValueError('nonnegative exponent required')
    out=ONE
    for _ in range(e):
        out=mul(out,x)
    return out

def norm(x: Z) -> int:
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]

ROOTS=[power((1,1),e) for e in range(6)]
SPLIT_PRIMES=[(7,2),(7,4),(13,3),(13,9)]

def symbol(u: Z, p: int, omega_mod_p: int) -> Z:
    a=(u[0]+u[1]*omega_mod_p)%p
    if a==0:
        return ZERO
    v=pow(a,(p-1)//6,p)
    for e in range(6):
        if pow(1+omega_mod_p,e,p)==v:
            return ROOTS[e]
    raise CheckFailure('residue outside sixth roots')

def product_character(z: tuple[Z,...], exps: tuple[int,...]) -> Z:
    out=ONE
    for a,e in zip(z,exps):
        out=mul(out,power(a,e))
    return out

def removed_character(z: tuple[Z,...], exps: tuple[int,...]) -> Z:
    scalar=product_character(z,tuple(e%6 for e in exps))
    mask=all(a!=ZERO or e//6==0 for a,e in zip(z,exps))
    return scalar if mask else ZERO


def convolution(c: dict[tuple[int,...],int], d: dict[tuple[int,...],int]) -> dict[tuple[int,...],int]:
    out: defaultdict[tuple[int,...],int]=defaultdict(int)
    for x,a in c.items():
        for y,b in d.items():
            out[tuple(i+j for i,j in zip(x,y))]+=a*b
    return dict(out)

def multinomial_coefficient(k: int, e: tuple[int,...]) -> int:
    total=sum(e)
    if total>k:
        return 0
    denom=factorial(k-total)
    for j in e:
        denom*=factorial(j)
    return (-1)**total * (factorial(k)//denom)


def kappa(n: int, r: int, sigma: F) -> F:
    return max(F(1)+r*max(F(0),1-2*sigma),
               r * (1 - sigma),
               F(n-1,n)+r*(F(1,2)+F(1,n)-sigma),
               F(2,n)+r*(1-F(1,2*n)-sigma))

def afe_dual(r: int, v: F, b: F, sigma: F) -> F:
    return r*(1-2*sigma)+(r-v)*(b+2*sigma-1)

def native_powers(n: int, k: int, h: F) -> tuple[F,...]:
    return (h+k, h/n + 2*k, h*(1-F(1,n))+k*(1+F(2,n)),
            h*F(2,n)+k*(2-F(1,n)))

def native_excess(k: int, h: F) -> F:
    return max(F(0), k-5*h/6, F(k,3)-h/6, F(5*k,6)-2*h/3)

def mellin_shift(a: F) -> F:
    return F(5,6)-a/3


def primes(bound: int) -> list[int]:
    mark=[True]*(bound+1)
    mark[0:2]=[False,False]
    for p in range(2,isqrt(bound)+1):
        if mark[p]:
            for j in range(p*p,bound+1,p):
                mark[j]=False
    return [p for p in range(2,bound+1) if mark[p]]

def mobius(n: int) -> int:
    out=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; out=-out
            if n%p==0:
                return 0
        p+=1
    return -out if n>1 else out

def chi3(n: int) -> int:
    return 0 if n%3==0 else (1 if n%3==1 else -1)


def complete_native_census(cap: int) -> tuple[int,list[int]]:
    # All distinct squarefree prime-ideal subsets, with every allowed norm <= cap.
    pq: list[tuple[int,int]]=[]
    for p in primes(cap):
        if p in (2,3):
            continue
        if p%3==1:
            pq.extend([(p,0),(p,1)])
        elif p*p<=cap:
            pq.append((p*p,0))
    ideals: list[tuple[int,int,tuple[int,...]]]=[(1,1,())]
    for ident,(q,_) in enumerate(pq):
        ideals.extend((N*q,-mu,support+(ident,))
                      for N,mu,support in tuple(ideals) if N*q<=cap)
    fibers=[0]*(cap+1)
    for N,mu,support in ideals:
        fibers[N]+=mu
        check('ideal_support_sign',mu==(-1)**len(support),(N,support))
    for n in range(1,cap+1):
        # Independent rational-integer Dirichlet convolution mu*(mu chi_-3).
        c=0
        if gcd(n,6)==1:
            for d in range(1,isqrt(n)+1):
                if n%d==0:
                    q=n//d
                    c+=mobius(d)*mobius(q)*chi3(q)
                    if d!=q:
                        c+=mobius(q)*mobius(d)*chi3(d)
        check('complete_norm_fibers',fibers[n]==c,n)
    check('prime_conjugates',fibers[7]==-2 and fibers[13]==-2 and fibers[25]==-1)
    return len(ideals),fibers


def test_physical_moments() -> dict[str,object]:
    rows=sorted((a,b) for a in range(-5,6) for b in range(-5,6)
                if 0<norm((a,b))<=13)
    check('physical_row_census',len(rows)==54)
    check('distinct_prime_characters',symbol((3,1),*SPLIT_PRIMES[0])!=symbol((3,1),*SPLIT_PRIMES[1]))
    # Independently norm-filtered good squarefree ideals <=13 are precisely
    # the unit, two prime ideals over 7, and two over 13.
    check('column_window',sorted([1]+[p for p,_ in SPLIT_PRIMES])==[1,7,7,13,13])
    base={(0,0,0,0):1}
    for j in range(4):
        e=tuple(int(i==j) for i in range(4)); base[e]=-1
    coeffs={(0,0,0,0):1}
    table=[]
    for k in range(1,9):
        coeffs=convolution(coeffs,base)
        check('product_support_count',len(coeffs)==factorial(k+4)//(factorial(k)*factorial(4)),k)
        for exps,c in coeffs.items():
            check('complete_product_coefficients',c==multinomial_coefficient(k,exps),(k,exps))
            check('product_sign',c*(-1)**sum(exps)>0,(k,exps))
        total=0
        for u in rows:
            zs=tuple(symbol(u,p,w) for p,w in SPLIT_PRIMES)
            A=ONE
            for z in zs:
                A=add(A,scale(z,-1))
            reconstructed=ZERO
            for exps,c in coeffs.items():
                z=product_character(zs,exps)
                if k in (1,6,7,8):
                    check('full_sixth_power_masks',z==removed_character(zs,exps),(k,u,exps))
                reconstructed=add(reconstructed,scale(z,c))
            check('native_power_identity',reconstructed==power(A,k),(k,u))
            check('native_moment_identity',norm(reconstructed)==norm(A)**k,(k,u))
            total+=norm(reconstructed)
        table.append({'k':k,'product_ideal_count':len(coeffs),'exact_full_54_row_moment':total})
    # These are not an asymptotic fit. They authenticate the whole finite sum.
    return {'physical_rows':len(rows),'column_ideals':5,'orders':table}


def test_exponents() -> dict[str,object]:
    known={1:F(1),2:F(7,6),3:F(19,12),4:F(2),8:F(4)}
    for r,expected in known.items():
        check('central_known_values',kappa(6,r,F(1,2))==expected,r)
    off=[(2,F(7,12),F(1)),(2,F(5,12),F(4,3)),
         (4,F(3,4),F(1)),(4,F(1,4),F(3))]
    for r,s,v in off:
        check('offcentral_known_values',kappa(6,r,s)==v,(r,s))
    for n in (3,4,6,12):
        for r in range(1,13):
            for j in range(1,12):
                s=F(j,12)
                if s<F(1,2):
                    check('functional_equation_exponents',
                          kappa(n,r,s)==r*(1-2*s)+kappa(n,r,1-s),(n,r,s))
                if r>=4:
                    check('all_character_orders_saturate',kappa(n,r,s)==max(1+r*max(0,1-2*s),r*(1-s)),(r,s))
                if s>=F(1,2):
                    mons=[(F(1),F(0)),(F(0),F(1)),(F(n-1,n),F(2,n)),(F(2,n),F(n-1,n))]
                    for v in (F(0),F(r,4),F(r,2),F(3*r,4),F(r)):
                        endpoints=[F(1)]
                        for a,b in mons:
                            dual=afe_dual(r,v,b,s)
                            check('dual_endpoint_identity',dual==(r-v)*b+v*(1-2*s),(n,r,s,v))
                            endpoints.extend((a+v*(1+b-2*s),a+dual))
                        check('unbalanced_model_no_gain',max(endpoints)>=kappa(n,r,s),(n,r,s,v))
                        if v==F(r,2):
                            check('balanced_endpoint_reconstruction',max(endpoints)==kappa(n,r,s),(n,r,s))
    for n in (3,4,6,12):
        for r in range(1,13):
            right_line=(F(1,2) if r==1 else F(1,2)+F(1,2*n) if r==2
                        else F(2,3)+F(1,6*n) if r==3 else 1-F(1,r))
            check('general_diagonal_line',kappa(n,r,right_line)==1,(n,r))
            check('below_diagonal_line',kappa(n,r,right_line-F(1,1000))>1,(n,r))
            for h in (F(2*r),F(3*r)):
                for exponent in native_powers(n,r,h)[1:]:
                    check('long_row_diagonal_corollary',exponent<=h+r,(n,r,h))
    for k in range(1,17):
        for h in (F(0),F(1),F(21,20),F(k,2),F(k),F(2*k)):
            powers=native_powers(6,k,h)
            excess=native_excess(k,h)
            check('native_excess_identity',max(powers)==h+k+excess,(k,h))
            check('principal_extraction_loss',h+excess>=k,(k,h))
    for j in range(1,120):
        a=F(j,240)
        envelope=mellin_shift(a)+max(a/2,F(1,2)-a)
        check('symmetric_model_floor',envelope>=F(8,9),a)
        for y in (F(1,4),F(5,12),F(1,2),F(7,12),F(3,4),F(1),F(3,2)):
            x=max(F(1,2),1-y) # Limiting faces, not legal contour assertions.
            cost=F(1) if y>=F(1,2) else F(3,2)-y
            E=x-1+a*(y-F(1,2))+(1-a)*cost
            check('full_good_class_floor',E>=F(1,2)-a,(a,y))
    check('symmetric_model_balance',mellin_shift(F(1,3))+F(1,6)==F(8,9))
    # A finite illustration of choosing one fixed order before taking X large.
    chosen=[]
    for delta in (F(1,10),F(1,100),F(1,1000)):
        h=F(1); C=F(10)
        k=int((h+C)/delta)+1
        check('sublinear_excess_quantifiers',(h+C)/(2*k)<delta/2,k)
        chosen.append({'delta':str(delta),'fixed_order_k':k,'root_excess':str((h+C)/(2*k))})
    return {'central_exponents':{str(k):str(v) for k,v in known.items()},'fixed_C_examples':chosen}


def main() -> None:
    n,_=complete_native_census(256)
    physical=test_physical_moments()
    exponents=test_exponents()
    report={
      'status':'PASS: exact finite algebra only; no analytic theorem certification',
      'counts':dict(sorted(COUNTS.items())),
      'total_predicates_including_repeated_guards':sum(COUNTS.values()),
      'complete_squarefree_good_ideals_through_256':n,
      'physical_fixture':physical,
      'exponent_diagnostics':exponents,
      'not_computed':['L-values','zeros','infinite native moment','theta projection','RH proof']}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
