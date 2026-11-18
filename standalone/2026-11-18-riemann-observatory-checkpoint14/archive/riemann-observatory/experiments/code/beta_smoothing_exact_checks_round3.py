#!/usr/bin/env python3
"""Exact arithmetic bookkeeping checks for the beta smoothing proof.
Not a numerical proof of transcendental tuning, source theorems, or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json

def main():
    nu=F(5,4); p=F(3,4)
    beta_correction=(4*nu*nu-1)/8
    endpoint_correction=p*(p+1)/2
    assert beta_correction==endpoint_correction==F(21,32)
    first_constant=F(5,16)-1+F(7,8)
    assert first_constant==F(3,16)
    # Q_T(1/2) is a polynomial in t=T².
    q=[F(1,16)*F(9,16),F(1,16)+F(9,16),F(1)]
    assert q==[F(5,16)**2-F(1,16),2*F(5,16),F(1)]
    # Endpoint-IVT estimate is below1 already atT256.
    endpoint_numerator=100000*3**9
    assert endpoint_numerator==1968300000<256**4
    assert F(44,7)*F(50,49)<7
    checked=[]
    for N in range(1,1001):
        B=8*N*N+50; T=10*N*B
        assert T>=580 and T>=256
        assert F(8*N*N,T*T)<F(1,12*B*B)
        assert F(1,6*B*B)-F(8*N*N,T*T)>F(1,12*B*B)
        # Exact squared comparison for the sine-test gamma upper bound.
        assert 4*(16*N**4+441)<(8*N*N+42)**2
        assert 4*(4*N*N-1)>(2*N)**2
        if N in [1,2,5,10,100,1000]:checked.append({'N':N,'T_N':T,'B_N':B})
    out={'status':'exact rational/integer checks passed',
         'completion_convention':'Z=pi^(s/2)F/[s(s-1)Gamma(s/2)], F(1)=1; no factor1/2',
         'beta_first_correction_factor':str(beta_correction),
         'summed_first_constant':str(first_constant),
         'endpoint_IVT_numerator':endpoint_numerator,'endpoint_T':256,
         'tested_N_range':[1,1000],'examples':checked,
         'limitations':'Analytic infinite-family statements and tuning existence are proved in the audit; these finite checks validate arithmetic only.'}
    path=(Path(__file__).resolve().parents[1]/'results'/'beta_smoothing_exact_checks_round3.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'output':str(path)}))
if __name__=='__main__':main()
