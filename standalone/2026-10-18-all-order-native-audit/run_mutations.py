#!/usr/bin/env python3
"""Run nine deliberately corrupted copies as separate optimized processes."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SOURCE=Path(__file__).with_name('verify.py').read_text()
CASES=[
 ('erased_sixth_power_mask','return scalar if mask else ZERO','return scalar','full_sixth_power_masks'),
 ('false_coprimality','return scalar if mask else ZERO','return scalar if mask and not any(e>=6 and e%6 for e in exps) else ZERO','full_sixth_power_masks'),
 ('collapsed_conjugate_prime','SPLIT_PRIMES=[(7,2),(7,4),(13,3),(13,9)]','SPLIT_PRIMES=[(7,2),(7,2),(13,3),(13,9)]','distinct_prime_characters'),
 ('erased_product_length_term','r * (1 - sigma)','F(0)','central_known_values'),
 ('lost_dual_conductor','return r*(1-2*sigma)+(r-v)*(b+2*sigma-1)','return (r-v)*(b+2*sigma-1)','dual_endpoint_identity'),
 ('erased_full_row_length_term','h/n + 2*k','F(0)','native_excess_identity'),
 ('falsely_bounded_native_excess','return max(F(0), k-5*h/6, F(k,3)-h/6, F(5*k,6)-2*h/3)','return F(1)','native_excess_identity'),
 ('wrong_principal_mellin_shift','return F(5,6)-a/3','return F(1,2)','symmetric_model_floor'),
 ('removed_native_product_sign','return (-1)**total * (factorial(k)//denom)','return factorial(k)//denom','complete_product_coefficients'),
]

def main() -> None:
    records=[]
    for name,old,new,gate in CASES:
        if SOURCE.count(old)!=1:
            raise RuntimeError(f'not one replacement: {name}')
        with tempfile.TemporaryDirectory(prefix='moment-mutation-') as temp:
            script=Path(temp)/'verify.py'
            script.write_text(SOURCE.replace(old,new))
            run=subprocess.run([sys.executable,'-O',str(script)],capture_output=True,text=True,timeout=20)
            if run.returncode==0 or f'CheckFailure: {gate}:' not in run.stderr:
                raise RuntimeError(f'{name} did not fail at {gate}: {run.returncode}\n{run.stderr[-1000:]}')
            records.append({'mutation':name,'result':'REJECTED','gate':gate,'exit_code':run.returncode})
    print(json.dumps({'status':'PASS','scope':'nine actual optimized corrupted subprocesses','results':records},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
