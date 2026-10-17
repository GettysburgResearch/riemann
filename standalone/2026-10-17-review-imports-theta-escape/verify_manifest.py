#!/usr/bin/env python3
"""Authenticate payload bytes, not theorem validity."""
from pathlib import Path
import hashlib
import json
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='MANIFEST.json'}
expected=set(manifest['files'])
if actual!=expected:
    raise RuntimeError(f'Inventory mismatch: missing={expected-actual}, extra={actual-expected}')
for name,record in manifest['files'].items():
    data=(root/name).read_bytes()
    calculated={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                'git_blob_sha1':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
    if calculated!=record: raise RuntimeError(f'Byte mismatch: {name}')
print(json.dumps({'status':'PASS','authenticated_files':len(expected),'scope':'bytes only'},sort_keys=True))
