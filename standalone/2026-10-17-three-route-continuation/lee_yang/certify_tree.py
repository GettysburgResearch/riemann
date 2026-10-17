#!/usr/bin/env python3
"""Full-source replay and outward integer interval contraction for T16C.

The input is rational center data, never a purported moment/solver receipt.
The complete theta source is regenerated before the root is accepted.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
import theta_source as t
import pr886_primitive as b
from flexible_tree import tree,jet
from tree_core import UNIT,COUNTS
ROOT=Path(__file__).resolve().parent
I=b.I;SCALE=b.SCALE

def load(path):
    def pairs(items):
        out={}
        for k,v in items:
            b.require(k not in out,'duplicate JSON key');out[k]=v
        return out
    def no_float(x):raise ValueError('float not allowed in proof input')
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=no_float,parse_constant=no_float)

def reconstruct():
    b.require(hashlib.sha256((ROOT/'pr886_primitive.py').read_bytes()).hexdigest()==
      '2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','inherited primitive source identity')
    b.require(COUNTS==(256,10,1,1,1,1,1,1,1,1,1),'integer component multiplicities')
    p=load(ROOT/'tree_parameters.json')
    b.require(p['schema']=='T16C.parameters.v1','schema')
    active=p['active'];b.require(active==[0,1,2,3,4,5,6,8],'active coordinates')
    c=[F(x)for x in p['centers']];b.require(len(c)==17,'full model data')
    rad=F(p['radius']);b.require(rad==F(1,10**30),'fixed root box')
    box=[I(I.coerce(x-(rad if k in active else 0)).lo,I.coerce(x+(rad if k in active else 0)).hi)for k,x in enumerate(c)]
    b.require(all(x.lo>0 for x in box),'positive parameters')
    for prob in box[12:]:
        b.require(prob.lo>I.rat(1,2).hi and prob.hi<I.rat(5,8).lo,'strict ferromagnetic dimers')
    biases=[box[11]*(3 if k in (6,7)else F(1,100))*box[k]for k in range(11)]
    b.require(min(x.lo for x in biases)>I.rat(1,200000).hi,'positive hub edges with margin')
    b.require(max(x.hi for x in biases)<I.rat(1,30).lo,'bounded hub biases')
    # tanh J for every physical edge. atanh c >= c and atanh c <= c/(1-c^2).
    corr=biases+[2*x-1 for x in box[12:]]
    b.require(min(x.lo for x in corr)>I.rat(1,200000).hi,'all edge couplings lower bound')
    b.require(all((x/(1-x*x)).hi<I.rat(1,4).lo for x in corr),'all edge couplings upper bound')
    src=t.reconstruct()
    variance=I(*src['variance'])
    b.require(variance.lo>I.rat(1,25).hi and variance.hi<I.rat(1,20).lo,'physical theta variance')
    s=[I(*q)for q in src['standardized_cumulant_ratios']]
    center,J0,_=jet(c,active,16);R=b.inverse(J0)
    for i in range(8):
        for j in range(8):
            b.require(sum(R[i][k]*J0[k][j]for k in range(8))==F(i==j),'exact left inverse')
            b.require(sum(J0[i][k]*R[k][j]for k in range(8))==F(i==j),'exact right inverse')
    res=[I.coerce(center[i])-s[i]for i in range(8)]
    beta=max(b.absup(sum((R[i][k]*res[k]for k in range(8)),I.coerce(0)))for i in range(8))
    _,J,_=jet(box,active,16)
    L=max(sum(b.absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j]for k in range(8)),I.coerce(0)))for j in range(8))for i in range(8))
    b.require(F(L,SCALE)<F(1,1000),'contraction below .001')
    b.require(F(beta,SCALE)<rad/1000,'source residual displacement below radius/1000')
    margin=rad-F(beta,SCALE)-F(L,SCALE)*rad
    b.require(margin>rad*F(99,100),'whole-box strict invariance')
    vals,mu=tree(box,18);delta=UNIT[18]*(vals[8]-s[8])
    b.require(delta.lo>I.rat(34,1000).hi and delta.hi<I.rat(35,1000).lo,'unmatched moment18 interval')
    # Weighted covariance between the two large dimers, by conditional independence.
    covariance=box[12]*box[13]*box[6]*box[7]*biases[6]*biases[7]
    b.require(covariance.lo>I.rat(1,60000).hi,'nonzero correlated observable covariance')
    # Direct raw-moment enclosure is a separate check of the cumulant-to-moment transfer.
    source_raw18=I(*src['standardized_moments'][18])
    direct_delta=mu[18]-source_raw18
    b.require(direct_delta.lo>I.rat(34,1000).hi and direct_delta.hi<I.rat(35,1000).lo,'raw next-moment check')
    from controls import controls
    evidence=controls()
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()for name in
       ['pr886_primitive.py','theta_source.py','tree_core.py','flexible_tree.py','tree_parameters.json','certify_tree.py','controls.py']}
    return {'schema':'T16C.certificate.v1','status':'proposed-computer-assisted-component','rh_proved':False,
      'spins':281,'edges':280,'positive_edges':280,'matched_even_orders':list(range(2,17,2)),
      'active':active,'radius':str(rad),'beta_upper':str(F(beta,SCALE)),
      'contraction_upper':str(F(L,SCALE)),'invariance_margin':str(margin),
      'unmatched18_standardized':delta.record(),'direct_raw18_box':direct_delta.record(),
      'standardized_covariance_of_two_dimers':covariance.record(),
      'hub_biases':[x.record()for x in biases],'internal_correlations':[(2*x-1).record()for x in box[12:]],
      'complete_theta_source':src,'independent_finite_enumeration':evidence,'input_hashes':hashes}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path);ap.add_argument('--emit',type=Path);args=ap.parse_args()
    b.require(bool(args.check)!=bool(args.emit),'choose --check or --emit')
    result=reconstruct();text=json.dumps(result,sort_keys=True,separators=(',',':'))+'\n'
    if args.check:b.require(load(args.check)==result,'recomputed result differs')
    else:args.emit.write_text(text)
    print('T16C_FULL_SOURCE_CERTIFICATE_PASS',hashlib.sha256(text.encode()).hexdigest())
    print('beta',float(F(result['beta_upper'])),'L',float(F(result['contraction_upper'])))
    print('delta18',*[float(F(x,SCALE))for x in result['unmatched18_standardized']])

if __name__=='__main__':main()
