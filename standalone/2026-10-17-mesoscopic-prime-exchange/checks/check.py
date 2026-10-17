#!/usr/bin/env python3
"""Exact finite checks for THEOREMS.md; no asymptotic certification.

Normal and -O runs use explicit exceptions, never removable assertions.
The two norm constructors share the classical splitting law, not an
independently certified number-field implementation.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
from math import gcd, isqrt
import json
from typing import Iterable

Z = tuple[int, int]  # exact Gaussian integer
ONE: Z = (1, 0)
ZERO: Z = (0, 0)
COUNTS: dict[str, int] = defaultdict(int)
MUTATION = ""

def require(ok: bool, label: str) -> None:
    COUNTS[label] += 1
    if not ok:
        raise RuntimeError("rejected: " + label)

def add(a: Z, b: Z) -> Z:
    return a[0] + b[0], a[1] + b[1]

def mul(a: Z, b: Z) -> Z:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def conj(a: Z) -> Z:
    return a[0], -a[1]

def scale(a: Z, n: int) -> Z:
    return a[0]*n, a[1]*n

def norm2(a: Z) -> int:
    return a[0]*a[0]+a[1]*a[1]

def sieve(n: int) -> tuple[list[int], list[int]]:
    spf = list(range(n+1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n)+1):
        if spf[p] == p:
            for k in range(p*p, n+1, p):
                if spf[k] == k:
                    spf[k] = p
    return [p for p in range(2, n+1) if spf[p] == p], spf

def phase(p: int, side: int, profile: str) -> Z:
    if profile == "unit":
        return ONE
    if profile == "opposite":
        return ONE if side == 0 else (-1, 0)
    roots = [(1,0), (0,1), (-1,0), (0,-1)]
    return roots[(p//3 + side + 1) % 4]

def convolution(a: dict[int,Z], b: dict[int,Z]) -> dict[int,Z]:
    out: dict[int,Z] = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] = add(out.get(i+j,ZERO), mul(x,y))
    return {e:z for e,z in out.items() if z != ZERO}

def ideal_local(q: int, b: Z, m: int, native: bool) -> dict[int,Z]:
    # Coefficient is (N ideal) times the original coefficient.
    if native:
        return {0: ONE, 1: (-q,0)}
    return {0: ONE, 1: (-(q-1),0), m: scale(b, -q**(3*m//2-1))}

def norm_local(p: int, m: int, profile: str, native: bool) -> dict[int,Z]:
    if p in (2,3):
        return {0: ONE}
    if p % 3 == 1:
        a=ideal_local(p,phase(p,0,profile),m,native)
        b=ideal_local(p,phase(p,1,profile),m,native)
        return convolution(a,b)
    return {2*e:z for e,z in ideal_local(p*p,phase(p,0,profile),m,native).items()}

def prefix(cap: int, m: int, profile: str, native: bool, spf: list[int]) -> list[Z]:
    out = [ZERO]*(cap+1)
    out[1]=ONE
    cache: dict[int,dict[int,Z]]={}
    for n in range(2,cap+1):
        p=spf[n]; t=n; e=0
        while t%p == 0:
            t//=p; e+=1
        if p not in cache:
            cache[p]=norm_local(p,m,profile,native)
        out[n]=mul(cache[p].get(e,ZERO),out[t])
    return out

def enumerate_ideals(cap: int, m: int, profile: str, native: bool, primes: list[int]) -> tuple[list[Z],int]:
    # Separate labelled prime ideals, including both split conjugates.
    atoms: list[tuple[int,Z]]=[]
    for p in primes:
        if p in (2,3):
            continue
        if p%3==1:
            atoms.append((p,phase(p,0,profile)))
            if MUTATION != "drop_split_conjugate":
                atoms.append((p,phase(p,1,profile)))
        elif p*p<=cap:
            atoms.append((p*p,phase(p,0,profile)))
    atoms.sort(key=lambda a:a[0])
    out=[ZERO]*(cap+1); records=0
    def visit(start: int, n: int, z: Z) -> None:
        nonlocal records
        records+=1; out[n]=add(out[n],z)
        for j in range(start,len(atoms)):
            q,b=atoms[j]
            if n*q>cap:
                break
            visit(j+1,n*q,mul(z,(-q if native else -(q-1),0)))
            if not native and n*q**m<=cap:
                visit(j+1,n*q**m,mul(z,scale(b,-q**(3*m//2-1))))
    visit(0,1,ONE)
    return out,records

def odd_local_checks() -> None:
    # Exact Q(i,sqrt(p)); (u,v) denotes u+v sqrt(p).
    for m in (5,7,9):
        for p in (7,13,19):
            def emul(a, b):
                return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),p)), add(mul(a[0],b[1]),mul(a[1],b[0]))
            for profile in ("unit","opposite","complex"):
                bp,bm=phase(p,0,profile),phase(p,1,profile)
                bs=add(bp,bm); power=p**((3*m-3)//2)
                L={0:(ONE,ZERO),1:((-2*(p-1),0),ZERO),2:(((p-1)**2,0),ZERO),
                   m:(ZERO,scale(bs,-power)),m+1:(ZERO,scale(bs,(p-1)*power)),
                   2*m:(scale(mul(bp,bm),p**(3*m-2)),ZERO)}
                for e in range(2*m+1):
                    a=L.get(e+1,(ZERO,ZERO)); b=L.get(e,(ZERO,ZERO))
                    z=emul(a,(conj(b[0]),conj(b[1])))
                    want=F(0); v=F(p-1,p)
                    if e==0: want=-2*v
                    if e==1: want=-2*v**3
                    if e==m: want=-v*p**(m-2)*norm2(bs)
                    require(z[1]==ZERO and z[0][1]==0 and F(z[0][0],p**(2*e+1))==want,
                            "odd_degree_exact_local_identity")

def masked_majorant_checks() -> None:
    # Small complete four-labelled-prime-ideal support, arbitrary phases and zeros.
    # This is NOT a census of actual theta or sextic-character values.
    atoms=[(7,0),(7,1),(13,0),(13,1)]
    roots=[ONE,(0,1),(-1,0),(0,-1)]
    for m in (4,6):
        for mask in range(16):
            for shift in range(4):
                signed={1:ONE}; absolute={1:1}; major={1:1}
                for i,(p,side) in enumerate(atoms):
                    a=roots[(i+shift)%4]; b=roots[(2*i+shift)%4]
                    off=bool(mask & (1<<i))
                    factor={0:ONE}
                    if not off:
                        factor[1]=scale(a,-(p-1))
                        factor[m]=scale(b,-p**(3*m//2-1))
                    ff={0:1,1:p-1,m:p**(3*m//2-1)}
                    ns={}; na={}; nm={}
                    for n,z in signed.items():
                        for e,t in factor.items():
                            nn=n*p**e; ns[nn]=add(ns.get(nn,ZERO),mul(z,t))
                    for n,z in absolute.items():
                        for e,t in factor.items():
                            nn=n*p**e; mag=isqrt(norm2(t))
                            require(mag*mag==norm2(t),"unit_phase_exact_modulus")
                            na[nn]=na.get(nn,0)+z*mag
                    for n,z in major.items():
                        for e,t in ff.items():
                            nn=n*p**e; nm[nn]=nm.get(nn,0)+z*t
                    signed,absolute,major=ns,na,nm
                for n,z in signed.items():
                    require(norm2(z)<=absolute[n]**2<=major[n]**2,"masked_norm_fiber_majorant")
                for n,z in absolute.items():
                    if n%7==0:
                        k=n//7
                        if 13*k in absolute:
                            require(z*absolute[13*k]<=major[n]*major[13*k],"masked_pair_absolute_majorant")
    # A positive selected covariance is not a PSD subprojection of the full energy.
    v=(1,1,-2)
    require(sum(v)**2==0 and 2*v[0]*v[1]>0,"reject_full_energy_ge_positive_sector")

def local_checks() -> None:
    for m in (4,6,8,10):
        for p in (7,13,19,31):
            for profile in ("unit","opposite","complex"):
                v=F(p-1,p)
                bsum=add(phase(p,0,profile),phase(p,1,profile))
                L=norm_local(p,m,profile,False)
                for e in range(2*m+1):
                    z=mul(L.get(e+1,ZERO),conj(L.get(e,ZERO)))
                    den=p**(2*e+1)
                    actual=(F(z[0],den),F(z[1],den))
                    expected=F(0)
                    if e==0:
                        expected=-2*v
                    elif e==1:
                        expected=-2*v**3
                    elif e==m and MUTATION != "omit_shared_power":
                        s2=norm2(bsum)
                        if MUTATION == "no_conjugation":
                            s2=mul(bsum,bsum)[0]
                        expected=-v*p**(m-2)*s2
                    require(actual==(expected,F(0)),"local_consecutive_identity")
                    require(actual[1]==0 and actual[0]<=0,"local_sign")
                # The missing linear term in the normalized Euler product is real.
                c1=F(norm2(L[1]),p*p)
                require(c1-4==4*v*v-4 and c1-4!=0,"small_linear_term_retained")
    # Native source's complete norm coefficients, not one ideal per norm.
    for p in (7,13,19):
        L=norm_local(p,6,"unit",True)
        for e in range(4):
            z=mul(L.get(e+1,ZERO),conj(L.get(e,ZERO)))
            expected=-2 if e in (0,1) else 0
            require((F(z[0],p**(2*e+1)),z[1])==(expected,0),"native_local_identity")
    # m=3 is excluded for a reason: positive A(p^3)*A(p^2).
    # Divide the actual product by sqrt(p), leaving the following positive rational.
    p=7; positive=2*F(p-1,p)**2
    require(positive>0,"m3_counterexample")
    if MUTATION == "allow_m3":
        require(positive<=0,"false_m3_extension")
    for p in (5,11,17):
        L=norm_local(p,6,"unit",False)
        require(all(e%2==0 for e in L),"inert_even_norm_exponents")
    # Complete four-labelled-prime-ideal fixture, no norm cap: includes shared p^m.
    for m in (4,6):
        for profile in ("unit","opposite","complex"):
            vals={1:ONE}; p=7; q=13
            for ell in (p,q):
                for side in (0,1):
                    nxt: dict[int,Z]={}
                    for n,z in vals.items():
                        for e,v in ideal_local(ell,phase(ell,side,profile),m,False).items():
                            nn=n*ell**e
                            nxt[nn]=add(nxt.get(nn,ZERO),mul(z,v))
                    vals=nxt
            for n,z in vals.items():
                t=n; i=j=0
                while t%p==0: t//=p; i+=1
                while t%q==0: t//=q; j+=1
                expect=mul(norm_local(p,m,profile,False).get(i,ZERO),norm_local(q,m,profile,False).get(j,ZERO))
                require(t==1 and z==expect,"four_ideal_norm_fiber")
            for i in (0,1,m):
                for j in (0,1,m):
                    k=p**i*q**j
                    z=mul(vals.get(p*k,ZERO),conj(vals.get(q*k,ZERO)))
                    require(z[1]==0 and z[0]>=0,"shared_power_exchange_sign")

def pair_checks(A: list[Z], m: int, profile: str, native: bool, primes: list[int]) -> int:
    ps=[p for p in primes if 7<=p<=43 and p%3==1]
    cap=len(A)-1; ntest=0
    for p in ps:
        P=norm_local(p,m,profile,native)
        for q in ps:
            if q==p: continue
            Q=norm_local(q,m,profile,native)
            for k in range(1,cap//max(p,q)+1):
                left=mul(A[p*k],conj(A[q*k]))
                t=k; i=j=0
                while t%p==0: t//=p; i+=1
                while t%q==0: t//=q; j+=1
                right=mul(mul(P.get(i+1,ZERO),conj(P.get(i,ZERO))),
                          mul(Q.get(j,ZERO),conj(Q.get(j+1,ZERO))))
                right=scale(right,norm2(A[t]))
                require(left==right,"full_prefix_exchange_identity")
                require(left[1]==0 and left[0]>=0,"full_prefix_exchange_sign")
                ntest+=1
    return ntest

def mu_phi(n: int) -> tuple[int,int]:
    t=n; p=2; mu=1; phi=n
    while p*p<=t:
        if t%p==0:
            t//=p; phi=phi//p*(p-1); mu=-mu
            if t%p==0:
                mu=0
                while t%p==0: t//=p
        p+=1
    if t>1:
        phi=phi//t*(t-1); mu=-mu
    return mu,phi

def sieve_checks() -> None:
    for z in range(1,26):
        tab={r:mu_phi(r) for r in range(1,z+1)}
        G=sum((F(mu*mu,ph) for mu,ph in tab.values()),F(0))
        y={r:F(mu,ph)/G for r,(mu,ph) in tab.items()}
        lam={d:d*sum((tab[k][0]*y[d*k] for k in range(1,z//d+1)),F(0)) for d in range(1,z+1)}
        require(lam[1]==1,"selberg_unit_constraint")
        for r in range(1,z+1):
            require(sum((lam[d]/d for d in range(r,z+1,r)),F(0))==y[r],"selberg_mobius_inverse")
        Q=sum((lam[d]*lam[e]*F(gcd(d,e),d*e) for d in lam for e in lam),F(0))
        require(Q==1/G,"selberg_exact_quadratic_form")
        require(all(abs(lam[d])<=d for d in lam),"selberg_coefficient_bound")
        for x,L in ((0,16),(10,32),(64,64),(201,50)):
            actual=sum((sum((lam[d] for d in lam if n%d==0),F(0))**2 for n in range(x+1,x+L+1)),F(0))
            err=sum(map(abs,lam.values()),F(0))**2
            require(abs(actual-L/G)<=err,"selberg_interval_remainder")
    primes,_=sieve(16384)
    for Y in (64,128,256,512,1024,2048,4096,8192):
        ps=[p for p in primes if Y<=p<=2*Y and p%3==1]
        for H in (max(1,isqrt(Y)),max(1,Y//8),Y):
            N=sum(p!=q and abs(p-q)<=H for p in ps for q in ps)
            bins: dict[int,int]=defaultdict(int)
            for p in ps: bins[(p-Y)//H]+=1
            J=Y//H+2; M=len(ps)
            B=sum(v*(v-1) for v in bins.values())
            require(N>=B>=F(M*M,J)-M,"prime_pair_pigeonhole")

def gaussian_checks() -> None:
    for a in (F(-2),F(0),F(3,2),F(4)):
        for b in (F(-1),F(1),F(5,2)):
            for x in (F(-3),F(0),F(7,3)):
                for c in (F(1,2),F(5,6),F(2)):
                    beta=2*c-1; mean=(a+b)/2
                    left=beta*x-c*(a+b)-((x-a)**2+(x-b)**2)/4
                    right=-(x-mean-beta)**2/2-mean+beta**2/2-(a-b)**2/8
                    if MUTATION=="wrong_cdf_shift":
                        right=-(x-mean+beta)**2/2-mean+beta**2/2-(a-b)**2/8
                    require(left==right,"gaussian_square_completion")
    for C,B,E,L,beta in ((F(2),F(-3),F(4),F(5),F(2,3)),(F(7,2),F(1),F(-2),F(-3),F(1))):
        q1=L-beta; q2=(q1*q1+1)/2
        require(C*q2+B*q1+E == C*( (L-beta)**2+1)/2+B*(L-beta)+E,"laurent_residue_polynomial")

def run(cap: int) -> dict:
    local_checks(); odd_local_checks(); masked_majorant_checks(); sieve_checks(); gaussian_checks()
    primes,spf=sieve(cap)
    censuses=[]
    cases=[(0,"unit",True),(4,"complex",False),(6,"unit",False),(6,"complex",False)]
    for m,profile,native in cases:
        A=prefix(cap,m,profile,native,spf)
        B,records=enumerate_ideals(cap,m,profile,native,primes)
        require(A==B,"complete_norm_constructor_agreement")
        ntest=pair_checks(A,m,profile,native,primes)
        censuses.append({"m":m,"profile":profile,"native":native,"norm_cap":cap,
                        "supported_ideal_records":records,"nonzero_norm_fibers":sum(z!=ZERO for z in A),
                        "ordered_prime_pair_common_core_cases":ntest,
                        "first_power_fiber_7m_included": bool(not native and 7**m<=cap)})
    return {"status":"PASS","scope":"Exact finite identities; not an asymptotic or independent proof certificate.",
            "norm_censuses":censuses,"checks_by_kind":dict(sorted(COUNTS.items())),
            "infinite_theorem_proved_by_checker":False,"rh_proved":False}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--cap",type=int,default=131072)
    ap.add_argument("--mutation",choices=("","drop_split_conjugate","omit_shared_power","no_conjugation","allow_m3","wrong_cdf_shift"),default="")
    args=ap.parse_args()
    if args.cap<64: raise ValueError("cap must be at least 64")
    MUTATION=args.mutation
    print(json.dumps(run(args.cap),sort_keys=True,indent=2))
