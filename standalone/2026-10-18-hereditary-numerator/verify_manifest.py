#!/usr/bin/env python3
"""Authenticate the complete flat packet, excluding this manifest's own bytes."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def main() -> None:
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    listed=manifest['files']
    actual={p.name for p in ROOT.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
    if actual!=set(listed):
        raise ValueError('Unexpected or missing packet files')
    for name,record in sorted(listed.items()):
        p=ROOT/name
        if p.is_symlink() or p.parent!=ROOT:
            raise ValueError('Unsafe path')
        data=p.read_bytes()
        if (len(data)!=record['bytes'] or hashlib.sha256(data).hexdigest()!=record['sha256']
                or blob(data)!=record['git_blob']):
            raise ValueError('Hash mismatch: '+name)
    print(json.dumps({'manifested_files':len(listed),'passed':True,
                      'analytic_verification':False},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
