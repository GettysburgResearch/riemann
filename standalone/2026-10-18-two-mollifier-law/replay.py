#!/usr/bin/env python3
"""Authenticate bytes and replay finite checks, not an analytic theorem validator."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

def oid(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def main():
    here=Path(__file__).resolve().parent
    manifest=json.loads((here/'MANIFEST.json').read_text())
    actual={p.name for p in here.iterdir() if p.is_file()}
    if actual!=set(manifest['files'])|{'MANIFEST.json'}:
        raise RuntimeError('Unexpected file inventory')
    for name,record in manifest['files'].items():
        data=(here/name).read_bytes()
        if (len(data)!=record['bytes'] or hashlib.sha256(data).hexdigest()!=record['sha256']
                or oid(data)!=record['git_blob']):
            raise RuntimeError('Manifest mismatch: '+name)
    for flags in ([],['-O']):
        result=subprocess.check_output([sys.executable,*flags,'verify.py'],cwd=here,timeout=40)
        if result!=(here/'CHECKS.json').read_bytes():
            raise RuntimeError('Accepting report mismatch')
    result=subprocess.check_output([sys.executable,'run_mutations.py'],cwd=here,timeout=120)
    if result!=(here/'MUTATIONS.json').read_bytes():
        raise RuntimeError('Mutation report mismatch')
    print(json.dumps({'manifested_files':len(manifest['files']),
       'modes':['normal','optimized'],'separate_corrupted_processes':8,
       'finite_predicates':35845,'analytic_certification':False,'rh_proved':False},sort_keys=True))

if __name__=='__main__': main()
