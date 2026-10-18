#!/usr/bin/env python3
"""Check payload bytes and rerun the exact reports. No external packages or network."""
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
        blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        if len(data)!=meta['bytes'] or hashlib.sha256(data).hexdigest()!=meta['sha256'] or blob!=meta['git_blob']:
            raise RuntimeError(f'payload mismatch: {name}')
    for args,expected in [(['verify.py'],'CHECKS.json'),(['-O','verify.py'],'CHECKS.json'),
                         (['run_mutations.py'],'MUTATIONS.json')]:
        result=subprocess.run([sys.executable]+args,cwd=HERE,capture_output=True,check=True,timeout=90)
        if result.stdout!=(HERE/expected).read_bytes():
            raise RuntimeError(f'replay mismatch: {args}')
    print(json.dumps({'status':'PASS','payloads':len(manifest['files']),
       'checker_modes':['normal','optimized'],'executed_negative_controls':10},sort_keys=True))

if __name__=='__main__':
    main()
