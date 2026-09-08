#!/usr/bin/env python3
"""Authenticate this bounded packet's exact inventory and byte manifest."""
from pathlib import Path
import hashlib
import re
import sys

EXPECTED={
 'PROOF.md','ATTEMPT.md','README.md','CLAIMS.tsv','EDGES.tsv','SOURCES.json',
 'checks.py','checks.normal.json','checks.optimized.json','validate.py',
 'rejections.py','rejections.json','VALIDATION.md','SHA256SUMS'}

def main():
    root=Path(__file__).resolve().parent
    children=list(root.iterdir())
    if {p.name for p in children} != EXPECTED:
        raise ValueError('exact packet inventory mismatch')
    if any(p.is_symlink() or not p.is_file() for p in children):
        raise ValueError('non-regular packet member')
    entries={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        match=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)',line)
        if not match: raise ValueError('invalid manifest row')
        digest,name=match.groups()
        if name in entries: raise ValueError('duplicate manifest member')
        entries[name]=digest
    if set(entries)!=EXPECTED-{'SHA256SUMS'}:
        raise ValueError('exact manifest coverage mismatch')
    for name,digest in entries.items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest:
            raise ValueError('byte mismatch: '+name)
    print('PASS_PACKET_BYTES_14_FILES_13_DIGESTS')

if __name__=='__main__':
    try: main()
    except Exception as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
