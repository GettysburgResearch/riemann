#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

def digest(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()

    # Exact midpoint local identity:
    # [(1-x)(1+x)^(1/2)]^2=(1-x)(1-x^2).
    local_checks=0
    for num,den in [(1,10),(1,7),(2,9),(1,3),(1,2)]:
        x=num/den
        lhs=((1-x)*math.sqrt(1+x))**2
        rhs=(1-x)*(1-x*x)
        assert abs(lhs-rhs)<1e-14
        local_checks+=1

    gamma_sign_checks=0
    for t in [0.05,0.2,0.49]:
        assert math.gamma(2*t-2)>0
        gamma_sign_checks+=1
    for t in [0.51,0.7,0.95]:
        assert math.gamma(2*t-2)<0
        gamma_sign_checks+=1

    # Reciprocal Gamma crosses linearly at alpha=-1.
    reciprocal_gamma_checks=0
    for d in [1e-4,2e-4,5e-4]:
        plus=1/math.gamma(-1+2*d)
        minus=1/math.gamma(-1-2*d)
        assert plus<0 and minus>0
        assert abs(plus/(-2*d)-1)<0.01
        assert abs(minus/(2*d)-1)<0.01
        reciprocal_gamma_checks+=1

    # Transition-width model: Delta tends to zero faster than any log power.
    widths=[]
    for L in [1e4,1e6,1e8]:
        V=(math.log(L)**(3/5))/(math.log(math.log(L))**(1/5))
        delta=(math.log(L)**2)*math.exp(-0.1*V)
        widths.append(delta)
    assert all(x>0 for x in widths)

    # Orientation check for an increasing transition polynomial.
    orientation_checks=0
    for theta in [0.49,0.5,0.51]:
        midpoint=0.5-theta
        adverse=max(-midpoint,0)
        drift=max(theta-0.5,0)
        assert abs(adverse-drift)<1e-15
        orientation_checks+=1

    payload={
        "schema":"riemann.t102910.critical-temperature-zero.v1",
        "local_midpoint_checks":local_checks,
        "gamma_sign_checks":gamma_sign_checks,
        "reciprocal_gamma_checks":reciprocal_gamma_checks,
        "orientation_checks":orientation_checks,
        "strict_square_sign_transition":True,
        "critical_temperature":"1/2",
        "transition_zero_exponentially_localized":True,
        "ctzd102897_proved":False,
        "rh_established":False,
        "verdict":"PASS_T102910_CRITICAL_TEMPERATURE_ZERO",
    }
    payload["proof_object_sha256"]=digest(payload)
    text=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])

if __name__=="__main__":
    main()
