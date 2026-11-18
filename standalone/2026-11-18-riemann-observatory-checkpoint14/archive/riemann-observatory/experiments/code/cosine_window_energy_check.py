"""Exact arithmetic check of first-window energy and resulting rational certificate constant.
Independent closed-form integration; not proof of the local inequality or zeta transfer.
"""
from fractions import Fraction as F
import json,pathlib
coeff=[F(n,10**6) for n in [193305,-23105,29166,13952,-21009,41052]]
def atan(q,n):
 a=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));b=a+F((-1)**n,(2*n+1)*q**(2*n+1));return min(a,b),max(a,b)
a,b=atan(5,80);c,d=atan(239,30);pl,pu=16*a-4*d,16*b-4*c
base=F(4,3)+sum((a*a/2 for a in coeff),F(0));S=sum(((-1)**j*a/F(j*j)-a*a/F(4*j*j) for j,a in enumerate(coeff,1)),F(0));lo,hi=sorted([base+S/(pl*pl),base+S/(pu*pu)])
C=F(266541,200000);assert hi<C
x,y,alpha=F(54350,10**6),F(69433,10**6),F(6219,10**6);b=6*alpha;q=(3-C+y-x-b)/(2-2*x+y)
assert q==F(1645064,1960733)
res={'kind':'exact_rational_constant_check_with_classical_cosine_integral_formula','positivity_lower_bound':str(1-sum(map(abs,coeff))),'energy_formula':'C=4/3+sum a_j^2/2+(1/pi^2)sum[(-1)^j a_j/j^2-a_j^2/(4j^2)]','energy_upper_bound':str(C),'energy_upper_bound_proved':True,'strict_positive_slack_lower_bound':str(C-hi),'certificate_q':str(q),'matches_source_q':True,'scope':'This proves energy/constant arithmetic assuming the elementary displayed integral formula, not the local inequality, its transfer or the zeta theorem.'}
p=pathlib.Path(__file__).resolve().parents[2]/'experiments/results/cosine_window_energy_check.json';p.write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
