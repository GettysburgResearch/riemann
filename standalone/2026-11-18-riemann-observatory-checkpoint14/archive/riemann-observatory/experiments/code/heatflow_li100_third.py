#!/usr/bin/env python3
"""Independent standard-library interval backend for heatflow Li100.
Uses elementary exp intervals and reciprocal-series convolution, not the author's
hyperbolic inputs/log-series recurrence. No ordinary floating acceptance.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import importlib.util,json
ROOT=Path(__file__).resolve().parents[2]
s=importlib.util.spec_from_file_location('ii',ROOT/'experiments/code/lagarias_compact_integer.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
m.BITS=512;m.S=1<<m.BITS
I=m.I;S=m.S

def main():
    N=100;a=F(1,100)
    ep=I(F(1,2)).exp();em=I(F(-1,2)).exp()
    ch=(ep+em)/2;sh=(ep-em)/2
    ca=(I(a).exp()+I(-a).exp())/2
    q=[ch+ca]+[(ch if k%2==0 else sh)/factorial(k) for k in range(1,N+1)]
    reciprocal=[1/q[0]]
    for n in range(1,N+1):
        reciprocal.append(-sum((q[k]*reciprocal[n-k] for k in range(1,n+1)),I(0))/q[0])
    logcoeff=[I(0)]
    for n in range(1,N+1):
        logcoeff.append(sum((k*q[k]*reciprocal[n-k] for k in range(1,n+1)),I(0))/n)
    rows=[]
    for n in range(1,N+1):
        value=n*sum((comb(n-1,k-1)*logcoeff[k] for k in range(1,n+1)),I(0))
        assert value.lo>0
        rows.append({'n':n,'lower':str(F(value.lo,S)),'upper':str(F(value.hi,S))})
    threshold=ca.log();assert threshold.lo>0
    result={'status':'independent exact scaled-integer interval enclosure; no external packages','parameter_a':str(a),'prefix_length':N,'scale_bits':m.BITS,'input_method':'exp(+/-1/2),exp(+/-a), then pairedcosh/sinh','coefficient_method':'reciprocalqseries then qprime/q convolution','all_lower_bounds_positive':True,'minimum_lower':str(min(F(r['lower']) for r in rows)),'threshold_lower':str(F(threshold.lo,S)),'threshold_upper':str(F(threshold.hi,S)),'rows':rows}
    (ROOT/'experiments/results/heatflow_li100_third.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'prefix':N,'all_lower_bounds_positive':True,'minimum_lower_display_only':float(F(result['minimum_lower'])),'threshold_interval_display_only':[float(F(result['threshold_lower'])),float(F(result['threshold_upper']))]},indent=2))
if __name__=='__main__':main()
