#!/usr/bin/env python3
"""Authenticate the sealed local inventory. The remote commit is the trust anchor."""
import hashlib
from pathlib import Path

EXPECTED={'PROOF.md','APPLICATION.md','README.md','CLAIMS.json','SOURCES.json',
          'check.py','result.json','validate.py','test_rejections.py',
          'VALIDATION.md','SHA256SUMS'}


def validate(root: Path) -> None:
    entries=list(root.iterdir())
    if any(p.is_symlink() or not p.is_file() for p in entries):
        raise ValueError('non-regular packet entry')
    if {p.name for p in entries}!=EXPECTED:raise ValueError('inventory mismatch')
    found={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        parts=line.split('  ')
        if len(parts)!=2:raise ValueError('malformed manifest')
        sha,name=parts
        if name in found or name not in EXPECTED-{'SHA256SUMS'}:
            raise ValueError('duplicate or extra manifest path')
        if len(sha)!=64 or any(c not in '0123456789abcdef' for c in sha):
            raise ValueError('malformed digest')
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=sha:
            raise ValueError('digest mismatch: '+name)
        found[name]=sha
    if set(found)!=EXPECTED-{'SHA256SUMS'}:raise ValueError('manifest coverage')

if __name__=='__main__':
    validate(Path(__file__).resolve().parent)
    print('PASS_EXACT_PACKET_INVENTORY')
