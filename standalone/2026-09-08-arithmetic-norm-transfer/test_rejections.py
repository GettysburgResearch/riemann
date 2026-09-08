#!/usr/bin/env python3
"""Actual subprocess refusals; no analytic result is inferred from them."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
NAMES=['rh','power','alias','profile','duplicate','proof','extra','parent','producer']


def reseal(p):
    files=sorted(x for x in p.iterdir() if x.is_file() and x.name!='SHA256SUMS')
    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256(x.read_bytes()).hexdigest()+'  '+x.name+'\n' for x in files))


def mutate(p,name):
    if name in {'rh','power','alias','profile'}:
        d=json.loads((p/'result.json').read_text())
        if name=='rh':d['rh_proved']=True
        if name=='power':d['fixed_power_saving_proved']=True
        if name=='alias':d['rh_proved']=0
        if name=='profile':d['profile_certificate']['outward_numerators'][1]-=100000
        (p/'result.json').write_text(json.dumps(d));reseal(p)
    elif name=='duplicate':
        t=(p/'result.json').read_text();(p/'result.json').write_text(t.replace('{','{"rh_proved":false,',1));reseal(p)
    elif name=='proof':
        with (p/'PROOF.md').open('a') as f:f.write('\nALTERED\n')
    elif name=='extra':
        (p/'UNREVIEWED.md').write_text('extra payload');reseal(p)
    elif name=='parent':
        d=json.loads((p/'SOURCES.json').read_text());d['publication_parent']='0'*40
        (p/'SOURCES.json').write_text(json.dumps(d));reseal(p)
    elif name=='producer':
        x=p/'verify.py';t=x.read_text();t=t.replace('D = (1, -5, 8, -4)','D = (1, -5, 8, -3)')
        x.write_text(t);reseal(p)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--part',type=int,choices=[1,2],required=True)
    ap.add_argument('--optimized',action='store_true');args=ap.parse_args()
    names=NAMES[:5] if args.part==1 else NAMES[5:]
    passed=[]
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        for name in ['pristine']+names:
            p=td/name;shutil.copytree(ROOT,p)
            if name!='pristine':mutate(p,name)
            cmd=[sys.executable,'-I','-S','-B']+(['-O'] if args.optimized else [])+[str(p/'verify.py'),'--check',str(p/'result.json')]
            run=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
            should_pass=name=='pristine'
            if (run.returncode==0)!=should_pass:
                raise RuntimeError(name+': unexpected status '+str(run.returncode)+' '+run.stderr[-500:])
            if not should_pass and 'REJECT:' not in run.stderr:raise RuntimeError('not a controlled refusal: '+name)
            passed.append(name)
    print(json.dumps({'part':args.part,'optimized':args.optimized,'cases':passed,'ok':True},sort_keys=True))


if __name__=='__main__':main()
