#!/usr/bin/env python3
"""Verify local payload bytes, not the mathematical claims."""
import hashlib,json,pathlib
root=pathlib.Path(__file__).resolve().parent
items=json.loads((root/'MANIFEST.json').read_text())['files']
for name,expected in items.items():
    data=(root/name).read_bytes()
    actual={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
    if actual!=expected:raise RuntimeError('Manifest mismatch: '+name)
print('PASS: '+str(len(items))+' payload files; byte identity only')
