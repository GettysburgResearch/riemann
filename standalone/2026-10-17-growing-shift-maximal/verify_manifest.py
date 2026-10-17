#!/usr/bin/env python3
"""Authenticate the exact packet, not its analytic claims."""
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for item in manifest['files']:
    p=root/item['path']; b=p.read_bytes()
    sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if len(b)!=item['bytes'] or hashlib.sha256(b).hexdigest()!=item['sha256'] or sha!=item['git_blob']:
        raise SystemExit('FAIL_MANIFEST '+item['path'])
print('PASS_MANIFEST',len(manifest['files']))
