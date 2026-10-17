#!/usr/bin/env python3
"""Run actual corrupted checker copies in separate optimized subprocesses."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile

root=Path(__file__).resolve().parent
source=(root/'verify.py').read_text()
changes=[
 ('erased_nonunit_zero','KEEP_NONUNIT_ZERO = True','KEEP_NONUNIT_ZERO = False'),
 ('omitted_j5_boundary','KEEP_J5_BOUNDARY = True','KEEP_J5_BOUNDARY = False'),
 ('decoupled_valuation_support','KEEP_VALUATION_SUPPORT = True','KEEP_VALUATION_SUPPORT = False'),
 ('erased_ramified_unit_phase','KEEP_RAMIFIED_UNIT_PHASE = True','KEEP_RAMIFIED_UNIT_PHASE = False'),
 ('old_B_exponent','USE_SHIFTED_B = True','USE_SHIFTED_B = False'),
 ('old_mollifier_weight','USE_SHIFTED_MOLLIFIER = True','USE_SHIFTED_MOLLIFIER = False'),
 ('omitted_dual_conductor','KEEP_DUAL_CONDUCTOR = True','KEEP_DUAL_CONDUCTOR = False'),
 ('wrong_count_exponent','COUNT_POWER = Q(1, 4)','COUNT_POWER = Q(1, 2)'),
]
out=[]
for name,old,new in changes:
    if source.count(old)!=1: raise ValueError('ambiguous mutation '+name)
    with tempfile.TemporaryDirectory(prefix='ramified-negative-') as tmp:
        p=Path(tmp)/'verify.py'
        p.write_text(source.replace(old,new))
        run=subprocess.run([sys.executable,'-O',str(p)],text=True,capture_output=True,timeout=25)
        if run.returncode == 0 or not run.stderr.startswith('FAIL: '):
            raise ValueError('mutation not rejected as intended: '+name+' '+run.stderr)
        out.append({'mutation':name,'returncode':run.returncode,'stderr':run.stderr.strip()})
print(json.dumps({'status':'PASS: eight separate corrupted optimized processes rejected','cases':out},indent=2,sort_keys=True))
