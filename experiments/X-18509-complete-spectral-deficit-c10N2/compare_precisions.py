#!/usr/bin/env python3
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path

def ep(e): return Fraction(int(e['mantissa'])) * (Fraction(2) ** int(e['exponent']))
def iv(x): return ep(x['lower']), ep(x['upper'])

def main():
    p=argparse.ArgumentParser();p.add_argument('coarse',type=Path);p.add_argument('fine',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    c=json.loads(a.coarse.read_text());f=json.loads(a.fine.read_text())
    if (c['support']['c'],c['support']['N'])!=(f['support']['c'],f['support']['N']) or c['metric_diagonal']!=f['metric_diagonal']:raise SystemExit('structural mismatch')
    checked=[]
    for key in ('P_even','E_even'):
        for i,row in enumerate(c[key]):
            for j,x in enumerate(row):
                ci=iv(x);fi=iv(f[key][i][j])
                if not (ci[0] <= fi[0] <= fi[1] <= ci[1]):raise SystemExit(f'nonnested {key}[{i},{j}]')
                checked.append(f'{key}[{i},{j}]')
    out={'schema':'riemann.x18509.precision-nesting.v1','classification':'HIGHER_PRECISION_INTERVALS_NESTED','checked':checked,'count':len(checked),'coarse_sha256':hashlib.sha256(a.coarse.read_bytes()).hexdigest(),'fine_sha256':hashlib.sha256(a.fine.read_bytes()).hexdigest()}
    out['proof_object_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text)
    else:print(text,end='')
if __name__=='__main__':main()
