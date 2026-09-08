#!/usr/bin/env python3
"""Actual CLI refusal checks. This script does not add mathematical coverage."""
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def seal(p):
    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.name+'\n' for f in sorted(p.iterdir()) if f.name!='SHA256SUMS' and f.is_file()))

def change_json(p,fn):
    f=p/'result.json';d=json.loads(f.read_text());fn(d);f.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');seal(p)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--optimized',action='store_true');args=ap.parse_args()
    cmd=[sys.executable,'-I','-S','-B']+(['-O'] if args.optimized else [])
    outcomes={}
    with tempfile.TemporaryDirectory() as td:
      base=Path(td)
      def run_case(name,mutate=None):
        p=base/name;shutil.copytree(ROOT,p)
        if mutate:mutate(p)
        cp=subprocess.run(cmd+[str(p/'verify.py'),'--check',str(p/'result.json')],capture_output=True,text=True,timeout=40)
        okay=cp.returncode==0 if mutate is None else cp.returncode!=0
        if not okay:raise RuntimeError('unexpected acceptance/refusal: '+name+'\n'+cp.stderr)
        outcomes[name]={'exit_code':cp.returncode,'expected':'accept' if mutate is None else 'reject'}
      run_case('pristine')
      run_case('false_rh',lambda p:change_json(p,lambda d:d.update(rh_proved=True)))
      run_case('false_global_bound',lambda p:change_json(p,lambda d:d.update(unbounded_energy_bound_proved=True)))
      run_case('boolean_alias',lambda p:change_json(p,lambda d:d.update(rh_proved=0)))
      run_case('float_precision',lambda p:change_json(p,lambda d:d.update(bits=192.0)))
      def duplicate(p):
        f=p/'result.json';s=f.read_text();f.write_text(s.replace('{','{"rh_proved":false,',1));seal(p)
      run_case('duplicate_json',duplicate)
      run_case('changed_proof',lambda p:(p/'PROOF.md').write_text((p/'PROOF.md').read_text()+'\nchanged\n'))
      run_case('missing_manifest',lambda p:(p/'SHA256SUMS').unlink())
      def extra(p):(p/'extra.txt').write_text('unexpected');seal(p)
      run_case('resealed_extra',extra)
      def false_energy(d):d['certificates'][0]['minimum_decimal']=['0','0']
      run_case('resealed_minimum',lambda p:change_json(p,false_energy))
      def candidate(p):
        f=p/'candidates.json';d=json.loads(f.read_text());d['cases'][0]['free']['3']='0';f.write_text(json.dumps(d));seal(p)
      run_case('resealed_candidate',candidate)
    print(json.dumps({'mode':'optimized' if args.optimized else 'ordinary','outcomes':outcomes},indent=2,sort_keys=True))

if __name__=='__main__':main()
