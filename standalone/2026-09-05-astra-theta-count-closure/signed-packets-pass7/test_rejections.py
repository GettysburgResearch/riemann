#!/usr/bin/env python3
"""Exercise altered-record refusals; reruns are not new mathematical controls."""
from pathlib import Path
import copy
import json
import subprocess
import sys
import tempfile


def main():
    here=Path(__file__).resolve().parent
    exact=json.loads((here/'checks.json').read_text())
    low=json.loads((here/'low_zeros.json').read_text())
    cases=[]
    def encode(x):return json.dumps(x,indent=2,sort_keys=True)+'\n'
    x=copy.deepcopy(exact);x['rh_proved']=True
    cases.append(('rh_flag','verify.py',encode(x),'Saved exact record differs'))
    x=copy.deepcopy(exact);x['distinct_checks']=float(x['distinct_checks'])
    cases.append(('numeric_type_alias','verify.py',encode(x),'Saved exact record differs'))
    x=encode(exact).replace('{','{"rh_proved":false,',1)
    cases.append(('duplicate_key','verify.py',x,'Saved exact record differs'))
    x=copy.deepcopy(exact)
    rec=next(r for r in x['checks'] if r['name']=='reservoir_full_signed_seed_m5')
    rec['tail_ratio_bound']='1'
    cases.append(('saved_tail_margin','verify.py',encode(x),'Saved exact record differs'))
    x=copy.deepcopy(low);x['enclosures'][0]['sign']=-1
    cases.append(('endpoint_sign','verify_low_zeros.py',encode(x),'Saved endpoint record differs'))
    x=copy.deepcopy(low);x['tail_bound']='0'
    cases.append(('eta_tail','verify_low_zeros.py',encode(x),'Saved endpoint record differs'))
    records=[]
    with tempfile.TemporaryDirectory() as tmp:
        bad=Path(tmp)/'bad.json'
        for optimized in [False,True]:
            for name,script,text,error in cases:
                bad.write_text(text)
                cmd=[sys.executable]+(['-O'] if optimized else [])+[script,'--check',str(bad)]
                p=subprocess.run(cmd,cwd=here,capture_output=True,text=True,timeout=35)
                if p.returncode==0 or error not in p.stdout+p.stderr:
                    raise RuntimeError(f'Incorrect refusal for {name}: {p.stderr}')
                records.append({'case':name,'optimized':optimized,'returncode':p.returncode,
                                'expected_error_observed':True})
    print(json.dumps({'status':'PASS_RECORD_CORRUPTION_REFUSALS',
                      'distinct_refusal_runs':len(records),'runs':records},indent=2,sort_keys=True))

if __name__=='__main__':main()
