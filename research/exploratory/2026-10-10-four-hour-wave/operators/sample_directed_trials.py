#!/usr/bin/env python3
"""Ordinary sampled R from directed U/trials; never an acceptance certificate."""
import argparse,json
from pathlib import Path
import numpy as np
from flint import arb
from analytic_residual import run as sampled

def run(path,order,coefficient):
    data=json.loads(path.read_text())
    def midpoint(x): return float(arb(x).mid())
    normalized={'z_coefficients_decimal':[[midpoint(x) for x in row] for row in data['exact_trial_z_coefficients_balls']],
       'complement_dimension':data['complement_dimension'],'trial_mode_count':data['trial_modes'],
       'u_matrix_decimal':[[midpoint(x) for x in row] for row in data['U_matrix_balls']]}
    temporary=Path('/tmp/riemann_sample_directed_trial.json')
    temporary.write_text(json.dumps(normalized))
    result=sampled(temporary,order)
    u=np.array(normalized['u_matrix_decimal'])
    r=np.array(result['residual_matrix'])
    result['lower_eigenvalues']=np.linalg.eigvalsh((u+u.T)/2-coefficient*r).tolist()
    result['residual_coefficient']=coefficient
    result['analytic_source_artifact']=str(path)
    result['limitations'].append('directed coefficient balls replaced by floating point midpoints')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('artifact',type=Path);p.add_argument('--order',type=int,default=2000)
    p.add_argument('--coefficient',type=float,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=run(a.artifact,a.order,a.coefficient);a.out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='residual_matrix'},indent=2))
