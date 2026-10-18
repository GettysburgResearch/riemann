"""Independent exhaustive tree-merge moment and derivative controls."""
from pathlib import Path
from fractions import Fraction as F
import argparse,itertools,json,hashlib,time
import model,merge_model as mm
ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:raise ValueError(message)

def enumerate_graph(z,counts,selected,ends,eta,degree,active):
    weights=[F(0)];dw=[{}];components=[];edges=[]
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        for copy in range(count):
            root=len(weights)
            if i==0:
                weights.append(A);dw.append({0:F(1)});components.append((i,root,None))
            else:
                weights.extend([(A+B)/2,(A-B)/2]);dw.extend([{3*i:F(1,2),3*i+1:F(1,2)},{3*i:F(1,2),3*i+1:F(-1,2)}]);components.append((i,root,root+1));edges.append((root,root+1,2*p-1,{3*i+2:F(2)}))
    left=next(c for c in components if c[0]==selected[0]);right=next(c for c in components if c[0]==selected[1] and c is not left)
    for item in components:
        if item is not right:edges.append((0,item[1],eta,{}))
    endpoints=[left[1+ends[0]],right[1+ends[1]]];require(None not in endpoints,'legal root/leaf endpoints')
    edges.append((*endpoints,z[-1],{len(z)-1:F(1)}));vertices=len(weights)
    raw=[F(0)]*(degree+1);deriv=[[F(0)]*len(active) for _ in raw];mass=F(0)
    for spins in itertools.product((-1,1),repeat=vertices):
        factors=[1+q*spins[a]*spins[b] for a,b,q,d in edges];prob=F(1,2**vertices)
        for f in factors:prob*=f
        mass+=prob;value=sum(w*s for w,s in zip(weights,spins))
        dvalue={k:sum(v.get(k,0)*s for v,s in zip(dw,spins)) for k in active}
        dprob={k:sum((prob*dd.get(k,0)*spins[a]*spins[b]/f for (a,b,q,dd),f in zip(edges,factors)),F(0)) for k in active}
        for n in range(degree+1):
            raw[n]+=prob*value**n
            for j,k in enumerate(active):deriv[n][j]+=dprob[k]*value**n+(n*prob*value**(n-1)*dvalue[k] if n else 0)
    require(mass==1,'exhaustive merged-tree normalization')
    return raw,deriv,vertices

def fixture(same=False,degree=26):
    if same:
        z=[F(3,7),F(0),F(1),F(7,9),F(-1,5),F(4,5),F(2,7)];counts=[1,2];selected=(1,1)
    else:
        z=[F(3,7),F(0),F(1),F(7,9),F(-1,5),F(4,5),F(5,8),F(1,8),F(3,5),F(2,7)];counts=[1,1,1];selected=(1,2)
    active=[j for j in range(len(z)) if j not in(1,2)];eta=F(1,11);tests=0
    for ends in itertools.product((0,1),repeat=2):
        raw,derivative,vertices=enumerate_graph(z,counts,selected,ends,eta,degree,active)
        zz=[model.Dual(v,[F(j==k) for k in active]) for j,v in enumerate(z)];_,got=mm.evaluate(zz,counts,selected,ends,eta,degree)
        require([v.v for v in got]==raw,'all exhaustive raw moments versus merged conditional cumulants')
        require([list(v.d) for v in got]==derivative,'all explicit graph derivatives versus complete AD')
        require(mm.direct_assembly(z,counts,selected,ends,eta,degree)==raw,'independent direct raw EGF assembly')
        require(mm.evaluate(z,counts,selected,ends,F(0),degree)[1]!=raw,'hub is load-bearing')
        tests+=1
    return {'same_type_copies':same,'endpoint_choices':tests,'vertices':vertices,'configurations_per_choice':2**vertices,'raw_orders':degree+1,'derivative_coordinates':len(active)}

def main(parameters=None,emit=None):
    start=time.time();fixtures=[fixture(False),fixture(True)];out={'status':'MERGE_CONTROLS_PASS','fixtures':fixtures}
    if parameters:
        p=json.loads(parameters.read_text());z=list(map(F,p['centers']));eta=F(p['hub_correlation']);degree=p['degree'];selected=tuple(p['merge_types']);ends=tuple(p['merge_ends'])
        raw=mm.evaluate(z,p['counts'],selected,ends,eta,degree)[1];require(raw==mm.direct_assembly(z,p['counts'],selected,ends,eta,degree),'all complete finite model moments via raw EGF')
        out['complete_model_degree']=degree;out['parameter_sha256']=hashlib.sha256(parameters.read_bytes()).hexdigest()
    out['input_hashes']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['model.py','merge_model.py','merge_controls.py']}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if emit:emit.write_text(txt)
    print('MERGE_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parameters',type=Path);p.add_argument('--emit',type=Path,default=ROOT/'merge_controls.json');a=p.parse_args();main(a.parameters,a.emit)
