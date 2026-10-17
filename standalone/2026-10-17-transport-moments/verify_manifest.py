#!/usr/bin/env python3
"""Verify payload bytes; this does not verify mathematical theorems."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root/'MANIFEST.json').read_text())
for name, rec in manifest['files'].items():
    data = (root/name).read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if len(data) != rec['bytes'] or hashlib.sha256(data).hexdigest() != rec['sha256'] or blob != rec['git_blob']:
        raise RuntimeError('Payload mismatch: '+name)
print(f"PASS: {len(manifest['files'])} payloads match; no mathematical certification implied")
