#!/usr/bin/env python3
"""Replay the complete finite certificate; no network or third-party packages."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent

def main():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name,info in manifest['files'].items():
        data=(ROOT/name).read_bytes()
        if len(data)!=info['bytes'] or hashlib.sha256(data).hexdigest()!=info['sha256']:
            raise ValueError('Manifest mismatch: '+name)
    matches=[]
    # Controls temporarily alter parameters with finally restoration: run sequentially.
    for script,expected in [('certify.py','CERTIFICATE.json'),('controls.py','CONTROLS.json')]:
        for mode in [[],['-O']]:
            actual=subprocess.check_output([sys.executable,*mode,str(ROOT/script)],cwd=ROOT)
            if actual!=(ROOT/expected).read_bytes():
                raise ValueError('Replay mismatch: '+script+' '+str(mode))
            matches.append(script+(' optimized' if mode else ' ordinary'))
    print(json.dumps({'status':'PASS finite replay only; not RH or independent mathematical review',
                      'verified_payloads':len(manifest['files']),'matched_runs':matches},sort_keys=True,indent=2))
if __name__=='__main__':main()
