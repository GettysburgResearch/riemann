#!/usr/bin/env python3
"""Run both accepting modes, all corruptions, and exact byte authentication."""
from pathlib import Path
import json,subprocess,sys
root=Path(__file__).resolve().parent
out=[]
for args,expected in [(['verify_manifest.py'],None),(['verify.py'],'CHECKS.json'),
                      (['-O','verify.py'],'CHECKS.json'),(['run_mutations.py'],'MUTATIONS.json')]:
    p=subprocess.run([sys.executable]+args,cwd=root,capture_output=True,timeout=90)
    if p.returncode:
        raise RuntimeError(p.stderr.decode(errors='replace'))
    if expected and p.stdout!=(root/expected).read_bytes():
        raise ValueError('Archived output mismatch: '+expected)
    out.append({'command':args,'expected_report':expected,'status':'PASS'})
print(json.dumps({'status':'PASS','reports':out,
                  'scope':'Finite regression and byte replay, not analytic certification.'},sort_keys=True,indent=2))
