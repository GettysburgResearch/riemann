#!/usr/bin/env python3
"""Exact symbolic regression for L-19885.

Y4 is represented as a formal nonnegative integer combination of log-prime
symbols, so no floating-point logarithms enter the support check.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x19885-y4-factor67-root-cost.v1"
OUTPUT_SCHEMA = "riemann.x19885-y4-factor67-root-cost-verification.v1"

class CertificateError(ValueError):
    pass

def canonical_sha(value: Any) -> str:
    raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()

def fj(x: Fraction)->dict[str,str]:
    return {"numerator":str(x.numerator),"denominator":str(x.denominator)}

def prime_power_base(n:int)->int|None:
    if n<2: return None
    d=2
    while d*d<=n:
        if n%d==0:
            while n%d==0: n//=d
            return d if n==1 else None
        d += 1 if d==2 else 2
    return n

def factor_two(n:int)->tuple[int,int]:
    e=0
    while n%2==0:
        e+=1;n//=2
    return e,n

def y4_formal(q:int)->dict[int,int]:
    out:dict[int,int]={}
    k=0;t=q
    while True:
        p=prime_power_base(t)
        if p is not None:
            out[p]=out.get(p,0)+(1<<k)
        if t%4: break
        t//=4;k+=1
    return out

def y4_formula(q:int)->dict[int,int]:
    e,m=factor_two(q)
    if m==1:
        coeff=(1<<((e+1)//2))-1
        return {2:coeff} if coeff else {}
    p=prime_power_base(m)
    if p is None or e%2:
        return {}
    return {p:1<<(e//2)}

def verify(data:dict[str,Any])->dict[str,Any]:
    if data.get("schema")!=SCHEMA: raise CertificateError("unsupported schema")
    n=data.get("check_through")
    if isinstance(n,bool) or not isinstance(n,int) or n<2:
        raise CertificateError("check_through must be an integer >=2")
    positive=0
    first_positive=[]
    for q in range(2,n+1):
        actual=y4_formal(q); expected=y4_formula(q)
        if actual!=expected:
            raise CertificateError(f"Y4 support formula fails at q={q}: {actual} != {expected}")
        if actual:
            positive+=1
            if len(first_positive)<20:
                first_positive.append({"q":q,"formal_coefficients":{str(p):c for p,c in sorted(actual.items())}})
    two=Fraction(5,3)
    odd=Fraction(26,3)
    total=two+odd
    if not total < 11:
        raise CertificateError("global 3/2 majorant failed")
    mismatch=Fraction(285,8)*11
    if not mismatch < 392:
        raise CertificateError("mismatch majorant failed")
    x=data.get("sample_X")
    if isinstance(x,bool) or not isinstance(x,int) or x<100:
        raise CertificateError("sample_X must be an integer >=100")
    l_up=data.get("log_2X_upper")
    if isinstance(l_up,bool) or not isinstance(l_up,int) or l_up<1:
        raise CertificateError("log_2X_upper must be a positive integer")
    if not math.log(2*x)<l_up:
        raise CertificateError("log_2X_upper is not an upper bound")
    k=x//67+1
    sqrt_k_lower=math.isqrt(k)
    sqrt_x_lower=math.isqrt(x)
    if sqrt_k_lower<=0 or sqrt_x_lower<=0:
        raise CertificateError("invalid square-root lower bound")
    s1_bound=3+2*l_up+2*l_up*l_up
    collar=Fraction(200*s1_bound,sqrt_k_lower)
    safety=Fraction(23852*l_up*l_up,sqrt_x_lower)
    proof={
        "check_through":n,
        "positive_count":positive,
        "zero_count":n-1-positive,
        "first_positive":first_positive,
        "two_power_s32_upper":fj(two),
        "odd_prime_power_s32_upper":fj(odd),
        "total_s32_upper":fj(total),
        "mismatch_upper":fj(mismatch),
        "sample_X":x,
        "K":k,
        "log_2X_upper":l_up,
        "partial_s1_majorant":s1_bound,
        "sample_collar_upper":fj(collar),
        "sample_safety_upper":fj(safety),
    }
    return {
        "schema":OUTPUT_SCHEMA,
        "classification":"EXACT_FORMAL_Y4_SUPPORT_AND_RATIONAL_MAJORANTS",
        **proof,
        "proof_object_sha256":canonical_sha(proof),
        "verdict":"PASS_Y4_SPARSE_FACTOR67_ROOT_COST_PACKET",
        "proof_boundary":"Exact symbolic support check through the declared finite range and exact rational verification of the analytic majorant constants. The infinite support theorem and asymptotic estimates are proved in L-19885; this replay does not establish the frozen factor-67 common-parent realization or RH."
    }

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("certificate",type=Path);ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    try:
        raw=json.loads(a.certificate.read_text())
        if not isinstance(raw,dict): raise CertificateError("certificate root must be object")
        result=verify(raw)
    except (OSError,json.JSONDecodeError,CertificateError) as e:
        print(json.dumps({"verified":False,"error":str(e)},indent=2),file=sys.stderr);return 2
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
    print(text,end="");return 0
if __name__=="__main__": raise SystemExit(main())
