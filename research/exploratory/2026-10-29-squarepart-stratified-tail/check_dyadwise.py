"""Exact dual certificates for the cutoff-free dyadwise cubic-cap bound.

Run with scipy and sympy. HiGHS suggests dual multipliers; every multiplier
is rationalized and checked for nonnegativity, and A.T*lambda=objective is
checked in exact rational arithmetic. Thus only exact dual bounds are used.
There are 1,152 face programs per case. At every dyad they impose both the
weighted-Cauchy prop:R estimate and the p6/p10 Abel estimates; the latter
deliberately omit prop:R, so their T2 caps are invariant under mask-divisor
rescaling. The actual row sector and analytic source/profile matching remain
external inputs; this script verifies scalar inequalities.

The code includes b itself as an LP variable from 23/25 to each stated
endpoint and the cube log is allowed on the entire interval [0,Delta/3]. No
cutoff, e guard, or monotonicity assumption is needed.
"""
import sympy as s,itertools,sys
from fractions import Fraction
from scipy.optimize import linprog
D,K,G,U,Q,T=s.symbols('d k g u q t');b,C=s.symbols('b C');vv=[D,K,G,U,Q,b,T];z=s.Rational(6,5)-D-G;Z=z-3*Q;M=b-U;W=b-2*U
pre=s.Rational(1,30)+2*D/3-5*K/6-b/6
base=[-D,-K,-G,-U,U-b/2,K-D,D+G+s.Rational(6,5)*K-C,-Q,Q-z/3,s.Rational(23,25)-b]
def th6(r,x):return [r,x,5*r/6+x/3,r/3+5*x/6]
def th3(r,x):return [r,x,2*(r+x)/3]
R=[b+K,2*b+3*K+G-z+3*Q];S=th6(b,Z);Q2=[W+x for x in th3(U,Z)];Q4=[W+x for x in th3(U,2*Z)];S4=th6(b,2*Z);obj=s.Matrix([0,0,0,0,0,0,1]);zero={x:0 for x in vv}
cases=[
 (s.Rational(7,50),s.Rational(243,250),s.Rational(88157,84000),s.Rational(21,20)),
 (s.Rational(1925877,15625000),s.Rational(997,1000),s.Rational(5281635419,4968750000),s.Rational(19949123,18750000)),
]
for cv,bv,expected_tail,target in cases:
 subs={C:cv}; tailmax=(-s.oo,None)
 def check(cs):
  cc=[s.expand(x.subs(subs)) for x in cs];aa=s.Matrix([[x.coeff(v) for v in vv] for x in cc]);rhs=s.Matrix([-x.subs(zero) for x in cc]);
  r=linprog([0,0,0,0,0,0,-1],A_ub=[[float(v) for v in aa.row(i)] for i in range(aa.rows)],b_ub=[float(v) for v in rhs],bounds=[(None,None)]*7,method='highs')
  if r.status==2:raise RuntimeError("floating solver reported infeasible; exact Farkas certificate required")
  if not r.success:raise Exception(r.message)
  lam=s.Matrix([s.Rational(str(Fraction(-x).limit_denominator(10000000))) for x in r.ineqlin.marginals]); assert all(x>=0 for x in lam);assert aa.T*lam==obj
  return (rhs.T*lam)[0],r.x
 count=0
 for j,m,n,l,r,a6,a10 in itertools.product(range(2),range(4),range(3),range(4),range(3),range(2),range(2)):
  t2=[M+Z,S[m],Q2[n]];t4=[S4[l],Q4[r]]
  cs=base+[b-bv,T-pre-R[j],T-pre-(M+Z),T-pre-S[m],T-pre-Q2[n]]
  for p,a in [(6,a6),(10,a10)]:
   Ap=([M+p*Q,U+2*p*Q])[a];ep=pre-2*Q+Ap/p
   cs += [T-ep-(1-s.Rational(2,p))*x-y/p for x in t2 for y in t4]
  v=check(cs);count+=1
  if v and v[0]>tailmax[0]:tailmax=(v[0],(j,m,n,l,r,a6,a10,v[1]))
 print('dyadwise',cv,bv,tailmax,'count',count,flush=True)
 assert count==1152 and tailmax[0]==expected_tail and expected_tail<target
