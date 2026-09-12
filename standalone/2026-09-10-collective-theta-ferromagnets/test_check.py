#!/usr/bin/env python3
"""Changed-copy CLI tests. Resealed producer errors must fail finite reconstruction."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def seal(root):
    lines = []
    for p in sorted(root.iterdir()):
        if p.name != 'SHA256SUMS':
            lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name)
    (root/'SHA256SUMS').write_text('\n'.join(lines)+'\n')


def change_result(root, key, value):
    p = root/'result.json'
    data = json.loads(p.read_text())
    data[key] = value
    p.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
    seal(root)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--optimized', action='store_true')
    ap.add_argument('--part', type=int, choices=(1,2), required=True)
    args = ap.parse_args()
    cases = ['false-rh', 'false-order', 'boolean-alias', 'duplicate-json'] if args.part==1 else [
        'cluster-producer', 'edge-producer', 'source-drift', 'unsealed-proof']
    outputs = []
    with tempfile.TemporaryDirectory() as folder:
        base = Path(folder)
        for name in ['pristine']+cases:
            dst = base/name
            shutil.copytree(ROOT, dst)
            if name=='false-rh':
                change_result(dst,'rh_proved',True)
            elif name=='false-order':
                change_result(dst,'all_order_realization_proved',True)
            elif name=='boolean-alias':
                change_result(dst,'schema',True)
            elif name=='duplicate-json':
                p=dst/'result.json'
                p.write_text(p.read_text().replace('{','{"schema":1,',1))
                seal(dst)
            elif name in ('cluster-producer','edge-producer'):
                p=dst/'check.py'; text=p.read_text()
                if name=='cluster-producer':
                    old='cluster_factor = 2 ** len(amplitude)'
                    new='cluster_factor = 1'
                else:
                    old='full.append((min(a, b), max(a, b), r))'
                    new='full.append((min(a, b), max(a, b), wire))'
                if text.count(old)!=1:
                    raise RuntimeError('producer mutation target count')
                p.write_text(text.replace(old,new))
                seal(dst)
            elif name=='source-drift':
                p=dst/'SOURCES.json'; data=json.loads(p.read_text()); data['parent_commit']='0'*40
                p.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n'); seal(dst)
            elif name=='unsealed-proof':
                with (dst/'PROOF.md').open('a') as f:
                    f.write('\nAltered source control.\n')
            command=[sys.executable,'-I','-S','-B']
            if args.optimized: command.append('-O')
            command += [str(dst/'check.py'),'--check',str(dst/'result.json')]
            run=subprocess.run(command,capture_output=True,text=True,timeout=40)
            expected=0 if name=='pristine' else 1
            if run.returncode!=expected:
                raise RuntimeError(name+': unexpected return '+str(run.returncode)+' '+run.stderr)
            if name!='pristine' and 'REJECT:' not in run.stderr:
                raise RuntimeError(name+': did not reject through checker')
            outputs.append({'case':name,'returncode':run.returncode,
                            'message':'PASS' if not run.stderr else run.stderr.strip()})
    print(json.dumps({'part':args.part,'optimized':args.optimized,'cases':outputs},indent=2))


if __name__=='__main__':
    main()
