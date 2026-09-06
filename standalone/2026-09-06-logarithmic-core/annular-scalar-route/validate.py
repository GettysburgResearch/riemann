#!/usr/bin/env python3
"""Closed delivery inventory, not a proof of the unbounded arithmetic sign."""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
FILES={'PROOF.md','README.md','SOURCES.md','SOURCE_LOCK.json','VALIDATION.md',
       'verify.py','result.json','validate.py','test_rejections.py','SHA256SUMS'}

def need(ok,message):
    if not ok: raise ValueError(message)

def main():
    actual={p.name for p in ROOT.iterdir() if p.name!='__pycache__'}
    need(actual==FILES,'unexpected or missing delivery path')
    declared={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)',line)
        need(m is not None,'invalid manifest row')
        digest,name=m.groups()
        need(name not in declared,'duplicate manifest path')
        declared[name]=digest
    need(set(declared)==FILES-{'SHA256SUMS'},'manifest inventory mismatch')
    for name,digest in declared.items():
        p=ROOT/name
        need(p.is_file() and not p.is_symlink(),'not a regular source file')
        need(sha256(p.read_bytes()).hexdigest()==digest,'hash mismatch: '+name)
    s=json.loads((ROOT/'SOURCE_LOCK.json').read_text())
    need(s['parent_commit']=='893d93b045099d9920fadf4b0e5bcb51d0455832','wrong parent')
    need(s['rh_proved'] is False and s['terminal_bound_proved'] is False,'false proof status')
    print(json.dumps({'status':'PASS_DELIVERY_ONLY','files':len(FILES),'hashes':len(declared)},sort_keys=True))

if __name__=='__main__':main()
