"""Exact rational dual certificates for the scale-wise p=4,5 tail.

Run with Python, scipy and sympy. HiGHS proposes nonnegative dual vectors;
each is rationalized and checked exactly against A.T*lambda = objective.
The resulting rational dual objective is therefore an unconditional upper
bound for each linear program, independent of numerical solver accuracy.
There are 2 A8 x 2 A10 x 2 source-T2 x 4 Theta6 choices. The constraints
impose the minimum with both trivial T2 and the Cauchy cap sqrt(B*T4).

The source domain has d,g,k>=0, k<=d, d+g+6k/5<=C and cube-log q between
c=1/20+d/15-g/20 and Delta/3. The proof drops the support condition, so
the endpoint b certifies all b down to 23/25 by monotonicity: after the
physical factor, even using the Cauchy cap the smallest b slope is 5/24
(p=4) or 7/30 (p=5). The cutoff was chosen so that every admissible mask
divisor e lies in the small-e rescaling regime throughout this interval.
"""
import sympy as s,itertools
from fractions import Fraction
from scipy.optimize import linprog
D,K,G,Q,T=s.symbols('d k g q t'); vv=[D,K,G,Q,T]; b,C=s.symbols('b C'); z=s.Rational(6,5)-D-G;Z=z-3*Q
pre=s.Rational(1,30)+2*D/3-5*K/6-b/6
A2=[b+4*Q,b/2+8*Q];A4=[b+5*Q,b/2+10*Q];U=[b+K,2*b+3*K+G-z+3*Q];TF=[b,2*Z,5*b/6+2*Z/3,b/3+5*Z/3]
cut=s.Rational(1,20)+D/15-G/20
base=[-D,-K,-G,K-D,D+G+s.Rational(6,5)*K-C,cut-Q,Q-z/3]
cases = [
 (s.Rational(7,50),s.Rational(10283,11000),s.Rational(21,20),s.Rational(1917,2000)),
 (s.Rational(1925877,15625000),s.Rational(3294802253,3437500000),s.Rational(19949123,18750000),s.Rational(606649567,625000000)),
]
for cv,bv,expected_tail,expected_short in cases:
 subs={b:bv,C:cv};results=[]
 for a2,a4,j,l in itertools.product(range(2),range(2),range(2),range(4)):
  e2=pre-2*Q+A2[a2]/4+TF[l]/4
  e4=pre-2*Q+A4[a4]/5+TF[l]/5
  con=[T-e2-U[j]/2,T-e2-(b+Z)/2,T-e2-(b+TF[l])/4,T-e4-3*U[j]/5,T-e4-3*(b+Z)/5,T-e4-3*(b+TF[l])/10]
  cs=[s.expand(x.subs(subs)) for x in base+con];zero={x:0 for x in vv}
  A=s.Matrix([[x.coeff(v) for v in vv] for x in cs]);rhs=s.Matrix([-x.subs(zero) for x in cs]);obj=[0,0,0,0,1]
  r=linprog([0,0,0,0,-1],A_ub=[[float(a) for a in A.row(i)] for i in range(A.rows)],b_ub=[float(x) for x in rhs],bounds=[(None,None)]*5,method='highs')
  if not r.success:raise Exception((a2,a4,j,l,r.message))
  lam=s.Matrix([s.Rational(str(Fraction(-x).limit_denominator(10000000))) for x in r.ineqlin.marginals]); assert all(x>=0 for x in lam); assert A.T*lam==s.Matrix(obj)
  bound=(rhs.T*lam)[0];results.append((bound,(a2,a4,j,l),r.x))
  # Also certify an exact matching primal point for the binding face.
  if (a2,a4,j,l)==(0,1,1,3):
   qstar=s.factor((11*(s.Rational(6,5)-cv)-2*bv)/93)
   primal={D:cv,K:0,G:0,Q:qstar,T:expected_tail}
   assert all(x.subs(primal)<=0 for x in cs)
 m=max(results,key=lambda x:x[0]);print('case=',cv,bv,'tailmax=',m,'value',float(m[0]));
 assert m[0] == expected_tail
 points=[{D:0,K:0,G:0},{D:cv,K:0,G:0},{D:0,K:0,G:cv},{D:cv/(1+s.Rational(6,5)),K:cv/(1+s.Rational(6,5)),G:0}]
 short_maxima=[]
 for j in range(2):
  vals=[s.factor((pre+U[j]).subs(subs).subs(Q,cut.subs(subs)).subs(p)) for p in points]
  print('short',j,max(vals),float(max(vals)))
  short_maxima.append(max(vals))
 assert max(short_maxima) == expected_short
 guard=s.factor((s.Rational(23,25)-s.Rational(1,2)-s.Rational(14,5)*cv)/6); print('e guard',guard); assert guard>0
 assert s.Rational(1,20)-cv/20 > 0
 assert s.Rational(7,20)-2*cv/5 > 0
