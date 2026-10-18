#!/usr/bin/env python3
"""Authenticate the exact payload inventory; execute no other file."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
actual={p.name for p in root.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
if actual != set(manifest['files']):
    raise ValueError('Unexpected or missing payload files')
for name,meta in manifest['files'].items():
    b=(root/name).read_bytes()
    if len(b)!=meta['bytes'] or hashlib.sha256(b).hexdigest()!=meta['sha256']:
        raise ValueError('Payload identity mismatch: '+name)
print(json.dumps({'status':'PASS','authenticated_payloads':len(actual)},sort_keys=True,indent=2))
