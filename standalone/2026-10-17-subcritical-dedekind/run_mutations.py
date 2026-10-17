#!/usr/bin/env python3
"""Launch actual corrupted finite models; not mutations of a formal proof."""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path
from verify import MUTATIONS
EXPECTED={
'drop-diagonal':'dyadic-envelope:',
'individual-numerator':'central-budgets: good',
'upper-count':'partition: count of middle 0',
'old-shift':'identities: principal shift',
'zero-tail-gap':'large-tail: strict cutoff gap',
'delete-subunit-profile':'profile-tail: retain C=1 when T<1',
'wrong-beta':'identities: local S0'}
reports=[]
for name in MUTATIONS:
    process=subprocess.run([sys.executable,'-O',str(Path(__file__).with_name('verify.py')),
                            '--mutation',name],capture_output=True,text=True,timeout=30)
    if process.returncode==0 or EXPECTED[name] not in process.stderr:
        raise RuntimeError(f'Wrong mutation result for {name}: {process.stderr}')
    reports.append({'mutation':name,'returncode':process.returncode,
                    'failure':process.stderr.strip().splitlines()[-1]})
print(json.dumps({'status':'PASS: all seven corrupted finite models rejected',
                  'scope':'not analytic or proof-assistant certification',
                  'results':reports},indent=2,sort_keys=True))
