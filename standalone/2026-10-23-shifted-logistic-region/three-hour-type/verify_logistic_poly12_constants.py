"""Exact constants for the proposed degree12 sum-of-squares detector.

The positive-Fourier curvature lemma is an analytic input documented
separately. All finite comparisons below use exact Fraction intervals.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import runpy

BASE=Path(__file__).with_name('verify_logistic_master_fraction.py')
SHA='cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413'
if hashlib.sha256(BASE.read_bytes()).hexdigest()!=SHA:
    raise RuntimeError('baseline hash mismatch')
ns=runpy.run_path(str(BASE))
I,check,log_point,log_i=(ns[k] for k in ('I','check','log_point','log_i'))
C=[3500513104,-5906953599,-1574092731,18166603739,6213449589,
   -38436761903,-16088159026,168141762350,447056663730,616860378424,
   541372347258,298691298328,83048065550]
M=10**14
NORM=sum(c*c for c in C)+13*M
A=[Q(sum(C[j]*C[j+k] for j in range(13-k))+M*(13-k),NORM)
   *(1 if k==0 else 2) for k in range(13)]
check(NORM==1000000001299439064580929,'normalization')
check(A[0]==1 and A[1]>1 and all(a>0 for a in A),'positive coefficients')
check(A[1]==Q(1738295793206197388801164,NORM),'a1')
AP=sum(A[1:])


def atan(q):
    total=sum(((-1)**j*q**(2*j+1)/Q(2*j+1) for j in range(40)),Q(0))
    return I(total,total+q**81/81)


pi=16*atan(Q(1,5))-4*atan(Q(1,239))
gamma_lower=I(sum((Q(1,j) for j in range(1,1001)),Q(0)))-log_point(Q(1000))-Q(1,2000)
carch=1-gamma_lower/2-(1+AP/2)*ns['LOG2']-(1+AP)/2*log_i(pi)
carch+=sum((A[k]/2*log_point(Q(k)) for k in range(1,13)),I(0))
check(carch.hi<Q(-3003196,10**6),'Carch <-3.003196')
curvature=ns['SEC2']*ns['TAN']**2*(ns['SEC2']*ns['THETA']*ns['COT']-1)
check(curvature.lo>50 and curvature.hi<51,'positive-Fourier curvature <51')
check(not carch.lo<Q(-3004,1000),'negative control: overly negative Carch')
check(not curvature.hi<50,'negative control: curvature <50')
print(json.dumps({'status':'pass','scope':'degree12 polynomial and gamma/curvature constants only',
                  'baseline_source_sha256':SHA,'normalization':str(NORM),
                  'a1':str(A[1]),'aP':str(AP),'coefficients':[str(x) for x in A],
                  'Carch_upper_decimal':float(carch.hi),'Carch_certified_upper':'-3.003196',
                  'curvature_interval_decimal':[float(curvature.lo),float(curvature.hi)],
                  'curvature_certified_upper':51,'negative_controls':2},sort_keys=True))
