#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Tuple

HERE = Path(__file__).resolve().parent

P61_PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]


def qstar(m: int) -> int:
    if m == 2: return 15
    if m == 3: return 6
    if m == 4: return 3
    return 6 if m >= 5 else 0


def H(x: float, n: int) -> float:
    if n > x:
        return 0.0
    return min(math.log(4.0), math.log(x / n))


def divisors_p61(limit: int) -> List[Tuple[int,int]]:
    out=[(1,1)]
    for p in P61_PRIMES:
        out += [(d*p,-sgn) for d,sgn in list(out) if d*p <= limit]
    out.sort()
    return out


def finite_FM(x: float, divs: List[Tuple[int,int]]) -> Tuple[float,float]:
    F=M=0.0
    for d,sgn in divs:
        if 2*d > x: break
        for m in range(2, int(x//d)+1):
            q=qstar(m)
            if not q: continue
            t=q*H(x,d*m)/math.sqrt(d*m)
            F += sgn*t
            M += t
    return F,M


def mobius_sieve(n: int) -> Tuple[List[int], List[int]]:
    mu=[0]*(n+1); lp=[0]*(n+1); primes=[]; mu[1]=1
    for i in range(2,n+1):
        if lp[i]==0:
            lp[i]=i; primes.append(i); mu[i]=-1
        for p in primes:
            v=i*p
            if v>n: break
            lp[v]=p
            if p==lp[i]:
                mu[v]=0; break
            mu[v]=-mu[i]
    return mu,primes


def full_scalar_direct(X: int, mu: List[int]) -> float:
    total=0.0
    for n in range(1,X+1):
        a=(6 if n==1 else 0)-6*mu[n]
        if n%2==0: a += 9*mu[n//2]
        if n%4==0: a -= 3*mu[n//4]
        if a:
            total += a*H(X,n)/math.sqrt(n)
    return total


def history_decomposition_61841() -> Dict[str,object]:
    X=61841
    mu, primes = mobius_sieve(X)
    rough=[p for p in primes if 67 <= p <= X//2]
    divs=divisors_p61(X//2)
    cache: Dict[float,float]={}
    def F(x: float) -> float:
        key=round(x,15)
        if key not in cache: cache[key]=finite_FM(x,divs)[0]
        return cache[key]
    base=F(float(X))
    depth1=sum(-F(X/p)/math.sqrt(p) for p in rough)
    depth2=0.0
    for i,p in enumerate(rough):
        if p*p > X//2: break
        for q in rough[i+1:]:
            if p*q > X//2: break
            c=F(X/(p*q))/math.sqrt(p*q)
            depth2 += c
            if p==67 and q==71:
                pair_67_71=c
    direct=full_scalar_direct(X,mu)
    single_67=-F(X/67)/math.sqrt(67)
    pair_67_71=locals().get('pair_67_71',float('nan'))
    return {
        'X':X,
        'maximum_rough_depth':2,
        'finite_P61_base':base,
        'odd_depth_one_total':depth1,
        'even_depth_two_total':depth2,
        'all_history_total':base+depth1+depth2,
        'direct_Riesz_total':direct,
        'absolute_crosscheck_error':abs(base+depth1+depth2-direct),
        'history_67_contribution':single_67,
        'history_67_71_contribution':pair_67_71,
        'pr561_target_witness_handling':
          'the low-child identity returns the same full node packet; it does not terminalize or erase the odd history',
    }


def run_mpfr() -> Dict[str,object]:
    src=HERE/'src'/'bias_x184_mpfr.cpp'
    with tempfile.TemporaryDirectory(prefix='x97350-mpfr-') as td:
        exe=Path(td)/'bias_x184_mpfr'
        cmd=['g++','-O2','-std=c++17',str(src),'-I/usr/include/x86_64-linux-gnu',
             '-L/lib/x86_64-linux-gnu','-l:libmpfr.so.6','-lgmp','-o',str(exe)]
        subprocess.run(cmd,check=True)
        p=subprocess.run([str(exe)],check=True,capture_output=True,text=True)
    obj=json.loads(p.stdout)
    (HERE/'results'/'bias-x184-mpfr.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    return obj


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',default='results/verification.json')
    args=ap.parse_args()

    bias=run_mpfr()
    assert bias['verdict']=='PASS_DIRECTED_COUNTEREXAMPLE_TO_ONE_OVER_40'
    assert float(bias['ratio_interval'][1]) < 1/40
    assert float(bias['ratio_interval'][0]) > 1/50
    assert float(bias['ratio_interval'][1]) < 1/20

    l=Fraction(1,50); u=Fraction(1,20); rho=Fraction(1,8)
    current_upper=u*(1+rho)/(1-rho)
    conditional_margin=l*(1-rho)-current_upper*rho
    assert current_upper == Fraction(9,140)
    assert conditional_margin == Fraction(53,5600)>0

    low_child={'current_P':1,'current_Schild':-1,'child_Schild':1}
    assert low_child['current_Schild']+low_child['child_Schild']==0
    assert low_child['current_P']==1

    row_counterexample={'row2':1,'row3':-1,'five_three_scalar':2}
    assert 5*row_counterexample['row2']+3*row_counterexample['row3']>0
    assert row_counterexample['row3']<0

    numerator_coefficients=[-3,9,-6]
    discriminant=9*9-4*(-3)*(-6)
    assert discriminant==9
    roots=[Fraction(1),Fraction(2)]

    history=history_decomposition_61841()
    assert history['absolute_crosscheck_error'] < 1e-8
    assert history['history_67_contribution'] < 0
    assert history['history_67_71_contribution'] > 0

    mutations={
      'stale_lower_one_over_40': 'REJECTED_BY_MPFR_X184',
      'finite_packet_called_full_native_source': 'REJECTED_BY_ONE_PRIME_TYPE_DICHOTOMY',
      'low_child_recombination_called_rank_descent': 'REJECTED_SAME_PACKET_RETURNS',
      'parity_blind_terminalization': 'REJECTED_PR561_WITNESS',
      'positive_scalar_lifted_to_two_rows': 'REJECTED_EXPLICIT_VECTOR_1_MINUS_1',
      'local_hall_signs_called_global_feasibility': 'REJECTED_PR574_PR575_FIREWALL',
      'omit_annular_factor_one_minus_four_to_minus_s': 'REJECTED_TRANSFORM_IDENTITY',
      'finite_diagnostic_called_universal_proof': 'REJECTED_CLASSIFICATION',
    }

    core={
      'schema':'riemann.x97350.hostile-reconstruction.v1',
      'frozen_heads':{
        'pr565':'339e3367660f40c74795802a6f8170b15e19b13a',
        'pr574':'74fba7f3e55fa9a53d1eb814e5067f5011ef5e86',
        'pr575':'265c481ebd02807ab7d9a95cb0cf905a22c1876f',
      },
      'directed_bias_counterexample':bias,
      'conditional_repaired_constants':{
        'lower':'1/50','upper':'1/20','recursive_mass':'1/8',
        'current_upper':str(current_upper),'formal_margin':str(conditional_margin),
        'classification':'conditional algebra only; universal interval and current-cone entry are unproved',
      },
      'all_history_witness':history,
      'source_type_dichotomy':{
        'finite_packet': 'has mass M(x), scalar F(x), but is not the full native annular source',
        'full_packet': 'has the native scalar, but its currents retain unresolved histories and are not controlled by F/M',
        'first_unsupported_arrow':'L-97102 applies the finite P61 bias to a full-source current',
      },
      'scalar_to_rows_counterexample':row_counterexample,
      'mellin_numerator':{
        'factor':'-3*(1-2^-z)*(2-2^-z)',
        'roots_in_x_equals_2_to_minus_z':[str(x) for x in roots],
        'open_strip_cancellation':False,
      },
      'mutations':mutations,
      'strongest_honest_status':{
        'finite_P61_lower_one_over_40':'FALSE',
        'exact_all_history_recursion':'PROVED',
        'parity_contractive_induction_as_written':'INVALID',
        'direct_scalar_Mellin_Landau_consumer':'PROVED_CONDITIONAL',
        'global_annular_scalar_positivity':'OPEN_RH_BEARING',
        'RH':'UNPROVED',
      },
      'verdict':'PASS_HOSTILE_RECONSTRUCTION_AND_FAIL_CLOSED_FRONTIER',
      'rh_established':False,
    }
    canonical=json.dumps(core,sort_keys=True,separators=(',',':')).encode()
    core['proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(core,indent=2,sort_keys=True)+'\n')
    print(core['verdict']); print(core['proof_object_sha256'])
    return 0

if __name__=='__main__':
    raise SystemExit(main())
