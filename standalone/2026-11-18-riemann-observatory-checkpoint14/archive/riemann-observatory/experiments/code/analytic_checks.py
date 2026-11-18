"""Exact exponent checks plus NONVALIDATED stress tests of a sourced finite inequality.
Python standard library only. Run from archive root: python experiments/code/analytic_checks.py
"""
import cmath, math, random, json
from fractions import Fraction as F
random.seed(20261117)
exact={}
for s in [F(7,10),F(3,4),F(4,5)]:
 d=15*(1-s)/(3+5*s); target=2*(1-s)
 exact[str(s)]={'GM':str(d),'strong_density_target':str(target),'gap':str(d-target)}
assert exact['3/4']['gap']=='1/18'
# Uniform eta^2 on[-1/2,1/2]: K(z)=sin(pi z)/(pi z), K(0)=1.
def k(z):return 1+0j if abs(z)<1e-12 else cmath.sin(math.pi*z)/(math.pi*z)
min_slack=1e99; max_im=0; failures=[]
for run in range(500):
 Z=[]; simple_real=0
 for j in range(random.randrange(1,8)):
  x=random.uniform(-5,5);m=random.randrange(1,4)
  if random.randrange(2):
   Z.extend([complex(x)]*m);simple_real+=int(m==1)
  else:
   z=complex(x,random.uniform(.01,1));Z.extend([z]*m+[z.conjugate()]*m)
 E=sum(k(z-s)**2 for z in Z for s in Z)
 slack=simple_real-2*len(Z)+E.real; min_slack=min(min_slack,slack);max_im=max(max_im,abs(E.imag))
 if slack < -1e-8:failures.append(run)
print(json.dumps({'exact_density_exponents':exact,'finite_kernel_stress':{'cases':500,'min_slack':min_slack,'max_imaginary_roundoff':max_im,'failed_case_indices':failures,'arithmetic':'ordinary complex floating point, not validated; not a proof'},'exact_missing_symmetry_witness':{'Z':'{i}','K(0)':1,'simple_real':0,'putative_lower_bound':1}},indent=2))
