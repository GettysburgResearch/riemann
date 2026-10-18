"""Reconstruct numerical target moments from the original theta density.

mpmath quadrature is NOT interval quadrature. Analytic formulas bound the
omitted index/time tails, but this script does not enclose arithmetic or
quadrature errors. Its output cannot serve as a root certificate.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import mpmath as mp

def build(degree:int=40,digits:int=60)->dict:
    if degree<2 or degree>40 or degree%2:raise ValueError('even degree 2..40 required')
    if not 30<=digits<=150:raise ValueError('digits must lie in 30..150')
    mp.mp.dps=digits
    T=mp.mpf(3);nmax=8
    qs=[mp.pi*n*n for n in range(1,nmax+1)]
    def density(t):
        e=mp.exp(2*t)
        return mp.fsum((4*q*q*mp.exp(mp.mpf(9)*t/2)-6*q*mp.exp(mp.mpf(5)*t/2))
                       *mp.exp(-q*e) for q in qs)
    raw=[];tails=[]
    for r in range(0,degree+1,2):
        raw.append(mp.quad(lambda t:t**r*density(t),[0,mp.mpf('.25'),mp.mpf('.5'),1,mp.mpf('1.5'),2,3]))
        time_tail=mp.mpf(0)
        for q in qs:
            A=2*q*mp.exp(2*T)-mp.mpf(9)/2
            time_tail+=4*q*q*mp.exp(mp.mpf(9)*T/2-q*mp.exp(2*T))*mp.fsum(
                math.comb(r,k)*T**(r-k)*mp.factorial(k)/A**(k+1) for k in range(r+1))
        q=mp.pi*(nmax+1)**2
        # The successive-index ratio is <1/2 for n>=9, including the denominator.
        index_tail=8*q*q*mp.exp(-q)*mp.factorial(r)/(2*q-mp.mpf(9)/2)**(r+1)
        tails.append(time_tail+index_tail)
    variance=raw[1]/raw[0]
    moments=[v/raw[0]/variance**r for r,v in enumerate(raw)]
    return {'status':'EXPLORATORY_SOURCE_ONLY','interval_arithmetic':False,
            'quadrature_error_enclosed':False,'digits':digits,'degree':degree,
            'explicit_indices':nmax,'time_cutoff':str(T),'variance':str(variance),
            'mom':[str(v) for v in moments],
            'one_sided_truncated_integrals':[str(v) for v in raw],
            'analytic_omission_bound_nondirected_evaluations':[str(v) for v in tails]}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--degree',type=int,default=40);ap.add_argument('--digits',type=int,default=60)
    args=ap.parse_args()
    if args.output.exists():ap.error('refusing to overwrite an existing output')
    result=build(args.degree,args.digits);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'degree':result['degree'],'digits':result['digits']}))
if __name__=='__main__':main()
