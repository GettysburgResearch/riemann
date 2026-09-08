#!/usr/bin/env python3
"""Run actual CLI refusals. No assert-based acceptance; no parent execution."""
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
FLAGS=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])


def command(path: Path, script: str, *args: str, good: bool) -> None:
    p=subprocess.run([sys.executable,*FLAGS,str(path/script),*args],
                     stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
    if (p.returncode==0)!=good:
        raise RuntimeError('unexpected CLI outcome: '+script+' '+p.stderr.decode()[-1500:])


def reseal(path: Path) -> None:
    names=sorted(p.name for p in path.iterdir() if p.is_file() and p.name!='SHA256SUMS')
    (path/'SHA256SUMS').write_text(''.join(hashlib.sha256((path/n).read_bytes()).hexdigest()
                                          +'  '+n+'\n' for n in names))


def main() -> None:
    original=json.loads((ROOT/'result.json').read_text())
    records=0;packets=0
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp)/'packet';shutil.copytree(ROOT,p)
        command(p,'validate.py',good=True)
        command(p,'check.py','--check',str(p/'result.json'),good=True)
        def change_result(mutator):
            nonlocal records
            d=copy.deepcopy(original);mutator(d)
            (p/'result.json').write_text(json.dumps(d));reseal(p)
            command(p,'check.py','--check',str(p/'result.json'),good=False)
            records+=1
        change_result(lambda d:d.update(rh_proved=True))
        change_result(lambda d:d['inverse_certificate'].update(inverse_upper='0/1'))
        change_result(lambda d:d['inverse_certificate']['rational_trial_numerators'].__setitem__(0,0))
        change_result(lambda d:d['tree'].update(finite_descendant_cases=True))
        change_result(lambda d:d['arithmetic'].update(divisor_identities=256.0))
        (p/'result.json').write_text('{"rh_proved":false,"rh_proved":true}');reseal(p)
        command(p,'check.py','--check',str(p/'result.json'),good=False);records+=1
        for mode in ('alter-proof','extra','missing','symlink'):
            shutil.rmtree(p);shutil.copytree(ROOT,p)
            if mode=='alter-proof':
                q=p/'PROOF.md';q.write_text(q.read_text()+'\nALTERED\n')
            elif mode=='extra':(p/'EXTRA').write_text('x');reseal(p)
            elif mode=='missing':(p/'CLAIMS.json').unlink()
            else:
                (p/'README.md').unlink();os.symlink(ROOT/'README.md',p/'README.md')
            command(p,'validate.py',good=False);packets+=1
    print(json.dumps({'altered_results_rejected':records,
                      'altered_packages_rejected':packets,
                      'pristine_cli_controls':2},sort_keys=True))

if __name__=='__main__':main()
