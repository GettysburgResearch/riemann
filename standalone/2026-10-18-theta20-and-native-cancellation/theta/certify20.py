"""Complete original-theta replay and directed contraction for degree20."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
import theta_source as source
import pr886_primitive as b
from connected_blocks import evaluate,jet,COUNTS,ETA
ROOT=Path(__file__).resolve().parent
I=b.I;SCALE=b.SCALE

def load(path):
    def pairs(items):
        out={}
        for k,v in items:
            b.require(k not in out,'duplicate JSON key');out[k]=v
        return out
    def no_float(x):raise ValueError('floating value in proof input')
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=no_float,parse_constant=no_float)

def reconstruct():
    b.require(hashlib.sha256((ROOT/'pr886_primitive.py').read_bytes()).hexdigest()=='2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','inherited primitive source identity')
    b.require(COUNTS==(256,10)+(1,)*14 and ETA==F(1,10**10),'full graph identities')
    p=load(ROOT/'parameters20.json');b.require(p['schema']=='T20D.parameters.v1','schema')
    active=p['active'];b.require(active==[6,0,15,21,3,27,9,12,4,42],'ten active coordinates')
    c=[F(x) for x in p['centers']];b.require(len(c)==48 and c[1]==0 and c[2]==1,'full model and collapsed single block')
    b.require(p['counts']==list(COUNTS) and F(p['hub_correlation'])==ETA,'multiplicities and hub')
    b.require(p['single_blocks']==[0] and p['dimer_blocks']==list(range(1,16)),'complete component types')
    radius=F(p['radius']);b.require(radius==F(1,10**30),'specified root cube')
    box=[I(I.coerce(x-(radius if j in active else 0)).lo,I.coerce(x+(radius if j in active else 0)).hi) for j,x in enumerate(c)]
    b.require(box[0].lo>0,'positive repeated fair-sign weight')
    weights=[box[0]];corr=[I.coerce(ETA)]
    for i in range(1,len(COUNTS)):
        A,B,pp=box[3*i:3*i+3]
        b.require(B.lo>0 and (A-B).lo>0,'two positive observable weights and orientation')
        b.require(pp.lo>I.rat(1,2).hi and pp.hi<SCALE,'strict finite ferromagnetic dimer')
        weights.extend([(A+B)/2,(A-B)/2]);corr.append(2*pp-1)
    b.require(all(q.lo>I.rat(1,10**11).hi and q.hi<I.rat(99,100).lo for q in corr),'edge correlations in(1e-11,.99)')
    # For q<.99, exp(6)>199 implies atanh(q)<3; a rational exp lower sum suffices.
    b.require(sum(F(6**j,b.factorial(j)) for j in range(7))>199,'elementary coupling upper bound')
    support=sum((COUNTS[i]*box[3*i] for i in range(len(COUNTS))),I.coerce(0))
    b.require(support.hi<I.coerce(11).lo,'observable support radius below11')
    print('T20D_RECONSTRUCT_COMPLETE_THETA_SOURCE',flush=True)
    src=source.reconstruct();target=[I(*x) for x in src['standardized_cumulant_ratios']]
    variance=I(*src['variance'])
    b.require(variance.lo>I.rat(1,25).hi and variance.hi<I.rat(1,20).lo,'original theta variance in(1/25,1/20)')
    b.require(len(target)==10 and len(src['standardized_moments'])==21,'all source orders0through20')
    print('T20D_EXACT_RATIONAL_CENTER_JACOBIAN',flush=True)
    value,J0,_=jet(c,active);R=b.inverse(J0)
    for i in range(10):
        for j in range(10):
            b.require(sum(R[i][k]*J0[k][j] for k in range(10))==F(i==j),'exact left inverse')
            b.require(sum(J0[i][k]*R[k][j] for k in range(10))==F(i==j),'exact right inverse')
    residual=[I.coerce(value[i])-target[i] for i in range(10)]
    beta=max(b.absup(sum((R[i][k]*residual[k] for k in range(10)),I.coerce(0))) for i in range(10))
    print('T20D_COMPLETE_BOX_JACOBIAN',flush=True)
    _,J,_=jet(box,active)
    L=max(sum(b.absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j] for k in range(10)),I.coerce(0))) for j in range(10)) for i in range(10))
    beta=F(beta,SCALE);L=F(L,SCALE);margin=radius-beta-L*radius
    b.require(L<F(1,1000),'strict contraction below.001')
    b.require(beta<radius/1000,'full-source center displacement below radius/1000')
    b.require(margin>F(99,100)*radius,'strict whole-cube invariance')
    # Direct interval moment overlap is diagnostic only; Banach proves equalities.
    _,raw=evaluate(box)
    b.require(all(raw[j].lo<=src['standardized_moments'][j][1] and raw[j].hi>=src['standardized_moments'][j][0] for j in range(21)),'all direct raw target intervals overlap')
    from check_connected import fixture
    small=fixture()
    names=['pr886_primitive.py','theta_source.py','tree_core.py','connected_blocks.py','parameters20.json','certify20.py','check_connected.py']
    return {'schema':'T20D.certificate.v1','status':'PROPOSED_COMPUTER_ASSISTED_FINITE_THEOREM','rh_proved':False,
      'vertices':305,'observed_vertices':304,'edges':304,'positive_edges':304,'zero_weight_hubs':1,
      'fair_signs':256,'dimers':24,'matched_even_orders':list(range(2,21,2)),'active':active,
      'radius':str(radius),'beta_upper':str(beta),'contraction_upper':str(L),'invariance_margin':str(margin),
      'support_radius_interval':support.record(),'edge_bias_types':[x.record() for x in corr],
      'complete_theta_source':src,'finite_enumeration':small,
      'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path);p.add_argument('--check',type=Path);a=p.parse_args()
    b.require(bool(a.emit)!=bool(a.check),'choose emit or check')
    out=reconstruct();txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    if a.check:b.require(load(a.check)==out,'recomputed certificate differs')
    print('T20D_FULL_SOURCE_CERTIFICATE_PASS',hashlib.sha256(txt.encode()).hexdigest(),flush=True)
    print('beta',float(F(out['beta_upper'])),'L',float(F(out['contraction_upper'])),flush=True)
