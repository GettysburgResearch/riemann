#!/usr/bin/env python3
"""Execute four actually corrupted optimized checkers in isolated directories."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
cases=[
 ('collapse_split_conjugates','return -2 if e == 1 else (1 if e == 2 else 0)',
  'return -1 if e == 1 else (1 if e == 2 else 0)'),
 ('erase_inert_mobius_sign','return -1 if e == 2 else 0',
  'return 1 if e == 2 else 0'),
 ('omit_split_shared_prime_branch','ds += [d*p for d in list(ds)]','ds += []'),
 ('omit_shared_factor_from_normalized_constant','return Fraction(-2*p*(p+1), den)',
  'return Fraction(-2*p*p, den)'),
]
results=[]
for name,old,new in cases:
    with tempfile.TemporaryDirectory(prefix='norm-cov-mutation-') as tmp:
        dest=Path(tmp)
        for filename in ['arithmetic.py','intervals.py','verify.py']:
            shutil.copy2(ROOT/filename,dest/filename)
        path=dest/'arithmetic.py'
        text=path.read_text()
        if text.count(old)!=1:
            raise RuntimeError(f'{name}: mutation anchor not unique')
        path.write_text(text.replace(old,new))
        proc=subprocess.run([sys.executable,'-O',str(dest/'verify.py'),'--quick'],
                            capture_output=True,text=True,timeout=30)
        last=proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else ''
        if proc.returncode==0 or 'ArithmeticError:' not in last:
            raise RuntimeError(f'{name}: corrupted checker not rejected as intended: {last}')
        results.append({'name':name,'returncode':proc.returncode,'last_error':last})
print(json.dumps({'status':'PASS','actually_executed_mutations':results},sort_keys=True,indent=2))
