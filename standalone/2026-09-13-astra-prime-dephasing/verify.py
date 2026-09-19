#!/usr/bin/env python3
"""PPD26 independent implementation; strict exact finite acceptance."""
import argparse, copy, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def serial(v): return json.dumps(v,sort_keys=True,separators=(',',':'))
def sha(v): return hashlib.sha256(serial(v).encode()).hexdigest()
def pair(v): return [v.numerator,v.denominator]
def require(ok,msg):
    if not ok: raise ValueError(msg)

def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def norm(a):
    # Complete finite max-kernel, with the terminal cancellation at X.
    s=0;v=F(0)
    for n in range(1,len(a)):
        v+=F(a[n]*(2*s+a[n]),n);s+=a[n]
    return v-F(s*s,len(a))

def grouped(a,keys):
    totals={};v=F(0); X=len(a)
    for n in range(1,X):
        g=keys[n];s=totals.get(g,0)
        v+=F(a[n]*(2*s+a[n]),n);totals[g]=s+a[n]
    return v-sum((F(s*s,X) for s in totals.values()),F(0))

def rough_at(mu,fs,ps,u):
    if u<=1:return F(0)
    last=(u.numerator-1)//u.denominator
    # Max-kernel source up to floor(u-0), endpoint may be rational.
    a=[0]+[mu[n] if not any(p in fs[n] for p in ps) else 0 for n in range(1,last+1)]
    s=0;v=F(0)
    for n in range(1,last+1):v+=F(a[n]*(2*s+a[n]),n);s+=a[n]
    return v-F(s*s)/u

def subsets(ps,limit=None):
    ds=[1]
    for p in ps:ds += [d*p for d in ds[:] if limit is None or d*p<limit]
    return sorted(ds)

def multiplier(N,ps,fs):
    S=set(ps);scale=2**96;v=F(0);rows=[]
    for n in range(1,N+1):
        f=fs[n]
        if set(f)<=S:
            r=2**len(f); inv=r*(-1)**sum(f.values());sq=int(max(f.values(),default=0)<=1)
            root=math.isqrt((scale*scale)//n)
            require(root*root*n<=scale*scale<(root+1)**2*n,'sqrt enclosure')
            v+=F(r*(root+1),scale); rows.append([n,r,inv,sq])
    # The ratio and its reciprocal compose to the identity at every index.
    direct={n:a for n,a,_,_ in rows};back={n:b for n,_,b,_ in rows}
    for n in range(1,N+1):
        require(sum(direct.get(d,0)*back.get(n//d,0) for d in range(1,n+1) if n%d==0)==int(n==1),'Euler inverse')
    return v,rows

def panel(X,ps,mu,fs,enumerate_all):
    keys=[tuple(p for p in ps if p in fs[n]) for n in range(X)]
    native=norm(mu[:X]); mean=sum((rough_at(mu,fs,ps,F(X,d))/d for d in subsets(ps,X)),F(0))
    rough=rough_at(mu,fs,ps,F(X)); diag=sum((F(mu[n]**2)*(F(1,n)-F(1,X)) for n in range(1,X)),F(0))
    a=mu[:X];stages=[];sig=[];active=set(ps);cur=mean
    require(grouped(a,keys)==mean,'rough/Walsh identity')
    for p in ps:
        active.remove(p)
        newkeys=[tuple(q for q in keys[n] if q in active) for n in range(X)]
        minus=[a[n]*(-1 if p in fs[n] else 1) for n in range(X)]
        plusE=grouped(a,newkeys);minusE=grouped(minus,newkeys)
        B=(plusE-minusE)/4
        require((plusE+minusE)/2==cur,'conditional expectation')
        sign=-1 if minusE<plusE else 1
        a=minus if sign==-1 else a;cur=min(plusE,minusE);sig.append(sign)
        stages.append([p,sign,pair(B),pair(cur)])
    require(norm(a)==cur,'signing output')
    mass,rows=multiplier(X-1,ps,fs)
    require(native/mass**2<=cur<=native*mass**2,'member comparison')
    t={'X':X,'primes':ps,'native':pair(native),'rough':pair(rough),'mean':pair(mean),'diagonal':pair(diag),
       'cross':pair(mean-diag),'signed':pair(cur),'signs':sig,'stages':stages,'mass_upper':pair(mass),
       'local_factors_hash':sha(rows)}
    if enumerate_all:
        vals=[]
        for mask in range(2**len(ps)):
            # Same lexicographic order as [1,-1]^k, without importing producer.
            flip={p for j,p in enumerate(ps) if mask&(1<<(len(ps)-1-j))}
            # Euler quotient times the unmodified Mobius source.
            r=[0]*X
            for n in range(1,X):
                if set(fs[n])<=flip:r[n]=2**len(fs[n])
            v=[0]*X
            for d in range(1,X):
                if r[d]:
                    for k in range(1,(X-1)//d+1):v[d*k]+=r[d]*mu[k]
            require(all(v[n]==mu[n]*(-1)**sum(p in fs[n] for p in flip) for n in range(1,X)),'native twist')
            val=norm(v); vals.append(val)
            require(native/mass**2<=val<=native*mass**2,'uniform family comparison')
        require(sum(vals,F(0))/len(vals)==mean,'complete family')
        t.update({'family_size':len(vals),'minimum':pair(min(vals)),'maximum':pair(max(vals)),
                  'family_hash':sha([pair(v) for v in vals])})
    else:t.update({'family_size':2**len(ps),'family_enumerated':False})
    return t

def reconstruct():
    fs=[{}]+[factors(n) for n in range(1,1025)]
    primes=[n for n in range(2,1025) if fs[n]=={n:1}]
    mu=[0]+[(-1)**len(f) if max(f.values(),default=0)<=1 else 0 for f in fs[1:]]
    panels=[panel(X,[p for p in primes if p<=y],mu,fs,True) for X in [8,16,32,64,128,256] for y in [2,3,5,7,11]]
    large=[panel(X,[p for p in primes if p<=(X.bit_length()-1)**2],mu,fs,False) for X in [16,32,64,128,256,512,1024]]
    def r(y,x):return sum(mu[n] for n in range(1,x+1) if not fs[n] or min(fs[n])>y)
    rec=[]
    for y in [2,3,5,7,11]:
        for x in range(1,129):
            val=r(y,x)
            require(val==1-sum(r(p,x//p) for p in primes if y<p<=x),'Buchstab')
            rec.append([y,x,val])
    blocks=[]
    for y in [2,3,5,7,11,17]:
        for x in range(1,y*y+1):
            val=r(y,x);require(val==1-sum(y<p<=x for p in primes),'prime-only')
            blocks.append([y,x,val])
    comb=[]
    for y in [5,7,11,13,17,19]:
        ps=[p for p in primes if p<=y]
        for r0 in range(1,min(3,len(ps))+1):
            ds=sorted(d for d in subsets(ps) if len(factors(d))==r0)
            require(len(ds)==math.comb(len(ps),r0) and max(ds)<=y**r0,'counting lower')
            comb.append([y,r0,len(ds),y**(2*r0),pair(F(len(ds)**2,4*y**r0)),sha(ds)])
    full={'schema':'PPD26-1','status':'PROPOSED; RH estimate OPEN','parent':'99101457b32b6f10f4eda88ca998048404b860ea',
          'scope':'finite exact arithmetic; no asymptotic norm or RH inference','panels':panels,'dyadic_bank_panels':large,
          'buchstab':{'cases':len(rec),'hash':sha(rec)},'prime_only':{'cases':len(blocks),'hash':sha(blocks)},
          'combinatorial':comb,'mu_hash':sha(mu),
          'counts':{'complete_ensembles':30,'enumerated_signatures':sum(t['family_size'] for t in panels),'dyadic_ensembles':7,
                    'dyadic_signatures_not_enumerated':sum(t['family_size'] for t in large),
                    'signing_stages':sum(len(t['stages']) for t in panels+large)}}
    scale=2**32
    def summary(t):
        out={k:t[k] for k in ('X','primes','family_size','signs')}
        for k in ('native','rough','mean','diagonal','cross','signed'):
            x=F(*t[k])*scale;out[k]=[x.numerator//x.denominator,-((-x.numerator)//x.denominator)]
        out['stages_hash']=sha(t['stages']);return out
    b={k:full[k] for k in ('schema','status','parent','scope','counts','mu_hash','buchstab','prime_only')}
    b.update({'interval_scale':scale,'ensembles_hash':sha(panels),'dyadic_hash':sha(large),
              'combinatorial_hash':sha(comb),'combinatorial_cases':len(comb),
              'samples':[summary(panels[i]) for i in (0,9,17,29)],'dyadic_samples':[summary(t) for t in large],'full_hash':sha(full)})
    return {'body':b,'sha256':sha(b)}

def strict(text):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'duplicate key');d[k]=v
        return d
    def bad(x):raise ValueError('noninteger numeric syntax')
    return json.loads(text,object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)

def accept(got,expected):
    require(type(got) is dict and set(got)=={'body','sha256'},'schema')
    require(got['sha256']==sha(got['body']),'digest')
    require(serial(got)==serial(expected),'primitive reconstruction or typed scope mismatch')

def selftest(expected):
    paths=[('status',),('parent',),('counts','complete_ensembles'),('counts','enumerated_signatures'),
      ('counts','signing_stages'),('buchstab','cases'),('prime_only','hash'),('ensembles_hash',),
      ('dyadic_hash',),('combinatorial_cases',),('full_hash',),('interval_scale',)]
    for j,path in enumerate(paths):
        x=copy.deepcopy(expected);d=x['body']
        for k in path[:-1]:d=d[k]
        old=d[path[-1]]
        d[path[-1]]=True if j==2 else (float(old) if j==3 else (old+1 if type(old) is int else 'altered'))
        x['sha256']=sha(x['body'])
        try:accept(x,expected)
        except ValueError:pass
        else:raise ValueError('mutation accepted')
    try:strict('{"x":1,"x":2}')
    except ValueError:pass
    else:raise ValueError('duplicate accepted')
    print('RESEALED MUTATIONS REJECTED 12; DUPLICATE REJECTED 1')

def authenticate():
    names={'PROOF.md','README.md','SOURCE_LOCK.json','VALIDATION.md','produce.py','verify.py','result.json','validation.json'}
    require({p.name for p in ROOT.iterdir()}==names|{'MANIFEST.json'},'packet inventory')
    require(all(not p.is_symlink() and p.is_file() for p in ROOT.iterdir()),'regular files only')
    m=strict((ROOT/'MANIFEST.json').read_text())
    require(type(m) is dict and set(m)==names,'manifest entries')
    for name in names:
        require(type(m[name]) is str and hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==m[name],'file hash '+name)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('report');ap.add_argument('--self-test',action='store_true');ap.add_argument('--output');args=ap.parse_args()
    authenticate();report=Path(args.report);require(report.is_file() and not report.is_symlink(),'regular report');got=strict(report.read_text());expected=reconstruct();accept(got,expected)
    if args.output:Path(args.output).write_text(serial(expected)+'\n')
    if args.self_test:selftest(expected)
    print('SEPARATE EXACT RECONSTRUCTION PASS',expected['sha256'])
if __name__=='__main__':main()
