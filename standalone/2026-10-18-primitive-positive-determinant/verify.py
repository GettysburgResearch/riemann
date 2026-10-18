#!/usr/bin/env python3
"""Finite exact checks, NOT a certification of the infinite analytic theorems.

Python standard library only. Explicit checks remain active under python -O.
All transcendental acceptance tests use rational enclosing intervals.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache

class CheckFailure(RuntimeError):
    pass

COUNTS: Counter[str] = Counter()
MUTANT = ""

def check(ok: bool, gate: str) -> None:
    COUNTS[gate] += 1
    if not ok:
        raise CheckFailure(gate)

@lru_cache(None)
def divisors(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("positive integer required")
    return tuple(d for d in range(1, n + 1) if n % d == 0)

@lru_cache(None)
def mu(n: int) -> int:
    if n < 1:
        raise ValueError("positive integer required")
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign

@lru_cache(None)
def phi(n: int) -> int:
    return sum(math.gcd(a, n) == 1 for a in range(1, n + 1))

@lru_cache(None)
def prime_base(n: int) -> int:
    if n < 2:
        return 0
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return p if n == 1 else 0
    return n

def trim(a: list) -> list:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a: list, b: list, sign: int = 1) -> list:
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += sign * v
    return trim(c)

def mul(a: list, b: list) -> list:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)

def exact_div(a: list, b: list) -> list:
    a = [Q(v) for v in a]
    b = trim([Q(v) for v in b])
    if b == [0]:
        raise ValueError("zero polynomial divisor")
    out = [Q(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        j, v = len(a)-len(b), a[-1]/b[-1]
        out[j] += v
        for i, w in enumerate(b):
            a[i+j] -= v*w
        trim(a)
    if a != [0]:
        raise CheckFailure("nonexact_polynomial_division")
    if any(v.denominator != 1 for v in out):
        raise CheckFailure("noninteger_polynomial_quotient")
    return trim([v.numerator for v in out])

def evaluate(a: list, x: Q) -> Q:
    out = Q(0)
    for v in reversed(a):
        out = out*x + v
    return out

def determinant_polynomials(limit: int) -> tuple[dict, dict, dict]:
    cyc = {0:[0], 1:[0,1]}
    det = {1:[0,1]}
    cyclotomic = {1:[-1,1]}
    for n in range(2, limit+1):
        cyc[n] = add(add(mul([2,1],cyc[n-1]),cyc[n-2],-1),[0,2])
        denom = [1]
        cdenom = [1]
        for d in divisors(n)[:-1]:
            denom = mul(denom, det[d])
            cdenom = mul(cdenom, cyclotomic[d])
        det[n] = exact_div(cyc[n],denom)
        cyclotomic[n] = exact_div([-1]+[0]*(n-1)+[1],cdenom)
    return cyc,det,cyclotomic

def projector(n: int) -> list[list[Q]]:
    if MUTANT == "erase_projection":
        return [[Q(i==j) for j in range(n)] for i in range(n)]
    c = [sum(d*mu(n//d) for d in divisors(math.gcd(n,k))) for k in range(n)]
    return [[Q(c[(i-j)%n],n) for j in range(n)] for i in range(n)]

def matrix(n: int, t: Q, p: list[list[Q]]) -> list[list[Q]]:
    if MUTANT == "wrong_mass":
        t *= 2
    return [[Q(i==j)+(1+t)*p[i][j]-p[i][(j-1)%n]-p[i][(j+1)%n]
             for j in range(n)] for i in range(n)]

def ldlt(a: list[list[Q]]) -> tuple[Q, list[Q]]:
    n = len(a)
    l = [[Q(i==j) for j in range(n)] for i in range(n)]
    d = []
    for j in range(n):
        pivot = a[j][j]-sum(l[j][k]**2*d[k] for k in range(j))
        if pivot <= 0:
            raise CheckFailure("positive_ldlt")
        d.append(pivot)
        for i in range(j+1,n):
            l[i][j]=(a[i][j]-sum(l[i][k]*l[j][k]*d[k] for k in range(j)))/pivot
    return math.prod(d),d

# Rational interval primitives. No binary64 value enters acceptance.
Interval = tuple[Q,Q]
def plus(a: Interval,b: Interval) -> Interval:
    return a[0]+b[0],a[1]+b[1]
def scale(a: Interval,k: Q | int) -> Interval:
    return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def minus(a: Interval,b: Interval) -> Interval:
    return plus(a,scale(b,-1))

def unit_log_interval(y: Q, terms: int=14) -> Interval:
    if not Q(1)<=y<=Q(2):
        raise ValueError("log normalization range")
    z=(y-1)/(y+1)
    value=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
    tail=2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return value,value+tail

LOG2=unit_log_interval(Q(2))
@lru_cache(None)
def log_interval(x: Q) -> Interval:
    x=Q(x)
    if x<=0:
        raise ValueError("log requires positive input")
    k=x.numerator.bit_length()-x.denominator.bit_length()
    pow2=Q(2**k) if k>=0 else Q(1,2**(-k))
    y=x/pow2
    while y<1:
        k-=1; y*=2
    while y>=2:
        k+=1; y/=2
    return plus(unit_log_interval(y),scale(LOG2,k))

def decimal_outward(interval: Interval, digits: int=12) -> list[str]:
    power=10**digits
    def fmt(n: int) -> str:
        sign="-" if n<0 else ""
        n=abs(n)
        return f"{sign}{n//power}.{n%power:0{digits}d}"
    low=(interval[0]*power).__floor__()
    high=(interval[1]*power).__ceil__()
    return [fmt(low),fmt(high)]

@lru_cache(None)
def bernoulli(n: int) -> Q:
    if n==0:
        return Q(1)
    return -sum((Q(math.comb(n+1,k))*bernoulli(k) for k in range(n)),Q(0))/Q(n+1)

@lru_cache(None)
def zeta_interval(s: int, cutoff: int=96) -> Interval:
    if s<=1:
        raise ValueError("zeta exponent")
    part=sum((Q(1,n**s) for n in range(1,cutoff+1)),Q(0))
    return part+Q(1,(s-1)*(cutoff+1)**(s-1)),part+Q(1,(s-1)*cutoff**(s-1))

@lru_cache(None)
def drift_interval(c: Q, terms: int=8) -> Interval:
    if not 0<=c<=1:
        raise ValueError("declared drift certificate range")
    out=(Q(0),Q(0))
    for j in range(1,terms+1):
        z=zeta_interval(2*j+1)
        coef=bernoulli(2*j)*c**(2*j)/Q(2*j*math.factorial(2*j)*(2*j+1)*(2*j+2))
        out=plus(out,scale((1/z[1],1/z[0]),coef))
    # Euler's Bernoulli formula, zeta(2j)<2 and pi>3:
    # omitted |coefficient| <= 4/6^(2j), before other denominators.
    ratio=c*c/36
    tail=4*ratio**(terms+1)/(1-ratio)
    return out[0]-tail,out[1]+tail


def root4_ceil(x: Q) -> int:
    if x<0:
        raise ValueError("fourth root range")
    hi=1
    while Q(hi**4)<x:
        hi*=2
    lo=0
    while hi-lo>1:
        mid=(lo+hi)//2
        if Q(mid**4)>=x:
            hi=mid
        else:
            lo=mid
    return hi


def run() -> dict:
    cyc,dets,phis=determinant_polynomials(96)
    for n in range(2,97):
        check(dets[n][-1]==1 and all(x>0 for x in dets[n]),"integer_positive_polynomial")
        check(len(dets[n])-1==phi(n),"primitive_degree")
        pb=prime_base(n)
        if MUTANT=="drop_prime_powers" and pb and pb!=n:
            pb=0
        expected=(pb or 1)**2
        check(dets[n][0]==expected,"complete_prime_power_height")
        check(evaluate(phis[n],Q(1))**2==dets[n][0],"cyclotomic_height")
        prod=[1]
        for d in divisors(n):
            prod=mul(prod,dets[d])
        check(prod==cyc[n],"complete_cycle_factorization")

    for n in range(2,21):
        p=projector(n)
        check(sum(p[i][i] for i in range(n))==phi(n) and all(sum(row)==0 for row in p),
              "primitive_projection")
        check(all(p[i][j]==p[j][i] for i in range(n) for j in range(n)),"symmetric_projection")
        check(all(sum(p[i][k]*p[k][j] for k in range(n))==p[i][j]
                  for i in range(n) for j in range(n)),"idempotent_projection")
        for t in (Q(0),Q(1,16),Q(1)):
            h=matrix(n,t,p)
            value,pivots=ldlt(h)
            check(value==evaluate(dets[n],t),"matrix_polynomial_identity")
            check(all(h[i][i]==1+(1+t)*Q(phi(n),n)-Q(2*mu(n),n) for i in range(n)),
                  "coordinate_hadamard_diagonal")
            check(all(v>0 for v in pivots),"positive_ldlt_fixture")

    for N in range(2,65):
        ap=math.prod((prime_base(n) or 1)**(N-n) for n in range(2,N+1))
        lc,al=1,1
        for n in range(1,N):
            lc=math.lcm(lc,n); al*=lc
        ac=math.prod(int(evaluate(phis[n],Q(1)))**(N-n) for n in range(2,N+1))
        check(ap==al==ac,"full_integer_assembly")

    # Complete divisor-fiber comparisons with monomial test profiles, not
    # independently randomized coefficients. Unit n=1 is subtracted.
    for N in range(2,33):
        for k in (2,4,6,8):
            true=sum((N-n)*sum(mu(n//d)*d**k for d in divisors(n)) for n in range(2,N+1))
            sample_mu=lambda m:abs(mu(m)) if MUTANT=="unsigned_mobius" else mu(m)
            grouped=sum(sample_mu(m)*sum((N-m*d)*d**k for d in range(1,N//m+1))
                        for m in range(1,N+1))
            if MUTANT!="omit_unit":
                grouped-=N-1
            check(grouped==true,"complete_unit_corrected_regrouping")

    # Endpoint-aware quadrature on exact polynomial profiles f(u)=u^k.
    # The universal TV proof gives error <= m f(b/m)/3.
    for N in range(2,21):
        for m in range(1,N+1):
            for k in (2,4,6):
                b=Q(1,2)
                total=sum((N-m*d)*(b*Q(d,N))**k for d in range(1,N//m+1))
                integral=Q(N*N,m)*(b/Q(m))**k/Q((k+1)*(k+2))
                budget=Q(m,3)*(b/Q(m))**k
                check(abs(total-integral)<=budget,"endpoint_aware_quadrature")

    # Entire prime valuation rectangle vs a separately enumerated layer sum.
    for R in range(2,22):
        for S in range(1,9):
            for p in (2,3,5,7,11):
                actual=2*sum(min(r//p,S-1-s) for r in range(R) for s in range(S))
                factor=1 if MUTANT=="gram_factor" else 2
                layers=factor*sum((R-p*h)*(S-h) for h in range(1,min((R-1)//p,S-1)+1))
                check(actual==layers,"gram_valuation_layers")
                alpha=1-Q(1,R)-Q(1,2*S)
                low=alpha/Q(p)-Q(2,R)-Q(R,3*S*p*p)
                check(Q(actual,S*R*R)>=low,"all_prime_floor_budget")

    parameter_cases=0
    for R in (10**6,10**8,10**12,10**20,10**40):
        li=log_interval(Q(2*R))
        check(li[0].__ceil__()==li[1].__ceil__(),"exact_log_ceiling")
        B=li[1].__ceil__()
        qmax=R*R//(4096*B**4)
        for q in (3,5,13,101,qmax):
            if R*R<4096*q*B**4:
                continue
            S=R//B
            a=root4_ceil(Q(16*R*R*q))
            b=root4_ceil(Q(16*R*R,q))
            alpha=1-Q(1,R)-Q(1,2*S)
            P=(R+S-1)//S
            check(R>=64*B*B and B>=4,"short_conductor_setup")
            check(4*R<=a*b<=9*R and b<=a<=S and 4*S<=R,"balanced_short_grid")
            check(S*a*b>a*R+2*R*S+S*S,"strict_jet_rank_budget")
            check(alpha>=Q(127,128) and P<=B+1<=2*B,"finite_height_constants")
            parameter_cases+=1

    # Directed exponential bound used in the rational tau=1 disk.
    z=Q(1,2); terms=12
    exp_low=sum((z**j/Q(math.factorial(j)) for j in range(terms)),Q(0))
    exp_high=exp_low+z**terms/Q(math.factorial(terms))/(1-z/Q(terms+1))
    check(Q(1)<exp_low<=exp_high<Q(5,3),"rational_complex_disk_constant")

    # Synthetic zero geometry: these are NOT actual L-function zeros.
    for tau in (Q(1,4),Q(1),Q(2)):
        for u in (Q(0),Q(1,7),Q(1),Q(3)):
            for v in (Q(1,5),Q(1),Q(2)):
                for m in (1,2,3):
                    b=Q(9,10)
                    pair=(1 if MUTANT=="lose_conjugate" else 2)*m*(tau+u)/((tau+u)**2+v*v)
                    disk=(u+tau-Q(m)/b)**2+v*v-(Q(m)/b)**2
                    check(b*disk
                          ==((tau+u)**2+v*v)*(b-pair),"conjugate_disk_identity")

    # Exact Mellin continuum and interpolation signs.
    for s in (Q(3,2),Q(7,4),Q(5,2),Q(4)):
        lhs=(1/(s-1)-2/s+1/(s+1))/2
        if MUTANT=="wrong_continuum":
            lhs=1/(2*(s-1))
        check(lhs==1/((s-1)*s*(s+1)),"one_sided_continuum")
    for a in (Q(0),Q(1,7),Q(1,2),Q(4,5),Q(1)):
        check(0<=a*(1-a)/2<=Q(1,8),"integer_interpolation_cost")

    interval_cases=[]
    for N in (2,3,4,5,8,12,20,32,48,64):
        C=(Q(0),Q(0))
        for n in range(2,N+1):
            pb=prime_base(n)
            if pb:
                C=plus(C,scale(log_interval(Q(pb)),N-n))
        hn=sum((Q(1,m) for m in range(1,N+1)),Q(0))
        for c in (Q(1,4),Q(1,2),Q(1)):
            t=c*c/Q(N*N)
            V=(Q(0),Q(0))
            for n in range(2,N+1):
                if N!=n:
                    V=plus(V,scale(log_interval(evaluate(dets[n],t)),Q(N-n,2)))
            error=minus(minus(V,C),scale(drift_interval(c),N*N))
            bound=c*c*(hn/72+Q(1,24*N)+Q(1,576))+c**4/1728
            check(-bound<=error[0]<=error[1]<=bound,"certified_complete_regularization")
            interval_cases.append({"N":N,"c":str(c),"error_interval":decimal_outward(error,9),
                                   "rational_bound":str(bound)})
    report={
        "status":"PASS_FINITE_CHECKS",
        "analytic_proof_certified":False,
        "independent_referee":False,
        "arithmetic":"integer and rational; directed rational transcendental enclosures",
        "count_semantics":"One predicate per declared identity/case; matrix coordinates are grouped.",
        "predicates":sum(COUNTS.values()),
        "counts":dict(sorted(COUNTS.items())),
        "ranges":{"cycle_polynomials":"n=2..96","complete_matrices":"n=2..20, three masses",
                  "integer_assemblies":"N=2..64","short_conductor_parameter_fixtures":parameter_cases,
                  "source_note":"Parameter and zero fixtures are not a number-field or zero census."},
        "B_1_interval":decimal_outward(drift_interval(Q(1)),12),
        "regularization_cases":interval_cases,
    }
    return report


def main() -> int:
    global MUTANT
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutant",choices=("erase_projection","wrong_mass","drop_prime_powers",
        "unsigned_mobius","omit_unit","gram_factor","lose_conjugate","wrong_continuum"),default="")
    args=parser.parse_args()
    MUTANT=args.mutant
    try:
        result=run()
    except CheckFailure as exc:
        print("REJECT:"+str(exc),file=sys.stderr)
        return 2
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
