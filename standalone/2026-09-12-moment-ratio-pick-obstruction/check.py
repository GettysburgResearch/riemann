#!/usr/bin/env python3
"""Native theta, ten moments, and a parameter-uniform Pick-class obstruction.

This certifies a model-class exclusion, NOT an RH-necessary inequality,
not a nonreal xi zero, and not the analytic proof independent of PROOF.md.
No zero, zeta value, fitted moment or floating-point number is an input.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json
from numeric_core import I, S, BITS, exp_i, pi_i, need

ERROR = F(1, 2**101)  # complete alias + theta tail + spatial lattice tail
N = 10

def coefficients() -> list[F]:
    return [F((-1)**n * (n*n+24*n+90)**2,
              factorial(n-1)*factorial(10-n)) for n in range(1, 11)]

def poly_product_except(n: int) -> list[int]:
    p = [1]
    for j in range(1, 11):
        if j == n:
            continue
        q = [0]*(len(p)+1)
        for k, a in enumerate(p):
            q[k] += j*a
            q[k+1] -= a
        p = q
    return p

def native_moments(den: int = 64) -> list[I]:
    need(isinstance(den, int) and den >= 64, 'mesh denominator must be >=64')
    pi = pi_i()
    need(3*S < pi.lo < pi.hi < 4*S, 'pi guard failed')
    out = [I.point(0) for _ in range(11)]
    for j in range(4*den+1):
        t = F(j, den)
        y = pi*exp_i(I.point(2*t))
        w = I.point(0)
        for n in range(1, 7):
            x = y*n*n
            w += (4*x*x-6*x)*exp_i(-x+t/2)
        scale = F(1 if j == 0 else 2, den)
        for r in range(11):
            out[r] += w*(scale*t**(2*r))
    return [v.widen(ERROR) for v in out]

def ratios(mom: list[I]) -> list[I]:
    need(len(mom) == 11 and all(x.lo > 0 for x in mom),
         'eleven positive native moments required')
    return [2*(2*n-1)*mom[n-1]/mom[n] for n in range(1, 11)]

def bernstein_numerator(v: list[I]) -> list[I]:
    need(len(v) == 10, 'ten coefficient ratios required')
    power = [I.point(0) for _ in range(10)]
    for n, (cn, vn) in enumerate(zip(coefficients(), v), 1):
        for k, a in enumerate(poly_product_except(n)):
            power[k] += cn*n*a*vn
    # P(theta) = sum b_j Binom(9,j)(2 theta)^j(1-2 theta)^(9-j).
    return [sum((power[k]*F(comb(j,k), comb(9,k)*2**k)
                 for k in range(j+1)), I.point(0)) for j in range(10)]

def rational_control() -> tuple[list[F], F]:
    # F(z)=cos(z)cos(4z) has only simple real zeros.
    # Its even moments are (5^(2n)+3^(2n))/2. It also fails our Pick test.
    mom = [F(5**(2*n)+3**(2*n), 2) for n in range(11)]
    v = [2*(2*n-1)*mom[n-1]/mom[n] for n in range(1,11)]
    return v, sum((c*x for c,x in zip(coefficients(), v)), F(0))

def reconstruct(den: int = 64) -> dict:
    c = coefficients()
    # These exact identities remove the nonnegative constant/drift terms.
    need(sum(c) == 0 and sum((n*x for n,x in enumerate(c,1)),F(0)) == 0,
         'constant/drift cancellation failed')
    # Independent exact partial-fraction polynomial identity.
    # Sum c_n n prod_{j != n}(t+j) = t (t^2-24t+90)^2.
    left = [F(0)]*10
    for n, cn in enumerate(c, 1):
        p = [(-1)**k*a for k,a in enumerate(poly_product_except(n))]
        for k,a in enumerate(p): left[k] += cn*n*a
    right = [F(0), F(8100), F(-4320), F(756), F(-48), F(1)] + [F(0)]*4
    need(left == right, 'nonnegative rational kernel identity failed')
    mom = native_moments(den)
    v = ratios(mom)
    q = sum((cn*vn for cn,vn in zip(c,v)), I.point(0))
    need(I.point(F(-146711,10**12)).hi < q.lo and
         q.hi < I.point(F(-146709,10**12)).lo, 'native obstruction interval failed')
    b = bernstein_numerator(v)
    need(all(x.hi < 0 for x in b), 'uniform theta obstruction failed')
    need(all(x.hi < -S//2 for x in b), 'robust polynomial margin failed')
    need(all(x.hi < 66*S for x in v), 'ratio magnitude guard failed')
    # First 9 scalar Bernstein difference tests pass despite the Pick failure.
    differences = []
    row = v[:]
    for k in range(1, 10):
        row = [row[j+1]-row[j] for j in range(len(row)-1)]
        signed = [((-1)**(k+1))*x for x in row]
        need(all(x.lo > 0 for x in signed), 'scalar alternating difference failed')
        differences.append(min(F(x.lo,S) for x in signed))
    cv, cq = rational_control()
    need(cq < 0, 'all-real control must fail the same stronger test')
    sensitivity = factorial(10)*sum(abs(x) for x in c)
    need(sensitivity == 345781760, 'sensitivity identity failed')
    need(F(1,2)-sensitivity*F(1,10**10)>F(46,100),
         'robust ratio-neighborhood bound failed')
    need(F(132,10**13-1) < F(1,10**10),
         'relative moment perturbation bound failed')
    return {'schema': 'MRP26-v1', 'status': 'model-class exclusion, not an RH test',
            'arithmetic_bits': BITS, 'mesh_denominator': den,
            'source_error_per_moment': str(ERROR),
            'moments': [x.record() for x in mom], 'phi_zero': [x.record() for x in v],
            'rational_witness': [str(x) for x in c], 'Q_zero': q.record(),
            'theta_numerator_Bernstein': [x.record() for x in b],
            'scalar_difference_lower_bounds': [str(x) for x in differences],
            'all_real_control_Q': str(cq), 'sensitivity': str(sensitivity),
            'moment_relative_neighborhood': '1/10000000000000'}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--den', type=int, default=64)
    args = parser.parse_args()
    record = reconstruct(args.den)
    if args.check:
        with args.check.open(encoding='utf-8') as f:
            need(json.load(f) == record, 'record differs from complete source reconstruction')
    if args.write:
        args.write.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print('ACCEPT: native ten-moment model-class exclusion; no RH assertion.')
    print('Q(0):', record['Q_zero']['outward_decimal_18'])
    print('max Bernstein upper:', max(record['theta_numerator_Bernstein'],
              key=lambda x: int(x['hi_integer']))['outward_decimal_18'][1])
    print('All-real control Q =', record['all_real_control_Q'])

if __name__ == '__main__':
    main()
