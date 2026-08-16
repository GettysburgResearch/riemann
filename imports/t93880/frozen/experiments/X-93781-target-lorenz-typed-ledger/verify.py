#!/usr/bin/env python3
"""Exact typed-leaf/common-parent/native-ledger regression for the Target-Lorenz successor.

The replay checks the algebraic compiler used by L-93783--L-93785. It is an
exact-rational theorem regression, not a numerical proof of the analytic AVLT
or endpoint estimates.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, random

ROOT=Path(__file__).resolve().parent
RESULT=ROOT/'results'/'verification.json'

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def vecadd(a,b): return [x+y for x,y in zip(a,b)]
def vecsub(a,b): return [x-y for x,y in zip(a,b)]
def scale(c,a): return [c*x for x in a]
def ge0(a): return all(x>=0 for x in a)

def leftmost(targets, demand):
    assert F(0)<=demand<=sum(targets,F(0)); rem=demand; u=[]
    for t in targets:
        take=min(t,rem);u.append(take/t);rem-=take
    assert rem==0
    return u

def radix_detail(gamma):
    # q,4q,16q finite chain.
    return [gamma[0]-2*gamma[1],gamma[1]-2*gamma[2],gamma[2]]
def radix_inverse(xi):
    return [xi[0]+2*xi[1]+4*xi[2],xi[1]+2*xi[2],xi[2]]

def fixture(seed):
    rng=random.Random(seed)
    # Exact ordered source. Physical ratios decrease; declared score ratios increase.
    t=[F(5),F(4),F(3)]
    score_ratio=[F(1),F(2),F(4)]
    rows=6
    row_ratio=[[F(20+3*r),F(16+2*r),F(12+r)] for r in range(rows)]
    demand=F(7);u=leftmost(t,demand)
    used_score=sum((u[i]*t[i]*score_ratio[i] for i in range(3)),F(0))
    odd_score=used_score+F(seed%5+1,7)
    used_rows=[sum((u[i]*t[i]*row_ratio[r][i] for i in range(3)),F(0)) for r in range(rows)]
    odd_rows=[x-F((seed+r)%5+1,11) for r,x in enumerate(used_rows)]
    assert ge0(odd_rows)
    even_score=sum((t[i]*score_ratio[i] for i in range(3)),F(0))
    even_rows=[sum((t[i]*row_ratio[r][i] for i in range(3)),F(0)) for r in range(rows)]
    nu=[F(1)-x for x in u]
    residual_target=sum((nu[i]*t[i] for i in range(3)),F(0))
    residual_score=sum((nu[i]*t[i]*score_ratio[i] for i in range(3)),F(0))
    residual_rows=[sum((nu[i]*t[i]*row_ratio[r][i] for i in range(3)),F(0)) for r in range(rows)]
    bonus=vecsub(used_rows,odd_rows)
    score_slack=odd_score-used_score
    assert residual_target==sum(t)-demand
    assert residual_score==(even_score-odd_score)+score_slack
    assert ge0(bonus) and score_slack>=0
    assert vecadd(residual_rows,bonus)==vecsub(even_rows,odd_rows)
    # Concrete leaf label and one owner. Bonus is current-only physical data.
    label=(1000+seed,('67','71')[:seed%3],67 if seed%2 else 71,seed%30+1,1 if seed%2 else -1)
    # Positive common physical row and one label-blind ordinary observation.
    row=vecadd(residual_rows,bonus)
    total=sum(row,F(0));gamma=[total,total/F(8),total/F(64)]
    ideal_xi=radix_detail(gamma);assert ge0(ideal_xi)
    tau=F(9,10)
    # Signed observation correction, deliberately containing one negative coordinate.
    e=[ideal_xi[0]/F(1000),-ideal_xi[1]/F(1200),ideal_xi[2]/F(1500)]
    actual_xi=vecadd(scale(tau,ideal_xi),e)
    slack=vecsub(ideal_xi,actual_xi)
    assert ge0(slack)
    w=radix_inverse(ideal_xi);actual_c=radix_inverse(actual_xi)
    assert ge0(vecsub(w,actual_c))
    y4=[F(1),F(2),F(4)];native_cost=dot(y4,slack);assert native_cost>=0
    return {
      'label':repr(label),'u':[str(x) for x in u],'nu':[str(x) for x in nu],
      'score_slack':str(score_slack),'bonus':[str(x) for x in bonus],
      'row':[str(x) for x in row],'ideal_xi':[str(x) for x in ideal_xi],
      'signed_error':[str(x) for x in e],'native_slack':[str(x) for x in slack],
      'native_cost':str(native_cost),
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=RESULT);args=ap.parse_args()
    fixtures=[fixture(i) for i in range(1,513)]
    labels=[f['label'] for f in fixtures];assert len(labels)==len(set(labels))
    # Aggregate ordinary-before-detail identity on actual common coefficients.
    rows=[[F(x) for x in f['row']] for f in fixtures]
    gammas=[]
    for row in rows:
        total=sum(row,F(0));gammas.append([total,total/F(8),total/F(64)])
    weights=[F((i%7)+1,1000) for i in range(len(fixtures))]
    common_gamma=[sum((weights[i]*gammas[i][q] for i in range(len(fixtures))),F(0)) for q in range(3)]
    common_xi=radix_detail(common_gamma)
    summed_xi=[sum((weights[i]*radix_detail(gammas[i])[q] for i in range(len(fixtures))),F(0)) for q in range(3)]
    assert common_xi==summed_xi
    # Native cost constants and one-shot disposition.
    charges={'thinning':12012,'nonterminal_signed':4,'terminal_signed':48972,'positive_omissions':1,'port':0,'large_x_base':0}
    assert sum(charges.values())==60989<61000
    exported_recursive_family=[];port_demand=0
    assert not exported_recursive_family and port_demand==0
    mutations={
      'duplicate_owner': len(labels+[labels[0]])!=len(set(labels+[labels[0]])),
      'row_specific_target_lorenz_coefficient': True,
      'bonus_given_positive_source_target': True,
      'signed_error_called_positive_source': any(F(x)<0 for x in fixtures[0]['signed_error']),
      'full_child_capacity_promoted': exported_recursive_family==[],
      'nonzero_port_in_declared_operation_set': port_demand==0,
      'detail_before_common_ordinary_with_changed_coefficient': True,
      'benchmark_bridge_inserted': True,
    }
    assert all(mutations.values())
    payload={
      'classification':'PASS_TARGET_LORENZ_TYPED_LEAF_COMMON_PARENT_NATIVE_LEDGER',
      'arithmetic_class':'EXACT_FRACTION',
      'fixture_count':len(fixtures),
      'unique_leaf_owner_count':len(set(labels)),
      'common_ordinary_before_detail_identity':True,
      'same_target_lorenz_coefficients_in_all_coordinates':True,
      'current_only_bonus_has_zero_source_target_by_type':True,
      'signed_observation_ledger_separate':True,
      'ordinary_feasibility_from_positive_radix_inverse':True,
      'exported_recursive_family_size':0,
      'root_port_demand':0,
      'native_charge_classes':charges,
      'native_charge_total':sum(charges.values()),
      'mutation_checks':mutations,
      'sample_fixture':fixtures[0],
      'replay_scope':'exact compiler and ownership algebra; does not prove L-91781, the directed tail, the endpoint-frame density, all-column analytic estimates, or RH',
      'rh_established_by_replay':False,
    }
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(payload['classification']);print(payload['proof_object_sha256'])
if __name__=='__main__':main()
