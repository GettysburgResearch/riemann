#!/usr/bin/env python3
"""Replay for tensor phase current collapse and four-adic Hilbert bound.

Classification:
    EXACT FINITE ARITHMETIC + FLOATING ROOT-OF-UNITY REGRESSION

The script checks finite DFT/current identities, the binomial current law,
phase-separated first/second moments, the two-layer support theorem, and
finite weighted-norm inequalities. It does not prove Montgomery--Vaughan,
the complete reflected floor, or RH.
"""
from __future__ import annotations
import cmath
import itertools
import json
import math
import random
from pathlib import Path

TOL = 5e-10

def roots(M: int) -> list[complex]:
    return [cmath.exp(2j * math.pi * j / M) for j in range(M)]

def mobius(n: int) -> int:
    x=n
    mu=1
    p=2
    while p*p<=x:
        if x%p==0:
            x//=p
            mu=-mu
            if x%p==0:
                return 0
            while x%p==0:
                x//=p
        p+=1
    if x>1:
        mu=-mu
    return mu

def bsharp(n: int) -> int:
    return mobius(n) - (4*mobius(n//4) if n%4==0 else 0)

def v4(n: int) -> int:
    r=0
    while n%4==0:
        n//=4
        r+=1
    return r

def assert_close(x: complex|float, y: complex|float, tol: float=TOL) -> None:
    if abs(x-y) > tol*max(1.0,abs(y)):
        raise AssertionError(f"{x!r} != {y!r}")

def check_tensor_dft() -> int:
    checks=0
    for k in range(1,5):
        M=7
        O=roots(M)
        a=1.17+0.31j
        B=0.43-0.19j
        q=-0.27+0.81j
        L=0.93
        rows=[]
        for omega in itertools.product(O, repeat=k):
            F=1+0j
            for w in omega:
                F*=1-w*a
            Fp=0j
            for ell,w in enumerate(omega):
                prod=1+0j
                for m,w2 in enumerate(omega):
                    if m!=ell:
                        prod*=1-w2*a
                Fp += L*w*a*prod
            rows.append((omega,F*B,F*q+Fp*B))
        for mask in range(1<<k):
            r=mask.bit_count()
            Bh=0j
            qh=0j
            for omega,Bv,qv in rows:
                chi=1+0j
                for ell in range(k):
                    if (mask>>ell)&1:
                        chi*=omega[ell]
                Bh += chi.conjugate()*Bv
                qh += chi.conjugate()*qv
            Bh/=M**k
            qh/=M**k
            assert_close(Bh,(-a)**r*B)
            assert_close(qh,(-a)**r*(q-r*L*B))
            checks+=2
    return checks

def check_frame_and_binomial() -> int:
    checks=0
    for k in range(1,7):
        M=7
        O=roots(M)
        a=2*cmath.exp(0.37j)
        B=0.31+0.17j
        q=-0.42+0.76j
        L=math.log(4)
        frame=0.0
        current=0.0
        for omega in itertools.product(O, repeat=k):
            F=1+0j
            Fp=0j
            for w in omega:
                F*=1-w*a
            for ell,w in enumerate(omega):
                prod=1+0j
                for m,w2 in enumerate(omega):
                    if m!=ell:
                        prod*=1-w2*a
                Fp += L*w*a*prod
            frame += abs(F)**2
            current += abs(F*q+Fp*B)**2
        frame/=M**k
        current/=M**k*5**k
        assert_close(frame,5**k)
        expected=abs(q-(4*k/5)*L*B)**2+(4*k/25)*L*L*abs(B)**2
        assert_close(current,expected)
        checks+=2
    return checks

def check_phase_reserve() -> int:
    checks=0
    M=11
    O=roots(M)
    P0=1.7
    d=[0.0,0.9,-1.2,0.4]
    for k in range(1,4):
        first=0.0
        phase_second=0j
        for omega in itertools.product(O,repeat=k):
            P=P0
            local=[]
            for w in omega:
                z=sum((w**r)*d[r] for r in range(1,len(d)))
                P+=z
                local.append(z)
            first+=abs(P)**2
            phase_second += sum(local) + 2*P0*sum(local)
            phase_second += sum(z*z for z in local)
            phase_second += sum(local[i]*local[j] for i in range(k) for j in range(k) if i!=j)
        first/=M**k
        phase_second/=M**k
        expected=P0**2+k*sum(x*x for x in d[1:])
        assert_close(first,expected)
        assert_close(phase_second,0.0)
        checks+=2
    return checks

def check_two_layer_support(limit: int=20000) -> int:
    checks=0
    for n in range(1,limit+1):
        b=bsharp(n)
        if b:
            if v4(n) not in (0,1):
                raise AssertionError((n,b,v4(n)))
            if abs(b)>4:
                raise AssertionError((n,b))
        checks+=1
    for n in range(1,limit+1):
        active=[]
        for r in range(0,12):
            if n%(4**r)==0 and bsharp(n//(4**r)):
                active.append(r)
        if len(active)>2:
            raise AssertionError((n,active))
        if any(abs(active[i]-active[j])>1 for i in range(len(active)) for j in range(len(active))):
            raise AssertionError((n,active))
        checks+=1
    return checks

def coefficient_norm(h: list[complex], X: int, deriv: int) -> float:
    coeff=[0j]*(X+1)
    for r,hr in enumerate(h):
        scale=4**r
        for m in range(1,X//scale+1):
            b=bsharp(m)
            if not b:
                continue
            n=scale*m
            coeff[n] += hr*scale*b*((-math.log(n))**deriv)
    return sum(abs(coeff[n])**2/n for n in range(1,X+1))

def check_weighted_bounds() -> int:
    rng=random.Random(237041)
    checks=0
    for X in (64,257,1024,4096):
        R=int(math.log(X,4))
        for _ in range(20):
            h=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(R+1)]
            crit=sum((4**r)*abs(hr)**2 for r,hr in enumerate(h))
            if crit==0:
                continue
            h=[hr/math.sqrt(crit) for hr in h]
            for deriv in (0,1,2):
                actual=coefficient_norm(h,X,deriv)
                bound=32*(1+math.log(X))*(math.log(X)**(2*deriv) if deriv else 1)
                if actual>bound*(1+1e-12):
                    raise AssertionError((X,deriv,actual,bound))
                checks+=1
    return checks

def check_coherent_polynomial_norm() -> int:
    rng=random.Random(501)
    checks=0
    for k in range(1,12):
        vals=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(1<<k)]
        norm=math.sqrt(sum(abs(z)**2 for z in vals))
        vals=[z/norm for z in vals]
        h=[]
        for r in range(k+1):
            total=sum(vals[mask] for mask in range(1<<k) if mask.bit_count()==r)
            h.append(((-1)**r)*total/(5**(k/2)))
        crit=sum(4**r*abs(h[r])**2 for r in range(k+1))
        if crit>1+2e-12:
            raise AssertionError((k,crit))
        checks+=1
    return checks

def main() -> None:
    counts={
        "tensor_dft":check_tensor_dft(),
        "critical_frame_and_binomial_current":check_frame_and_binomial(),
        "phase_reserve":check_phase_reserve(),
        "two_layer_support":check_two_layer_support(),
        "weighted_norm_bounds":check_weighted_bounds(),
        "coherent_polynomial_norm":check_coherent_polynomial_norm(),
    }
    payload={
        "classification":"PASS_TENSOR_PHASE_CURRENT_HILBERT_BOUND",
        "arithmetic_class":"EXACT_FINITE_PLUS_FLOATING_ROOT_OF_UNITY",
        "checks":counts,
        "not_certified":[
            "Montgomery-Vaughan mean-value theorem",
            "complete reflected arithmetic floor",
            "Riemann Hypothesis",
        ],
    }
    out=Path(__file__).with_name("verification.json")
    out.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2,sort_keys=True))
if __name__=="__main__":
    main()
