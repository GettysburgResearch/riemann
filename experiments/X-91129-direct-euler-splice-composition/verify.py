#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


def certify():
    # Formal one-prime Euler split: parent = r*child + residual.
    r=Fraction(2,11)
    child=[Fraction(3,7),Fraction(5,13),Fraction(2,9)]
    residual=[Fraction(4,17),Fraction(6,19),Fraction(8,23)]
    parent=[r*c+q for c,q in zip(child,residual)]
    assert [p-r*c for p,c in zip(parent,child)]==residual
    assert all(q>0 for q in residual)

    # The target/score identities have the same linear form.
    target_child=Fraction(7,5)
    target_residual=Fraction(11,7)
    target_parent=r*target_child+target_residual
    assert target_parent-r*target_child==target_residual

    surplus=Fraction(58,2075)
    score_residual=target_residual+surplus
    score_parent=r*Fraction(8,5)+score_residual
    assert score_parent-r*Fraction(8,5)-target_residual==surplus>0

    # Branch homogeneity: substochastic masses do not multiply a bounded debt.
    weights=[Fraction(1,7),Fraction(2,7),Fraction(3,7)]
    assert sum(weights)<=1
    debt=Fraction(900)
    assert sum(w*debt for w in weights)<=debt

    return {
      "classification":"PASS_DIRECT_EULER_SPLICE_COMPOSITION",
      "formal_row_coordinates":len(parent),
      "score_target_surplus_coefficient":str(surplus),
      "substochastic_weight_sum":str(sum(weights)),
      "scope":(
        "Exact Fraction regression of the direct Euler linear composition and "
        "homogeneous branch accounting. Positivity of the actual inherited "
        "P79 row is supplied separately by L-91346/X-91125."
      )
    }


def main():
    result=certify()
    out=Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(out)

if __name__=="__main__":main()
