#!/usr/bin/env python3
"""Exact rational k=3 detector-face certificate, finite fixed n only."""
from fractions import Fraction as F
import json
from pathlib import Path

D = F(187,250)
CASES = [(8,F(449,1000)),(9,F(7,16)),(10,F(43,100)),(11,F(21,50)),(15,F(2,5)),(20,F(39,100)),(30,F(37,100))]

def faces(b,n,x):
    u=1-2*b
    q=1-3*b
    return (u*(1-D*x),b+q/n+(1-D)*u*x,b+q*(1-F(1,n))+(F(2,n)-D)*u*x)

def windows(t):
    return [('inverse',(t-F(1,2),t)),('second',(t/2,t)),('fourth',(2*t/3,max(t,F(1))))]

cert = {}
for n,R in CASES:
    records=[]
    for j in range(100):
        a=F(j,300);b=F(j+1,300)
        if 1-2*a<=R:
            records.append({'interval':[str(a),str(b)],'mode':'trivial'});continue
        got=None
        for i in range(251,751):
            t=F(i,500)
            for mode,(lo,hi) in windows(t):
                exact=max(v for y in (a,b) for x in (lo,hi) for v in faces(y,n,x))
                if exact<=R:
                    got={'interval':[str(a),str(b)],'mode':mode,'t':str(t),'max':str(exact)};break
            if got:break
        if not got:raise AssertionError((n,R,a,b))
        records.append(got)
    sigma=F(437,500)
    deF=1-D*(D*n*n-(6*sigma-2)*n+3)/(D*(3-2*sigma)*n*n-4*sigma*n+2)
    assert deF>R
    cert[str(n)]={'target':str(R),'defaveri':str(deF),'gap':str(deF-R),'bins':records}
    print(n,'target',R,'source',deF,'gap',deF-R,flush=True)
with Path(__file__).with_name('cover.json').open('w') as out:json.dump(cert,out,indent=2);out.write('\n')
