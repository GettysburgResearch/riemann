#!/usr/bin/env python3
"""Run real copied-package CLI controls. No assert-based acceptance."""
from pathlib import Path
import hashlib
import argparse
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:raise RuntimeError(message)

def seal(d):
    files=sorted(p for p in d.iterdir() if p.name!='SHA256SUMS')
    (d/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))

def run(d):
    cmd=[sys.executable,'-I','-S','-B']+(['-O'] if sys.flags.optimize else [])+['check.py','--check','result.json']
    return subprocess.run(cmd,cwd=d,capture_output=True,text=True,timeout=60)

def changed_result(d,key,value):
    p=d/'result.json';v=json.loads(p.read_text());v[key]=value
    p.write_text(json.dumps(v,sort_keys=True,separators=(',',':'))+'\n');seal(d)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--part",type=int,choices=(1,2),required=True)
    part=ap.parse_args().part
    names=[]; index=0
    with tempfile.TemporaryDirectory(prefix='icr26-tests-') as t:
        top=Path(t)
        pristine=top/'pristine';shutil.copytree(ROOT,pristine)
        r=run(pristine);require(r.returncode==0,'pristine failed: '+r.stderr[-1000:])
        def case(name,mutate):
            nonlocal index
            index+=1
            if (part==1 and index>4) or (part==2 and index<=4):return
            print("checking "+name,file=sys.stderr,flush=True)
            d=top/name;shutil.copytree(ROOT,d);mutate(d);r=run(d)
            require(r.returncode!=0,name+' unexpectedly accepted');names.append(name)
        case('false-rh',lambda d:changed_result(d,'rh_proved',True))
        case('wrong-energy',lambda d:changed_result(d,'standardized_unmatched16',[0,1]))
        case('boolean-alias',lambda d:changed_result(d,'positive_edges',True))
        def duplicate(d):
            p=d/'result.json';s=p.read_text().rstrip();p.write_text(s[:-1]+',"spins":272}\n');seal(d)
        case('duplicate-json',duplicate)
        def wrong_density(d):
            p=d/'check.py';s=p.read_text();require('pref=[4*q*q*x-6*q*y' in s,'mutation site')
            p.write_text(s.replace('pref=[4*q*q*x-6*q*y','pref=[5*q*q*x-6*q*y'));seal(d)
        case('wrong-theta-coefficient',wrong_density)
        def wrong_coupling(d):
            p=d/'parameters.json';v=json.loads(p.read_text());v['q']=[3,2]
            p.write_text(json.dumps(v));seal(d)
        case('negative-coupling',wrong_coupling)
        def changed_proof(d):
            p=d/'PROOF.md';p.write_text(p.read_text()+'\nUnsealed edit.\n')
        case('changed-proof',changed_proof)
        case('extra-file',lambda d:(d/'extra.txt').write_text('not in inventory'))
        def symlink(d):
            p=d/'PROOF.md';p.unlink();p.symlink_to(ROOT/'PROOF.md')
        case('symlink-proof',symlink)
    print(json.dumps({'pristine':1,'part':part,'refusals':names,'optimized':bool(sys.flags.optimize)},sort_keys=True))

if __name__=='__main__':main()
