#!/usr/bin/env python3
"""Verify exact local payload identities; not a mathematical verifier."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'MANIFEST.json').read_text())
for f in data['files']:
    p=root/f['path'];b=p.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if len(b)!=f['bytes'] or hashlib.sha256(b).hexdigest()!=f['sha256'] or blob!=f['git_blob']:
        raise SystemExit('identity mismatch: '+f['path'])
print(json.dumps({'status':'PASS','payload_files':len(data['files']),'scope':'file identities only'},sort_keys=True))
