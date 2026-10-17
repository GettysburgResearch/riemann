#!/usr/bin/env python3
"""Verify payload bytes, not the correctness of their mathematics."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'MANIFEST.json').read_text())
for row in data['files']:
    b=(root/row['path']).read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256'] or blob!=row['git_blob']:
        raise RuntimeError('payload mismatch: '+row['path'])
print('PASS: '+str(len(data['files']))+' payload files match; no proof certification implied.')
