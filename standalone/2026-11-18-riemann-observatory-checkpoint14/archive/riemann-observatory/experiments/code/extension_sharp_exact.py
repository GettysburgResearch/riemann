#!/usr/bin/env python3
"""Exact counts for the sharp two-sided momentum-extension example."""
from fractions import Fraction as F
from pathlib import Path
import json

def counts(theta,K):
    assert 0<theta<1
    return [max(0,(j*K-theta).__floor__()+1) for j in [1,2,4]]

def main():
    K=F(7,10);rows=[]
    for d in [1,2,5,10]:
        c0=[d*x for x in counts(F(9,10),K)];c1=[d*x for x in counts(F(3,5),K)]
        D0=c0[2]-3*c0[1]+2*c0[0];D1=c1[2]-3*c1[1]+2*c1[0]
        assert D1-D0==3*d
        rows.append({'defect':d,'K':str(K),'A0_phase':'9/10','A1_phase':'3/5','counts_A0_at_K_2K_4K':c0,'counts_A1_at_K_2K_4K':c1,'delta_A0':D0,'delta_A1':D1,'difference':D1-D0})
    result={'status':'exact rational counts; differential-operator realization proved analytically','rows':rows}
    out=Path(__file__).resolve().parents[1]/'results'/'extension_sharp_exact.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
