#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path

def mobius_sieve(n: int) -> list[int]:
    mu=[1]*(n+1)
    mu[0]=0
    prime=[True]*(n+1)
    if n>=0: prime[0]=False
    if n>=1: prime[1]=False
    p=2
    while p*p<=n:
        if prime[p]:
            for k in range(p*p,n+1,p):
                prime[k]=False
        p+=1
    for p in range(2,n+1):
        if prime[p]:
            for k in range(p,n+1,p):
                mu[k]*=-1
            pp=p*p
            for k in range(pp,n+1,pp):
                mu[k]=0
    return mu

def mu_at(mu: list[int], n: int, d: int) -> int:
    return mu[n//d] if n % d == 0 else 0

def a2(mu: list[int], n: int) -> int:
    return (1 if n==1 else 0)-mu[n]+2*mu_at(mu,n,2)-mu_at(mu,n,3)

def a3x3(mu: list[int], n: int) -> int:
    return ((1 if n==1 else 0)-mu[n]-mu_at(mu,n,2)
            +5*mu_at(mu,n,3)-3*mu_at(mu,n,4))

def q(j: int, m: int) -> Fraction:
    if m<j: return Fraction(0)
    if m==j: return Fraction(j+1,j-1)
    if m==j+1: return -Fraction((j+1)*(j-2),j*(j-1))
    return Fraction(2,j*(j-1))

def divisors(n: int):
    return [d for d in range(1,n+1) if n%d==0]

def convolution_coeff(mu: list[int], j: int, n: int) -> Fraction:
    return sum(Fraction(mu[d])*q(j,n//d) for d in divisors(n))

def exact_checks(limit: int = 5000) -> dict:
    mu=mobius_sieve(limit)
    residual=sum(Fraction((1 if d in (1,6) else -1))*q(3,24//d)
                 for d in (1,2,3,6))
    assert residual == -1

    rough=[m for m in range(2,10) if math.gcd(m,30)==1]
    assert rough == [7]
    assert 4 < 7
    assert 16 < 18
    assert 1331 < 1600

    for n in range(1,limit+1):
        assert convolution_coeff(mu,2,n) == a2(mu,n)
        assert 3*convolution_coeff(mu,3,n) == a3x3(mu,n)

    r2_expected={(0,0):-1,(0,2):1,(1,0):3,(1,1):-2,(1,2):-1,(2,0):-2,(2,1):2}
    r3_expected={(0,0):-1,(0,1):6,(0,2):-5,(1,1):-5,(1,2):5,
                 (2,0):-2,(2,1):2,(3,0):3,(3,1):-3}
    r2={};r3={}
    for aa in range(5):
        for bb in range(4):
            n=(2**aa)*(3**bb)*5
            v2=-a2(mu,n)
            v3=-a3x3(mu,n)
            if v2: r2[(aa,bb)]=v2
            if v3: r3[(aa,bb)]=v3
    assert r2==r2_expected
    assert r3==r3_expected

    common_poly=(-3,9,-6)
    assert common_poly[0]+common_poly[1]+common_poly[2] == 0
    assert 4*common_poly[0]+2*common_poly[1]+common_poly[2] == 0

    return {
        "fixed_product":{"j":3,"P":6,"n":24,"residual":str(residual)},
        "rough_store":{"P":30,"p":5,"u":2,"block":[2,10],
                       "actual_rough_integers":rough,
                       "exact_upper_statement":"1/sqrt(7)<1/2",
                       "claimed_lower_statement":"sqrt(2)*log(5)>2"},
        "coefficient_identity_limit":limit,
        "r2_table":{f"{a},{b}":v for (a,b),v in sorted(r2.items())},
        "r3_table":{f"{a},{b}":v for (a,b),v in sorted(r3.items())},
        "common_zero_polynomial":list(common_poly)
    }

def diagnostic_scan(nmax: int = 200000) -> dict:
    mu=mobius_sieve(nmax)
    out={}
    for j in (2,3):
        M=0.0
        L=0.0
        min_c=1e300
        min_n=None
        for n in range(1,nmax+1):
            av=float(a2(mu,n) if j==2 else Fraction(a3x3(mu,n),3))
            if av:
                w=av/math.sqrt(n)
                M+=w
                L+=w*math.log(n)
            if n>=j+1:
                c=math.log(n)*M-L
                if c<min_c:
                    min_c=c; min_n=n
        out[str(j)]={"range":[j+1,nmax],"minimum_float":min_c,
                     "minimum_at":min_n,"final_float":math.log(nmax)*M-L,
                     "classification":"diagnostic_only"}
    return out

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    ap.add_argument("--limit",type=int,default=5000)
    ap.add_argument("--scan",type=int,default=200000)
    args=ap.parse_args()
    result={
        "schema":"riemann.x96400.v1",
        "classification":"PASS_T96400_PRIME_SIEVED_HARDENING_EXACT_ALGEBRA",
        "exact":exact_checks(args.limit),
        "diagnostic":diagnostic_scan(args.scan),
        "scope":{"fixed_product_frontier_chain_proved":False,
                 "global_rough_block_transport_proved":False,
                 "two_row_algebra_checked":True,
                 "TRP23_proved":False,"RH_established":False}
    }
    canonical=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    result["proof_object_sha256"]=hashlib.sha256(canonical).hexdigest()
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(result["proof_object_sha256"])

if __name__=="__main__":
    main()
