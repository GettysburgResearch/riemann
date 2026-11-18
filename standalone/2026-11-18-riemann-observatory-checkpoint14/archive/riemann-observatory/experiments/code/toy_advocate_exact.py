#!/usr/bin/env python3
"""Independent exact finite-dimensional residual checks for a double boundary root."""
from fractions import Fraction as F
import json
from pathlib import Path

def residual(a):
    c=[F(0)]*(len(a)+2)
    c[0]=1
    for j,x in enumerate(a):
        c[j]-=x; c[j+1]+=2*x; c[j+2]-=x
    return c

def main():
    rows=[]
    for N in range(0,101):
        L=N+2; D=(L+1)*(L+2)
        a=[F((n+1)*(L-n)*(L-n-1),D) for n in range(N+1)]
        c=residual(a)
        formula=[F(2*(2*L+1)-6*k,D) for k in range(L+1)]
        assert c==formula
        assert sum(c)==1 and sum(k*x for k,x in enumerate(c))==0
        norm=sum(x*x for x in c)
        assert norm==F(2*(2*L+1),D)
        # Orthogonality to all columns of multiplication by (1-z)^2
        assert all(c[j]-2*c[j+1]+c[j+2]==0 for j in range(N+1))
        row={'N':N,'optimal_norm_squared':str(norm)}
        if N:
            w=[F(n+1)*(1-F(n,N)) for n in range(N+1)]
            cw=residual(w)
            triangular=sum(x*x for x in cw)
            assert triangular==1+F(4,N)
            row['triangular_norm_squared']=str(triangular)
        rows.append(row)
    path=Path(__file__).resolve().parents[1]/'results'/'toy_advocate_exact.json'
    path.write_text(json.dumps({'method':'independent rational residual + orthogonality checks; analytic proof in audit','rows':rows},indent=2)+'\n')
    print('Verified exact formulas for N=0..100; triangular window for N=1..100.')
if __name__=='__main__': main()
