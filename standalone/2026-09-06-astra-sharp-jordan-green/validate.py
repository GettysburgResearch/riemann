#!/usr/bin/env python3
"""Verify the exact packet inventory and SHA256; this is not a proof checker."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys

P=Path(__file__).resolve().parent
try:
    records={}
    for line in (P/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        if len(digest)!=64 or any(c not in '0123456789abcdef' for c in digest):
            raise ValueError('bad digest')
        if '/' in name or name in records or name=='SHA256SUMS':
            raise ValueError('bad or duplicate filename')
        records[name]=digest
    files={p.name for p in P.iterdir() if p.is_file()}
    if files!=set(records)|{'SHA256SUMS'}:
        raise ValueError('inventory mismatch')
    if any(p.is_dir() for p in P.iterdir()):
        raise ValueError('unexpected directory')
    for name,digest in records.items():
        if hashlib.sha256((P/name).read_bytes()).hexdigest()!=digest:
            raise ValueError('hash mismatch: '+name)
    a=(P/'checks.normal.json').read_bytes();b=(P/'checks.optimized.json').read_bytes()
    if a!=b:raise ValueError('normal/optimized result mismatch')
    obj=json.loads(a)
    if obj['RH_proved'] is not False or obj['analytic_proofs_machine_checked'] is not False:
        raise ValueError('scope flags')
    print(json.dumps({'status':'PASS_PACKET_BYTES','files':len(files),'hashes':len(records)},sort_keys=True))
except (OSError,ValueError,KeyError) as exc:
    print(json.dumps({'status':'REJECTED','reason':str(exc)},sort_keys=True))
    sys.exit(2)
