#!/usr/bin/env python3
"""Authenticate this flat packet. This is not a mathematical proof checker."""
import hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
NAMES={'README.md','PROOF.md','SYNTHESIS_AND_ATTEMPT.md','SOURCES.json','CLAIMS.json',
       'check.py','result.json','validate.py','test_rejections.py','VALIDATION.md','SHA256SUMS'}

def validate():
    paths=list(ROOT.iterdir())
    if {p.name for p in paths}!=NAMES:raise ValueError('unexpected packet inventory')
    if any(p.is_symlink() or not p.is_file() for p in paths):raise ValueError('nonregular packet input')
    entries={}
    for row in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,n=row.split('  ')
        if n in entries or n not in NAMES or len(h)!=64 or any(c not in '0123456789abcdef' for c in h):raise ValueError('invalid manifest')
        entries[n]=h
    if set(entries)!=NAMES-{'SHA256SUMS'}:raise ValueError('incomplete manifest')
    for n,h in entries.items():
        if hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h:raise ValueError('hash mismatch: '+n)
    print('PASS_PACKET_BYTES files=11 hashed=10; no infinite mathematics is machine-verified')

if __name__=='__main__':validate()
