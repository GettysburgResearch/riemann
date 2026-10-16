#!/usr/bin/env python3
"""Check this packet's own byte identities, not mathematical correctness."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'MANIFEST.json').read_text())
for item in manifest['files']:
    data=(root/item['path']).read_bytes()
    if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256']:
        raise RuntimeError('byte mismatch: '+item['path'])
print(json.dumps({'payload_files_verified':len(manifest['files']),
                  'mathematical_certification':False},sort_keys=True))
