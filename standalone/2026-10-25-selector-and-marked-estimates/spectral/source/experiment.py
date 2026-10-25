#!/usr/bin/env python3
"""Empirical full-Weil Galerkin/resolvent experiment; NOT interval certification.

All prime powers below exp(2a) and the analytic archimedean tail are included.
Xi enters only the comparison and the explicitly disclosed Gaussian gauge.
No zeta zeros enter the matrix, the shift, or the linear solve.
Requires mpmath. Examples are in NUMERICS.md.
"""
from __future__ import annotations
import argparse
import json
from functools import lru_cache
from pathlib import Path
import mpmath as mp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


@lru_cache(maxsize=8)
def legendre_rule(order: int, dps: int) -> tuple:
    """High-precision Newton roots/weights; not an outward-rounded rule."""
    out = []
    with mp.workdps(dps):
        for k in range(1, order + 1):
            x = mp.cos(mp.pi * (mp.mpf(k) - mp.mpf('.25')) / (order + mp.mpf('.5')))
            for _ in range(32):
                p0, p1 = mp.mpf(1), x
                for j in range(2, order + 1):
                    p0, p1 = p1, ((2*j-1)*x*p1-(j-1)*p0)/j
                derivative = order*(x*p1-p0)/(x*x-1)
                dx = p1/derivative
                x -= dx
                if abs(dx) < 16*mp.eps:
                    break
            else:
                raise RuntimeError('Legendre Newton iteration did not converge')
            p0, p1 = mp.mpf(1), x
            for j in range(2, order + 1):
                p0, p1 = p1, ((2*j-1)*x*p1-(j-1)*p0)/j
            derivative = order*(x*p1-p0)/(x*x-1)
            out.append((x, 2/((1-x*x)*derivative*derivative)))
        out.sort()
        require(abs(mp.fsum(w for _, w in out)-2) < mp.mpf(10)**(-dps+8),
                'Legendre weight mass mismatch')
    return tuple(out)


def primes_to(n: int) -> list[int]:
    flags = bytearray(b'\1')*(n+1)
    flags[:min(n+1, 2)] = b'\0'*min(n+1, 2)
    for p in range(2, int(n**.5)+1):
        if flags[p]:
            flags[p*p:n+1:p] = b'\0'*((n-p*p)//p+1)
    return [p for p in range(2, n+1) if flags[p]]


def prime_power_data(a: mp.mpf) -> list[tuple]:
    upper = int(mp.floor(mp.exp(2*a)))
    result = []
    for p in primes_to(upper):
        n = p
        while n <= upper:
            result.append((n, p, mp.log(n), mp.log(p)/mp.sqrt(n)))
            n *= p
    return sorted(result)


def assemble(a: mp.mpf, modes: int, order: int, include_primes: bool = True):
    """Full matrix in centered orthonormal exponential basis and parity blocks."""
    D = 2*a
    nodes = [(D*(x+1)/2, D*w/2) for x, w in legendre_rule(order, mp.mp.dps)]
    quad = lambda f: mp.fsum(w*f(x) for x, w in nodes)
    data = prime_power_data(a) if include_primes else []
    A = lambda t: mp.exp(-t/2)/(-mp.expm1(-2*t))
    S, diag = {0: mp.mpf(0)}, {}
    constant = mp.log(4*mp.pi)+mp.euler
    for n in range(modes+1):
        k = 2*mp.pi*n/D
        if n:
            S[n] = quad(lambda t: A(t)*mp.sin(k*t)) + mp.fsum(v*mp.sin(k*t) for _, _, t, v in data)
            S[-n] = -S[n]
        # Stable removable singularity: the bracket is O(t) near zero.
        integral = quad(lambda t: 2*A(t)*(-2*mp.sin(k*t/2)**2-mp.expm1(-t/2)-t/D*mp.cos(k*t)))
        diag[n] = (-constant-integral+2*mp.atanh(mp.exp(-D))
                   -2*mp.fsum(v*(1-t/D)*mp.cos(k*t) for _, _, t, v in data))
    def entry(m, n):
        pole = (32*D*mp.sinh(D/4)**2*(D**2-16*mp.pi**2*m*n)
                / ((D**2+16*mp.pi**2*m*m)*(D**2+16*mp.pi**2*n*n)))
        if m == n:
            return pole+diag[abs(n)]
        return (-1)**(m-n)*(pole-(S[m]-S[n])/(mp.pi*(n-m)))
    full = mp.matrix([[entry(m,n) for n in range(-modes,modes+1)]
                      for m in range(-modes,modes+1)])
    even, odd = mp.matrix(modes+1), mp.matrix(modes)
    for i in range(modes+1):
        for j in range(modes+1):
            even[i,j] = (entry(0,0) if i == j == 0 else
                         mp.sqrt(2)*entry(i,j) if i == 0 or j == 0 else
                         entry(i,j)+entry(i,-j))
    for i in range(1,modes+1):
        for j in range(1,modes+1):
            odd[i-1,j-1] = entry(i,j)-entry(i,-j)
    safe = (mp.digamma(mp.mpf('.25'))-mp.log(mp.pi)
            -2*(mp.sinh(a)-a)-2*mp.fsum(t[3] for t in data)-1)
    return full, even, odd, data, safe


def fourier(c, a, z):
    z = mp.mpc(z)
    def sinc(x):
        return mp.mpf(1) if x == 0 else mp.sin(x)/x
    return (c[0]*sinc(a*z)+mp.fsum(c[n]/mp.sqrt(2)*
            (sinc(a*z-mp.pi*n)+sinc(a*z+mp.pi*n))
            for n in range(1,len(c))))/c[0]


def log_coefficients(c, a, count=4):
    """Coefficients of z^(2j) in log F, from convergent Taylor algebra."""
    b = [mp.mpf(1)]+[-mp.sqrt(2)*mp.fsum((-1)**n*c[n]/c[0]/(mp.pi*n)**(2*r)
                     for n in range(1,len(c))) for r in range(1,count+1)]
    f = [a**(2*j)*mp.fsum((-1)**(j-r)*b[r]/mp.factorial(2*(j-r)+1)
                         for r in range(j+1)) for j in range(count+1)]
    log = [mp.mpf(0)]
    for j in range(1,count+1):
        log.append(f[j]-mp.fsum(r*log[r]*f[j-r] for r in range(1,j))/j)
    return log[1:]


def xi(z):
    s = mp.mpf('.5')+1j*z
    if s == 0 or s == 1:
        return mp.mpf('.5')
    return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)/2


def format_real(x, digits=40):
    return mp.nstr(mp.re(x),digits)


def sample_case(E, c, shift, a, reference_variance, label):
    c /= c[0]
    logs = log_coefficients(c,a)
    variance = -2*logs[0]
    points = [('1',mp.mpf(1)),('5',mp.mpf(5)),('10',mp.mpf(10)),
              ('14',mp.mpf(14)),('20',mp.mpf(20)),('i',mp.j),('0.3+i',mp.mpf('.3')+mp.j)]
    samples = []
    for name,z in points:
        F = fourier(c,a,z)
        X = xi(z)/xi(0)
        H = mp.exp((variance-reference_variance)*z*z/2)*F
        samples.append({'z':name,'raw_error':format_real(abs(F-X),24),
                        'gaussian_compensated_error':format_real(abs(H-X),24),
                        'F_real':format_real(F),'F_imag':format_real(mp.im(F))})
    r = (E-shift*mp.eye(E.rows))*c
    # Normalized solve should have no component away from the forcing vector.
    residual = max([abs(r[k]) for k in range(1,E.rows)]+[mp.mpf(0)])
    return {'kind':label,'shift':format_real(shift),'variance':format_real(variance),
            'log_coefficients_z2_to_z8':[format_real(v) for v in logs],
            'normalized_even_coefficients':[format_real(v,60) for v in c],
            'projected_matrix_residual':format_real(residual,12),'samples':samples}


def run(a_text: str, modes: int, dps: int, order: int, include_primes=True) -> dict:
    require(modes>=1 and dps>=50 and order>=2*modes+8,'Invalid numerical resolution')
    with mp.workdps(dps):
        a = mp.mpf(a_text)
        require(0<a<=5,'This bounded experiment supports 0<a<=5')
        full,E,O,data,safe = assemble(a,modes,order,include_primes)
        even_values = mp.eigsy(E,eigvals_only=True)
        odd_values = mp.eigsy(O,eigvals_only=True)
        low = min(even_values[0],odd_values[0])
        e0=mp.matrix([1]+[0]*modes)
        # All eigenvalue-dependent choices are EMPIRICAL finite-matrix choices.
        require(abs(low)>mp.mpf(10)**(-dps+25),'Precision insufficient to resolve smallest eigenvalue')
        gap = abs(low)*mp.mpf('1e-12')
        near = low-gap
        with mp.workdps(min(dps,70)):
            vx = mp.re(-mp.diff(lambda z:xi(z)/xi(0),0,2))
        cases=[]
        for label,shift in [('explicit_safe_shift',safe),('near_finite_bottom',near),('fixed_gap_1e-6',low-mp.mpf('1e-6'))]:
            c=mp.lu_solve(E-shift*mp.eye(modes+1),e0)
            cases.append(sample_case(E,c,shift,a,vx,label))
        return {'status':'EMPIRICAL_NOT_INTERVAL_CERTIFIED','halfwidth':str(a),
                'modes_each_side':modes,'full_dimension':2*modes+1,
                'precision_decimal_digits':dps,'quadrature_nodes':order,
                'prime_terms_included':include_primes,
                'prime_powers':[{'n':n,'prime':p} for n,p,_,_ in data],
                'even_min':format_real(even_values[0]),'odd_min':format_real(odd_values[0]),
                'second_even':format_real(even_values[1]),
                'reference_xi_variance':format_real(vx,60),'cases':cases,
                'mpmath_version':mp.__version__}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a',default='1.3');parser.add_argument('--modes',type=int,default=16)
    parser.add_argument('--dps',type=int,default=120);parser.add_argument('--order',type=int,default=192)
    parser.add_argument('--omit-primes',action='store_true',help='Negative-control source, not the full Weil form')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report=run(args.a,args.modes,args.dps,args.order,not args.omit_primes)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':str(args.output),'status':report['status'],
                      'even_min':report['even_min'],'odd_min':report['odd_min']},sort_keys=True))
