#!/usr/bin/env python3
"""Verify packet bytes only; this does not certify the mathematics."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
expected = set(manifest['files'])
actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
          and p.name != 'MANIFEST.json' and '__pycache__' not in p.parts}
if actual != expected:
    raise RuntimeError(f'inventory mismatch: {actual ^ expected}')
for name, record in manifest['files'].items():
    data = (root / name).read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if (len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']
            or blob != record['git_blob_sha1']):
        raise RuntimeError(f'content mismatch: {name}')
print(json.dumps({'status': 'PASS', 'files': len(expected)}, sort_keys=True))
