#!/usr/bin/env python3
"""Exact finite checks of an all-m multiplicity-aware polynomial approximant."""
from fractions import Fraction as F
from math import comb,prod
from pathlib import Path
import json

def main():
    rows=[]
    for m in range(1,11):
        for N in [0,1,2,3,5,10,30,100]:
            L=N+m; D=prod(L+j for j in range(1,m+1))
            a=[F(comb(n+m-1,m-1)*prod(L-n-j for j in range(m)),D) for n in range(N+1)]
            c=[F(0)]*(L+1); c[0]=1
            for n,x in enumerate(a):
                for j in range(m+1): c[n+j]-=x*((-1)**j)*comb(m,j)
            # Every column is orthogonal to residual: this certifies optimality.
            assert all(sum(((-1)**j)*comb(m,j)*c[n+j] for j in range(m+1))==0 for n in range(N+1))
            norm=sum(x*x for x in c)
            asserted=1-F(prod(L-j for j in range(m)),D)
            assert norm==asserted==c[0]
            rows.append({'m':m,'N':N,'L':L,'optimal_norm_squared':str(norm),'orthogonality_passed':True})
    path=Path(__file__).resolve().parents[1]/'results'/'multiplicity_general_exact.json'
    path.write_text(json.dumps({'method':'exact rational orthogonality and norm checks','rows':rows},indent=2)+'\n')
    print(f'Checked {len(rows)} (m,N) pairs with exact rational arithmetic.')
if __name__=='__main__':main()
