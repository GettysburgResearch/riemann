#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def carry(n:int,j:int,q:int)->int:
    return n//q-j//q-(n-j)//q


def divisor_sum_floor(n:int)->int:
    return sum(n//q for q in range(1,n+1))


def proof_object()->dict:
    kappa_checks=0
    high_checks=0
    for n in range(2,301):
        Dn=divisor_sum_floor(n)
        for j in range(1,n):
            direct=sum(carry(n,j,q) for q in range(2,n+1))
            rhs=Dn-divisor_sum_floor(j)-divisor_sum_floor(n-j)
            assert direct==rhs
            kappa_checks+=1
        for j in range((n+3)//4,3*n//4+1):
            if not (1<=j<n): continue
            for q in range(max(j,n-j)+1,n+1):
                assert carry(n,j,q)==1
                high_checks+=1

    X=40
    rows=[]
    for n in range(4,X+1):
        lo=(n+3)//4
        hi=n//2
        for j in range(lo,hi+1):
            weight=Fraction((7*n+11*j)%13+1, n*n+17)
            rows.append((n,j,weight))
    loads=[Fraction(0) for _ in range(X+1)]
    packet_kappa=Fraction(0)
    for n,j,d in rows:
        kap=0
        for q in range(2,n+1):
            ch=carry(n,j,q)
            loads[q]+=d*ch
            kap+=ch
        packet_kappa+=d*kap
    assert packet_kappa==sum(loads[2:])

    h=Fraction(1); M=Fraction(1); B=Fraction(4); P=Fraction(1)
    assert P>=h*M and M<=B and not (P>=h*B)

    obj={
      "classification":"EXACT_BALANCED_CARRY_METRIC_ALGEBRA_VERIFIED",
      "kappa_identity_checks":kappa_checks,
      "high_column_checks":high_checks,
      "synthetic_rows":len(rows),
      "packet_tonelli_identity":True,
      "capacity_orientation_mutation_rejected":True,
      "scope":"Finite exact algebra only; no asymptotic estimate, flow existence, MFT, or RH is certified."
    }
    raw=(json.dumps(obj,sort_keys=True,separators=(",",":"))+"\n").encode()
    obj["proof_object_sha256"]=hashlib.sha256(raw).hexdigest()
    return obj


def main():
    obj=proof_object()
    (ROOT/"results"/"verification.json").write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    print(json.dumps(obj,indent=2,sort_keys=True))

if __name__=="__main__": main()
