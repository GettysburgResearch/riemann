#!/usr/bin/env python3
"""Independent finite-Li-prefix check. Numerical output is not a validated proof.
Requires mpmath and numpy. Analytic proof and error bounds are in li_skeptic.md.
"""
import json, math, pathlib
import mpmath as mp
import numpy as np
mp.mp.dps=120
N=100
T=mp.mpf(10000)
beta=mp.mpf('0.75')
a=mp.mpf(1)
# Independent Taylor/Leibniz evaluation of Li derivatives.
c=mp.taylor(lambda t:mp.log(mp.cosh(a*(t-mp.mpf('.5')))),mp.mpf(1),N)
baseline=[]
quartet=[]
for n in range(1,N+1):
    baseline.append(mp.fsum(k*mp.binomial(n,k)*c[k] for k in range(1,n+1)))
    roots=[beta+1j*T,beta-1j*T,1-beta+1j*T,1-beta-1j*T]
    # Derivative formula, independent from reflection-based positive-power form.
    q=mp.fsum(1-(r/(r-1))**n for r in roots)
    pospower=mp.fsum(1-(1-1/r)**n for r in roots)
    assert abs(q-pospower)<mp.mpf('1e-100')
    quartet.append(mp.re(q))
# Independent paired-zero partial sum; exact mathematical remainder >=0 and
# <= n^2/[pi^2(K-1/2)] for a=1, with K positive pairs included.
K=100000
gamma=(np.arange(K,dtype=float)+0.5)*math.pi
theta=2*np.arctan(1/(2*gamma))
errors=[]
for n in range(1,N+1):
    partial=float(np.sum(4*np.sin(n*theta/2)**2))
    tailbound=n*n/(math.pi**2*(K-.5))
    err=float(baseline[n-1])-partial
    assert -1e-8 <= err <= tailbound+1e-8
    errors.append(err)
bound=4*N/T*(1+1/T)**(N-1)
minimum=min(baseline)
assert minimum>bound
rows=[{'n':n,'baseline':mp.nstr(baseline[n-1],50),'quartet':mp.nstr(quartet[n-1],50),'perturbed':mp.nstr(baseline[n-1]+quartet[n-1],50)} for n in range(1,N+1)]
out={'status':'non-validated numerical illustration; analytic proof separate','parameters':{'a':'1','beta':'3/4','T':str(T),'N':N,'working_decimal_digits':mp.mp.dps,'zero_pairs_for_independent_check':K},'minimum_baseline':mp.nstr(minimum,50),'maximum_prefix_perturbation_bound':mp.nstr(bound,50),'minimum_perturbed':mp.nstr(min(b+q for b,q in zip(baseline,quartet)),50),'max_observed_tail_difference':max(errors),'rows':rows}
p=pathlib.Path(__file__).resolve().parents[1]/'results'/'li_skeptic.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
