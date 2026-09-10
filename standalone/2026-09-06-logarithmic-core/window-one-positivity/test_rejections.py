#!/usr/bin/env python3
"""Actual CLI rejection cases; every case must fail with its intended reason."""
from pathlib import Path
import subprocess,sys,tempfile,json,copy
ROOT=Path(__file__).resolve().parent
base=json.loads((ROOT/'certificate.json').read_text())
cases=[]
def add(name,edit,error):
 d=copy.deepcopy(base);edit(d);cases.append((name,json.dumps(d),error))
add('mode-denominator',lambda d:d.update(finite_modes=2048.0),'mode denominator')
add('negative-weight',lambda d:d['weights'].__setitem__(0,'-1'),'positive atom range')
add('missing-frequency',lambda d:d['frequencies'].pop(),'witness dimension')
add('larger-window',lambda d:d.update(source_interval='2'),'fixed source interval')
add('false-zero-weights',lambda d:d.update(weights=['0']*20),'finite coefficient failed')
cases.append(('duplicate-json','{"schema":"x",'+json.dumps(base)[1:],'duplicate JSON key'))
receipts=[]
with tempfile.TemporaryDirectory() as tmp:
 for mode in ([['-O']] if '--optimized' in sys.argv else [[]]):
  for name,data,err in cases:
   f=Path(tmp)/'bad.json';f.write_text(data)
   p=subprocess.run([sys.executable,'-B',*mode,str(ROOT/'verify.py'),'--certificate',str(f)],capture_output=True,text=True,timeout=60)
   if p.returncode==0 or err not in p.stderr:raise RuntimeError(f'unexpected outcome {mode} {name}: {p.stderr}')
   receipts.append({'mode':'optimized' if mode else 'ordinary','case':name,'expected_reason':err,'exit_code':p.returncode})
print(json.dumps({'status':'PASS_CLI_REJECTIONS','cases':receipts,'total':len(receipts)},sort_keys=True,indent=2))
