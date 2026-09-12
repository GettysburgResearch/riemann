"""Exact rational center derivatives for the #875 calibrated seed.

Exploratory unless and until whole-root-box interval bounds are added.
No source coefficients or repository files are modified.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import json

CENTERS=tuple(Q(s) for s in (
 '0.02214740729441991945467506172554831495554696774107269533',
 '0.06294208128372751271228155631799086369338395596615177837',
 '0.1113970777650096508879646441011077685460850985953812789',
 '0.0047318790614544977006562261968942563874719938269197464'))
MULT=(25,4,1,1)
POWERS=(1,2,4,6)
NAMES=('a','b','c','e')

def inverse(mat):
 n=len(mat); a=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(mat)]
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
  p=a[j][j];a[j]=[v/p for v in a[j]]
  for i in range(n):
   if i!=j:
    p=a[i][j];a[i]=[u-p*v for u,v in zip(a[i],a[j])]
 ans=[r[n:] for r in a]
 if any(sum(ans[i][k]*mat[k][j] for k in range(n))!=Q(i==j) for i in range(n) for j in range(n)):
  raise ArithmeticError('inverse failed')
 return ans

def lambdas(xs):
 J=[[nu*k*x**(k-1) for nu,x in zip(MULT,xs)] for k in POWERS]
 R=inverse(J)
 row=[8*nu*x**7 for nu,x in zip(MULT,xs)]
 return [sum(row[k]*R[k][j] for k in range(4)) for j in range(4)]

def edge_response(u,v):
 return [Q(0),2*u*v,4*u*v*(u*u+v*v),6*u*v*(u**4+v**4)+5*u**3*v**3,
         8*u*v*(u**6+v**6)+Q(112,17)*u**3*v**3*(u*u+v*v)]

def main():
 lam=lambdas(CENTERS)
 rows=[]
 for i,j in combinations_with_replacement(range(4),2):
  if i==j and MULT[i]<2:continue
  ds=edge_response(CENTERS[i],CENTERS[j]); normalized=ds[4]-sum(lam[k]*ds[k] for k in range(4))
  rows.append({'edge':NAMES[i]+NAMES[j],'raw_kappa8_derivative':str(-272*normalized),'approximate':float(-272*normalized)})
 result={'scope':'exact center derivatives, not whole native-root box','lambda':[str(v) for v in lam], 'lambda_approx':[float(v) for v in lam],'edges':rows}
 print(json.dumps(result,indent=2))

if __name__=='__main__':main()
