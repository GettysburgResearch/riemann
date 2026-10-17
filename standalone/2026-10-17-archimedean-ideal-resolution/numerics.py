#!/usr/bin/env python3
"""Non-certified 70-digit checks of finite Gaussian/Fourier identities.

These computations are NOT interval certificates or asymptotic evidence.
The exact arithmetic backend is check.py; numerical branches independently
use the discrete and periodized Fourier formulas and direct log-scale quadrature.
"""
from __future__ import annotations
import json
from math import ceil
import mpmath as mp
import check as ex
mp.mp.dps=70
COUNT=0

def require(t,label):
    global COUNT
    COUNT+=1
    if not t:raise ArithmeticError(label)

def realq(x):return mp.mpf(x.numerator)/x.denominator

def cmplx(x):return realq(ex.F(x[0]))+realq(ex.F(x[1]))*mp.mpc(-mp.mpf('0.5'),mp.sqrt(3)/2)

def ang(a):return mp.arg(cmplx(ex.psi(a)))

def theta_fourier(R,theta):
    # Finite numerical truncation, with |ell|<=18R. Its positive Gaussian
    # tail is far below the 1e-55 comparison tolerance in these R>=1 cases.
    L=int(mp.ceil(18*R));den=mp.fsum(mp.exp(-mp.mpf(l*l)/(2*R*R)) for l in range(-L,L+1))
    return mp.fsum(mp.exp(-mp.mpf(l*l)/(2*R*R))*mp.cos(l*theta) for l in range(-L,L+1))/den

def theta_wrapped(R,theta):
    theta=mp.atan2(mp.sin(theta),mp.cos(theta))
    return mp.fsum(mp.exp(-R*R*(theta-2*mp.pi*j)**2/2) for j in range(-5,6))/mp.fsum(mp.exp(-2*mp.pi**2*R*R*j*j) for j in range(-5,6))

def kernel(R,a,b):
    return mp.exp(-R*R*mp.log(ex.norm(a)/mp.mpf(ex.norm(b)))**2/2)*theta_wrapped(R,ang(a)-ang(b))

def fmt(x):return mp.nstr(x,25)

def run():
    errs=[]
    for R in map(mp.mpf,[1,2,4,8]):
        for theta in [mp.mpf(0),mp.mpf(1)/7,mp.pi/2,mp.pi,2*mp.pi+mp.mpf(1)/3]:
            e=abs(theta_fourier(R,theta)-theta_wrapped(R,theta));errs.append(e)
            require(e<mp.mpf('1e-55'),'Poisson/discrete Gaussian agreement')
    ideals=ex.all_ideals(128);ps=ex.build_primes(128,ideals)
    fac={a:ex.factor(a,ps) for a in ideals}
    good=[a for a in ideals if all(ps[j][1] not in(2,3) and e==1 for j,e in fac[a])]
    cols=[(a,(ex.F((-1)**len(fac[a])),ex.F(0))) for a in good if 32<ex.norm(a)<=64]
    vectors=ex.finite_poly(cols,2)
    diagonal=sum(ex.norm(c) for c in vectors.values());fib={}
    for a,c in vectors.items():fib[ex.norm(a)]=ex.add(fib.get(ex.norm(a),ex.ZERO),c)
    normdiagonal=sum(ex.norm(c) for c in fib.values())
    moments=[]
    for R in map(mp.mpf,[1,8,64,128]):
        aa=list(vectors);phi={a:ang(a) for a in aa};N={a:ex.norm(a) for a in aa};C={a:cmplx(vectors[a]) for a in aa}
        total=mp.mpf(0);rowmass={a:mp.mpf(0) for a in aa}
        for a in aa:
            for b in aa:
                ker=mp.exp(-R*R*mp.log(mp.mpf(N[a])/N[b])**2/2)*theta_wrapped(R,phi[a]-phi[b])
                total+=mp.re(C[a]*mp.conj(C[b]))*ker
                if a!=b:rowmass[a]+=abs(ker)
        require(total>=0,'finite full hybrid positivity')
        if R>=128:require(abs(total-diagonal)<=mp.mpf(600)/2401*diagonal,'proved finite near-isometry')
        moments.append({'R':fmt(R),'complete_finite_M4_average':fmt(total),
                        'maximum_offdiagonal_kernel_row_sum':fmt(max(rowmass.values()))})
    # Exact K_D for finite coefficient pairs versus direct log-scale quadrature.
    c=mp.mpf(5)/6; beta=2*c-1; kappa=mp.exp(beta*beta/2)/(2*mp.sqrt(2*mp.pi))
    quadrature=[]
    for v,z,D in [(7,7,16),(7,25,64),(25,49,4),(49,61,128)]:
        def integrand(r):
            Wv=mp.exp(-c*(mp.log(v)-r)-(mp.log(v)-r)**2/4)/(2*mp.sqrt(mp.pi))
            Wz=mp.exp(-c*(mp.log(z)-r)-(mp.log(z)-r)**2/4)/(2*mp.sqrt(mp.pi))
            return Wv*Wz*mp.exp(-r)
        direct=mp.quad(integrand,[-mp.inf,0,mp.log(D)])
        x=mp.log(D)-mp.log(mp.mpf(v)*z)/2-beta
        formula=kappa/mp.sqrt(mp.mpf(v)*z)*mp.exp(-mp.log(mp.mpf(v)/z)**2/8)*(1+mp.erf(x/mp.sqrt(2)))/2
        require(abs(direct-formula)<mp.mpf('1e-55'),'full log-Gaussian pair integral')
        quadrature.append({'v':v,'z':z,'D':D,'kernel':fmt(formula),'absolute_error':fmt(abs(direct-formula))})
    # The generator-distance inequality is checked numerically on all pairs
    # through norm 64, including distinct equal-norm ideals. This is diagnostic,
    # not the proof of the elementary inequality.
    geometry=[]; pairs=[a for a in ideals if ex.norm(a)<=64]
    worst=mp.mpf(0)
    for a in pairs:
        ca=cmplx(a)
        for b in pairs:
            if a==b:continue
            choices=[cmplx(ex.mul(b,u)) for u in ex.UNITS]
            cb=min(choices,key=lambda z:abs(mp.arg(z/ca)))
            d=6*abs(mp.arg(cb/ca));rr=mp.log(mp.mpf(ex.norm(a))/ex.norm(b));Y=max(ex.norm(a),ex.norm(b))
            lhs=abs(ca-cb)**2;rhs=mp.mpf(Y)*(rr*rr/4+d*d/36)
            require(lhs<=rhs+mp.mpf('1e-60'),'norm-angle separation formula')
            require(lhs>=1-mp.mpf('1e-60'),'nonzero lattice gap')
            worst=max(worst,lhs/rhs)
    return {'status':'ordinary 70-digit approximations, NOT certified intervals or asymptotic evidence',
            'fourier_pairs':len(errs),'max_fourier_error':fmt(max(errs)),
            'scalar_native_hard_window':{'lower_exclusive':32,'upper_inclusive':64,'columns':len(cols),
                'product_ideals':len(vectors),'product_ideal_diagonal':str(diagonal),'product_norm_diagonal':str(normdiagonal),
                'native_t0_l0_M4':str(ex.norm(sum_poly(cols))**2)},
            'finite_joint_averages':moments,'pair_quadratures':quadrature,
            'geometry_ideal_cap':64,'geometry_ideal_count':len(pairs),
            'largest_distance_ratio':fmt(worst),'numerical_predicates':COUNT}

def sum_poly(cols):
    z=ex.ZERO
    for a,c in cols:z=ex.add(z,c)
    return z
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
