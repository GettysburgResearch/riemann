#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib, json

HERE=Path(__file__).resolve().parent
result=json.loads((HERE/'results/verification.json').read_text())
mins={int(k):float(v) for k,v in json.loads((HERE/'results/row_minima.json').read_text()).items()}
assert result['activation_row_cells']==sum(min(66,N//67)*65 for N in range(67,166000))
assert result['coarse_direct_passes']+len(result['coarse_dependency_exceptions'])==result['activation_row_cells']
assert result['minimum_raw_direct_cell']==[125,1,62]
assert result['minimum_raw_direct_lower']>0.0012
assert min(result['exception_certified_lowers'].values())>0.3

# Conservative coefficient and arithmetic perturbation audit.
rAt=3e-13; rBt=1.2e-12; At=2.5; Bt=23.0
ra=1.2e-8; rb=1.2e-7; am=5000.0; bm=50000.0
q=.123; q2=q*q; q3=q2*q; ql=.26; q2l=.032; q3l=.004
def pe(X,rX,Y,rY): return X*rY+Y*rX+rX*rY
ea=pe(At,rAt,am,ra); eb=pe(At,rAt,bm,rb)
eBa=pe(Bt,rBt,am,ra); eBb=pe(Bt,rBt,bm,rb)
eC1=2*ea*(1+q+q2+q3)
eC2=2*eb*(1+q+q2+q3)+4*ea*(ql+q3l)
eC3=2*eBa*(1+2*q+q2)
eC4=2*eBb*(1+2*q+q2)+4*eBa*(ql+q2l)
def audit_error(j):
    return (19560*eC1+1629*eC2+36.1*eC3+3*eC4)/(j*(j-1))+1e-8
def cap(j):
    if j==2:return .01
    if j==3:return .005
    if j<=9:return .002
    if j<=20:return .001
    if j<=40:return .0002
    return .00005
for j in range(2,67):
    assert audit_error(j)<cap(j),(j,audit_error(j),cap(j))
for j,v in mins.items():
    assert v-cap(j)>.001,(j,v,cap(j))
assert result['minimum_raw_direct_lower']-cap(62)>.001

# Exact directed replay of the P61 tail parity-prefix reserve.
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
DEN=10**60
vals=[(1,1)]
for prime in P: vals += [(d*prime,-mu) for d,mu in list(vals)]
vals.sort()
Ae=Ao=Fraction(0);Be_lo=Be_hi=Bo_lo=Bo_hi=Fraction(0)
minimum=None;arg=None;states=0
for d,mu in vals:
    if mu==1:Ae+=Fraction(1,d)
    else:Ao+=Fraction(1,d)
    n=DEN*DEN; lo=isqrt(n//d)
    while (lo+1)*(lo+1)*d<=n:lo+=1
    while lo*lo*d>n:lo-=1
    hi=lo if lo*lo*d==n else lo+1
    ilo,ihi=Fraction(lo,DEN),Fraction(hi,DEN)
    if mu==1:Be_lo+=ilo;Be_hi+=ihi
    else:Bo_lo+=ilo;Bo_hi+=ihi
    if d>=166000:
        lower=Ae*Bo_lo-Ao*Be_hi;states+=1
        if minimum is None or lower<minimum:minimum,arg=lower,d
assert states==result['tail_prefix_states']
assert arg==result['tail_prefix_minimum_start']
assert minimum>Fraction(7,4)

# Exact rational check of the proportional competitor used by L-91780.
fixtures=[
    ([Fraction(5),Fraction(3),Fraction(2)], [Fraction(7),Fraction(4),Fraction(1)], Fraction(6)),
    ([Fraction(4),Fraction(4),Fraction(1)], [Fraction(9),Fraction(6),Fraction(1)], Fraction(5))
]
for targets,rows,M in fixtures:
    total=sum(targets)
    proportional=sum((M/total)*r for r in rows)
    assert proportional==M*sum(rows)/total

assert result['analytic_tail_avlt_proved'] is False
assert result['live_native_allocation_proved'] is False
assert result['rh_established_by_replay'] is False
canonical=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
print('PASS_TARGET_LORENZ_COMPACT_PROPORTIONAL_AVLT')
print('result_sha256',hashlib.sha256(canonical).hexdigest())
print('tail_prefix_exact_lower',minimum)
print('RH_UNPROVEN')
