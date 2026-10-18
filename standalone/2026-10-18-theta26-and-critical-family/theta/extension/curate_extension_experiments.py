#!/usr/bin/env python3
"""Compact measured outcomes of the unsuccessful small-cloud/strip runs.

The untrusted producer points are re-evaluated at Decimal precision150.
No existence, impossibility, or rigorous strip theorem is inferred.
"""
from decimal import Decimal as D,getcontext
from pathlib import Path
import argparse
import hashlib
import json
from power_source import targets,DEFAULT_SOURCE

ROOT=Path(__file__).resolve().parent


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=ROOT/'extension_experiments.json')
    args=ap.parse_args()
    getcontext().prec=150
    params_path=ROOT.parent/'gaussian_parameters.json'
    params=json.loads(params_path.read_text())
    start=next(x for x in params['models'] if x['degree']==22 and x['nodes']==64)
    goal=targets(24)
    records=[]
    for L in (1,4,8,12,16):
        path=ROOT/f'power_extension_22_64_cloud{L}_switch.json'
        raw=path.read_bytes();log=json.loads(raw);last=log['rows'][-1]
        b=list(map(D,start['centers']))
        for row in log['rows']:
            for i,x in zip(row['active'],row['beta']):b[i]=D(x)
        b.extend([D(last['x'])]*L)
        values=[sum((x**r for x in b),D(0)) for r in range(2,13)]
        error=max(abs((x-y)/y) for x,y in zip(values[:-1],goal[:-1]))
        deficit=goal[-1]-values[-1]
        fraction=1-deficit/D(log['target_next_delta'])
        if log['crossed'] or error>=D('1e-115'):raise ValueError('unexpected stopped-cloud state')
        records.append({'kind':'real_integer_cloud','input_degree':22,'input_nodes':64,
                        'added_roots':L,'endpoint_nodes':len(b),'target_degree':24,
                        'crossed':False,'anchor_switches':log['anchor_switches'],
                        'maximum_switches':30,'shared_new_node':last['x'],
                        'gaussian_coefficient':last['a'],
                        'next_power_deficit_recomputed':str(deficit),
                        'fraction_of_initial_deficit_closed':str(fraction),
                        'relative_preserved_power_error_recomputed':str(error),
                        'all_endpoint_nodes_positive':min(b)>0,
                        'origin_log':path.name,'origin_sha256':hashlib.sha256(raw).hexdigest(),
                        'limitation':'selected chart or switch budget stopped; no infeasibility claim'})
    for L in (1,4):
        path=ROOT/f'conjugate_pair_cloud{L}_bandthird.json'
        raw=path.read_bytes();log=json.loads(raw);last=log['rows'][-1]
        records.append({'kind':'conjugate_pair_after_real_cloud','added_roots':L,
                        'target_degree':24,'crossed':log['crossed_next_power_target'],
                        'shared_new_node':last['x'],'pair_u':last['y'][-2],
                        'pair_d':last['pair_d'],'physical_band':last['physical_band'],
                        'absolute_square_budget':last['absolute_square_budget'],
                        'next_power_deficit':str(-D(last['next_residual'])),
                        'relative_preserved_power_error':last['relative_preserved_power_error'],
                        'origin_log':path.name,'origin_sha256':hashlib.sha256(raw).hexdigest(),
                        'limitation':'physical1/3 band approached before next moment was matched'})
    out={'schema':'theta.extension.exploratory_boundaries.v1',
         'status':'ORDINARY_DECIMAL_DIAGNOSTICS_NOT_EXISTENCE_OR_IMPOSSIBILITY_CERTIFICATES',
         'input_parameters_sha256':hashlib.sha256(params_path.read_bytes()).hexdigest(),
         'theta26_source_sha256':hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest(),
         'records':records}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('CURATED_EXTENSION_DIAGNOSTICS',len(records))


if __name__=='__main__':main()
