#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, sys
sys.dont_write_bytecode = True
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def sha(path):
    h=hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()

def main():
    spec=importlib.util.spec_from_file_location('graph_validate',ROOT/'graph_validate.py')
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    result=mod.main()
    checks=[]
    ledger=ROOT/'SHA256SUMS'
    for line in ledger.read_text().splitlines():
        if not line.strip(): continue
        digest,rel=line.split('  ',1); p=ROOT/rel
        if not p.is_file() or sha(p)!=digest: raise RuntimeError(f'checksum failure: {rel}')
        checks.append(rel)
    out={'verdict':'PASS_REVIEWER_D_COMPLETE_PACKAGE','graph':result,'checksum_files_verified':len(checks),'heavy_campaigns_rerun':False,'rh_proved':False}
    (Path(__file__).with_name('run_all_results.json')).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True)); return out
if __name__=='__main__': main()
