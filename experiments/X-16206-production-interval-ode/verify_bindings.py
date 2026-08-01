#!/usr/bin/env python3
"""Verify source, producer, primitive, and wrapper digest bindings for X-16206."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any


def canonical(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()

def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def sha_obj(obj: Any, drop: str | None = None) -> str:
    value = dict(obj)
    if drop is not None:
        value.pop(drop, None)
    return hashlib.sha256(canonical(value)).hexdigest()

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--producer',type=Path,required=True)
    ap.add_argument('--primitive',type=Path,required=True)
    ap.add_argument('--wrapper',type=Path,required=True)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    p=json.loads(a.primitive.read_text()); w=json.loads(a.wrapper.read_text())
    checks={
      'producer_file': sha_file(a.producer)==p['producer_sha256']==w['radial_replay']['producer_sha256'],
      'source_object': sha_obj(p['source'])==p['source_sha256']==w['production_bindings']['source_sha256'],
      'primitive_object': sha_obj(p,'primitive_sha256')==p['primitive_sha256']==w['radial_replay']['primitive_sha256']==w['production_bindings']['actual_primitive_object_sha256'],
      'primitive_file': sha_file(a.primitive)==w['production_bindings']['actual_primitive_file_sha256'],
      'classification': p['classification']=='DIRECTED_INTERVAL_ODE' and w['radial_replay']['classification']=='DIRECTED_INTERVAL_ODE',
    }
    result={'schema':'riemann.x16206-binding-verification.v1','checks':checks,'accepted':all(checks.values())}
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.output: a.output.write_text(text)
    else: print(text,end='')
    return 0 if result['accepted'] else 2
if __name__=='__main__': raise SystemExit(main())
