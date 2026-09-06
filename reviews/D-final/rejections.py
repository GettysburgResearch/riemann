#!/usr/bin/env python3
"""Exercise the exact same parser/comparator used by checks.py --check."""
import copy, json, sys, tempfile
from pathlib import Path
import checks

def main():
    expected=checks.run(); cases=[]
    altered=copy.deepcopy(expected);altered['fixtures']+=1
    cases.append(('fixture_count',json.dumps(altered)))
    altered=copy.deepcopy(expected);altered['checks'][0]['result']['u']=1
    cases.append(('counterexample_sign',json.dumps(altered)))
    altered=copy.deepcopy(expected);altered['checks'].pop()
    cases.append(('missing_check',json.dumps(altered)))
    altered=copy.deepcopy(expected);altered['checks'][0]['fixtures']=True
    cases.append(('boolean_integer_alias',json.dumps(altered)))
    altered=copy.deepcopy(expected);altered['checks'][0]['fixtures']=1.0
    cases.append(('float_integer_alias',json.dumps(altered)))
    text=json.dumps(expected)
    cases.append(('duplicate_key','{"schema":"bad",'+text[1:]))
    cases.append(('nonfinite_constant',text.replace('26407','NaN',1)))
    altered=copy.deepcopy(expected);altered['proof_status']='RH_PROVED'
    cases.append(('proof_status_promotion',json.dumps(altered)))
    result=[]
    with tempfile.TemporaryDirectory() as d:
        path=Path(d)/'bad.json'
        for name,text in cases:
            path.write_text(text)
            try:
                parsed=checks.load_strict(path)
                checks.require(checks.strict_equal(parsed,expected),'retained output mismatch')
            except (ValueError,TypeError,KeyError,json.JSONDecodeError):
                result.append({'case':name,'rejected':True})
            else:raise ValueError('corruption accepted: '+name)
    print(json.dumps({'optimized':bool(sys.flags.optimize),'rejected':len(result),'cases':result},indent=2,sort_keys=True))
if __name__=='__main__':main()
