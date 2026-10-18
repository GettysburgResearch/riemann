"""Fresh complete-source rational/interval contraction for the degree22 model.

Saved targets, solver residuals and old certificates are not acceptance inputs.
The only primitive is the exact pinned outward-integer backend from #994.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,argparse,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import source_extended,model
I=b.I;SCALE=b.SCALE

def load(path):
    def pairs(items):
        out={}
        for k,v in items:
            b.require(k not in out,'duplicate JSON key');out[k]=v
        return out
    def no_float(x):raise ValueError('floating or nonfinite input in proof data')
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=no_float,parse_constant=no_float)

def certify(parameters=None):
    b.require(hashlib.sha256((ROOT/'inherited/pr886_primitive.py').read_bytes()).hexdigest()=='2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','pinned outward primitive identity')
    p=load(parameters or ROOT/'parameters22.json');degree=p['degree'];n=degree//2;counts=p['counts'];active=p['active'];c=list(map(F,p['centers']));eta=F(p['hub_correlation']);radius=F(p['radius'])
    b.require(p['schema']=='T22S.parameters.v1' and degree==22,'exact degree22 schema')
    b.require(counts==[256,10]+[1]*15 and len(c)==51,'complete17component multiplicity list')
    b.require(active==[6,0,15,21,3,27,48,9,12,5,42],'exact eleven-coordinate chart')
    b.require(len(set(active))==n and c[1]==0 and c[2]==1,'complete active chart and single block')
    b.require(eta==F(1,10**10) and radius==F(1,10**30),'exact hub and cube')
    box=[I(I.coerce(x-(radius if j in active else 0)).lo,I.coerce(x+(radius if j in active else 0)).hi) for j,x in enumerate(c)]
    b.require(box[0].lo>0,'positive repeated fair-spin weight')
    bias=[I.coerce(eta)];weights=[box[0]]
    for i in range(1,len(counts)):
        A,B,p0=box[3*i:3*i+3]
        b.require((A+B).lo>0 and (A-B).lo>0,'both dimer observable weights positive on full cube')
        b.require(p0.lo>I.rat(1,2).hi and p0.hi<SCALE,'strict finite positive dimer coupling on full cube')
        weights.extend([(A+B)/2,(A-B)/2]);bias.append(2*p0-1)
    b.require(all(q.lo>I.rat(1,10**11).hi and q.hi<I.rat(999999999,10**9).lo for q in bias),'all positive edge biases bounded below1')
    support=sum((counts[i]*box[3*i] for i in range(len(counts))),I.coerce(0))
    b.require(support.hi<I.coerce(12).lo,'complete observable support below12')
    print('T22S_FRESH_COMPLETE_THETA_SOURCE',flush=True);src=source_extended.reconstruct(degree)
    target=[I(*x) for x in src['standardized_cumulant_ratios']]
    b.require(len(target)==n and len(src['standardized_moments'])==degree+1,'all original theta source orders0through22')
    variance=I(*src['variance']);b.require(variance.lo>I.rat(1,25).hi and variance.hi<I.rat(1,20).lo,'theta variance enclosure')
    print('T22S_EXACT_RATIONAL_JACOBIAN',flush=True);value,J0,_=model.jet(c,counts,eta,degree,active);R=b.inverse(J0)
    for i in range(n):
        for j in range(n):
            b.require(sum(R[i][k]*J0[k][j] for k in range(n))==F(i==j),'exact left inverse')
            b.require(sum(J0[i][k]*R[k][j] for k in range(n))==F(i==j),'exact right inverse')
    residual=[I.coerce(value[i])-target[i] for i in range(n)]
    beta=F(max(b.absup(sum((R[i][k]*residual[k] for k in range(n)),I.coerce(0))) for i in range(n)),SCALE)
    print('T22S_WHOLE_BOX_JACOBIAN',flush=True);_,J,_=model.jet(box,counts,eta,degree,active)
    L=F(max(sum(b.absup(I.coerce(int(i==j))-sum((R[i][k]*J[k][j] for k in range(n)),I.coerce(0))) for j in range(n)) for i in range(n)),SCALE)
    margin=radius-beta-L*radius
    b.require(L<F(1,1000),'strict whole-cube contraction below.001')
    b.require(beta<radius/1000,'fresh full-source center displacement below radius/1000')
    b.require(margin>F(99,100)*radius,'strict cube invariance margin')
    _,raw=model.evaluate(box,counts,eta,degree)
    b.require(all(raw[j].lo<=src['standardized_moments'][j][1] and raw[j].hi>=src['standardized_moments'][j][0] for j in range(degree+1)),'all raw target boxes overlap diagnostically')
    names=['model.py','source_extended.py','certify.py','parameters22.json','inherited/pr886_primitive.py']
    return {'schema':'T22S.certificate.v1','status':'PROPOSED_COMPUTER_ASSISTED_FINITE_THEOREM','rh_proved':False,
        'degree':degree,'matched_even_orders':list(range(2,degree+1,2)),'vertices':307,'observed_vertices':306,'edges':306,'positive_edges':306,
        'counts':counts,'active':active,'hub_correlation':str(eta),'radius':str(radius),'beta_upper':str(beta),'contraction_upper':str(L),'invariance_margin':str(margin),
        'support_interval':support.record(),'edge_bias_types':[q.record() for q in bias],'complete_theta_source':src,
        'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--emit',type=Path);parser.add_argument('--check',type=Path);a=parser.parse_args();b.require(bool(a.emit)!=bool(a.check),'choose emit or check')
    start=time.time();out=certify();txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    if a.check:b.require(load(a.check)==out,'fresh certificate equality')
    print('T22S_CERTIFICATE_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,'beta',float(F(out['beta_upper'])),'L',float(F(out['contraction_upper'])),flush=True)
