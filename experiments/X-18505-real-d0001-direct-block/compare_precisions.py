#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,hashlib
from fractions import Fraction
from pathlib import Path

def ep(x):return Fraction(int(x['mantissa']))*Fraction(2)**int(x['exponent'])
def iv(x):return ep(x['lower']),ep(x['upper'])
def intervals(obj,path=''):
 if isinstance(obj,dict):
  if set(obj)=={'lower','upper'} and all(isinstance(obj[k],dict) for k in obj):yield path,iv(obj)
  else:
   for k,v in obj.items():yield from intervals(v,f'{path}.{k}' if path else k)
 elif isinstance(obj,list):
  for i,v in enumerate(obj):yield from intervals(v,f'{path}[{i}]')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('outer',type=Path);ap.add_argument('inner',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();O=json.loads(a.outer.read_text());I=json.loads(a.inner.read_text());od=dict(intervals(O));id=dict(intervals(I));common=sorted(set(od)&set(id));bad=[]
 for p in common:
  ol,oh=od[p];il,ih=id[p]
  if not(ol<=il<=ih<=oh):bad.append(p)
 if bad:raise SystemExit('non-nested intervals: '+', '.join(bad[:10]))
 r={'schema':'riemann.x18505.precision-nesting.v1','outer_precision':O['provenance']['precision_bits'],'inner_precision':I['provenance']['precision_bits'],'interval_count':len(common),'nonnested':bad,'verdict':'HIGHER_PRECISION_INTERVALS_NESTED'};r['sha256']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest();a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__':main()
