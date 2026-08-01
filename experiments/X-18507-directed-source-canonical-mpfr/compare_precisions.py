#!/usr/bin/env python3
import argparse,json
from fractions import Fraction
from pathlib import Path
from common import *
def walk(x,p=''):
    if isinstance(x,dict):
        if set(x)=={'lower','upper'}:
            try:yield p,iv(x);return
            except:pass
        for k,v in x.items():yield from walk(v,p+'.'+k if p else k)
    elif isinstance(x,list):
        for i,v in enumerate(x):yield from walk(v,f'{p}[{i}]')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('outer',type=Path);ap.add_argument('inner',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();O=json.loads(a.outer.read_text());I=json.loads(a.inner.read_text());oo=dict(walk(O));ii=dict(walk(I));bad=[]
    for p in sorted(oo.keys()&ii.keys()):
        x,y=oo[p],ii[p]
        if not(x.lo<=y.lo<=y.hi<=x.hi):bad.append(p)
    if bad:raise SystemExit('nonnested: '+','.join(bad[:10]))
    out={'schema':'riemann.x18507.precision-nesting.v1','outer_sha256':file_sha(a.outer),'inner_sha256':file_sha(a.inner),'interval_count':len(oo.keys()&ii.keys()),'nonnested':bad,'verdict':'HIGHER_PRECISION_CERTIFICATE_NESTED'};out['sha256']=canonical_sha(out);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
