#!/usr/bin/env python3
"""Bounded exact checks, not a verification of OPEN or the analytic contour proof."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
PARENT = 'ed074bcabfd2c1ca3336e457b8fdd09a25bcd2a7'
PARENT_FILES = {
    '../balanced-mobius-contour/PROOF.md': (
        'e493ba173d6736fca88a84fc7821fc72d73cad89f7a689d7e219c394c245557e',
        '8ebf299f6985600f56af0e340bf2ee57c090a65f'),
    '../sparse-sign-bootstrap/PROOF.md': (
        '036e9d3d7b429e9ac8d850e81910c53addfa1d9654050732cfc3dc8bcc4e47c7',
        '046a12cd9233aa7d8a9a3a5d4d4c64a67d4207be'),
}
FILES = {'README.md','PROOF.md','REVIEW.md','SOURCES.json','VALIDATION.md',
         'verify.py','result.json','SHA256SUMS'}

class Refusal(Exception):
    pass

def need(condition: bool, message: str) -> None:
    if not condition:
        raise Refusal(message)

def unique(pairs):
    d = {}
    for k, v in pairs:
        need(k not in d, 'duplicate JSON key')
        d[k] = v
    return d

def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda _: (_ for _ in ()).throw(Refusal('nonfinite JSON')))

def canonical(x) -> str:
    return json.dumps(x, sort_keys=True, separators=(',',':'), allow_nan=False)

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def authenticate() -> None:
    found = set()
    for p in ROOT.rglob('*'):
        need(not p.is_symlink(), 'symlink in packet')
        if p.is_file(): found.add(p.relative_to(ROOT).as_posix())
    need(found == FILES, 'packet inventory mismatch')
    entries = {}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ',1)
        need(name not in entries, 'duplicate manifest path')
        entries[name] = digest
    need(set(entries) == FILES-{'SHA256SUMS'}, 'manifest coverage mismatch')
    for name, digest in entries.items():
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,
             'packet hash mismatch: '+name)
    source = load(ROOT/'SOURCES.json')
    need(source['parent_head'] == PARENT, 'wrong parent head')
    for name,(sha,git) in PARENT_FILES.items():
        p=ROOT/name
        need(p.is_file() and not p.is_symlink(), 'missing parent')
        data=p.read_bytes()
        need(hashlib.sha256(data).hexdigest()==sha and blob(data)==git,
             'parent source mismatch')

def mu_trial(n: int) -> int:
    sign=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; sign=-sign
            if n%p==0: return 0
            while n%p==0: n//=p
        p+=1
    return -sign if n>1 else sign

def mu_sieve(N: int):
    a=[1]*(N+1); a[0]=0
    prime=[True]*(N+1)
    for p in range(2,N+1):
        if prime[p]:
            for n in range(p,N+1,p): a[n]=-a[n]; prime[n]=False
            for n in range(p*p,N+1,p*p): a[n]=0
    return a

def logarithm(n: int):
    out={}; p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,Q(0))+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,Q(0))+1
    return out

def add(a,b,scale=Q(1)):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,Q(0))+scale*v
        if not c[k]: del c[k]
    return c

def multiply(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items(): c[i+j]=c.get(i+j,Q(0))+x*y
    return {i:x for i,x in c.items() if x}

def derivative(a):
    return {i-1:i*x for i,x in a.items() if i}

def convolution(a,b,N):
    out=[Q(0)]*(N+1)
    for i in range(1,min(N,len(a)-1)+1):
        if not a[i]: continue
        for j in range(1,min(N//i,len(b)-1)+1):
            if b[j]: out[i*j]+=a[i]*b[j]
    return out

def convolution_log(a,b,N):
    out=[{} for _ in range(N+1)]
    for i in range(1,min(N,len(a)-1)+1):
        if not a[i]: continue
        for j in range(1,min(N//i,len(b)-1)+1):
            if b[j]: out[i*j]=add(out[i*j],b[j],a[i])
    return out

def w(u):
    if Q(1,4)<u<=1: return u/3-Q(1,192)/u**2
    if 1<u<4: return Q(1,3)/u**2-u/192
    return Q(0)

@lru_cache(None)
def ln_interval(n: int):
    need(type(n) is int and n>=1,'log domain')
    k=n.bit_length()-1; x=Q(n,2**k); t=(x-1)/(x+1)
    def series(t):
        v=t; total=Q(0)
        for j in range(80):
            total+=2*v/(2*j+1); v*=t*t
        return total,total+2*v/(161*(1-t*t))
    lo,hi=series(t); a,b=series(Q(1,3))
    return lo+k*a,hi+k*b

def outward_dyadic(lo,hi,bits=112):
    S=2**bits
    return [str((lo*S).__floor__()),str((hi*S).__ceil__()),str(S)]

def reconstruct():
    groups={}
    def check(g,cond):
        need(cond,'mathematical fixture: '+g)
        groups[g]=groups.get(g,0)+1
    mu=mu_sieve(256)
    for n in range(1,257): check('mobius_sieve_vs_trial',mu[n]==mu_trial(n))
    for Y in range(2,11):
        N=2*Y*Y
        u=[Q(0)]+[Q(1)]*N; e=[Q(0)]*(N+1); e[1]=1
        l=[{}]+[logarithm(n) for n in range(1,N+1)]
        muv=[Q(0)]+[Q(mu_trial(n)) for n in range(1,N+1)]
        lam=convolution_log(muv,l,N)
        M=sum((Q(mu_trial(n),n) for n in range(1,Y)),Q(0))
        native=None
        for c in [Q(-1),Q(0),Q(1,3)]:
            p=[Q(0)]*(4*Y+1)
            for n in range(1,Y): p[n]=Q(mu_trial(n))
            p[Y]=-Y*M+c*Y; p[2*Y]=-2*c*Y
            check('value_normalization',sum(p[n]/n for n in range(1,len(p)))==0)
            r=[x-y for x,y in zip(e,convolution(u,p,N))]
            pl=convolution_log(p,l,N)
            pp=convolution(p,p,N)
            ppu=convolution(pp,u,N)
            last=convolution_log(ppu,l,N)
            proxy=[add({},add(pl[n],last[n],Q(-1)),Q(1)) for n in range(N+1)]
            proxy=[add(proxy[n],pl[n]) for n in range(N+1)]
            rr=convolution(r,r,N); rem=convolution_log(rr,lam,N)
            check('complete_convolution_identity',
                  all(add(lam[n],proxy[n],Q(-1))==rem[n] for n in range(1,N+1)))
            check('exact_prefix_range',all(proxy[n]==lam[n] for n in range(1,N)))
            check('first_omitted_coefficient',rem[N]==({2:r[Y]**2} if r[Y] else {}))
            if Y>=4:
                m=Q(Y,2); sums=[]
                for src in [lam,proxy]:
                    ans={}
                    for n in range(1,Y*Y+1): ans=add(ans,src[n],w(Q(n)/m**2)/m)
                    sums.append(ans)
                check('full_native_annular_identity',sums[0]==sums[1])
                if native is not None: check('tail_variation_native_invariance',sums[1]==native)
                native=sums[1]
    # Laurent coefficients are reconstructed, rather than inserting the residue formula.
    for a in [Q(-2),Q(0),Q(1,3)]:
      for b in [Q(-1),Q(1),Q(3,2)]:
       for c in [Q(-2,3),Q(0),Q(5)]:
        for gamma in [Q(0),Q(3,5)]:
            zeta={-1:Q(1),0:gamma,1:Q(2,7),2:Q(-4,9),3:Q(1,11)}
            dz=derivative(zeta); p={0:a,1:b,2:c/2,3:Q(2,13)}
            lp=add(multiply(dz,p),{},Q(1))
            lp={i:-2*x for i,x in lp.items()}
            lp=add(lp,multiply(multiply(zeta,dz),multiply(p,p)))
            H={0:Q(5,7),1:Q(-3,4),2:Q(11,18)}
            got=multiply(H,lp).get(-1,Q(0))
            want=-a*a*Q(11,9)/2+(2*a-2*a*b-gamma*a*a)*H[1]
            want+=(2*b-b*b-a*c-2*gamma*a*b)*H[0]
            check('general_three_jet_residue',got==want)
            if a==0: check('normalized_rank_one_residue',got==H[0]*(2*b-b*b))
    for x in [Q(-2),Q(0),Q(1,3),Q(2)]:
      for y in [Q(-1),Q(0),Q(5,4)]:
        zeta={-1:Q(1),0:Q(3,5),1:Q(2,7)}
        v={1:x,2:Q(2,3)}; q={1:y,2:Q(-7,3)}
        coeff=multiply(multiply(zeta,derivative(zeta)),multiply(v,q)).get(-1,Q(0))
        check('polarized_tail_residue',coeff==-x*y)
        f0=Q(45,64); D=Q(-3,7)
        check('homogeneous_determinant', (D+f0)*f0-f0*f0==f0*D)
    # Formal jets of a null tail use factorization, not floating logarithms.
    for Y in range(2,17):
        v={Y:Q(Y),2*Y:Q(-4*Y),4*Y:Q(4*Y)}
        j0=sum(v[n]/n for n in v); j1={}
        for n,a in v.items(): j1=add(j1,logarithm(n),-a/n)
        check('two_jet_null_tail',j0==0 and j1=={})
    for n in range(4,25):
        nu=Q(2,3)+Q(1,n)
        margin=3*nu/2-1; eps=margin/2; eta=eps/(2*nu)
        exponents=[-3*nu/4+nu*eta,Q(1,2)-5*nu/4+nu*eta,
                   -nu/2+2*nu*eta,1-3*nu/2+2*nu*eta]
        check('uniform_tail_exponents',all(e<=-margin+eps<0 for e in exponents))
    check('three_quarter_cutoff',1-Q(3,2)*Q(3,4)==-Q(1,8))
    coeff={}
    for n in range(2,17):
        fac=logarithm(n)
        if len(fac)==1:
            prime=next(iter(fac)); coeff[prime]=coeff.get(prime,Q(0))+w(Q(n,4))/2
    expected={2:Q(35,128),3:Q(18343,124416),5:Q(3971,38400),7:Q(1251,25088),
              11:Q(2765,185856),13:Q(633,86528)}
    check('native_m2_log_coefficients',coeff==expected)
    lo=hi=-Q(45,64)
    for p,c in coeff.items():
        l,h=ln_interval(p); lo+=c*l; hi+=c*h
    check('native_negative_integral',-Q(17,500)<lo<=hi<-Q(33,1000))
    return {'schema':'completion-rigidity-v1','parent_head':PARENT,
            'rh_proved':False,'native_sign_estimate_proved':False,
            'scope':'bounded exact algebra; no contour quadrature or independent analytic acceptance',
            'groups':groups,'fixture_count':sum(groups.values()),
            'native_I2_enclosure':outward_dyadic(lo,hi),
            'cutoff_exponent':'3/4','tail_power_before_epsilon':'-1/8',
            'rank_one_fixture_contract':'real tail variations with zero value at one'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--emit',action='store_true')
    ap.add_argument('--check',type=Path); args=ap.parse_args()
    if args.check:
        authenticate(); data=reconstruct(); saved=load(args.check)
        need(canonical(data)==canonical(saved),'reconstructed result mismatch')
    else:
        need(args.emit,'use --emit or --check result.json'); data=reconstruct()
    print(json.dumps(data,sort_keys=True,indent=2))

if __name__=='__main__':
    try: main()
    except (Refusal,ValueError,KeyError,OSError,TypeError) as exc:
        print('REFUSE: '+str(exc),file=sys.stderr); sys.exit(2)
