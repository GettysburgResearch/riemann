#!/usr/bin/env python3
"""Exact consumer for the X-17804 directed prime interval ladder."""
from __future__ import annotations
import argparse, hashlib, json
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA="riemann.x17804-local-cell-mpfr-summary.v1"

def dec(x: Any, name: str) -> Fraction:
    if not isinstance(x,str): raise ValueError(f"{name} must be a decimal string")
    return Fraction(Decimal(x))

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def canonical_sha(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def verify(data: dict[str,Any], source: Path | None=None) -> dict[str,Any]:
    if data.get("schema")!=SCHEMA: raise ValueError("schema")
    if data.get("classification")!="DIRECTED_MPFR_PRIME_INTERVAL": raise ValueError("classification")
    if data.get("J")!=12 or data.get("base_rational_knots")!=800 or data.get("prime_power_terms")!=103384:
        raise ValueError("structural constants")
    t=data.get("translation")
    if t!={"numerator":"17730793345827","denominator":str(2**40)}: raise ValueError("translation")
    rows=data.get("precision_ladder")
    if not isinstance(rows,list) or [r.get("precision_bits") for r in rows] != [256,320,384,448]:
        raise ValueError("precision ladder")
    normalized=[]; previous=None
    for i,row in enumerate(rows):
        if row.get("segments")!=800 or row.get("prime_power_terms")!=103384 or row.get("ambiguous_knots")!=0:
            raise ValueError(f"row {i} structure")
        lo=dec(row.get("lower"),f"row[{i}].lower"); hi=dec(row.get("upper"),f"row[{i}].upper")
        if lo>hi: raise ValueError("reversed interval")
        if previous is not None and not (previous[0] <= lo <= hi <= previous[1]):
            raise ValueError("precision intervals are not nested")
        previous=(lo,hi); normalized.append((row["precision_bits"],lo,hi))
    mid=dec(data.get("independent_moment_sweep_midpoint"),"moment midpoint")
    lo,hi=previous
    if not lo <= mid <= hi: raise ValueError("independent moment midpoint outside directed interval")
    if hi-lo >= Fraction(1,10**110): raise ValueError("finest interval too wide")
    if source is not None:
        if sha(source)!=data.get("source_sha256"): raise ValueError("source hash mismatch")
    proof={
      "schema":"riemann.x17804-local-cell-mpfr-verification.v1",
      "verdict":"DIRECTED_COMPLETE_PRIME_CELL_CLOSED",
      "precision_bits":[p for p,_,_ in normalized],
      "segments":800,"prime_power_terms":103384,"ambiguous_knots":0,
      "finest_lower":{"numerator":str(lo.numerator),"denominator":str(lo.denominator)},
      "finest_upper":{"numerator":str(hi.numerator),"denominator":str(hi.denominator)},
      "finest_width":{"numerator":str((hi-lo).numerator),"denominator":str((hi-lo).denominator)},
      "moment_midpoint_inside":True,
      "scope":"Prime side only; no zero-phase or RH verdict is inferred."
    }
    proof["proof_object_sha256"]=canonical_sha(proof)
    return proof

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("summary",type=Path); ap.add_argument("--source",type=Path); ap.add_argument("--output",type=Path)
    a=ap.parse_args(); result=verify(json.loads(a.summary.read_text()),a.source)
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if a.output:a.output.write_text(text)
    print(text,end="");return 0
if __name__=="__main__":raise SystemExit(main())
