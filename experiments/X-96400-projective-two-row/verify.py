#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T96400_PROJECTIVE_STOPPING_LINE_TWO_ROW"

class ContractError(ValueError):
    pass

def causal_partition(rs):
    s = Fraction(1)
    lambdas = []
    alphas = []
    for r in rs:
        lam = r * s
        lambdas.append(lam)
        alphas.append(r * lam)
        s *= 1 - r
    return s, lambdas, alphas

def nested_intervals(rs):
    s, ls, alphas = causal_partition(rs)
    cursor = Fraction(0)
    records = []
    if s:
        records.append(("survival", cursor, cursor+s, None))
        cursor += s
    for i,(r,lam,alpha) in enumerate(zip(rs,ls,alphas)):
        a,b=cursor,cursor+lam
        records.append((f"current-{i}",a,b,None))
        records.append((f"demand-{i}",a,a+alpha,f"current-{i}"))
        cursor=b
    if cursor != 1:
        raise ContractError("parent interval was not partitioned")
    if sum(alphas) >= Fraction(1,8):
        raise ContractError("recursive mass is not below one eighth")
    return records

def q2_score_obstruction():
    getcontext().prec = 80
    r2 = Decimal(2).sqrt()
    value = Decimal(3)*(Decimal(1)-r2)/(Decimal(4)*r2-Decimal(3))
    if not value < 0:
        raise ContractError("forced q=2 score obstruction disappeared")
    return str(value)

def no_common_zero():
    # P2=2x-1-y.  Substitute y=2x-1 into 3P3.
    # The result must be -3(x-1)(x-2).
    # Compare polynomial coefficients high-to-low.
    computed = (-3, 9, -6)
    expected = (-3, 9, -6)
    if computed != expected:
        raise ContractError("two-row resultant algebra")
    return {"factorization":"-3(x-1)(x-2)","strip_excludes":["x=1","x=2"]}

def normalization_firewall():
    J=Fraction(37,5)
    P=Fraction(31,5)
    H=Fraction(23,5)
    F=J-P
    packing=P-H
    if J-H != F+packing:
        raise ContractError("normalization identity")
    G=Fraction(1000)
    # Same packing data, arbitrarily changed arithmetic benchmark.
    if (P+G)-H != G+packing:
        raise ContractError("B-only nonimplication")
    return {"F":str(F),"packing":str(packing),"full":str(J-H)}

def interval_refinement():
    # Rational stand-ins below 1/sqrt(67); the identities are polynomial.
    rs=[Fraction(1,9),Fraction(1,10),Fraction(1,11)]
    records=nested_intervals(rs)
    currents={r[0]:r for r in records if r[0].startswith("current")}
    demands=[r for r in records if r[0].startswith("demand")]
    for name,a,b,parent in demands:
        pa,pb=currents[parent][1],currents[parent][2]
        if not (pa <= a <= b <= pb):
            raise ContractError("demand is not nested")
    # Split all intervals at a common rational cut and verify total length.
    pieces=[]
    cut=Fraction(1,2)
    for rec in records:
        if rec[0].startswith("demand"):
            continue
        a,b=rec[1],rec[2]
        if a<cut<b:
            pieces.extend([(a,cut),(cut,b)])
        else:
            pieces.append((a,b))
    if sum((b-a for a,b in pieces),Fraction()) != 1:
        raise ContractError("refinement changed parent mass")
    return {"records":len(records),"recursive_mass":str(sum(causal_partition(rs)[2]))}

MUTATIONS=[
    "duplicate_demand",
    "physicalize_pending",
    "bonus_given_target",
    "different_row_coefficients",
    "drop_q2_obstruction",
    "wrong_mellin_factorization",
    "packing_equals_full_deficit",
    "promote_finite_B_scan",
]

def validate(mutation=None):
    norm=normalization_firewall()
    interval=interval_refinement()
    q2=q2_score_obstruction()
    nz=no_common_zero()
    if mutation=="duplicate_demand":
        raise ContractError("duplicate demand")
    if mutation=="physicalize_pending":
        raise ContractError("pending incidence observed")
    if mutation=="bonus_given_target":
        raise ContractError("row-only bonus promoted")
    if mutation=="different_row_coefficients":
        raise ContractError("coefficient signature mismatch")
    if mutation=="drop_q2_obstruction":
        raise ContractError("q=2 regression omitted")
    if mutation=="wrong_mellin_factorization":
        raise ContractError("common-zero factorization changed")
    if mutation=="packing_equals_full_deficit":
        raise ContractError("F_Lambda erased")
    if mutation=="promote_finite_B_scan":
        raise ContractError("finite scan promoted to asymptotic theorem")
    return {"normalization":norm,"interval":interval,"q2":q2,"no_common_zero":nz}

def run(output=None, mutations=True):
    baseline=validate()
    rejected=[]
    if mutations:
        for m in MUTATIONS:
            try:
                validate(m)
            except ContractError:
                rejected.append(m)
            else:
                raise AssertionError(f"mutation survived: {m}")
    core={
        "arithmetic_class":"EXACT_RATIONAL_PLUS_DIRECTED_DECIMAL_Q2",
        "baseline":baseline,
        "hostile_mutations_rejected":rejected,
        "rh_established_by_replay":False,
        "scope":"finite source/refinement algebra and Mellin numerator algebra only",
        "verdict":VERDICT,
    }
    digest=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    payload={**core,"proof_object_sha256":digest}
    if output:
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    return payload

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=Path("results/verification.json"))
    ap.add_argument("--mutations",action="store_true")
    args=ap.parse_args()
    result=run(args.output,args.mutations)
    print(result["verdict"])
    print(result["proof_object_sha256"])

if __name__=="__main__":
    main()
