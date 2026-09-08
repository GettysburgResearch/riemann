#!/usr/bin/env python3
"""Run real checker CLIs against bounded result corruptions; do not alter originals."""
import json
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile

root=Path(__file__).resolve().parent
base=json.loads((root/'checks.normal.json').read_text())
records=[]
for optimized in (False,True):
    command=[sys.executable]+(['-O'] if optimized else [])+['-B',str(root/'checks.py')]
    control=subprocess.run(command+['--check',str(root/'checks.normal.json')],capture_output=True,timeout=45)
    if control.returncode:
        raise ValueError('pristine checker failed')
    payloads=[]
    for key,value in [('rh_proved',True),('total_cases',232),('total_cases',231.0),('extra',1)]:
        changed=dict(base);changed[key]=value
        payloads.append((key+':'+str(value),json.dumps(changed)))
    payloads.append(('duplicate_key','{"rh_proved": false, "rh_proved": false}'))
    changed=json.loads(json.dumps(base));changed['groups'][0]['rational_payload_sha256']='0'*64
    payloads.append(('changed_finite_norms',json.dumps(changed)))
    with tempfile.TemporaryDirectory() as td:
        for label,text in payloads:
            path=Path(td)/'bad.json';path.write_text(text)
            r=subprocess.run(command+['--check',str(path)],capture_output=True,timeout=45)
            if r.returncode==0:
                raise ValueError('corruption accepted: '+label)
            records.append({'optimized':optimized,'case':label,'rejected':True})
package_records=[]
for optimized in (False,True):
    with tempfile.TemporaryDirectory() as td:
        parent=Path(td)
        pristine=parent/'pristine'
        shutil.copytree(root,pristine)
        cmd=[sys.executable]+(['-O'] if optimized else [])+['-B']
        good=subprocess.run(cmd+[str(pristine/'validate.py')],capture_output=True,timeout=45)
        if good.returncode:
            raise ValueError('pristine packet validation failed')
        for name in ('changed_proof','missing_proof','extra_file','duplicate_manifest'):
            dest=parent/name;shutil.copytree(root,dest)
            if name=='changed_proof':
                p=dest/'PROOF.md';p.write_text(p.read_text()+'\nchanged\n')
            elif name=='missing_proof':
                (dest/'PROOF.md').unlink()
            elif name=='extra_file':
                (dest/'extra.txt').write_text('unexpected')
            else:
                p=dest/'SHA256SUMS';p.write_text(p.read_text()+p.read_text().splitlines()[0]+'\n')
            bad=subprocess.run(cmd+[str(dest/'validate.py')],capture_output=True,timeout=45)
            if bad.returncode==0:
                raise ValueError('package corruption accepted: '+name)
            package_records.append({'optimized':optimized,'case':name,'rejected':True})
print(json.dumps({'pristine_controls':4,'result_rejections':records,
                  'package_rejections':package_records},indent=2,sort_keys=True))
