#!/usr/bin/env python3
"""Check exact payload bytes; --write freezes a local inventory (not proof validity)."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def inventory(root):
    return {p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                        git_blob=blob(p.read_bytes()))
            for p in sorted(root.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    actual=inventory(root)
    if args.write:
        (root/'MANIFEST.json').write_text(json.dumps(actual,sort_keys=True,indent=2)+'\n')
    expected=json.loads((root/'MANIFEST.json').read_text())
    if actual!=expected: raise ValueError('Payload manifest mismatch')
    print(json.dumps({'verified_payload_files':len(actual),'analytic_certification':False},sort_keys=True))

if __name__=='__main__': main()
