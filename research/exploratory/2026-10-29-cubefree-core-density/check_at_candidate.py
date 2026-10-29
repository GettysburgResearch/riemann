#!/usr/bin/env python3
"""Rational b,h corner certificates for all fixed n >= 11."""
from fractions import Fraction as F
import json
from pathlib import Path
D=F(1869347,2500000)
def faces(b,h,x):
    u=1-2*b;q=1-3*b
    return (u*(1-D*x),b+q*h+(1-D)*u*x,b+q*(1-h)+(2*h-D)*u*x)
def windows(t):
    return [('inverse',(t-F(1,2),t)),('second',(t/2,t)),('fourth',(2*t/3,max(t,F(1))))]
configs=[('11-14',F(1,14),F(1,11),F(21,50)),('15+',F(0),F(1,15),F(2,5))]
output={}
for label,hlo,hhi,R in configs:
    records=[]
    for j in range(100):
        blo,bhi=F(j,300),F(j+1,300)
        if 1-2*blo<=R:
            records.append({'interval':[str(blo),str(bhi)],'mode':'trivial'});continue
        got=None
        for i in range(51,151):
            t=F(i,100)
            for mode,(lo,hi) in windows(t):
                vals=[v for b in (blo,bhi) for h in (hlo,hhi) for x in (lo,hi) for v in faces(b,h,x)]
                if max(vals)<=R:
                    got={'interval':[str(blo),str(bhi)],'mode':mode,'t':str(t),'max':str(max(vals))};break
            if got:break
        if got is None: raise AssertionError((label,blo,bhi))
        records.append(got)
    output[label]={'h':[str(hlo),str(hhi)],'target':str(R),'bins':records}
    print(label,'target',R,'verified',len(records),'bins',flush=True)
with Path(__file__).with_name('at-candidate-cover.json').open('w') as out:
    json.dump(output,out,indent=2);out.write('\n')
