#!/usr/bin/env python3
"""Directed Decimal interval enclosure of a finite Li-type prefix.

Analytic family X_a(s)=cosh(s-1/2)+cosh(a), a=1/100.
All transcendental input intervals use exact positive Taylor sums and rational
geometric tail bounds. No floating-point differentiation or uncaptured tail.
"""
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING
from fractions import Fraction as Q
from math import factorial,comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
PREC=180;N=100;TERMS=80
DOWN=Context(prec=PREC,rounding=ROUND_FLOOR)
UP=Context(prec=PREC,rounding=ROUND_CEILING)
def decfrac(q,ctx):return ctx.divide(Decimal(q.numerator),Decimal(q.denominator))
class IV:
 __slots__=('lo','hi')
 def __init__(self,x=0,hi=None):
  if hi is not None:self.lo,self.hi=x,hi
  elif isinstance(x,IV):self.lo,self.hi=x.lo,x.hi
  else:
   q=Q(x);self.lo,self.hi=decfrac(q,DOWN),decfrac(q,UP)
  assert self.lo<=self.hi
 def __add__(a,b):
  b=IV(b);return IV(DOWN.add(a.lo,b.lo),UP.add(a.hi,b.hi))
 __radd__=__add__
 def __neg__(a):return IV(a.hi.copy_negate(),a.lo.copy_negate())
 def __sub__(a,b):return a+-IV(b)
 def __rsub__(a,b):return IV(b)+-a
 def __mul__(a,b):
  b=IV(b);pairs=[(x,y) for x in [a.lo,a.hi] for y in [b.lo,b.hi]]
  return IV(min(DOWN.multiply(x,y) for x,y in pairs),max(UP.multiply(x,y) for x,y in pairs))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=IV(b);assert b.lo>0 or b.hi<0
  recip=IV(DOWN.divide(Decimal(1),b.hi),UP.divide(Decimal(1),b.lo))
  return a*recip
 def obj(a):return {'lower':str(a.lo),'upper':str(a.hi)}

def hyperbolic_bound(x,odd=False):
 """Sum k=0..TERMS and bound all later positive terms geometrically."""
 off=1 if odd else 0
 partial=sum((x**(2*k+off)/factorial(2*k+off) for k in range(TERMS+1)),Q(0))
 degree=2*(TERMS+1)+off
 nextterm=x**degree/factorial(degree)
 ratio=x*x/((degree+1)*(degree+2))
 assert 0<=ratio<1
 tail=nextterm/(1-ratio)
 return IV(decfrac(partial,DOWN),decfrac(partial+tail,UP)),{'partial_terms':TERMS+1,'next_degree':degree,'tail_upper_rational':str(tail)}

A=Q(1,100)
ch_half,bc=hyperbolic_bound(Q(1,2));sh_half,bs=hyperbolic_bound(Q(1,2),True)
ch_a,ba=hyperbolic_bound(A)
q=[ch_half+ch_a]+[(ch_half if k%2==0 else sh_half)/factorial(k) for k in range(1,N+1)]
c=[IV(0)]
for n in range(1,N+1):
 correction=sum((k*c[k]*q[n-k] for k in range(1,n)),IV(0))/(n*q[0])
 c.append(q[n]/q[0]-correction)
li=[]
for n in range(1,N+1):
 value=n*sum((comb(n-1,k-1)*c[k] for k in range(1,n+1)),IV(0))
 assert value.lo>0,(n,value.obj())
 li.append({'n':n,**value.obj()})
# log C >= (C-1)/C for C>=1, and log C <= C-1.
# This gives a rigorous positive interval for the exact heat threshold.
tau_lo=((ch_a-1)/ch_a).lo;tau_hi=(ch_a-1).hi
assert tau_lo>0
# The elementary inequality behind the classification lower bound:
# log(1+y)-y+y²/2 has derivative y²/(1+y)>=0, y>=0 (proved in report).
result={'family':'X_a(s)=cosh(s-1/2)+cosh(a)','a_exact':str(A),'prefix_length':N,'decimal_precision':PREC,'rounding':'Every basic interval operation uses Decimal Context ROUND_FLOOR/ROUND_CEILING; exact Fraction Taylor input bounds.','cosh_half':ch_half.obj(),'sinh_half':sh_half.obj(),'cosh_a':ch_a.obj(),'Taylor_tail_evidence':{'cosh_half':bc,'sinh_half':bs,'cosh_a':ba},'recurrence':'q0=cosh(1/2)+cosh(a); qn=(cosh(1/2) if n even else sinh(1/2))/n!; c_n=q_n/q0-sum(k*c_k*q_(n-k),k<n)/(n*q0); lambda_n=n*sum(binomial(n-1,k-1)*c_k,k=1..n).','li_intervals':li,'all_lower_bounds_strictly_positive':True,'atomic_heat_threshold':{'exact':'log(cosh(1/100))','lower':str(tau_lo),'upper':str(tau_hi),'bound_used':'(C-1)/C <= log C <= C-1, C=cosh(a)>1'},'proof_scope':'Finite analytic Taylor-interval enclosure only; no all-n conclusion and no Riemann-xi assertion. Smoothing/source-class and sharpness proofs are analytic in audits/heatflow_round2.md.','independent_review':'Interval recurrence/tail arithmetic awaits independent adversarial review.'}
path=ROOT/'experiments/results/heatflow_round2.json';path.write_text(json.dumps(result,indent=2))
print(json.dumps({'a':str(A),'certified_prefix':N,'positive_interval_lower_min':str(min(Decimal(row['lower']) for row in li)),'atomic_threshold_positive_interval':result['atomic_heat_threshold'],'result_file':str(path)},indent=2))
