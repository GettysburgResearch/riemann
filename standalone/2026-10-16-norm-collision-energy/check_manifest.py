#!/usr/bin/env python3
"""Check payload byte identities; not a mathematical verifier."""
from pathlib import Path
import hashlib
import json

def main():
    root=Path(__file__).resolve().parent
    manifest=json.loads((root/'MANIFEST.json').read_text())
    for rel, expected in manifest['files'].items():
        path=(root/rel).resolve()
        if not path.is_relative_to(root):
            raise RuntimeError(f'unsafe manifest path: {rel}')
        b=path.read_bytes()
        actual={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
                'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
        if actual!=expected:raise RuntimeError(f'payload mismatch: {rel}')
    print(f"PASS: {len(manifest['files'])} payload files match; no proof certification implied")
if __name__=='__main__':main()
