#!/usr/bin/env python3
"""Changed-copy CLI tests, including one primitive mutation after resealing."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
FLAGS=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])

def seal(root):
    files=sorted(p for p in root.iterdir() if p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))

def run(root):
    return subprocess.run([sys.executable,*FLAGS,str(root/'check.py'),'--check',str(root/'result.json')],capture_output=True,text=True,timeout=35)

def main():
    cases=['wrong_result','false_status','boolean_alias','float_alias','duplicate_key','primitive_rate','changed_proof','extra_file']
    for name in ['pristine']+cases:
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'packet'; shutil.copytree(ROOT,root)
            p=root/'result.json'; data=json.loads(p.read_text())
            if name=='wrong_result': data['records']['target_squared_norms_D1_to_D12'][0]='1/1'
            if name=='false_status': data['status']='RH proved'
            if name=='boolean_alias': data['counts']['gamma_moment_cases']=True
            if name=='float_alias': data['counts']['gamma_moment_cases']=12.0
            if name in ['wrong_result','false_status','boolean_alias','float_alias']:
                p.write_text(json.dumps(data)); seal(root)
            if name=='duplicate_key':
                p.write_text(p.read_text().replace('{','{"schema":"bad",',1)); seal(root)
            if name=='primitive_rate':
                q=root/'check.py'; text=q.read_text(); old='(F(1,2)-D)**j'
                if old not in text: raise RuntimeError('missing mutation target')
                q.write_text(text.replace(old,'(F(1,3)-D)**j',1)); seal(root)
            if name=='changed_proof':
                q=root/'PROOF.md'; q.write_text(q.read_text()+'\nchanged\n')
            if name=='extra_file': (root/'EXTRA').write_text('not in inventory')
            r=run(root)
            if name=='pristine':
                if r.returncode!=0: raise RuntimeError('pristine failed: '+r.stderr)
            elif r.returncode==0: raise RuntimeError('accepted '+name)
    print(json.dumps({'pristine':1,'refusals':len(cases),'cases':cases},sort_keys=True))

if __name__=='__main__': main()
