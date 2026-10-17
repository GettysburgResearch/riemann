#!/usr/bin/env python3
"""Check the exact files, lengths, SHA-256 values and Git blob identities."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for name,item in manifest['files'].items():
    data=(root/name).read_bytes()
    blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
    if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256'] or blob!=item['git_blob']:
        raise RuntimeError(f'manifest mismatch: {name}')
print(json.dumps({'status':'PASS','payload_files_checked':len(manifest['files'])},sort_keys=True))
