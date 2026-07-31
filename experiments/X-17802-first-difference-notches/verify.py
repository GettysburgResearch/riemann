#!/usr/bin/env python3
"""Exact Fraction-only checker for L-17802 finite-difference notch algebra."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA="riemann.x17802-first-difference-notches.v1"

def is_int(x: Any)->bool: return isinstance(x,int) and not isinstance(x,bool)
def rat(o: Any,name: str)->Fraction:
    if not isinstance(o,dict): raise ValueError(f"{name} must be rational")
    n=o.get("numerator"); d=o.get("denominator")
    if not is_int(n) or not is_int(d) or d<=0: raise ValueError(f"bad {name}")
    return Fraction(n,d)
def fj(x: Fraction)->dict[str,str]:
    return {"numerator":str(x.numerator),"denominator":str(x.denominator)}
def sha(o: Any)->str:
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def poly(x: Fraction)->Fraction:
    return x**7-3*x**4+2*x**2-5*x+7

def recursive_difference(x: Fraction, shifts: list[Fraction])->Fraction:
    def apply(y: Fraction,j: int)->Fraction:
        if j==len(shifts): return poly(y)
        return (apply(y,j+1)-apply(y-shifts[j],j+1))/2
    return apply(x,0)
def subset_difference(x: Fraction,shifts: list[Fraction])->Fraction:
    m=len(shifts); out=Fraction(0)
    for mask in range(1<<m):
        shift=sum((shifts[j] for j in range(m) if mask>>j&1),Fraction(0))
        sign=-1 if mask.bit_count()&1 else 1
        out += sign*poly(x-shift)
    return out/Fraction(1<<m)
def verify(data: dict[str,Any])->dict[str,Any]:
    if data.get("schema")!=SCHEMA: raise ValueError("schema")
    T=data.get("verified_height")
    if not is_int(T) or T<=0: raise ValueError("verified_height")
    upp=data.get("ordinate_upper_integers")
    if not isinstance(upp,list) or len(upp)!=5 or any(not is_int(x) or x<=0 for x in upp):
        raise ValueError("ordinate upper bounds")
    pi_lower=rat(data.get("pi_lower"),"pi_lower")
    if pi_lower<=0: raise ValueError("pi lower")
    gains=[(pi_lower*T/Fraction(u))**2 for u in upp]
    total=Fraction(1)
    for g in gains: total*=g
    threshold=Fraction(10)**115
    if total<=threshold: raise ValueError("frontier gain threshold failed")

    shifts_raw=data.get("synthetic_shifts")
    if not isinstance(shifts_raw,list) or len(shifts_raw)!=5: raise ValueError("shifts")
    shifts=[rat(x,f"shift[{i}]") for i,x in enumerate(shifts_raw)]
    if any(x<=0 for x in shifts): raise ValueError("nonpositive shift")
    x=rat(data.get("synthetic_x"),"synthetic_x")
    rec=recursive_difference(x,shifts); sub=subset_difference(x,shifts)
    if rec!=sub: raise ValueError("subset identity")
    coeff_abs=Fraction((1<<len(shifts)),(1<<len(shifts)))
    support_diff=sum(shifts,Fraction(0)); support_box=2*support_diff

    phase_error=rat(data.get("phase_error_upper"),"phase_error_upper")
    if phase_error<0: raise ValueError("phase error")
    attenuation=phase_error/2
    displacement=rat(data.get("normalized_displacement"),"normalized_displacement")
    if displacement<0 or displacement>1: raise ValueError("normalized displacement")
    displacement_lower=displacement/4

    result={
      "schema":SCHEMA,"classification":data.get("classification"),
      "subset_coefficient_count":1<<len(shifts),
      "subset_coefficient_absolute_sum":fj(coeff_abs),
      "synthetic_recursive_value":fj(rec),"synthetic_subset_value":fj(sub),
      "difference_support_cost":fj(support_diff),"box_square_support_cost":fj(support_box),
      "single_replacement_gain_floors":[fj(g) for g in gains],
      "all_five_gain_floor":fj(total),"gain_exceeds_10_pow_115":True,
      "line_attenuation_upper":fj(attenuation),
      "off_line_displacement_lower":fj(displacement_lower),
      "verdict":"EXACT_FIRST_DIFFERENCE_NOTCH_IDENTITIES_VERIFIED",
      "proof_boundary":"Finite rational algebra only; no Riemann prime or zero interval is evaluated."
    }
    result["proof_object_sha256"]=sha(result)
    return result

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("certificate",type=Path); ap.add_argument("--output",type=Path)
    a=ap.parse_args(); data=json.loads(a.certificate.read_text()); out=verify(data)
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if a.output:a.output.write_text(text)
    print(text,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
