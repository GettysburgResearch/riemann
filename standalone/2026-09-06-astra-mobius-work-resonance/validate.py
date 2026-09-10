#!/usr/bin/env python3
"""Authenticate the exact local packet inventory; not mathematical acceptance."""
from pathlib import Path
import hashlib,json,sys

def validate(root:Path)->dict:
    entries={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        h,sep,name=line.partition('  ')
        if not sep or len(h)!=64 or name in entries or '/' in name or name.startswith('.'):
            raise ValueError('invalid or duplicate manifest row')
        entries[name]=h
    for p in root.iterdir():
        if p.is_symlink() or (p.is_dir() and p.name!='__pycache__'):
            raise ValueError('unexpected directory or symlink')
    actual={p.name for p in root.iterdir() if p.is_file()}
    if actual != set(entries)|{'SHA256SUMS'}:raise ValueError('exact file inventory mismatch')
    for name,h in entries.items():
        p=root/name
        if p.is_symlink() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:
            raise ValueError('file authentication failed: '+name)
    if (root/'checks.normal.json').read_bytes()!=(root/'checks.optimized.json').read_bytes():
        raise ValueError('exact-check modes disagree')
    if (root/'certificate.normal.json').read_bytes()!=(root/'certificate.optimized.json').read_bytes():
        raise ValueError('directed-certificate modes disagree')
    return {'status':'INVENTORY_AUTHENTICATED','files':len(actual),
            'scope':'Byte inventory only; analytic proofs are not machine-checked.'}
if __name__=='__main__':
    try:print(json.dumps(validate(Path(__file__).resolve().parent),sort_keys=True));sys.exit(0)
    except (OSError,ValueError) as e:print(str(e),file=sys.stderr);sys.exit(2)
