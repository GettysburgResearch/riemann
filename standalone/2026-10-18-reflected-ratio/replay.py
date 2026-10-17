#!/usr/bin/env python3
"""Reproduce only the declared finite checks and archive identities."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
MUTATIONS={
 'convex-numerator':'central class budget',
 'reverse-fe-power':'functional equation conductor power',
 'wrong-character':'functional-equation character matches denominator',
 'old-domain':'old ramified domain',
 'upper-count':'count at lower threshold',
 'lost-tail-gap':'large-frequency negative power',
 'missing-terminal':'all 37 classes including terminal',
 'wrong-mellin-shift':'wrong borrowed Mellin shift',
}

def execute(args):
 return subprocess.run([sys.executable,*args],cwd=HERE,capture_output=True,text=False,timeout=30)

def main():
 for mode in ([],['-O']):
  for opts,target in (([],'CHECKS.json'),(['--details'],'CERTIFICATE.json')):
   proc=execute([*mode,'verify.py',*opts])
   if proc.returncode or proc.stdout!=(HERE/target).read_bytes():
    raise RuntimeError(f'replay failed: {mode} {opts}: {proc.stderr.decode()}')
 outcomes={}
 for mutation,message in MUTATIONS.items():
  proc=execute(['-O','verify.py','--mutate',mutation])
  text=proc.stderr.decode()
  if proc.returncode==0 or message not in text:
   raise RuntimeError(f'mutation not rejected at intended gate: {mutation}: {text}')
  outcomes[mutation]={'rejected':True,'expected_error':message}
 expected=json.loads((HERE/'MUTATIONS.json').read_text())
 if outcomes!=expected:raise RuntimeError('mutation report mismatch')
 manifest=json.loads((HERE/'MANIFEST.json').read_text())
 for name,meta in manifest['files'].items():
  data=(HERE/name).read_bytes()
  if len(data)!=meta['bytes'] or hashlib.sha256(data).hexdigest()!=meta['sha256']:
   raise RuntimeError(f'manifest mismatch: {name}')
 print(json.dumps({'status':'PASS','normal_and_optimized_reports':4,'mutations_rejected':8,
                   'manifest_files':len(manifest['files']),'analytic_theorem_certified':False},sort_keys=True,indent=2))

if __name__=='__main__':main()
