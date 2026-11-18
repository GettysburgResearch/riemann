"""Exact first-four sine-Gram model moment calculation.

Analytic graph-integrability and Fourier identities are in the accompanying
review. This script performs only exact finite combinatorics and rational
integrals, not a simulation of zeta zeros or the sine process.
"""
from fractions import Fraction as F
from itertools import permutations
from collections import Counter
from pathlib import Path
import json


def conv(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c


def integral(p,a,b):
 return sum((x*(b**(j+1)-a**(j+1))/F(j+1) for j,x in enumerate(p)),F(0))


def edge(i,j):return tuple(sorted((i,j)))

def graph_base_and_perm(p):
 g=Counter(edge(i,(i+1)%4) for i in range(4))
 for i,j in enumerate(p):
  if i!=j:g[edge(i,j)]+=1
 return g


def canonical(g,n=4):
 return min(tuple(sorted((edge(p[i],p[j]),c) for (i,j),c in g.items())) for p in permutations(range(n)))


def cycle_type(p):
 seen=set();lengths=[]
 for x in range(len(p)):
  if x not in seen:
   j=x;ell=0
   while j not in seen:seen.add(j);ell+=1;j=p[j]
   lengths.append(ell)
 return tuple(sorted(lengths,reverse=True))


def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def partitions(n):
 def rec(a):
  if len(a)==n:yield tuple(a);return
  for x in range(max(a)+2):yield from rec(a+[x])
 yield from rec([0])


def main():
 central=[F(3,4),F(0),-F(1)]
 H=2*integral(conv(central,central),F(0),F(1,2))
 outer=conv([F(3,2),-F(1)],[F(3,2),-F(1)])
 outer=[x/2 for x in outer]
 k6=H+2*integral(conv(outer,outer),F(1,2),F(3,2))
 k2=F(1);k4=F(2,3);J3=F(1,2);J4=F(2,5)
 crossing=2*integral([0,0,0,1,-F(1,3)],F(0),F(1))
 assert H==F(9,20) and k6==F(11,20) and crossing==F(11,30)
 triangle=1-3*k4+2*J3
 star=1-2*k4-J3+2*H
 assert triangle==0 and star==F(1,15)
 cross_graph=canonical(graph_base_and_perm((2,3,0,1))) # (13)(24)
 rows=[];classes=Counter();signed=F(0)
 for p in permutations(range(4)):
  typ=cycle_type(p);g=graph_base_and_perm(p);sgn=parity(p)
  if typ==(1,1,1,1):label='identity';I=F(1)
  elif typ==(2,1,1):label='transposition';I=k4
  elif typ==(3,1):label='three_cycle';I=J3
  elif typ==(2,2):
   if max(g.values())==3:label='noncross_double_transposition';I=H
   else:
    label='cross_double_transposition';I=crossing
    assert canonical(g)==cross_graph
  elif typ==(4,):
   if len(g)==4 and all(v==2 for v in g.values()):label='base_or_reverse_four_cycle';I=J4
   else:
    label='mixed_four_cycle';I=crossing
    assert canonical(g)==cross_graph
  else:raise AssertionError(typ)
  classes[label]+=1;signed+=sgn*I
  rows.append({'permutation_1based':[x+1 for x in p],'cycle_type':typ,'class':label,'sign':sgn,'integral':str(I)})
 assert classes==Counter(identity=1,transposition=6,three_cycle=8,noncross_double_transposition=2,cross_double_transposition=1,base_or_reverse_four_cycle=2,mixed_four_cycle=4)
 assert signed==0
 parts=[];counts=Counter();total=F(0)
 for a in partitions(4):
  v=max(a)+1;g=Counter(edge(a[i],a[(i+1)%4]) for i in range(4) if a[i]!=a[(i+1)%4])
  if v==1:label='all_equal';value=F(1)
  elif v==2:
   degree=sum(g.values())
   if degree==2:label='two_points_non_alternating';value=k2-k4
   elif degree==4:label='two_points_alternating';value=k4-k6
   else:raise AssertionError(a)
  elif v==3:
   if len(g)==3:label='three_points_adjacent_repeat';value=triangle
   else:label='three_points_opposite_repeat';value=star;assert len(g)==2 and set(g.values())=={2}
  else:label='all_distinct';value=signed
  counts[label]+=1;total+=value
  parts.append({'restricted_growth_partition':a,'class':label,'contribution':str(value)})
 assert len(parts)==15
 assert counts==Counter(all_equal=1,two_points_non_alternating=6,two_points_alternating=1,three_points_adjacent_repeat=4,three_points_opposite_repeat=2,all_distinct=1)
 assert total==F(13,4)
 m3=1+3*(k2-k4)+triangle
 assert m3==2
 result={'arithmetic':'exact Fraction and finite permutation/set-partition enumeration','normalization':'k(t)=sin(pi*t)/(pi*t), unit density, per lengthR','integrals':{'k2':str(k2),'k4':str(k4),'k6':str(k6),'triangle_squared_cycle':str(J3),'four_squared_cycle':str(J4),'noncross_double':str(H),'cross_double':str(crossing),'rho3_triangle':str(triangle),'rho3_star':str(star)},'determinant_classes':dict(classes),'permutation_terms':rows,'all_distinct_four_cycle':str(signed),'trace_partition_classes':dict(counts),'trace_partitions':parts,'moments':['1','4/3',str(m3),str(total)],'D_84m3_minus16m4':str(84*m3-16*total),'scope':'Random sine-Gram model only. No arithmetic prime-side higher-moment asymptotic or RH claim.'}
 dest=Path(__file__).resolve().parents[1]/'results/sine_gram_fourth_exact_advocate_round3.json';dest.write_text(json.dumps(result,indent=2)+'\n')
 print('Exact Fourier polynomial integrals,24 permutation classes,4 mixed-cycle graph isomorphisms,15 trace partitions, A4=0 andm4=13/4 passed.')

if __name__=='__main__':main()
