#!/usr/bin/env python3
"""Extract complete endpoints and compact provenance from exploration logs.

No trajectory or endpoint receives a rigorous claim from this curation.
The endpoint checker consumes the curated rational centers separately.
"""
from pathlib import Path
from decimal import Decimal as D,getcontext
import argparse
import hashlib
import json
from power_source import targets,DEFAULT_SOURCE

ROOT=Path(__file__).resolve().parent


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--logs',type=Path,nargs='+',default=[ROOT/f'power_extension_22_64_cloud{L}_switch.json' for L in (20,24,32)])
    ap.add_argument('--parameters',type=Path,default=ROOT.parent/'gaussian_parameters.json')
    ap.add_argument('--output',type=Path,default=ROOT/'power_extension_candidates.json')
    args=ap.parse_args()
    getcontext().prec=150
    models=[]
    for path in args.logs:
        raw=path.read_bytes();log=json.loads(raw)
        final=log['final']
        if not log['crossed'] or final is None or not final['all_nodes_positive']:
            raise ValueError('only completed positive-node endpoints can be curated')
        b=list(map(D,final['b']));degree=log['input_degree']+2
        goal=targets(degree)
        measured=[sum((x**r for x in b),D(0)) for r in range(2,degree//2+1)]
        error=max(abs((x-y)/y) for x,y in zip(measured,goal))
        if error>=D('1e-120'):raise ValueError('curated endpoint midpoint residual too large')
        bracket=[{k:row[k] for k in ('x','a','next_residual')}
                 for row in log['rows'][-2:]]
        models.append({'degree':degree,'nodes':len(b),'settled':True,
                       'b':final['b'],'target':[str(x) for x in goal],
                       'a':final['a'],'relative_power_error_recomputed':str(error),
                       'input_degree':log['input_degree'],'input_nodes':log['input_nodes'],
                       'added_node_multiplicity':log['cloud'],
                       'shared_new_node':final['shared_new_node'],
                       'old_active_indices_at_crossing':final['active_old_indices'],
                       'anchor_switches':log['anchor_switches'],
                       'crossing_bracket_producer_values':bracket,
                       'origin_log':path.name,'origin_log_sha256':hashlib.sha256(raw).hexdigest(),
                       'trajectory_status':'ORDINARY_DECIMAL_UNCERTIFIED',
                       'exact_endpoint_claim':'NONE; requires the separate directed checker'})
    out={'schema':'theta.power_extension.chosen_candidates.v1',
         'status':'RATIONAL_CENTERS_FROM_ORDINARY_DECIMAL_CONTINUATION_NOT_CERTIFICATE',
         'input_parameters_sha256':hashlib.sha256(args.parameters.read_bytes()).hexdigest(),
         'theta26_source_sha256':hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest(),
         'models':models}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('CURATED_POWER_ENDPOINTS',[(m['degree'],m['nodes']) for m in models])


if __name__=='__main__':main()
