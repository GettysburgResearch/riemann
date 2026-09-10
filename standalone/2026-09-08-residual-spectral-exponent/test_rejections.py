#!/usr/bin/env python3
"""Actual subprocess refusal tests; no background work or repository writes."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent/'2026-09-08-residual-normalization-and-minima'/'PROOF.md'

def seal(root):
    names=sorted(p.name for p in root.iterdir() if p.is_file() and p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--optimized',action='store_true'); args=ap.parse_args()
    cases=['false_rh','false_edge','boolean_count','float_count','changed_parent_ref',
           'duplicate_json','changed_proof','extra_file','changed_parent_bytes','missing_manifest']
    done=[]
    for case in ['pristine']+cases:
        with tempfile.TemporaryDirectory(prefix='residual-rg-') as td:
            base=Path(td); root=base/ROOT.name; shutil.copytree(ROOT,root)
            parent=base/PARENT.parent.name; parent.mkdir(); shutil.copyfile(PARENT,parent/'PROOF.md')
            path=root/'result.json'; data=json.loads(path.read_text())
            if case=='false_rh': data['rh_proved']=True
            elif case=='false_edge': data['zero_edge_evaluated']=True
            elif case=='boolean_count': data['total_bounded_checks']=True
            elif case=='float_count': data['total_bounded_checks']=float(data['total_bounded_checks'])
            elif case=='changed_parent_ref': data['parent_commit']='0'*40
            if case in cases[:5]: path.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n'); seal(root)
            elif case=='duplicate_json':
                s=path.read_text(); path.write_text(s.replace('{','{"rh_proved": false,',1)); seal(root)
            elif case=='changed_proof': (root/'PROOF.md').write_text('altered proof\n')
            elif case=='extra_file': (root/'unlisted.txt').write_text('extra\n'); seal(root)
            elif case=='changed_parent_bytes': (parent/'PROOF.md').write_text('altered parent\n')
            elif case=='missing_manifest': (root/'SHA256SUMS').unlink()
            cmd=[sys.executable,'-I','-S','-B']+(['-O'] if args.optimized else [])
            cmd += [str(root/'verify.py'),'--check','result.json']
            run=subprocess.run(cmd,capture_output=True,text=True,timeout=35)
            good=(run.returncode==0) if case=='pristine' else (run.returncode!=0 and 'REFUSE:' in run.stderr)
            if not good: raise RuntimeError(case+': '+run.stdout[-300:]+run.stderr[-300:])
            done.append({'case':case,'returncode':run.returncode})
    print(json.dumps({'optimized_target':args.optimized,'pristine':1,'refusals':len(cases),'cases':done},sort_keys=True,indent=2))
if __name__=='__main__': main()
