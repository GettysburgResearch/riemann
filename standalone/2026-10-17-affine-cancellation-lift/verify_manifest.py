#!/usr/bin/env python3
"""Check payload identity; this is not mathematical verification."""
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for rec in manifest['files']:
    p=(root/rec['path']).resolve()
    if not p.is_relative_to(root): raise SystemExit('Unsafe manifest path')
    data=p.read_bytes()
    blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
    if len(data)!=rec['bytes'] or hashlib.sha256(data).hexdigest()!=rec['sha256'] or blob!=rec['git_blob']:
        raise SystemExit('Payload mismatch: '+rec['path'])
print('PASS_MANIFEST',len(manifest['files']))
