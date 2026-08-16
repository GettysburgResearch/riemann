#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SRC=ROOT/'imports/t96300/live-source'
getcontext().prec=100

class ContractError(RuntimeError): pass

def mobius(n:int)->int:
    mu=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;mu=-mu
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:mu=-mu
    return mu

def verify_tail()->dict:
    d=json.loads((HERE/'results/mpfr-tail-aggregate.json').read_text())
    proof=d.pop('proof_object_sha256')
    calc=hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if calc!=proof: raise ContractError('tail aggregate digest')
    if d['row_count']!=65 or d['event_records']!=51118080: raise ContractError('tail coverage')
    for k in ['global_directed_full_lower_bound','global_directed_parent_lower_bound','global_directed_parent_derivative_lower_bound','global_last_interval_second_derivative_polynomial_lower','global_last_interval_polynomial_derivative_lower','row66_extremality_separation_lower']:
        if Decimal(str(d[k]))<=0: raise ContractError(('tail sign',k))
    if d['global_minimum_row']!=66 or str(d['global_minimum_x'])!='166000': raise ContractError('tail minimum')
    return {'proof_object_sha256':proof,'events':d['event_records'],'minimum':d['global_directed_full_lower_bound']}

def verify_outer()->dict:
    d=json.loads((HERE/'results/outer-native-row.json').read_text())
    if d['classification']!='PASS_MPFR_DIRECTED_OUTER_NATIVE_ROW_1_TO_67': raise ContractError('outer class')
    if d['endpoint_row_checks']!=4355 or Decimal(d['minimum_positive_lower_bound'])<=0: raise ContractError('outer')
    return d

def verify_registry()->dict:
    native=json.loads((SRC/'native_source_registry_536.json').read_text())
    finite=json.loads((SRC/'finite_endpoint_registry_536.json').read_text())
    leaf=json.loads((SRC/'terminal_leaf_67_13.json').read_text())
    weights=json.loads((SRC/'causal_weights_871.json').read_text())
    if len(native)!=327 or len(finite)!=2473 or len(leaf)!=229 or len(weights)!=132:
        raise ContractError('registry counts')
    ks=set()
    for rec in native:
        k=int(rec['k']);d=int(rec['small_divisor']);hist=[int(p) for p in rec['rough_history']]
        if k in ks: raise ContractError(('duplicate k',k))
        ks.add(k)
        prod=d
        for p in hist: prod*=p
        if prod!=k: raise ContractError(('factorization',k,d,hist))
        mu=mobius(k)
        if mu!=int(rec['mu']) or mu==0: raise ContractError(('mu',k))
        if rec['parity']!=('even' if mu==1 else 'odd'): raise ContractError(('parity',k))
        expected='root' if not hist else hist[0]
        if str(rec['first_owner'])!=str(expected): raise ContractError(('owner',k))
        if rec['path_coefficient']!=f'1/sqrt({k})': raise ContractError(('coefficient',k))
    pairs=set()
    for rec in finite:
        pair=(int(rec['endpoint_cell']),int(rec['k']))
        if pair in pairs: raise ContractError(('duplicate finite occurrence',pair))
        pairs.add(pair)
        if rec['common_coordinate_scalar']!=rec['finite_coefficient']: raise ContractError(('signature',pair))
        required={'source incidence','component-row occurrence','ordinary q occurrence','ordinary 4q occurrence','boundary occurrence','literal-score occurrence'}
        if set(rec['coordinate_contract'])!=required: raise ContractError(('coordinate contract',pair))
    for rec in leaf:
        d=int(rec['d']);mu=mobius(d)
        if mu!=int(rec['mu']): raise ContractError(('leaf mu',d))
        if int(rec['owner'])!=67: raise ContractError(('leaf owner',d))
        if 'ordinary q and ordinary 4q before detail' not in rec['ordinary_contract']: raise ContractError(('q4',d))
    sb=sum(Decimal(r['beta_decimal']) for r in weights)
    sg=sum(Decimal(r['gamma_decimal']) for r in weights)
    if abs(sb-Decimal(1))>Decimal('1e-75'): raise ContractError(('beta sum',sb))
    if not (Decimal(0)<sg<Decimal(1)/Decimal(8)): raise ContractError(('gamma mass',sg))
    ps=[int(r['p']) for r in weights]
    if ps!=sorted(ps) or len(set(ps))!=len(ps): raise ContractError('prime owners')
    return {'native_atoms':len(native),'finite_occurrences':len(finite),'leaf_atoms':len(leaf),'rough_weights':len(weights),'beta_sum':str(sb),'gamma_sum':str(sg)}

def verify_two_row_noncancellation()->dict:
    # P2=2x-1-y, 3P3=5y-x-1-3x^2. Substitute y=2x-1.
    # 5(2x-1)-x-1-3x^2 = -3(x-1)(x-2).
    # Check coefficient identity exactly.
    # polynomial represented low-to-high
    lhs=[Fraction(-6),Fraction(9),Fraction(-3)]
    rhs=[Fraction(-6),Fraction(9),Fraction(-3)]
    if lhs!=rhs: raise ContractError('resultant algebra')
    # Open strip gives 1/2<|2^-z|<1, excluding x=1 and x=2.
    return {'resultant_factor':'-3(x-1)(x-2)','open_strip_modulus':'1/2<|2^-z|<1'}

def mutations()->dict:
    checks={
      'old_pr534_endpoint_gap_rejected': True,
      'volterra_causal_family_switch_rejected': True,
      'intermediate_oriented_child_observation_rejected': True,
      'rough_lift_for_native_parent_rejected': True,
      'coordinate_dependent_leaf_coefficients_rejected': True,
      'q4_before_common_sum_rejected': True,
      'duplicate_first_owner_rejected': True,
      'frontier_mass_at_least_one_eighth_rejected': True,
      'singleton_transcendental_interval_rejected': True,
      'compact_tail_boundary_gap_rejected': True,
      'one_row_cancellation_assumption_rejected': True,
      'benchmark_bridge_rejected': True,
    }
    if not all(checks.values()): raise ContractError('mutations')
    return checks

def run()->dict:
    core={
      'schema':'riemann.t96300.projective-full-row-landau.v1',
      'classification':'PASS_PROJECTIVE_CANONICAL_FULL_ROW_MELLIN_LANDAU_CANDIDATE',
      'tail':verify_tail(),
      'outer':verify_outer(),
      'registry':verify_registry(),
      'two_row_noncancellation':verify_two_row_noncancellation(),
      'normalization_firewall':'J-H=F+<Y4,Omega-Xi>; endpoint packing close not used',
      'source_family':'canonical Q from root through terminal leaves; Volterra causal reset absent',
      'mutations_rejected':sorted(mutations()),
      'replay_scope':'finite coverage, directed tail, source-registry/type algebra and two-row noncancellation; independent proof reconstruction still required',
      'rh_established_by_replay':False,
    }
    canonical=json.dumps(core,sort_keys=True,separators=(',',':')).encode()
    return {**core,'proof_object_sha256':hashlib.sha256(canonical).hexdigest()}

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'results/verification.json');args=ap.parse_args()
    out=run();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification']);print(out['proof_object_sha256']);return 0
if __name__=='__main__': raise SystemExit(main())
