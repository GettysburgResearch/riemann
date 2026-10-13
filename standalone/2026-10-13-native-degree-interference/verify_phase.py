#!/usr/bin/env python3
"""Exact finite controls for MICROSCOPIC_PHASE.md, not analytic certification.
Standard library only. The asymptotic and its classical inputs need proof review.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json
import math

HERE=Path(__file__).resolve().parent
CHECKS=Counter()
def need(ok,label):
    CHECKS[label]+=1
    if not ok: raise ValueError(label)

def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def peval(a,t):
    z=F(0)
    for x in reversed(a): z=z*t+x
    return z

# Gaussian rational pairs; no approximate trigonometric or Gamma calls.
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def power(a,j):
    z=(F(1),F(0))
    for _ in range(j): z=mul(z,a)
    return z

def gamma_controls():
    prev=None
    for j in range(13):
        # Numerator of 1/Gamma(-w-j), in w=1+t, over Gamma(1-t).
        p=[F(0),F((-1)**j)]
        for r in range(j+1): p=pmul(p,[F(r+1),F(1)])
        need(p[0]==0,'gamma_zero_at_native_parameter')
        need(p[1]==(-1)**j*math.factorial(j+1),'gamma_native_derivative')
        if prev is not None:
            need(p==pmul(prev,[F(-j-1),F(-1)]),'gamma_reciprocal_recurrence')
        prev=p
        for t in (F(-1,16),F(0),F(1,16)):
            direct=(-1)**j*t*math.prod(1+r+t for r in range(j+1))
            need(peval(p,t)==direct,'gamma_polynomial_identity')

def phase_controls():
    points=[]
    for denominator in (4,8,16,64,256):
        for numerator in (-2,-1,1,2):
            t=F(numerator,denominator)
            w=((1-t*t)/(1+t*t),2*t/(1+t*t))
            need(w[0]*w[0]+w[1]*w[1]==1,'rational_unit_phase')
            for j in range(1,33):
                u=power(w,j)
                wc=(w[0],-w[1])
                need(power(wc,j)==(u[0],-u[1]),'phase_conjugation')
                need(abs(u[1])<=j*abs(w[1]),'imaginary_prime_degree_bound')
                series=tuple(sum(power(w,r)[i] for r in range(j)) for i in (0,1))
                need(mul((w[0]-1,w[1]),series)==(u[0]-1,u[1]),'phase_difference_factor')
            points.append(w)
    return points

def arithmetic_controls(points):
    p=HERE.parent/'2026-10-13-native-matching-geometry'/'census_source.py'
    b=p.read_bytes()
    need(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
         =='2a074ccede483324392a729056ccbf43a1f26eac','arithmetic_source_binding')
    spec=importlib.util.spec_from_file_location('native_source',p)
    c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
    ps=c.prime_ideals(256)
    representatives=[]
    for j,(q,p,r,table) in enumerate(ps[:8]):
        gen=next(u for u in c.element_rows(q) if c.norm(u)==q and c.local_phase(u,ps[j])==6)
        # exact multiplication in O_K, with no residue reduction.
        def emul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
        row=(1,0)
        for _ in range(6): row=emul(row,gen)
        need(c.norm(row)==q**6,'sixth_copy_physical_height')
        representatives.append((j,row))
    for D in (32,64,128,256):
        columns=[f for n,f,_ in c.ideals_through(D,ps) if D<2*n and all(e==1 for j,e in f)]
        countdegree=sum(len(f) for f in columns)
        for w in points[::4]:
            base=[F(0),F(0)]
            for fac in columns:
                v=power(w,len(fac));sgn=(-1)**len(fac)
                base=[x+sgn*y for x,y in zip(base,v)]
            for j,row in representatives:
                actual=[F(0),F(0)];deleted_im=F(0);deleted_degree=0
                for fac in columns:
                    phase=c.phase(row,fac,ps)
                    excluded=any(a==j for a,e in fac)
                    need(phase==(6 if excluded else 0),'literal_sixth_copy_mask')
                    value=power(w,len(fac));sgn=(-1)**len(fac)
                    if excluded:
                        deleted_im+=sgn*value[1];deleted_degree+=len(fac)
                    else: actual=[x+sgn*y for x,y in zip(actual,value)]
                need(base[1]-actual[1]==deleted_im,'copy_imaginary_deletion_identity')
                need(abs(deleted_im)<=abs(w[1])*deleted_degree,'theta_proportional_mask_bound')
                need(deleted_degree<=countdegree,'positive_count_domination')

def exponents():
    for k in range(1,33):
        for h in (F(1,2),F(1),F(21,20),F(2),F(4)):
            critical=F(1,2)-5*h/(12*k)
            for a in (F(1,8),F(1,4),F(9,32),F(1,2),F(3,4)):
                excess=2*k*(1-a)+h/6-(h+k)
                need(excess==2*k*(critical-a),'moment_excess_identity')
                need((excess>0)==(a<critical),'strict_phase_obstruction_condition')
    need(F(1,2)-5*F(21,20)/24==F(9,32),'quartic_phase_threshold')
    need(4*(1-F(1,4))+F(21,20)/6-(F(21,20)+2)==F(1,8),'quartic_phase_excess')
    need(2*2*2+1==9,'quartic_logarithmic_denominator')
    return {'k':2,'h':'21/20','phase_exponent':'1/4','critical_phase_exponent':'9/32',
            'lower_power_excess':'1/8','logarithmic_denominator_power':9}

def main():
    gamma_controls();points=phase_controls();arithmetic_controls(points);example=exponents()
    print(json.dumps({'status':'PASS_FINITE_PHASE_CONTROLS_ONLY','checks':dict(sorted(CHECKS.items())),
          'predicates_including_setup':sum(CHECKS.values()),'example':example,
          'scope':'Exact Gamma numerator recurrences, rational phase algebra, complete small hard-window ideal columns, sixth-copy masks and exponent identities. No analytic asymptotic or prime-ideal theorem is tested.'},sort_keys=True,indent=2))

if __name__=='__main__': main()
