#!/usr/bin/env python3
"""Verify the packet's frozen local bytes; this is not a mathematical review."""
from hashlib import sha256
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'MANIFEST.json').read_text())
for item in manifest['files']:
    path=root/item['path']
    data=path.read_bytes()
    if len(data)!=item['bytes'] or sha256(data).hexdigest()!=item['sha256']:
        raise SystemExit(f"Integrity mismatch: {item['path']}")
expected={item['path'] for item in manifest['files']}|{'MANIFEST.json'}
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
if actual!=expected:
    raise SystemExit(f"Unexpected inventory difference: {actual^expected}")
print(f"PASS: {len(manifest['files'])} file hashes and complete local inventory")
