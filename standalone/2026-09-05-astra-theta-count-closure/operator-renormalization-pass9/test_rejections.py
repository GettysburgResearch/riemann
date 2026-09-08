#!/usr/bin/env python3
"""Run deliberate corruptions in disposable copies, preserving packet files."""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def main() -> None:
    cases=['rh_flag','numeric_alias','duplicate_key','wrong_margin','changed_proof','changed_lock']
    results=[]
    for case in cases:
        with tempfile.TemporaryDirectory() as tmp:
            work=Path(tmp)
            for name in ['verify.py','PROOF.md','SOURCE_LOCK.json','result.json']:
                shutil.copyfile(ROOT/name,work/name)
            saved=work/'result.json'
            data=json.loads(saved.read_text())
            if case=='rh_flag':
                data['claims']['rh_proved']=True
            elif case=='numeric_alias':
                data['finite_comparisons']=float(data['finite_comparisons'])
            elif case=='duplicate_key':
                saved.write_text(saved.read_text().replace('{','{"status":"DUPLICATE",',1))
            elif case=='wrong_margin':
                data['actual_X2_test_upper_bound']='13/3240'
            elif case=='changed_proof':
                with (work/'PROOF.md').open('a') as out: out.write('\ncorruption\n')
            elif case=='changed_lock':
                with (work/'SOURCE_LOCK.json').open('a') as out: out.write(' \n')
            if case in ['rh_flag','numeric_alias','wrong_margin']:
                saved.write_text(json.dumps(data))
            command=[sys.executable]+(['-O'] if sys.flags.optimize else [])
            command += ['verify.py','--check','result.json']
            proc=subprocess.run(command,cwd=work,text=True,capture_output=True,timeout=15)
            expected=('duplicate JSON key' if case=='duplicate_key' else
                      'source hash mismatch' if case in ['changed_proof','changed_lock'] else
                      'saved result mismatch')
            if proc.returncode==0 or expected not in proc.stderr:
                raise SystemExit('unexpected rejection behavior: '+case+' '+proc.stderr)
            results.append({'case':case,'expected_diagnostic':expected,'exit_code':proc.returncode})
    print(json.dumps({'status':'PASS_EXPECTED_REFUSALS','cases':results},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
