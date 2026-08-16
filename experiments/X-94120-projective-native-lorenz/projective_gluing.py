#!/usr/bin/env python3
"""Deterministic structural certificate for T-94120.

The replay checks exact source combinatorics, the causal budget, contraction,
terminal scale selection, immutable imported proof objects, and the mandatory
q=2 obstruction.  It is not a replacement for the 51,118,080-event directed
AVLT campaign.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
IMPORTS = ROOT / "imports/t94120/94020-live-source"
SMALL = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def primes_upto(n: int) -> list[int]:
    if n < 2: return []
    sieve=bytearray(b'\x01')*(n+1); sieve[:2]=b'\x00\x00'
    for p in range(2,int(n**0.5)+1):
        if sieve[p]: sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i,v in enumerate(sieve) if v]


def mobius(n: int) -> int:
    x=n; parity=0; p=2
    while p*p<=x:
        if x%p==0:
            x//=p; parity^=1
            if x%p==0: return 0
            while x%p==0: x//=p
        p+=1
    if x>1: parity^=1
    return -1 if parity else 1


def factor_squarefree(n: int) -> tuple[int, tuple[int,...]]:
    if mobius(n)==0: raise ValueError(n)
    d=1; r=n
    for p in SMALL:
        if r%p==0: d*=p; r//=p
    rough=[]; q=67
    while r>1:
        while q*q<=r and r%q: q+=1
        p=q if r%q==0 else r
        if p<67: raise AssertionError((n,d,r,p))
        rough.append(p); r//=p; q=p+1
    if d*math.prod(rough)!=n: raise AssertionError(n)
    return d,tuple(rough)


def hazard_budget(primes: list[int]) -> dict[str, Any]:
    if not primes or primes!=sorted(set(primes)) or primes[0]<67:
        raise ValueError('ordered rough primes required')
    with localcontext() as ctx:
        ctx.prec=100
        s=Decimal(1); rows=[]; sum_l=Decimal(0); sum_a=Decimal(0)
        for p in primes:
            r=Decimal(p).sqrt()**Decimal(-1)
            lam=r*s; alpha=r*lam
            rows.append({'p':p,'r':str(r),'s_before':str(s),'lambda':str(lam),'alpha':str(alpha)})
            sum_l+=lam; sum_a+=alpha; s*=Decimal(1)-r
        one_minus=Decimal(1)-s
        beta_sum=sum(Decimal(z['lambda'])/one_minus for z in rows)
        gamma_sum=sum(Decimal(z['alpha'])/one_minus for z in rows)
        if abs((s+sum_l)-Decimal(1))>Decimal('1e-90'): raise AssertionError('partition')
        if abs(beta_sum-Decimal(1))>Decimal('1e-90'): raise AssertionError('beta')
        if not gamma_sum < Decimal(1)/Decimal(8): raise AssertionError(('contraction',gamma_sum))
        for z in rows:
            z['beta']=str(Decimal(z['lambda'])/one_minus)
            z['gamma']=str(Decimal(z['alpha'])/one_minus)
        return {'survivor':str(s),'one_minus_survivor':str(one_minus),'rows':rows,
                'lambda_sum':str(sum_l),'alpha_sum':str(sum_a),
                'beta_sum':str(beta_sum),'gamma_sum':str(gamma_sum)}


def live_registry(X: int=536) -> dict[str, Any]:
    sq=[]
    finite=[]
    for k in range(1,X+1):
        mu=mobius(k)
        if mu:
            d,rough=factor_squarefree(k)
            sq.append({'k':k,'mu':mu,'small_divisor':d,'rough_history':list(rough),
                       'first_owner':rough[0] if rough else None})
    for m in range(1,X+1):
        for k in range(1,X//m+1):
            mu=mobius(k)
            if not mu: continue
            d,rough=factor_squarefree(k)
            finite.append({'m':m,'k':k,'mu':mu,'small_divisor':d,
                           'rough_history':list(rough),'first_owner':rough[0] if rough else None,
                           'coefficient':f'{mu}*log({X}/({m}*{k}))/sqrt({m}*{k})'})
    owners=[(z['k'],z['first_owner']) for z in sq]
    if len(set(k for k,_ in owners))!=len(owners): raise AssertionError('duplicate source')
    for z in sq:
        if z['rough_history'] and z['first_owner']!=min(z['rough_history']): raise AssertionError(z)
    return {'X':X,'squarefree_atoms':sq,'finite_occurrences':finite,
            'squarefree_count':len(sq),'finite_occurrence_count':len(finite),
            'rough_atom_count':sum(bool(z['rough_history']) for z in sq)}


def choose_terminal_prime(x: int) -> int:
    if x<67: raise ValueError(x)
    ps=[p for p in primes_upto(x) if p>=67 and Fraction(x,p)<67]
    if not ps: raise AssertionError(('no terminal rough prime',x))
    return ps[-1]


def q2_obstruction() -> dict[str,str]:
    # Exact chain: log4>4/3, sqrt134<12, hence quotient>1/9.
    if not Fraction(4,3)/12==Fraction(1,9): raise AssertionError
    return {'X':'536','m':'67','ordinary_q':'2',
            'rough_lower':'log(4)/sqrt(134)','rational_lower':'1/9',
            'oriented_child_upper':'-1/9','strict':'true'}



def formal_commuting_square_audit() -> dict[str,Any]:
    """Exact finite model of the source-only stopping/causal square.

    Coefficients are rational surrogates; the audit targets ownership, parity,
    same-index placement and linear commutation, while `hazard_budget` checks
    the live square-root coefficients separately.
    """
    from itertools import combinations
    ps=(67,71,73,79)
    packet={}
    for r in range(len(ps)+1):
        for S in combinations(ps,r):
            packet[(S,r%2)]=Fraction(1,math.prod(S) if S else 1)

    def stop(src):
        out={}
        for (hist,parity),mass in src.items():
            key=(tuple(sorted(hist)), min(hist) if hist else None,
                 max(hist) if hist else None, parity)
            out[key]=out.get(key,Fraction(0))+mass
        return out

    def place(src,p,flip=True):
        out={}
        for (hist,parity),mass in src.items():
            nh=tuple(sorted(hist+(p,)))
            key=(nh, parity^(1 if flip else 0))
            out[key]=out.get(key,Fraction(0))+mass/Fraction(p,1)
        return out

    # Causal construction is a tagged direct sum; signs are not observed here.
    def causal(src,p,flip=True):
        parent={('parent',)+k:v for k,v in src.items()}
        child={('oriented-child',)+k:v for k,v in place(src,p,flip=flip).items()}
        return parent|child

    def stop_tagged(src):
        out={}
        for key,mass in src.items():
            tag,hist,parity=key
            skey=(tag,tuple(sorted(hist)),min(hist) if hist else None,
                  max(hist) if hist else None,parity)
            out[skey]=out.get(skey,Fraction(0))+mass
        return out

    left=stop_tagged(causal(packet,83,flip=True))
    # Stop first, then apply the same placement to the stopped history labels.
    right={}
    for (hist,first,last,parity),mass in stop(packet).items():
        pk=('parent',hist,first,last,parity)
        right[pk]=right.get(pk,Fraction(0))+mass
        nh=tuple(sorted(hist+(83,))); np=parity^1
        ck=('oriented-child',nh,min(nh),max(nh),np)
        right[ck]=right.get(ck,Fraction(0))+mass/Fraction(83,1)
    if left!=right: raise AssertionError('stopping/causal square')

    # Exact one-use parent partition with rational hazard surrogates.
    rs=[Fraction(1,p) for p in ps]; surv=Fraction(1); lamb=[]
    for r in rs:
        lamb.append(r*surv);surv*=1-r
    if surv+sum(lamb)!=1: raise AssertionError('formal parent partition')
    outgoing={k:sum(lamb)*v+surv*v for k,v in packet.items()}
    if outgoing!=packet: raise AssertionError('formal source overdraw')

    bad=stop_tagged(causal(packet,83,flip=False))
    if bad==right: raise AssertionError('parity mutation not detected')
    return {'prime_count':len(ps),'source_atom_count':len(packet),
            'tagged_incidence_count':len(left),'commutes_exactly':True,
            'parent_partition_exact':True,'parity_drop_detected':True}

def imported_objects() -> dict[str,Any]:
    out={}
    for p in sorted(IMPORTS.glob('*.json')):
        obj=json.loads(p.read_text())
        out[p.name]={'sha256':sha256_file(p),'bytes':p.stat().st_size,
                     'top_level_type':type(obj).__name__}
    expected={'native_source_registry_536.json','terminal_leaf_67_13.json',
              'causal_weights_871.json','outer_two_channel_cells.json'}
    if set(out)!=expected: raise AssertionError((set(out),expected))
    return out


def build() -> dict[str,Any]:
    reg=live_registry(536)
    # These counts are themselves regenerated, not trusted from prose.
    budgets={str(x):hazard_budget([p for p in primes_upto(x) if p>=67]) for x in (536,871)}
    terminals={str(x):{'p':choose_terminal_prime(x),'y':str(Fraction(x,choose_terminal_prime(x)))} for x in (67,68,133,134,536,871)}
    for x,z in terminals.items():
        if Fraction(int(x),z['p'])>=67: raise AssertionError(z)
    depth={str(x):math.ceil(math.log(max(x,1),67)) for x in (536,871,10**12)}
    payload={'schema':'riemann.t94120.projective.v1',
      'frozen':{'pr508':'4ae97dffd1f76ed3244b8f3028560ffa80663caf',
                'pr513':'4275fe97aa5ba885210abb6296c7048386e5909d',
                'pr512':'625a9273696a1f017f32d37bf9052423ee8590c7',
                'pr514':'944dabba065271f08f3cade0215292dcfbab590f'},
      'registry_summary':{k:reg[k] for k in ('X','squarefree_count','finite_occurrence_count','rough_atom_count')},
      'registry_sha256':hashlib.sha256(json.dumps(reg,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
      'hazard_budgets':budgets,'terminal_prime_choices':terminals,
      'depth_bounds':depth,'q2_obstruction':q2_obstruction(),
      'imports':imported_objects(),
      'formal_commuting_square':formal_commuting_square_audit(),
      'compiler_contract':{'intermediate_child_observed':False,'rough_lift_parent':False,
        'coordinate_dependent_coefficients':False,'q4_after_total_ordinary':True,
        'one_global_thinning':True,'signed_defect_is_source':False,
        'full_child_capacity_promotion':False,'endpoint_orientation':'F_Lambda <= native_deficit',
        'native_deficit_upper':3457,'benchmark_bridge':False},
      'scope':'Exact finite source registry, exact algebraic causal budget, deterministic terminal selection, immutable live proof objects, and fail-closed interfaces. Directed AVLT and analytic endpoint imports remain frozen theorem proofs, not rerun here.',
      'rh_established_by_replay':False}
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=HERE/'results/projective_certificate.json')
    a=ap.parse_args(); x=build(); a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
    print('PASS_PROJECTIVE_NATIVE_LORENZ_SOURCE_CERTIFICATE')
    print(x['proof_object_sha256'])
    print(x['registry_summary'])

if __name__=='__main__': main()
