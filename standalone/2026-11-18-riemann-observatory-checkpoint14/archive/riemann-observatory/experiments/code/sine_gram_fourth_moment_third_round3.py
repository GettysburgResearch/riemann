"""Exact coincidence/permutation accounting and Fourier-polynomial integrals.
This checks finite algebra/combinatorics; DPP/Fourier/DCT proof is in the audit.
No stochastic simulation, numerical quadrature, arithmetic moment claim, or build.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb
from pathlib import Path
import json
B=Path(__file__).resolve().parents[2]
def conv(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def integrate(p,l=F(0),r=F(1)):
 return sum((a*(r**(i+1)-l**(i+1))/F(i+1) for i,a in enumerate(p)),F(0))
def power_poly(n):return [F((-1)**j*comb(n,j)) for j in range(n+1)]
I2=F(1);I4=2*integrate(power_poly(2));J=2*integrate(power_poly(3));U=2*integrate(power_poly(4));L=2*integrate(conv([F(3,4),0,-1],[F(3,4),0,-1]),r=F(1,2));I6=L+F(1,2)*integrate([0,0,0,0,1]);V=2*integrate([0,0,0,1,-F(1,3)])
assert(I4,I6,J,L,U,V)==(F(2,3),F(11,20),F(1,2),F(9,20),F(2,5),F(11,30))
def partitions(n):
 def go(a,maximum):
  if len(a)==n:yield tuple(a);return
  for v in range(maximum+2):yield from go(a+[v],max(maximum,v))
 yield from go([0],0)
def edge_word(word):
 out={}
 for a,b in zip(word,word[1:]+word[:1]):
  if a!=b:e=tuple(sorted([a,b]));out[e]=out.get(e,0)+1
 return out
counts={3:{},4:{}};partition_rows=[]
for m in [3,4]:
 for word in partitions(m):
  l=max(word)+1;edges=edge_word(word);powers=sorted(edges.values())
  if l==1:tag='single'
  elif l==2:tag='two_k'+str(powers[0])
  elif l==3:tag='triangle' if powers==[1,1,1] else 'double_spoke'
  else:tag='four_cycle'
  counts[m][tag]=counts[m].get(tag,0)+1;partition_rows.append({'m':m,'canonical_partition_word':list(word),'tag':tag})
assert counts[3]=={'single':1,'two_k2':3,'triangle':1}
assert counts[4]=={'single':1,'two_k2':6,'triangle':4,'two_k4':1,'double_spoke':2,'four_cycle':1}
base={(0,1),(1,2),(2,3),(0,3)}
def cycles(p):
 seen=set();out=[]
 for i in range(len(p)):
  if i not in seen:
   cyc=[];j=i
   while j not in seen:seen.add(j);cyc.append(j);j=p[j]
   out.append(cyc)
 return out
rows=[];sums={}
for p in permutations(range(4)):
 cs=cycles(p);kind=sorted(map(len,cs));sign=(-1)**(4-len(cs))
 if kind==[1,1,1,1]:tag='identity';value=I2
 elif kind==[1,1,2]:tag='single_transposition';value=I4
 elif kind==[2,2]:
  matching={tuple(sorted(c)) for c in cs};tag='double_adjacent' if matching<=base else 'K4_doubled_matching';value=L if matching<=base else V
 elif kind==[1,3]:tag='three_cycle';value=J
 else:
  edges={tuple(sorted([i,p[i]])) for i in range(4)};tag='four_cycle_same' if edges==base else 'K4_doubled_matching';value=U if edges==base else V
 rows.append({'permutation':[x+1 for x in p],'cycle_type':kind,'sign':sign,'graph_integral_class':tag,'integral':str(value),'signed_contribution':str(sign*value)})
 if tag not in sums:sums[tag]={'count':0,'signed_count':0,'integral':str(value)}
 sums[tag]['count']+=1;sums[tag]['signed_count']+=sign
C=sum((F(row['signed_contribution']) for row in rows),F(0));assert C==0
A=1-3*I4+2*J;Bstar=1-2*I4-J+2*L;third=1+3*(I2-I4)+A;fourth=1+6*(I2-I4)+(I4-I6)+4*A+2*Bstar+C
assert(A,Bstar,third,fourth)==(F(0),F(1,15),F(2),F(13,4))
out={'kind':'exact_DPP_coincidence_and_determinant_combinatorics_with_polynomial_integrals','normalization':'(1/R) expectation Tr G_R^j, not expectation of normalization by random N_R','partition_counts':counts,'kernel_integrals':{k:str(v) for k,v in {'I2':I2,'I4':I4,'I6':I6,'triangle_squared_J':J,'triangle_31_L':L,'four_cycle_squared_U':U,'K4_doubled_matching_V':V}.items()},'fourth_determinant_classes':sums,'third_all_distinct_cycle':str(A),'fourth_three_vertex_double_spoke':str(Bstar),'fourth_all_distinct_cycle':str(C),'third_moment_limit':str(third),'fourth_moment_limit':str(fourth),'partition_records':partition_rows,'all24_fourth_permutations':rows,'scope':'Exact finite accounting/integral algebra only; Fourier reductions and dominated limits are analytically justified in the independent audit. Not prime-side moment matching.'}
(B/'experiments/results/sine_gram_fourth_moment_third_round3.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['partition_records','all24_fourth_permutations']},indent=2))
