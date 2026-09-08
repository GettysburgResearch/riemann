#!/usr/bin/env python3
"""Explicit corrupt-result/source tests. No mathematical acceptance is inferred."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent

def main():
    records=[]
    for optimized in (False,True):
        for case in ('rh_flag','float_alias','count','duplicate_key','proof','source_lock'):
            with tempfile.TemporaryDirectory() as name:
                work=Path(name)
                for filename in ('verify.py','PROOF.md','SOURCE_LOCK.json','result.json'):
                    shutil.copy2(HERE/filename,work/filename)
                data=json.loads((work/'result.json').read_text())
                if case=='rh_flag': data['rh_proved']=True
                if case=='float_alias': data['finite_fixtures']=float(data['finite_fixtures'])
                if case=='count': data['finite_fixtures']+=1
                if case in ('rh_flag','float_alias','count'):
                    (work/'result.json').write_text(json.dumps(data))
                if case=='duplicate_key':
                    text=(work/'result.json').read_text()
                    (work/'result.json').write_text(text.replace('{','{"rh_proved": false,',1))
                if case=='proof':
                    with (work/'PROOF.md').open('a') as f: f.write('\nchanged proof\n')
                if case=='source_lock':
                    with (work/'SOURCE_LOCK.json').open('a') as f: f.write('\n ')
                cmd=[sys.executable]+(['-O'] if optimized else [])+[
                    str(work/'verify.py'),'--check',str(work/'result.json')]
                run=subprocess.run(cmd,capture_output=True,text=True,timeout=20)
                diagnostic='duplicate JSON key' if case=='duplicate_key' else 'saved result mismatch'
                if run.returncode==0 or diagnostic not in run.stderr:
                    raise RuntimeError('intended rejection failed: '+case)
                records.append({'mode':'optimized' if optimized else 'normal',
                                'case':case,'rejected':True,'expected_diagnostic':diagnostic})
    print(json.dumps({'tests':records,'total':len(records)},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
