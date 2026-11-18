#!/usr/bin/env python3
"""Independent third reconstruction via Laurent variable r=exp(2u).
Unlike the first certificate, derive all f derivatives using 2r d/dr, convert
r^j+r^-j by Chebyshev recurrence, then reconstruct every Bernstein polynomial.
Standard library/Fraction only. Does not use stored P2/P4 input coefficients.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import importlib.util,json
ROOT=Path(__file__).resolve().parents[2]

def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 q={}
 for p in ps:
  for k,v in p.items():q[k]=q.get(k,F())+v
 return clean(q)
def scale(p,s):return clean({k:v*s for k,v in p.items()})
def mul(p,q):
 d={}
 for a,v in p.items():
  for b,w in q.items():
   k=tuple(x+y for x,y in zip(a,b));d[k]=d.get(k,F())+v*w
 return clean(d)
def du(p):return clean({k:2*k[0]*v for k,v in p.items()})
# Coordinates r-power (possibly negative), c-power, h=T²-power.
one={(0,0,0):F(1)}
logfprime={(1,1,0):F(-1),(-1,1,0):F(1)}
derivs=[one]
for _ in range(4):derivs.append(add(du(derivs[-1]),mul(logfprime,derivs[-1])))
h={(0,0,1):F(1)};a2=F(1,16)
p=add(derivs[4],scale(mul(add(h,scale(one,-a2)),derivs[2]),2),mul(add(h,scale(one,a2)),add(h,scale(one,a2))))
# Direct r-chain rule for log(fP), independently of v-chain rule.
cv={(1,1,0):F(1,2),(-1,1,0):F(1,2)}
r_laurent=add(mul(cv,mul(p,p)),scale(add(mul(du(du(p)),p),scale(mul(du(p),du(p)),-1)),F(-1,4)))
# Chebyshev T_j(v): coefficients keyed by power of v.
def pu_add(a,b):
 d=dict(a)
 for k,v in b.items():d[k]=d.get(k,F())+v
 return clean(d)
maxr=max(abs(k[0]) for k in r_laurent)
cheb=[{0:F(1)},{1:F(1)}]
for j in range(2,maxr+1):cheb.append(pu_add({k+1:2*v for k,v in cheb[-1].items()},{k:-v for k,v in cheb[-2].items()}))
rv={}
for (j,cp,hp),coeff in r_laurent.items():
 assert r_laurent.get((-j,cp,hp),F())==coeff,'Laurent symmetry failed'
 if j<0:continue
 factor=F(1) if j==0 else F(2)
 basis={0:F(1)} if j==0 else cheb[j]
 for vp,b in basis.items():
  key=(vp,cp,hp);rv[key]=rv.get(key,F())+factor*coeff*b
rv=clean(rv)
# Substitute v=1+x,c=6+z,h=1024+y independently by binomial expansion.
expanded={}
for (vp,cp,hp),coef in rv.items():
 for xp in range(vp+1):
  for zp in range(cp+1):
   for yp in range(hp+1):
    key=(xp,yp,zp)
    term=coef*comb(vp,xp)*comb(cp,zp)*6**(cp-zp)*comb(hp,yp)*1024**(hp-yp)
    expanded[key]=expanded.get(key,F())+term
expanded=clean(expanded)
# Run the original generator, but only now compare independently reconstructed R.
source=ROOT/'experiments/code/positive_kernel_bessel_logconcavity_skeptic_round3.py'
spec=importlib.util.spec_from_file_location('original_certificate',source)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
original,rows=mod.certificate()
assert expanded==original,'Independent R polynomial differs'
# Re-expand Bernstein polynomials back into powers; do not trust forward conversion.
for row in rows:
 n=row['z_degree'];bs=[F(q) for q in row['z_bernstein_coefficients']]
 assert all(q>0 for q in bs)
 recovered={}
 for ell,b in enumerate(bs):
  for q in range(n-ell+1):
   k=ell+q;recovered[k]=recovered.get(k,F())+b*comb(n,ell)*comb(n-ell,q)*(-1)**q
 expected={k:F(v) for k,v in enumerate(row['z_power_coefficients']) if F(v)}
 assert clean(recovered)==expected,'Bernstein basis reconstruction differs'
for (cp,hp) in [(0,0)]:assert any(row['x_power']==cp and row['y_power']==hp for row in rows)
minimum=min(F(q) for row in rows for q in row['z_bernstein_coefficients']);assert minimum==6
result={'status':'PASS: independent Laurent/Chebyshev reconstruction and inverse Bernstein expansion','arithmetic':'Python standard-library Fraction; no CAS, sampling or transcendental approximation','reconstruction':'f derivative recurrence A_(n+1)=2r dA_n/dr-c(r-r^-1)A_n; direct log second derivative in r; Chebyshev conversion of symmetric Laurent powers','nonzero_R_monomials':len(expanded),'xy_groups':len(rows),'maximum_Bernstein_degree':max(row['z_degree'] for row in rows),'minimum_Bernstein_coefficient':str(minimum),'constant_xy_group_present':True,'domain':'v>=1,T²>=1024,6<=c<=7,a²=1/16','proof_scope':'Validates polynomial input/reduction and exact sign certificate; separate analytic P>0/ODE/count/Li proofs reviewed in written adjudication.'}
(ROOT/'experiments/results/bessel_logconcavity_third_round3.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
