#!/usr/bin/env python3
"""Small actual CLI rejection tests. No mathematical theorem is checked here."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def reseal(root):
    names=sorted(p.name for p in root.iterdir() if p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

cases=['false_count_proof','numeric_alias','duplicate_json','changed_proof','extra_file']
results={}
for case in cases:
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)/'packet'
        shutil.copytree(ROOT,root)
        rp=root/'result.json'
        data=json.loads(rp.read_text())
        if case=='false_count_proof':
            data['target_count_bound_proved']=True
            rp.write_text(json.dumps(data)); reseal(root)
        elif case=='numeric_alias':
            data['rh_proved']=0
            rp.write_text(json.dumps(data)); reseal(root)
        elif case=='duplicate_json':
            rp.write_text('{"rh_proved":false,"rh_proved":false}'); reseal(root)
        elif case=='changed_proof':
            with (root/'PROOF_ATTEMPT.md').open('a') as f: f.write('\nchanged\n')
        else:
            (root/'unexpected.txt').write_text('extra')
        cmd=[sys.executable,'-I','-S','-B']
        if sys.flags.optimize: cmd+=['-O']
        cmd += [str(root/'verify.py'),'--manifest','--check',str(rp)]
        run=subprocess.run(cmd,capture_output=True,text=True,timeout=40)
        if run.returncode==0:
            raise RuntimeError('corruption was accepted: '+case)
        intended={'false_count_proof':'saved result differs','numeric_alias':'saved result differs',
                  'duplicate_json':'duplicate JSON key','changed_proof':'manifest hash:',
                  'extra_file':'unexpected/missing packet entry'}[case]
        if intended not in run.stderr:
            raise RuntimeError('unexpected refusal: '+case+'\n'+run.stderr)
        results[case]='rejected: '+intended
print(json.dumps(results,sort_keys=True,indent=2))
