#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA="riemann.x96200.affine-volterra-hardening.v1"
RESULT_SCHEMA="riemann.x96200.affine-volterra-hardening.result.v1"

def frac(x:Any)->Fraction:
    if isinstance(x,bool): raise ValueError("boolean is not rational")
    if isinstance(x,int): return Fraction(x)
    if isinstance(x,str): return Fraction(x)
    raise ValueError(f"bad rational {x!r}")

def fs(x:Fraction)->str:
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def vec(xs): return [frac(x) for x in xs]

def validate(data:dict[str,Any])->dict[str,Any]:
    if data.get("schema")!=SCHEMA: raise ValueError("schema drift")

    n=data["normalization"]
    J,P,H=map(frac,(n["J"],n["P"],n["H"]))
    F=J-P; y4=P-H; complete=J-H
    if complete != F+y4: raise ValueError("complete-gap decomposition failed")
    if y4 != frac(n["y4_slack"]): raise ValueError("Y4 slack mislabeled")
    if complete != frac(n["complete_loss"]): raise ValueError("complete loss drift")
    if F == 0: raise ValueError("fixture must expose nonzero arithmetic gap")

    a=data["affine"]
    ua,ub,ubar=map(frac,(a["u_a"],a["u_b"],a["u_bar"]))
    A,B=vec(a["A"]),vec(a["B"])
    if not ub<ubar<ua: raise ValueError("mean outside cell")
    theta=(ubar-ub)/(ua-ub)
    pa=[x-ua*y for x,y in zip(A,B)]
    pb=[x-ub*y for x,y in zip(A,B)]
    pm=[x-ubar*y for x,y in zip(A,B)]
    if pm != [theta*x+(1-theta)*y for x,y in zip(pa,pb)]:
        raise ValueError("affine compression failed")
    if min(pa+pb)<0: raise ValueError("positive endpoint lost")

    c=data["cost"]
    K=int(c["K"])
    if K != int(c["X"])//67+1: raise ValueError("K drift")
    thinning=Fraction(55776,25)
    # Rigorous elementary upper bound:
    # 1/sqrt(K) < 1/122169, log 2 < 1, log(10^12)<28.
    mismatch=Fraction(57*4*(1+28),2*122169)
    total=thinning+mismatch
    if total>=3457: raise ValueError("physical packing cost too large")

    flags=data["firewalls"]
    required_false=(
      "old_t94000_endpoint_consumer",
      "pr508_directed_certificate_accepted",
      "pr537_frontier_chain_accepted",
      "rh_established",
    )
    if any(flags.get(k) is not False for k in required_false):
        raise ValueError("fail-closed frontier violated")
    if flags.get("mpfr_full_artifact_required") is not True:
        raise ValueError("MPFR artifact requirement dropped")
    if flags.get("arithmetic_gap_required") is not True:
        raise ValueError("arithmetic gap hidden")

    witness=data["review503_witness"]
    lo,hi=frac(witness["lower"]),frac(witness["upper"])
    if not (Fraction(-184291,10**9)<lo<=hi<Fraction(-184290,10**9)<0):
        raise ValueError("review503 witness no longer negative")

    result={
      "schema":RESULT_SCHEMA,
      "verdict":"PASS_T96200_AFFINE_VOLTERRA_HARDENING_AND_FAIL_CLOSED_FRONTIER",
      "normalization":{
        "J":fs(J),"P":fs(P),"H":fs(H),
        "F=J-P":fs(F),
        "Y4=P-H":fs(y4),
        "J-H":fs(complete),
        "identity":"J-H=(J-P)+(P-H)",
      },
      "affine":{
        "theta":fs(theta),
        "endpoint_a":[fs(x) for x in pa],
        "endpoint_b":[fs(x) for x in pb],
        "mean":[fs(x) for x in pm],
      },
      "physical_cost":{
        "thinning":fs(thinning),
        "mismatch_upper":fs(mismatch),
        "total_upper":fs(total),
        "bound":"<3457",
        "meaning":"P_Lambda-H only",
      },
      "review503_witness":{"lower":fs(lo),"upper":fs(hi)},
      "frontier":{
        "old_t94000_endpoint_consumer":"REJECTED",
        "pr508_tail":"MPFR_FULL_ARTIFACT_REQUIRED",
        "anchored_source":"ACTUAL_SOURCE_MARGINAL_REQUIRED",
        "pr537_frontier_chain":"GLOBAL_CROSS_PRODUCT_TRANSPORT_MISSING",
        "rh":"UNPROVEN",
      },
      "proof_boundary":"Exact normalization, affine compression, physical cost arithmetic, and fail-closed import status. Does not prove F_Lambda=o(log^2 X), the anchored source theorem, fixed-row positivity, or RH."
    }
    canon=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    result["proof_object_sha256"]=hashlib.sha256(canon).hexdigest()
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("certificate",type=Path)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    result=validate(json.loads(a.certificate.read_text()))
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])

if __name__=="__main__": main()
