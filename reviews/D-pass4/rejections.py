#!/usr/bin/env python3
"""Exercise actual result parser/comparator and semantic P61 checks."""
from __future__ import annotations
import copy,json,sys,tempfile
from pathlib import Path
sys.dont_write_bytecode=True
from checks import Failure,need,read,p61_contract
R=Path(__file__).resolve().parent
out=[]
def rejects(name,fn):
    try:fn()
    except (Failure,ValueError,TypeError,KeyError):out.append(name)
    else:raise Failure('mutation accepted '+name)
a=read(R/'checks.normal.json')
with tempfile.TemporaryDirectory() as d:
    p=Path(d)/'candidate.json'
    for name,mutate in [
      ('status',lambda x:x.update(status='FAIL')),
      ('missing_record',lambda x:x['records'].pop()),
      ('wrong_count',lambda x:x.update(bounded_fixtures=6254)),
      ('false_primitive_claim',lambda x:x.update(primitive_Pick_values_recomputed=True)),
      ('extra_claim',lambda x:x.update(RH=True))]:
        b=copy.deepcopy(a);mutate(b);p.write_text(json.dumps(b));rejects(name,lambda:need(read(p)==a,'result mismatch'))
    p.write_text('{"status":"PASS","status":"PASS"}');rejects('duplicate_key',lambda:read(p))
    p.write_text('{"x":NaN}');rejects('nonfinite_json',lambda:read(p))
    p.write_text('{');rejects('malformed_json',lambda:read(p))
for name,mutate in [
 ('P61_short_scan',lambda x:x.update(finite_endpoint=999999)),
 ('P61_skipped_checks',lambda x:x.update(finite_inequalities_checked=1)),
 ('P61_boolean_count',lambda x:x.update(divisor_count=True)),
 ('P61_tail_zero',lambda x:x['tail_minima'][0].update(lower_numerator='0')),
 ('P61_missing_slab',lambda x:x['tail_minima'][1].update(slabs_checked=256804)),
 ('P61_reversed_interval',lambda x:x['finite_minima'][0].update(numerator_interval=['2','1'])),
 ('P61_wrong_denominator',lambda x:x.update(tail_denominator='1')),
 ('P61_RH_claim',lambda x:x.update(RH_proved=True))]:
    b=read(R/'p61.full.json');mutate(b);rejects(name,lambda:p61_contract(b))
result={'schema':'reviewer-D.pass4.rejections.v1','status':'PASS','rejected_count':len(out),'rejected':out,'boundary':'Parser/comparator and semantic-result corruption tests; not primitive replay.'}
if '--output' in sys.argv:Path(sys.argv[sys.argv.index('--output')+1]).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
else:print(json.dumps(result,sort_keys=True,indent=2))
