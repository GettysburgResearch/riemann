#!/usr/bin/env python3
"""Execute ten deliberately incorrect implementations in separate optimized processes."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=(HERE/'verify.py').read_text()
CASES=[
 ('wrong_local_sign','value *= -(1-F(1,q**h))*F(1,q**((e-1)*h))',
  'value *= (1-F(1,q**h))*F(1,q**((e-1)*h))','complete_convolution'),
 ('wrong_prime_power_tail','q**((e-1)*h)','q**(e*h)','complete_convolution'),
 ('erased_unit_subtraction','return (F(a==UNIT)-coefficient(a,h))/h',
  'return -coefficient(a,h)/h','unit_subtraction'),
 ('lost_translation_weight','coefficient(b,h)*coefficient(d,k)/ideal_norm(d)**h',
  'coefficient(b,h)*coefficient(d,k)','translation_cocycle'),
 ('false_coprimality','if allowed(b,excluded) and allowed(d,excluded)),F(0))',
  'if allowed(b,excluded) and allowed(d,excluded) and not (dict(b).keys() & dict(d).keys())),F(0))',
  'complete_convolution'),
 ('wrong_stencil_sign','return (-1)**(j-1)*comb(m,j)',
  'return (-1)**j*comb(m,j)','stencil_constant'),
 ('unsubtracted_shifted_pole','return (1-q)/h-1/(s+h-1)',
  'return (1-q)/h','shifted_pole_centering'),
 ('wrong_continuum_shift','(1-t)*L+b*b-(u-L-2*b)**2/4',
  '(1-t)*L+b*b-(u-L+2*b)**2/4','exact_continuum_square'),
 ('wrong_critical_jacobian','return -F(p,2)-1',
  'return -F(p)-1','critical_jacobian'),
 ('collapsed_ideal_prime_support','return PQS[a[0][0]] if len(a)==1 else 0',
  'return PQS[a[0][0]] if a else 0','same_norm_not_prime_power'),
]

def main() -> None:
    reports=[]
    for name,old,new,gate in CASES:
        if SOURCE.count(old)!=1:
            raise RuntimeError(f'nonunique mutation {name}: {SOURCE.count(old)}')
        with tempfile.TemporaryDirectory(prefix='critical-translation-mutation-') as directory:
            file=Path(directory)/'verify.py'
            file.write_text(SOURCE.replace(old,new))
            result=subprocess.run([sys.executable,'-O',str(file)],capture_output=True,text=True,timeout=20)
            if result.returncode==0 or f'Failure: {gate}:' not in result.stderr:
                raise RuntimeError(f'{name} did not fail at {gate}: {result.stderr[-1200:]}')
            reports.append({'mutation':name,'gate':gate,'exit_code':result.returncode,'result':'REJECTED'})
    print(json.dumps({'status':'PASS','scope':'ten actual optimized corrupted subprocesses',
                      'results':reports},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
