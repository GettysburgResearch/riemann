#!/usr/bin/env python3
"""Exact rational cover for the n>=11 natural-label scalar relaxation.

This checks inequalities, not the analytic sieve or detector assumptions.
Each b bin is closed and adjacent bins overlap at endpoints. For each bin a
single cutoff/mode is valid for every h in the stated closed interval.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def faces(b, h, x):
    return (
        (1-b)*(1-F(3,5)*x),
        b+(1-2*b)*h+F(2,5)*(1-b)*x,
        b+(1-2*b)*(1-h)+(2*h-F(3,5))*(1-b)*x,
    )


def certify(lo, hi, h0, h1, target):
    if 1-lo <= target:
        return {"mode":"trivial"}
    for j in range(50,151):
        t=F(j,100)
        modes=(('inverse',t-F(1,2),t),('second',t/2,t),
               ('fourth',2*t/3,max(t,F(1))))
        for mode,x0,x1 in modes:
            # Each face is multilinear in b,h,x. Thus the closed-box maximum
            # occurs at a corner, including the h=0 limiting endpoint.
            if all(max(faces(b,h,x)) <= target
                   for b in (lo,hi) for h in (h0,h1) for x in (x0,x1)):
                return {"mode":mode,"t":str(t),"x0":str(x0),"x1":str(x1)}
    raise AssertionError((lo,hi,h0,h1,target))


def make_cover():
    blocks=(('11-20',F(1,20),F(1,11),F(29,50)),
            ('21+',F(0),F(1,21),F(14,25)))
    out={}
    for name,h0,h1,R in blocks:
        rows=[]
        for j in range(100):
            lo=F(j,200);hi=F(j+1,200)
            rows.append({"b_lo":str(lo),"b_hi":str(hi),
                         **certify(lo,hi,h0,h1,R)})
        assert rows[0]['b_lo']=='0' and rows[-1]['b_hi']=='1/2'
        out[name]={"h_lo":str(h0),"h_hi":str(h1),"R":str(R),"rows":rows}
        print(name,'PASS',len(rows),'t=1/2',sum(r.get('t')=='1/2' for r in rows))
    # D(n)=(12n²−38n+5)/(21n²−80n+50) is strictly decreasing for n>=4:
    # D'(n)=−6(3n−10)(9n−25)/(21n²−80n+50)².
    def D(n):return F(12*n*n-38*n+5,21*n*n-80*n+50)
    assert D(20)-F(29,50)==F(36,3425)
    # D(n)−14/25=(6n²+170n−575)/[25(21n²−80n+50)] >0 for n>=21.
    assert 6*21**2+170*21-575>0
    return out


if __name__=='__main__':
    result=make_cover()
    p=Path(__file__).with_name('all-orders-cover.json')
    p.write_text(json.dumps(result,indent=2)+'\n')
