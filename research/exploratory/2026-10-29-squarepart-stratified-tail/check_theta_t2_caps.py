"""Rational dual LP certificate with both direct theta T2 caps.

The solver proposes multipliers; their nonnegativity and exact rational
A.T*lambda=objective identities are checked before each bound is accepted.
This older conservative calculation retains the original short-cube bound.
The 256 programs cover both prefix faces, both prop:R faces and all direct
Theta6 second- and fourth-moment faces over the full square-part core.
"""
import sympy as s,itertools,time
from fractions import Fraction
from scipy.optimize import linprog
D,K,G,U,Q,T=s.symbols('d k g u q t');vv=[D,K,G,U,Q,T];b,C=s.symbols('b C');z=s.Rational(6,5)-D-G;Z=z-3*Q;M=b-U;W=b-2*U
pre=s.Rational(1,30)+2*D/3-5*K/6-b/6
A=[M+6*Q,U+12*Q];U2=[b+K,2*b+3*K+G-z+3*Q]
def th(r,x):return [r,x,5*r/6+x/3,r/3+5*x/6]
TF=th(b,2*Z);QB=th(b,Z);QV=[U+x for x in th(W,Z)]
cut=s.Rational(1,16)+D/10-G/10
base=[-D,-K,-G,-U,U-b/2,K-D,D+G+s.Rational(6,5)*K-C,cut-Q,Q-z/3]
cases = [
 (s.Rational(7,50),s.Rational(19,20),s.Rational(39163,37440),s.Rational(6227,6000)),
 (s.Rational(1925877,15625000),s.Rational(39,40),s.Rational(5305,4992),s.Rational(492532993,468750000)),
]
for cv,bv,expected_tail,expected_short in cases:
 subs={b:bv,C:cv};results=[]
 for a,j,l,m,n in itertools.product(range(2),range(2),range(4),range(4),range(4)):
  e=pre-2*Q+A[a]/6+TF[l]/6
  con=[T-e-2*U2[j]/3,T-e-2*(M+Z)/3,T-e-(M+TF[l])/3,T-e-2*QB[m]/3,T-e-2*QV[n]/3]
  cs=[s.expand(x.subs(subs)) for x in base+con];zero={x:0 for x in vv}
  AA=s.Matrix([[x.coeff(v) for v in vv] for x in cs]);rhs=s.Matrix([-x.subs(zero) for x in cs]);obj=[0,0,0,0,0,1]
  r=linprog([0,0,0,0,0,-1],A_ub=[[float(a) for a in AA.row(i)] for i in range(AA.rows)],b_ub=[float(x) for x in rhs],bounds=[(None,None)]*6,method='highs')
  if not r.success:raise Exception((a,j,l,m,n,r.message))
  lam=s.Matrix([s.Rational(str(Fraction(-x).limit_denominator(10000000))) for x in r.ineqlin.marginals]);assert all(x>=0 for x in lam);assert AA.T*lam==s.Matrix(obj)
  bound=(rhs.T*lam)[0];results.append((bound,(a,j,l,m,n),r.x))
 Mmax=max(results,key=lambda x:x[0]);print('case=',cv,bv,'tailmax=',Mmax,'value',float(Mmax[0]),flush=True)
 assert Mmax[0] == expected_tail
 points=[{D:0,K:0,G:0},{D:cv,K:0,G:0},{D:0,K:0,G:cv},{D:cv/(1+s.Rational(6,5)),K:cv/(1+s.Rational(6,5)),G:0}]
 short_maxima=[]
 for j in range(2):
  vals=[s.factor((pre+U2[j]).subs(subs).subs(Q,cut.subs(subs)).subs(p)) for p in points];print('short',j,max(vals),float(max(vals)),flush=True)
  short_maxima.append(max(vals))
 assert max(short_maxima)==expected_short
 # b >= 23/25 suffices to put every e in the rescaling regime.
 guard=s.factor((s.Rational(23,25)-s.Rational(11,40)-s.Rational(11,5)*cv)/6)
 assert guard > 0
 assert s.Rational(1,16)-cv/10 > 0
 assert s.Rational(27,80)-13*cv/30 > 0
