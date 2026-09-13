#!/usr/bin/env python3
"""PPD26 producer: exact finite prime-sign ensembles, not an RH proof."""
import argparse, hashlib, itertools, json, math
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def pack(x):
    return [x.numerator, x.denominator]

def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def primitive(n):
    mu = [1] * (n + 1); mu[0] = 0; primes = []
    for p in range(2, n + 1):
        if all(p % q for q in primes if q*q <= p):
            primes.append(p)
            for k in range(p, n + 1, p): mu[k] *= -1
            for k in range(p*p, n + 1, p*p): mu[k] = 0
    return primes, mu

def energy(a):
    s = 0; ans = Q(0)
    for k in range(1, len(a)):
        s += a[k]; ans += Q(s*s, k*(k+1))
    return ans

def flags(n, ps):
    return sum(1 << j for j,p in enumerate(ps) if n % p == 0)

def grouped_energy(a, masks, remaining):
    sums = {}; square = 0; ans = Q(0)
    for n in range(1, len(a)):
        g = masks[n] & remaining; old = sums.get(g, 0)
        sums[g] = old + a[n]; square += 2*old*a[n] + a[n]*a[n]
        ans += Q(square, n*(n+1))
    return ans

def pairing(a, masks, remaining, bit):
    sums = {}; paired = 0; ans = Q(0)
    for n in range(1, len(a)):
        g = masks[n] & remaining
        paired += a[n] * sums.get(g ^ bit, 0)
        sums[g] = sums.get(g, 0) + a[n]
        ans += Q(paired, n*(n+1))
    return ans

def smooth_data(n, ps):
    mass = Q(0); records = []
    scale = 1 << 96
    for d in range(1,n+1):
        t=d; omega=0; total=0; squarefree=True
        for p in ps:
            e=0
            while t%p==0: t//=p; e+=1
            omega += bool(e); total += e; squarefree &= e<=1
        if t==1:
            coeff=2**omega
            mass += Q(coeff*(math.isqrt(scale*scale//d)+1),scale)
            records.append([d,coeff,coeff*(-1)**total,int(squarefree)])
    return mass, records

def finite_panel(X, ps, mu, enumerate_family):
    a=mu[:X]; masks=[0]+[flags(n,ps) for n in range(1,X)]
    remaining=(1<<len(ps))-1
    initial=grouped_energy(a,masks,remaining)
    native=energy(a)
    diagonal=sum((Q(mu[n]*mu[n])*(Q(1,n)-Q(1,X)) for n in range(1,X)),Q(0))
    rough=energy([a[n] if masks[n]==0 else 0 for n in range(X)])
    states=[]; current=initial; signs=[]
    for j,p in enumerate(ps):
        b=pairing(a,masks,remaining,1<<j)
        sign=-1 if b>0 else 1
        signs.append(sign)
        a=[a[n]*(sign if masks[n]&(1<<j) else 1) for n in range(X)]
        remaining ^= 1<<j
        after=grouped_energy(a,masks,remaining)
        if after != current-2*abs(b): raise ValueError('conditional energy identity')
        states.append([p,sign,pack(b),pack(after)])
        current=after
    if energy(a)!=current: raise ValueError('terminal energy')
    mass, factors=smooth_data(X-1,ps)
    if not native/mass**2 <= current <= native*mass**2: raise ValueError('uniform member bound')
    row={'X':X,'primes':ps,'native':pack(native),'rough':pack(rough),'mean':pack(initial),
         'diagonal':pack(diagonal),'cross':pack(initial-diagonal),'signed':pack(current),
         'signs':signs,'stages':states,'mass_upper':pack(mass),'local_factors_hash':digest(factors)}
    if enumerate_family:
        vals=[]
        for sig in itertools.product([1,-1],repeat=len(ps)):
            v=[0]+[mu[n]*math.prod(sig[j] for j in range(len(ps)) if masks[n]&(1<<j)) for n in range(1,X)]
            vals.append(energy(v))
        if sum(vals,Q(0))/len(vals)!=initial: raise ValueError('Walsh mean')
        if not all(native/mass**2<=v<=native*mass**2 for v in vals): raise ValueError('all member bound')
        row.update({'family_size':len(vals),'minimum':pack(min(vals)),'maximum':pack(max(vals)),
                    'family_hash':digest([pack(v) for v in vals])})
    else:
        row['family_size']=2**len(ps); row['family_enumerated']=False
    return row

def buchstab(primes,mu,N):
    out=[]
    def R(y,x): return sum(mu[n] for n in range(1,x+1) if all(n%p for p in primes if p<=y))
    for y in [2,3,5,7,11]:
        for x in range(1,N+1):
            lhs=R(y,x); rhs=1-sum(R(p,x//p) for p in primes if y<p<=x)
            if lhs!=rhs: raise ValueError('strict least-prime recursion')
            out.append([y,x,lhs])
    return out

def build_full():
    primes,mu=primitive(1024)
    panels=[]
    for X in [8,16,32,64,128,256]:
        for y in [2,3,5,7,11]:
            panels.append(finite_panel(X,[p for p in primes if p<=y],mu,True))
    large=[]
    for X in [16,32,64,128,256,512,1024]:
        y=(X.bit_length()-1)**2
        large.append(finite_panel(X,[p for p in primes if p<=y],mu,False))
    rec=buchstab(primes,mu,128)
    blocks=[]
    for y in [2,3,5,7,11,17]:
        for x in range(1,y*y+1):
            got=sum(mu[n] for n in range(1,x+1) if all(n%p for p in primes if p<=y))
            want=1-sum(1 for p in primes if y<p<=x)
            if got!=want: raise ValueError('prime-only range')
            blocks.append([y,x,got])
    combinatorial=[]
    for y in [5,7,11,13,17,19]:
        ps=[p for p in primes if p<=y]
        for r in range(1,min(3,len(ps))+1):
            ds=sorted(math.prod(c) for c in itertools.combinations(ps,r))
            if len(set(ds))!=math.comb(len(ps),r) or max(ds)>y**r: raise ValueError('prime-product injection')
            combinatorial.append([y,r,len(ds),y**(2*r),pack(Q(len(ds)**2,4*y**r)),digest(ds)])
    body={'schema':'PPD26-1','status':'PROPOSED; RH estimate OPEN','parent':'99101457b32b6f10f4eda88ca998048404b860ea',
          'scope':'finite exact arithmetic; no asymptotic norm or RH inference',
          'panels':panels,'dyadic_bank_panels':large,
          'buchstab':{'cases':len(rec),'hash':digest(rec)},
          'prime_only':{'cases':len(blocks),'hash':digest(blocks)},
          'combinatorial':combinatorial,'mu_hash':digest(mu),
          'counts':{'complete_ensembles':30,'enumerated_signatures':sum(p['family_size'] for p in panels),
                    'dyadic_ensembles':7,'dyadic_signatures_not_enumerated':sum(p['family_size'] for p in large),
                    'signing_stages':sum(len(p['stages']) for p in panels+large)}}
    return body

def compact(full):
    scale=1<<32
    def sample(t):
        o={k:t[k] for k in ('X','primes','family_size','signs')}
        for k in ('native','rough','mean','diagonal','cross','signed'):
            v=Q(*t[k])*scale; o[k]=[v.numerator//v.denominator,-((-v.numerator)//v.denominator)]
        o['stages_hash']=digest(t['stages'])
        return o
    body={'schema':full['schema'],'status':full['status'],'parent':full['parent'],'scope':full['scope'],
      'interval_scale':scale,'counts':full['counts'],'mu_hash':full['mu_hash'],
      'ensembles_hash':digest(full['panels']),'dyadic_hash':digest(full['dyadic_bank_panels']),
      'buchstab':full['buchstab'],'prime_only':full['prime_only'],
      'combinatorial_hash':digest(full['combinatorial']), 'combinatorial_cases':len(full['combinatorial']),
      'samples':[sample(full['panels'][i]) for i in (0,9,17,29)],
      'dyadic_samples':[sample(t) for t in full['dyadic_bank_panels']],
      'full_hash':digest(full)}
    return {'body':body,'sha256':digest(body)}

def build():
    return compact(build_full())

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--check');args=ap.parse_args()
    r=build(); text=json.dumps(r,sort_keys=True,separators=(',',':'))+'\n'
    if args.check:
        got=json.loads(Path(args.check).read_text())
        if json.dumps(got,sort_keys=True,separators=(',',':'))!=text.strip(): raise ValueError('mismatch')
    if args.output: Path(args.output).write_text(text)
    print('PRODUCER PASS',r['sha256']);print(json.dumps(r['body']['counts'],sort_keys=True))
if __name__=='__main__': main()
