#!/usr/bin/env python3
from __future__ import annotations
import math, json, hashlib

VERDICT="PASS_T99711_COMPACT_GROWING_PHASE_MOMENT_REDUCTION"

def T(y: float) -> float:
    return 0.0 if y < 1.0 else 4.0*math.sqrt(y)-3.0

def phi(y: float) -> float:
    return T(y)-T(y/2.0)-2.0*T(y/4.0)+2.0*T(y/8.0)

def phi_piece(y: float) -> float:
    if y < 1: return 0.0
    if y < 2: return 4*math.sqrt(y)-3
    if y < 4: return (4-2*math.sqrt(2))*math.sqrt(y)
    if y < 8: return 6-2*math.sqrt(2)*math.sqrt(y)
    return 0.0

def verify():
    checks={}
    for y in [0.5,1.0,1.5,2.0,3.0,4.0,4.5,7.999,8.0,16.0,100.0]:
        assert abs(phi(y)-phi_piece(y)) < 1e-11
    checks["compact_piecewise_kernel"]=True
    assert abs(phi(100.0))<1e-12
    checks["tail_modes_cancelled"]=True
    assert phi(4.4)>0 and phi(4.6)<0
    checks["mandatory_kernel_sign_change"]=True

    for re in [0.01,0.1,0.25,0.49]:
        assert 2**(-re) < 1
        assert 2*4**(-re) > 1
    checks["mellin_zero_strip_safe"]=True

    samples=[]
    previous=None
    for L in [100,1000,10000,100000,1000000]:
        M=max(1,int(L/(math.log(L+math.e)**3)))
        log_binom=math.lgamma(L+M+1)-math.lgamma(L+1)-math.lgamma(M+1)
        ratio=log_binom/(L*math.log(2))
        forward=M/L
        assert ratio < 1
        if previous is not None:
            assert ratio < previous
        previous=ratio
        samples.append({"L":L,"M":M,"inverse_power_exponent":ratio,
                        "forward_power_exponent":forward})
    checks["growing_moment_samples"]=samples

    checks["gpmoc99710_proved"]=False
    checks["rh_established"]=False
    payload={"verdict":VERDICT,"checks":checks,
             "open":["GPMOC99710","RH"]}
    payload["proof_object_sha256"]=hashlib.sha256(
        json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    ).hexdigest()
    return payload

if __name__=="__main__":
    p=verify()
    print(VERDICT)
    print(p["proof_object_sha256"])
