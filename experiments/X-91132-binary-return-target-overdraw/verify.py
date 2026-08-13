#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path

def rowmul(w,A):
    return [sum(w[k]*A[k][j] for k in range(len(A))) for j in range(len(A[0]))]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrices(r):
    C=[[(1-r)*(1+2*r),F(0)],[(1-r)*r,(1-r)*(1-2*r)]]
    H=[[r*r,2*r*(1-r)],[F(0),r*(2-r)]]
    return C,H

def main():
    rows=[]
    for r in (F(1,9),F(1,11),F(1,16),F(2,5)):
        C,H=matrices(r)
        total=add(C,H)
        target=rowmul([F(1),F(2)],total)
        score=rowmul([F(2),F(1)],total)
        delta=3*r*(1-r)
        assert target==[1+delta,F(2)]
        assert score==[2+delta,1+delta]
        rows.append({'r':str(r),'target':[str(x) for x in target],
                     'score':[str(x) for x in score],
                     'excess':str(delta)})
    C,H=matrices(F(1,9))
    witness=rowmul([F(1),F(2)],add(C,H))[0]
    assert witness==F(35,27)>1
    result={
      'classification':'PASS_BINARY_RETURN_TARGET_OVERDRAW_COUNTEREXAMPLE',
      'formula':'(1,2)(C_r+H_r)=(1+3r-3r^2,2)',
      'witness_r':'1/9','witness_target':'35/27',
      'checks':rows,
      'scope':'Exact Fraction arithmetic refutes target conservation for the advertised matrices. It does not propose corrected matrices or prove RH.'}
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification'])
    print(out)
if __name__=='__main__':main()
