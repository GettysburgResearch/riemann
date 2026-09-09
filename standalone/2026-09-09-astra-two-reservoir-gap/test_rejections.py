#!/usr/bin/env python3
"""Exercise the actual accepting CLI. Resealed mutations test reconstruction."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent


def seal(d):
    lines=[]
    for p in sorted(d.iterdir()):
        if p.name!='SHA256SUMS':
            lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name)
    (d/'SHA256SUMS').write_text('\n'.join(lines)+'\n')


def mutate(d,name):
    r=d/'result.json'
    if name in ('false_rh','changed_gap','boolean_integer'):
        obj=json.loads(r.read_text())
        if name=='false_rh': obj['rh_proved']=True
        elif name=='changed_gap': obj['actual_gap_certificates'][0]['gap_interval'][0]='0'
        else: obj['groups']['coincident_root_cases']=True
        r.write_text(json.dumps(obj));seal(d)
    elif name=='duplicate_json':
        r.write_text(r.read_text().replace('"rh_proved": false','"rh_proved": false, "rh_proved": false'))
        seal(d)
    elif name=='float_alias':
        r.write_text(r.read_text().replace('"dyadic_bits": 160','"dyadic_bits": 160.0'))
        seal(d)
    elif name=='wrong_shared_mass':
        p=d/'verify.py';s=p.read_text()
        old='return za + zb - 1 - z *'
        if old not in s: raise ValueError('mutation target absent')
        p.write_text(s.replace(old,'return za + zb - 2 - z *'))
        seal(d)
    elif name=='extra_resealed':
        (d/'EXTRA').write_text('unlisted');seal(d)
    elif name=='changed_proof':
        (d/'PROOF.md').write_text((d/'PROOF.md').read_text()+'\nchanged\n')
    elif name=='symlink_core':
        p=d/'verify.py';raw=p.read_bytes();p.unlink()
        q=d.parent/'external.py';q.write_bytes(raw);p.symlink_to(q)
    else: raise ValueError(name)


def main():
    p=argparse.ArgumentParser();p.add_argument('--optimized',action='store_true')
    p.add_argument('--part',type=int,choices=[1,2],default=1);args=p.parse_args()
    cases=(['false_rh','changed_gap','boolean_integer','duplicate_json','float_alias']
           if args.part==1 else ['wrong_shared_mass','extra_resealed','changed_proof','symlink_core'])
    out=[]
    for case in ['pristine']+cases:
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp)/'packet';shutil.copytree(HERE,d)
            if case!='pristine': mutate(d,case)
            cmd=[sys.executable,'-I','-S','-B']+(['-O'] if args.optimized else [])
            cmd +=[str(d/'verify.py'),'--check',str(d/'result.json')]
            run=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
            expected=(run.returncode==0) if case=='pristine' else (run.returncode!=0)
            if not expected: raise ValueError('unexpected acceptance boundary: '+case+'\n'+run.stderr)
            out.append({'case':case,'passed_boundary':True})
    print(json.dumps({'part':args.part,'cases':out},sort_keys=True,indent=2))


if __name__=='__main__':main()
