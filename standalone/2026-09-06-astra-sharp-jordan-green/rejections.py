#!/usr/bin/env python3
"""Actual CLI refusals for corrupted retained reports; no analytic-proof claim."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

P=Path(__file__).resolve().parent
base=json.loads((P/'checks.normal.json').read_text())
mutations=[]
for key,value in [('RH_proved',True),('analytic_proofs_machine_checked',True),
                  ('fixture_count',777),('check_count',True),('zeta_gamma_evaluations',1),
                  ('schema','wrong')]:
    obj=copy.deepcopy(base);obj[key]=value
    mutations.append((key,json.dumps(obj)))
obj=copy.deepcopy(base);obj['checks'].pop();mutations.append(('removed_control',json.dumps(obj)))
mutations.append(('duplicate_schema',json.dumps(base)[:-1]+',"schema":"duplicate"}'))
mode='optimized' if not __debug__ else 'normal'
rows=[]
with tempfile.TemporaryDirectory() as temp:
    for name,text in mutations:
        f=Path(temp)/(name+'.json');f.write_text(text)
        cmd=[sys.executable]+(['-O'] if not __debug__ else [])+[str(P/'checks.py'),'--compare',str(f)]
        out=subprocess.run(cmd,text=True,capture_output=True,timeout=25)
        if out.returncode!=2 or 'REJECTED' not in out.stdout:
            raise RuntimeError('corruption was not refused: '+name+' '+out.stdout+out.stderr)
        rows.append({'mutation':name,'rejected':True})
result={'schema':'riemann.astra.jgc26.rejections.v1','mode':mode,
        'count':len(rows),'mutations':rows,'analytic_proofs_checked':False}
print(json.dumps(result,sort_keys=True,indent=2))
