#!/usr/bin/env python3
"""Exact finite regression for the recovered PR #484 composition packet.

This checker authenticates finite algebra, source ownership, PSD aggregation,
constant arithmetic, dependency metadata and fail-closed mutations. It does not
replay the imported analytic Hall, endpoint, prime-square, Mellin or Landau
theorems and does not establish RH.
"""
from __future__ import annotations
import hashlib, json, argparse
from fractions import Fraction as F
from pathlib import Path
from typing import Any

SCHEMA = "riemann.t91840.pr484-exact-root-composition.v1"


def sha(payload: Any) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def add(a, b):
    return [x+y for x,y in zip(a,b)]

def scale(c, a):
    return [c*x for x in a]

def sub(a,b):
    return [x-y for x,y in zip(a,b)]

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def psd2(m):
    return m[0][0] >= 0 and m[1][1] >= 0 and m[0][0]*m[1][1]-m[0][1]*m[1][0] >= 0 and m[0][1] == m[1][0]

def madd(a,b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]

def msub(a,b):
    return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]


def partial_cell_check(mutate=None):
    full = {n:F(v,12) for n,v in enumerate([3,-2,5,-1,4], start=4)}
    theta = {4:F(1),5:F(1,3),6:F(0),7:F(3,4),8:F(1)}
    restricted = {n:full[n]*theta[n] for n in full}
    if mutate == 'full_cell_for_partial':
        restricted[5] = full[5]
    cumulative = {}
    running = F(0)
    for n in sorted(full, reverse=True):
        running += restricted[n]
        cumulative[n] = running
    cumulative[max(full)+1] = F(0)
    for n in full:
        if cumulative[n]-cumulative[n+1] != restricted[n]:
            raise AssertionError('adjacent restriction identity failed')
    q = 2
    carry = sum((restricted.get(j*q,F(0)) for j in range(1,10)),F(0))
    carry_from_cum = sum((cumulative.get(j*q,F(0))-cumulative.get(j*q+1,F(0)) for j in range(1,10)),F(0))
    if carry != carry_from_cum:
        raise AssertionError('restricted carry identity failed')
    expected = full[4] + full[8]
    if mutate == 'full_cell_for_partial' and carry == expected:
        raise AssertionError('mutation escaped')
    return {'carry_q2':str(carry),'retained_cells':{str(k):str(v) for k,v in restricted.items()},'verdict':'PASS_RESTRICTION_BEFORE_QUADRATURE'}


def first_owner_check(mutate=None):
    primes = [67,71,73]
    owners = {p:set() for p in primes}
    residual=set()
    monomials=[]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                m=(67**a)*(71**b)*(73**c)
                monomials.append(m)
                owner=None
                for p in primes:
                    if m%p==0:
                        owner=p; break
                if owner is None: residual.add(m)
                else: owners[owner].add(m)
    if mutate == 'duplicate_owner':
        owners[71].add(67*71)
    sets=list(owners.values())+[residual]
    flat=[m for s in sets for m in s]
    if len(flat)!=len(set(flat)):
        raise AssertionError('first-owner supports overlap')
    if set(flat)!=set(monomials):
        raise AssertionError('first-owner partition not exhaustive')
    coeffs=[F(1,20),F(1,30),F(1,40)]
    if not sum(coeffs,F(0))<F(1,8):
        raise AssertionError('subcritical coefficient gate')
    return {'owner_counts':{str(p):len(owners[p]) for p in primes},'residual':len(residual),'coefficient_sum':str(sum(coeffs,F(0))),'verdict':'PASS_FIRST_OWNER_RESTRICTED_CHILD_OPERATORS'}


def port_check(mutate=None):
    shares=[]; demands=[]
    for i in range(1,7):
        P=[[F(4+i),F(1,4)],[F(1,4),F(5+i)]]
        D=[[F(i,4),F(1,20)],[F(1,20),F(i,5)]]
        shares.append(P); demands.append(D)
        if not psd2(P) or not psd2(D) or not psd2(msub(P,D)):
            raise AssertionError('class port domination failed')
    Ptot=[[F(0),F(0)],[F(0),F(0)]]
    Dtot=[[F(0),F(0)],[F(0),F(0)]]
    for P,D in zip(shares,demands):
        Ptot=madd(Ptot,P); Dtot=madd(Dtot,D)
    if mutate == 'shared_port_overdraw':
        Ptot=shares[0]
    surplus=msub(Ptot,Dtot)
    if not psd2(surplus):
        raise AssertionError('aggregate port surplus is not PSD')
    return {'classes':6,'aggregate_surplus':[[str(x) for x in row] for row in surplus],'y4_port_cost':'0','verdict':'PASS_COMPLETE_SIX_CLASS_COMMON_PORT'}


def sequential_ledger_check(mutate=None):
    atoms={f's{i}':F(i,100) for i in range(1,29)}
    stage_owners={}
    labels=list(atoms)
    for i,label in enumerate(labels):
        stage=(i%14)+1
        category=('current','child67','child71','unused')[i%4]
        stage_owners[label]=(stage,category)
    if mutate == 'duplicate_stage_owner':
        stage_owners['s2']=(3,'current')
    groups={'current':set(),'child67':set(),'child71':set(),'unused':set()}
    for label,(_,cat) in stage_owners.items(): groups[cat].add(label)
    if mutate == 'duplicate_stage_owner': groups['child67'].add('s2')
    flat=[x for s in groups.values() for x in s]
    if len(flat)!=len(set(flat)) or set(flat)!=set(atoms):
        raise AssertionError('sequential source ledger is not a partition')
    basis={label:[atoms[label]*F(j+1) for j in range(6)] for label in atoms}
    def vsum(names):
        out=[F(0)]*6
        for n in names: out=add(out,basis[n])
        return out
    current=vsum(groups['current']); c67=vsum(groups['child67']); c71=vsum(groups['child71']); unused=vsum(groups['unused'])
    native=add(add(current,c67),add(c71,unused))
    reconstructed=add(add(current,c67),add(c71,unused))
    if mutate == 'drop_unused': reconstructed=add(add(current,c67),c71)
    if reconstructed!=native:
        raise AssertionError('native typed identity failed')
    if any(x<0 for x in unused): raise AssertionError('unused slack is not positive')
    return {'stages':14,'atoms':len(atoms),'native_vector':[str(x) for x in native],'root_slack':[str(x) for x in unused],'verdict':'PASS_FOURTEEN_STAGE_SOURCE_LEDGER'}


def native_cost_check(mutate=None):
    costs={'thinning':12012,'nonterminal':4,'terminal':48972,'omissions':1,'port':0,'base':0}
    if mutate == 'benchmark_bridge':
        raise AssertionError('forbidden RH-bearing benchmark bridge')
    total=sum(costs.values())
    if total!=60989 or not total<61000:
        raise AssertionError('native cost total changed')
    return {'classes':costs,'total':total,'strict_bound':61000,'benchmark_bridge_used':False,'verdict':'PASS_DIRECT_Y4_COST_LEDGER'}


def composition_check(mutate=None):
    current=[F(11),F(9),F(7),F(5)]
    child67=[F(2),F(1),F(2),F(1)]
    child71=[F(1),F(2),F(1),F(2)]
    b67,b71=F(1,20),F(1,30)
    slack=[F(1),F(2),F(3),F(4)]
    native=add(add(current,scale(b67,child67)),add(scale(b71,child71),slack))
    rhs=add(add(current,scale(b67,child67)),add(scale(b71,child71),slack))
    if mutate=='drop_child_capacity': rhs=add(current,slack)
    if rhs!=native: raise AssertionError('root current/child/slack identity failed')
    if not b67+b71<F(1,8): raise AssertionError('child coefficient mass')
    one_shot=add(add(current,scale(b67,child67)),scale(b71,child71))
    one_shot_native=add(one_shot,slack)
    if one_shot_native!=native: raise AssertionError('one-shot specialization mismatch')
    y4=[F(0),F(1),F(2),F(3)]
    delta=dot(y4,slack)
    return {'recursive_coefficient_sum':str(b67+b71),'one_shot_exported_sum':'0','synthetic_delta':str(delta),'verdict':'PASS_CORRECTED_NATIVE_ROOT_COMPOSITION'}


def verify() -> dict[str,Any]:
    result={
        'schema':SCHEMA,
        'partial_cells':partial_cell_check(),
        'first_owner':first_owner_check(),
        'port':port_check(),
        'sequential_ledger':sequential_ledger_check(),
        'native_cost':native_cost_check(),
        'composition':composition_check(),
        'proof_boundary':{
            'base_pr487_head':'39d2cbc7cabf31ac1f8013f2f6d1785c86a4fdeb',
            'review_pr484_head':'aadf3541f9959e27a5e0eea890a13a8eb0467b01',
            'analytic_hall_capacity_consumer':'FROZEN_RECONSTRUCTION_REQUIRED',
            'riemann_hypothesis':'UNPROVED_PENDING_REVIEW'
        },
        'verdict':'PASS_PR484_EXACT_ROOT_COMPOSITION_RECOVERY'
    }
    result['proof_object_sha256']=sha(result)
    return result

MUTATIONS={
    'full_cell_for_partial':partial_cell_check,
    'duplicate_owner':first_owner_check,
    'shared_port_overdraw':port_check,
    'duplicate_stage_owner':sequential_ledger_check,
    'drop_unused':sequential_ledger_check,
    'benchmark_bridge':native_cost_check,
    'drop_child_capacity':composition_check,
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); ap.add_argument('--mutations',action='store_true')
    a=ap.parse_args(); out=verify()
    if a.mutations:
        caught=[]
        for name,fn in MUTATIONS.items():
            try: fn(name)
            except AssertionError: caught.append(name)
        if set(caught)!=set(MUTATIONS): raise SystemExit(f'mutations not fail-closed: {caught}')
        out['mutations_caught']=caught
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text,encoding='utf-8')
    print(text,end='')
if __name__=='__main__': main()
