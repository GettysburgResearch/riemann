#!/usr/bin/env python3
"""Exact rational finite-block interlacing checks; supplemental to all-operator proof."""
from fractions import Fraction as F
from pathlib import Path
import json,random
class PivotZero(Exception):pass

def below(matrix,x):
    # Exact LDL congruence without pivoting; singular leading minors are rejected.
    a=[[F(v) for v in row] for row in matrix]
    for i in range(len(a)):a[i][i]-=x
    neg=0
    for k in range(len(a)):
        p=a[k][k]
        if not p:raise PivotZero
        neg+=int(p<0)
        for i in range(k+1,len(a)):
            for j in range(i,len(a)):
                a[i][j]-=a[i][k]*a[j][k]/p
                a[j][i]=a[i][j]
    return neg

def block(a,b,d):
    n=len(a);m=len(d)
    return [list(a[i])+list(b[i]) for i in range(n)]+[[b[i][j] for i in range(n)]+list(d[j]) for j in range(m)]
def diag(values):return [[F(x) if i==j else F(0) for j in range(len(values))] for i,x in enumerate(values)]
def run():
    rng=random.Random(20261117);samples=[];skipped=0
    for n in [4,8,12]:
      for m in [1,2,3]:
       for trial in range(10):
        a=diag([2*i-n+F(1,2) for i in range(n)])
        d=diag([F(4*j+3,2) for j in range(m)])
        b=[[F(rng.randrange(-4,5),3) for j in range(m)] for i in range(n)]
        t=block(a,b,d)
        for K in [F(1,2),F(1),F(3,2),F(2)]:
          try:
            shifts=[below(t,k*K)-below(a,k*K) for k in [1,2,4]]
          except PivotZero:skipped+=1;continue
          assert all(0<=x<=m for x in shifts)
          curvature=shifts[2]-3*shifts[1]+2*shifts[0]
          assert abs(curvature)<=3*m
          samples.append({'n':n,'M':m,'trial':trial,'K':str(K),'exact_count_shifts':shifts,'curvature_difference':curvature})
    result={'status':'exact_Fraction_checks_passed','proof_status':'supplemental finite rational matrix checks; operator theorem proved separately','checked_cases':len(samples),'skipped_zero_leading_pivot_cases':skipped,'samples':samples}
    out=Path(__file__).resolve().parents[1]/'results'/'auxiliary_parent_exact.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='samples'},indent=2))
if __name__=='__main__':run()
