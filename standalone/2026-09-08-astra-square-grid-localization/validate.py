#!/usr/bin/env python3
"""Authenticate the exact SSQ26 packet inventory; optionally its parent proof.
This is byte validation, not mathematical verification of the manuscripts.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys

FILES = {'README.md','PROOF.md','ATTEMPT.md','SOURCES.json','CLAIMS.json',
         'check.py','result.json','validate.py','test_rejections.py',
         'rejections.json','VALIDATION.md','SHA256SUMS'}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-root', type=Path)
    args=ap.parse_args()
    root=Path(__file__).absolute().parent
    require({x.name for x in root.iterdir()} == FILES, 'inventory mismatch')
    for name in FILES:
        p=root/name
        require(p.is_file() and not p.is_symlink(), 'nonregular payload '+name)
    entries={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        digest, name=line.split('  ',1)
        require(name in FILES-{'SHA256SUMS'} and name not in entries, 'manifest path')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest), 'digest')
        entries[name]=digest
    require(set(entries)==FILES-{'SHA256SUMS'}, 'incomplete manifest')
    for name,digest in entries.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,
                'payload digest '+name)
    parent_checked=False
    if args.parent_root:
        source=json.loads((root/'SOURCES.json').read_text())['parent_proof']
        p=args.parent_root/source['path']
        require(p.is_file() and not p.is_symlink(), 'parent unavailable/nonregular')
        b=p.read_bytes()
        require(len(b)==source['bytes'], 'parent length')
        require(hashlib.sha256(b).hexdigest()==source['sha256'], 'parent SHA256')
        require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
                ==source['git_blob'], 'parent Git identity')
        parent_checked=True
    print(json.dumps({'status':'PASS_SSQ26_PACKET_BYTES','files':len(FILES),
                      'parent_proof_bytes_checked':parent_checked},sort_keys=True))

if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
