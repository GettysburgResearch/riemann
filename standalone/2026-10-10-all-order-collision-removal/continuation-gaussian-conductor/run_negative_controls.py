#!/usr/bin/env python3
"""Execute algebraic mutations and a tampered-output refusal in both modes."""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path)
    ns=parser.parse_args()
    if ns.write and ns.check:
        parser.error('choose --write or --check')
    here=Path(__file__).resolve().parent
    source=(here/'check_eisenstein_covariance.py').read_text(encoding='utf-8')
    mutations=[
        ('erase_shared_prime_mask','for d in submasks(g):','for d in (0,):',
         'ValueError: row_kernel:exact_mask_identity'),
        ('erase_dilation_phase','mul(psi(a,b,gen[d],primes),inner)','inner',
         'ValueError: row_kernel:exact_mask_identity'),
        ('wrong_quadratic_conjugation','return x[0]-x[1], -x[1]','return x[0], -x[1]',
         'ValueError: local:Gauss_autocorrelation'),
    ]
    records=[]
    with tempfile.TemporaryDirectory(prefix='sextic-negative-') as td:
        folder=Path(td)
        for optimized in (False,True):
            base=[sys.executable,'-I','-S','-B']+(['-O'] if optimized else [])
            for name,old,new,expected in mutations:
                if source.count(old)!=1:
                    raise SystemExit(f'REJECT: mutation anchor {name} is not unique')
                p=folder/(name+'.py')
                p.write_text(source.replace(old,new),encoding='utf-8')
                r=subprocess.run(base+[str(p)],capture_output=True,text=True,timeout=45)
                if r.returncode==0 or expected not in r.stderr:
                    raise SystemExit(f'REJECT: {name} was not rejected at its intended check: {r.stderr}')
                records.append({'mode':'optimized' if optimized else 'normal',
                                'mutation':name,'returncode':r.returncode,'expected_failure':expected})
            data=json.loads((here/'result.json').read_text(encoding='utf-8'))
            data['total_predicates']+=1
            bad=folder/'tampered.json'
            bad.write_text(json.dumps(data),encoding='utf-8')
            r=subprocess.run(base+[str(here/'check_eisenstein_covariance.py'),'--check',str(bad)],
                             capture_output=True,text=True,timeout=45)
            expected='REJECT: recorded result differs from full exact replay'
            if r.returncode==0 or expected not in r.stderr:
                raise SystemExit('REJECT: tampered output was not rejected as intended')
            records.append({'mode':'optimized' if optimized else 'normal','mutation':'tampered_result',
                            'returncode':r.returncode,'expected_failure':expected})
    result={'status':'PASS','executed_refusals':len(records),'records':records}
    if ns.check and json.loads(ns.check.read_text(encoding='utf-8'))!=result:
        raise SystemExit('REJECT: negative-control receipt differs from re-execution')
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if ns.write:
        ns.write.write_text(text,encoding='utf-8')
    print(text,end='')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
