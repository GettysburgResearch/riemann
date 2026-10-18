#!/usr/bin/env python3
"""Authenticate payload and replay exact finite reports. No network access."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent

def main() -> None:
    manifest=json.loads((HERE/'MANIFEST.json').read_text())
    for name,meta in manifest['files'].items():
        data=(HERE/name).read_bytes()
        git=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        if len(data)!=meta['bytes'] or hashlib.sha256(data).hexdigest()!=meta['sha256'] or git!=meta['git_blob']:
            raise RuntimeError(f'payload mismatch: {name}')
    for args,target in [(['verify.py'],'CHECKS.json'),(['-O','verify.py'],'CHECKS.json'),
                        (['run_mutations.py'],'MUTATIONS.json')]:
        run=subprocess.run([sys.executable]+args,cwd=HERE,check=True,capture_output=True,timeout=90)
        if run.stdout!=(HERE/target).read_bytes():
            raise RuntimeError(f'replay mismatch: {args}')
    print(json.dumps({'status':'PASS','manifest_payloads':len(manifest['files']),
                      'exact_modes':['normal','optimized'],'actual_mutation_processes':9},sort_keys=True))

if __name__=='__main__':
    main()
