#!/usr/bin/env python3
"""Check precision nesting for X-5603 FLINT gap certificates."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

FIELDS = (
    "lower_zero_imaginary_ball",
    "upper_zero_imaginary_ball",
    "target_minus_lower",
    "upper_minus_target",
    "gap",
    "gap_in_local_mean_spacings",
)

def endpoint(raw):
    m=int(raw["mantissa"]); e=int(raw["exponent"])
    return Fraction(m*(1<<e),1) if e>=0 else Fraction(m,1<<(-e))

def interval(raw):
    return endpoint(raw["lower"]), endpoint(raw["upper"])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('low',type=Path); ap.add_argument('high',type=Path)
    args=ap.parse_args(); low=json.loads(args.low.read_text()); high=json.loads(args.high.read_text())
    for key in ("lower_zero_index","upper_zero_index"):
        if low[key] != high[key]: raise SystemExit(f"index mismatch {key}: {low[key]} != {high[key]}")
    for key in FIELDS:
        llo,lhi=interval(low[key]); hlo,hhi=interval(high[key])
        if hlo < llo or hhi > lhi: raise SystemExit(f"non-nested field {key}")
    print(json.dumps({"verified":True,"same_indices":True,"nested_fields":list(FIELDS)},indent=2))
if __name__=='__main__': main()
