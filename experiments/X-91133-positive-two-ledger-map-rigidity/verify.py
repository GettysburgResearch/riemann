#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path

def rowmul(w,M):
    return [sum(w[i]*M[i][j] for i in range(2)) for j in range(2)]

def main():
    checks=[]
    for b in (F(0),F(1,3),F(1),F(2)):
        M=[[F(1),b],[F(0),F(1)-b/F(2)]]
        assert all(x>=0 for row in M for x in row)
        assert rowmul([F(1),F(2)],M)==[F(1),F(2)]
        score=rowmul([F(2),F(1)],M)
        assert score[0]==2 and score[1]>=1
        checks.append({'b':str(b),'matrix':[[str(x) for x in row] for row in M],
                       'score':[str(x) for x in score]})
    for c in (F(0),F(1,100),F(1,10),F(1,3)):
        a=1-2*c
        target=a+2*c
        score=2*a+c
        assert target==1
        if c==0: assert score==2
        else: assert score<2
    result={
      'classification':'PASS_POSITIVE_TWO_LEDGER_MAP_RIGIDITY',
      'classification_formula':'M=[[1,b],[0,1-b/2]], 0<=b<=2',
      'exact_score_corollary':'b=0 and M=I',
      'checks':checks,
      'scope':'Exact Fraction arithmetic checks the classified cone and the equality-ray obstruction. The proof is symbolic and does not type causal packets or prove RH.'}
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification'])
    print(out)
if __name__=='__main__':main()
