#!/usr/bin/env python3
"""Finite exact controls, not a machine proof of the analytic manuscript.

Standard library only. No assert-based acceptance, floating-point special
functions, actual xi matrix evaluation, or finite-to-infinite extrapolation.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PROOF_HASH = '132022d080f582bd5776d410aa482280685b581b4140239294f4244f9a844efe'
LOCK_HASH = '7bcf756f778ce0479c6848e365d30ea09b73d6c17ab19679afded3e207fa1d91'
BASE = 'c64a0ae131d60cce48bc0dcc73358f7a1a857a89'


def fail(message: str) -> None:
    raise ValueError(message)


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            fail('duplicate JSON key: ' + key)
        out[key] = value
    return out


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


def authenticate() -> None:
    for name, digest in [('PROOF.md', PROOF_HASH), ('SOURCE_LOCK.json', LOCK_HASH)]:
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
            fail('source hash mismatch: ' + name)
    lock = load_json(HERE / 'SOURCE_LOCK.json')
    if lock['base_commit'] != BASE or lock['rh_proved'] is not False:
        fail('source scope mismatch')


class Checks:
    def __init__(self) -> None:
        self.groups: dict[str, int] = {}
    def require(self, group: str, condition: bool) -> None:
        if not condition:
            fail('finite control failed: ' + group)
        self.groups[group] = self.groups.get(group, 0) + 1


def poly_add(*vectors: list[F]) -> list[F]:
    n = max(map(len, vectors), default=0)
    return [sum((v[i] if i < len(v) else F(0) for v in vectors), F(0))
            for i in range(n)]


def poly_mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def poly_scale(v: list[F], c: F) -> list[F]:
    return [c*x for x in v]


def poly_derivative(v: list[F]) -> list[F]:
    return [F(i)*v[i] for i in range(1, len(v))]


def rational_string(value: F) -> str:
    return f'{value.numerator}/{value.denominator}'


def build() -> dict[str, Any]:
    authenticate()
    c = Checks()
    # Finite exponential series with a rigorous elementary positive tail.
    e_upper = sum((F(1, math.factorial(k)) for k in range(11)), F(0))
    e_upper += F(12, 11*math.factorial(11))
    c.require('elementary_constants', e_upper < F(11,4))
    c.require('elementary_constants', e_upper < 3)
    c.require('elementary_constants', F(11,4)**12 < 12**5)
    c.require('elementary_constants', F(11,4)**2 < 8)
    c.require('elementary_constants', F(10,7)**2 > 2)
    c.require('elementary_constants', F(5,2)**2 > 6)
    exp_lower = sum((F(39,20)**k/F(math.factorial(k)) for k in range(21)), F(0))
    c.require('elementary_constants', exp_lower > 7)
    h6 = sum((F(1,k) for k in range(1,7)), F(0))
    c.require('elementary_constants', h6 == F(49,20))
    c.require('elementary_constants', h6-F(39,20) == F(1,2))

    # Bound 1/a<=6l, with l=1+t, is the polynomial 3+12t+5t^2>=0.
    c.require('contour_constants', [F(3),F(12),F(5)] ==
              poly_add(poly_scale(poly_mul([F(1),F(1)],[F(2),F(1)]),F(6)),
                       poly_scale(poly_mul([F(3),F(1)],[F(3),F(1)]),F(-1))))
    c.require('contour_constants', all(x>0 for x in [F(3),F(12),F(5)]))
    c.require('contour_constants', F(3)*4*F(5,2)/2 == 15)
    c.require('contour_constants', 15 < 16)
    c.require('contour_constants', F(3)*4*3*F(5,2) == 90)
    c.require('contour_constants', F(90)+F(16,2) < 100)
    c.require('contour_constants', F(2) < 4)  # sqrt(2)/2 < 1
    for ell in [F(1),F(3,2),F(2),F(7),F(30),F(1000)]:
        y=F(1,2)-1/(ell+2)
        a=F(1,4)-y*y
        c.require('contour_algebra', a == (ell+1)/(ell+2)**2)
        c.require('contour_algebra', 1/a <= 6*ell)
        c.require('contour_algebra', -y*ell == -ell/2+ell/(ell+2))
    # Complete-square exponent in the exact continuum primitive.
    for v, ell in [(F(1,3),F(2)),(F(1),F(5)),(F(4),F(1)),(F(17,2),F(31,5))]:
        c.require('continuum_exponents', -(ell-v)**2/(4*v) ==
                  -v/4+ell/2-ell*ell/(4*v))

    # The scalar K_0 resolvent entries, pi factored out.
    for a,b in [(F(1),F(2)),(F(3,2),F(5,2)),(F(2),F(4)),(F(5,4),F(7,4))]:
        p,q=a*a-F(1,4),b*b-F(1,4)
        c.require('gaussian_resolvent', (1/a-1/b)/(q-p)==1/(a*b*(a+b)))
        c.require('gaussian_resolvent', p>0 and q>0)

    # Antiderivative: d_T[e^(-cT)(T^2/c+2T/c^2+2/c^3)]=-T^2 e^(-cT).
    for rate in [F(1,7),F(1,2),F(1),F(3),F(11,2)]:
        p=[2/rate**3,2/rate**2,1/rate]
        lhs=poly_add(poly_derivative(p), poly_scale(p,-rate))
        c.require('pnt_tail_antiderivative', lhs==[F(0),F(0),F(-1)])

    # Formal source jet at s=2, in basis (1,gamma_E,log pi,log2,pi^2,(log2)^2).
    F2=[F(1),F(-1,2),F(-1,2),F(-1,4),F(0),F(0)]
    Fp2=[F(-3,4),F(0),F(0),F(1,2),F(1,24),F(1,4)]
    numerator=poly_add(poly_scale(F2,F(2)),poly_scale(Fp2,F(-3)))
    expected=[F(17,4),F(-1),F(-1),F(-2),F(-1,8),F(-3,4)]
    c.require('actual_X2_formal_jet', numerator==expected)
    c.require('actual_X2_formal_jet', (2*F(2)-1)**3==27)
    margin=(F(17,4)-F(1,2)-F(12,5)-F(9,8)-F(1,3))/27
    c.require('actual_X2_margins', margin==F(-13,3240))
    density= -1-F(14,15)+F(12,7)
    c.require('actual_X2_margins', density==F(-23,105))
    c.require('actual_X2_margins', margin<0 and density<0)
    # Trace identity at X=2: base plus log2/4 = (2-gamma-log(2pi))/4.
    trace_base=[F(1,2),F(-1,4),F(-1,4),F(-1,2)]
    trace_cut=poly_add(trace_base,[F(0),F(0),F(0),F(1,4)])
    c.require('trace_normalizations', trace_cut==[F(1,2),F(-1,4),F(-1,4),F(-1,4)])
    trace_limit=poly_add(trace_base,[F(0),F(1,2),F(0),F(0)])
    c.require('trace_normalizations', trace_limit==[F(1,2),F(1,4),F(-1,4),F(-1,2)])
    c.require('trace_normalizations', F(1,2)+F(3,2)==2)
    # Check original-L2 Gram and abstract all-rank domination independently.
    nodes=[F(1),F(2),F(4)]
    for coeff in [[F(1),F(-2),F(1)],[F(-3),F(1),F(5)],[F(1),F(1),F(-1)]]:
        gram=sum((coeff[i]*coeff[j]/(nodes[i]+nodes[j])
                  for i in range(3) for j in range(3)), F(0))
        c.require('original_metric_controls', gram>0)
        # Rank-one f=e^-t contribution is dominated by ||f||^2 times Gram.
        pairing=sum((coeff[i]/(nodes[i]+1) for i in range(3)),F(0))
        c.require('original_metric_controls', pairing**2<=gram/2)

    return {'status':'PASS_FINITE_EXACT_CONTROLS', 'arithmetic':'fractions_only',
            'base_commit':BASE, 'proof_sha256':PROOF_HASH,
            'groups':c.groups, 'finite_comparisons':sum(c.groups.values()),
            'actual_X2_test_upper_bound':rational_string(margin),
            'actual_X2_density_upper_bound':rational_string(density),
            'claims':{'rh_proved':False,'all_rank_source_sign_proved':False,
                      'analytic_proofs_machine_checked':False,
                      'explicit_numeric_PNT_constants_certified':False},
            'scope':'Finite algebra and constant controls only; analytic arguments require proof review.'}


def type_equal(a: Any,b: Any) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(type_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(type_equal(x,y) for x,y in zip(a,b))
    return a==b


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', type=Path)
    args=ap.parse_args()
    result=build()
    if args.check and not type_equal(load_json(args.check),result):
        fail('saved result mismatch (including exact types)')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError) as exc:
        raise SystemExit('REFUSED: '+str(exc))
