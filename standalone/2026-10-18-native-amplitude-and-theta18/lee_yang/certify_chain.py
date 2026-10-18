#!/usr/bin/env python3
"""Full original-theta replay and directed rational contraction for T18C."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse,time
import theta_source as t
import pr886_primitive as b
from chain_exact import evaluate,jet,COUNTS,ETA
from tree_core import UNIT
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
    b.require(COUNTS==(256,10)and ETA==F(1,1000),'fixed leaf counts and hub correlation')
    p=load(ROOT/'chain_parameters.json');b.require(p['schema']=='T18C.parameters.v1','schema')
    active=p['active'];b.require(active==[2,13,0,10,1,11,5,3,7],'active coordinates')
    c=[F(x)for x in p['centers']];b.require(len(c)==29,'full model data')
    b.require(p['counts']==[256,10]and p['core_vertices']==14,'full connected graph')
    b.require(F(p['hub_core_correlation'])==ETA and F(p['weak_core_correlation'])==F(1,10**8),'edge identities')
    b.require(c[17:]==[F(1,10**8)]*12,'twelve exact weak core edges')
    rad=F(p['radius']);b.require(rad==F(1,10**30),'fixed root box')
    box=[I(I.coerce(x-(rad if k in active else 0)).lo,I.coerce(x+(rad if k in active else 0)).hi)for k,x in enumerate(c)]
    b.require(all(x.lo>0 for x in box),'strictly positive parameters')
    b.require(all(x.hi<I.coerce(1).lo for x in box[:16]),'observable weights below one')
    corr=[box[0]/1000,box[1]/1000,I.coerce(ETA)]+box[16:]
    b.require(all(x.lo>I.rat(1,10**9).hi and x.hi<I.coerce(1).lo for x in corr),'every edge correlation strictly between0and1')
    b.require(all((x/(1-x*x)).hi<I.rat(1,4).lo for x in corr),'all finite edge couplings below1/4')
    # Every actual q= tanh(J) is positive; q<J<=q/(1-q^2).
    print('T18C_RECONSTRUCT_SOURCE',flush=True)
    src=t.reconstruct();variance=I(*src['variance'])
    b.require(variance.lo>I.rat(1,25).hi and variance.hi<I.rat(1,20).lo,'original theta variance')
    s=[I(*q)for q in src['standardized_cumulant_ratios']]
    print('T18C_EXACT_CENTER_JACOBIAN',flush=True)
    center,J0,_=jet(c,active,18);R=b.inverse(J0)
    for i in range(9):
        for j in range(9):
            b.require(sum(R[i][k]*J0[k][j]for k in range(9))==F(i==j),'exact left inverse')
            b.require(sum(J0[i][k]*R[k][j]for k in range(9))==F(i==j),'exact right inverse')
    res=[I.coerce(center[i])-s[i]for i in range(9)]
    beta=max(b.absup(sum((R[i][k]*res[k]for k in range(9)),I.coerce(0)))for i in range(9))
    print('T18C_WHOLE_BOX_JACOBIAN',flush=True)
    _,J,_=jet(box,active,18)
    L=max(sum(b.absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j]for k in range(9)),I.coerce(0)))for j in range(9))for i in range(9))
    b.require(F(L,SCALE)<F(1,1000),'contraction below.001')
    b.require(F(beta,SCALE)<rad/1000,'full-source displacement below radius/1000')
    margin=rad-F(beta,SCALE)-F(L,SCALE)*rad
    b.require(margin>rad*F(99,100),'whole-box strict invariance')
    vals,mu=evaluate(box,20);delta=UNIT[20]*(vals[9]-s[9])
    b.require(delta.lo>I.rat(45,100).hi and delta.hi<I.rat(451,1000).lo,'strict unmatched cumulant20 interval')
    direct_delta=mu[20]-I(*src['standardized_moments'][20])
    b.require(direct_delta.lo>I.rat(45,100).hi and direct_delta.hi<I.rat(451,1000).lo,'strict direct raw20 interval')
    covariance=box[2]*box[3]*box[16]
    b.require(covariance.lo>I.rat(1,60).hi and covariance.hi<I.rat(17,1000).lo,'substantial first-pair covariance')
    support=256*box[0]+10*box[1]+sum(box[2:16],I.coerce(0))
    b.require(support.hi<I.coerce(10).lo,'bounded observable support')
    from chain_controls import controls
    evidence=controls()
    names=['pr886_primitive.py','theta_source.py','tree_core.py','chain_exact.py','chain_parameters.json','certify_chain.py','chain_controls.py']
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()for name in names}
    return {'schema':'T18C.certificate.v1','status':'proposed-computer-assisted-component','rh_proved':False,
      'spins':281,'edges':280,'positive_edges':280,'core_vertices':14,'leaf_counts':[256,10],
      'matched_even_orders':list(range(2,19,2)),'active':active,'radius':str(rad),
      'beta_upper':str(F(beta,SCALE)),'contraction_upper':str(F(L,SCALE)),'invariance_margin':str(margin),
      'unmatched20_standardized':delta.record(),'direct_raw20_box':direct_delta.record(),
      'standardized_first_pair_covariance':covariance.record(),'support_radius':support.record(),
      'edge_correlation_types':[x.record()for x in corr],
      'complete_theta_source':src,'independent_finite_enumeration':evidence,'input_hashes':hashes}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path);ap.add_argument('--emit',type=Path);args=ap.parse_args()
    b.require(bool(args.check)!=bool(args.emit),'choose --check or --emit')
    result=reconstruct();text=json.dumps(result,sort_keys=True,separators=(',',':'))+'\n'
    if args.check:b.require(load(args.check)==result,'recomputed result differs')
    else:args.emit.write_text(text)
    print('T18C_FULL_SOURCE_CERTIFICATE_PASS',hashlib.sha256(text.encode()).hexdigest())
    print('beta',float(F(result['beta_upper'])),'L',float(F(result['contraction_upper'])))
    print('delta20',*[float(F(x,SCALE))for x in result['unmatched20_standardized']])

if __name__=='__main__':main()
