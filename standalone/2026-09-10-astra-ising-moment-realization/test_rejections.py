#!/usr/bin/env python3
"""Run pristine acceptance, then actual changed-copy CLI refusals."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
FLAGS=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])

def seal(dst):
    files=sorted(p for p in dst.iterdir() if p.name!='SHA256SUMS')
    (dst/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))

def run(dst):
    return subprocess.run([sys.executable,*FLAGS,str(dst/'check.py'),'--check',str(dst/'result.json')],capture_output=True,text=True,timeout=45)

def main():
    labels=['moment-endpoint','false-closure','coverage','spin-multiplicity','float-alias',
            'boolean-alias','duplicate-json','resealed-density','unsealed-proof','extra-file','symlink-proof']
    with tempfile.TemporaryDirectory() as tmp:
        tmp=Path(tmp)
        pristine=tmp/'pristine';shutil.copytree(ROOT,pristine)
        control=run(pristine)
        if control.returncode:raise RuntimeError('pristine acceptance failed: '+control.stderr)
        for case in labels:
            dst=tmp/case;shutil.copytree(ROOT,dst)
            p=dst/'result.json';obj=json.loads(p.read_text())
            if case=='moment-endpoint':obj['moments']['8'][0]+=1
            elif case=='false-closure':obj['all_order_realization_proved']=True
            elif case=='coverage':obj['coverage']['cells']=83
            elif case=='spin-multiplicity':obj['seed']['multiplicities'][0]=24
            elif case=='float-alias':obj['bits']=256.0
            elif case=='boolean-alias':obj['bits']=True
            if case in labels[:6]:
                p.write_text(json.dumps(obj));seal(dst)
            elif case=='duplicate-json':
                p.write_text('{"bits":256,'+p.read_text().lstrip()[1:]);seal(dst)
            elif case=='resealed-density':
                c=dst/'check.py';text=c.read_text()
                old='pref=[4*q*q*x-6*q*y';new='pref=[5*q*q*x-6*q*y'
                if text.count(old)!=1:raise RuntimeError('density mutation did not hit once')
                c.write_text(text.replace(old,new));seal(dst)
            elif case=='unsealed-proof':
                with (dst/'PROOF.md').open('a') as f:f.write('\nchanged\n')
            elif case=='extra-file':(dst/'extra.txt').write_text('unlisted')
            elif case=='symlink-proof':
                proof=dst/'PROOF.md';proof.unlink();proof.symlink_to(ROOT/'PROOF.md')
            result=run(dst)
            if result.returncode==0:raise RuntimeError('accepted corruption: '+case)
            if 'REJECT:' not in result.stderr:raise RuntimeError('unexpected failure: '+case+result.stderr)
            print('rejected '+case)
    print('PASS pristine + '+str(len(labels))+' CLI refusals')

if __name__=='__main__':main()
