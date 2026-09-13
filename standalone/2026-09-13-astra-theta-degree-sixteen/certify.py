#!/usr/bin/env python3
"""Reconstruct the native theta moments and the complete degree-16 root box.
Standard-library integer/Fraction arithmetic only. --emit is producer-only;
--check authenticates and reconstructs. The analytic proof is PROOF.md.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import primitive as b
I=b.I; SCALE=b.SCALE
require=b.require


def load_json(path):
    def obj(pairs):
        d={}
        for k,v in pairs:
            require(k not in d, 'duplicate JSON key')
            d[k]=v
        return d
    def forbidden(s): raise ValueError('noninteger JSON number forbidden')
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=obj,
                      parse_float=forbidden,parse_constant=forbidden)


def raw_pair_and_sign(R):
    cs=b.cumulants([F(int(n%2==0)) for n in range(2*R+1)])
    mo=[F(0) if n%2 else F(3,5) for n in range(2*R+1)];mo[0]=F(1)
    dc=b.cumulants(mo)
    return cs,[dc[2*r]/cs[2*r] for r in range(1,R+1)]


def reconstruct():
    p=load_json(ROOT/'parameters.json')
    require(p['schema']=='D16.parameters.v1','schema')
    require(p['r']==8 and type(p['r']) is int,'moment scope')
    nu=p['nu'];active=p['free'];fixed=p['fixed']
    require(nu==[256,10,1,1,1,1] and all(type(x)is int for x in nu),'multiplicity')
    require(active==[0,1,2,3,4,5,7,9] and fixed==[6,8,10]
       and all(type(x)is int for x in active+fixed),'active coordinates')
    require(p['pair_probability']==[3,5],'coupling/probability')
    require(all(type(s)is str for s in p['centers']) and len(p['centers'])==11,'centers')
    c=[F(s) for s in p['centers']];rad=F(p['radius'])
    require(rad==F(1,10**14),'fixed box radius')
    box=[I(I.coerce(x-(rad if i in active else 0)).lo,
           I.coerce(x+(rad if i in active else 0)).hi) for i,x in enumerate(c)]
    require(all(v.lo>I.rat(1,2000).hi and v.hi<SCALE for v in box),'positive box')
    require(b.BITS==320 and b.DEGREE==120,'source precision/degree')
    raw,mu,tails=b.theta_moments();v=mu[2]
    require(v.lo>I.rat(1,25).hi and v.hi<I.rat(1,20).lo,'theta variance range')
    require(set(raw)==set(range(0,19,2)),'complete moments through eighteen')
    mom=[I.coerce(0) for _ in range(19)];mom[0]=I.coerce(1)
    for r in range(1,10):mom[2*r]=mu[2*r]/v**r
    kap=b.cumulants(mom);cs,ar=raw_pair_and_sign(9)
    s=[kap[2*r]/cs[2*r] for r in range(1,10)]
    def val(r,vec):
        return sum((nu[i]*vec[i]**r for i in range(6)),I.coerce(0)) \
           +ar[r-1]*sum((vec[i]**r for i in range(6,11)),I.coerce(0))
    J0=[[r*(nu[i] if i<6 else ar[r-1])*c[i]**(r-1) for i in active]
           for r in range(1,9)]
    R=b.inverse(J0)
    for i in range(8):
        for j in range(8):
            require(sum(R[i][k]*J0[k][j] for k in range(8))==F(i==j),'left inverse')
            require(sum(J0[i][k]*R[k][j] for k in range(8))==F(i==j),'right inverse')
    norm=max(sum(abs(x) for x in row) for row in R)
    require(norm<3200000000,'inverse row norm')
    residual=[val(r,c)-s[r-1] for r in range(1,9)]
    beta=max(b.absup(sum((R[i][r]*residual[r] for r in range(8)),I.coerce(0))) for i in range(8))
    J=[[r*(nu[i] if i<6 else ar[r-1])*box[i]**(r-1) for i in active]for r in range(1,9)]
    L=max(sum(b.absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j] for k in range(8)),I.coerce(0)))
              for j in range(8)) for i in range(8))
    require(L<I.rat(1,500000).lo,'contraction row sum below 2e-6')
    require(beta<I.rat(1,10**19).lo,'displacement below 1e-19')
    require(F(beta,SCALE)+F(L,SCALE)*rad<rad,'whole-box invariance')
    delta=F(p['target_kappa16_half_width']);jj=F(p['connected_coupling_max'])
    require(delta==F(1,10**15) and jj==F(1,10**150),'robust schedule')
    target_cost=max(abs(row[7]) for row in R)*delta/abs(cs[16])
    require(target_cost<F(1,10**15),'target perturbation cost')
    # Complete finite Gibbs bounds on all 280 spins and every pair.
    gibbs=10**80
    for n in range(2,19,2):
        cn=factorial(n)*2**(n-1)
        require(cn*80000*n*280**n<gibbs,'Gibbs moment bound')
        require(cn*80000*n*n*10000*280**(n-1)<gibbs,'Gibbs derivative bound')
    beta_all=F(beta,SCALE)+target_cost+norm*gibbs*jj
    L_all=F(L,SCALE)+8*norm*gibbs*jj
    require(beta_all+rad*L_all<rad and L_all<F(1,100),'uniform target/positive coupling box')
    require(rad-beta_all-rad*L_all>F(9,10**15),'uniform strict margin')
    err18=cs[18]*(val(9,box)-s[8])
    require(err18.lo>I.rat(169,1000).hi and err18.hi<I.rat(170,1000).lo,'eighteenth moment differs')
    # Raw moment transfer under delta at cumulant16: +binom(18,16)*delta,
    # since kappa2=1 and all lower even cumulants agree. j effect paid separately.
    err_extra=153*delta+jj*gibbs
    require(F(err18.lo,SCALE)-err_extra>F(169,1000)
        and F(err18.hi,SCALE)+err_extra<F(170,1000),'robust next moment separation')
    share=F(3,5)*sum(box[6:],I.coerce(0))
    require(share.lo>I.rat(191,1000).hi and share.hi<I.rat(192,1000).lo,'pair variance share')
    weights=[(v*box[i]).sqrt() for i in range(6)]+[(v*x).sqrt()/2 for x in box[6:]]
    from checks import controls
    evidence=controls()
    return {'schema':'D16.result.v1','status':'proposed-computer-assisted-component','rh_proved':False,
       'matched_even_orders':list(range(2,17,2)),'spins':280,'fixed_positive_edges':5,
       'connected_positive_edges':39060,'connected_coupling_max':str(jj),
       'theta_bits':b.BITS,'theta_degree':b.DEGREE,'theta_cells':84,
       'normalization':raw[0].record(),'variance':v.record(),
       'theta_raw_integrals':{str(k):x.record() for k,x in raw.items()},
       'complete_source_remainders':tails,'standardized_cumulant_ratios':[x.record() for x in s],
       'active_parameters':active,'fixed_parameters':fixed,
       'beta_dyadic_upper':beta,'row_sum_L_dyadic_upper':L,
       'inverse_row_norm':str(norm),'target_only_parameter_cost':str(target_cost),
       'robust_invariance_margin':str(rad-beta_all-rad*L_all),
       'physical_weight_intervals':[x.record() for x in weights],
       'variance_share_of_five_pairs':share.record(),
       'standardized_unmatched18':err18.record(),
       'two_sided_inverse_entries':128,'bounded_controls':evidence}


def authenticate():
    require(not ROOT.is_symlink(),'symlink root')
    lines=(ROOT/'SHA256SUMS').read_text(encoding='utf-8').splitlines();names=set()
    for line in lines:
        digest,name=line.split('  ',1)
        require(name not in names and Path(name).name==name,'manifest name')
        path=ROOT/name
        require(path.is_file() and not path.is_symlink(),'regular file '+name)
        require(hashlib.sha256(path.read_bytes()).hexdigest()==digest,'hash '+name)
        names.add(name)
    require({x.name for x in ROOT.iterdir()}==names|{'SHA256SUMS'},'complete inventory')
    require({'PROOF.md','certify.py','primitive.py','parameters.json','result.json'}<=names,'core inventory')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--check')
    args=ap.parse_args();require(args.emit != bool(args.check),'choose emit or check')
    if args.check:authenticate()
    result=reconstruct()
    text=json.dumps(result,sort_keys=True,separators=(',',':'))
    if args.check:
        old=load_json(args.check)
        require(json.dumps(old,sort_keys=True,separators=(',',':'))==text,'reconstructed result differs')
    print(text)

if __name__=='__main__':main()
