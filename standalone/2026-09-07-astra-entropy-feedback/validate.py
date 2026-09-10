#!/usr/bin/env python3
"""Authenticate this packet's exact inventory; not an analytic proof checker."""
import hashlib
import json
from pathlib import Path
import re
import sys


def main():
    root=Path(__file__).resolve().parent
    manifest=root/'SHA256SUMS'
    rows={}
    for line in manifest.read_text().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)',line)
        if not m or m[2] in rows or m[2]=='SHA256SUMS':
            raise ValueError('invalid/duplicate manifest entry')
        rows[m[2]]=m[1]
    actual={p.name for p in root.iterdir() if p.name!='SHA256SUMS'}
    if not rows or actual != rows.keys():
        raise ValueError('exact inventory mismatch')
    for name, digest in rows.items():
        p=root/name
        if p.is_symlink() or not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
            raise ValueError('payload mismatch: '+name)
    source=json.loads((root/'SOURCES.json').read_text())
    if source['status']!='PROPOSED_COMPONENTS_RH_OPEN':
        raise ValueError('source status changed')
    if any(p['commit']!='b6635a70a75b60050177d5cde67e911093698664'
           for p in source['parent_sources']):
        raise ValueError('parent version changed')
    print(json.dumps({'status':'PASS_PACKET_BYTES_ONLY','files':len(rows)+1,
                      'parent_mathematical_suites_rerun':False,
                      'infinite_analytic_proofs_machine_verified':False},sort_keys=True))


if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError,TypeError) as e:
        print('REJECT: '+str(e),file=sys.stderr)
        raise SystemExit(1)
