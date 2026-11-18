#!/usr/bin/env python3
"""Exact rational sharpness witnesses for the auxiliary-state3M bound."""
from fractions import Fraction as F
from pathlib import Path
import json

def delta(eigenvalues,K=F(1)):
    def count(t):return sum(0<x<=t for x in eigenvalues)
    return count(4*K)-3*count(2*K)+2*count(K)

def main():
    out=[]
    for M in [1,2,5,10]:
        for sign,a,b in [(1,F(3,2),F(1)),(-1,F(3),F(3,2))]:
            # Equal diagonal2x2 block has exact eigenvalues a-b,a+b.
            base=[a]*M; extended=[v for _ in range(M) for v in [a-b,a+b]]
            shift=delta(extended)-delta(base)
            assert shift==sign*3*M
            out.append({'M':M,'A_eigenvalue':str(a),'D_eigenvalue':str(a),'B_diagonal':str(b),'block_eigenvalues':[str(a-b),str(a+b)],'delta_A':delta(base),'delta_block':delta(extended),'difference':shift,'bound':3*M})
    result={'status':'exact Fraction witnesses; no floating-point assertion','rows':out}
    path=Path(__file__).resolve().parents[1]/'results'/'auxiliary_sharp_exact.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
