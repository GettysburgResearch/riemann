#!/usr/bin/env python3
"""Verify recorded payload identities; not a mathematical certificate."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for item in manifest['files']:
    p=root/item['path'];data=p.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256'] or blob!=item['git_blob']:
        raise SystemExit('mismatch: '+item['path'])
print('PASS '+str(len(manifest['files']))+' payload files')
