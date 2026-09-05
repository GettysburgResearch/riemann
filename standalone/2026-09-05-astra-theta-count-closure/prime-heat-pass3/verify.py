#!/usr/bin/env python3
"""Finite rational controls, not a machine proof of analytic heat inequalities.

No third-party dependencies, zeros, numerical quadrature, or RH assumption.
All proof-relevant checks use Fraction and remain active under python -O.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import sys

COUNTS: dict[str, int] = {}
Poly = dict[tuple[int, int], F]  # powers of r=1/t and z=ell^2


def check(group: str, condition: bool, explanation: str) -> None:
    if not condition:
        raise ArithmeticError(f"{group}: {explanation}")
    COUNTS[group] = COUNTS.get(group, 0) + 1


def clean(p: Poly) -> Poly:
    return {k: v for k, v in p.items() if v}


def add_term(p: Poly, powers: tuple[int, int], value: F) -> None:
    p[powers] = p.get(powers, F(0)) + value


def time_derivative(p: Poly) -> Poly:
    # (-d/dt)(J*P)/J = (1/4+r/2-z*r^2/4)P + r^2 dP/dr.
    out: Poly = {}
    for (a, b), value in p.items():
        add_term(out, (a, b), value/4)
        add_term(out, (a+1, b), value*(F(1, 2)+a))
        add_term(out, (a+2, b+1), -value/4)
    return clean(out)


def hermite_polynomial(m: int) -> Poly:
    # Independent physicists' H_(2j) finite expansion, with the invariant shift.
    out: Poly = {}
    for j in range(m+1):
        for k in range(j+1):
            value = F(comb(m, j)*(-1)**(j+k)*factorial(2*j),
                      4**m*factorial(k)*factorial(2*j-2*k))
            add_term(out, (2*j-k, j-k), value)
    return clean(out)


def evaluate(p: Poly, r: F, z: F) -> F:
    return sum(value*r**a*z**b for (a, b), value in p.items())


def gamma_half_ratio(m: int, l: int) -> F:
    value = F(1)
    for k in range(l):
        value *= F(1, 1)/F(2*(m-k)-1, 2)
    return value


def run() -> dict[str, object]:
    COUNTS.clear()
    d = F(1, 4)
    # Elementary exponential/logarithm certificates used in the proof.
    e_upper = sum(F(1, factorial(k)) for k in range(5))+F(1,120)/(1-F(1,6))
    check('constants', e_upper < F(11,4), 'Taylor upper bound for e')
    check('constants', sum(F(1,factorial(k)) for k in range(5)) > F(8,3), 'Taylor lower bound for e')
    check('constants', F(11,4)**5 < 4**4, 'exp(5/4)<4')
    check('constants', F(11,4)**2 < 8, 'exp(2)<8')
    check('constants', F(11,4) < 4, 'log 2>1/2')
    check('constants', F(11,4)**16 < 10**8, 'log 10^8>16')
    check('constants', sum(F(3,4)**k/factorial(k) for k in range(4)) > 2, 'log 2<3/4')
    check('constants', F(4,9)+F(3,4)/F(3,2) == F(17,18), 'Euler sum at contour height 2')
    check('constants', 2*(2*d+3*2**2) == 25, 'early contour exponent')
    check('constants', F(3)/F(15,16) < 4, 'sharper contour constant')
    check('constants', 2*4*8*2 == 128, 'adaptive prime factor')
    check('constants', F(13,2) < 7, 'archimedean constant')
    check('constants', F(1,20)*F(11,4) < F(1,2), 'early gamma error')
    check('constants', 10**15/F(1,10) >= (10**8)**2, 'early-order switch')

    for m in range(1,97):
        ratio = F(1)
        for l in range(m+1):
            if l:
                ratio *= F(m-l+1)/F(2*(m-l+1)-1,2)
            check('gamma_coefficients', ratio == factorial(m)//factorial(m-l)*gamma_half_ratio(m,l), 'binomial Gaussian coefficient')
            check('gamma_coefficients', 1 <= ratio <= 2**l, 'all coefficient bounds')
            if 2*l <= m:
                check('low_gamma_coefficients', ratio < 2, 'lower-half coefficient bound')
                reciprocal_sum = sum(F(1, 2*(m-k)-1) for k in range(l))
                check('low_gamma_coefficients', reciprocal_sum <= F(l,m), 'logarithm majorant')
        for q in [F(0),F(1,100),F(1,4),F(1),F(m,16)]:
            coeff = [F(factorial(m),factorial(m-l))*gamma_half_ratio(m,l) for l in range(m+1)]
            low = sum(coeff[l]*q**l/factorial(l) for l in range(m+1) if 2*l<=m)
            check('finite_gamma_majorants', low <= 2*sum(q**l/factorial(l) for l in range(m+1)), 'low finite exponential majorant')
            full = sum(coeff[l]*q**l/factorial(l) for l in range(m+1))
            check('finite_gamma_majorants', full <= sum((2*q)**l/factorial(l) for l in range(m+1)), 'whole finite exponential majorant')
            if q and m>=16*q:
                check('finite_gamma_majorants', F(q,m+1) < F(1,16), 'denominator mass bound')

    for x in [F(-3),F(-1,5),F(0),F(2,3),F(5)]:
        for y in [F(3,5),F(1),F(2),F(4)]:
            lhs = (x*x-y*y+d)**2+4*x*x*y*y
            rhs = (x*x+y*y+d)**2-4*d*y*y
            check('complex_amplitude', lhs==rhs, 'exact complex quadratic modulus')
            check('complex_amplitude', lhs <= (x*x+y*y+d)**2, 'shifted Gaussian envelope')

    for i in range(1,161):
        t = F(i,16)
        y = F(1,2)+1/(t+1)
        check('adaptive_contour', 2*t*y*y == t/2+2-2/(t+1)**2, 'exact adaptive exponent')
        check('adaptive_contour', d+y*y <= F(5,2), 'uniform contour-width premise')
        check('adaptive_contour', (t+1)**2+F(3,4)*(t+1) < 2*(t+1)**2, 'Euler prime majorant')
        check('adaptive_contour', t/2+128*(t+1)**2 < 130*(t+1)**2, 'complete growing-time constant')

    p: Poly = {(0,0):F(1)}
    for m in range(13):
        independent = hermite_polynomial(m)
        check('hermite_identities', p==independent, 'time derivative versus explicit Hermite expansion')
        for r in [F(1,10),F(1),F(3)]:
            # At ell=0, direct Gaussian moments of (x^2+1/4)^m.
            direct=F(0)
            for j in range(m+1):
                moment=F(1)
                for k in range(j):
                    moment *= F(2*k+1,2)*r
                direct += comb(m,j)*d**(m-j)*moment
            check('zero_frequency', evaluate(p,r,F(0))==direct, 'unshifted Fourier mass normalization')
            for z in [F(0),F(1),F(9,4),F(4)]:
                check('hermite_values', evaluate(p,r,z)==evaluate(independent,r,z), 'rational frequency evaluation')
        p=time_derivative(p)
    p1=hermite_polynomial(1)
    check('adversarial', evaluate(p1,F(1),F(0))>0, 'first kernel positive near zero frequency')
    check('adversarial', evaluate(p1,F(1),F(4))<0, 'first kernel negative at other frequency')
    for m in range(1,15):
        check('endpoint', sum(comb(m,j)*(-d)**j*d**(m-j) for j in range(m+1))==0, 'endpoint vanishes for positive order')
    check('adversarial', d**0==1, 'order zero endpoint cannot be removed')

    height=3*10**12; M=10**22; tau=F(1,10)
    check('finite_depth_overlap', F(height**2+1,196)<height**2, 'logarithm numerator')
    check('finite_depth_overlap', F(8,3)**60>height**2, 'first logarithm threshold')
    check('finite_depth_overlap', 2**100>32*height**2, 'second logarithm threshold')
    check('finite_depth_overlap', 2*(M+1)<tau*height**2, 'late-time incomplete-Gamma premise')
    check('finite_depth_overlap', 60*M+100<tau*(height**2-226), 'late-time domination overlap')
    # Multiplicity, endpoint and factorial factors in the mixed heat transfer.
    for A in [F(196),F(200),F(225),F(10000)]:
        for v in [F(1,3),F(1),F(17)]:
            for a in range(7):
                for b in range(7):
                    k=v/(v+A)
                    mixed=sum((-1)**j*comb(b,j)*k**(a+j+1) for j in range(b+1))
                    integral=v**(a+1)*A**b/(v+A)**(a+b+1)
                    check('mixed_transfer', mixed==integral, 'complete Gamma integral transfer')
    return {
        'status':'PASS_ASTRA_PH_FINITE_RATIONAL_CONTROLS',
        'counts':dict(sorted(COUNTS.items())),
        'total_checks':sum(COUNTS.values()),
        'arithmetic':'EXACT_RATIONAL',
        'new_common_time_interval':'0<t<=1/10',
        'new_global_mixed_depth':M,
        'finite_verification_import_height':height,
        'analytic_theorems_machine_proved':False,
        'independent_mathematical_review':False,
        'external_zero_verification_rerun':False,
        'rh_proved':False,
    }


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    try:
        result=run()
        if args.check is not None:
            retained=json.loads(args.check.read_text(encoding='utf-8'))
            if retained!=result:
                raise ArithmeticError('retained JSON differs from fresh exact controls')
        print(json.dumps(result,indent=2,sort_keys=True))
        return 0
    except (ArithmeticError,ValueError,TypeError,OSError) as exc:
        print(f'FAIL_ASTRA_PH: {exc}',file=sys.stderr)
        return 1

if __name__=='__main__':
    raise SystemExit(main())
