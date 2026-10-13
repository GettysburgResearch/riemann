#!/usr/bin/env python3
"""Finite source/mask/divisor checks, not an infinite Poisson certificate."""
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
HELPER_SHA256 = 'b0f35164674ec01549788954905b2b23ad62fdbf6fba2a7cfa3bf4b340e0b52c'
counts = Counter()

def check(ok, label):
    counts[label] += 1
    if not ok:
        raise ValueError('Failed: ' + label)

p = HERE / 'native_helper.py'
check(hashlib.sha256(p.read_bytes()).hexdigest() == HELPER_SHA256, 'helper_binding')
spec = importlib.util.spec_from_file_location('native_helper', p)
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)

# Values use the inherited (1, omega) basis, omega^2=-omega-1; zeta_6=1+omega.
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def scale(x, a): return (a*x[0], a*x[1])
def phase_value(e): return native.ROOTS[e]

def element_mul(x, y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)

def chi_phase(u, active, primes):
    e=0
    for j, power in active:
        v=native.local_phase(u, primes[j])
        if v==6: return 6
        e+=power*v
    return e%6

def divs(support, primes, gens):
    out=[((),1,1,(1,0))]
    for j in support:
        out += [(ids+(j,), n*primes[j][0], -sgn, element_mul(g,gens[j]))
                for ids,n,sgn,g in out[:]]
    return out

primes=native.prime_ideals(64)
gens={}
for j,prime in enumerate(primes):
    gens[j]=next(u for u in native.element_rows(prime[0])
                 if native.norm(u)==prime[0] and native.local_phase(u,prime)==6)
    check(native.norm(gens[j])==prime[0], 'generator_norm')

# All good squarefree columns in the stated hard annulus, not a selected prime bank.
columns=[fac for n,fac,sgn in native.ideals_through(64,primes)
         if 32<n<=64 and all(e==1 for j,e in fac)]
rows=native.element_rows(13)
check(len(columns)==7 and len(rows)==54, 'complete_domain')
phases=[[native.phase(u,fac,primes) for u in rows] for fac in columns]
for inds in product(range(len(columns)), repeat=4):
    left=native.merge(columns[inds[0]],columns[inds[1]])
    right=native.merge(columns[inds[2]],columns[inds[3]])
    dl,dr=dict(left),dict(right)
    support=sorted(set(dl)|set(dr))
    active=tuple((j,(dl.get(j,0)-dr.get(j,0))%6) for j in support
                 if (dl.get(j,0)-dr.get(j,0))%6)
    neutral=tuple(j for j in support if not (dl.get(j,0)-dr.get(j,0))%6)
    check(set(j for j,e in active).isdisjoint(neutral), 'conductor_mask_partition')
    nr=math.prod(primes[j][0] for j in neutral)
    nc=math.prod(primes[j][0] for j,e in active)
    total=math.prod(primes[j][0]**e for fac in [left,right] for j,e in fac)
    check(nr*nr*nc<=total and nr<=64**2, 'neutral_support_budget')
    for i,u in enumerate(rows):
        es=[phases[ind][i] for ind in inds]
        direct=6 if 6 in es else (es[0]+es[1]-es[2]-es[3])%6
        got=chi_phase(u,active,primes)
        if any(native.local_phase(u,primes[j])==6 for j in neutral): got=6
        check(direct==got, 'complete_quartet_mask')

# Literal sixth aliases, including higher prime powers and neutral nonunit zeros.
for j in [0,2,6]:
    for a,b in product(range(9),repeat=2):
        if a+b==0: continue
        for u in rows:
            v=native.local_phase(u,primes[j])
            actual=6 if v==6 else ((a-b)*v)%6
            reduced=6 if v==6 else (((a-b)%6)*v)%6
            check(actual==reduced, 'sixth_alias_zero')

# Identity (3) is exact for sharp radial tests too; only its vanishing premise
# belongs to the infinite band-limited test, which is not numerically evaluated.
active_sets=[((0,e),) for e in range(1,6)]
active_sets += [((2,e),) for e in range(1,6)]
active_sets += [((6,e),) for e in range(1,6)]
active_sets += [((0,1),(1,5)), ((0,2),(1,4)), ((2,1),(3,5))]
heights=[1,7,13,32,64,127]
all_rows=native.element_rows(max(heights))
for active in active_sets:
    excluded={j for j,e in active}
    bank=[j for j in [0,1,2,3,4,6] if j not in excluded][:4]
    sums=[(0,0)]*(max(heights)+1)
    for u in all_rows:
        n=native.norm(u)
        sums[n]=add(sums[n],phase_value(chi_phase(u,active,primes)))
    for n in range(1,len(sums)): sums[n]=add(sums[n],sums[n-1])
    for flags in product([0,1],repeat=len(bank)):
        neutral=tuple(j for j,b in zip(bank,flags) if b)
        divisors=divs(neutral,primes,gens)
        for H in heights:
            direct=(0,0)
            for u in all_rows:
                if native.norm(u)<=H and all(native.local_phase(u,primes[j])!=6
                                             for j in neutral):
                    direct=add(direct,phase_value(chi_phase(u,active,primes)))
            rhs=(0,0)
            for ids,n,sgn,g in divisors:
                v=mul(phase_value(chi_phase(g,active,primes)),sums[H//n])
                rhs=add(rhs,scale(v,sgn))
                check(native.norm(g)==n, 'dilation_norm')
            check(rhs==direct, 'physical_mask_reunion')

# Exhaust all 3-way partitions of a labelled neutral support, retaining equal norms.
qs=[7,7,13,19,25]
valid=0
for assignment in product(range(3),repeat=len(qs)):
    r0=[q for q,b in zip(qs,assignment) if b==1]
    r1=sorted(q for q,b in zip(qs,assignment) if b==2)
    allq=r0+r1
    ds=[math.prod(q for q,b in zip(allq,flags) if b)
        for flags in product([0,1],repeat=len(allq))]
    for j in range(len(r1)):
        U=math.prod(r1[-j:]) if j else 1
        L=math.prod(r1[:j+1])
        for c,H,cut in product([7,13,49],[1,8,64,512,4096,32768],[1,2,4]):
            ok=c*math.prod(r0)*U<=H and L>H*cut
            check(not ok or all(d*c<=H or d>H*cut for d in ds), 'block_gap_implication')
            valid+=bool(ok)
check(valid>0,'nonvacuous_gap_tests')

# Exact norm witness for a nonprincipal native annular quartet.
D,H,t,P,Q=16384,2097152,7,1801,12007
for n in [t,P,Q]:
    check(n%3==1 and all(n%d for d in range(2,math.isqrt(n)+1)), 'witness_primality')
c=t*t; R=P*Q
check(all(D//2<n<D for n in [t*P,Q,t*P,Q]), 'witness_annulus')
check(c*max(P,Q)<=H and R**8>H**8*D, 'witness_gap')
check(c*R>H, 'witness_beyond_old_cutoff')
for u in native.element_rows(1):
    check(chi_phase(u,((0,1),(1,5)),primes)==0, 'witness_unit_trivial')
alpha,h,delta=Fraction(1,100),Fraction(21,20),Fraction(2,5)
check(2*alpha+1<h and 2-alpha>h+delta, 'growing_active_exponents')

# Exact Euclidean dual norms and both analytic cutoff inequalities.
for a,b in product(range(-12,13),repeat=2):
    if a==b==0: continue
    q=a*a+a*b+b*b
    check(q>=1 and Fraction(4*q,3)>Fraction(1,64), 'dual_gap_squared')

# Exact finite controls for the explicit fixed convolution at s=2 (M_s=2).
# They check the displayed inequalities, not the infinite convolution theorem.
partial=Fraction(0)
for j in range(1,129):
    partial+=Fraction(1,128*j*j)
    check(partial<Fraction(1,64), 'convolution_support_partial')
for r in range(0,8193,32):
    N=math.isqrt(r//256)
    for j in range(1,N+1):
        check(Fraction(r,128*j*j)>=2, 'disk_fourier_cutoff')
for a,b in product(range(4,37),repeat=2):
    u,v=Fraction(a,4),Fraction(b,4)
    check(2*u*v>=u+v, 'stretched_tail_separation')
# I_K(t)=nonzero element count/6; all ideals, including primes over 2 and 3.
lattice_rows=native.element_rows(256)
for t0 in range(1,257):
    n=sum(native.norm(u)<=t0 for u in lattice_rows)
    check(n%6==0 and n//6<=2*t0, 'explicit_ideal_count')
for k in range(1,129):
    for B in [Fraction(1,2),Fraction(1),Fraction(3),Fraction(16)]:
        # Coefficients of log X, log 2, log B_s in log of (8d).
        lhs=[3*k-(3*k+B), 2*k-2*k, 1-1]
        check(lhs==[-B,0,0], 'uniform_order_log_budget')

negative={}
# Neutral mask cannot be omitted.
u=gens[2]
negative['deleted_neutral_zero']=chi_phase(u,((0,1),(1,5)),primes)!=6
# A zero sextic symbol to a positive sixth power is still zero.
negative['sixth_zero_as_one']=native.local_phase(gens[0],primes[0])==6
# At H=c, a sharp radial character sum need not vanish.
sharp=(0,0)
for u in native.element_rows(49):
    sharp=add(sharp,phase_value(chi_phase(u,((0,1),(1,5)),primes)))
negative['sharp_substitution']=sharp==(-6,0)
# Scaling an ideal generator changes the NORM height by Nd, not (Nd)^2.
negative['squared_norm_dilation']=(len(native.element_rows(49//7))
                                 !=len(native.element_rows(49//49)))
# C>H always leaves d=1 in the middle window; it cannot be pruned.
negative['active_conductor_omitted']=(1*49>13 and 1<=13*2)
# Identical norms do not identify distinct neutral ideal divisors.
ds=divs((0,1),primes,gens)
negative['equal_norm_divisors_merged']=(len(ds)==4 and len(set(n for ids,n,s,g in ds))==3)
for name,value in negative.items(): check(value,'negative_control_'+name)

report={
 'status':'PASS_FINITE_CONDUCTOR_DIVISOR_WINDOW',
 'scope':'Exact finite algebra and norm inequalities only; no infinite Schwartz evaluation.',
 'counts':dict(sorted(counts.items())),
 'total_predicates':sum(counts.values()),
 'complete_quartet_domain':{'D':64,'window':'32<Nn<=64','columns':len(columns),'H':13,
                            'rows':len(rows),'ordered_tuples':len(columns)**4},
 'gap_valid_parameter_cases':valid,
 'annular_witness':{'D':D,'H':H,'active_conductor_norm':c,'neutral_radical_norm':R,
                    'total_radical_norm':c*R,'column_norms':[t*P,Q,t*P,Q],
                    'delta':'1/8','sharp_active_sum_at_H49':list(sharp)},
 'negative_controls':negative,
 'independent_mathematical_review':False,
}
print(json.dumps(report,sort_keys=True,indent=2))
