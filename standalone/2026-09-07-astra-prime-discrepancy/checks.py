#!/usr/bin/env python3
"""Bounded EXACT_RATIONAL controls; not a proof of the analytic estimates."""
from __future__ import annotations
import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def pairs_no_duplicates(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError('duplicate JSON key: ' + key)
        out[key] = value
    return out


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs_no_duplicates,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def dump(obj) -> str:
    return json.dumps(obj, indent=2, sort_keys=True, allow_nan=False) + '\n'


def text(x: F) -> str:
    return f'{x.numerator}/{x.denominator}'


def sieve(n: int) -> list[int]:
    a = [True] * (n + 1)
    a[:2] = [False, False]
    for p in range(2, math.isqrt(n) + 1):
        if a[p]:
            for j in range(p*p, n + 1, p):
                a[j] = False
    return [i for i in range(2, n + 1) if a[i]]


def prime_trial(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


def atom_checks(nodes: list[int], amplitudes: list[F]) -> tuple[F, F, F]:
    """Atoms at log(nodes); exact Cauchy norm and full first-order state norm."""
    require(len(nodes) == len(amplitudes) and nodes == sorted(set(nodes)), 'bad atoms')
    q = sum((a*b*F(min(n,m), max(n,m))
             for n,a in zip(nodes,amplitudes)
             for m,b in zip(nodes,amplitudes)), F(0))
    safe = sum((a/F(n) for n,a in zip(nodes,amplitudes)), F(0))
    real_q = sum((a*b*(F(min(n,m), max(n,m))+F(1,n*m))/2
                  for n,a in zip(nodes,amplitudes)
                  for m,b in zip(nodes,amplitudes)), F(0))
    state = F(0)
    energy = F(0)
    for j,(n,a) in enumerate(zip(nodes,amplitudes)):
        state += a*n
        next_term = F(1,nodes[j+1]**2) if j+1 < len(nodes) else F(0)
        energy += state**2 * (F(1,n*n)-next_term)/2
    require(q == 2*energy, 'lost state tail or Fourier factor two')
    require(real_q == energy+safe**2/2, 'wrong real-part correction')
    return q, energy, real_q


def run():
    groups = []
    records = {}
    primes = sieve(512)
    prime_set = set(primes)
    for n in range(2,513):
        require((n in prime_set) == prime_trial(n), 'prime input mismatch')
    groups.append({'name':'sieve_vs_independent_trial_factorization', 'cases':511})

    for n in range(1,65):
        pprod=math.prod(p for p in primes if n < p <= 2*n)
        b=math.comb(2*n,n)
        require(b % pprod == 0 and b < 2**(2*n), 'Chebyshev finite control')
    groups.append({'name':'binomial_prime_divisibility', 'cases':64})

    consts = [F(225,4)<64, F(23,6)<4, F(96)<100, F(2)<F(9,4),
              F(3)+12+14<32, F(2)+F(9,4)<5, F(8)*(1+F(3,4))==14,
              F(2,3)*F(7,2)<3, F(1,4)+10<11]
    for ok in consts:
        require(ok, 'constant comparison')
    groups.append({'name':'rational_majorant_constants', 'cases':len(consts)})

    square_records=[]
    for cutoff in (2,3,5,7,11,13,17,23,31,43,97):
        ps=[p for p in primes if p<=cutoff]
        nodes=[p*p for p in ps]
        coeff=[F(1,2*p) for p in ps]
        q,e,r=atom_checks(nodes,coeff)
        split=sum((F(1,4*p*p) for p in ps),F(0))
        split+=sum((F(p,2*q0**3) for q0 in ps for p in ps if p<q0),F(0))
        require(q==split, 'prime-square diagonal/off-diagonal split')
        require(q<F(121), 'bounded finite square control')
        square_records.append({'cutoff':cutoff,'complex_norm_squared':text(q),
                               'real_norm_squared':text(r)})
    records['prime_square_finite_norms']=square_records
    groups.append({'name':'actual_prime_square_physical_norms', 'cases':11})

    block_count=0
    for lower,upper in ((2,7),(3,13),(7,31),(13,97),(43,97)):
        ps=[p for p in primes if lower<p<=upper]
        atom_checks([p*p for p in ps],[F(1,2*p) for p in ps])
        block_count+=1
    groups.append({'name':'prime_base_tail_endpoint_controls','cases':block_count})

    count=0
    for n in range(2,10):
        nodes=list(range(2,n+2))
        for k in range(3):
            aa=[F((-1)**(j+k)*(j+k+1), (j+2)*(k+1)) for j in range(n)]
            atom_checks(nodes,aa)
            count+=1
    groups.append({'name':'signed_atoms_complete_state_identity','cases':count})

    # Formal logarithmic values are stored as (coefficient of log 2, rational part).
    # Pure uniform density on [log2,log4]: past log2-5/8, future 1/8.
    require(F(-5,8)+F(1,8)==F(-1,2), 'uniform continuum future')
    require(2*F(-1,2)==-1, 'uniform continuum complex norm')
    require(F(-1,2)+F(1,32)==F(-15,32), 'uniform continuum real norm')
    # Add an atom of mass 1/2 at log2: state is 1-exp(-t) then 3exp(-t).
    require(F(-13,32)+F(9,32)==F(-1,8), 'mixed state future')
    require(F(-1,8)+F(1,2)*F(1,2)**2==0, 'mixed real norm log2')
    groups.append({'name':'continuous_and_atomic_normalization_controls','cases':5})

    # Actual first-prime X=2: sqrt2 cancels in every required square.
    require(F(2,2*4)==F(1,4), 'I(2)')
    require(F(1,4)+F(1,8)/2==F(5,16), 'Re C2 norm')
    records['actual_first_prime_X2']={'I':'1/4','c_squared':'1/8','real_norm_squared':'5/16'}
    groups.append({'name':'actual_first_prime_empty_continuum','cases':2})

    # Analytic continuous control: r=X^(delta/2)>=2 ensures r^2-r>=r^2/2.
    for r in (F(2),F(3),F(4),F(11,2)):
        require(r*r-r >= r*r/2,'synthetic integral lower endpoint')
    require(F(1)-F(1,2)==F(1,2),'cosine interval lower bound')
    groups.append({'name':'synthetic_continuous_source_bound_algebra','cases':5})

    return {'status':'PASS_BOUNDED_EXACT_CONTROLS','rh_proved':False,
            'arithmetic':'EXACT_RATIONAL_FINITE',
            'analytic_proofs_machine_verified':False,
            'actual_entropy_or_discrepancy_quadrature_run':False,
            'groups':groups,'total_cases':sum(x['cases'] for x in groups),
            'records':records}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',type=Path)
    ap.add_argument('--verify',type=Path)
    args=ap.parse_args()
    require(not(args.write and args.verify),'choose one mode')
    obj=run()
    if args.verify:
        # Canonical JSON text equality rejects int/float and bool/int aliases.
        require(dump(load_json(args.verify))==dump(obj),'retained result does not match recomputation')
    if args.write:
        args.write.write_text(dump(obj),encoding='utf-8')
    print(dump(obj),end='')

if __name__=='__main__':
    main()
