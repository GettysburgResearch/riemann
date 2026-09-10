#!/usr/bin/env python3
"""Exercise the actual byte validator on three mutated package copies."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parent
records=[]
for kind in ('changed_proof','missing_result','unexpected_file'):
    with tempfile.TemporaryDirectory() as td:
        dest=Path(td)/'packet'
        shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('__pycache__'))
        if kind=='changed_proof':
            p=dest/'CONSTRUCTION.md';p.write_text(p.read_text()+'\nUNBOUND MUTATION\n')
        elif kind=='missing_result':(dest/'checks.optimized.json').unlink()
        else:(dest/'unexpected.txt').write_text('not in declared inventory')
        p=subprocess.run([sys.executable,str(ROOT/'validate.py'),'--root',str(dest)],capture_output=True,text=True,timeout=10)
        if p.returncode!=2:raise RuntimeError((kind,p.stdout,p.stderr))
        records.append({'mutation':kind,'rejected':True})
print(json.dumps({'package_mutations':records},indent=2,sort_keys=True))
