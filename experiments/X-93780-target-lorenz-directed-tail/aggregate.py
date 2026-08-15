#!/usr/bin/env python3
from __future__ import annotations
from decimal import Decimal
from pathlib import Path
import argparse, hashlib, json

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--row66',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); records=[]
    for j in range(2,67):
        p=a.rows/f'row_{j}.json'; d=json.loads(p.read_text())
        assert d['classification']=='PASS_DIRECTED_TARGET_LORENZ_TAIL_AVLT'
        assert d['row_count']==1 and d['event_records']==786432
        assert d['directed_full_minimum_row']==j
        assert Decimal(d['directed_full_lower_bound'])>26
        assert Decimal(d['directed_parent_lower_bound'])>79
        assert Decimal(d['directed_parent_derivative_lower_bound'])>Decimal('0.23')
        assert Decimal(d['last_interval_second_derivative_polynomial_lower'])>0
        assert Decimal(d['last_interval_polynomial_derivative_lower'])>0
        records.append({
            'row':j,
            'full_lower':d['directed_full_lower_bound'],
            'minimum_x':d['directed_full_minimum_x'],
            'parent_lower':d['directed_parent_lower_bound'],
            'parent_derivative_lower':d['directed_parent_derivative_lower_bound'],
        })
    r66=json.loads(a.row66.read_text()); upper=Decimal(r66['directed_full_interval_upper_at_minimum']);
    ordered=sorted(records,key=lambda r:Decimal(r['full_lower']))
    assert ordered[0]['row']==66 and ordered[0]['minimum_x']=='166000'
    assert ordered[1]['row']==65
    sep=Decimal(ordered[1]['full_lower'])-upper
    assert sep>Decimal('1.45')
    payload={
        'classification':'PASS_DIRECTED_ALL_ROW_TARGET_LORENZ_TAIL_AND_ROW66_EXTREMALITY',
        'arithmetic_class':'65_INDEPENDENT_BOOST_FENV_INTERVAL_UINT128_EVENT_SWEEPS',
        'tail_start':166000,
        'rows':[2,66],
        'divisor_count':262144,
        'event_records_total':65*3*262144,
        'global_full_lower':ordered[0]['full_lower'],
        'global_minimum_row':66,
        'global_minimum_x':'166000',
        'row66_interval_upper_at_boundary':str(upper),
        'nearest_competitor_row':65,
        'nearest_competitor_lower':ordered[1]['full_lower'],
        'row66_extremality_separation_lower':str(sep),
        'global_parent_lower':min((r['parent_lower'] for r in records),key=Decimal),
        'global_parent_derivative_lower':min((r['parent_derivative_lower'] for r in records),key=Decimal),
        'row_records':records,
        'extremality_scope':'global minimum of the published analytic lower-envelope certificate, not a pointwise ordering of the exact determinants',
        'rh_established_by_replay':False,
    }
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(payload['classification']);print(payload['proof_object_sha256'])
if __name__=='__main__':main()
