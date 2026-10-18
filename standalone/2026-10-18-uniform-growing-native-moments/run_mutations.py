#!/usr/bin/env python3
"""Run actual corrupted finite proof models in separate optimized processes."""
from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
from verify import MUTATIONS
root=Path(__file__).resolve().parent
reports=[]
for name in MUTATIONS:
    proc=subprocess.run([sys.executable,'-O','verify.py','--mutation',name],
                        cwd=root,capture_output=True,text=True,timeout=30)
    if proc.returncode==0:
        raise RuntimeError('Corrupted model accepted: '+name)
    diagnostic=proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else ''
    if not diagnostic.startswith('ValueError:'):
        raise RuntimeError('Mutation failed for an unintended reason: '+repr(diagnostic))
    reports.append({'mutation':name,'returncode':proc.returncode,'diagnostic':diagnostic})
print(json.dumps({'status':'PASS','rejected_models':len(reports),'models':reports,
                 'scope':'Corrupted finite models, not proof-assistant perturbations.'},indent=2,sort_keys=True))
