#!/usr/bin/env python3
"""Exact finite-field counts and formal-zeta stress test; standard library only."""
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
P=5

def add(a,b):return tuple((x+y)%P for x,y in zip(a,b))
def neg(a):return tuple(-x%P for x in a)
def mul(a,b,modulus):
 n=len(a);c=[0]*(2*n-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
 for d in range(2*n-2,n-1,-1):
  for j in range(n):c[d-n+j]=(c[d-n+j]-c[d]*modulus[j])%P
 return tuple(c[:n])
def curve_count(n,modulus):
 F=list(product(range(P),repeat=n));zero=(0,)*n;one=(1,)+(0,)*(n-1)
 # Check inverses directly, so the advertised extension is certified a field.
 for a in F:
  if a!=zero:assert any(mul(a,b,modulus)==one for b in F)
 squares={}
 for y in F:
  yy=mul(y,y,modulus);squares[yy]=squares.get(yy,0)+1
 count=1 # unique projective point at infinity
 for x in F:
  rhs=add(mul(mul(x,x,modulus),x,modulus),neg(x))
  count+=squares.get(rhs,0)
 return {'q':P**n,'degree':n,'modulus_coefficients_low_to_high':modulus,'direct_projective_points':count,'arithmetic':'exact integer tuple arithmetic mod 5; all nonzero inverses checked'}
curves=[curve_count(1,[0,1]),curve_count(2,[3,0,1]),curve_count(3,[1,1,0,1])]
# Frobenius prediction from N_1=8: a_5=5+1-8=-2.
s=[2,-2]
for n in range(2,4):s.append(-2*s[-1]-5*s[-2])
for row in curves:
 row['predicted_points_from_degree_one']=5**row['degree']+1-s[row['degree']]
 assert row['direct_projective_points']==row['predicted_points_from_degree_one']

def mobius(n):
 m=n;num=0;p=2
 while p*p<=m:
  if m%p==0:
   m//=p;num+=1
   if m%p==0:return 0
   while m%p==0:m//=p
  p+=1
 if m>1:num+=1
 return (-1)**num

def divisors(n):return [d for d in range(1,n+1) if n%d==0]
trace=[2,5]
for n in range(2,81):trace.append(5*trace[-1]-5*trace[-2])
formal=[]
for n in range(1,81):
 numerator=sum(mobius(d)*(5**(n//d)+1-trace[n//d]) for d in divisors(n))
 assert numerator%n==0
 b=numerator//n
 full=sum(mobius(d)*5**(n//d) for d in divisors(n))//n
 graph=sum(mobius(d)*trace[n//d] for d in divisors(n))//n
 assert b==full-graph+(n==1) and b>=0
 formal.append({'n':n,'N_n':5**n+1-trace[n],'euler_exponent':b,'full_five_shift_primitive_orbits':full,'graph_primitive_orbits':graph})
# Exhaustive word check through period 8: a label fixes arrival vertex.
# edges: source, label, target
edges=[(0,1,0),(0,2,0),(0,3,1),(1,1,0),(1,3,1),(1,4,1),(1,5,1)]
for n in range(1,9):
 seen={}
 for origin in [0,1]:
  partial=[(origin,())]
  for _ in range(n):
   partial=[(target,word+(label,)) for state,word in partial for source,label,target in edges if source==state]
  for end,word in partial:
   if end==origin:seen[word]=seen.get(word,0)+1
 assert len(seen)==trace[n] and all(v==1 for v in seen.values())
result={'curve':'smooth projective elliptic curve y^2=x^3-x over F_5','curve_counts':curves,'curve_numerator':'1+2t+5t^2','curve_frobenius_eigenvalues':'-1+2i, -1-2i; squared absolute values exactly 5','formal_zeta':'(1-5t+5t^2)/((1-t)(1-5t))','formal_eigenvalues':'(5+sqrt(5))/2, (5-sqrt(5))/2; off modulus sqrt(5)','formal_euler_exponents':formal,'finite_checks':'n<=80 Euler integrality/nonnegativity; cyclic label injection exhaustively checked for n<=8','proof_limit':'Finite checks do not prove all n. The all-n labeled graph proof is given in frontiers/geometry_round2.md.'}
path=ROOT/'experiments/results/geometry_round2_exact.json';path.write_text(json.dumps(result,indent=2))
print(json.dumps({'curve_counts':curves,'formal_first_ten':formal[:10],'checks':'passed'},indent=2))
