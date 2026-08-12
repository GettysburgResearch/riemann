#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

DEN=10**80

def sqrt_bounds(n:int):
    m=isqrt(n*DEN*DEN)
    return Fraction(m,DEN),Fraction(m+1,DEN)

def main():
    rt2_lo,rt2_hi=sqrt_bounds(2)
    rt55_lo,rt55_hi=sqrt_bounds(55)
    assert rt2_hi < Fraction(17,12)
    assert rt55_hi < Fraction(15,2)

    W=10000
    omission_lower=Fraction(W)* (2-rt2_hi)-800
    full_overfill_upper=512*rt55_hi+204
    assert omission_lower > 5033
    assert full_overfill_upper < 4044
    assert omission_lower > full_overfill_upper
    assert 512*rt2_hi < 800

    # Direct finite checks of the three terminal derivative brackets.
    b1=2-rt2_hi
    b2=4-rt55_hi*0  # placeholder removed below; use exact interval arithmetic explicitly
    # J=2: 4-sqrt(3)(1+1/sqrt(2)) > 2-sqrt(2).
    rt3_lo,rt3_hi=sqrt_bounds(3)
    invrt2_hi=1/rt2_lo
    j2_lower=4-rt3_hi*(1+invrt2_hi)
    # J=3: 6-2(1+1/sqrt(2)+1/sqrt(3)) > 2-sqrt(2).
    invrt3_hi=1/rt3_lo
    j3_lower=6-2*(1+invrt2_hi+invrt3_hi)
    assert j2_lower > b1
    assert j3_lower > b1

    out={
      "classification":"PASS_FIXED_TOP_TERMINAL_OMISSION",
      "W":W,
      "two_minus_sqrt2_lower":float(2-rt2_hi),
      "omission_coefficient_lower":float(omission_lower),
      "full_overfill_coefficient_upper":float(full_overfill_upper),
      "terminal_margin_lower":float(omission_lower-full_overfill_upper),
      "J2_derivative_bracket_lower":float(j2_lower),
      "J3_derivative_bracket_lower":float(j3_lower),
      "scope":"Exact Fraction arithmetic and directed rational square-root enclosures. Analytic response and collar identities are proved in L-91115."
    }
    path=Path(__file__).resolve().parent/"results"/"verification.json"
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["classification"])

if __name__=="__main__":
    main()
