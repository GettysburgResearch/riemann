#!/usr/bin/env python3
"""Run bounded corruption refusals in both Python modes; no network or repo writes."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',type=Path,required=True)
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    script=(root/'checks.py').read_bytes()
    original=(root/'checks.normal.json').read_text()
    expected=json.loads(original)
    cases=[]
    for label,key,value in [
        ('changed_named_count','named_checks',expected['named_checks']+1),
        ('float_alias','fixture_count',float(expected['fixture_count'])),
        ('boolean_alias','rh_proved',0),
        ('false_RH_flag','rh_proved',True),
    ]:
        obj=copy.deepcopy(expected);obj[key]=value
        cases.append((label,json.dumps(obj),script))
    cases.append(('duplicate_JSON_key','{"rh_proved":false,'+original.lstrip()[1:],script))
    cases.append(('changed_checker_bytes',original,script+b'\n# deliberate corruption control\n'))
    rows=[]
    with tempfile.TemporaryDirectory(prefix='reviewerD-refusals-') as directory:
        temp=Path(directory);checker=temp/'checks.py';result=temp/'candidate.json'
        for optimized in [False,True]:
            for label,text,code in cases:
                checker.write_bytes(code);result.write_text(text)
                cmd=[sys.executable]+(['-O'] if optimized else [])+[str(checker),'--check',str(result)]
                run=subprocess.run(cmd,text=True,capture_output=True,timeout=40)
                if run.returncode!=2 or 'REJECT:' not in run.stderr:
                    raise RuntimeError(f'corruption not rejected: {label}, optimized={optimized}, {run.returncode}')
                rows.append({'case':label,'optimized':optimized,'returncode':run.returncode,
                             'stderr':run.stderr.strip()})
    payload={'schema':'riemann.reviewerD.refusals.v1','count':len(rows),
             'checker_sha256':hashlib.sha256(script).hexdigest(),
             'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'all_expected_refusals':True,'rows':rows}
    args.write.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    print(f'PASS_REVIEWER_D_CORRUPTION_REFUSALS count={len(rows)}')


if __name__=='__main__':
    main()
