#!/usr/bin/env python3
"""Authenticate the declared byte inventory; optional exact parent-source check."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys


def validate(root: Path,parent:Path|None=None)->dict:
    manifest=root/'SHA256SUMS'
    wanted={}
    for line in manifest.read_text().splitlines():
        digest,name=line.split('  ',1)
        if name in wanted or not name or Path(name).is_absolute() or '..' in Path(name).parts:
            raise ValueError('invalid or repeated manifest path')
        wanted[name]=digest
    present={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
             and '__pycache__' not in p.parts and p.name!='SHA256SUMS'}
    if set(wanted)!=present:raise ValueError('inventory mismatch')
    for name,digest in wanted.items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest:
            raise ValueError('hash mismatch: '+name)
    if (root/'checks.normal.json').read_bytes()!=(root/'checks.optimized.json').read_bytes():
        raise ValueError('normal/optimized output mismatch')
    checked=0
    if parent is not None:
        for row in csv.DictReader((root/'SOURCES.tsv').open(),delimiter='\t'):
            data=(parent/row['path']).read_bytes()
            blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            if blob!=row['git_blob'] or hashlib.sha256(data).hexdigest()!=row['sha256']:
                raise ValueError('parent source identity mismatch')
            checked+=1
    return {'status':'PASS_BYTE_INVENTORY','files':len(wanted)+1,
            'parent_sources_checked':checked,'analytic_proofs_machine_verified':False}

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--parent-repo',type=Path)
    a=ap.parse_args()
    try:print(json.dumps(validate(a.root,a.parent_repo),sort_keys=True));return 0
    except (OSError,ValueError,KeyError) as e:
        print('REJECTED: '+str(e),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
