#!/usr/bin/env python3
"""Verify packet identities, not mathematical validity."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'MANIFEST.json').read_text())
for name, expected in manifest['files'].items():
    path=root/name
    if not path.is_file():
        raise RuntimeError(f'missing {name}')
    data=path.read_bytes()
    actual={'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
    if actual != expected:
        raise RuntimeError(f'identity mismatch: {name}')
print(json.dumps({'status':'PASS','payloads':len(manifest['files']),
                  'scope':'file identity only; no proof certification'},sort_keys=True))
