#!/usr/bin/env python3
"""Check payload identities. The manifest excludes itself by design."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for name,expected in manifest['files'].items():
    data=(root/name).read_bytes()
    actual={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
    if actual!=expected:
        raise ArithmeticError('Identity mismatch: '+name)
print('PASS: '+str(len(manifest['files']))+' payload identities; not proof certification')
