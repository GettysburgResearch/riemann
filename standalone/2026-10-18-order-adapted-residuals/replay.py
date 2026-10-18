#!/usr/bin/env python3
"""Byte and finite-algebra replay. Executes ONLY the checked local verifier."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent

def main():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name, info in manifest['files'].items():
        p=ROOT/name
        if p.parent!=ROOT:raise ValueError('Unsafe manifest name')
        data=p.read_bytes()
        if len(data)!=info['bytes'] or hashlib.sha256(data).hexdigest()!=info['sha256']:
            raise ValueError(f'Byte mismatch: {name}')
    archived=(ROOT/'CHECKS.json').read_bytes()
    for opt in [[],['-O']]:
        got=subprocess.run([sys.executable,*opt,str(ROOT/'verify.py')],check=True,capture_output=True).stdout
        if got!=archived:raise ValueError(f'Changed accepting report: {opt}')
    controls=json.loads((ROOT/'MUTATIONS.json').read_text())
    for name,expected in controls.items():
        got=subprocess.run([sys.executable,'-O',str(ROOT/'verify.py'),'--mutation',name],capture_output=True)
        text=got.stderr.decode()
        if got.returncode==0 or expected['gate'] not in text:raise ValueError(f'Mutation not rejected: {name}')
    print(json.dumps({'manifest_payloads':len(manifest['files']),'accepting_modes':2,
                      'rejected_mutations':len(controls),'scope':'finite algebra and bytes, not independent analytic review'},sort_keys=True,indent=2))

if __name__=='__main__':main()
