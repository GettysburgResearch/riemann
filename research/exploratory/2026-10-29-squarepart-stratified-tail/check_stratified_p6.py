"""Exact rational dual and primal certificates for the stratified p=6 tail.

HiGHS proposes dual multipliers; the program rationalizes them, then checks
nonnegativity and every A.T*lambda=objective identity exactly. The matching
primal is verified exactly. Thus floating solver tolerances do not affect the
upper bounds. The 16 cases cover both A12 faces, both prop:R T2 faces, and
all four Theta6 T4 faces; each LP imposes both additional T2 alternatives.
No scale-wise mixture or T4 trivial cap is needed.

The physical domain has 0 <= u=log_Y V <= b/2, d,g,k>=0, k<=d,
d+g+6k/5<=C and c<=q<=Delta/3, with c=1/20+d/15-g/20. Dropping the
nonempty-support condition enlarges it. For fixed u all objective exponents
increase in b by at least 1/6, even on the Cauchy T2 branch, while the
available interval for u grows with b. The endpoint b therefore certifies
the entire interval from 23/25 to b_max.
"""
import sympy as s,itertools
from fractions import Fraction
from scipy.optimize import linprog
D,K,G,U,Q,T=s.symbols('d k g u q t'); vv=[D,K,G,U,Q,T]; b,C=s.symbols('b C'); z=s.Rational(6,5)-D-G;Z=z-3*Q;M=b-U
pre=s.Rational(1,30)+2*D/3-5*K/6-b/6
A=[M+6*Q,U+12*Q];U2=[b+K,2*b+3*K+G-z+3*Q];TF=[b,2*Z,5*b/6+2*Z/3,b/3+5*Z/3]
cut=s.Rational(1,20)+D/15-G/20
base=[-D,-K,-G,-U,U-b/2,K-D,D+G+s.Rational(6,5)*K-C,cut-Q,Q-z/3]
cases = [
 (s.Rational(7,50),s.Rational(4213,4450),s.Rational(21,20),s.Rational(21813,22250)),
 (s.Rational(1925877,15625000),s.Rational(1348218883,1390625000),s.Rational(19949123,18750000),s.Rational(13778849011,13906250000)),
]
for cv,bv,expected_tail,expected_short in cases:
 subs={b:bv,C:cv};results=[]
 for a,j,l in itertools.product(range(2),range(2),range(4)):
  e=pre-2*Q+A[a]/6+TF[l]/6
  con=[T-e-2*U2[j]/3,T-e-2*(M+Z)/3,T-e-(M+TF[l])/3]
  cs=[s.expand(x.subs(subs)) for x in base+con];zero={x:0 for x in vv}
  AA=s.Matrix([[x.coeff(v) for v in vv] for x in cs]);rhs=s.Matrix([-x.subs(zero) for x in cs]);obj=[0,0,0,0,0,1]
  r=linprog([0,0,0,0,0,-1],A_ub=[[float(a) for a in AA.row(i)] for i in range(AA.rows)],b_ub=[float(x) for x in rhs],bounds=[(None,None)]*6,method='highs')
  if not r.success:raise Exception((a,j,l,r.message))
  lam=s.Matrix([s.Rational(str(Fraction(-x).limit_denominator(10000000))) for x in r.ineqlin.marginals]);assert all(x>=0 for x in lam);assert AA.T*lam==s.Matrix(obj)
  bound=(rhs.T*lam)[0];results.append((bound,(a,j,l),r.x))
  if (a,j,l)==(0,1,3):
   qstar=s.factor((11*(s.Rational(6,5)-cv)-8*bv)/33)
   primal={D:cv,K:0,G:0,U:0,Q:qstar,T:expected_tail}
   assert all(x.subs(primal)<=0 for x in cs)
 m=max(results,key=lambda x:x[0]);print('case=',cv,bv,'tailmax=',m,'value',float(m[0]));
 assert m[0] == expected_tail
 points=[{D:0,K:0,G:0},{D:cv,K:0,G:0},{D:0,K:0,G:cv},{D:cv/(1+s.Rational(6,5)),K:cv/(1+s.Rational(6,5)),G:0}]
 short_maxima=[]
 for j in range(2):
  vals=[s.factor((pre+U2[j]).subs(subs).subs(Q,cut.subs(subs)).subs(p)) for p in points];print('short',j,max(vals),float(max(vals)))
  short_maxima.append(max(vals))
 assert max(short_maxima) == expected_short
 guard=s.factor((s.Rational(23,25)-s.Rational(1,2)-s.Rational(14,5)*cv)/6);print('e guard',guard);assert guard>0
 assert s.Rational(1,20)-cv/20>0
 assert s.Rational(7,20)-2*cv/5>0
