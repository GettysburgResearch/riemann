#!/usr/bin/env python3
"""Execute checker rejection controls in separate processes; no analytic claim."""
from __future__ import annotations
import json, subprocess, sys, tempfile, shutil
from pathlib import Path

ROOT=Path(__file__).parent
MODE=['-O'] if sys.flags.optimize else []

def call(args, good):
    p=subprocess.run([sys.executable,*MODE,'-B',*map(str,args)],capture_output=True,text=True,timeout=15)
    if (p.returncode==0)!=good:
        raise RuntimeError('unexpected subprocess result: '+p.stdout+p.stderr)


def main():
    with tempfile.TemporaryDirectory() as td:
        t=Path(td)
        call([ROOT/'checks.py','--verify',ROOT/'checks.normal.json'],True)
        base=json.loads((ROOT/'checks.normal.json').read_text())
        variants=[]
        o=json.loads(json.dumps(base));o['rh_proved']=True;variants.append(json.dumps(o))
        o=json.loads(json.dumps(base));o['total_cases']=float(o['total_cases']);variants.append(json.dumps(o))
        o=json.loads(json.dumps(base));o['records']['actual_first_prime_X2']['I']='1/8';variants.append(json.dumps(o))
        variants.append((ROOT/'checks.normal.json').read_text().replace('{','{"rh_proved":true,',1))
        for i,s in enumerate(variants):
            p=t/f'bad{i}.json';p.write_text(s)
            call([ROOT/'checks.py','--verify',p],False)
        pristine=t/'pristine';shutil.copytree(ROOT,pristine)
        call([pristine/'validate.py'],True)
        for i in range(3):
            p=t/f'packet{i}';shutil.copytree(ROOT,p)
            if i==0: (p/'PROOF.md').write_text((p/'PROOF.md').read_text()+'\nchanged\n')
            elif i==1: (p/'CLAIMS.tsv').unlink()
            else: (p/'unexpected.txt').write_text('untracked addition')
            call([p/'validate.py'],False)
    print(json.dumps({'status':'PASS_REJECTIONS','result_refusals':4,'package_refusals':3,
                      'pristine_controls':2,'analytic_proofs_verified':False},sort_keys=True))

if __name__=='__main__':main()
