"""Exact rational dual certificates for the two source-qualified endpoint bounds.
HiGHS proposes multipliers; all inequalities and dual identities are
verified exactly after rational reconstruction. Floating primal points are
diagnostic only. The b monotonicity reduction is in README.md.
"""
import sympy as s,itertools
from fractions import Fraction
from scipy.optimize import linprog
d,k,g,z,t=s.symbols('d k g z t'); vv=[d,k,g,z,t];b,C=s.symbols('b C'); D=s.Rational(6,5)-d-g;p=s.Rational(1,30)+2*d/3-5*k/6-b/6
src=[b+k,2*b+3*k+g-z]; tf=[b,z,5*b/6+z/3,b/3+5*z/6]; base=[-d,-k,-g,k-d,d+g+s.Rational(6,5)*k-C,-z,z-D]
for cv,bv in [(s.Rational(7,50),s.Rational(554,575)),(s.Rational(1925877,15625000),s.Rational(88917107,89843750))]:
 out=[]
 for a,h in itertools.product(range(2),range(4)):
  cs=[s.expand(x.subs({C:cv,b:bv})) for x in base+[t-p-src[a],t-p-tf[h]]];zero={v:0 for v in vv}; AA=s.Matrix([[x.coeff(v) for v in vv] for x in cs]);bb=s.Matrix([-x.subs(zero) for x in cs]);r=linprog([0,0,0,0,-1],A_ub=[[float(q) for q in AA.row(i)] for i in range(AA.rows)],b_ub=[float(q) for q in bb],bounds=[(None,None)]*5,method='highs');assert r.success;lam=s.Matrix([s.Rational(str(Fraction(-q).limit_denominator(10**7))) for q in r.ineqlin.marginals]);assert all(q>=0 for q in lam);assert AA.T*lam==s.Matrix([0,0,0,0,1]);out.append(((bb.T*lam)[0],a,h,r.x))
 result=max(out,key=lambda x:x[0]); target=s.Rational(21,20) if cv==s.Rational(7,50) else s.Rational(19949123,18750000)
 assert result[0] == target
 print(cv,bv,result)
