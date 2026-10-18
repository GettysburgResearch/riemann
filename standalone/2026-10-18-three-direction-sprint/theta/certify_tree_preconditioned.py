"""Fresh complete-source interval contraction for a hub-and-dimer tree.

This generic additional checker leaves the degree22 identity frozen.
A rational preconditioner is a finite witness; whole-box L<1 proves its
invertibility, so its equality to a computed center inverse is not assumed.
Every graph multiplicity, root coordinate, tail and positivity test is
reconstructed from finite exact data; no saved residual is trusted.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,argparse,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import source_extended,model
from certify_nonnegative_obstruction import load
I=b.I;SCALE=b.SCALE

def certify(parameters):
    b.require(hashlib.sha256((ROOT/'inherited/pr886_primitive.py').read_bytes()).hexdigest()=='2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','pinned outward primitive identity')
    p=load(parameters);degree=p['degree'];n=degree//2;counts=p['counts'];active=p['active'];c=list(map(F,p['centers']));eta=F(p['hub_correlation']);radius=F(p['radius'])
    b.require(p['schema']=='TS.tree.parameters.v1' and type(degree)is int and 2<=degree<=32 and degree%2==0,'finite generic even-degree tree schema')
    b.require(len(counts)>=2 and len(c)==3*len(counts) and all(type(x)is int and x>0 for x in counts),'complete positive integer multiplicities')
    b.require(len(active)==n and len(set(active))==n and all(type(j)is int and 0<=j<len(c) and j not in(1,2) for j in active),'complete distinct square chart')
    b.require(c[1]==0 and c[2]==1,'honest repeated fair-sign block')
    b.require(eta==F(1,10**10) and 0<radius<=F(1,10**20),'positive fixed hub and small rational cube')
    box=[I(I.coerce(x-(radius if j in active else 0)).lo,I.coerce(x+(radius if j in active else 0)).hi) for j,x in enumerate(c)]
    b.require(box[0].lo>0,'positive repeated fair weight')
    bias=[I.coerce(eta)]
    for i in range(1,len(counts)):
        A,B,p0=box[3*i:3*i+3]
        b.require((A+B).lo>0 and (A-B).lo>0,'both physical dimer weights positive on full cube')
        b.require(p0.lo>I.rat(1,2).hi and p0.hi<SCALE,'all internal dimer interactions positive and finite')
        bias.append(2*p0-1)
    b.require(all(q.lo>I.rat(1,10**11).hi and q.hi<I.rat(999999999,10**9).lo for q in bias),'all edge biases strictly bounded inside(0,1)')
    support=sum((counts[i]*box[3*i] for i in range(len(counts))),I.coerce(0));b.require(support.hi<I.coerce(12).lo,'complete support below12')
    print('TS_TREE_FRESH_COMPLETE_THETA_SOURCE',degree,flush=True);src=source_extended.reconstruct(degree)
    target=[I(*x) for x in src['standardized_cumulant_ratios']]
    b.require(len(target)==n and len(src['standardized_moments'])==degree+1,'all full source moment orders present')
    print('TS_TREE_RATIONAL_PRECONDITIONER',flush=True)
    R=[[F(v) for v in row] for row in p['rational_preconditioner']]
    b.require(len(R)==n and all(len(row)==n for row in R),'complete square rational preconditioner witness')
    value,_=model.evaluate([I.coerce(v) for v in c],counts,eta,degree)
    residual=[I.coerce(value[i])-target[i] for i in range(n)]
    beta=F(max(b.absup(sum((R[i][k]*residual[k] for k in range(n)),I.coerce(0))) for i in range(n)),SCALE)
    print('TS_TREE_WHOLE_BOX_JACOBIAN',flush=True);_,J,_=model.jet(box,counts,eta,degree,active)
    L=F(max(sum(b.absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j] for k in range(n)),I.coerce(0))) for j in range(n)) for i in range(n)),SCALE)
    margin=radius-beta-L*radius
    print('TS_TREE_BOUNDS','beta',float(beta),'L',float(L),flush=True)
    b.require(L<F(1,1000),'strict whole-cube contraction below.001')
    b.require(beta<radius/1000,'fresh complete-source displacement below radius/1000')
    b.require(margin>F(99,100)*radius,'strict cube invariance margin')
    _,raw=model.evaluate(box,counts,eta,degree)
    b.require(all(raw[j].lo<=src['standardized_moments'][j][1] and raw[j].hi>=src['standardized_moments'][j][0] for j in range(degree+1)),'all raw source boxes overlap diagnostically')
    observed=counts[0]+2*sum(counts[1:]);edges=sum(counts)+sum(counts[1:])
    b.require(edges==observed,'complete tree edge count')
    names=['model.py','source_extended.py','certify_tree_preconditioned.py','certify_nonnegative_obstruction.py','inherited/pr886_primitive.py']
    return {'schema':'TS.tree.preconditioned-certificate.v1','status':'PROPOSED_COMPUTER_ASSISTED_FINITE_THEOREM','rh_proved':False,
        'degree':degree,'matched_even_orders':list(range(2,degree+1,2)),'vertices':observed+1,'observed_vertices':observed,'edges':edges,'positive_edges':edges,
        'counts':counts,'active':active,'hub_correlation':str(eta),'radius':str(radius),'beta_upper':str(beta),'contraction_upper':str(L),'invariance_margin':str(margin),
        'support_interval':support.record(),'edge_bias_types':[q.record() for q in bias],'complete_theta_source':src,
        'parameters':p,'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names},'parameter_sha256':hashlib.sha256(parameters.read_bytes()).hexdigest()}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parameters',type=Path,required=True);p.add_argument('--emit',type=Path);p.add_argument('--check',type=Path);a=p.parse_args();b.require(bool(a.emit)!=bool(a.check),'choose emit or check')
    start=time.time();out=certify(a.parameters);txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    if a.check:b.require(load(a.check)==out,'fresh complete tree certificate equality')
    print('TS_TREE_CERTIFICATE_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)
