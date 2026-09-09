#!/usr/bin/env python3
"""Actual subprocess refusal checks for the new packet only."""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import hashlib

HERE=Path(__file__).resolve().parent
PARENTS=['euler-tail-stability','annular-scalar-route']

def reseal(root):
    files=sorted(p for p in root.iterdir() if p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))

def main():
    cases=['false-rh','false-count-bound','boolean-alias','duplicate-result-key',
           'wrong-parent-pin','changed-proof','changed-parent','extra-file']
    receipts=[]
    for case in cases:
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);root=base/HERE.name
            shutil.copytree(HERE,root)
            for name in PARENTS:
                (base/name).mkdir()
                shutil.copyfile(HERE.parent/name/'PROOF.md',base/name/'PROOF.md')
            p=root/'result.json';d=json.loads(p.read_text())
            if case=='false-rh':d['rh_proved']=True;p.write_text(json.dumps(d));reseal(root)
            elif case=='false-count-bound':d['failure_count_upper_bound_proved']=True;p.write_text(json.dumps(d));reseal(root)
            elif case=='boolean-alias':d['rh_proved']=0;p.write_text(json.dumps(d));reseal(root)
            elif case=='duplicate-result-key':p.write_text('{"rh_proved":false,"rh_proved":false}');reseal(root)
            elif case=='wrong-parent-pin':
                s=root/'SOURCES.json';v=json.loads(s.read_text());v['publication_parent']='0'*40;s.write_text(json.dumps(v));reseal(root)
            elif case=='changed-proof':
                with (root/'PROOF.md').open('a') as f:f.write('\nchanged\n')
            elif case=='changed-parent':
                with (base/PARENTS[0]/'PROOF.md').open('a') as f:f.write('\nchanged\n')
            else:(root/'extra.txt').write_text('unexpected')
            cmd=[sys.executable,'-I','-S','-B']
            if sys.flags.optimize:cmd.append('-O')
            cmd +=[str(root/'verify.py'),'--check',str(p)]
            run=subprocess.run(cmd,capture_output=True,text=True,timeout=40)
            if run.returncode==0 or 'REJECT:' not in run.stderr:
                raise RuntimeError('bad refusal: '+case+' '+run.stderr[-400:])
            receipts.append({'case':case,'exit_code':run.returncode,'reason':run.stderr.strip()})
    print(json.dumps({'schema':'riemann.prime-curvature.refusals.v1','optimized':bool(sys.flags.optimize),
                      'cases':receipts},indent=2))
if __name__=='__main__':main()
