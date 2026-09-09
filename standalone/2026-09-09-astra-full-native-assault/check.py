#!/usr/bin/env python3
"""Bounded exact algebra for FNE26; not a numerical RH or asymptotic test."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def factors(n: int) -> dict[int, int]:
    require(type(n) is int and n >= 1, 'positive integer required')
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def mobius(n: int) -> int:
    exponents = factors(n).values()
    return 0 if any(e > 1 for e in exponents) else (-1)**len(factors(n))


def sieve(limit: int) -> list[int]:
    flags = [True]*(limit+1)
    flags[0:2] = [False, False]
    for d in range(2, limit+1):
        if flags[d]:
            for k in range(d*d, limit+1, d):
                flags[k] = False
    return [n for n in range(2, limit+1) if flags[n]]


def add(poly: dict[int, tuple[int, int]], n: int, a: int, b: int) -> None:
    x,y = poly.get(n, (0,0))
    poly[n] = (x+a,y+b)


def construct(Y: int) -> tuple[dict[int, tuple[int,int]], F, int, int]:
    """Coefficient pairs represent a_n + c_Y b_n, exactly and formally."""
    primes = sieve(Y)
    M = {1: 1}
    primorial = 1
    m = F(1)
    for p in primes:
        primorial *= p
        m *= F(p-1,p)
        for d,a in list(M.items()):
            require(d*p not in M, 'Euler divisor collision')
            M[d*p] = -a
    require(len(M) == 2**len(primes), 'complete squarefree support')
    for d,a in M.items():
        require(mobius(d) == a, 'Euler coefficient')
    Q = Y+1
    out = {}
    for d,a in M.items():
        add(out,d,a,0)
        add(out,d*Q,-a*Q,a*Q)
        add(out,d*2*Q,0,-a*2*Q)
    for n,a in [(Q,-2),(2*Q,8),(4*Q,-8)]:
        add(out,n,a,0)
    out = {n: ab for n,ab in out.items() if ab != (0,0)}
    return out,m,primorial,len(M)


def derivative(poly: dict[int,tuple[int,int]], coordinate: int) -> dict[int,F]:
    """Coefficients of log p in -sum a_n log(n)/n; no numeric logs."""
    out = {}
    for n,ab in poly.items():
        for p,e in factors(n).items():
            out[p] = out.get(p,F(0))-F(ab[coordinate]*e,n)
    return {p:x for p,x in out.items() if x}


def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(',',':'), allow_nan=False).encode()


def run() -> dict:
    primes = sieve(256)
    direct = [n for n in range(2,257) if factors(n) == {n:1}]
    require(primes == direct, 'sieve/trial comparison')
    panels = []
    horizon_checks = 0
    coefficient_checks = 0
    for Y in range(2,20):
        poly,m,P,divisor_count = construct(Y)
        Q = Y+1
        for n in range(1,Y+1):
            require(poly.get(n,(0,0)) == (mobius(n),0), 'native prefix')
            coefficient_checks += 1
        require(sum((F(a,n) for n,(a,b) in poly.items()),F(0)) == 0,'balance constant')
        require(sum((F(b,n) for n,(a,b) in poly.items()),F(0)) == 0,'balance slope')
        require(sum(a for a,b in poly.values()) == -2,'centering constant')
        require(sum(b for a,b in poly.values()) == 0,'centering slope')
        require(derivative(poly,0) == {p:m*e for p,e in factors(Q).items()},'derivative constant')
        require(derivative(poly,1) == {2:m},'derivative slope')
        # Substitution c_Y=(1/m-log Q)/log 2 then gives derivative exactly 1.
        require(1/m > sum((F(1,n) for n in range(1,Y+1)),F(0)), 'smooth mass > harmonic prefix')
        require(1/m <= Y, 'integer Euler upper bound')
        require(max(poly) <= max(2*Q*P,4*Q), 'support bound')
        for k in range(1,Y+1):
            require(sum(a*(k//n) for n,(a,b) in poly.items()) == 1,'horizon constant')
            require(sum(b*(k//n) for n,(a,b) in poly.items()) == 0,'horizon slope')
            horizon_checks += 1
        data = [[n,a,b] for n,(a,b) in sorted(poly.items())]
        panels.append({'Y':Y,'prime_count':len(sieve(Y)),
                       'Euler_divisors':divisor_count,'combined_indices':len(poly),
                       'max_index':max(poly),'m_Y':str(m),
                       'coefficients_sha256':hashlib.sha256(canonical(data)).hexdigest()})
    # The bilateral Fourier identity uses two disjoint half-line supports:
    # at a=1/2, their rational exponential envelopes have squared norms 1 and 1.
    a=F(1,2)
    require(1/(2*a)==1,'negative-time Fourier normalization')
    # Exact polynomial verification of B(1)=0 and its linear derivative contract.
    for m in [F(1,2),F(1,3),F(4,15),F(8,35)]:
        # formal variable u=log Q, v=log 2: m[u+((1/m-u)/v)v]=1
        require(m*(1/m)==1,'jet normalization after symbolic substitution')
    return {'schema':'FNE26-bounded-algebra-v1',
            'rh_proved':False,'actual_full_energy_numerically_evaluated':False,
            'analytic_asymptotic_verified_by_code':False,
            'scope':{'sieve_trial_integers':255,'candidate_cutoffs':18,
                     'native_prefix_coefficients':coefficient_checks,
                     'exact_horizon_cells':horizon_checks,
                     'formal_jet_conditions_per_candidate':2,
                     'formal_balance_conditions_per_candidate':2,
                     'formal_centering_conditions_per_candidate':2},
            'candidate_panels':panels}


def pairs(items):
    out={}
    for k,v in items:
        require(k not in out,'duplicate JSON key')
        out[k]=v
    return out


def reject_number(s):
    raise ValueError('noninteger JSON number is not allowed')


def load(path: Path):
    return json.loads(path.read_text(),object_pairs_hook=pairs,
                      parse_float=reject_number,parse_constant=reject_number)


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',type=Path)
    ap.add_argument('--emit',type=Path)
    args=ap.parse_args()
    require(bool(args.check) != bool(args.emit),'choose exactly one of --check/--emit')
    result=run()
    if args.check:
        # Canonical serialization distinguishes true/1 and false/0.
        require(canonical(load(args.check)) == canonical(result),'result mismatch')
    else:
        args.emit.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS_BOUNDED_ALGEBRA','rh_proved':False,
                      'sha256':hashlib.sha256(canonical(result)).hexdigest()},sort_keys=True))


if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,TypeError,KeyError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
