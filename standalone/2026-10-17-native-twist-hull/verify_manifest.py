#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text())
for item in manifest['files']:
    data=(root/item['path']).read_bytes()
    sha=hashlib.sha256(data).hexdigest()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if (sha,blob,len(data))!=(item['sha256'],item['git_blob'],item['bytes']):
        raise SystemExit('Mismatch: '+item['path'])
print('PASS: all '+str(len(manifest['files']))+' payload files match.')
