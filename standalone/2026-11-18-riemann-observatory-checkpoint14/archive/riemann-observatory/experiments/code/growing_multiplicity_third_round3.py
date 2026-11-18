"""Independent exact H2 projection checks for the growing-multiplicity formula.
Constructs polynomial coefficient vectors and solves their Gram system over Fraction.
Finite checks support indexing, not an asymptotic proof; analytic review is separate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
B=Path(__file__).resolve().parents[2]
def solve(matrix,rhs):
 a=[[F(x) for x in row]+[F(rhs[i])] for i,row in enumerate(matrix)];n=len(a)
 for j in range(n):
  pivot=next(k for k in range(j,n) if a[k][j])
  a[j],a[pivot]=a[pivot],a[j]
  v=a[j][j];a[j]=[x/v for x in a[j]]
  for k in range(n):
   if k==j:continue
   v=a[k][j]
   if v:a[k]=[x-v*y for x,y in zip(a[k],a[j])]
 return [row[-1] for row in a]
rows=[]
for N in range(1,9):
 for m in range(1,13):
  L=N+m
  basis=[[((-1)**(k-j))*comb(m,k-j) if 0<=k-j<=m else 0 for k in range(L+1)] for j in range(N+1)]
  gram=[[sum(x*y for x,y in zip(v,w)) for w in basis] for v in basis]
  coefficient=solve(gram,[1]+[0]*N)
  error=1-coefficient[0]
  product=F(1)
  for j in range(m):product*=F(L-j,L+1+j)
  probability=F(comb(N+m,m),comb(N+2*m,m))
  assert error==1-product==1-probability
  assert 0<error<1 and error<F(m*m,N)
  rows.append({'N':N,'m':m,'exact_Gram_projection_error':str(error),'product_and_hypergeometric_identity_pass':True})
out={'kind':'independent_exact_polynomial_Gram_projection_checks_NOT_asymptotic_proof','cases':len(rows),'N_range':[1,8],'m_range':[1,12],'includes_m_greater_than_N':True,'all_pass':True,'method':'Direct coefficient vectors for (1-z)^m z^j; rational Gram-system solve; comparison with product and binomial-ratio formulas. Complex H2 projection has the same real Gram solution.','scope':'Finite independent indexing/projection checks only. Artanh bounds, uniformity and limiting regimes proved analytically in growing_multiplicity_third_round3.md.','records':rows}
(B/'experiments/results/growing_multiplicity_third_round3.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
