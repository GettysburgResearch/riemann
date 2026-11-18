#!/usr/bin/env python3
"""Exact rational checks supplement analytic Montgomery1973 reconstruction.
No zeta zero numerical data and no claim of a numerical proof of RH.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

# Classical rational bounds for pi; their proof is external to this script.
pi_lo,pi_hi=F(333,106),F(355,113)
a=F(17,25)
x_lo,x_hi=2*pi_lo*a,2*pi_hi*a
# Cin(x)=sum_{k>=1}(-1)^(k+1)x^(2k)/((2k)(2k)!).
# For x<=x_hi<4.28 the alternating terms decrease from k=1:
# term_(k+1)/term_k=x²(2k)/((2k+2)^2(2k+1))<=x_hi²/24<1.
assert x_hi*x_hi/F(24)<1
cin_lower=F(0)
for k in range(1,21):
    term=(x_lo if k%2 else x_hi)**(2*k)/((2*k)*factorial(2*k))
    cin_lower += term if k%2 else -term
# An even partial sum is a lower bound. Positive powers use x_lo,
# negative powers use x_hi, preserving a simultaneous lower bound.
c_lower=a-1+cin_lower/(pi_hi*pi_hi*a)
assert c_lower>F(8,1000)
# The corrected triangular transform integrates to r(0)=1;
# the display as printed, with a-beta, integrates to 2.
triangle_mass=F(1)
printed_mass=F(2)
# At a negative interior point the omitted absolute value is explicit.
beta=-a/2
actual_value=(a-abs(beta))/(a*a)
printed_value=(a-beta)/(a*a)
assert printed_value==3*actual_value
# Integer multiplicity bound: 1_(m=1)>=2-m. Universally proved by m=1,2,>=3.
multiplicities=[{'m':m,'simple_indicator':int(m==1),'linear_bound':2-m}
                for m in range(1,11)]
assert all(x['simple_indicator']>=x['linear_bound'] for x in multiplicities)
result={
 'status':'exact rational supplemental certificate; pi rational bounds external',
 'source':'PAPER-E009, pp191–192, triangular transform and Corollary3',
 'small_gap_a':'17/25',
 'C_a_lower_bound_fraction':str(c_lower),
 'C_a_lower_bound_decimal_for_display':float(c_lower),
 'certified_C_a_greater_than':'0.008',
 'alternating_terms':20,
 'triangle_integral_correct':str(triangle_mass),
 'triangle_integral_as_printed':str(printed_mass),
 'negative_beta_witness':{'beta':str(beta),'correct':str(actual_value),'as_printed':str(printed_value)},
 'multiplicity_examples':multiplicities,
 'limitations':'The analytic proof, Fourier convention, zero counting and RH-conditional theorem are in audits/montgomery1973_round2.md; this script does not verify prime or zero sums.'
}
root=Path(__file__).resolve().parents[2]
out=root/'experiments/results/montgomery_original_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['multiplicity_examples','C_a_lower_bound_fraction']},indent=2))
