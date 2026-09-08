#!/usr/bin/env python3
"""Eight bounded malformed-result/delivery tests in this interpreter's mode."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
PREFIX=[sys.executable,'-B']+(['-O'] if sys.flags.optimize else [])

def run(cmd):
    return subprocess.run(PREFIX+cmd,text=True,capture_output=True,timeout=20)

def main():
    records=[]
    with tempfile.TemporaryDirectory() as tmp:
        d=Path(tmp)
        base=json.loads((ROOT/'result.json').read_text())
        mutations=[('rh_flag','rh_proved',True),('numeric_alias','bits',160.0),
                   ('lost_samples','sample_count',0),('wrong_source','C0_interval',['0','0'])]
        for label,key,value in mutations:
            b=dict(base); b[key]=value
            p=d/(label+'.json'); p.write_text(json.dumps(b))
            r=run([str(ROOT/'verify.py'),'--check',str(p)])
            if r.returncode==0 or 'stored result mismatch' not in r.stderr:
                raise ValueError('unexpected negative-control outcome: '+label)
            records.append(label)
        p=d/'duplicate.json'
        p.write_text('{"rh_proved":false,"rh_proved":false}')
        r=run([str(ROOT/'verify.py'),'--check',str(p)])
        if r.returncode==0 or 'duplicate JSON key' not in r.stderr: raise ValueError('duplicate JSON accepted')
        records.append('duplicate_json')
        for label in ['changed_proof','missing_source','extra_file']:
            dest=d/label; shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('__pycache__'))
            if label=='changed_proof':
                p=dest/'PROOF.md'; p.write_text(p.read_text()+'\nChanged.\n')
            elif label=='missing_source': (dest/'SOURCE_LOCK.json').unlink()
            else: (dest/'unlisted.txt').write_text('unlisted')
            r=run([str(dest/'validate.py')])
            expected='hash mismatch' if label=='changed_proof' else 'unexpected or missing delivery path'
            if r.returncode==0 or expected not in r.stderr: raise ValueError('delivery mutant accepted: '+label)
            records.append(label)
    print(json.dumps({'status':'PASS_EXPECTED_REFUSALS','cases':records,'count':len(records),
                      'optimized':bool(sys.flags.optimize)},sort_keys=True))

if __name__=='__main__':main()
