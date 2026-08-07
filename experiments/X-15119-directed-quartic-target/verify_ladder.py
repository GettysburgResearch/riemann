#!/usr/bin/env python3
"""Fail-closed exact consumer for directed quartic target-preservation rows."""
from __future__ import annotations
import argparse, json, hashlib
from decimal import Decimal
from pathlib import Path
from typing import Any

SCHEMA = "riemann.quartic-target-ladder.v1"

def iv(x: Any) -> tuple[Decimal, Decimal]:
    if not isinstance(x, list) or len(x) != 2:
        raise ValueError("interval must be [lo,hi]")
    lo, hi = Decimal(str(x[0])), Decimal(str(x[1]))
    if not lo.is_finite() or not hi.is_finite() or lo > hi:
        raise ValueError("malformed interval")
    return lo, hi

def overlap(a: tuple[Decimal,Decimal], b: tuple[Decimal,Decimal]) -> bool:
    return max(a[0],b[0]) <= min(a[1],b[1])

def verify(data: dict[str,Any]) -> dict[str,Any]:
    if data.get("schema") != SCHEMA: raise ValueError("wrong schema")
    target = iv(data["tau4"])
    rows = data.get("rows")
    if not isinstance(rows, list): raise ValueError("rows must be a list")
    verdicts=[]
    for r in rows:
        for key in ("M","N","a4_linear","trA4","trK4","jet_body_norm","readout_tail_s4"):
            if key not in r: raise ValueError(f"missing row key {key}")
        vals={k:iv(r[k]) for k in ("a4_linear","trA4","trK4","jet_body_norm","readout_tail_s4")}
        if vals["jet_body_norm"][0] < 0 or vals["readout_tail_s4"][0] < 0:
            raise ValueError("norm interval has negative endpoint")
        if vals["jet_body_norm"][0] > 0:
            status="JET_BODY_PERSISTENCE_CERTIFIED"
        elif all(overlap(vals[k],target) for k in ("a4_linear","trA4","trK4")):
            status="QUARTIC_ROW_OVERLAPS_TARGET"
        elif any(not overlap(vals[k],target) for k in ("a4_linear","trA4","trK4")):
            status="QUARTIC_TARGET_CHANGE_CERTIFIED"
        else:
            status="UNRESOLVED_INTERVAL"
        verdicts.append({"M":r["M"],"N":r["N"],"status":status})
    status="QUARTIC_TARGET_ONLY" if not rows else "QUARTIC_ROWS_CHECKED"
    canonical=json.dumps(data,sort_keys=True,separators=(",",":")).encode()
    return {"status":status,"tau4":[str(target[0]),str(target[1])],
            "row_verdicts":verdicts,
            "certificate_sha256":hashlib.sha256(canonical).hexdigest(),
            "scope":"target and finite row consistency only; no asymptotic inference"}

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("certificate",type=Path); args=ap.parse_args()
    print(json.dumps(verify(json.loads(args.certificate.read_text())),indent=2,sort_keys=True))
if __name__=="__main__": main()
