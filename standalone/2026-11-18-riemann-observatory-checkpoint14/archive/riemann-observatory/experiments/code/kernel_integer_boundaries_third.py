#!/usr/bin/env python3
"""Third-review exact checks at Fourier-orthogonality integer cell boundaries.
This does NOT rerun the all-cell interval validator or execute Lean.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,struct

def main():
    root=Path(__file__).resolve().parents[2]
    data=root/'experiments/inputs/839_first_window'
    meta=json.loads((data/'inputs.json').read_text());raw=(data/'kernel_lower.bin').read_bytes()
    H,V,R=meta['grid'],meta['scale'],meta['R']
    tab=struct.unpack('<'+'I'*(R+1),raw)
    digest=hashlib.sha256(raw).hexdigest()
    assert digest==meta['table_sha256']=='b80e5a8c70e4beb3b872dada426016bc97b0954c1a8a5eabaeb40fba49cded36'
    a=[F(x,meta['denominator']) for x in meta['window_coefficients']]
    assert sum(map(abs,a))==F(321589,1000000)
    rows=[]
    for n in range((R+1)//H+1):
        K=F(1) if n==0 else a[n-1]/2 if n<=len(a) else F(0)
        for k in [n*H-1,n*H]:
            if not 0<=k<=R:continue
            assert F(tab[k],V)<=K*K
            rows.append({'integer_t':n,'cell':k,'claim':tab[k],'scaled_exact_K_squared':str(V*K*K)})
    result={'status':'exact Fraction boundary checks; no all-cell rerun','table_sha256':digest,'checks':len(rows),'rows':rows}
    (root/'experiments/results/kernel_integer_boundaries_third.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Passed',len(rows),'exact integer-boundary checks; binary hash matches pinned inputs.')
if __name__=='__main__':main()
