#!/usr/bin/env python3
"""Authenticate payloads and replay finite checks, never a theorem validator."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def main():
    root=Path(__file__).resolve().parent
    manifest=json.loads((root/'MANIFEST.json').read_text())
    actual={p.name for p in root.iterdir() if p.is_file()}
    expected=set(manifest['files'])|{'MANIFEST.json'}
    if actual!=expected: raise RuntimeError('Unexpected payload inventory')
    for name,rec in manifest['files'].items():
        data=(root/name).read_bytes()
        if len(data)!=rec['bytes'] or hashlib.sha256(data).hexdigest()!=rec['sha256'] or git_blob(data)!=rec['git_blob']:
            raise RuntimeError('Integrity failure: '+name)
    for flags in ([],['-O']):
        out=subprocess.check_output([sys.executable,*flags,'verify.py'],cwd=root,timeout=30)
        if out!=(root/'CHECKS.json').read_bytes(): raise RuntimeError('Check report mismatch')
    out=subprocess.check_output([sys.executable,'run_mutations.py'],cwd=root,timeout=90)
    if out!=(root/'MUTATIONS.json').read_bytes(): raise RuntimeError('Mutation report mismatch')
    print(json.dumps({'manifested_files':len(manifest['files']),'checker_modes':['normal','optimized'],'mutations':7,'scope':'finite algebra and bytes; not analytic proof','rh_proved':False},sort_keys=True))

if __name__=='__main__':main()
