#!/usr/bin/env python3
"""Authenticate payload bytes only, never mathematical validity."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
actual={p.name for p in root.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
if actual!=set(manifest['files']): raise ValueError('Unexpected or missing payload file')
for name,expected in manifest['files'].items():
    data=(root/name).read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    got={'bytes':len(data),'git_blob':blob,'sha256':hashlib.sha256(data).hexdigest()}
    if got!=expected: raise ValueError(f'Manifest mismatch: {name}')
print(json.dumps({'status':'PASS','authenticated_files':len(actual),'scope':'bytes only'},sort_keys=True))
