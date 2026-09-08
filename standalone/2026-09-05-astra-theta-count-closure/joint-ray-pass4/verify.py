#!/usr/bin/env python3
"""Bounded exact controls, NOT a proof of the analytic theorems or RH.

Python standard library only. Every mathematical assertion here is checked
with Fraction/integer arithmetic. No zeta zero is computed or assumed.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
from typing import Dict, Tuple

COUNTS: Counter[str] = Counter()

def require(ok: bool, category: str) -> None:
    if not ok:
        raise ArithmeticError(f'Exact control failed: {category}')
    COUNTS[category] += 1

# Gaussian rationals, with no conversion to floating point.
C = Tuple[Q, Q]

def add(a: C, b: C) -> C:
    return a[0]+b[0], a[1]+b[1]

def mul(a: C, b: C) -> C:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def power(a: C, n: int) -> C:
    r = (Q(1), Q(0))
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n //= 2
    return r

# Sparse polynomials in t and ell; negative t exponents are allowed.
Poly = Dict[Tuple[int, int], Q]

def acc(p: Poly, key: Tuple[int, int], value: Q) -> None:
    p[key] = p.get(key, Q(0)) + value
    if not p[key]:
        del p[key]

def next_fourier(p: Poly) -> Poly:
    result: Poly = {}
    # R_next=(1/(2t)+1/4-ell^2/(4t^2))*R-dR/dt.
    for (a,b), c in p.items():
        acc(result, (a-1,b), (Q(1,2)-a)*c)
        acc(result, (a,b), c/4)
        acc(result, (a-2,b+2), -c/4)
    return result

def hermite_fourier(m: int) -> Poly:
    result: Poly = {}
    for j in range(m+1):
        for h in range(j+1):
            c = (Q(comb(m,j), 4**(m-j)) * (-1)**(j+h)
                 * Q(factorial(2*j), 4**j*factorial(h)*factorial(2*j-2*h)))
            acc(result, (-(2*j-h),2*j-2*h), c)
    return result

def run() -> dict:
    COUNTS.clear()
    for m in range(1,49):
        ratios = [Q(1)]
        for l in range(m):
            ratios.append(ratios[-1]*Q(2*(m-l),2*(m-l)-1))
            require(ratios[-1] <= 2*ratios[-2], 'gamma_ratio_step')
        for delta in [Q(0), Q(1,4), Q(1), Q(5), Q(20)]:
            weights = [ratios[l]*delta**l/factorial(l) for l in range(m+1)]
            total = sum(weights)
            mean = sum(l*w for l,w in enumerate(weights))/total
            tail = sum(w for l,w in enumerate(weights) if 2*l>m)/total
            require(mean <= 2*delta, 'gamma_mixture_mean')
            require(tail <= 4*delta/m, 'gamma_mixture_tail')
            # Different construction: elementary Gaussian moments.
            gamma_rat = [Q(1)]
            for l in range(1,m+1):
                gamma_rat.append(gamma_rat[-1]/Q(2*(m-l)+1,2))
            alternate = sum(comb(m,l)*delta**l*gamma_rat[l] for l in range(m+1))
            require(alternate == total, 'binomial_gamma_mixture')

    for a in range(1,8):
        k = a*a
        for v in [Q(1,3), Q(1), Q(5,2), Q(a), Q(a+3)]:
            score = 2*k/v-2*v+4*(v-a)
            require(score == 2*(v-a)**2/v, 'root_gamma_score_identity')
            require(score >= 0, 'root_gamma_score_nonnegative')

    p: Poly = {(0,0):Q(1)}
    for m in range(15):
        require(p == hermite_fourier(m), 'hermite_time_recurrence')
        for t in [Q(1,10),Q(1),Q(5)]:
            delta=t/4
            r_l=Q(1)
            W=Q(1)
            for l in range(1,m+1):
                r_l*=Q(2*(m-l+1),2*(m-l+1)-1)
                W+=r_l*delta**l/factorial(l)
            R0=sum(c*t**a for (a,b),c in p.items() if b==0)
            g_m=Q(factorial(2*m),4**m*factorial(m))
            require(t**m*R0 == g_m*W, 'fourier_mass_normalization')
        if m:
            # F(i/2)=0 and the exact division that yields I_(m-1)/2.
            base = (Q(0), Q(1,2))
            a2 = add(mul(base,base),(Q(1,4),Q(0)))
            require(power(a2,m) == (Q(0),Q(0)), 'endpoint_vanishing')
            for x in [Q(0), Q(1,3), Q(2)]:
                u=x*x+Q(1,4)
                require(u**m/u == u**(m-1), 'poisson_division')
        p=next_fourier(p)

    for t in [Q(1,100),Q(1,2),Q(1),Q(10)]:
        for ell in [Q(0),Q(1),Q(3),Q(50)]:
            # Gaussian exponential exponent <= shifted-line exponent.
            gap = 2*t-ell+ell*ell/(8*t)
            require(gap == (ell-4*t)**2/(8*t), 'gaussian_contour_square')
            require(gap >= 0, 'gaussian_contour_domination')

    for q in [Q(1,10000),Q(1,1000),Q(1,100),Q(1,10)]:
        gain_lower = 3*q*q/8-q**4/4
        phase_lower = q*q/(2+q)-q**3/3
        require(gain_lower >= q*q/3, 'ray_atom_gain_bound')
        require(phase_lower >= q*q/3, 'ray_atom_phase_lower')
        require(q*q/(2+q) <= q*q/2, 'ray_atom_phase_upper')

    # Exact periodic dominant spectra test the Cesaro mechanism. These are
    # SYNTHETIC transformed atoms, not alleged zeros of actual xi.
    spectra = [
        [((Q(0),Q(1)),1),((Q(0),Q(-1)),1)],
        [((Q(0),Q(1)),1),((Q(0),Q(-1)),1),((Q(-1),Q(0)),3)],
        [((Q(-1),Q(0)),2)],
    ]
    periodic_results=[]
    for spec in spectra:
        P=sum(d for _,d in spec)
        V=sum(d*d for _,d in spec)
        values=[]
        for n in range(4):
            val=(Q(0),Q(0))
            for atom,d in spec:
                z=power(atom,n)
                val=add(val,(d*z[0],d*z[1]))
            require(val[1]==0, 'ray_conjugation')
            values.append(val[0])
        require(sum(values)==0, 'ray_cesaro_mean')
        require(sum(x*x for x in values)/4==V, 'ray_cesaro_square')
        eta=Q(V,4*P)
        density=Q(sum(x <= -eta for x in values),4)
        require(density>=Q(V,4*P*P), 'ray_negative_density')
        periodic_results.append({'values':[str(x) for x in values],
                                 'density':str(density),
                                 'lower_bound':str(Q(V,4*P*P))})

    # A positive-real dominant atom invalidates the zero-mean step. Ensure
    # this countercontrol is not silently admitted to the sign theorem.
    vals=[Q(2)+Q((-1)**n) for n in range(4)]
    require(sum(vals)/4==2 and min(vals)>0, 'positive_real_dominant_exclusion')

    return {
        'status':'PASS_BOUNDED_EXACT_JOINT_RAY_CONTROLS',
        'arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
        'counts':dict(sorted(COUNTS.items())),
        'total_checks':sum(COUNTS.values()),
        'periodic_synthetic_controls':periodic_results,
        'analytic_theorems_machine_proved':False,
        'new_zeta_zeros_computed':False,
        'rh_proved':False,
        'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group()
    group.add_argument('--write',type=Path)
    group.add_argument('--check',type=Path)
    args=ap.parse_args()
    result=run()
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write:
        args.write.write_text(text,encoding='utf-8')
    if args.check:
        observed=json.loads(args.check.read_text(encoding='utf-8'))
        if observed != result:
            raise SystemExit('REFUSED: retained result differs from fresh exact execution')
    print(text,end='')

if __name__=='__main__':
    main()
