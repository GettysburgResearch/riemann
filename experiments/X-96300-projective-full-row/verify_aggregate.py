#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from decimal import Decimal
from pathlib import Path
HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'aggregate.json').read_text())
proof=d.pop('proof_object_sha256')
calc=hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert calc==proof,(calc,proof)
assert d['classification']=='PASS_COMPLETE_MPFR_DIRECTED_TARGET_LORENZ_TAIL_51M'
assert d['row_count']==65 and d['event_records']==51118080
assert [x['row_start'] for x in d['chunks']]==[2,10,18,26,34,42,50,58]
assert [x['row_end'] for x in d['chunks']]==[9,17,25,33,41,49,57,66]
for k in ['global_directed_full_lower_bound','global_directed_parent_lower_bound','global_directed_parent_derivative_lower_bound','global_last_interval_second_derivative_polynomial_lower','global_last_interval_polynomial_derivative_lower','row66_extremality_separation_lower']:
    assert Decimal(str(d[k]))>0,k
assert d['global_minimum_row']==66 and str(d['global_minimum_x'])=='166000'
assert d['rh_established_by_replay'] is False
print('PASS_COMPLETE_MPFR_DIRECTED_TARGET_LORENZ_TAIL_51M')
print(proof)
