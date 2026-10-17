#!/usr/bin/env python3
"""Check file bytes and Git blob identities, not mathematical validity."""
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
actual={p.name for p in root.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
if actual!=set(manifest['files']):
    raise RuntimeError('missing or unlisted payload file')
for name,item in manifest['files'].items():
    b=(root/name).read_bytes()
    got={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
         'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
    if got!=item:
        raise RuntimeError(f'payload identity mismatch: {name}')
print(json.dumps({'status':'PASS: bytes only','payload_files':len(actual)},sort_keys=True))
