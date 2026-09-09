#!/usr/bin/env python3
"""Exact finite source checks. Not an RH proof or a numerical contour evaluation."""
from __future__ import annotations
import argparse, copy, hashlib, json
from fractions import Fraction as F
from pathlib import Path

SCHEMA='astra-critical-source-attack/1'
BASE='f99d9e3908dde4865377c75d9ca051c1f545bf4f'
class CheckError(RuntimeError): pass

def require(c, msg):
    if not c: raise CheckError(msg)

def mobius_trial(n):
    sign=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; sign=-sign
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    return -sign if n>1 else sign

def mobius_sieve(N):
    mu=[1]*(N+1);mu[0]=0; primes=[True]*(N+1)
    if N:primes[0]=primes[1]=False
    for p in range(2,N+1):
        if primes[p]:
            for k in range(p,N+1,p):mu[k]=-mu[k]
            for k in range(p*p,N+1,p):primes[k]=False
            for k in range(p*p,N+1,p*p):mu[k]=0
    return mu

def pair(x):return [x.numerator,x.denominator]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def digest(x):return hashlib.sha256(canonical(x)).hexdigest()
def clean(a):return {k:v for k,v in a.items() if v}

def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,F(0))+v
    return clean(c)

def m(mu,x):return sum((F(mu[k],k) for k in range(1,int(x)+1,2)),F(0))
def M(mu,x):return sum(mu[k] for k in range(1,int(x)+1,2))
def Q(mu,x):return F(M(mu,x))-x*m(mu,x)

def balanced_sources(mu,Y):
    a={k:F(mu[k]) for k in range(1,Y,2) if mu[k]}
    mp=sum((v/k for k,v in a.items()),F(0))
    terminal=add(a,{Y:-Y*mp})
    tail=list(range(Y,2*Y,2));S=sum((F(1,k) for k in tail),F(0));c=-mp/S
    diffuse=add(a,{k:c for k in tail})
    return terminal,diffuse,S,c

def gram(a):
    return sum((va*vb/max(i,j) for i,va in a.items() for j,vb in a.items()),F(0))

def step_energy(a):
    # Independent cumulative-state evaluation of integral A(t)^2/t^2 dt.
    value=F(0);out=F(0);prev=F(1)
    for k,v in sorted(a.items()):
        out+=value*value*(1/prev-F(1,k)); value+=v;prev=F(k)
    return out+value*value/prev

def excess(a,Y,q):
    value=sum((v for k,v in a.items() if k<Y),F(0));prev=F(Y);out=F(0)
    for k,v in sorted((k,v) for k,v in a.items() if k>=Y):
        out+=(value-q)**2*(1/prev-F(1,k));value+=v;prev=F(k)
    return out+(value-q)**2/prev

def integral_m2(mu,Y):
    running=F(0);result=F(0)
    for k in range(1,Y):
        if k%2:running+=F(mu[k],k)
        result+=running*running
    return result

def make_W(N):
    h=[F(0)]*(N+1);cnt=[0]*(N+1)
    for k in range(1,N+1):
        h[k]=h[k-1]+(F(1,k) if k%2 else 0)
        cnt[k]=cnt[k-1]+(k%2)
    def W(z):
        if z<1:return F(0)
        k=z.numerator//z.denominator
        return z*h[k]-cnt[k]
    return W

def quadratic(a,Y,W):
    return sum((v*w*W(F(Y*Y,i*j)) for i,v in a.items() for j,w in a.items()),F(0))

def reconstruct():
    largest=65;N=largest*largest
    mu=mobius_sieve(N)
    require(all(mu[n]==mobius_trial(n) for n in range(1,N+1)), 'primitive mu mismatch')
    W=make_W(N);rows=[];nchecks=0
    for Y in range(3,largest+1,2):
        t,d,S,c=balanced_sources(mu,Y)
        require(sum((v/k for k,v in t.items()),F(0))==0,'terminal balance')
        require(sum((v/k for k,v in d.items()),F(0))==0,'diffuse balance')
        require(S>F(1,4) and abs(c)<8,'diffuse pointwise bounds')
        require(len(range(Y,2*Y,2))==F(Y+1,2),'tail cardinality')
        nchecks+=4
        E=integral_m2(mu,Y);qt=Q(mu,F(Y))
        require(gram(t)==step_energy(t)==E,'minimum-energy identity')
        cumulative=0; integral=F(0)
        for k in range(1,Y):
            if k%2:cumulative+=mu[k]
            integral+=cumulative*cumulative*(F(1,k)-F(1,k+1))
        require(E==integral+qt*qt/Y,'exact M/m/Q energy identity')
        require(gram(d)==step_energy(d)==E+excess(d,Y,qt),'orthogonal excess')
        require(gram(d)>=gram(t),'global energy minimizer')
        nchecks+=4
        bt=quadratic(t,Y,W);bd=quadratic(d,Y,W)
        require(bt==Q(mu,F(Y*Y))-2*qt,'terminal Newton identity')
        require(bd==Q(mu,F(Y*Y))-2*sum(d.values()),'diffuse Newton identity')
        require(abs(bd-bt)<4*Y,'same critical target')
        diag=sum((v*v/k for k,v in d.items()),F(0))
        prefix_diag=sum((F(mu[k]*mu[k],k) for k in range(1,Y,2)),F(0))
        require(diag==prefix_diag+c*c*S and c*c*S<16,'diagonal uniformity')
        nchecks+=4
        a,b,cc=Y,Y+2,Y+4
        h={a:F(a*(b-cc)),b:F(b*(cc-a)),cc:F(cc*(a-b))}
        require(sum(h.values())==sum((v/k for k,v in h.items()),F(0))==0,'two-moment direction')
        changed=add(d,h)
        require(quadratic(changed,Y,W)==bd,'full quadratic completion invariance')
        require(gram(changed)==E+excess(changed,Y,qt),'arbitrary completion orthogonality')
        nchecks+=3
        # Independently check Newton support via direct odd divisor convolution.
        if Y in (3,5,9,17):
            lim=Y*Y;bvec=[F(0)]*(lim+1)
            for n in range(1,lim+1,2):
                bvec[n]=F(n==1)-sum((v for k,v in d.items() if n%k==0),F(0))
            require(all(bvec[n]==0 for n in range(1,Y,2)),'defect support')
            require(sum((bvec[k]*bvec[lim//k] for k in range(1,lim+1,2) if lim%k==0),F(0))==bvec[Y]**2,'square boundary')
            nchecks+=2
        rows.append({'Y':Y,'energy':pair(E),'terminal_mass':pair(qt),'diffuse_mass':pair(sum(d.values())),
                     'diffuse_coefficient':pair(c),'diffuse_diagonal':pair(diag),'energy_excess':pair(gram(d)-E),
                     'terminal_quadratic':pair(bt),'diffuse_quadratic':pair(bd)})
    # The actual source Euler-factor bridge, with all arguments below 1 zero.
    bridges=0
    for x in range(1,1025):
        beta=[0]+[mu[n]-(mu[n//67] if n%67==0 else 0) for n in range(1,x+1)]
        lhs=sum((F(beta[k],k) for k in range(1,x+1)),F(0))
        rhs=m(mu,x)-F(1,2)*m(mu,x//2)-F(1,67)*m(mu,x//67)+F(1,134)*m(mu,x//134)
        require(lhs==rhs,'literal beta / odd source bridge');bridges+=1
    # A legitimate signed zero-balance perturbation can make diagonal energy larger or smaller;
    # full critical energy remains >= the terminal one. Record actual, not synthetic, source rows.
    return {'schema':SCHEMA,'main':BASE,'scope':'finite exact arithmetic only; no RH estimate or contour numerical evaluation',
            'RH_proved':False,'primitive_mu_checks':N,'cutoff_count':len(rows),'source_assertions':nchecks,
            'Euler_bridge_checks':bridges,'rows':rows}

def validate(doc,expected):
    require(type(doc) is dict and set(doc)=={'payload','sha256'},'outer schema')
    require(doc['sha256']==digest(doc['payload']),'payload hash')
    require(canonical(doc['payload'])==canonical(expected),'primitive reconstruction disagreement')

def load(path):
    def pairs(xs):
        d={}
        for k,v in xs:
            require(k not in d,'duplicate JSON key');d[k]=v
        return d
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=lambda s: (_ for _ in ()).throw(CheckError('floats forbidden')))

def tests(expected):
    base={'payload':expected,'sha256':digest(expected)};validate(base,expected);count=0
    changes=[lambda p:p.__setitem__('RH_proved',True),
             lambda p:p.__setitem__('scope','uniform all-cutoff RH proof'),
             lambda p:p['rows'].pop(),
             lambda p:p['rows'][0]['energy'].__setitem__(0,p['rows'][0]['energy'][0]+1),
             lambda p:p['rows'][0]['diffuse_quadratic'].__setitem__(0,p['rows'][0]['diffuse_quadratic'][0]+1),
             lambda p:p.__setitem__('primitive_mu_checks',0),
             lambda p:p.__setitem__('main','0'*40),
             lambda p:p.__setitem__('Euler_bridge_checks',0)]
    for change in changes:
        d=copy.deepcopy(base);before=canonical(d['payload']);change(d['payload'])
        require(canonical(d['payload'])!=before,'no-op mutation');d['sha256']=digest(d['payload'])
        try:validate(d,expected)
        except CheckError:count+=1
        else:raise CheckError('resealed corrupt report accepted')
    require(count==8,'mutation coverage')
    return count

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',type=Path);p.add_argument('--check',type=Path);p.add_argument('--self-test',action='store_true');a=p.parse_args()
    try:
        payload=reconstruct();doc={'payload':payload,'sha256':digest(payload)}
        if a.write:a.write.write_bytes(canonical(doc)+b'\n')
        if a.check:validate(load(a.check),payload)
        rejected=tests(payload) if a.self_test else 0
        print(json.dumps({'PASS':True,'RH_proved':False,'primitive_mu':payload['primitive_mu_checks'],'cutoffs':payload['cutoff_count'],'source_checks':payload['source_assertions'],'Euler_checks':payload['Euler_bridge_checks'],'resealed_rejections':rejected,'sha256':doc['sha256']},sort_keys=True))
        return 0
    except (CheckError,OSError,ValueError,KeyError,TypeError) as e:
        print('ERROR:',e);return 1
if __name__=='__main__':raise SystemExit(main())
