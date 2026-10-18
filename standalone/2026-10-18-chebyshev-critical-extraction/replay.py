#!/usr/bin/env python3
"""Authenticate bytes, reproduce exact finite tests, execute negative controls."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
GATES={
 'endpoint':'endpoint_reproduction', 'quadrature':'root_quadrature',
 'kernel_norm':'kernel_norm', 'raw_cost':'markov_cost',
 'unit':'unit_subtraction', 'mobius':'prime_power_derivative',
 'shared_divisor':'cocycle', 'conjugates':'ideal_census',
 'continuum':'pole_cancellation', 'single_shift':'shift_visibility',
}

def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def main():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name,item in manifest['files'].items():
        if Path(name).name!=name:
            raise RuntimeError('unsafe manifest member')
        data=(ROOT/name).read_bytes()
        if (len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256']
                or blob(data)!=item['git_blob']):
            raise RuntimeError('payload mismatch: '+name)
    expected=(ROOT/'CHECKS.json').read_bytes()
    for flags in ([],['-O']):
        run=subprocess.run([sys.executable,'-B',*flags,str(ROOT/'verify.py')],
                           capture_output=True,timeout=40)
        if run.returncode or run.stdout!=expected:
            raise RuntimeError('accepting replay failed: '+str(flags))
    outcomes=[]
    for mutation,gate in GATES.items():
        run=subprocess.run([sys.executable,'-B','-O',str(ROOT/'verify.py'),
                            '--mutation',mutation],capture_output=True,timeout=40)
        if run.returncode!=2 or run.stderr.decode().strip()!='REJECT:'+gate:
            raise RuntimeError('negative control failed: '+mutation)
        outcomes.append({'mutation':mutation,'gate':gate,'rejected':True,
                         'returncode':run.returncode})
    actual=(json.dumps(outcomes,sort_keys=True,indent=2)+'\n').encode()
    if actual!=(ROOT/'MUTATIONS.json').read_bytes():
        raise RuntimeError('mutation report mismatch')
    print('PASS: manifest; 2 exact modes; 10 executed negative controls. Analytic proof not certified.')

if __name__=='__main__': main()
