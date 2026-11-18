#!/usr/bin/env python3
"""Exploratory float stress test for the uniform cluster bound.
All numbers are NON-VALIDATED floating approximations; the analytic proof
is proposals/independent_campaigns/uniform_cluster_remainder.md.
Stable divided differences/centered variances avoid c≈0 cancellation.
"""
import math,json
from pathlib import Path

def g(c,x):
    if c==0:return complex(x,0)
    return complex(math.sin(c*x)/c,2*math.sin(c*x/2)**2/c)

def profile(c):
    if abs(c)<0.5:
        a=math.fsum(2*(-1)**n*c**(2*n)/math.factorial(2*n+3) for n in range(14))
        v=math.fsum(2*(-1)**n*c**(2*n)/math.factorial(2*n+4) for n in range(14))
        return a/v
    return (2-2*math.sin(c)/c)/(1-(2*math.sin(c/2)/c)**2)

def actual_scaled_error(L,c):
    theta=c/L
    # Handle exact requested aliases by an explicit semantic branch in caller.
    vals=[g(c,k/L) for k in range(L+1)]
    mean=complex(math.fsum(z.real for z in vals),math.fsum(z.imag for z in vals))/(L+1)
    a=math.fsum(abs(z)**2 for z in vals)/(L+1)
    v=math.fsum(abs(z-mean)**2 for z in vals)/(L+1)
    return L*a/((L+1)*v)
rows=[]
for C in [0,1,4,10,30]:
    B=12+C*C
    for L in [2,3,10,100,1000]:
        cs=[0] if C==0 else [0,1e-12,-1e-6]+[C*j/20 for j in range(-20,21)]
        for c in cs:
            exact_alias=False
            lhs=actual_scaled_error(L,c)
            err=abs(lhs-profile(c))
            rows.append({'C':C,'L':L,'c':c,'L_E_float':lhs,'F_float':profile(c),
                         'L_times_absolute_error_float':L*err,'bound_constant':38*B*B,
                         'float_bound_holds':L*err<=38*B*B,'exact_alias_case':exact_alias})
        if C>=2*math.pi*L:
            # Actual polynomial is (1-z)^2 at theta=2pi.
            c=2*math.pi*L
            lhs=L*2*(2*L+1)/((L+1)*(L+2))
            rows.append({'C':C,'L':L,'c':c,'L_E_float':lhs,'F_float':2.0,
                         'L_times_absolute_error_float':L*abs(lhs-2),'bound_constant':38*B*B,
                         'float_bound_holds':L*abs(lhs-2)<=38*B*B,'exact_alias_case':True})
assert all(r['float_bound_holds'] for r in rows)
p=Path(__file__).resolve().parents[1]/'results'/'uniform_cluster_remainder.json'
p.write_text(json.dumps({'arithmetic':'NON-VALIDATED double precision; no proof claim',
 'proof':'proposals/independent_campaigns/uniform_cluster_remainder.md',
 'case_count':len(rows),'rows':rows},indent=2)+'\n')
print(p)
print('Cases:',len(rows),'Max L*absolute_error:',max(r['L_times_absolute_error_float'] for r in rows))
