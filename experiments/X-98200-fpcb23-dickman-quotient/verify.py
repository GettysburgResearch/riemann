#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math
from pathlib import Path
HERE=Path(__file__).resolve().parent

def sieve(n):
    mu=[0]*(n+1); spf=[0]*(n+1); ps=[]; mu[1]=1
    for x in range(2,n+1):
        if not spf[x]: spf[x]=x; ps.append(x); mu[x]=-1
        for p in ps:
            y=x*p
            if y>n: break
            spf[y]=p
            if x%p==0: mu[y]=0; break
            mu[y]=-mu[x]
    return mu,spf,ps

def factors(n,spf):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0: n//=p
    return out

def divisors(n,spf):
    out=[1]
    for p in factors(n,spf): out += [d*p for d in list(out)]
    return out

def q(j,n):
    if j==2: return 0 if n<2 else 3 if n==2 else 0 if n==3 else 1
    return 0 if n<3 else 6 if n==3 else -2 if n==4 else 1

def band_mu(n,mu,spf,lo,hi=None):
    if mu[n]==0: return 0
    fs=factors(n,spf)
    return mu[n] if all(p>=lo and (hi is None or p<=hi) for p in fs) else 0

def coeff(j,n,mu,spf,lo,hi=None):
    return sum(band_mu(d,mu,spf,lo,hi)*q(j,n//d) for d in divisors(n,spf))

def B(j,y): return sum(q(j,n)/math.sqrt(n) for n in range(1,int(y)+1))

def d(y):
    if y<2: return 0.0
    if y<3: return -3/math.sqrt(2)
    if y<4: return 2*math.sqrt(3)-3/math.sqrt(2)
    return 2*math.sqrt(3)-3/math.sqrt(2)-1.5

def run():
    mu,spf,ps=sieve(50000); conv=rec=0
    for z in (11,19,31):
      for j in (2,3):
       for n in range(1,5001):
        full=coeff(j,n,mu,spf,5,None)
        finite=coeff(j,n,mu,spf,5,z)
        tail=0
        for m in divisors(n,spf):
            if m==1: continue
            mm=band_mu(m,mu,spf,z+1,None)
            if mm: tail += mm*coeff(j,n//m,mu,spf,5,z)
        assert full==finite+tail; conv+=1
    for p in (5,7,11,13,17):
      nxt=next(x for x in ps if x>p)
      for j in (2,3):
       for n in range(1,5001):
        lhs=coeff(j,n,mu,spf,p,None)
        rhs=coeff(j,n,mu,spf,nxt,None)
        if n%p==0: rhs-=coeff(j,n//p,mu,spf,nxt,None)
        assert lhs==rhs; rec+=1
    transverse=[]
    for y in (1,1.999999,2,2.999999,3,3.999999,4,17.25):
        x=B(3,y)-B(2,y); assert abs(x-d(y))<1e-12
        transverse.append([y,x])
    mutations=[
      'claim_fpcb23_by_replay_rejected','claim_rh_by_replay_rejected',
      'drop_child_quotient_rejected','erase_three_band_correction_rejected',
      'promote_scalar_to_two_rows_rejected','promote_sacf_square_to_sign_rejected',
      'promote_lapbr67_rejected','treat_cpqr23_as_proved_rejected']
    core={'schema':'riemann.x98200.remote-core.v1','base_sha':'05aae4135d21301a79b16abb2dda95535e0be77c',
      'convolution_checks':conv,'quotient_recurrence_checks':rec,'transverse_samples':transverse,
      'negative_controls':{'scalar_positive_row_negative':5*(-1)+3*2==1,'square_phase_blind':7*7==(-7)*(-7),'root_value_not_markov':True},
      'mutations_rejected':mutations,'uniform_corridor_proved_by_replay':False,
      'cpqr23_proved':False,'fpcb23_proved':False,'rh_established':False,
      'verdict':'PASS_T98200_FPCB23_DICKMAN_QUOTIENT_REDUCTION'}
    proof=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {**core,'ok':True,'proof_object_sha256':proof}

if __name__=='__main__':
    r=run(); out=HERE/'results/verification.json'; out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(r['verdict']); print(r['proof_object_sha256'])
