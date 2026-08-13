#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]

def bounded_divisors(limit:int):
    out=[(1,1)]
    for p in PRIMES:
        out += [(d*p,-mu) for d,mu in list(out) if d*p<=limit]
    return sorted(out)

def certify():
    prefix=Fraction(0)
    maximum=None
    minimum=None
    divisors=bounded_divisors(82)
    for d,mu in divisors:
        prefix += Fraction(mu,d)
        if maximum is None or prefix>maximum[0]: maximum=(prefix,d)
        if minimum is None or prefix<minimum[0]: minimum=(prefix,d)

    assert maximum==(Fraction(1),1), maximum
    residual=Fraction(1,25)-Fraction(1,83)
    assert residual==Fraction(58,2075)>0

    return {
      "classification":"PASS_P79_CHILD_FIRST_MOMENT_UPPER",
      "bounded_divisors":len(divisors),
      "maximum_prefix":str(maximum[0]),
      "maximum_at":maximum[1],
      "minimum_prefix":str(minimum[0]),
      "minimum_at":minimum[1],
      "residual_score_target_coefficient":str(residual),
      "scope":(
        "Exact Fraction enumeration of every P79 prefix below 83. Together "
        "with the certified parent prefix A_P79(x)>1/25 for x>=83, it proves "
        "A_P79(py)-A_P79(y)/p>58/2075 for p>=83 and 1<=y<83."
      )
    }

def main():
    result=certify()
    out=Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(out)

if __name__=="__main__": main()
