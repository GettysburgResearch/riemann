"""Exact check of an ordinary-Christoffel versus one-sided moment distinction.
No actual zeta matrix or prime-side moment is constructed.
"""
from pathlib import Path
from fractions import Fraction as F
import json
B=Path(__file__).resolve().parents[2]
def inner(a,b,m):return sum(x*y*m[i+j] for i,x in enumerate(a) for j,y in enumerate(b))
x=[F(-1),F(1),F(6,5)];w=[F(5,66),F(11,66),F(50,66)]
m=[sum(v*t**k for t,v in zip(x,w)) for k in range(5)]
assert m==[F(1),F(1),F(4,3),F(7,5),F(136,75)]
p=[F(1),F(12,103),F(-85,103)]
assert inner(p,[0,1],m)==inner(p,[0,0,1],m)==0
lam=inner(p,p,m);assert lam==F(5,309)
positive=sum(v for t,v in zip(x,w) if t>0);assert positive==F(61,66)
assert 1-lam>positive
# Since the three support points are distinct with positive weights, their degree2
# moment Gram matrix is positive definite; p's two orthogonality equations make
# it the unique minimum at constant coefficient1. This is ordinary Christoffel.
actual=[F(1),F(1),F(4,3),F(2),F(13,4)];pa=[F(1),F(-7,4),F(2,3)]
assert inner(pa,[0,1],actual)==inner(pa,[0,0,1],actual)==0
la=inner(pa,pa,actual);assert la==F(5,36)
out={'kind':'exact_rational_scope_check_NOT_actual_zeta_or_full_prime_moment','countermodel_dimension':66,'eigenvalues':['-1','1','6/5'],'multiplicities':[5,11,50],'normalized_moments':[str(v) for v in m],'christoffel_minimizer_coefficients':[str(v) for v in p],'orthogonality_to_x_and_x_squared':True,'ordinary_Lambda2_0':str(lam),'one_minus_Lambda':str(1-lam),'actual_positive_fraction':str(positive),'generic_one_sided_claim_fails':True,'difference':str(1-lam-positive),'source_specific_sine_moments':[str(v) for v in actual],'source_specific_minimizer':[str(v) for v in pa],'source_specific_Lambda2':str(la),'source_specific_one_sided_certificate_valid':'For x<=0,1-7x/4+2x^2/3>=1, hence its square majorizes1_{x<=0}.','conditional_positive_fraction':str(1-la),'conditional_simple_critical_fraction_after_source_count_step':str(2*(1-la)-1),'scope':'Generic ordinary Christoffel function controls an atom at0, not automatically a negative halfline. The source-specific four-moment certificate is valid; no main-theorem error alleged.'}
(B/'experiments/results/christoffel_one_sided_scope.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
