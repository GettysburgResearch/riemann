#!/usr/bin/env python3
"""Rigorous interval size check for the historical constant discrepancy.
Requires python-flint0.9.0 (Arb); the proof in the audit is independent of this check.
Run with PYTHONPATH=/workspace/riemann-runtime in the current research workspace.
"""
from pathlib import Path
import json
from flint import arb, ctx
ctx.prec=192
s=arb(1)/2
xi_half=(s*(s-1)/2)*arb.pi()**(-s/2)*(s/2).gamma()*s.zeta()
modern_constant=-(arb(2).log())
original_constant=xi_half.log()
correction=((arb(1)/2)/xi_half).log()
if not (xi_half>0 and xi_half<arb(1)/2 and correction>0):
    raise ArithmeticError('Required interval separation failed')
out={'status':'rigorous interval inequalities passed','precision_bits':ctx.prec,
     'library':'python-flint0.9.0, Arb interval special functions',
     'xi_modern_half_equals_xi_R_zero':str(xi_half),
     'original_real_constant_log_xi_R_zero':str(original_constant),
     'corrected_real_constant_minus_log_two':str(modern_constant),
     'positive_correction_to_add':str(correction),
     'scope':'Checks size only. No numerical zeros or RH assumption. Exact product normalization and historical primary sources carry the proof.'}
p=Path('/workspace/riemann-observatory/experiments/results/riemann_constant_arb_round4.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
