#!/usr/bin/env python3
"""Exact finite controls for HSC26; not an infinite theorem prover.

The full theta moment certificate is the pinned ICR26 dependency. This program
independently checks finite-star probabilities/moments, the rational seed
Jacobian, and arithmetic in the harmonic-tail construction. No floating point,
zeta value, zero oracle, or unchecked numerical retuning enters acceptance.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SEED_BLOB='e338c68ec803acd7991d52a83f7d5b5b97896ee3'


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def strict_load(path: Path):
    def pairs(items):
        result={}
        for k,v in items:
            require(k not in result,'duplicate JSON key')
            result[k]=v
        return result
    def bad(value):
        raise ValueError('float or nonfinite JSON token: '+value)
    return json.loads(path.read_text(),object_pairs_hook=pairs,
                      parse_float=bad,parse_constant=bad)


def git_blob(data: bytes)->str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def encoded(x: F):
    return [x.numerator,x.denominator]


def cumulants(m):
    k=[F(0)]*len(m)
    for n in range(1,len(m)):
        k[n]=m[n]-sum(F(math.comb(n-1,j-1))*k[j]*m[n-j]
                         for j in range(1,n))
    return k


def inverse(a):
    n=len(a); b=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next((i for i in range(j,n) if b[i][j]),None)
        require(p is not None,'singular exact matrix')
        b[j],b[p]=b[p],b[j]
        q=b[j][j];b[j]=[v/q for v in b[j]]
        for i in range(n):
            if i!=j:
                q=b[i][j];b[i]=[v-q*w for v,w in zip(b[i],b[j])]
    return [row[n:] for row in b]


def star_moments(a0,leaves,degree=16):
    """Conditional independent-edge convolution, then root symmetrization."""
    require(a0>=0,'negative root weight')
    out=[a0**k for k in range(degree+1)]
    for a,r in leaves:
        require(a>0 and 0<=r<1,'invalid ferromagnetic leaf')
        moments=[a**k*(1 if k%2==0 else r) for k in range(degree+1)]
        out=[sum(F(math.comb(k,j))*out[j]*moments[k-j] for j in range(k+1))
             for k in range(degree+1)]
    return [v if k%2==0 else F(0) for k,v in enumerate(out)]


def direct_gibbs(a0,leaves,degree=16):
    """Separate enumeration of all physical spin configurations."""
    numer=[F(0)]*(degree+1);norm=F(0)
    for sig in itertools.product((-1,1),repeat=len(leaves)+1):
        weight=F(1)
        for j,(_,r) in enumerate(leaves,1):
            weight*=1+r*sig[0]*sig[j]
        x=a0*sig[0]+sum(a*sig[j] for j,(a,_) in enumerate(leaves,1))
        norm+=weight
        for k in range(degree+1):numer[k]+=weight*x**k
    require(norm==2**(len(leaves)+1),'complete star normalization')
    return [v/norm for v in numer]


def linear_add(*vectors):
    keys=set().union(*(v.keys() for v in vectors))
    return {k:sum((v.get(k,F(0)) for v in vectors),F(0)) for k in sorted(keys)
            if sum((v.get(k,F(0)) for v in vectors),F(0))}


def scaled(a,vec):return {k:a*v for k,v in vec.items()}


def reconstruct():
    params=ROOT/'seed_parameters.json'
    require(git_blob(params.read_bytes())==SEED_BLOB,'exact parent seed parameters')
    p=strict_load(params)
    # The copied file's numerical strings are literal exact rationals.
    centers=[F(t) for t in p['centers']]
    nu=p['multiplicities']
    require(nu==[256,10,1,1,1,1] and len(centers)==7,'seed structure')
    sign=[F(1) if j%2==0 else F(0) for j in range(17)]
    dim=[F(3,5) if j%2==0 else F(0) for j in range(17)];dim[0]=F(1)
    cs,ds=cumulants(sign),cumulants(dim)
    ratios=[ds[2*j]/cs[2*j] for j in range(1,9)]
    jac=[[F(r)*nu[i]*centers[i]**(r-1) for i in range(6)]+
         [F(r)*ratios[r-1]*centers[6]**(r-1)] for r in range(1,8)]
    inv=inverse(jac)
    for i in range(7):
        for j in range(7):
            require(sum(inv[i][k]*jac[k][j] for k in range(7))==F(i==j),'inverse identity')
    rnorm=max(sum(abs(x) for x in row) for row in inv)
    require(rnorm<75000000,'inherited Jacobian norm independently reconstructed')
    panels=[];configs=0
    for n in range(1,9):
        a0=F(1,n+2)
        leaves=[(F(j+1,3*n+1),F((j%4)+1,6)) for j in range(n)]
        m=star_moments(a0,leaves)
        require(m==direct_gibbs(a0,leaves),'conditional/Gibbs moment mismatch')
        mean=a0+sum(a*r for a,r in leaves)
        variance=mean**2+sum(a*a*(1-r*r) for a,r in leaves)
        require(m[2]==variance,'variance includes shared root cross terms')
        require(m[4]<=3*m[2]**2,'finite fourth moment control')
        configs+=2**(n+1)
        panels.append({'leaves':n,'moments':[encoded(x) for x in m[::2]]})
    # Dimer specialization, not three free mixture probabilities.
    require(star_moments(F(1,2),[(F(1,2),F(1,5))])==dim,'actual dimer law')
    rejected=0
    for invalid in ((F(1),[(F(1),F(-1,4))]),(F(1),[(F(1),F(1))]),
                    (F(1),[(F(-1),F(1,4))])):
        try:star_moments(*invalid)
        except ValueError:rejected+=1
    require(rejected==3,'invalid model accepted')
    tail_checks=0
    for n in range(3,67):
        require(F(1,n*n)<=F(1,n*(n-1)),'upper telescoping tail')
        require(F(1,n*n)>=F(1,n*(n+1)),'lower telescoping tail')
        a=F(1,2*n);r=F(7,4*n)
        require(a*r==F(7,8*n*n) and a*a==F(1,4*n*n),'harmonic parameters')
        tail_checks+=3
    ballast=[]
    for n in (3,4,8,16,32):
        M=n*n;b=F(n,7);r=F(1,M*M)
        # Moment formula for M identical conditional leaves, no enumeration.
        mean=b*r;noise=b*b/F(M)*(1-r*r)
        finite=star_moments(F(0),[(b/M,r)]*M,degree=2)[2]
        require(finite==mean*mean+noise,'complete ballast variance')
        ballast.append([n,encoded(mean),encoded(noise)])
    # Exact symbolic growing coefficient, basis {gamma,1,log2,logpi,H,Acore}.
    A={'gamma':F(2),'1':F(-1),'log2':F(2),'logpi':F(-1)}
    harmonic=scaled(F(1,2),linear_add(A,{'log2':F(-1),'H':F(-1)}))
    b={'H':F(1,2),'gamma':F(-1),'log2':F(-1),'Acore':F(-1)}
    coefficient=linear_add(harmonic,b,{'Acore':F(1)})
    desired={'1':F(-1,2),'log2':F(-1,2),'logpi':F(-1,2)}
    require(coefficient==desired,'theta large-field linear coefficient')
    # Stirling: 2 log h from s(s-1), -1/4 log h from Gamma(h/2+1/4).
    require(F(2)-F(1,4)==F(7,4),'theta logarithmic coefficient')
    # exp[-(c+ell)/c]=exp(log2+logpi)=2*pi, times c is pi.
    exponent=scaled(F(-2),linear_add({'1':F(1,2)},coefficient))
    require(exponent=={'log2':F(1),'logpi':F(1)},'probability tail coefficient')
    require(F(1)-F(1,2)**2/F(6)>F(1,2),'sine lower bound constant')
    return {'schema':'HSC26.finite-controls.v1','status':'proposed-components-not-RH',
      'rh_proved':False,'all_order_realization_proved':False,
      'new_theta_moment_order':14,'new_retuned_N_certified':False,
      'finite_star_panels':panels,'physical_configurations_enumerated':configs,
      'rational_seed_inverse_identities':49,'seed_inverse_row_norm':encoded(rnorm),
      'harmonic_arithmetic_checks':tail_checks,'ballast_variance_panels':ballast,
      'invalid_ferromagnetic_inputs_rejected':rejected,
      'large_field_h_log_h':encoded(F(1,2)),
      'large_field_h_coefficient':{k:encoded(v) for k,v in coefficient.items()},
      'large_field_log_h':encoded(F(7,4)),
      'scope':'finite algebra only; analytic global proofs and parent theta integration are separate'}


def authenticate():
    require(not (ROOT/'SHA256SUMS').is_symlink(),'symlink manifest')
    listed={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        require(name not in listed and '/' not in name,'manifest entry')
        file=ROOT/name
        require(file.is_file() and not file.is_symlink(),'regular payload')
        require(hashlib.sha256(file.read_bytes()).hexdigest()==digest,'payload hash '+name)
        listed[name]=digest
    require({p.name for p in ROOT.iterdir()}==set(listed)|{'SHA256SUMS'},'exact inventory')


def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',action='store_true');g.add_argument('--check',type=Path)
    opt=ap.parse_args()
    if opt.check:authenticate()
    expected=reconstruct()
    if opt.check:
        received=strict_load(opt.check)
        require(json.dumps(received,sort_keys=True,separators=(',',':'))==
                json.dumps(expected,sort_keys=True,separators=(',',':')),'reconstructed result differs')
    print(json.dumps(expected,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
