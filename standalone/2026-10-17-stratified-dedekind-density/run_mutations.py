#!/usr/bin/env python3
"""Actually run four corrupted optimized checkers; no source files are changed."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
reports=[]
for name in ['wrong-stratum-count','omit-good-class','wrong-principal-shift','use_closed_endpoint']:
    proc=subprocess.run([sys.executable,'-O',str(ROOT/'verify.py'),'--mutation',name],
                        capture_output=True,text=True,timeout=20)
    last=proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else ''
    if proc.returncode==0 or not last.startswith('ArithmeticError:'):
        raise RuntimeError(f'failed negative control: {name}: {last}')
    reports.append({'mutation':name,'returncode':proc.returncode,'error':last})
print(json.dumps({'status':'PASS: four executed corrupted optimized processes rejected',
                  'reports':reports},indent=2,sort_keys=True))
