#!/usr/bin/env python3
from __future__ import annotations
import json, math, hashlib
from fractions import Fraction

VERDICT="PASS_T99710_ADAPTIVE_POISSON_OWNER_GAP"
OPEN=["APOC99710","RH"]

def critical_local_coeffs(depth: int) -> list[int]:
    # At 67^u=2, c_u(67^e m)/J_u(m).
    out=[]
    for e in range(depth+1):
        if e==0: out.append(1)
        elif e==1: out.append(0)
        else: out.append(2**(e-2))
    return out

def verify() -> dict:
    checks={}

    # e=2 owner weights.  Write S=sum_(p|m) log p and L=log 67:
    # (4L+2L)/(3(2L+S)) + S/(2L+S) = 1.
    for L,S in [(1,0),(1,3),(7,11),(67,101)]:
        lhs=Fraction(6*L,3*(2*L+S))+Fraction(S,2*L+S)
        assert lhs==1
    checks["duplicated_67_owner_weights_sum_one"]=True

    # The two exceptional duplicated-67 edges dominate the universal gap.
    for tau in [0.01,0.1,0.5,1.0]:
        universal=2*(1-2**(-tau))
        assert 10-6*67**(-tau) >= universal
        assert 10+6*67**(-2*tau) >= universal
        assert universal >= tau - 1e-14
    checks["cauchy_poisson_gap"]=True

    coeffs=critical_local_coeffs(8)
    assert coeffs==[1,0,1,2,4,8,16,32,64]
    checks["critical_continuous_order_coefficients"]=coeffs

    ustar=math.log(2)/math.log(67)
    assert 0 < ustar < 1
    assert 67**(ustar-1e-6)-2 < 0
    assert 67**(ustar+1e-6)-2 > 0
    checks["continuous_order_threshold"]=ustar

    vals=[]
    for logx in [100.0,1000.0,10000.0,1_000_000.0]:
        tau=1/math.log(logx)
        gap=2*(1-2**(-tau))
        assert gap >= tau - 1e-14
        vals.append({"log_x":logx,"tau":tau,
                     "power_exponent":tau,"gap":gap})
    assert vals[-1]["power_exponent"] < vals[0]["power_exponent"]
    checks["adaptive_strip_samples"]=vals

    checks["real_order_positive_pole_s"]=ustar+0.5
    checks["real_order_landau_pole_removed"]=False
    checks["apoc99710_proved"]=False
    checks["rh_established"]=False

    payload={"verdict":VERDICT,"checks":checks,"open":OPEN}
    proof=hashlib.sha256(
        json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    ).hexdigest()
    payload["proof_object_sha256"]=proof
    return payload

if __name__=="__main__":
    p=verify()
    print(VERDICT)
    print(p["proof_object_sha256"])
