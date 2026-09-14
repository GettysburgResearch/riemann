#!/usr/bin/env python3
"""Deterministic replay for L/T-106710.

This replay verifies exact odd-endpoint anti-carrier Fourier algebra. It does
not prove the physical scale bridge, full source-Pick free-energy bound,
ninety percent, density one, or RH.
"""
from __future__ import annotations
import hashlib, json, math
from pathlib import Path
import sympy as sp

def run() -> dict:
    s, delta, lam = sp.symbols('s delta lam', positive=True)
    u, v = s-delta, s+delta
    exact_checks = 0
    odd_orders = []
    for K in range(1, 16, 2):
        anti = sp.expand((u**K+v**K)*(1-lam**2*u*v))
        split = sp.expand((1-lam**2*s**2)*(u**K+v**K)+lam**2*delta**2*(u**K+v**K))
        assert sp.expand(anti-split) == 0
        exact_checks += 1
        terms=[]
        for j in range((K+1)//2):
            power=2*j+1
            coef=2*(K*math.comb(K,power)-math.comb(K,2*j))
            assert coef >= 0
            terms.append({'power':power,'coefficient':coef})
            exact_checks += 1
        odd_orders.append(K)
    K=5
    anti_adapt=sp.factor((u**K+v**K)*(delta**2/s**2))
    source=sp.factor((v-u)*(v**K-u**K))
    gap5=sp.factor((sp.Rational(K,2)/s)*source-anti_adapt)
    expected_gap5=sp.factor(48*s**3*delta**2+80*s*delta**4)
    assert sp.expand(gap5-expected_gap5)==0
    exact_checks += 2
    x=sp.symbols('x', real=True)
    ratio5=sp.factor(x*((1-x)**5+(1+x)**5)/((1+x)**5-(1-x)**5))
    expected_ratio5=sp.factor((1+10*x**2+5*x**4)/(5+10*x**2+x**4))
    assert sp.factor(ratio5-expected_ratio5)==0
    correction=sp.factor(5*expected_ratio5-1)
    expected_correction=sp.factor((40*x**2+24*x**4)/(5+10*x**2+x**4))
    assert sp.factor(correction-expected_correction)==0
    exact_checks += 2
    payload={
      'schema':'riemann.x106710.carrier-adapted-antiphase.v1',
      'classification':'PASS_T106710_CARRIER_ADAPTED_ANTIPHASE_SOURCE_SOFTENING',
      'exact_checks':exact_checks,
      'odd_orders_checked':odd_orders,
      'all_gap_coefficients_nonnegative':True,
      'k5_positive_gap':str(expected_gap5),
      'k5_conditional_ratio_factor':str(expected_ratio5),
      'k5_conditional_relative_correction':str(expected_correction),
      'xi_conditional_concentration_dependency':'L-106502',
      'physical_scale_bridge_proved':False,
      'balanced_phase_bound_proved':False,
      'full_source_pick_free_energy_bound_proved':False,
      'ninety_percent_established':False,
      'density_one_established':False,
      'rh_established':False,
    }
    proof=json.dumps(payload,sort_keys=True,separators=(',',':'))
    payload['proof_object_sha256']=hashlib.sha256(proof.encode()).hexdigest()
    return payload

if __name__=='__main__':
    out=run()
    Path(__file__).parent.joinpath('results').mkdir(exist_ok=True)
    Path(__file__).parent.joinpath('results/verification.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
