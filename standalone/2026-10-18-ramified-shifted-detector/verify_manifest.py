#!/usr/bin/env python3
"""Authenticate packet bytes; does not certify mathematical conclusions."""
from pathlib import Path
import hashlib
import json

def unique(pairs):
    out={}
    for key,value in pairs:
        if key in out: raise ValueError('duplicate manifest key '+key)
        out[key]=value
    return out

root=Path(__file__).resolve().parent
m=json.loads((root/'MANIFEST.json').read_text(),object_pairs_hook=unique)
for name,item in m['files'].items():
    if Path(name).name!=name: raise ValueError('unexpected path '+name)
    data=(root/name).read_bytes()
    actual={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
    if actual!=item: raise ValueError('byte identity mismatch '+name)
print('PASS: '+str(len(m['files']))+' payload byte identities; no analytic certification')
