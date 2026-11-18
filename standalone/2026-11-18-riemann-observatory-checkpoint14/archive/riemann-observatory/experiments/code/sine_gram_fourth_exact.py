"""Exact DPP coincidence/permutation bookkeeping for sine-Gram moments1..4.
Analytic diagram integrals/limit justification are proved in the companion note.
No prime-side zeta asymptotic or numerical integration is used.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations
from collections import defaultdict
import json,math
B=Path(__file__).resolve().parents[2]
def canon(n,edges):
 pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
 weights=defaultdict(int)
 for a,b,m in edges:
  if a!=b:weights[tuple(sorted((a,b)))]+=m
 return min(tuple(weights[tuple(sorted((p[i],p[j])))] for i,j in pairs) for p in permutations(range(n)))
def cyc(powers):return [(i,(i+1)%len(powers),v) for i,v in enumerate(powers)]
values={}
def register(n,edges,val,name):
 key=(n,canon(n,edges))
 if key in values:assert values[key][0]==val
 values[key]=(val,name)
register(1,[],F(1),'single vertex')
for r,v in [(2,F(1)),(4,F(2,3)),(6,F(11,20))]:register(2,[(0,1,r)],v,f'k^{r}')
for a,b,c,v,name in [(1,1,1,F(1),'triangle111'),(3,1,1,F(2,3),'triangle311'),(2,2,2,F(1,2),'triangle222'),(3,3,1,F(9,20),'triangle331')]:register(3,[(0,1,a),(1,2,b),(2,0,c)],v,name)
register(3,[(0,1,2),(0,2,2)],F(1),'double-edge star22')
register(3,[(0,1,4),(0,2,2)],F(2,3),'double-edge star42')
register(4,cyc([1,1,1,1]),F(1),'cycle1111')
register(4,cyc([3,1,1,1]),F(2,3),'cycle3111')
register(4,cyc([1,1,1,1])+[(0,2,2)],F(2,3),'cycle plus squared diagonal')
register(4,cyc([3,1,3,1]),F(9,20),'cycle3131')
register(4,cyc([1,1,1,1])+[(0,2,2),(1,3,2)],F(11,30),'K4 opposite edges doubled')
register(4,cyc([1,1,1,1])+[(0,1,1),(1,2,1),(2,0,1)],F(1,2),'cycle plus triangle')
register(4,cyc([2,2,2,2]),F(2,5),'cycle2222')
def partitions(m):
 def grow(a):
  if len(a)==m:yield tuple(a);return
  for j in range(max(a)+2):yield from grow(a+[j])
 yield from grow([0])
all_results={}
for m in range(1,5):
 acc=defaultdict(int);by_l=defaultdict(lambda:F(0));nparts=0
 for word in partitions(m):
  nparts+=1;n=1+max(word);trace=[(word[i],word[(i+1)%m],1) for i in range(m)]
  for p in permutations(range(n)):
   sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));edges=trace+[(i,p[i],1) for i in range(n)];key=(n,canon(n,edges));assert key in values,(m,word,p,key)
   acc[key]+=sign;by_l[n]+=sign*values[key][0]
 total=sum(by_l.values(),F(0));assert total==[None,F(1),F(4,3),F(2),F(13,4)][m]
 all_results[m]={'set_partitions':nparts,'moment':str(total),'contributions_by_distinct_vertices':{str(k):str(v) for k,v in sorted(by_l.items())},'diagram_table':[{'vertices':key[0],'canonical_edge_multiplicities':list(key[1]),'name':values[key][1],'signed_coefficient':coef,'integral':str(values[key][0]),'contribution':str(coef*values[key][0])} for key,coef in sorted(acc.items())]}
# Independently integrate the single nontrivial K4 diamond polynomial by monomials:
# ∫_{a,b>=0,a+b<=1} a^i b^j da db=i!j!/(i+j+2)!.
poly={(0,0):F(1)}
for fac in [{(0,0):F(1),(1,0):F(-1)},{(0,0):F(1),(0,1):F(-1)},{(0,0):F(1),(1,0):F(-1),(0,1):F(-1)}]:
 out=defaultdict(lambda:F(0))
 for (i,j),v in poly.items():
  for (r,s),w in fac.items():out[i+r,j+s]+=v*w
 poly=dict(out)
diamond=4*sum(v*F(math.factorial(i)*math.factorial(j),math.factorial(i+j+2)) for (i,j),v in poly.items());assert diamond==F(11,30)
out={'kind':'exact_combinatorial_and_polynomial_integral_check_NOT_prime_asymptotics','moments':all_results,'K4_diamond_integral':str(diamond),'input_assumptions':'Stationary unit-intensity sine DPP correlation densities det[k(xi-xj)], k=sinc; analytic diagram identities and dominated-limit proof separate.','scope':'Exact partition/permutation coefficients and one rational polynomial integral; this script alone is not the full analytic proof.'}
(B/'experiments/results/sine_gram_fourth_exact.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'moments':{k:v['moment'] for k,v in all_results.items()},'fourth_contributions':all_results[4]['contributions_by_distinct_vertices'],'K4_integral':str(diamond)},indent=2))
