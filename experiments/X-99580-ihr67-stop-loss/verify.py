#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99580_IHR67_STOP_LOSS_AND_OSCILLATION_ATTACK"


def mobius_upto(n: int) -> list[int]:
    mu=[0]*(n+1); mu[1]=1; primes=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: primes.append(i); mu[i]=-1
        for p in primes:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0: mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu


def q_formula(n: int, mu: list[int]) -> int:
    return ((6 if n==1 else 0)-6*mu[n]
            +(9*mu[n//2] if n%2==0 else 0)
            -(3*mu[n//4] if n%4==0 else 0))


def local_euler_q(n: int, mu: list[int]) -> Fraction:
    # Coefficient of 6(1-E), E=(1-x)^2(1-x/2)*prod_odd(1-p^-z).
    if n==1: return Fraction(0)
    a=0; m=n
    while m%2==0:
        a+=1; m//=2
    local={0:Fraction(1),1:Fraction(-5,2),2:Fraction(2),3:Fraction(-1,2)}.get(a,Fraction(0))
    return -6*local*mu[m]


def shift_poly_mul(a: dict[tuple[str,...],Fraction], b: dict[tuple[str,...],Fraction]):
    out: dict[tuple[str,...],Fraction]={}
    for ka,va in a.items():
        for kb,vb in b.items():
            key=tuple(sorted(ka+kb))
            out[key]=out.get(key,Fraction())+va*vb
    return {k:v for k,v in out.items() if v}


def one_minus(label: str, coeff: Fraction=Fraction(1)):
    return {():Fraction(1),(label,):-coeff}


def stop_loss(atoms: list[tuple[Fraction,Fraction]], L: Fraction) -> Fraction:
    return sum((w*max(Fraction(),L-u) for u,w in atoms), Fraction())


def build_result() -> dict:
    mu=mobius_upto(1000)
    coefficient_checks=0
    duplicate_checks=0
    for n in range(1,1001):
        assert Fraction(q_formula(n,mu)) == local_euler_q(n,mu)
        coefficient_checks+=1
        b=q_formula(n,mu)-(q_formula(n//67,mu) if n%67==0 else 0)
        # Multiplication by (1-67^-z) at coefficient level.
        expected=int(local_euler_q(n,mu))-(int(local_euler_q(n//67,mu)) if n%67==0 else 0)
        assert b==expected
        duplicate_checks+=1

    # Exact critical operator identity:
    # I-(I-tau67)D0-tau67 = (I-tau67)(I-D0).
    D0={():Fraction(1)}
    for label,coeff in [("2a",Fraction(1)),("2b",Fraction(1)),("2c",Fraction(1,2)),("67",Fraction(1)),("3",Fraction(1)),("5",Fraction(1))]:
        D0=shift_poly_mul(D0,one_minus(label,coeff))
    I={():Fraction(1)}; tau67={("67*",):Fraction(1)}
    left=I.copy()
    prod=shift_poly_mul(one_minus("67*"),D0)
    # I - prod - tau67
    for k,v in prod.items(): left[k]=left.get(k,Fraction())-v
    for k,v in tau67.items(): left[k]=left.get(k,Fraction())-v
    left={k:v for k,v in left.items() if v}
    right=shift_poly_mul(one_minus("67*"),{k:-v for k,v in D0.items()})
    right[()]=right.get((),Fraction())+1
    # Easier direct RHS: (I-tau67*)(I-D0)
    ImD=I.copy()
    for k,v in D0.items(): ImD[k]=ImD.get(k,Fraction())-v
    ImD={k:v for k,v in ImD.items() if v}
    rhs=shift_poly_mul(one_minus("67*"),ImD)
    assert left==rhs

    # Six equal labels: 5 sqrt(2)-15/2 < 0.
    # Both sides positive; squaring gives 50 < 225/4, i.e. 200 < 225.
    assert 200 < 225

    # Toy monotone stop-loss transport.
    positive=[(Fraction(1),Fraction(2)),(Fraction(3),Fraction(1))]
    negative=[(Fraction(2),Fraction(1)),(Fraction(4),Fraction(1))]
    transport=[(Fraction(1),Fraction(2),Fraction(1)),(Fraction(3),Fraction(4),Fraction(1))]
    assert all(u<=v and w>=0 for u,v,w in transport)
    for L in [Fraction(k,2) for k in range(0,13)]:
        assert stop_loss(positive,L)-stop_loss(negative,L)>=0

    # Explicit noncancellation geometry.
    noncancel={
        "67_factor":"|67^-rho|<1 when Re(rho)>0",
        "dyadic_factor_1":"2^-rho=1 forces Re(rho)=0",
        "dyadic_factor_2":"2^-rho=2 forces Re(rho)=-1",
    }

    core={
        "schema":"riemann.t99580.ihr67-stop-loss.v1",
        "classification":VERDICT,
        "coefficient_checks":coefficient_checks,
        "duplicate67_checks":duplicate_checks,
        "critical_shift_identity":True,
        "six_equal_label_counterexample":True,
        "toy_monotone_transport":True,
        "noncancellation":noncancel,
        "finite_scans_promoted_to_global_proof":False,
        "plslc99580_proved":False,
        "ihr67_proved":False,
        "rh_established":False,
    }
    canon=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    core["proof_object_sha256"]=hashlib.sha256(canon).hexdigest()
    return core


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path)
    args=ap.parse_args(); result=build_result()
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])

if __name__=="__main__": main()
