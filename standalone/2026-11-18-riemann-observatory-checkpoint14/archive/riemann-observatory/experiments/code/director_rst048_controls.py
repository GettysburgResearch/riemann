#!/usr/bin/env python3
"""Independent exact local controls for RST048v2, not an infinite proof.

Run from any directory with Python3 and SymPy. No source supplement is used.
"""
import json, math
from fractions import Fraction as F
from pathlib import Path
import sympy as s

u,v=s.symbols('u v',real=True)
b=s.Rational(1,4)
def integral_poly(poly,lo,hi):
 p=s.Poly(s.expand(poly),u)
 return s.cancel(sum(c*(hi**(n[0]+1)-lo**(n[0]+1))/(n[0]+1) for n,c in p.terms()))

checks=[]
for k in range(1,9):
 if k==1:
  w=1-u
 else:
  Q=sum(s.binomial(2*k-2,h)*v**h*(1-v)**(2*k-2-h) for h in range(k))
  w=s.expand((1-u)*Q.subs(v,(u-b)/(1-b)))
  for j in range(k):
   assert s.diff(w-(1-u),u,j).subs(u,b)==0
 for j in range(k):assert s.diff(w,u,j).subs(u,1)==0
 for m in range(1,k+1):
  f=u**(m-1)*w/s.factorial(m-1)
  g=s.diff(f,u,m)
  ghead=-m
  energy=integral_poly(ghead**2,s.S.Zero,b)+integral_poly(g*g,b,s.S.One)
  assert energy>=m*m
  for j in range(m):
   leg=s.legendre(j,2*u-1)
   moment=integral_poly(ghead*leg,s.S.Zero,b)+integral_poly(g*leg,b,s.S.One)
   assert s.simplify(moment-(-1)**(j+1))==0
  checks.append({'k':k,'m':m,'delayed_energy':str(energy)})
for m in range(1,13):
 g=s.diff(u**(m-1)*(1-u)**m/s.factorial(m-1),u,m)
 assert integral_poly(g*g,s.S.Zero,s.S.One)==m*m

D=e=F(1,10000);delta=F(1,1000000);a=F(1,20);bf=F(1,4);c=F(3,20)
exponents={
 'collective_low':(4+2*e)*a-2*bf*(1-delta)+c*(1+2*e),
 'collective_high':(2+2*e)*a+2*delta+c*(-1+2*e),
 'high_strip_slowest':2*delta+a*(-1+4*e),
 'anchor':(1+e)*a-bf*(F(1,2)-delta)}
assert all(x<0 for x in exponents.values())
assert 2*float(D)+5*float(e)+2*float(D)*math.log(1200)<.01
assert 2*(2*float(e)+float(D)*math.log(200))+2*float(e)<.01
out={'status':'PASS_exact_finite_controls','scope':'36 delayed-profile energies and matching Legendre moments;12 optimal local energies; exact rational cutoff exponents. Not verification of infinite analytic estimates or RH.','sympy_version':s.__version__,'delayed_cases':checks,'optimal_energy_cases':12,'cutoff_exponents':{k:{'rational':str(x),'decimal':float(x)} for k,x in exponents.items()}}
path=Path(__file__).resolve().parents[1]/'results/director_rst048_controls.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'delayed_cases':len(checks),'optimal_cases':12,'exponents':out['cutoff_exponents']}))
