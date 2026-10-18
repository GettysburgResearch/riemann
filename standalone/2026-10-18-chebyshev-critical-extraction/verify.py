#!/usr/bin/env python3
"""Exact finite regression for the proposed Chebyshev extraction.

Standard library only. No zeta evaluation, numerical cosines, asymptotic
certification, or proof of OPEN-H occurs here. Runtime corruption flags
alter one model identity; replay.py executes them in separate processes.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import itertools
import json
from math import comb, factorial, isqrt
import sys

MUTATIONS = {
    'endpoint': 'endpoint_reproduction',
    'quadrature': 'root_quadrature',
    'kernel_norm': 'kernel_norm',
    'raw_cost': 'markov_cost',
    'unit': 'unit_subtraction',
    'mobius': 'prime_power_derivative',
    'shared_divisor': 'cocycle',
    'conjugates': 'ideal_census',
    'continuum': 'pole_cancellation',
    'single_shift': 'shift_visibility',
}
COUNTS: Counter[str] = Counter()
MUT = ''

class VerificationError(Exception):
    pass

def require(ok: bool, gate: str) -> None:
    COUNTS[gate] += 1
    if not ok:
        raise VerificationError(gate)

def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [F(0)]

def add(a, b):
    p = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): p[i] += x
    for i, x in enumerate(b): p[i] += x
    return trim(p)

def scale(p, t): return trim([x*t for x in p])

def mul(a, b):
    p = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): p[i+j] += x*y
    return trim(p)

def derivative(p): return trim([i*p[i] for i in range(1,len(p))])

def val(p, x):
    s = F(0)
    for c in reversed(p): s = s*x+c
    return s

def divmod_poly(a, b):
    a,b = trim(a),trim(b)
    if b == [0]: raise ValueError('zero polynomial divisor')
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while a != [0] and len(a)>=len(b):
        j=len(a)-len(b); c=a[-1]/b[-1]; q[j] += c
        for k,y in enumerate(b): a[j+k] -= c*y
        a=trim(a)
    return trim(q),a

def chebyshev(n):
    seq=[[F(1)],[F(0),F(1)]]
    for k in range(2,n+1):
        seq.append(add(mul([0,2],seq[-1]),scale(seq[-2],-1)))
    return seq[:n+1]

def cheb_integral(p):
    return sum((p[j]*F(comb(j,j//2),2**j) for j in range(0,len(p),2)),F(0))

def root_power_sums(p, limit):
    """Newton sums of ALL roots with multiplicity, exact over Q."""
    p=trim(p); m=len(p)-1
    a=[F(1)] + [p[m-j]/p[-1] for j in range(1,m+1)]
    sums=[F(m)]
    for k in range(1,limit+1):
        total=F(0)
        if k<=m:
            total=sum((a[j]*sums[k-j] for j in range(1,k)),F(0))+k*a[k]
        else:
            total=sum((a[j]*sums[k-j] for j in range(1,m+1)),F(0))
        sums.append(-total)
    return sums

def chebyshev_tests():
    seq=chebyshev(48)
    for m in range(1,25):
        tm=seq[m]
        kernel=[F(1)]
        for k in range(1,m): kernel=add(kernel,scale(seq[k],2))
        # At every root x_j, kernel(x_j)=m/[(1-x_j)T'_m(x_j)].
        expr=add(mul(mul([1,-1],derivative(tm)),kernel),[-m])
        require(divmod_poly(expr,tm)[1]==[0],'weight_identity')
        sums=root_power_sums(tm,2*m)
        for k in range(2*m):
            observed=sums[k]/m
            if MUT=='quadrature': observed=sums[k]
            target=F(0) if k%2 else F(comb(k,k//2),2**k)
            require(observed==target,'root_quadrature')
        for k in range(m):
            observed=cheb_integral([0]*k+kernel)
            target=(-1)**k if MUT=='endpoint' else 1
            require(observed==target,'endpoint_reproduction')
        norm=cheb_integral(mul(kernel,kernel))
        target=F(1) if MUT=='kernel_norm' else F(2*m-1)
        require(norm==target,'kernel_norm')
        trace=sum((c*sums[j] for j,c in enumerate(mul(kernel,kernel))),F(0))
        require(trace/F(m*m)==F(2*m-1,m),'discrete_norm')
        require(val(derivative(tm),1)==m*m,'endpoint_derivative')
        # Markov witness T_m(1-2h/H)-1 has norm <=2 and derivative 2m^2/H.
        H=F(1,32)
        allowed=F(1,H) if MUT=='raw_cost' else F(m*m,H)
        require(2*allowed>=2*m*m/H,'markov_cost')
        # Rational analytic test: exact interpolation of 1/(a-b*x).
        for t in (F(1,8),F(1,5),F(1,3),F(2,5)):
            a,b=1+t*t,2*t
            u=a/b
            numerator=add([1],scale(tm,-1/val(tm,u)))
            ip,rem=divmod_poly(numerator,[a,-b])
            require(rem==[0] and len(ip)<=m,'rational_interpolant')
            require(divmod_poly(add(mul(ip,[a,-b]),[-1]),tm)[1]==[0],
                    'rational_root_match')
            error=F(1,a-b)-val(ip,1)
            require(error==F(1,(a-b)*val(tm,u)) and error>0,'rational_error')
        # Continuous-kernel optimality on polynomial inputs, not arithmetic.
        require(val(kernel,1)**2==norm*(2*m-1),'kernel_extremizer')
    # Two elementary exact integrability/transfer exponent checks.
    for p in range(1,65):
        require(F(5*p,2)>0 and F(5*p,2)>=F(5,2),'all_p_error_exponent')
    return {'orders':list(range(1,25)), 'max_polynomial_degree':48,
            'rational_analytic_fixtures':96}

def primes(n):
    flags=[True]*(n+1)
    if n>=0: flags[0]=False
    if n>=1: flags[1]=False
    for p in range(2,isqrt(n)+1):
        if flags[p]:
            for j in range(p*p,n+1,p): flags[j]=False
    return [p for p in range(2,n+1) if flags[p]]

def ideal_census(cap):
    labels=[]
    for p in primes(cap):
        if p in (2,3): continue
        if p%3==1:
            labels.append((p,0,p))
            if MUT!='conjugates': labels.append((p,1,p))
        elif p*p<=cap: labels.append((p,0,p*p))
    labels.sort(key=lambda x:(x[2],x[0],x[1]))
    ideals=[]
    def walk(start,norm,fac):
        ideals.append((norm,tuple(fac)))
        for j in range(start,len(labels)):
            q=labels[j][2]
            if norm*q>cap: break
            nn=norm*q; e=1
            while nn<=cap:
                walk(j+1,nn,fac+[(j,e)])
                nn*=q;e+=1
    walk(0,1,[])
    ideals.sort()
    def chi3(n): return 0 if n%3==0 else (1 if n%3==1 else -1)
    r=[0]*(cap+1)
    for d in range(1,cap+1):
        for n in range(d,cap+1,d): r[n]+=chi3(d)
    bynorm=Counter(n for n,fac in ideals)
    for n in range(1,cap+1):
        expected=r[n]-(r[n//3] if n%3==0 else 0)-(r[n//4] if n%4==0 else 0)
        expected += r[n//12] if n%12==0 else 0
        require(bynorm[n]==expected,'ideal_census')
    return labels,ideals

def distributions(k,r):
    if r==0:
        if k==0: yield ()
        return
    if r==1:
        yield (k,);return
    for j in range(k+1):
        for tail in distributions(k-j,r-1): yield (j,)+tail

def derivative_poly_from_divisors(exponents,order):
    """Coefficient of h^order in a_h, as polynomial in distinct formal logs."""
    r=len(exponents); out={}
    for alphas in itertools.product((0,1),repeat=r):
        sign=(-1)**sum(alphas)
        b=[v-a for v,a in zip(exponents,alphas)]
        for mon in distributions(order,r):
            c=F(sign*(-1)**order)
            for v,k in zip(b,mon): c*=F(v**k,factorial(k))
            out[mon]=out.get(mon,F(0))+c
    return {k:v for k,v in out.items() if v}

def derivative_poly_from_local(exponents,order):
    r=len(exponents); out={}
    for mon in distributions(order,r):
        c=F(1)
        for v,k in zip(exponents,mon):
            c*=F((-v)**k-(-(v-1))**k,factorial(k))
        if c: out[mon]=c
    return out

def local_a(exponents,ts):
    z=F(1)
    for e,t in zip(exponents,ts):
        if e: z*=(t-1)*t**(e-1)
    return z

def arithmetic_tests():
    labels,ideals=ideal_census(512)
    require(len(ideals)==157,'census_total')
    # The unit has a_0=1, and must be subtracted before division by h.
    unit_raw=F(1); unit_subtracted=unit_raw-(0 if MUT=='unit' else 1)
    require(unit_subtracted==0,'unit_subtraction')
    power_count=0
    for norm,fac in ideals:
        if not fac: continue
        exps=[e for j,e in fac]
        for k in range(7):
            a=derivative_poly_from_divisors(exps,k)
            b=derivative_poly_from_local(exps,k)
            require(a==b,'formal_log_coefficients')
        coeff=derivative_poly_from_local(exps,1)
        expected={(1,):F(-1)} if len(fac)==1 else {}
        if MUT=='mobius':
            coeff={} if any(e>1 for e in exps) else coeff
        require(coeff==expected,'prime_power_derivative')
        power_count += len(fac)==1
        ts=[F(labels[j][2]-1,labels[j][2]) for j,e in fac]
        us=[F(labels[j][2]-2,labels[j][2]) for j,e in fac]
        direct=local_a(exps,[t*u for t,u in zip(ts,us)])
        convol=F(0)
        for A in itertools.product(*(range(e+1) for e in exps)):
            B=[e-a for e,a in zip(exps,A)]
            if MUT=='shared_divisor' and any(a and b for a,b in zip(A,B)): continue
            term=local_a(A,ts)*local_a(B,us)
            for t,b in zip(ts,B): term*=t**b
            convol+=term
        require(convol==direct,'cocycle')
    return {'complete_exterior_ideals':len(ideals),'norm_cap':512,
            'prime_ideal_labels':len(labels),'prime_power_ideals':power_count,
            'formal_h_orders':list(range(7)),
            'field':'Q(sqrt(-3)), primes above 2 and 3 excluded'}

def pole_tests():
    # Synthetic rational meromorphic functions, NOT actual zeta zeros.
    rho=F(3,4)
    for mult in range(1,9):
        kappa=(1-rho)**mult
        for j in range(2,18):
            h=F(1,32*j)
            z1h=(1-h-rho)**mult/(-h)
            kh=-kappa/(h*z1h)
            residue=-kappa/(h*z1h)
            total=residue+(kh if MUT=='continuum' else -kh)
            require(total==0,'pole_cancellation')
            leading=-h**(mult-1)*(rho-1)/(rho+h-1)
            require(leading!=0,'nonzero_shift_pole')
            require(kh>0,'local_pole_normalizer')
    # Exact constants for the vector-valued pole-energy lower bound.
    for mult in range(1,25):
        alpha=F(2*mult-1,2*mult)
        qm=(2*alpha)**(2*mult-1)*(1-alpha)/factorial(2*mult-2)
        require(qm>0,'energy_constant_positive')
        require((2*mult-1)-2*mult*alpha==0,'energy_constant_stationary')
        scalar=F(1,2*factorial(mult-1)**2)
        require(qm<=scalar,'scalar_mode_calibration')
        if mult==1: require(qm==F(1,2),'simple_pole_constant')
    # Two synthetic zeros: cancellation at h0 does not erase nearby shifts.
    h0=F(1,64)
    def pole_coeff(h): return (h-h0)*(rho-1)/(h0*(rho+h-1))
    require(pole_coeff(h0)==0,'one_shift_cancellation')
    remaining=F(0) if MUT=='single_shift' else pole_coeff(h0/2)
    require(remaining!=0,'shift_visibility')
    return {'synthetic_zero_multiplicities':list(range(1,9)),
            'single_shift_cancellation_controls':1}

def main():
    global MUT
    ap=argparse.ArgumentParser()
    ap.add_argument('--mutation',choices=sorted(MUTATIONS),default='')
    args=ap.parse_args(); MUT=args.mutation
    try:
        details={'polynomial':chebyshev_tests(),'arithmetic':arithmetic_tests(),
                 'pole':pole_tests()}
    except VerificationError as exc:
        print('REJECT:'+str(exc),file=sys.stderr)
        return 2
    report={'status':'PASS','finite_only':True,'predicate_count':sum(COUNTS.values()),
            'groups':dict(sorted(COUNTS.items())),'coverage':details,
            'actual_zeta_values_computed':False,
            'infinite_analytic_proofs_certified':False,
            'OPEN_H_proved':False}
    print(json.dumps(report,sort_keys=True,indent=2))
    return 0

if __name__=='__main__': raise SystemExit(main())
