#!/usr/bin/env python3
"""Corrupt copied packets; invoke the actual validator in both Python modes."""
from __future__ import annotations
import json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
results=[]
for mode in [[],['-O']]:
    for mutation in ['result_change','producer_change','missing_header','extra_file','predecessor_change']:
        with tempfile.TemporaryDirectory() as td:
            base=Path(td)/'reviews';shutil.copytree(ROOT.parent,base);p=base/'D-pass4'
            if mutation=='result_change':
                f=p/'p61.full.json';a=json.loads(f.read_text());a['finite_endpoint']=10;f.write_text(json.dumps(a))
            elif mutation=='producer_change':
                with (p/'p61_replay.cpp').open('a') as f:f.write('\n// changed\n')
            elif mutation=='missing_header':(p/'mpfr_abi.h').unlink()
            elif mutation=='extra_file':(p/'UNDECLARED').write_text('unlisted')
            else:
                with (base/'D'/'REPORT.md').open('a') as f:f.write('\nchanged\n')
            q=subprocess.run([sys.executable,*mode,str(p/'validate.py')],capture_output=True,text=True)
            if q.returncode!=2:raise RuntimeError(f'{mutation} was not rejected: {q.returncode} {q.stdout} {q.stderr}')
            results.append({'mode':'optimized' if mode else 'normal','mutation':mutation,'exit_code':q.returncode})
out={'schema':'reviewer-D.pass4.package-rejections.v1','status':'PASS','records':results}
text=json.dumps(out,sort_keys=True,indent=2)+'\n'
if '--output' in sys.argv:Path(sys.argv[sys.argv.index('--output')+1]).write_text(text)
else:print(text,end='')
