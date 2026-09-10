#!/usr/bin/env python3
"""Actual CLI refusal tests for this packet; standard library only."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def bad_result(root, key, value):
    p=root/'result.json'; d=json.loads(p.read_text()); d[key]=value
    p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')

def cases():
    return [
        ('rh_upgrade', lambda r: bad_result(r,'rh_proved',True), 'result differs'),
        ('actual_sign_upgrade', lambda r: bad_result(r,'actual_window_certified',True), 'result differs'),
        ('boolean_integer_alias', lambda r: bad_result(r,'rh_proved',0), 'result differs'),
        ('changed_count', lambda r: bad_result(r,'checks',0), 'result differs'),
        ('empty_scope', lambda r: (r/'result.json').write_text('{}\n'), 'result differs'),
        ('floating_alias', lambda r: bad_result(r,'checks',618.0), 'non-integer JSON number'),
        ('duplicate_key', lambda r: (r/'result.json').write_text('{"checks":618,"checks":618}'), 'duplicate JSON key'),
        ('proof_changed', lambda r: (r/'PROOF.md').write_text((r/'PROOF.md').read_text()+'\nchanged\n'), 'proof anchor mismatch'),
        ('source_changed', lambda r: (r/'SOURCE_LOCK.json').write_text('{}\n'), 'source anchor mismatch'),
        ('unlisted_file', lambda r: (r/'UNLISTED.txt').write_text('not in manifest\n'), 'manifest coverage'),
        ('missing_manifest_row', lambda r: (r/'SHA256SUMS').write_text('\n'.join((r/'SHA256SUMS').read_text().splitlines()[1:])+'\n'), 'manifest coverage'),
        ('duplicate_manifest_row', lambda r: (r/'SHA256SUMS').write_text((r/'SHA256SUMS').read_text()+(r/'SHA256SUMS').read_text().splitlines()[0]+'\n'), 'manifest schema'),
    ]

def main():
    outcomes=[]
    for opt in [False,True]:
        for name,mutate,needle in cases():
            with tempfile.TemporaryDirectory(prefix='logcore-refusal-') as tmp:
                dest=Path(tmp)/'packet'; shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('__pycache__'))
                mutate(dest)
                cmd=[sys.executable,'-I','-S']+(['-O'] if opt else [])+[str(dest/'verify.py'),'--check',str(dest/'result.json')]
                got=subprocess.run(cmd,text=True,capture_output=True,timeout=20)
                if got.returncode!=2 or needle not in got.stderr:
                    raise RuntimeError((name,opt,got.returncode,got.stdout,got.stderr))
                outcomes.append({'case':name,'optimized':opt,'exit':got.returncode,'reason':needle})
    result={'schema':'riemann.logarithmic_core.refusals.v1','cases_per_mode':len(cases()),
            'outcomes':outcomes,'status':'PASS_EXPECTED_REFUSALS'}
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if len(sys.argv)==3 and sys.argv[1]=='--write':
        Path(sys.argv[2]).write_text(text)
    elif (ROOT/'refusals.json').read_text()!=text:
        raise RuntimeError('retained refusal results differ')
    print(json.dumps({'status':result['status'],'executions':len(outcomes)},sort_keys=True))

if __name__=='__main__': main()
