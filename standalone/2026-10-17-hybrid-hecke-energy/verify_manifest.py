#!/usr/bin/env python3
"""Authenticate this packet's listed bytes, not its mathematical conclusions."""
import hashlib,json,pathlib
p=pathlib.Path(__file__).resolve().parent
m=json.loads((p/'MANIFEST.json').read_text())
for name,v in m['files'].items():
    b=(p/name).read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if len(b)!=v['bytes'] or hashlib.sha256(b).hexdigest()!=v['sha256'] or blob!=v['git_blob']:
        raise RuntimeError('manifest mismatch: '+name)
print('PASS: '+str(len(m['files']))+' payload files match; not a proof certificate')
