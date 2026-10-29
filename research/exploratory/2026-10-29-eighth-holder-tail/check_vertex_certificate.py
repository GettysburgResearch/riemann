"""Exact LP certificate for the two fixed-cube-cutoff applications.

The tail is the supremum over all cube scales, not merely its value at the
cutoff.  For each A8/source-T2/Theta6 face, maximize a hypograph variable
subject to both the source and trivial T2 bounds.  Every inequality and
vertex is rational; infeasible and singular vertices are discarded. Dropping
the nonempty-support constraint enlarges the domain. In that larger domain
all physical short and tail exponents increase with b: their minimum slope
is -1/6 + 1/8 + 1/2 = 11/24, and max/min preserve this lower slope. Thus the
endpoint b values certify the whole increment with b >= 89/100. The cutoff
is c = 1/12 + d/15 - g*3/20.
"""
import sympy as s
import itertools, time
from fractions import Fraction
D,K,G,Q,T=s.symbols('d k g q t'); vv=[D,K,G,Q,T]; b,C=s.symbols('b C'); z=s.Rational(6,5)-D-G;Z=z-3*Q
pre=s.Rational(1,30)+2*D/3-5*K/6-b/6
A=[b+4*Q,b/2+8*Q];U=[b+K,2*b+3*K+G-z+3*Q];TF=[b,2*Z,5*b/6+2*Z/3,b/3+5*Z/3]
cutoff=s.Rational(1,12)+D/15-3*G/20
base=[-D,-K,-G,K-D,D+G+s.Rational(6,5)*K-C,cutoff-Q,Q-z/3]
cases = [
 (s.Rational(7,50),s.Rational(277,300),s.Rational(21,20),s.Rational(9337,9000)),
 (s.Rational(1925877,15625000),s.Rational(88917107,93750000),s.Rational(19949123,18750000),s.Rational(2959410557,2812500000)),
]
for cv,bv,expected_tail,expected_short in cases:
 subs={b:bv,C:cv};results=[]
 for i,j,l in itertools.product(range(2),range(2),range(4)):
  e=pre-2*Q+A[i]/4+TF[l]/4
  cs=[x.subs(subs) for x in base]+[(T-e-U[j]/2).subs(subs),(T-e-(b+Z)/2).subs(subs)]
  mx=None;pt=None
  for ids in itertools.combinations(range(len(cs)),5):
   mat, rhs=s.linear_eq_to_matrix([cs[jj] for jj in ids],vv)
   if mat.det()==0:continue
   sol=mat.inv()*rhs; env=dict(zip(vv,sol))
   if all(x.subs(env)<=0 for x in cs):
    if mx is None or sol[-1]>mx:mx=sol[-1];pt=sol
  results.append((mx,i,j,l,pt))
 m=max(results,key=lambda a:a[0]);print('C,b=',cv,bv,'max=',m, 'float',float(m[0]));
 assert m[0] == expected_tail
 # short endpoint (BK or S), maximize polytope using these 4 vertices
 points=[{D:0,K:0,G:0},{D:cv,K:0,G:0},{D:0,K:0,G:cv},{D:cv/(1+s.Rational(6,5)),K:cv/(1+s.Rational(6,5)),G:0}]
 short_maxima=[]
 for j in range(2):
  vals=[s.factor((pre+U[j]).subs(subs).subs(Q,cutoff).subs(p)) for p in points]
  print('short',j,max(vals),float(max(vals)))
  short_maxima.append(max(vals))
 assert max(short_maxima) == expected_short
 # For b >= 89/100, the lower bound c >= 1/12+d/30-g/6 and
 # d+g <= C give log_Y N(e) < 3c throughout the core.
 guard=s.factor((s.Rational(1,10)+s.Rational(89,100)-s.Rational(17,5)*cv)/6)
 print('uniform e guard=',guard)
 assert guard > 0
 assert s.Rational(1,12)-3*cv/20 > 0
 assert s.Rational(19,60)-2*cv/5 > 0
