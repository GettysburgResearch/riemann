#!/usr/bin/env python3
"""Bounded CLI refusal tests. These test the checker, not the analytic proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def seal(root:Path)->None:
    files=sorted(p for p in root.iterdir() if p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))

def main(optimized:bool)->None:
    cases=['pristine','false_rh','wrong_cutoff','float_alias','duplicate_key','producer_weight','unsealed_proof']
    for case in cases:
        with tempfile.TemporaryDirectory(prefix='whole-xi-check-') as td:
            root=Path(td)/'packet'
            shutil.copytree(ROOT,root)
            p=root/'result.json'
            obj=json.loads(p.read_text())
            if case=='false_rh':
                obj['rh_proved']=True
                p.write_text(json.dumps(obj))
            elif case=='wrong_cutoff':
                obj['twist_certificate']['N']=255
                p.write_text(json.dumps(obj))
            elif case=='float_alias':
                p.write_text(p.read_text().replace('"N": 256','"N": 256.0'))
            elif case=='duplicate_key':
                p.write_text(p.read_text().replace('"rh_proved": false','"rh_proved": false, "rh_proved": false'))
            elif case=='producer_weight':
                q=root/'verify.py'
                text=q.read_text()
                old='r *= F(N-n+1, N+n)'
                if text.count(old)!=1:
                    raise RuntimeError('mutation target not unique')
                q.write_text(text.replace(old,'r *= F(N-n+1, N+n+1)'))
            elif case=='unsealed_proof':
                with (root/'PROOF.md').open('a') as f:
                    f.write('\nUnsealed mutation.\n')
            if case!='unsealed_proof':
                seal(root)
            cmd=[sys.executable,'-I','-S','-B']+(['-O'] if optimized else [])+[str(root/'verify.py'),'--check',str(p)]
            run=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
            expected_pass=case=='pristine'
            if (run.returncode==0)!=expected_pass:
                raise RuntimeError(f'{case}: unexpected exit {run.returncode}: {run.stderr[-1000:]}')
            print(case+': '+('PASS' if expected_pass else 'REFUSED'))
    print('All seven CLI cases completed; six refusals and one pristine replay.')

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--optimized',action='store_true')
    main(ap.parse_args().optimized)
