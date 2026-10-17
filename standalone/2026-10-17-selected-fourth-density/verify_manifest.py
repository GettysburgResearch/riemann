#!/usr/bin/env python3
"""Authenticate the local payload bytes, not its mathematical statements."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
manifest = json.loads((root/'MANIFEST.json').read_text())
for name, item in manifest['files'].items():
    data = (root/name).read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256'] or blob != item['git_blob']:
        raise ValueError('payload mismatch: '+name)
print('PASS: '+str(len(manifest['files']))+' payload byte identities; no mathematical certification')
