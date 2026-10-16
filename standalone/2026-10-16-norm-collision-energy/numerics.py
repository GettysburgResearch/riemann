#!/usr/bin/env python3
"""Non-certified high-precision finite Gaussian checks; no asymptotic evidence."""
from __future__ import annotations
import json
from fractions import Fraction
import mpmath as mp
from check import complete_ideal_list


def run():
    mp.mp.dps=55
    c=mp.mpf(5)/6; beta=2*c-1
    kc=mp.exp(beta*beta/2)/(2*mp.sqrt(2*mp.pi))
    def val(q): return mp.mpf(q.numerator)/q.denominator
    def Phi(x): return mp.erfc(-x/mp.sqrt(2))/2
    def kernel(D,n,l):
        return kc/mp.sqrt(n*l)*mp.exp(-mp.log(mp.mpf(n)/l)**2/8)*Phi(mp.log(D)-mp.log(n*l)/2-beta)
    cases=[]
    for m,profile,D,tau in [(2,'unit',8,0),(6,'conjugate',64,mp.mpf(1)/3),
                            (2,'mask',64,mp.mpf(-1)/2)]:
        data=complete_ideal_list(64,m,profile)
        terms=[(mp.mpf(n),val(a)) for n,a in data]
        def integrand(x):
            z=mp.fsum(a*mp.exp(1j*tau*mp.log(n)-c*(mp.log(n)-x)-(mp.log(n)-x)**2/4) for n,a in terms)
            return abs(z)**2*mp.exp(-x)/(4*mp.pi)
        integral=mp.quad(integrand,[-mp.inf,-8,0,mp.log(D)])
        pair=mp.re(mp.fsum(a*b*mp.exp(1j*tau*mp.log(n/l))*kernel(D,n,l) for n,a in terms for l,b in terms))
        error=abs(pair-integral)
        if error>mp.mpf('1e-40'): raise ValueError('Gaussian energy mismatch')
        delta_norm=mp.fsum(a*b*kernel(D,n,l) for n,a in terms for l,b in terms if n==l)
        delta_ideal=mp.fsum(a*a*kernel(D,n,n) for n,a in terms)
        cases.append(dict(m=m,profile=profile,D=D,tau=str(tau),ideals=len(data),
                          energy=mp.nstr(pair,18),norm_diagonal=mp.nstr(delta_norm,18),
                          ideal_diagonal=mp.nstr(delta_ideal,18),error_below_1e_minus_40=True))
    # Numerical Fourier integral is separate from the energy-kernel assembly.
    for T,ratio in [(1,mp.mpf(7)/13),(2,mp.mpf(13)/25),(5,mp.mpf(49)/25),(3,mp.mpf(1))]:
        freq=T*mp.log(ratio)
        direct=mp.quad(lambda y:mp.exp(-y*y/2)*mp.cos(freq*y),[-mp.inf,0,mp.inf])/mp.sqrt(2*mp.pi)
        if abs(direct-mp.exp(-freq*freq/2))>mp.mpf('1e-40'):raise ValueError('Fourier mismatch')
    schur=[]
    for N,T in [(1,1),(7,1),(7,8),(64,32)]:
        partial=mp.fsum(mp.exp(-T*T*mp.log(mp.mpf(l)/N)**2/2) for l in range(1,1001) if l!=N)
        bound=N*mp.sqrt(2*mp.pi)/T*mp.exp(mp.mpf(1)/(2*T*T))
        if partial>bound:raise ValueError('Schur bound mismatch')
        schur.append(dict(N=N,T=T,finite_sum=mp.nstr(partial,18),infinite_upper_bound=mp.nstr(bound,18)))
    return dict(status='PASS: ordinary high precision, NOT certified intervals',dps=55,
                finite_gaussian_energy_cases=cases,independent_fourier_quadratures=4,
                schur_partial_sum_checks=schur,
                limitations='Finite coefficients only; mpmath quadrature is not directed rounding, an infinite ideal sum, or independent mathematical review.')

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
