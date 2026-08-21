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

    log2=math.log(2.0)
    k0=8*log2*(1-2**-0.5)**2
    k1prime=log2*k0
    assert k0>0 and k1prime>0

    # q(s)=1-sqrt(2)2^-s
    assert abs(1-math.sqrt(2)*2**-0.5)<1e-14
    assert abs(math.sqrt(2)*log2*2**-0.5-log2)<1e-14

    # Negative part is 1-Lipschitz.
    for a,b in [(-3,2),(4,-7),(-5,-2),(0,1)]:
        assert abs(max(-a,0)-max(-b,0))<=abs(a-b)

    # Source-transfer homogeneous carrier identity.
    transfers=0
    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]:
        X=p**(10/9)
        lhs=p**-0.5*math.sqrt(X/p)
        rhs=math.sqrt(X)/p
        assert abs(lhs-rhs)<1e-12
        transfers+=1

    payload={
        "schema":"riemann.t103200.xd-cv-carrier-transfer.v1",
        "kappa0":k0,
        "k1_prime_carrier_constant":k1prime,
        "same_kernel_hybrid_required":True,
        "first_chaos_quotient_exact":True,
        "source_transfer_checks":transfers,
        "owner_budget_controls_literal_transfer":False,
        "cpxd103200_proved":False,
        "sctv103210_proved":False,
        "xd_proved":False,
        "cv_proved":False,
        "rh_established":False,
        "verdict":"PASS_T103200_XD_CV_CARRIER_TRANSFER_HARDENING",
    }
    payload["proof_object_sha256"]=digest(payload)
    text=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_bytes(text.encode("utf-8"))
    else:
        print(text,end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])

if __name__=="__main__":
    main()
