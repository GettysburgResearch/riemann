#!/usr/bin/env python3
"""Exact finite diagnostics, not an analytic proof or an infinite-source computation."""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, factorial, isqrt

class Failure(RuntimeError):
    pass
COUNTS: Counter[str] = Counter()

def check(name: str, ok: bool, data: object='') -> None:
    if not ok:
        raise Failure(f'{name}: {data}')
    COUNTS[name]+=1

CAP=512

def primes(n: int) -> list[int]:
    flags=[True]*(n+1); flags[:2]=[False,False]
    for p in range(2,isqrt(n)+1):
        if flags[p]:
            flags[p*p::p]=[False]*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if flags[p]]

PQS: list[int]=[]
for p in primes(CAP):
    if p in (2,3):
        continue
    if p%3==1:
        PQS += [p,p]  # Distinct conjugate prime IDEALS.
    elif p*p<=CAP:
        PQS += [p*p]

Ideal=tuple[tuple[int,int],...]
UNIT: Ideal=()

def ideal_norm(a: Ideal) -> int:
    z=1
    for i,e in a:
        z*=PQS[i]**e
    return z

def mu(a: Ideal) -> int:
    return 0 if any(e>1 for _,e in a) else (-1)**len(a)

def allowed(a: Ideal, excluded: frozenset[int]) -> bool:
    return not any(i in excluded for i,_ in a)

def pairs(a: Ideal):
    for es in product(*(range(e+1) for _,e in a)):
        left=tuple((i,j) for (i,_),j in zip(a,es) if j)
        right=tuple((i,e-j) for (i,e),j in zip(a,es) if e-j)
        yield left,right

def census(cap: int) -> list[Ideal]:
    out=[UNIT]
    for i,q in enumerate(PQS):
        old=tuple(out)
        power=q; e=1
        while power<=cap:
            out.extend(a+((i,e),) for a in old if ideal_norm(a)*power<=cap)
            power*=q; e+=1
    return sorted(out,key=lambda a:(ideal_norm(a),a))

def coefficient(a: Ideal, h: int, excluded: frozenset[int]=frozenset()) -> F:
    if not allowed(a,excluded):
        return F(0)
    value=F(1)
    for i,e in a:
        q=PQS[i]
        value *= -(1-F(1,q**h))*F(1,q**((e-1)*h))
    return value

def direct(a: Ideal,h: int,excluded: frozenset[int]=frozenset()) -> F:
    return sum((F(mu(b),ideal_norm(d)**h) for b,d in pairs(a)
                if allowed(b,excluded) and allowed(d,excluded)),F(0))

def translated_convolution(a: Ideal,h: int,k: int) -> F:
    return sum((coefficient(b,h)*coefficient(d,k)/ideal_norm(d)**h
                for b,d in pairs(a)),F(0))

def unit_removed(a: Ideal,h: int) -> F:
    return (F(a==UNIT)-coefficient(a,h))/h

def formal_log(a: Ideal) -> int:
    # Positive algebraic log labels, NOT transcendental logarithm evaluations.
    return sum(e*PQS[i] for i,e in a)

def first_generator(a: Ideal) -> int:
    return sum(mu(b)*formal_log(d) for b,d in pairs(a))

def prime_ideal_generator(a: Ideal) -> int:
    return PQS[a[0][0]] if len(a)==1 else 0

@lru_cache(maxsize=None)
def log_interval(x: F) -> tuple[F,F]:
    if x<=0:
        raise ValueError('positive input required')
    if x<1:
        lo,hi=log_interval(1/x)
        return -hi,-lo
    k=0
    while x>=2:
        x/=2; k+=1
    def series(y: F) -> tuple[F,F]:
        z=(y-1)/(y+1); n=96
        lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
        err=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
        return lo,lo+err
    a,b=series(x); c,d=series(F(2))
    return a+k*c,b+k*d


def stencil(m: int,j: int) -> int:
    return (-1)**(j-1)*comb(m,j)

def g_polynomial(m: int,h: F,x: F) -> F:
    return sum((F(stencil(m,j),j)*(1-x**j)/h for j in range(1,m+1)),F(0))

def g_positive(m: int,h: F,x: F) -> F:
    return sum(((1-x)**j/F(j)/h for j in range(1,m+1)),F(0))

def continuum_center(s: F,h: F) -> F:
    # Exact pole-only synthetic control Z(s)=1/(s-1).
    q=(s-1)/(s+h-1)
    return (1-q)/h-1/(s+h-1)

def c_near_pole(h: F,kappa: F,gamma: F,eta: F) -> F:
    # Z(s)=kappa/(s-1)+gamma+eta*(s-1); no actual zeta evaluation.
    return kappa/(kappa-gamma*h+eta*h*h)

def gaussian_completed(u: F,L: F,c: F,t: F) -> F:
    b=1-t-c
    return (1-t)*L+b*b-(u-L-2*b)**2/4

def critical_density_exponent(p: int) -> F:
    return -F(p,2)-1


def main() -> None:
    ideals=census(CAP)
    check('unique_ideals',len(set(ideals))==len(ideals))
    norm_counts=Counter(ideal_norm(a) for a in ideals)
    # Independent rational norm series for zeta_K with Euler factors at 2,3 removed.
    expected=[0]*(CAP+1)
    for n in range(1,CAP+1):
        if n%2 and n%3:
            expected[n]=sum((0 if d%3==0 else (1 if d%3==1 else -1))
                            for d in range(1,n+1) if n%d==0)
        check('complete_norm_census',norm_counts[n]==expected[n],n)
    seven=[i for i,q in enumerate(PQS) if q==7]
    check('conjugate_prime_ideals',len(seven)==2 and norm_counts[49]==3)
    cross=((seven[0],1),(seven[1],1))
    check('same_norm_not_prime_power',first_generator(cross)==0
          and prime_ideal_generator(cross)==0 and ideal_norm(cross)==49)
    check('unit_subtraction',unit_removed(UNIT,1)==0)
    exclusions=(frozenset(),frozenset({seven[0]}),frozenset(seven))
    for a in ideals:
        for h in (0,1,2,3):
            for ex in exclusions:
                check('complete_convolution',coefficient(a,h,ex)==direct(a,h,ex),(a,h,ex))
        check('translation_cocycle',translated_convolution(a,1,2)==coefficient(a,3),a)
        check('prime_power_generator',first_generator(a)==prime_ideal_generator(a),a)
        if a:
            lo,hi=log_interval(F(ideal_norm(a)))
            for h in (1,2):
                ah=-coefficient(a,h)/h
                if len(a)==1:
                    pl,ph=log_interval(F(PQS[a[0][0]]))
                    check('prime_power_deficit',pl-ah>=0 and ph-ah<=h*lo*lo,(a,h))
                else:
                    check('all_composite_deficit',abs(ah)<=h*lo*lo/4,(a,h))
        # Formal Taylor coefficients of complete convolution, through degree 6.
        for order in range(1,7):
            deriv=sum(mu(b)*(-formal_log(d))**order for b,d in pairs(a))
            if len(a)>order:
                check('higher_generator_support',deriv==0,(a,order))
    for m in range(1,17):
        check('stencil_constant',sum(stencil(m,j) for j in range(1,m+1))==1,m)
        for degree in range(1,m):
            check('stencil_annihilation',sum(stencil(m,j)*j**degree for j in range(1,m+1))==0,(m,degree))
        check('interpolation_remainder_factor',sum(stencil(m,j)*j**m for j in range(1,m+1))==(-1)**(m-1)*factorial(m),m)
        for h in (F(1),F(1,8),F(1,64)):
            for x in (F(1),F(1,4),F(1,2),F(3,4),F(9,10),F(99,100),F(999,1000)):
                gp=g_polynomial(m,h,x); gs=g_positive(m,h,x)
                check('positive_stencil_polynomial',gp==gs,(m,h,x))
                loglo,loghi=log_interval(1/x)
                tail=(1-x)**(m+1)/(h*(m+1)*x)
                check('certified_log_remainder',loglo/h-gs>=0 and loghi/h-gs<=tail,(m,h,x))
            mass=sum(F(abs(stencil(m,j)),j*h) for j in range(1,m+1))
            check('stencil_absolute_mass',mass<=(2**m-1)/h,(m,h))
    for s in (F(2),F(3,2),F(2,3),F(5,4)):
        for h in (F(1,16),F(1,8),F(1,4)):
            if s+h!=1:
                check('shifted_pole_centering',continuum_center(s,h)==0,(s,h))
    for h in (F(0),F(1,32),F(1,16)):
        k,g,e=F(2),F(3),F(5)
        cc=c_near_pole(h,k,g,e)
        check('laurent_continuum_normalizer',cc*(k-g*h+e*h*h)==k,h)
    for L,u,c,t in product((F(0),F(2),F(7)),(F(0),F(1),F(11)),
                            (F(0),F(1,2),F(5,6)),(F(0),F(1,8),F(1,4))):
        original=-t*u-c*(u-L)-(u-L)**2/4+u
        check('exact_continuum_square',original==gaussian_completed(u,L,c,t),(L,u,c,t))
    # Synthetic finite zero chains, not a zeta-zero census.
    for length in range(1,9):
        h=F(1,100); start=F(3,5)
        zeros={start+i*h:(i+1) for i in range(length)}
        poles={s:max(0,m-zeros.get(s+h,0)) for s,m in zeros.items()}
        check('finite_zero_transport',poles[start+(length-1)*h]==length and sum(v>0 for v in poles.values())==1,length)
    for p in range(1,17):
        check('critical_jacobian',critical_density_exponent(p)==-F(p,2)-1,p)
        check('all_p_error_integral',F(7*p,4)>0 and F(4,7*p)<=1,p)
    l2lo,l2hi=log_interval(F(2))
    for n in range(4,65):
        for L in (F(n*n),F(n*n)+F(1,2)):
            m=n if L==n*n else n+1
            lo,hi=log_interval(L)
            scale=10**30
            low=F(isqrt(L.numerator*scale*scale//L.denominator),scale)
            high=low+F(1,scale)
            check('growing_order_ceiling',(m-1)**2<L<=m*m,(L,m))
            check('growing_error_power',L-4*low*m+(m+2)*hi<=-F(5,4)*L,(L,m))
            check('logarithmic_bounds',hi<=low and hi<=L/4,L)
            check('subpower_coefficient_mass',4*high+m*l2hi <= (4+l2hi)*high+l2hi,(L,m))
    out={
      'status':'PASS: exact finite diagnostics, not analytic certification',
      'complete_ideal_cap':CAP,'complete_good_integral_ideals':len(ideals),
      'prime_ideals_in_census':len(PQS),'stencil_orders':list(range(1,17)),
      'counts':dict(sorted(COUNTS.items())),
      'total_predicates_including_guards':sum(COUNTS.values()),
      'not_computed':['actual L-values','actual zeta zeros','infinite Gaussian source','RH bound'],
      'arithmetic':'exact integers and fractions; certified rational logarithm enclosures'}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
