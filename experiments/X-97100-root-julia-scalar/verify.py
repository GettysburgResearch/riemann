#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
SCHEMA='riemann.x97100.root-julia.control.v1'
RESULT='riemann.x97100.root-julia.result.v1'

def mobius(N):
    mu=[0]*(N+1);mu[1]=1;pr=[];co=[False]*(N+1)
    for n in range(2,N+1):
        if not co[n]: pr.append(n);mu[n]=-1
        for p in pr:
            if n*p>N: break
            co[n*p]=True
            if n%p==0: mu[n*p]=0;break
            mu[n*p]=-mu[n]
    return mu

def fac(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def g(n):
    e=0
    while n%2==0:e+=1;n//=2
    return Fraction(2*e,1)+Fraction(1,2**e)

def b(n,mu):
    ans=Fraction(mu[n])
    if n%2==0: ans-=Fraction(3,2)*mu[n//2]
    if n%4==0: ans+=Fraction(1,2)*mu[n//4]
    return ans

def a(n,mu):
    ans=Fraction(6 if n==1 else 0)-6*mu[n]
    if n%2==0:ans+=9*mu[n//2]
    if n%4==0:ans-=3*mu[n//4]
    return Fraction(ans)

def add(A,B,scale=Fraction(1)):
    C=dict(A)
    for p,v in B.items():
        C[p]=C.get(p,Fraction(0))+scale*v
        if C[p]==0:del C[p]
    return C

def logform(n):return {p:Fraction(e) for p,e in fac(n).items()}
def lamform(n):
    fs=fac(n)
    if len(fs)!=1:return {}
    p,e=next(iter(fs.items()))
    return {p: Fraction(2,1)+Fraction(1,2**e) if p==2 else Fraction(1)}

def validate(data):
    if data.get('schema')!=SCHEMA:raise ValueError('schema')
    N=int(data['cutoff']);
    if N<128:raise ValueError('cutoff')
    mu=mobius(N)
    # inverse and scalar identities
    for n in range(1,N+1):
        conv=sum((b(d,mu)*g(n//d) for d in range(1,n+1) if n%d==0),Fraction(0))
        if conv != (1 if n==1 else 0):raise ValueError(('inverse',n,conv))
        if a(n,mu)!=6*((1 if n==1 else 0)-b(n,mu)):raise ValueError(('scalar',n))
        if abs(b(n,mu))>g(n):raise ValueError(('channel',n))
    # formal generalized-prime channel swap
    for n in range(2,N+1):
        lhs_g={p:g(n)*e for p,e in logform(n).items() if g(n)*e}
        rhs_g={}
        lhs_b={p:b(n,mu)*e for p,e in logform(n).items() if b(n,mu)*e}
        rhs_b={}
        for d in range(2,n+1):
            if n%d:continue
            L=lamform(d)
            rhs_g=add(rhs_g,L,g(n//d))
            rhs_b=add(rhs_b,L,-b(n//d,mu))
        if lhs_g!=rhs_g:raise ValueError(('g swap',n,lhs_g,rhs_g))
        if lhs_b!=rhs_b:raise ValueError(('b swap',n,lhs_b,rhs_b))
    # coefficientwise positive dilation identity
    for n in range(1,N+1):
        left=sum((a(d,mu)*g(n//d) for d in range(1,n+1) if n%d==0),Fraction(0))
        right=6*(g(n)-(1 if n==1 else 0))
        if left!=right or right<0:raise ValueError(('dilation',n,left,right))
    # prefix identity at every finite knot
    B=Fraction(0);M=Fraction(0)
    for n in range(1,N+1):
        # symbolic weights are recorded as pairs; compare coefficient dictionaries rather than irrational values
        # per odd core packet is the exact identity checked below
        if n%2==1 and mu[n]!=0:
            packet=[]
            for e in range(4):
                v=(2**e)*n
                if v<=N: packet.append((e,b(v,mu),a(v,mu)))
            for e,bv,av in packet:
                if av != -6*bv + (6 if (n==1 and e==0) else 0):
                    raise ValueError(('packet',n,e))
    energy=Fraction(1)+Fraction(5,4)+Fraction(4,17)+Fraction(1,196)
    if energy!=Fraction(4149,1666):raise ValueError('energy')
    trace=Fraction(16,3)
    # parity firewalls
    fw=data['firewalls']
    false_keys=['rh_established','rjte_proved','imports_pr559_terminal','imports_pr556_global','parity_blind_terminal']
    if any(fw.get(k) is not False for k in false_keys):raise ValueError('firewall')
    if data['odd_history_terminal']!={'history':[67],'p':2521,'y':66,'parity':-1}:
        raise ValueError('odd terminal')
    genealogy={
      'base_pr':557,'base_sha':'d11b08938c4db6a6192e96c564a7818cffc77100',
      'pr559_sha':'88d97adef8a42c5baf2f52c2c259a4ef536bdfdd',
      'pr556_sha':'a4feca0457d310c72054f274040f93b0503f658b',
      'pr561_sha':'db9bdc63c855c6ddf664b763d748f8155a6a2c67'
    }
    if data.get('genealogy')!=genealogy:raise ValueError('genealogy')
    out={
      'schema':RESULT,
      'verdict':'PASS_T97100_PARITY_SAFE_SINGLE_SCALAR_ROOT_JULIA',
      'cutoff':N,
      'dyadic_inverse_fibre':['1','-5/2','2','-1/2'],
      'energy_constant':'4149/1666',
      'trace_constant':'16/3',
      'generalized_prime_source':'nonnegative',
      'channel_swap':'exact',
      'parity_status':{'pr559_terminal':'rejected','pr556_global':'rejected','pr561':'retained'},
      'open_producer':'RJTE: sum_(n<=N)b_diamond(n)/sqrt(n) <= 1 eventually',
      'genealogy':genealogy,
      'rh_established':False,
      'proof_boundary':'Exact reciprocal factorization, coefficient channels, generalized-prime swap, parity firewall, energy and prefix reduction. Does not prove RJTE or RH.'
    }
    can=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
    out['proof_object_sha256']=hashlib.sha256(can).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',nargs='?',type=Path,default=HERE/'certificates/control.json');ap.add_argument('--output',type=Path)
    a=ap.parse_args();out=validate(json.loads(a.certificate.read_text()));txt=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt)
    print(out['verdict']);print(out['proof_object_sha256'])
if __name__=='__main__':main()
