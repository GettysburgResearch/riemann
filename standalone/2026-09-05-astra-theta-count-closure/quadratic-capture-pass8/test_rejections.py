#!/usr/bin/env python3
"""Deliberately corrupt local copies; require the expected checker rejection."""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def main() -> None:
    records=[]
    cases=['rh_flag','integer_float_alias','integer_bool_alias','duplicate_key',
           'wrong_witness','proof_change','source_lock_change']
    for optimized in [False,True]:
        for case in cases:
            with tempfile.TemporaryDirectory(prefix='astra-qc-reject-') as tmp:
                p=Path(tmp)
                for name in ['verify.py','PROOF.md','ENDPOINT_DEFECT.md','README.md','SOURCE_LOCK.json','result.json']:
                    shutil.copyfile(ROOT/name,p/name)
                raw=(p/'result.json').read_text(); data=json.loads(raw)
                expected='saved result mismatch'
                if case=='rh_flag': data['rh_proved']=True
                elif case=='integer_float_alias': data['distinct_controls']=float(data['distinct_controls'])
                elif case=='integer_bool_alias': data['groups']['source_strip_budget']=True
                elif case=='duplicate_key':
                    (p/'result.json').write_text('{"rh_proved":false,'+raw[1:])
                    expected='duplicate JSON key'
                elif case=='wrong_witness': data['synthetic_witnesses'][0]['quadratic_value']='2'
                elif case=='proof_change':
                    (p/'PROOF.md').write_text((p/'PROOF.md').read_text()+'\nchanged\n')
                    expected='source authentication failed'
                elif case=='source_lock_change':
                    data_lock=json.loads((p/'SOURCE_LOCK.json').read_text())
                    data_lock['base_commit']='0'*40
                    (p/'SOURCE_LOCK.json').write_text(json.dumps(data_lock))
                    expected='source authentication failed'
                if case not in ['duplicate_key','proof_change','source_lock_change']:
                    (p/'result.json').write_text(json.dumps(data))
                cmd=[sys.executable]+(['-O'] if optimized else [])+['verify.py','--check','result.json']
                run=subprocess.run(cmd,cwd=p,capture_output=True,text=True,timeout=30)
                if run.returncode==0 or expected not in run.stderr:
                    raise RuntimeError(f'wrong rejection: {optimized}, {case}, {run.stderr[-400:]}')
                records.append({'optimized':optimized,'case':case,'expected_error':expected,'rejected':True})
    print(json.dumps({'status':'PASS_EXPECTED_REJECTIONS','cases':len(records),'records':records},sort_keys=True,indent=2))

if __name__=='__main__': main()
