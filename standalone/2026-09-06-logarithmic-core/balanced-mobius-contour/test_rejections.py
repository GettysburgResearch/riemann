#!/usr/bin/env python3
"""Run actual CLI corruption checks in a temporary, isolated copy."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def reseal(path):
    lines=[]
    for file in sorted(path.iterdir()):
        if file.is_file() and file.name!='SHA256SUMS':
            lines.append(hashlib.sha256(file.read_bytes()).hexdigest()+'  '+file.name)
    (path/'SHA256SUMS').write_text('\n'.join(lines)+'\n')

def main():
    cases=['false_rh','false_count','boolean_count','duplicate_key','changed_proof',
           'changed_parent','extra_file','missing_checksum']
    answers=[]
    with tempfile.TemporaryDirectory(prefix='bmc-rejections-') as tmp:
        tmp=Path(tmp)
        def clone(name):
            home=tmp/name
            folder=home/'balanced-mobius-contour'
            shutil.copytree(ROOT,folder)
            p=home/'sparse-sign-bootstrap';p.mkdir()
            shutil.copy2(ROOT.parent/'sparse-sign-bootstrap'/'PROOF.md',p/'PROOF.md')
            return folder
        def run(folder):
            cmd=[sys.executable,'-I','-S','-B']
            if not __debug__:
                cmd+=['-O']
            cmd+=['verify.py','--check','result.json']
            return subprocess.run(cmd,cwd=folder,text=True,capture_output=True,timeout=35)
        clean=run(clone('clean'))
        if clean.returncode:
            raise RuntimeError('pristine copy failed: '+clean.stderr)
        for name in cases:
            p=clone(name)
            if name in ['false_rh','false_count','boolean_count']:
                result=json.loads((p/'result.json').read_text())
                key={'false_rh':'rh_proved','false_count':'native_count_power_saving_proved',
                     'boolean_count':'bounded_checks'}[name]
                result[key]=True
                (p/'result.json').write_text(json.dumps(result))
                reseal(p)
            elif name=='duplicate_key':
                text=(p/'result.json').read_text()
                (p/'result.json').write_text('{"rh_proved":false,'+text[1:]);reseal(p)
            elif name=='changed_proof':
                with (p/'PROOF.md').open('a') as f:f.write('\nchanged\n')
            elif name=='changed_parent':
                (p.parent/'sparse-sign-bootstrap'/'PROOF.md').write_text('not the parent')
            elif name=='extra_file':
                (p/'unlisted.txt').write_text('extra')
            elif name=='missing_checksum':
                lines=(p/'SHA256SUMS').read_text().splitlines()
                (p/'SHA256SUMS').write_text('\n'.join(lines[1:])+'\n')
            outcome=run(p)
            expected={'false_rh':'reconstruction mismatch','false_count':'reconstruction mismatch',
                      'boolean_count':'reconstruction mismatch','duplicate_key':'duplicate JSON key',
                      'changed_proof':'digest mismatch','changed_parent':'parent source mismatch',
                      'extra_file':'packet inventory','missing_checksum':'manifest coverage'}[name]
            if outcome.returncode!=1 or expected not in outcome.stderr:
                raise RuntimeError(name+' did not fail as expected: '+outcome.stderr)
            answers.append({'case':name,'returncode':outcome.returncode,'reason':expected})
    print(json.dumps({'optimized':not __debug__,'pristine_copy_passed':True,
                      'rejected':answers},sort_keys=True))

if __name__=='__main__':main()
